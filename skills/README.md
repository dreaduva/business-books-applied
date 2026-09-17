# Installable Business Skills

[Home](../README.md) · [Book guides](../books/README.md) · [Playbooks](../playbooks/README.md)

Install a focused business workflow in your AI assistant. These are instructions and supporting templates; they work from the information you provide and do not invent customer evidence.

<!-- SKILLS:START -->
| Skill | What you produce | Supporting book |
| --- | --- | --- |
| [Startup Experiment Planner](startup-experiment-planner/SKILL.md) | Startup Experiment Plan | [The Lean Startup](../books/the-lean-startup/README.md) |
| [Customer Interview Planner](customer-interview-planner/SKILL.md) | Interview plan, evidence debrief, and next test | [The Mom Test](../books/the-mom-test/README.md) |
| [Product Positioning](product-positioning/SKILL.md) | Positioning Brief | [Obviously Awesome](../books/obviously-awesome/README.md) |
| [Lead Generation Planning](lead-generation-planner/SKILL.md) | Lead Generation Plan | [$100M Leads](../books/100m-leads/README.md) |
| [Landing-Page Messaging](landing-page-messaging/SKILL.md) | Landing-Page Messaging Brief | [Building a StoryBrand](../books/building-a-storybrand/README.md) |
| [Acquisition Channel Testing](acquisition-channel-testing/SKILL.md) | Acquisition Channel Test Plan | [Traction](../books/traction-gabriel-weinberg/README.md) |
| [Offer Design](offer-design/SKILL.md) | Offer Design Brief | [$100M Offers](../books/100m-offers/README.md) |
| [Business Process Design](business-process-design/SKILL.md) | Repeatable Process Brief | [The E-Myth Revisited](../books/the-e-myth-revisited/README.md) |
| [Habit Experiment Planning](habit-experiment-planner/SKILL.md) | Habit Experiment Plan | [Atomic Habits](../books/atomic-habits/README.md) |
| [Deep Work Planning](deep-work-planner/SKILL.md) | Focused Work Plan | [Deep Work](../books/deep-work/README.md) |
<!-- SKILLS:END -->

## Quick install

Requires Node.js and npm. Run from your project directory:

```bash
npx skills add dreaduva/business-books-applied
```

The installer lets you choose skills and supported assistants. Installation is project-scoped by default. Only completed skills appear in the installer; planned book guides are not installed.

## Choose an assistant

Install the interview skill for Claude Code:

```bash
npx skills add dreaduva/business-books-applied --skill customer-interview-planner --agent claude-code
```

Or for Codex:

```bash
npx skills add dreaduva/business-books-applied --skill customer-interview-planner --agent codex
```

Add `--global` if you want the skill available across projects rather than in the current project. Start a new assistant session after installation if it has not picked up the skill yet.

## Try it

```text
Use the customer-interview-planner skill to plan interviews with independent
tutors about schedule changes. I suspect confirmations create admin work,
but I have no customer evidence. Help me investigate without pitching an app.
```

For planning, expect a learning objective, participant criteria, actual interview questions, and an evidence log. For existing scripts, ask for a question-by-question revision. For supplied notes, ask for a traceable debrief and next-test card. You still need to conduct the interviews and supply real findings.

## Preview or use manually

List available skills without installing:

```bash
npx skills add dreaduva/business-books-applied --list
```

For a chat assistant without skill installation, provide the [skill instructions](customer-interview-planner/SKILL.md) and [output template](customer-interview-planner/assets/interview-plan.md) as context, then describe your situation. This is manual use, not a persistent installation.

The installer is the [open-source skills CLI](https://github.com/vercel-labs/skills). Packages follow the [Agent Skills format](https://agentskills.io/specification); each skill folder includes its own supporting files. Book guides and purchase links stay outside the installed skill.

## What gets installed

Every skill includes its own instructions, editable worksheet, method reference, and completed fictional example. The Customer Interview Planner also includes question repair, evidence debrief, and next-test resources.

Local references stay inside each package, so a skill works without the rest of the repository. Shared worksheets and examples are synchronized automatically. These tools help structure work; they do not supply real customer evidence or establish that a business decision will succeed.
