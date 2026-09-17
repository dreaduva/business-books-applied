# Implementation plan: Business Books, Applied

Decision date: 2026-09-17. Repository: `dreaduva/business-books-applied`.

## Outcome

Build a useful, free GitHub library around 100 widely read business books. Readers can find a book, understand a relevant idea, and apply it using an original resource. Google discovery and optional Amazon referrals support the project; usefulness is the publication test.

The current 100-book research list is the starting catalog. It has not been established as the 100 most popular business books of all time. Validate the selection before making a ranking claim; do not silently replace it.

## Reader experience and information structure

| Surface | Reader question | Implementation |
| --- | --- | --- |
| Root README | What can I do here? | Short introduction, three useful starting routes, topics, featured example |
| Books index | Which book helps me? | All 100 titles, grouped by subject, authors, guide status |
| Book README | What does this book mean for my situation? | Cover, affiliate line when configured, summary, original application, example, limits, sources |
| Playbook | How do I complete this task? | Inputs, steps, useful deliverable, decision checks, supporting books |
| Skill | Can my assistant help me do this? | Specific trigger, required inputs, process, output, quality checks |
| Example | What does good work look like? | Completed artifacts using one explicitly fictional business |

Use ordinary Markdown, relative links to explicit files, short tables, and occasional `<details>` blocks. Readers should reach a guide from the root in at most two clicks. Navigation and summaries stay visible. Expandable sections are for optional long examples or templates.

```text
README.md
books/README.md
books/<book-slug>/README.md
playbooks/README.md
playbooks/<task>.md
skills/README.md
skills/<task>/SKILL.md
templates/<task>.md
examples/tutor-scheduling/<artifact>.md
catalog/books.json
catalog/keywords.json
config/affiliate-links.json
config/covers.json
docs/
scripts/
```

Every book has one principal guide. A summary, review, and application normally share that guide. Separate comparison or resource pages need a distinct task and substantial content. A biography does not need an artificial worksheet or an unnecessary AI skill.

## Naming and keyword rules

Brand: **Business Books, Applied**. Repository: `business-books-applied`.

Use a natural page title: **[Exact book title]: Summary and [Useful application]**. Add the author where the title is ambiguous. Use a stable slug without dates or words such as `best`, `ultimate`, or `free-pdf`.

The existing research contains 1,323 keyword rows and 266 provider estimates across 21 books. The remaining rows are hypotheses or unavailable observations. Estimates are US-market provider data, not verified Google Keyword Planner counts. Preserve source URLs, retrieval dates, direct-versus-related labels, and unknown values. Do not sum overlapping variants or call a blank value zero.

Create one brief per title using that evidence. Check the actual Google results and search intent in the intended country before writing. This is especially important for workbook queries that refer to official paid products and for ambiguous titles such as *Traction*.

See [SEO strategy](seo-strategy.md) and [100 keyword briefs](keyword-briefs.md).

## Stage 1 — first repository

- [x] Create the GitHub-native navigation and 100-book catalog.
- [x] Preserve the existing keyword evidence and create per-book editorial briefs.
- [x] Write one useful sample guide, playbook, reusable template, skill, and worked example.
- [x] Add source, AI-assistance, reviewer, cover-rights, and affiliate configuration fields.
- [x] Add validation for catalog integrity, local links, headers, and publication metadata.
- [ ] Complete human editorial review of the first guide.
- [ ] Obtain or verify cover-art usage rights for the first guide.
- [ ] Activate the owner's Amazon links after marketplace and account requirements are checked.

The sample is published as a draft, not represented as a completed human-reviewed article. Its template and skill are usable now. Cover and affiliate activation are independent of writing the repository.

## Stage 2 — validate the selection and prepare ten guides

Preserve all 100 IDs while reviewing title/author/edition accuracy and dated popularity evidence. Use publisher or author sales disclosures, established bestseller records, and documented editorial judgment. Search volume measures current demand, not lifetime sales. Record where evidence is unavailable and avoid a fake numerical ranking.

Initial editorial queue:

