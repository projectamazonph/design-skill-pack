# Quick Start Guide

## Install

```bash
# From Codex marketplace
codex plugin install design-skill-pack

# Or from local checkout
codex plugin install /path/to/design-skill-pack
```

## Invoke a Skill

In your Codex prompt, reference the plugin and skill:

```
@Design Skill Pack premium
```

Or for a specific task:

```
@Design Skill Pack hallmark redesign src/components/Hero.tsx
```

## Common Workflows

### 1. Redesign an Existing Page
```
@Design Skill Pack hallmark redesign src/app/landing/page.tsx
```
This audits the current design, picks a theme, and restructures the visual layer.

### 2. Add Premium Polish
```
@Design Skill Pack premium
@Design Skill Pack beautiful-shadows
@Design Skill Pack animation-on-scroll
```

### 3. Build a Landing Page From Scratch
```
@Design Skill Pack design-system-master
```
The orchestrator reads your project type and picks the best skill combo.

### 4. Design a Pricing Page
```
@Design Skill Pack pricing-page
@Design Skill Pack premium
```

### 5. Audit Design Quality
```
@Design Skill Pack styleseed-design-review
```

## Tips

- **Combine skills**: Layer utility skills (beautiful-shadows, staggered-word-reveal) on top of design system skills (premium, editorial)
- **Use the orchestrator**: When unsure, `design-system-master` is the safest starting point
- **Override dials**: For `design-taste-frontend`, set explicit DESIGN_VARIANCE, MOTION_INTENSITY, VISUAL_DENSITY values
- **Study existing designs**: Use `hallmark study <URL>` to extract design DNA from any page
