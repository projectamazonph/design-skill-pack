# Agent Instructions — Design Skill Pack

This directory contains a portable design skill pack — a collection of opinionated Markdown files that encode premium design systems. Any AI agent (Claude, GPT, Copilot, Cursor, Gemini, etc.) can use these to produce polished, non-template UIs.

## How This Works

Each `.md` file in `skills/` is a **self-contained skill** that an agent can read and execute. Skills have no dependencies, no runtime, no special tooling — they are pure instruction.

## Entry Points

| File | When to Use |
|------|-------------|
| `skills/design-system-master.md` | **Orchestrator** — reads project context and recommends a skill. Start here if unsure. |
| `skills/<skill-name>.md` | **Direct skill** — apply a specific design direction (premium, editorial, hallmark, etc.) |
| `docs/SKILL-CATALOG.md` | **Catalog** — browse all available skills to pick the right one |
| `docs/guides/QUICKSTART.md` | **Quick start** — runnable examples for different workflows |

## Workflow

1. **Read the brief** — understand the project type (SaaS, landing, portfolio, etc.) and desired mood
2. **Pick a skill** — use the orchestrator or scan the catalog
3. **Read the skill file** — load `skills/<skill>.md` in full
4. **Apply in order**:
   - Design tokens → CSS custom properties in `:root`
   - Layout archetype → structural grid/flow
   - Component rules → anatomy, states, variants
   - Motion → animations with reduced-motion fallback
   - QA checklist → verify against quality gates
5. **Respect reduced motion** — always include `prefers-reduced-motion: reduce` fallbacks
6. **Respect mobile** — collapse layouts below 768px, ensure 44px+ touch targets

## When to Use Which Skill

| The user wants... | Load this skill |
|------------------|----------------|
| "Don't make it look AI-generated" | `hallmark` or `design-taste-frontend` |
| "Make it look premium / Apple-like" | `premium` |
| "Make it look like an award-winning agency" | `high-end-visual-design` |
| "Make it look like a magazine" | `editorial` |
| "Make it minimalist and clean" | `sleek` or `minimal` |
| "Make it look professional / B2B" | `professional` |
| "Make it look warm and editorial" | `editorial` or `impeccable` |
| "Add glass effects" | `glassmorphism` |
| "Add good shadows" | `beautiful-shadows` |
| "Add scroll animations" | `animation-on-scroll` or `staggered-word-reveal` |
| "I don't know, pick something" | `design-system-master` (orchestrator) |

## Anti-Patterns (Agent Rules)

When applying any design skill, the agent MUST NOT:

- Use **Inter, Roboto, Arial, Open Sans, Helvetica** as fonts (these are AI defaults)
- Use **default Tailwind shadows** (`shadow-sm`, `shadow-md`, etc.) — use beautiful-shadows or custom layered shadows instead
- Use **linear or ease-in-out** for transitions — use custom cubic-bezier curves
- Output **symmetrical 3-column grids** without structural variety
- Use **purple gradients** as the primary brand color
- Use **thick-stroked icons** (Lucide default) — prefer ultra-light or thin variants
- Forget **reduced-motion** alternatives
- Forget **mobile responsive** collapse
- **Delete production files** without explicit user approval

## Adding Skills

See `docs/CONTRIBUTING.md`. The short workflow: create a `.md` file in `skills/` with `name:` and `description:` in frontmatter, then update the catalog. Validate with `python3 scripts/validate.py`.

## Portability

This pack is designed to work with **any AI coding agent** on **any platform**:

| Agent | How to Reference |
|-------|-----------------|
| Claude (Anthropic) | "Read skills/premium.md and apply it" |
| ChatGPT / GPT (OpenAI) | "I have a design skill pack, read skills/design-system-master.md" |
| GitHub Copilot / Cursor | "@workspace read skills/hallmark.md and redesign this component" |
| Gemini (Google) | "Follow the design rules in skills/editorial.md" |
| Any agent | Attach or reference the skill file directly |
