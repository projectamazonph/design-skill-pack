# Design Skill Pack 🎨

> **20+ premium design skills for Codex** — bundled into one plugin with a master orchestrator that auto-selects the right design direction for your project.

[![Plugin Version](https://img.shields.io/badge/version-1.0.0-blue)](.codex-plugin/plugin.json)
[![Codex](https://img.shields.io/badge/Codex-Plugin-ff9900)](https://github.com/openai/codex)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

---

## Quick Start

```bash
# Install the plugin
codex plugin install design-skill-pack

# Or via Codex UI: Plugins → Design Skill Pack → Install

# Use the master orchestrator
@Design Skill Pack design-system-master
```

**No dependencies.** Just install and invoke.

---

## Why This Exists

LLMs default to the same patterns — purple gradients, three-card feature grids, Inter font, centered heroes on dark mesh. The **Design Skill Pack** breaks that by encoding 20+ distinct design philosophies into **structured, opinionated skills** that agents follow rigorously.

Each skill has:
- **Anti-patterns** (what NOT to do)
- **Design tokens** (colors, type, spacing, shadows)
- **Layout archetypes** (bento, editorial, split-screen, cascade)
- **Motion guidelines** (physics curves, reduced-motion fallbacks)
- **Quality gates** (accessibility, responsiveness, performance)

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

## Setup & Installation

### For Codex Users

```bash
# Install from marketplace
codex plugin install design-skill-pack

# Or from local path
codex plugin install /path/to/design-skill-pack
```

### For Plugin Development

```bash
# Clone the repo
git clone <repo-url>
cd design-skill-pack

# Validate the plugin
python3 .codex-plugin/scripts/validate_plugin.py .

# Update cachebuster after changes
python3 .codex-plugin/scripts/update_plugin_cachebuster.py .
```

---

## Usage Examples

### Redesign a Landing Page with Hallmark

```
@Design Skill Pack hallmark redesign src/app/landing
```

The agent will:
1. Audit the current design
2. Pick a theme from 20 named options
3. Apply structural variety (macrostructure fitting your content)
4. Implement tokens, layout, motion, and responsive behavior

### Add Premium Polish to a Dashboard

```
@Design Skill Pack premium
@Design Skill Pack beautiful-shadows
```

The agent will:
1. Apply Apple-inspired token system
2. Upgrade all card/panel shadows to layered beautiful-shadows
3. Add premium easing curves
4. Refine typography and spacing

### Full Agency-Quality Redesign

```
@Design Skill Pack high-end-visual-design
@Design Skill Pack staggered-word-reveal
@Design Skill Pack animation-on-scroll
```

The agent will:
1. Apply double-bezel nested architecture
2. Add fluid island nav with staggered reveals
3. Implement magnetic button physics
4. Add scroll interpolation with custom cubic-bezier

### Let the Master Decide

```
@Design Skill Pack design-system-master
```

The orchestrator reads your project and picks the optimal skill combo.

---

## Design System Philosophy

Each skill in this pack follows a **token-first** approach:

```css
:root {
  /* Design tokens defined by the skill */
  --surface-0: #...;
  --ink-900: #...;
  --accent: #...;
  --radius-md: ...;
  --shadow-md: ...;
  --ease-out: cubic-bezier(...);
}
```

Tokens are followed by **component architecture** (layout, spacing, typography), then **motion**, then **quality gates**.

### Anti-Patterns (Common Across All Skills)

| Anti-Pattern | Why It's Banned |
|-------------|----------------|
| `Inter`, `Roboto`, `Arial` fonts | LLM default, overused |
| `shadow-md`, `rgba(0,0,0,0.3)` | Harsh, template-like |
| `linear`, `ease-in-out` transitions | Robotic, not organic |
| 3-column Bootstrap grids | Template layout |
| Purple gradients | AI-generated signal |
| Generic Lucide/FontAwesome icons | Thick-stroked, heavy |

---

## Architecture

```
design-skill-pack/
├── .codex-plugin/
│   └── plugin.json           # Plugin manifest (name, version, skills path)
├── skills/                    # Individual skill files (Markdown)
│   ├── design-system-master.md
│   ├── amazon-ad-console-redesign.md
│   └── ... (more skills to add)
├── docs/
│   ├── SKILL-CATALOG.md       # Full catalog with descriptions
│   ├── ARCHITECTURE.md        # Plugin architecture deep-dive
│   ├── CONTRIBUTING.md        # How to contribute skills
│   └── guides/                # Usage tutorials
├── examples/                  # Example implementations
├── scripts/                   # Utility scripts
├── AGENTS.md                  # Instructions for Codex agents
└── README.md                  # This file
```

---

## Contributing

See [CONTRIBUTING.md](docs/CONTRIBUTING.md) for detailed guidelines.

Short version:
1. Create `skills/<your-skill>.md` with frontmatter
2. Include: tokens, anti-patterns, layout archetypes, motion, quality gates
3. Update the catalog
4. Validate with `python3 scripts/validate.py`

---

## License

MIT — use freely, attribute appreciated.

Built for [Codex](https://github.com/openai/codex) — the open-source AI coding agent.
