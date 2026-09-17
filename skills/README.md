# Installable Business Skills

[Home](../README.md) · [Book guides](../books/README.md) · [Playbooks](../playbooks/README.md)

Install a focused business workflow in your AI assistant. These are instructions and supporting templates; they work from the information you provide and do not invent customer evidence.

| Skill | Use it to | Based on |
| --- | --- | --- |
| [Customer Interview Planner](customer-interview-planner/SKILL.md) | Prepare neutral questions, an interview plan, and an evidence log | [The Mom Test](../books/the-mom-test/README.md) |

## Quick install

Requires Node.js and npm. Run from your project directory:

```bash
npx skills add dreaduva/business-books-applied
```

The installer lets you choose skills and supported assistants. Installation is project-scoped by default. The collection currently contains one installable skill; planned book guides are not installed as skills.

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

Expect a learning objective, participant criteria, interview prompts, and an evidence log using the bundled template. You still need to conduct the interviews and supply real findings.

## Preview or use manually

List available skills without installing:

```bash
npx skills add dreaduva/business-books-applied --list
```

For a chat assistant without skill installation, provide the [skill instructions](customer-interview-planner/SKILL.md) and [output template](customer-interview-planner/assets/interview-plan.md) as context, then describe your situation. This is manual use, not a persistent installation.

The installer is the [open-source skills CLI](https://github.com/vercel-labs/skills). Packages follow the [Agent Skills format](https://agentskills.io/specification); each skill folder includes its own supporting files. Book guides and purchase links stay outside the installed skill.