| Order | Book | First application | Basis |
| --- | --- | --- | --- |
| 1 | The Mom Test | Customer interviews | Pilot chosen for a concrete founder task; direct questions estimate 30/month |
| 2 | Atomic Habits | Founder habit worksheet | Summary 6,600/month; worksheet-related query 1,600/month; official workbook intent needs care |
| 3 | The Lean Startup | MVP experiment brief | Summary 210/month; methodology variants need consolidation |
| 4 | Good to Great | Flywheel exercise | Direct flywheel estimate 210/month |
| 5 | Profit First | Explain allocation scenarios | Direct percentages estimate 1,000/month; financial claims require careful source review |
| 6 | Obviously Awesome | Positioning brief | Strong task fit; proposed angle, no claimed measured opportunity |
| 7 | Building a StoryBrand | Message outline | Direct framework estimate 70/month |
| 8 | Deep Work | Focus schedule | Direct rules estimate 40/month |
| 9 | The Personal MBA | Business model review | Direct review estimate 110/month |
| 10 | Never Split the Difference | Conversation preparation | Useful companion task; techniques query unavailable, not zero |

This is an editorial production sequence, not an SEO difficulty ranking. No organic difficulty measurements are available.

For each guide: source packet → original draft → application tested with a worked example → factual and stylistic review → rights and affiliate checks → publication. A real human reviewer records their name or GitHub handle and review date. Publish reviewed guides in small batches rather than filling 100 folders with interchangeable drafts.

## Stage 3 — expand to 25, 50, and 100

At each checkpoint, inspect which guides readers use, recurring corrections, broken links, and available search evidence. Improve weak examples before expanding. Add playbooks only when multiple books help with the same task. Keep one coherent fictional example for connected founder workflows, with other examples only where the topic requires them.

Use biographies for decision analysis, constraints, and alternative interpretations. Use finance books for clearly sourced educational explanations; do not turn generalized rules into personal financial advice. There is no fixed word-count quota or obligation to create 100 separate AI skills.

## Stage 4 — measure discovery and usefulness

Record publication dates and manual Google spot-checks by exact query, country, language, date, and observed URL. A `site:` search is only a spot-check, not a complete index or ranking report. Use GitHub's own traffic/referrer and contribution information where available; keep private analytics outside the public repository.

A GitHub repository does not give us control of GitHub.com's HTML metadata, canonical tags, robots rules, or normal Search Console ownership verification. A committed sitemap or verification file does not change that. If stronger search control later proves necessary, evaluate a separately authorized documentation domain; this implementation remains a repository and does not enable GitHub Pages.

## Release checks

A finished guide has a source-backed explanation, one useful original contribution, a completed example or appropriate case analysis, clear limits, working navigation, accurate authorship/review metadata, and an approved cover-use record. A configured affiliate link sits directly underneath the cover with a visible disclosure. It must point to the matching book and edition, use the owner's account, and remain secondary to the guide.

Run `python3 scripts/check.py` before publishing. It cannot establish truth, rights ownership, human review quality, or future rankings; those require editorial evidence.

## Sources for platform decisions

- [GitHub advertising rules](https://docs.github.com/en/site-policy/acceptable-use-policies/github-acceptable-use-policies#10-advertising-on-github): related promotion is allowed, but cannot be the primary focus.
- [GitHub robots.txt](https://github.com/robots.txt): inspected on 2026-09-17; directory routes are disallowed for the general crawler group. Use explicit Markdown file links and recheck behavior after publishing.
- [Google helpful-content guidance](https://developers.google.com/search/docs/fundamentals/creating-helpful-content): emphasize original value, accurate authorship, and reader usefulness.
- [Google guidance on generative AI content](https://developers.google.com/search/docs/fundamentals/using-gen-ai-content): automation does not excuse low-value scaled content.
- [Amazon operating agreement](https://affiliate-program.amazon.com/help/operating/agreement) and [program policies](https://affiliate-program.amazon.com/help/operating/policies): disclosures, links, and image use have separate conditions. Verify the relevant marketplace before activation.
