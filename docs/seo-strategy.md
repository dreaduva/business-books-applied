# SEO strategy and evidence

## The search promise

Answer a reader's question about a specific book, then help them use an idea. The main book guide combines summary intent with a relevant application. Avoid publishing separate thin pages for every wording of the same query.

Book titles belong in headings, readable filenames, catalog links, and descriptive cover alt text. Use specific application headings only when the section actually answers that query. Do not add invisible keywords, fake reviews, repeated synonyms, or full-book PDF bait.

## What the research supports

The preserved dataset has 100 books, 1,323 rows, and 266 provider estimates across 21 books. A row labeled `Provider estimate` is still an estimate. A `Related suggestion` is not an exact direct lookup. `Unverified candidate` and HTTP 404 rows do not establish search volume.

The provider was seodata.dev; country parameter `us`; retrieval dates 2026-09-16 and 2026-09-17. The dataset's `date` field is retained as supplied by the earlier research and must not be represented as a verified Google measurement period. We do not have comparable organic difficulty or complete 100-book volume coverage.

[Keyword evidence](../catalog/keywords.json) preserves the source rows. [Editorial briefs](keyword-briefs.md) map each title to one principal guide and useful application ideas. Numeric evidence and editorial hypotheses remain distinct. Do not sum overlapping keywords to forecast traffic.

## Page intent and headings

| Page | Title pattern | Main purpose |
| --- | --- | --- |
| Book guide | The Mom Test: Summary and Customer Interview Questions | Understand the book and apply one idea |
| Task playbook | Plan Your First Customer Interviews | Complete a task, drawing on relevant sources |
| Skill | Customer Interview Planner | Give an assistant an actionable procedure |
| Catalog | 100 Business Books: Summaries and Practical Guides | Navigate titles and topics |

The root brand and subtitle explain the project. Individual guide headings carry the precise book/topic language. There is no claim that a repository name alone produces rankings.

## GitHub-specific limits

Link to `books/the-mom-test/README.md`, not just the directory. GitHub's [robots rules](https://github.com/robots.txt), checked 2026-09-17, disallow `/tree/` directory paths in the general crawler group. Explicit Markdown files normally resolve to `/blob/` views. Check the live rendered pages; allowed crawling is not guaranteed indexing.

We control Markdown content, structure, internal links, filenames, repository description, and topics. GitHub controls the surrounding HTML, canonical URLs, crawler rules, and most search metadata. Do not pretend YAML frontmatter in a README configures an HTML title, or that adding a sitemap enables Search Console ownership verification.

Keep stable default-branch paths. Do not create duplicate repositories for keyword variants or use fake stars, mass issues, unsolicited promotional comments, or automated search queries as a ranking tactic.

## Before writing

Inspect the Google results for the actual query in the intended country and record date, intent, and a few representative result URLs. Public research queries were already collected, but they are not a complete live Google ranking audit. For example, “Atomic Habits workbook” can mean the author's official product; call our resource an original worksheet and explain its independence.

## After publication

Use a dated observation log for Google discovery spot-checks and real reader feedback. Record the exact URL that appears, not just whether the repository appears somewhere. Inspect GitHub traffic/referrers where available and Amazon reporting only after links are configured. Do not fabricate click-through rates, conversions, or a 90-day traffic forecast.

Google recommends [helpful, original content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content), and warns against [scaled content made without added value](https://developers.google.com/search/docs/fundamentals/using-gen-ai-content). The editorial process implements those principles; no ranking is guaranteed.
