#!/usr/bin/env python3
"""Generate navigation and editorial briefs from the catalog; never generate prose guides."""
import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATEGORIES = [
    "Startups and discovery", "Strategy and business models", "Product and innovation",
    "Marketing and growth", "Sales and communication", "Money and operations",
    "Leadership and teams", "Productivity and execution", "Founder stories and judgment",
]


def cell(value):
    return str(value).replace("|", "\\|").replace("\n", " ")


def outputs():
    books = json.loads((ROOT / "catalog/books.json").read_text())
    research = json.loads((ROOT / "catalog/keywords.json").read_text())
    lines = ["# 100 Business Books: Summaries and Practical Guides", "",
             "[Home](../README.md) · [Playbooks](../playbooks/README.md) · [AI skills](../skills/README.md)", "",
             "A curated catalog of 100 titles. **Published** means the guide and resources are available with a source-check and editorial note; **draft** means still being developed; **planned** means no guide exists yet. Publication does not imply human expert review. This is not an all-time sales ranking. [How books are selected](../docs/book-selection.md).", "",
             " · ".join(f"[{c}](#{c.lower().replace(' ', '-')})" for c in CATEGORIES), ""]
    for category in CATEGORIES:
        lines += [f"## {category}", "", "| Book and author | Practical resource | Guide |", "| --- | --- | --- |"]
        for book in sorted((b for b in books if b["category"] == category), key=lambda b: b["title"].casefold()):
            title = cell(book["title"])
            status = "Planned"
            if book["guide_path"]:
                link = book["guide_path"].removeprefix("books/")
                title = f"[{title}]({link})"
                status = f"[{book['status'].capitalize()}]({link})"
            lines.append(f"| {title}<br>{cell(book['author'])} | {cell(book['application_resource'])} | {status} |")
        lines += [""]
    lines += ["Original catalog IDs and research evidence are preserved in [books.json](../catalog/books.json). To suggest a correction, read [CONTRIBUTING.md](../CONTRIBUTING.md).", ""]

    briefs = ["# Editorial Keyword Briefs for 100 Business Books", "",
              "Generated from the existing research, not a fresh Google ranking audit. US monthly estimates are provider estimates; unknown values stay unknown. Query suggestions and application ideas are hypotheses until the search intent and sources have been checked. [Method and limitations](seo-strategy.md).", "",
              "These briefs plan future guides. They are not 100 published articles and do not prescribe one AI skill per book.", ""]
    for book in books:
        rows = [q for q in research["queries"] if q["id"] == book["id"]]
        measured = [q for q in rows if q["volume"] is not None]
        # Prefer exact proposed intents, then other direct evidence, then related suggestions.
        measured.sort(key=lambda q: (q["keyword"] not in [book["primary_query"], book["application_query"]], q["kind"] != "Direct query", -q["volume"]))
        briefs += [f"## {book['id']}. {book['title']} — {book['author']}", "",
                   f"- Proposed heading: **{book['proposed_heading']}**",
                   f"- Intended guide: `{book['proposed_guide_path']}`",
                   f"- Primary query: `{book['primary_query']}` — " + (f"{book['primary_query_estimate']:,}/month, provider estimate." if book['primary_query_estimate'] is not None else "volume unverified."),
                   f"- Application query: `{book['application_query']}` — " + (f"{book['application_query_estimate']:,}/month, provider estimate; inspect the evidence kind below." if book['application_query_estimate'] is not None else "volume unverified."),
                   f"- Original resource to develop: {book['application_resource']}.",
                   f"- Possible complementary comparison: {book['comparison_candidate']}. Validate intent before creating a separate page.",
                   "- Before drafting: check the current Google results in the target market; verify edition, sources, popularity evidence, and cover rights.", ""]
        if measured:
            briefs += ["| Observed query | US monthly estimate | Evidence kind | Retrieved | Source |", "| --- | ---: | --- | --- | --- |"]
            for q in measured[:5]:
                briefs.append(f"| {cell(q['keyword'])} | {q['volume']:,} | {q['kind']} | {q['retrieved']} | [Provider response]({q['url']}) |")
            briefs += [""]
        else:
            briefs += ["No numerical estimate is available for this book in the current dataset. Do not infer low demand or assign an invented difficulty score.", ""]
    return {ROOT / "books/README.md": "\n".join(lines), ROOT / "docs/keyword-briefs.md": "\n".join(briefs)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    stale = []
    for path, content in outputs().items():
        if args.check:
            if not path.exists() or path.read_text() != content:
                stale.append(str(path.relative_to(ROOT)))
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content)
    if stale:
        raise SystemExit("Regenerate catalog files: " + ", ".join(stale))
    print("Catalog and keyword briefs are current." if args.check else "Generated catalog and 100 editorial briefs.")


if __name__ == "__main__":
    main()
