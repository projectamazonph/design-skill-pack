# Design Skill Pack — Agent Instructions

This repo contains the **Design Skill Pack** — a Codex plugin bundling 20+ premium design skills.

## Structure

```
design-skill-pack/
├── .codex-plugin/plugin.json    # Plugin manifest (required)
├── skills/                       # Skill files
│   ├── design-system-master.md   # Master orchestrator (primary skill)
│   └── amazon-ad-console-redesign.md  # Example project-specific redesign
├── docs/                         # Documentation
│   ├── SKILL-CATALOG.md          # Full catalog of bundled skills
│   ├── ARCHITECTURE.md           # Plugin architecture
│   ├── CONTRIBUTING.md           # How to add new skills
│   └── guides/                   # Usage guides
├── examples/                     # Example outputs
├── scripts/                      # Utility scripts
└── README.md                     # This file
```

## How to Use

1. **Install the plugin:**
   ```bash
   codex plugin install design-skill-pack
   ```
   Or via the Codex UI: Plugins → Design Skill Pack → Install

2. **Use a specific skill:**
   ```bash
   @Design Skill Pack <skill-name>
   ```
   Example: `@Design Skill Pack hallmark redesign src/app/landing`

3. **Use the master orchestrator:**
   ```bash
   @Design Skill Pack design-system-master
   ```
   The orchestrator auto-selects the right skill combination based on your project type.

## When to Use Each Skill

| You want... | Use this skill |
|-------------|---------------|
| Anti-AI-slop design with structural variety | `hallmark` |
| Awwwards-tier agency aesthetics | `high-end-visual-design` |
| Apple-inspired precision | `premium` |
| Magazine editorial layouts | `editorial` |
| Clean minimalist interfaces | `sleek` or `minimal` |
| Frosted glass effects | `glassmorphism` |
| Bold high-contrast design | `neobrutalism` |
| Warm beige calm systems | `clean-minimal-beige-light-mode` |
| Technical split-screen | `split-layout-technical` |
| Agency nested shells | `nested-container-clean-agency` |
| Editorial-poster aesthetic | `impeccable` |
| Polished business-ready | `professional` |
| High-conversion landing pages | `landing-page` |
| Pricing page expertise | `pricing-page` |
| Design quality audit/scoring | `styleseed-design-review` |
| Upgrade existing UIs | `redesign-existing-projects` |
| Design inference & anti-default | `design-taste-frontend` |
| Layered shadows | `beautiful-shadows` |
| Word-by-word animations | `staggered-word-reveal` |
| Scroll-triggered animations | `animation-on-scroll` |
| Don't know which to pick | `design-system-master` (orchestrator) |

## Adding a New Skill

1. Create `skills/<your-skill-name>.md` with frontmatter (name, description)
2. Follow the SKILL.md structure from existing skills
3. Update docs/SKILL-CATALOG.md
4. Validate:
   ```bash
   python3 scripts/validate.py
   ```

## Conventions

- Skill files use Markdown with YAML frontmatter
- The `name` field in frontmatter is the slug used to invoke the skill
- Skills should be self-contained (readers should not need external references)
- Anti-patterns are as important as patterns
- Always include reduced-motion alternatives
