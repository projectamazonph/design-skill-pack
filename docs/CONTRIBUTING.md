# Contributing

## How to Add a New Skill

### 1. Create the skill file

```
skills/your-skill-name.md
```

With frontmatter:
```markdown
---
name: your-skill-name
description: One-line description of what this skill does
---
```

### 2. Structure your content

Every design skill should include:

```markdown
## Design Tokens
```css
:root { /* colors, typography, spacing, shadows, motion */ }
```

## Anti-Patterns
- What to avoid
- Specific banned values

## Layout Archetypes
- Pattern name + description
- Mobile collapse behavior

## Component Rules
- Anatomy, states, variants
- Spacing, typography, color tokens

## Motion Guidelines
- Entry/exit animations
- Easing curves
- Reduced-motion fallback

## Quality Gates
- [ ] Testable acceptance criteria
- [ ] Accessibility checks
```

### 3. Update the catalog

Add your skill to `docs/SKILL-CATALOG.md` with:
- Name, type, description
- Key features, tokens, fonts
- Anti-patterns
- Source reference

### 4. Validate

```bash
python3 scripts/validate.py
```

### 5. Bump version

Update `version` in `.codex-plugin/plugin.json` (semver).

### 6. Update cachebuster

```bash
python3 .codex-plugin/scripts/update_plugin_cachebuster.py .
```

## Skill Quality Standards

| Criterion | Required |
|-----------|----------|
| YAML frontmatter with name + description | ✅ |
| Anti-patterns section | ✅ |
| Specific CSS tokens | ✅ |
| Mobile responsive rules | ✅ |
| Reduced-motion fallback | ✅ |
| Quality gate checklist | ✅ |
| Implementation-ready examples | ✅ |

## Code Review Checklist

- [ ] Skill has unique name (no conflicts)
- [ ] No placeholder/todo content
- [ ] Anti-patterns are specific (not generic)
- [ ] Tokens use CSS custom properties
- [ ] Mobile responsive behavior defined
- [ ] Reduced-motion alternatives provided
- [ ] Plugin validates clean
- [ ] Cachebuster updated
