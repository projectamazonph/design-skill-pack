# Architecture

## Overview

The Design Skill Pack is a Codex plugin that bundles 20+ individual design skills under a single plugin manifest. Each skill is a standalone Markdown file with YAML frontmatter containing executable design guidance.

```
design-skill-pack/
├── .codex-plugin/
│   └── plugin.json          # Plugin manifest — tells Codex where skills live
├── skills/                   # Individual *.md skill files
│   ├── design-system-master.md
│   └── amazon-ad-console-redesign.md
├── docs/                     # Documentation
│   ├── SKILL-CATALOG.md
│   ├── ARCHITECTURE.md
│   └── CONTRIBUTING.md
└── README.md                 # Entry point
```

## Plugin Manifest

`.codex-plugin/plugin.json` defines the plugin:

```json
{
  "name": "design-skill-pack",
  "version": "1.0.0",
  "description": "20+ premium design skills bundled...",
  "skills": "./skills/",
  "interface": {
    "displayName": "Design Skill Pack",
    "shortDescription": "20+ premium design skills bundled",
    "category": "Design",
    "capabilities": ["design-system", "ui-ux", "frontend-design", "redesign", "animation", "typography", "color-tokens", "responsive-layout"]
  }
}
```

The `skills` field points to a directory; every `.md` file in that directory becomes an invocable skill.

## Skill File Format

Each skill file must have:

```markdown
---
name: <skill-name>              # Invocation slug (required)
description: <one-liner>        # Shown in UI (required)
---

# Title

...skill content...
```

### Required Content for Design Skills

1. **Design tokens** — CSS custom properties for colors, typography, spacing, shadows, motion
2. **Anti-patterns** — What NOT to do (specific banned values/patterns)
3. **Layout archetypes** — Structure patterns (bento, editorial, split, cascade, etc.)
4. **Component rules** — Anatomy, states, variants for key components
5. **Motion guidelines** — Animation specs, easing curves, reduced-motion fallbacks
6. **Mobile responsive** — Collapse behavior below 768px
7. **Quality gates** — Testable acceptance criteria

## Orchestrator Pattern

The `design-system-master.md` skill acts as an **orchestrator** — it doesn't design itself, but reads project context and dispatches to the appropriate skill(s). Its selection matrix maps:

- Project type (SaaS, landing, portfolio, editorial, e-commerce, etc.)
- Desired aesthetic (premium, editorial, minimalist, glass, etc.)
- Primary + secondary skill recommendations

## Execution Flow

```
User Prompt → Codex loads plugin → Skill matched by name
  → Agent reads SKILL.md → Follows workflow →
  Applies tokens → Layout → Components → Motion → QA
```

For the orchestrator:
```
User Prompt → Codex loads plugin → design-system-master matched
  → Agent reads selection matrix → Picks optimal skill(s)
  → Loads selected SKILL.md → Executes as above
```

## Performance Considerations

- Skill files are Markdown — minimal parsing overhead
- No runtime dependencies — pure agent instruction
- Cachebuster versioning for updates
- Skills can reference each other across files
