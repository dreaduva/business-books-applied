# Book guide template

Use these content requirements as a starting point. Adjust the flow to the book; do not repeat identical introductions across the library.

1. **Title:** exact book name, “Summary,” and one useful application where justified.
2. **Book header:** approved cover at about 180 px wide; owner-supplied affiliate link immediately underneath; visible disclosure. A draft may show a pending cover note.
3. **Context:** author, relevant edition if verified, who this helps, and a specific opening problem.
4. **Summary:** original concise explanation supported by consulted sources. Avoid a chapter-by-chapter substitute for the book.
5. **Application:** a real task, original questions or exercise, and the decisions it supports.
6. **Worked example:** completed material, with fictional status unmistakable where applicable.
7. **Limits:** weak evidence, contextual dependence, or situations where another approach fits better.
8. **Resources:** useful links to a template, playbook, skill, or complementary guide.
9. **Reading decision and sources:** explain who would benefit from the full book; cite source material without copying sales blurbs.
10. **Editorial note:** AI assistance, actual reviewer, source-check scope, and substantive update date.

The [sample guide](../books/the-mom-test/README.md) demonstrates the structure. The affiliate and cover lines are generated from explicit configuration using `python3 .github/library/render_headers.py`; they are never guessed from a title.

## Permanent home and navigation

Use `books/<stable-title-slug>/README.md`. Keep book-specific resources directly alongside the guide: `interview-plan.md`, `worked-example.md`, or another descriptive filename. Add subfolders only when a book actually needs several resources of the same type. Add only resources that exist to its catalog `resources` map. Use one primary topic; connect other topics through useful links rather than duplicate pages.

The guide's opening should link to its summary, template, example, and AI skill where available. Skills stay under `skills/` and shared workflows under `playbooks/`. Do not create a skill automatically for every book. Keep guide URLs stable. Update every internal link when moving a supporting resource.
