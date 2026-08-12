---
name: game-design-docs
description: >-
  Produce game design documents: single modes (Pitch, GDD, Systems/economy,
  Postmortem, Playtest/review) or full-pack analysis folder for one title
  (all six models + systems teardown). Use when the user asks to pitch, write a
  GDD, economy model, postmortem, playtest, review checklist, phân tích game,
  full dossier, analysis pack, or "tất cả models" for a game. Prefer full-pack
  when analyzing a whole title. Prefer this over ad-hoc docs. Teardown-only
  essays can also use skill game-systems-teardown.
---

# Game design docs (hub)

Modes for **forward design** (your project) and **title analysis packs** (shipped or WIP games).

**Sibling skill:** deep teardown essay only → `game-systems-teardown` (also included inside `full-pack`).

**Index:** `domains/game-dev/analyses/README.md`

## Before writing

1. **Pick mode** (ask if unclear):

| Mode id | Triggers | Template / output |
| --- | --- | --- |
| `full-pack` | phân tích game, full dossier, analysis pack, tất cả models, cover everything | Hub + 6 files — see `modes/full-pack.md` |
| `pitch` | pitch, one-pager | `domains/game-dev/game-design/templates/game-pitch-one-pager.md` |
| `gdd` | GDD, design bible | `…/game-gdd.md` |
| `systems-economy` | systems map, economy, sources/sinks | `…/game-systems-map-economy.md` |
| `postmortem` | postmortem, retro | `…/game-postmortem.md` |
| `playtest-review` | playtest, build review | `…/game-playtest-review.md` |

2. Read `modes/<mode>.md` (required sections + quality bar).
3. Theory hubs under `domains/game-dev/game-design/` as needed (loops, economy, psyche, live-ops, playtest, genre-deep-dives).
4. Match user language (VI/EN). Prefer tables. Tag evidence.

## Default: full-pack when analyzing a title

If the user names a **game title** and wants analysis/docs without specifying a single mode → run **`full-pack`**.

**Canonical folder:**

```text
domains/game-dev/analyses/<slug>/
  README.md              # hub index + status matrix + DoD
  pitch.md
  gdd.md
  systems-economy.md
  systems-teardown.md    # via game-systems-teardown quality bar
  playtest-review.md
  postmortem.md
```

Hub template: `domains/game-dev/game-design/templates/game-analysis-pack-readme.md`

### Full-pack fill policy

| Artifact | Shipped title (study) | Own project |
| --- | --- | --- |
| Pitch / GDD / Economy / Teardown | Reconstruct from play; tag `(observed)`/`(inferred)` | Spec as `(proposed)`/`(locked)` |
| Playtest-review | Study protocol **or** blank TBD scores | Real protocol + findings |
| Postmortem | Public/study retro **or** stub `(TBD)` — never invent metrics | Real blameless retro |

Density for teardown/economy: `domains/game-dev/analyses/_quality-bar.md`.

Never invent D1/D7, revenue, or fake review scores.

### Definition of Done (full-pack)

Pack is incomplete until **all** are true:

- [ ] Folder `analyses/<slug>/` exists
- [ ] `README.md` hub with thesis + status matrix
- [ ] All six model files present (stub OK for playtest/postmortem)
- [ ] Pitch · GDD · economy · teardown marked `filled` (or honest `partial` with why)
- [ ] Every file links back to `./README.md`
- [ ] Row added/updated in `analyses/README.md`
- [ ] No parallel canonical copies under `pitches/` / `design/` / `case-studies/` (redirect stubs only)

## Shared quality rules

| Do | Don’t |
| --- | --- |
| State audience + decision the doc enables | Dump lore as design |
| Separate Core / Meta / Live | Mix shop into core loop |
| Mark `(TBD)` / `(assumed)` | Fake live KPIs |
| Link siblings inside the pack | Scatter files without hub |
| Cite theory paths in footers | Put Make analyses under Games OS Play/Follow |

## Mode quick map (single)

1. **Pitch** — why this game (~1–2 pages).
2. **GDD** — thin living bible + systems index.
3. **Systems/economy** — currencies, source/sink, gates, KPIs.
4. **Postmortem** — facts → causes → lessons → actions.
5. **Playtest/review** — protocol + scores → actions.
6. **full-pack** — all of the above + **systems-teardown** in one folder.

## After / save

**Rule:** One title → one pack. Always prefer `domains/game-dev/analyses/<slug>/`.

| Situation | Path |
| --- | --- |
| `full-pack` or “phân tích &lt;game&gt;” | Create/update `analyses/<slug>/` (required) |
| Single mode + pack exists | Write/update file **inside that pack** |
| Single mode + no pack yet | Create pack folder + hub (stub siblings) **or** ask to run `full-pack`; do **not** invent new canonical files under `pitches/` / `design/` |
| Teardown-only | `analyses/<slug>/systems-teardown.md` (+ hub row). Legacy `case-studies/` = redirect only |
| Legacy paths `pitches/`, `design/<title>-*.md` | Redirect stubs pointing at pack — never second source of truth |

Update the pack `README.md` status matrix whenever a file is added/filled.

## Anti-patterns

- Creating pitch + GDD + teardown in three unrelated folders for the same title without a pack hub
- full-pack with empty decorative files and no hub status / failing DoD
- Using playtest scores you did not collect
- Confusing leisure taste notes (`guides/05-games-os/play/`) with Make analysis packs
