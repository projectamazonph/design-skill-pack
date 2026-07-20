#!/usr/bin/env python3
"""Validate the Design Skill Pack structure and skill files."""

import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent

errors = []
warnings = []

def check(path, condition, msg):
    if not condition:
        errors.append(f"{path}: {msg}")

def warn(path, msg):
    warnings.append(f"{path}: {msg}")

# 1. Check manifest
manifest = ROOT / '.codex-plugin' / 'plugin.json'
check('plugin.json', manifest.exists(), "Missing plugin.json")
if manifest.exists():
    import json
    data = json.loads(manifest.read_text())
    check('plugin.json', 'name' in data, "Missing 'name'")
    check('plugin.json', 'skills' in data, "Missing 'skills' field")
    check('plugin.json', data.get('skills') == './skills/', "Skills should point to './skills/'")

# 2. Check skills directory
skills_dir = ROOT / 'skills'
check('skills/', skills_dir.is_dir(), "Missing skills directory")
if skills_dir.is_dir():
    md_files = list(skills_dir.glob('*.md'))
    check('skills/', len(md_files) > 0, "No .md files in skills/")
    for f in md_files:
        content = f.read_text()
        check(f.name, '---' in content, "Missing YAML frontmatter (---)")
        if content.startswith('---'):
            # Extract frontmatter
            parts = content.split('---', 2)
            if len(parts) >= 2:
                fm = parts[1]
                check(f.name, 'name:' in fm, "Missing 'name:' in frontmatter")
                check(f.name, 'description:' in fm, "Missing 'description:' in frontmatter")

# 3. Check docs
docs_dir = ROOT / 'docs'
check('docs/', docs_dir.is_dir(), "Missing docs/ directory")
if docs_dir.is_dir():
    for doc in ['ARCHITECTURE.md', 'CONTRIBUTING.md', 'SKILL-CATALOG.md']:
        check(f'docs/{doc}', (docs_dir / doc).exists(), f"Missing {doc}")

# 4. Check README
check('README.md', (ROOT / 'README.md').exists(), "Missing README.md")

# Summary
if errors:
    print(f"❌ {len(errors)} error(s):")
    for e in errors:
        print(f"  - {e}")
    sys.exit(1)

if warnings:
    print(f"⚠️  {len(warnings)} warning(s):")
    for w in warnings:
        print(f"  - {w}")

print(f"✅ All checks passed ({len(list(skills_dir.glob('*.md'))) if skills_dir.is_dir() else 0} skill files)")
sys.exit(0)
