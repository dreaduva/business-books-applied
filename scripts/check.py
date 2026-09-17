#!/usr/bin/env python3
"""Check catalog integrity, internal navigation, publication metadata, and generated content."""
import argparse
import json
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

from render_headers import safe_url
from build_catalog import CATEGORIES

ROOT = Path(__file__).resolve().parents[1]
errors = []


def check(condition, message):
    if not condition:
        errors.append(message)


def anchors(text):
    result, used = set(), {}
    for heading in re.findall(r"^#{1,6}\s+(.+)$", text, flags=re.M):
        clean = re.sub(r"[^\w\- ]", "", heading.lower()).replace(" ", "-")
        n = used.get(clean, 0)
        result.add(clean + (f"-{n}" if n else ""))
        used[clean] = n + 1
    result.update(re.findall(r'\bid="([^"]+)"', text))
    return result


books = json.loads((ROOT / "catalog/books.json").read_text())
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--research", action="store_true", help="Also validate ignored local keyword evidence")
args = parser.parse_args()
research = json.loads((ROOT / "private/catalog/keywords.json").read_text()) if args.research else None
covers = json.loads((ROOT / "config/covers.json").read_text())
affiliate = json.loads((ROOT / "config/affiliate-links.json").read_text())
check(set(range(1, 101)).issubset({b["id"] for b in books}), "Preserve the original 100 catalog IDs.")
check(len({b["id"] for b in books}) == len(books), "Duplicate catalog ID.")
check(len({b["slug"] for b in books}) == len(books), "Duplicate book slug; disambiguate identical titles.")
ids = {b["id"] for b in books}
if research is not None:
    for q in research["queries"]:
        check(q["id"] in ids, f"Unknown keyword book ID: {q['id']}")
        if q["volume"] is not None:
            check(isinstance(q["volume"], (int, float)) and q["volume"] >= 0, "Invalid search estimate.")
            check(q["status"] == "Provider estimate" and bool(q["url"]), "Numerical estimate lacks provenance.")
    measured = [q for q in research["queries"] if q["volume"] is not None]
    check(len(measured) == research["stats"]["measured"], "Research measured-row count is stale.")
    check(len(research["queries"]) == research["stats"]["keywords"], "Research keyword count is stale.")
    check(len({q["id"] for q in measured}) == research["stats"]["booksWithEstimates"], "Research book coverage count is stale.")

for book in books:
    check(book["category"] in CATEGORIES, f"Unknown category: {book['slug']}")
    check(re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", book["slug"]), "Unsafe book slug")
    check(not any(k in book for k in ["primary_query", "primary_query_estimate", "application_query", "source_keyword"]), "Private SEO fields in public catalog")
    for label, resource in book.get("resources", {}).items():
        target = (ROOT / resource).resolve()
        check(target.is_relative_to(ROOT) and target.is_file(), f"Missing or unsafe resource: {resource}")
    if book.get("guide_path"):
        check(book["guide_path"] == f"books/{book['slug']}/README.md", "Guide must have its canonical book home")
    check(book["status"] in {"planned", "draft", "published"}, f"Invalid status: {book['slug']}")
    path = book.get("guide_path")
    if book["status"] != "planned":
        check(bool(path) and (ROOT / path).is_file(), f"Missing guide: {book['slug']}")
    if book["status"] == "published":
        check(bool(book["review"].get("source_checked_on")) and bool(book["review"].get("source_scope")), f"Published guide lacks source-check metadata: {book['slug']}")
        check(isinstance(book["review"].get("ai_assisted"), bool), f"Published guide lacks authorship disclosure: {book['slug']}")
        check(bool(book["review"].get("human_reviewer")) == bool(book["review"].get("reviewed_on")), f"Human reviewer and review date must be recorded together: {book['slug']}")
        check(covers.get(book["slug"], {}).get("status") in {"approved", "service-embed"}, f"Published guide lacks documented cover display basis: {book['slug']}")

for slug, url in affiliate["links"].items():
    check(slug in {b["slug"] for b in books}, f"Unknown affiliate book: {slug}")
    try:
        safe_url(url, amazon=True)
    except ValueError as exc:
        errors.append(f"{slug}: {exc}")
if affiliate["enabled"]:
    check(all(affiliate.get(k) for k in ["marketplace", "site_registered", "account_confirmed"]), "Affiliate account confirmation incomplete.")

markdown = [p for p in ROOT.rglob("*.md") if not set(p.relative_to(ROOT).parts) & {"private", ".git", "node_modules", ".venv"}]
for path in markdown:
    text = path.read_text()
    # Ignore code blocks when checking navigable links and heading anchors.
    body = re.sub(r"```.*?```", "", text, flags=re.S)
    check(len(re.findall(r"^# ", body, re.M)) == 1, f"Expected one H1: {path.relative_to(ROOT)}")
    for label, url in re.findall(r"\[([^\]]+)\]\(([^\s)]+)\)", body):
        parsed = urlsplit(url)
        if parsed.scheme or parsed.netloc:
            continue
        target = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path
        check("private" not in target.relative_to(ROOT).parts if target.is_relative_to(ROOT) else False, f"Public link targets private material: {url}")
        check(target.is_relative_to(ROOT), f"Link escapes repository: {path.relative_to(ROOT)} → {url}")
        check(target.is_file(), f"Broken or directory-only link: {path.relative_to(ROOT)} → {url}")
        if parsed.fragment and target.is_file() and target.suffix == ".md":
            target_body = re.sub(r"```.*?```", "", target.read_text(), flags=re.S)
            check(unquote(parsed.fragment) in anchors(target_body), f"Broken anchor: {path.relative_to(ROOT)} → {url}")

for path in ROOT.glob("skills/*/SKILL.md"):
    text = path.read_text()
    check(text.startswith("---\n"), f"Missing skill frontmatter: {path}")
    check(f"name: {path.parent.name}\n" in text, f"Skill name mismatch: {path}")
    check("description: " in text.split("---", 2)[1], f"Missing skill description: {path}")
    check("amzn.to/" not in text and "?tag=" not in text, f"Affiliate link in skill: {path}")

for script in ["build_catalog.py", "render_headers.py"]:
    result = subprocess.run([sys.executable, str(ROOT / "scripts" / script), "--check"], capture_output=True, text=True)
    if result.returncode:
        errors.append(result.stdout + result.stderr)

if errors:
    print("\n".join("ERROR: " + e for e in errors))
    raise SystemExit(1)
print(f"PASS: {len(books)} books, {len(markdown)} public Markdown files; links, metadata, and generated content checked.")
if research is not None:
    print(f"Private research: {len(research['queries'])} keyword rows validated.")
