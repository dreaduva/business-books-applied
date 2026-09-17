# Maintaining the Library

Python 3.10 or later is enough for the repository scripts. There are no third-party Python dependencies.

## Update the catalog

Edit `catalog/books.json`. Keep IDs stable. When a useful draft guide exists, set its `guide_path` and status to `draft`; do not create empty files for planned books.

```bash
python3 scripts/build_catalog.py
python3 scripts/render_headers.py
python3 scripts/check.py
```

The build script generates the homepage library section, alphabetical index, topic navigation, and planned collection. Book prose, examples, and criticism remain editorial work.

## Complete review

Follow [the editorial checklist](editorial-standards.md), then record the source-check date and scope in the catalog. Check the edition, examples, links, and presentation before marking a guide `published`. Human review is a separate optional credit: record a reviewer and review date only when a person has actually performed it.

## Add a cover

In `config/covers.json`, record the image URL, source, edition, credit, permitted use, evidence URL, and check date. Set status to `approved` only when the rights basis has been established. Use a stable authorized HTTPS image URL suitable for GitHub's rendering and image proxy. The header renderer displays it at 180 px wide with descriptive alt text and a credit.

For an Open Library cover, use `service-embed` instead of `approved`, retain the direct cover-service URL, and record the service's embedding guidelines as the display basis. This does not claim a copyright license to the artwork. Keep private correspondence and internal research in `private/`, which is ignored by Git. Summarize permission publicly without exposing private contact details. This repository does not scrape Amazon images or store API credentials.

## Add affiliate links later

The owner deferred Amazon setup. When details are available, verify [the account and placement requirements](affiliate-and-cover-policy.md), then edit `config/affiliate-links.json`:

- Set the actual marketplace, and record confirmation of the account and registered site.
- Add an owner-provided Amazon product URL under the matching book slug in `links`.
- Set `enabled` to `true` only after those steps.
- Run the header renderer and review the resulting Markdown diff.
- Update the root README's affiliate-status sentence when links are actually enabled.

The rendered text link appears directly below the cover, followed by the disclosure. Prices, ratings, and live availability are intentionally absent.

## Validate and publish

The checker verifies preservation of the original 100 IDs, unique slugs, explicit local file links and heading anchors, generated-file freshness, and required publication metadata. It does not make live affiliate clicks or fetch every external source.

After a push, inspect the rendered README and the sample guide on GitHub. Check that navigation resolves to file views, images render where approved, and the Actions check passes. Review Google discovery separately; a successful check is not SEO evidence.

## Public and private material

Public: book guides, templates, examples, usable AI skills, reader navigation, minimal catalog metadata, editorial standards, image attribution, and validation scripts.

Local only: raw keyword research, SEO briefs, implementation plans, account notes, and agent working instructions. Keep these under ignored `private/`; never link public pages to them. The public build must work from a clean clone without this folder. Removing a previously published file from the current branch does not remove it from Git history.

## Scale and resource ownership

Assign each book one primary category from `scripts/build_catalog.py`. Add a category there when a real editorial need arises. Keep slugs and IDs stable, disambiguate identical titles, and never use IDs as popularity rankings. New books may extend the original 100.

Only published guides appear in the homepage, alphabetical index, and topic directory. Planned and draft titles appear separately in `books/roadmap.md`. Empty topic pages and empty book folders are not generated.

Edit the homepage outside its LIBRARY markers. The generated section lists each published book once, grouped by its primary category. Its resource links come from `catalog/books.json`.

Book-specific templates and examples live in the book folder; shared workflows live in `playbooks/`. Skill assets can include a portable output scaffold so downloading a skill does not depend on other folders; avoid duplicating whole book guides there.
