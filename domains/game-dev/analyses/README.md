---
title: "Game analyses index"
description: "Hub of per-title analysis packs (pitch, GDD, economy, teardown, playtest, postmortem)."
updated: "2026-08-10"
canonical: true
tags: [game-design, analyses, index]
audience: [intermediate, advanced]
related:
  - ../game-design/templates/game-analysis-pack-readme.md
  - ../game-design/README.md
sensitivity: public
---

# Game analyses

> [← Game Dev](../README.md) · Templates: [game-analysis-pack-readme.md](../game-design/templates/game-analysis-pack-readme.md)  
> Skill: `.cursor/skills/game-design-docs/` · Mode: **`full-pack`**  
> Routing: `meta/routing.md` topics `game.analysis_pack` · `game.design_docs` · `game.systems_teardown`

Mỗi title một folder `analyses/<slug>/` gồm đủ models (pitch · gdd · systems-economy · systems-teardown · playtest-review · postmortem).

**Quality bar (systems density):** [`_quality-bar.md`](./_quality-bar.md)

| Slug | Title | Pack status | Hub |
| --- | --- | --- | --- |
| `triangle-strategy` | Triangle Strategy | complete (playtest/postmortem = study stubs) | [triangle-strategy/](./triangle-strategy/) |
| `honkai-star-rail` | Honkai: Star Rail | **deep complete** | [honkai-star-rail/](./honkai-star-rail/) |
| `infect-them-all` | Infect Them All (series) | complete — **gold density** teardown | [infect-them-all/](./infect-them-all/) |

## Create a new pack

1. Ask agent: *“full-pack cho &lt;game&gt;”* (skill `game-design-docs`).
2. Or copy templates from `domains/game-dev/game-design/templates/`.
3. Meet **Definition of Done** in the pack hub template + density in [`_quality-bar.md`](./_quality-bar.md).
4. Add a row to this table.

## Boundary vs Games OS

| Need | Where |
| --- | --- |
| Systems / GDD / teardown (Make) | **This folder** (`domains/game-dev/analyses/`) |
| Leisure backlog / fun budget (Play) | [`guides/05-games-os/play/`](../../../guides/05-games-os/play/README.md) |
| Industry / culture news (Follow) | [`guides/05-games-os/follow/`](../../../guides/05-games-os/follow/README.md) |

## Legacy paths (redirects only)

Do **not** add new canonical analyses here:

| Legacy | Points to |
| --- | --- |
| `domains/game-dev/pitches/*` | pack `pitch.md` |
| `domains/game-dev/design/<title>-gdd.md` | pack `gdd.md` |
| `domains/game-dev/case-studies/<title>-systems-teardown.md` | pack `systems-teardown.md` |

Make analyses stay under **Make** (`domains/game-dev/`). Leisure taste / backlog → `guides/05-games-os/play/`.
