# The Lean Startup: Summary, MVP Experiments, and Decision Log

<!-- BOOK-HEADER:START -->
<img src="https://covers.openlibrary.org/b/isbn/9780307887894-M.jpg?default=false" alt="The Lean Startup by Eric Ries — book cover" width="180">

[Official book information and buying options](https://theleanstartup.com/)

Cover: via Open Library; artwork remains the property of its respective rights holders. [Image source](https://openlibrary.org/isbn/9780307887894).
<!-- BOOK-HEADER:END -->

**Eric Ries · Complete applied toolkit v1.0**

[Summary](#summary) · [Worksheet](worksheet.md) · [Worked example](worked-example.md) · [Playbook](../../playbooks/startup-experiment-planner.md) · [AI skill](../../skills/startup-experiment-planner/SKILL.md)

Your team can ship quickly and still learn very little. If nobody knows which assumption a feature tests, a release may produce activity without changing a decision.

## Summary

Eric Ries presents startup work as learning under uncertainty. His methodology connects building a limited intervention, measuring what happens, and deciding what to change. The point of an MVP is to begin useful learning, not merely release a smaller product. Progress depends on evidence about the business rather than the amount of software produced. [Author's methodology](https://theleanstartup.com/principles).

## Build-Measure-Learn in practice

Start by naming the decision. “Build an automated reminder” is a task; “Should we automate confirmations for this segment?” is a decision. Work backward to the evidence that could alter it, then choose the smallest responsible intervention capable of producing that evidence.

| Stage | Original tutor-product application | Common mistake |
| --- | --- | --- |
| Build | Offer a manually operated confirmation process with explicit participant consent | Pretend a human service is automated |
| Measure | Record completed confirmations and coordinator effort | Count page views as successful coordination |
| Learn | Compare outcomes and burden with the prior process | Declare success because some people signed up |

An MVP still has to respect the user's expectations. A small test that mishandles sensitive information or promises functionality it cannot deliver is not improved by being cheap.

## Choose a metric that answers the question

Define the unit, denominator, time window, and inclusion rules before seeing the results. In a scheduling test, the unit might be a lesson-change event. If the question is repeated adoption, a single successful event is insufficient: return use needs its own observation window.

Track a guardrail as well as the desired outcome. Reducing missed confirmations by requiring an hour of founder labor per tutor might solve the immediate problem while failing the business constraint. Neither result should disappear from the review.

## Pivot, persevere, or investigate further?

A disappointing result can reflect the hypothesis, recruitment, execution, or measurement. Name these competing explanations before choosing a direction. A pivot changes a substantive assumption; changing button color is not necessarily one. Conversely, limited evidence is not a reason to rebuild the whole business.

Use the completed example to see a test that improves one outcome but fails its effort limit. Its numbers are invented and its thresholds are local decisions, not benchmarks attributed to Ries.

## Questions readers ask

**Is an MVP always software?** Our worksheet permits a service or manual process when that can test the assumption honestly. State what participants are actually receiving.

**How many users prove an idea?** This toolkit supplies no universal number. Specify what the evidence can resolve and what uncertainty remains.

**What should happen before an experiment?** If the problem itself is unclear, start with [customer interviews](../the-mom-test/README.md). If it is clear enough, define a test rather than using more discussion to postpone action.

## Use the toolkit

Copy [the worksheet](worksheet.md), compare it with [the completed fictional example](worked-example.md), or follow [the playbook](../../playbooks/startup-experiment-planner.md). The skill installation includes its worksheet, method reference, and completed example.

```bash
npx skills add dreaduva/business-books-applied --skill startup-experiment-planner
```

## Sources and further reading

- [Author: Lean Startup methodology](https://theleanstartup.com/principles)
- [Publisher: book and edition](https://www.penguinrandomhouse.com/books/210088/the-lean-startup-by-eric-ries/)

Cover edition: ISBN 9780307887894. This guide is an independent practical application, not an official workbook. Read the full book for the author's wider argument and examples.

[All books](../README.md) · [All skills](../../skills/README.md)
