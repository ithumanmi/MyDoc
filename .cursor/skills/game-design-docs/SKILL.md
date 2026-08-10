---
name: game-design-docs
description: >-
  Produce game design documents in one of five modes: Pitch/one-pager, GDD/design
  bible, Systems map/economy model, Postmortem, or Playtest/review checklist.
  Use when the user asks to write a pitch, one-pager, GDD, design bible, systems
  map, economy model, postmortem, playtest plan, or build review checklist.
  Prefer this over ad-hoc docs. For reverse-engineering an existing shipped title,
  use skill game-systems-teardown instead.
---

# Game design docs (hub)

One skill, **five modes**. Output is a **prescriptive or evaluative design artifact** for *your* project — not a feature laundry list and not a store-page blurb.

**Sibling:** reverse-reading an existing game → skill `game-systems-teardown` + template `domains/game-dev/game-design/templates/game-systems-teardown.md`.

## Before writing

1. **Pick mode** (ask if unclear):

| Mode id | Triggers | Template |
| --- | --- | --- |
| `pitch` | pitch, one-pager, elevator, fund deck lite | `domains/game-dev/game-design/templates/game-pitch-one-pager.md` |
| `gdd` | GDD, design bible, design doc, feature spec pack | `…/game-gdd.md` |
| `systems-economy` | systems map, economy model, sources/sinks, currency | `…/game-systems-map-economy.md` |
| `postmortem` | postmortem, retro, after-action, ship postmortem | `…/game-postmortem.md` |
| `playtest-review` | playtest plan, review checklist, build review | `…/game-playtest-review.md` |

2. Read the mode file under `modes/<mode>.md` in this skill (required sections + quality bar).
3. Open theory hubs as needed (paths under `domains/game-dev/game-design/`):
   - Loop/meta: `core-loop-mastery.md`, `advanced-core-loops.md`, `metagame-design.md`
   - Economy: `economy-systems.md`, `game-economics-monetization.md`, `balancing-methodology.md`
   - Psyche: `player-psychology.md`
   - LiveOps: `live-ops-design.md`
   - Playtest/review: `playtest-framework.md`, `checklist-game-review.md`, `game-review-checklist.md`
   - Genre: `genre-deep-dives/`
4. Match user language (VI/EN). Keep headings sharp. Prefer tables.

## Shared quality rules

| Do | Don’t |
| --- | --- |
| State **audience** + **decision this doc enables** | Dump lore as design |
| Separate **Core / Meta / Live** when relevant | Mix shop UI into core loop |
| Name tradeoffs and open risks | Fake D1/D7, revenue, or playtest scores |
| Mark unknowns `(TBD)` / assumptions `(assumed)` | Pretend WIP sections are locked |
| Cite Docs theory paths in a short footer | Invent studio process as fact |
| Offer save path under `domains/game-dev/` when asked | Put Make analyses under Games OS Play/Follow |

**Evidence / status tags:** `(locked)` · `(proposed)` · `(assumed)` · `(TBD)` · for playtest findings `(observed)`.

## Mode quick map

1. **Pitch** — Sell *why this game*: fantasy, player, USP, loop in 1 breath, scope & risk. Max ~1–2 pages.
2. **GDD** — Living spec: pillars → loops → systems → content → tech/live constraints → open questions. Prefer modular sections over encyclopedias.
3. **Systems map / economy** — Diagrammable loops + currency taxonomy + source/sink + progression curve + anti-inflation + KPI to watch. Numbers as models, not truth.
4. **Postmortem** — What happened / why / lessons / next experiments. Blameless; separate facts from interpretations.
5. **Playtest / review** — Goal → protocol → metrics/survey → insight → scored checklist + actions. Align with `playtest-framework.md` + review checklists.

## Output craft

- Lead with doc metadata (title, owner, status, date, mode).
- Fill the matching template structure; omit empty ornamental sections rather than padding.
- Length: Pitch short; GDD modular (start thin); Economy concrete tables; Postmortem 1 sitting; Playtest actionable in one sprint.
- If critical inputs missing: ask 1–3 blocking questions **or** write with `(TBD)` and an “Open questions” section — do not stall forever.

## After / save (if user wants it in Docs)

| Mode | Suggested path |
| --- | --- |
| Pitch | `domains/game-dev/pitches/<slug>-pitch.md` |
| GDD | `domains/game-dev/design/<slug>-gdd.md` |
| Systems/economy | `domains/game-dev/design/<slug>-economy.md` |
| Postmortem | `domains/game-dev/postmortems/<slug>-postmortem.md` |
| Playtest/review | `domains/game-dev/playtests/<slug>-playtest-<date>.md` |

Create folders only when saving. Link related theory in a short footer.

## Anti-patterns

- Using this skill to teardown *another studio’s shipped game* → use `game-systems-teardown`
- GDD that is only a feature backlog with no pillars/loop
- Economy doc without sinks
- Postmortem that only blames people or tools with no systemic cause
- Playtest checklist with scores but no **actions + owners**
