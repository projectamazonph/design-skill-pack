# Design Skill Pack 🎨

> **20+ opinionated design skills for any AI coding agent** — bundled into one portable pack with a master orchestrator that auto-selects the right design direction for your project.

[![Version](https://img.shields.io/badge/version-1.0.0-blue)](.)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

---

## What This Is

A collection of **23 structured design skills** that any AI agent can use to produce premium, non-template UIs. Each skill is a self-contained Markdown file with:

- **Design tokens** — CSS variables for colors, typography, spacing, shadows, motion
- **Anti-patterns** — exactly what NOT to do (banned fonts, shadows, layouts)
- **Layout archetypes** — structural patterns (bento, editorial, split-screen, cascade)
- **Component rules** — anatomy, states, variants, responsive behavior
- **Motion guidelines** — animation specs, easing curves, reduced-motion fallbacks
- **Quality gates** — testable acceptance criteria

---

## Why This Exists

AI agents default to the same tired patterns — purple gradients, three-card feature grids, Inter font, centered heroes on dark mesh. This pack breaks that by encoding **23 distinct design philosophies** into rigorous, opinionated instructions that agents follow step by step.

---

## Quick Start

1. **Clone or copy** this repo into your project
2. **Reference a skill** in your agent prompt:
   ```
   Read skills/premium.md and apply its design system to the landing page
   ```
3. **Or let the orchestrator choose**:
   ```
   Read skills/design-system-master.md and follow its selection matrix for my project
   ```

**Zero dependencies.** Just Markdown files and CSS tokens.

---

## The Skills

| # | Skill | Description | Best For |
|---|-------|-------------|----------|
| 1 | `hallmark` | Anti-AI-slop design with structural variety, 20 named themes, audit/redesign/study verbs | Greenfield pages, redesigns, design extraction |
| 2 | `high-end-visual-design` | Awwwards-tier agency aesthetics with double-bezel architecture, fluid motion, variance engine | Portfolios, agency sites, premium SaaS |
| 3 | `premium` | Apple-inspired precision, refined spacing, polished typography | SaaS dashboards, product pages, enterprise |
| 4 | `editorial` | Magazine-inspired layouts with serif typography, structured grids | Blogs, editorial sites, content-heavy pages |
| 5 | `sleek` | Modern minimalist with clean lines, muted palette, subtle interactions | Modern apps, minimal dashboards |
| 6 | `modern` | Contemporary editorial with serif type, minimal palettes | Digital products, creative studios |
| 7 | `minimal` | Stripped-back design emphasizing whitespace and clarity | Portfolios, landing pages |
| 8 | `professional` | Polished, business-ready with trustworthy visual identity | B2B, corporate, enterprise |
| 9 | `refined` | Curated sophistication with elegant serif typography | Luxury, high-end brands |
| 10 | `neobrutalism` | Bold borders, vivid accents, raw high-contrast layouts | Creative agencies, edgy brands |
| 11 | `glassmorphism` | Frosted glass with translucent layers and luminous borders | SaaS, AI products, tech startups |
| 12 | `beautiful-shadows` | Polished layered elevation with multi-stop shadow utilities | Any project needing refined depth |
| 13 | `staggered-word-reveal` | Editorial word-by-word reveal on scroll | Headlines, hero copy, premium text |
| 14 | `animation-on-scroll` | IntersectionObserver-driven scroll animations | Section entries, feature reveals |
| 15 | `landing-page` | High-conversion patterns, structure, copywriting | SaaS landing pages, marketing sites |
| 16 | `pricing-page` | Pricing page structure, plan design, conversion | SaaS pricing pages |
| 17 | `design-taste-frontend` | Anti-default design inference with 3-dial system | Any project needing taste-level guidance |
| 18 | `redesign-existing-projects` | Upgrade existing UIs without breaking functionality | Brownfield projects |
| 19 | `styleseed-design-review` | AI-generated design detection and quality scoring | Code reviews, pre-ship checks |
| 20 | `clean-minimal-beige-light-mode` | Warm beige systems with restrained accents | Calm, premium, process-oriented UIs |
| 21 | `nested-container-clean-agency` | Agency nested shells with editorial frames | Agency sites, service pages |
| 22 | `split-layout-technical` | Technical split-screen with mono metadata | Product pages, showcases, specs |
| 23 | `impeccable` | Editorial-poster aesthetic with warm amber tones | Graphic portfolios, creative brands |
| ∞ | `design-system-master` | **Orchestrator** — auto-selects the right skill(s) for your context | When you don't know which to pick |

---

## How to Use with Any AI Agent

### Claude (Anthropic)
```
Attached is a design skill pack. Read skills/design-system-master.md and apply the recommended design direction to the landing page at src/app/landing/page.tsx.
```

### GPT / ChatGPT
```
I have a design skill pack in my project at skills/. Read skills/premium.md and apply its design tokens and layout rules to my dashboard components.
```

### Copilot / Cursor
```
@workspace Please read skills/hallmark.md and do a redesign of the src/components/Hero.tsx component following its rules.
```

### Any Agent
```
I'm attaching a set of design skill files. Read the one called "hallmark" and follow its instructions to redesign my landing page.
```

---

## Common Workflows

### 1. Redesign an Existing Page
Point the agent to `hallmark` with a redesign verb:
```
Read skills/hallmark.md. Do a hallmark redesign of src/app/landing/page.tsx — audit the current design, pick a theme, and restructure the visual layer.
```

### 2. Add Premium Polish
Layer utility skills on top of design system skills:
```
Read skills/premium.md and skills/beautiful-shadows.md. Apply premium tokens and layered shadows to all cards, KPIs, and panels.
```

### 3. Build a Landing Page from Scratch
Let the orchestrator choose:
```
Read skills/design-system-master.md. Follow its selection matrix for my SaaS landing page and apply the recommended skill.
```

### 4. Design a Pricing Page
```
Read skills/pricing-page.md for structure guidance, then skills/premium.md for the visual system.
```

### 5. Audit Design Quality
```
Read skills/styleseed-design-review.md. Review my UI against its criteria and produce a ranked punch list.
```

---

## Project Structure

```
design-skill-pack/
├── skills/                    # Individual skill files (Markdown with YAML frontmatter)
│   ├── design-system-master.md
│   ├── hallmark.md              (placeholder — add the source)
│   ├── premium.md               (placeholder — add the source)
│   ├── beautiful-shadows.md     (placeholder — add the source)
│   └── ... (more skills)
├── docs/
│   ├── SKILL-CATALOG.md       # Full catalog with descriptions and references
│   ├── ARCHITECTURE.md        # Skill structure and format specification
│   ├── CONTRIBUTING.md        # How to add new skills
│   └── guides/                # Usage tutorials
├── scripts/validate.py        # Validation script (Python, no deps)
├── AGENTS.md                  # Instructions for AI agents using this pack
├── README.md                  # This file
└── LICENSE                    # MIT
```

---

## Design System Philosophy

Every skill follows the same structure:

```
1. Design tokens  →  CSS custom properties
2. Anti-patterns  →  What to avoid (specific banned values)
3. Layout         →  Structural archetypes with mobile collapse
4. Components     →  Anatomy, states, variants
5. Motion         →  Physics-based curves, reduced-motion fallbacks
6. Quality gates  →  Testable checklist for code review
```

### Universal Anti-Patterns

| Anti-Pattern | Why It's Banned |
|-------------|----------------|
| `Inter`, `Roboto`, `Arial` fonts | AI agent default, overused |
| `shadow-md`, `rgba(0,0,0,0.3)` | Harsh, template-like |
| `linear`, `ease-in-out` transitions | Robotic, not organic |
| Symmetrical 3-column grids | Template layout, no structural variety |
| Purple gradients | AI-generated signal |
| Generic thick-stroked icons | Heavy, unrefined |

---

## Adding Skills

See [CONTRIBUTING.md](docs/CONTRIBUTING.md) for the full guide. Short version:

1. Create `skills/<your-skill>.md` with YAML frontmatter (`name`, `description`)
2. Include: tokens, anti-patterns, layout archetypes, motion, quality gates
3. Update the catalog
4. Validate: `python3 scripts/validate.py`

---

## License

MIT — use freely, attribute appreciated.
