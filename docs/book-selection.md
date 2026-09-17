# How books are selected

The current catalog preserves the owner's existing 100-book research list. It spans business fundamentals, entrepreneurship, management, marketing, personal effectiveness, money, and founder biographies. This broad scope is intentional, but it is not a verified list of the 100 most popular business books of all time.

## What popularity means here

Lifetime sales, current search demand, bestseller appearances, readership, and founder usefulness are different measures. They must not be merged into a number that looks like a sales ranking.

For each candidate, record:

- Exact title, authors, and the edition discussed.
- A dated publisher/author sales claim or established bestseller record, where available.
- The scope of that evidence: global or national, all editions or one, total copies or a chart appearance.
- Current keyword evidence, clearly separated from historical popularity.
- Why the book belongs in this project's business scope.

The `popularity_evidence` field in `catalog/books.json` holds sourced observations. An empty list means unverified. Catalog IDs preserve the earlier research order; they are not rankings.

## Changes to the list

Preserve the original 100 catalog IDs while auditing candidates; future additions receive new IDs. Do not silently remove books with low measured search volume or mistake unavailable data for a lack of readers. Record replacements and the owner's editorial decision before changing the scope.

Two entries are titled *Traction*: Gabriel Weinberg and Justin Mares's marketing book, and Gino Wickman's operations book. Keep their authors, slugs, sources, and query intent separate.

## Public wording

Use “100 business books” or “a curated business-book library.” Use “most popular of all time” only if a defensible definition, adequate evidence, and clear limitations support the claim. A well-sourced curated list may be more accurate than a purported definitive ranking.
