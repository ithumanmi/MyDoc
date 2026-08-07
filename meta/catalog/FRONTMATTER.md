# Frontmatter schema (recommended)

Apply to **new** docs and when touching hubs / canonical deep-dives.

```yaml
---
title: "Human readable title"
description: "One-line summary for agents & search"
updated: "YYYY-MM-DD"
canonical: true          # true only for preferred source of a topic
tags: [domain, subtopic]
audience: [beginner, intermediate, advanced]  # subset ok
related:
  - relative/path/to/other.md
sensitivity: public      # or private (personal/*)
---
```

## Rules
- `canonical: true` ≤ 1 primary doc per topic id in `topics.yaml`.
- Keep `description` ≤ 160 chars.
- Do not put secrets in frontmatter.
- Long deep-dives: also add an **Agent SUMMARY** section (5–12 bullets) immediately after the H1 / breadcrumb.
