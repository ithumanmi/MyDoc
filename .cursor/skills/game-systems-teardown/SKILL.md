---
name: game-systems-teardown
description: >-
  Produce high-quality systems-design essays for any game or genre (core/meta
  loops, feedback physics, tradeoff axes, balance tiers, economy/monetization
  friction, UX/psychology). Use when the user asks to analyze, teardown,
  reverse-engineer, or write a design reading of a game like the Infect Them
  All exponential-growth style. Prefer this over shallow feature lists.
---

# Game systems teardown

Write **systems essays**, not store-page summaries. Quality bar: named mechanisms, phase physics, opposing axes with costs, escalation model, economy sinks, UX under density — like a strong Infect Them All analysis.

**Sibling (forward design + full title packs):** skill `game-design-docs` — modes Pitch · GDD · Systems/economy · Postmortem · Playtest/review · **`full-pack`** (`domains/game-dev/analyses/<slug>/`).  
When the user asks to phân tích a whole game / tất cả models → prefer **`full-pack`** (includes this teardown as `systems-teardown.md`).

## Before writing

1. Identify **genre family** + platform + economy type (premium / freemium / GaaS / live).
2. Play, VODs, or wiki enough to ground claims. Label **observed** vs **inferred**.
3. Open theory hubs when needed:
   - Core/meta: `domains/game-dev/game-design/advanced-core-loops.md`, `core-loop-mastery.md`
   - Economy: `economy-systems.md`, `game-economics-monetization.md`
   - Psyche: `player-psychology.md`
   - LiveOps: `live-ops-design.md`
   - Genre pillars: `domains/game-dev/game-design/genre-deep-dives/`
   - Score checklist (optional): `checklist-game-review.md`
4. Copy structure from template: `domains/game-dev/game-design/templates/game-systems-teardown.md`

## Essay skeleton (required sections)

Use Vietnamese or English to match the user. Keep headings sharp.

1. **Pitch / role inversion** — What does this game *flip* vs genre norms? One thesis sentence.
2. **Loop physics** — Core actions as a chain; positive/negative feedback; **phases** (early / tipping / late) with player agency change (high control → spectacle).
3. **Systems map** — Core loop (in-session) · Meta loop (progress) · Live/retention hooks (modes that diversify session length).
4. **Decision axes** — 1–3 binary or opposing choices (e.g. Bite vs Eat). Each: + / − / when rational.
5. **Escalation & balance** — How power growth is answered (enemy tiers, soft gates, soft/hard currency walls). Name the anti–power-creep lever.
6. **Economy & monetization friction** — Sources/sinks; where grinding wall / IAP pressure appears; ethics note if extractive.
7. **UX & psychology** — Controls, FTUE, visual hierarchy under clutter; agency vs fatigue across session.
8. **Transfer notes** — What *pattern* ports to other games; what is title-specific.
9. **Open questions / verify** — What you’d measure (telemetry) or re-play to harden claims.

## Quality rules

| Do | Don’t |
| --- | --- |
| Name systems (“Health Decay”, “Tipping Point”) | Vague “gameplay is addictive” |
| Show **tradeoffs** (both options costly) | Only list features |
| Tie mobile/console pacing to agency curve | Paste lore as design |
| Separate Core vs Meta vs Live | Mix shop UI into core loop |
| Genre-adapt questions (see below) | Force “infect” metaphor onto every game |
| Cite Docs paths when using theory | Invent retention numbers |

**Evidence tags** inline: `(observed)` · `(inferred)` · `(common genre pattern)`.

## Genre adapters (ask these instead of forcing one template)

| Genre family | Extra probes |
| --- | --- |
| Action / arcade / infection | Unit count tipping; density UX; bite-length tradeoffs |
| Idle / incremental | Soft-reset; prestige; offline progress ethics |
| Roguelike / roguelite | Run vs meta; death tax; build identity |
| Puzzle | First-48h fail points; hint economy; level scoped difficulty |
| Shooter / extraction | Loadout risk; circle/pressure; inventory entropy |
| Strategy / 4X / auto-battler | Fog/tempo; counters; snowball brakes |
| RPG / ARPG | Vertical vs horizontal power; loot sinks |
| GaaS / live service | Battle pass cadence; FOMO; catch-up |
| Social deduction / party | Information asymmetry; round reset |
| Sports / racing | Assist systems; rubber-banding honesty |

## Output craft

- Lead with thesis; then sections 2→7; end with transfer + open questions.
- Prefer tables for axes, tiers, loops.
- Length guide: ~800–2000 words for one title; longer only if multi-mode deep dive.
- If data missing: write the **mechanism hypothesis** and list verification steps — never fake D1/D7.

## After / save (if user wants it in Docs)

- Case study path suggestion: `domains/game-dev/case-studies/<slug>-systems-teardown.md` or under Games OS Follow only if culture/news — **Make** analyses stay in `domains/game-dev/`.
- Link related theory modules in a short “Theory refs” footer.

## Anti-patterns

- Feature laundry list without feedback physics
- Monetization rant without sink/source map
- Copying Infect Them All sections onto a game that has no growth loop — pick the real loop physics instead
- Confusing play-taste review with systems teardown (leisure taste → `guides/05-games-os/play/`)
