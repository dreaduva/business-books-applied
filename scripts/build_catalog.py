#!/usr/bin/env python3
"""Build public navigation from reader-facing metadata; no private research required."""
import argparse
import json
import os
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATEGORIES = [
    "Startups and discovery", "Strategy and business models", "Product and innovation",
    "Marketing and growth", "Sales and communication", "Money and operations",
    "Leadership and teams", "Productivity and execution", "Founder stories and judgment",
]
START, END = '<!-- LIBRARY:START -->', '<!-- LIBRARY:END -->'


def slug(category):
    return category.lower().replace(' ', '-')


def cell(value):
    return str(value).replace('|', '\\|').replace('\n', ' ')


def link(path, base):
    return os.path.relpath(ROOT / path, ROOT / base)


def row(book, base):
    title = f"[{cell(book['title'])}]({link(book['guide_path'], base)})<br>{cell(book['author'])}"
    resources = ' · '.join(f"[{label}]({link(path, base)})" for label, path in book['resources'].items()) or 'Guide'
    return f"| {title} | {cell(book['application_resource'])} | {resources} |"


def table(books, base):
    return ['| Book and author | Put an idea to work | Resources |', '| --- | --- | --- |'] + [row(b, base) for b in sorted(books, key=lambda b: (b['title'].casefold(), b['author']))]


def outputs():
    books = json.loads((ROOT / 'catalog/books.json').read_text())
    published = [b for b in books if b['status'] == 'published']
    planned = [b for b in books if b['status'] != 'published']
    categories = [c for c in CATEGORIES if any(b['category'] == c for b in published)]
    result = {}
    lines = [START, f"**{len(published)} published {'guide' if len(published)==1 else 'guides'} · {len(planned)} titles in the planned collection.** Every resource below is available now.", '',
             '[A–Z book index](books/README.md) · [Browse topics](topics/README.md) · [Planned collection](books/roadmap.md)', '']
    for c in categories:
        group = [b for b in published if b['category'] == c]
        lines += ['<details open>' if len(categories)==1 else '<details>', f'<summary><strong>{c}</strong> · {len(group)} {"guide" if len(group)==1 else "guides"}</summary>', '']
        lines += table(group, '.') + ['', '</details>', '']
    lines += [END]
    root = (ROOT / 'README.md').read_text()
    if root.count(START)!=1 or root.count(END)!=1:
        raise ValueError('Expected one library block in root README.')
    result[ROOT/'README.md'] = re.sub(re.escape(START)+r'.*?'+re.escape(END), lambda _: '\n'.join(lines), root, flags=re.S)
    lines = ['# Business Book Summaries and Practical Guides', '', '[Home](../README.md) · [Topics](../topics/README.md) · [Planned collection](roadmap.md)', '',
             'Browse published guides alphabetically by title. Each book has one permanent home, with its templates and examples linked alongside it. Publication describes availability, not human expert review; read each guide’s editorial note.', '']
    lines += table(published, 'books')
    result[ROOT/'books/README.md'] = '\n'.join(lines)+'\n'
    lines = [f'# Planned Business Book Collection', '', '[Home](../README.md) · [Published guides](README.md) · [Selection methodology](../docs/book-selection.md)', '',
             f'The collection currently contains {len(books)} selected titles. The {len(planned)} entries below are planned or in development, not published summaries. This is a curated reading list, not an all-time sales ranking. No publication dates are promised.', '',
             ' · '.join(f'[{c}](#{slug(c)})' for c in CATEGORIES if any(b['category']==c for b in planned)), '']
    for c in CATEGORIES:
        group = [b for b in planned if b['category']==c]
        if not group: continue
        lines += [f'## {c}', '', '| Book | Author | Status |', '| --- | --- | --- |']
        for b in sorted(group, key=lambda b: (b['title'].casefold(), b['author'])):
            lines.append(f"| {cell(b['title'])} | {cell(b['author'])} | {b['status'].capitalize()} |")
        lines += ['']
    result[ROOT/'books/roadmap.md']='\n'.join(lines)
    lines=['# Business Books by Topic', '', '[Home](../README.md) · [A–Z index](../books/README.md) · [Planned collection](../books/roadmap.md)', '',
           'Choose a topic to find published guides and practical resources. Each book has one primary category; related guides can link across topics without duplicating content.', '', '| Topic | Published guides |', '| --- | ---: |']
    for c in categories:
        group=[b for b in published if b['category']==c]
        lines.append(f'| [{c}]({slug(c)}.md) | {len(group)} |')
        page=[f'# {c}: Business Books and Practical Guides', '', '[All topics](README.md) · [A–Z index](../books/README.md) · [Home](../README.md)', '']+table(group,'topics')
        result[ROOT/f'topics/{slug(c)}.md']='\n'.join(page)+'\n'
    lines += ['', 'Other subjects will appear here as guides are published. The [planned collection](../books/roadmap.md) includes the full topic range.', '']
    result[ROOT/'topics/README.md']='\n'.join(lines)
    return result


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check',action='store_true')
    args=parser.parse_args()
    stale=[]
    for path,content in outputs().items():
        if args.check:
            if not path.exists() or path.read_text()!=content: stale.append(str(path.relative_to(ROOT)))
        else:
            path.parent.mkdir(parents=True,exist_ok=True)
            path.write_text(content)
    if stale: raise SystemExit('Regenerate public navigation: '+', '.join(stale))
    print('Public navigation is current.' if args.check else 'Generated homepage library, A–Z index, topic pages, and planned collection.')


if __name__=='__main__':
    main()
