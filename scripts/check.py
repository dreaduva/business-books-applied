#!/usr/bin/env python3
"""Check catalog integrity, internal navigation, publication metadata, and generated content."""
import json
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

from render_headers import safe_url

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
research = json.loads((ROOT / "catalog/keywords.json").read_text())
covers = json.loads((ROOT / "config/covers.json").read_text())
affiliate = json.loads((ROOT / "config/affiliate-links.json").read_text())
check(len(books) == 100, "Catalog must preserve exactly 100 books.")
check(len({b["id"] for b in books}) == 100, "Duplicate catalog ID.")
check(len({b["slug"] for b in books}) == 100, "Duplicate book slug; disambiguate identical titles.")
ids = {b["id"] for b in books}
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
    check(book["status"] in {"planned", "draft", "published"}, f"Invalid status: {book['slug']}")
    path = book.get("guide_path")
    if book["status"] != "planned":
        check(bool(path) and (ROOT / path).is_file(), f"Missing guide: {book['slug']}")
    if book["status"] == "published":
        check(bool(book["review"]["human_reviewer"]) and bool(book["review"]["reviewed_on"]), f"Published guide lacks human review: {book['slug']}")
        check(covers.get(book["slug"], {}).get("status") == "approved", f"Published guide lacks approved cover: {book['slug']}")

for slug, url in affiliate["links"].items():
    check(slug in {b["slug"] for b in books}, f"Unknown affiliate book: {slug}")
    try:
        safe_url(url, amazon=True)
    except ValueError as exc:
        errors.append(f"{slug}: {exc}")
if affiliate["enabled"]:
    check(all(affiliate.get(k) for k in ["marketplace", "site_registered", "account_confirmed"]), "Affiliate account confirmation incomplete.")

markdown = list(ROOT.rglob("*.md"))
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
print(f"PASS: {len(books)} books, {len(research['queries'])} keyword rows, {len(markdown)} Markdown files; links, metadata, and generated content checked.")
