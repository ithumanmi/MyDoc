# Mode: GDD / design bible

**Job:** Living production spec so design, art, eng, narrative share one truth.  
**Not:** Pitch deck; not infinite lore dump. Prefer **thin GDD + linked system sheets**.

Template: `domains/game-dev/game-design/templates/game-gdd.md`

## Required sections

1. **Meta** — Title, genre, platforms, team, status `(locked|proposed|TBD)`.
2. **Vision & pillars** — 3 pillars + anti‑goals (what we refuse to be).
3. **Player fantasy & target** — Experience promise; session model.
4. **Core / Meta / Live loops** — Chains + win/lose/exit conditions.
5. **Systems index** — Table: system → purpose → owner → doc link / status.
6. **Progression & content** — Horizontal vs vertical; content buckets; soft/hard gates.
7. **UX / controls / FTUE** — Input map; first‑30‑min beat sheet.
8. **Narrative (if any)** — Structure only; details → narrative toolkit docs.
9. **Audio/visual direction** — Constraints that affect systems (readability, VFX budget).
10. **Tech & live constraints** — Netcode class, platform limits, LiveOps cadence if GaaS.
11. **Milestones** — Vertical slice → alpha → soft launch criteria.
12. **Open questions & changelog** — Dated decisions.

## Quality bar

| Do | Don’t |
| --- | --- |
| Spec behaviors & edge cases | Vague “fun combat” |
| Link out heavy systems (economy sheet) | Duplicate economy novel inside GDD |
| Mark status per section | Silently contradict pitch pillars |
| Keep modular | Write a 200‑page unread bible day one |

## Expansion (optional modules)

Combat · Inventory · Social · Monetization ethics · Accessibility · Localization · Analytics event list.

## Theory

- `core-loop-mastery.md`, `advanced-core-loops.md`, `metagame-design.md`
- `narrative-toolkit.md`, `level-design-flow.md`, `live-ops-design.md`
- Genre pillars: `genre-deep-dives/`
