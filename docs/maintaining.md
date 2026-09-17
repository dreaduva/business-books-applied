# Maintaining the Library

Python 3.10 or later is enough for the repository scripts. There are no third-party Python dependencies.

## Update the catalog

Edit `catalog/books.json`. Keep IDs stable. When a useful draft guide exists, set its `guide_path` and status to `draft`; do not create empty files for planned books.

```bash
python3 scripts/build_catalog.py
python3 scripts/render_headers.py
python3 scripts/check.py
```

The build script generates only navigation and research briefs. Book prose, examples, and criticism remain editorial work.

## Complete review

Follow [the editorial checklist](editorial-standards.md), then record the actual human reviewer and date in the catalog. Check the edition and sources before marking a guide `published`. Human review metadata must describe real work.

## Add a cover

In `config/covers.json`, record the image URL, source, edition, credit, permitted use, evidence URL, and check date. Set status to `approved` only when the rights basis has been established. Use a stable authorized HTTPS image URL suitable for GitHub's rendering and image proxy. The header renderer displays it at 180 px wide with descriptive alt text and a credit.

Keep private correspondence in `private/`, which is ignored by Git. Summarize permission publicly without exposing private contact details. This repository does not scrape Amazon images or store API credentials.

## Add affiliate links later

The owner deferred Amazon setup. When details are available, verify [the account and placement requirements](affiliate-and-cover-policy.md), then edit `config/affiliate-links.json`:

- Set the actual marketplace, and record confirmation of the account and registered site.
- Add an owner-provided Amazon product URL under the matching book slug in `links`.
- Set `enabled` to `true` only after those steps.
- Run the header renderer and review the resulting Markdown diff.
- Update the root README's affiliate-status sentence when links are actually enabled.

The rendered text link appears directly below the cover, followed by the disclosure. Prices, ratings, and live availability are intentionally absent.

## Validate and publish

The checker verifies the 100-book count, unique slugs, keyword provenance, explicit local file links and heading anchors, generated-file freshness, and required publication metadata. It does not make live affiliate clicks or fetch every external source.

After a push, inspect the rendered README and the sample guide on GitHub. Check that navigation resolves to file views, images render where approved, and the Actions check passes. Review Google discovery separately; a successful check is not SEO evidence.
