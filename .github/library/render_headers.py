#!/usr/bin/env python3
"""Render cover and affiliate blocks only from documented, owner-configured metadata."""
import argparse
import html
import json
import re
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[2]
START = "<!-- BOOK-HEADER:START -->"
END = "<!-- BOOK-HEADER:END -->"
AMAZON_HOSTS = {"amazon.com", "amazon.co.uk", "amazon.de", "amazon.fr", "amazon.it", "amazon.es", "amazon.ca", "amazon.com.au", "amazon.co.jp", "amazon.in", "amazon.com.br", "amazon.com.mx", "amazon.nl", "amazon.se", "amazon.pl", "amazon.sg", "amazon.ae", "amazon.sa", "amazon.com.tr", "amazon.eg", "amazon.com.be", "amazon.ie", "amzn.to"}


def safe_url(url, amazon=False):
    if not isinstance(url, str) or re.search(r'[\s<>"\'()]', url):
        raise ValueError("Use a properly encoded HTTPS URL.")
    parsed = urlparse(url)
    host = (parsed.hostname or "").removeprefix("www.")
    if parsed.scheme != "https" or not host or parsed.username or parsed.password:
        raise ValueError("Use an HTTPS URL without credentials.")
    if amazon and host not in AMAZON_HOSTS:
        raise ValueError("The configured affiliate URL is not an approved Amazon hostname.")
    return url


def header(book, covers, affiliate):
    slug = book["slug"]
    cover = covers.get(slug, {})
    cover_ready = cover.get("status") in {"approved", "service-embed"}
    lines = []
    if cover_ready:
        for key in ["source_url", "credit", "permission_basis", "permission_evidence_url", "edition", "checked_on"]:
            if not cover.get(key):
                raise ValueError(f"{slug}: approved cover requires {key}.")
        image = safe_url(cover.get("image_url"))
        safe_url(cover["source_url"])
        safe_url(cover["permission_evidence_url"])
        if cover.get("status") == "service-embed":
            if urlparse(image).hostname != "covers.openlibrary.org" or cover["permission_evidence_url"] != "https://openlibrary.org/dev/docs/api/covers":
                raise ValueError("Service embeds must use Open Library's cover host and documented embedding policy.")
        alt = html.escape(f"{book['title']} by {book['author']} — book cover", quote=True)
        lines.append(f'<img src="{html.escape(image, quote=True)}" alt="{alt}" width="180">')
    else:
        lines.append("*Cover image pending a documented reuse permission.*")

    link = affiliate.get("links", {}).get(slug)
    if affiliate.get("enabled") and link:
        if not all(affiliate.get(k) for k in ["marketplace", "site_registered", "account_confirmed"]):
            raise ValueError("Affiliate activation requires marketplace and account/site confirmation.")
        url = safe_url(link, amazon=True)
        lines += ["", f"[View {book['title']} on Amazon (affiliate link)]({url})", "", affiliate["disclosure"]]
    elif book.get("official_url"):
        official_url = safe_url(book["official_url"])
        lines += ["", f"[Book details and buying options — author's website]({official_url})"]
    else:
        lines += ["", "*Amazon affiliate link not configured.*"]
    if cover_ready:
        lines += ["", f"Cover: {cover['credit']}. [Image source]({cover['source_url']})."]
    return START + "\n" + "\n".join(lines) + "\n" + END


def outputs():
    books = json.loads((ROOT / ".github/library/books.json").read_text())
    covers = json.loads((ROOT / ".github/library/covers.json").read_text())
    affiliate = json.loads((ROOT / ".github/library/affiliate-links.json").read_text())
    results = {}
    for book in books:
        if not book["guide_path"]:
            continue
        path = ROOT / book["guide_path"]
        text = path.read_text()
        if text.count(START) != 1 or text.count(END) != 1:
            raise ValueError(f"{path}: expected one book header block.")
        results[path] = re.sub(re.escape(START) + r".*?" + re.escape(END), lambda _: header(book, covers, affiliate), text, flags=re.S)
    return results


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    for path, content in outputs().items():
        if args.check and path.read_text() != content:
            raise SystemExit(f"Stale header: {path.relative_to(ROOT)}; run .github/library/render_headers.py")
        if not args.check:
            path.write_text(content)
    print("Book headers are current." if args.check else "Rendered configured book headers.")


if __name__ == "__main__":
    main()
