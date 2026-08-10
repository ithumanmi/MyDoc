---
title: "Honkai: Star Rail — GDD (reconstructed thin bible)"
description: "Thin GDD: Paths, Break/SP combat, Trailblaze Power, endgame cycles, gacha meta."
updated: "2026-08-10"
canonical: false
tags: [game-design, gdd, gaas, analysis-pack]
audience: [intermediate, advanced]
related:
  - ./README.md
  - ./pitch.md
  - ./systems-economy.md
  - ./systems-teardown.md
sensitivity: public
---

# Honkai: Star Rail — GDD / design bible

> [← Pack](./README.md) · [Pitch](./pitch.md) · Mode: `gdd`  
> Thin GDD **tái dựng** — teaching reference, không phải tài liệu studio.

| Field | Value |
| --- | --- |
| Title | Honkai: Star Rail |
| Genre / platforms | Turn-based RPG · Mobile + PC · GaaS `(locked)` |
| Doc status | Reconstructed `(proposed)` |
| Linked pitch | [pitch.md](./pitch.md) |
| Linked economy | [systems-economy.md](./systems-economy.md) |

---

## 1. Vision & pillars

- **Vision:** Voyage fantasy + tactical team puzzle mỗi trận; collection Path/aeon identity; LiveOps giữ “lịch vũ trụ” sống. `(assumed)`
- **Pillars:** Shared SP · Break windows · Roster breadth via cycles (xem pitch).
- **Anti‑goals:** Mandatory precision action; single permanent endgame team; story paywall tường minh. `(assumed)`

---

## 2. Player fantasy & target

- **Fantasy:** Nameless Trailblazer; build iconic characters (Ultimate spectacle). `(locked)`
- **Target:** Hoyoverse + gacha RPG audience; F2P viable ceiling vs whale mirror clears. `(assumed)`
- **Session:** Dailies short; story/events medium; endgame puzzle long. `(observed)`

---

## 3. Loops — Core / Meta / Live

| Layer | Chain | Win / fail / exit |
| --- | --- | --- |
| Core | Weakness → SP → Break → Burst → Stabilize | Win: clear; Fail: wipe / timer (endgame) |
| Meta | Level/Traces/LC/Relics/comps · TB Level | Gates: Equilibrium, story walls |
| Live | TB Power · Events · MoC/PF/AS · Banners · BP | Cycle refresh; FOMO limited |

Simulated Universe = meta-in-mode (roguelite build lab). `(observed)`

---

## 4. Systems index

| System | Purpose | Detail | Status |
| --- | --- | --- | --- |
| Elements + Toughness/Break | Combat puzzle gate | Teardown | `(locked)` |
| Skill Points (team) | Action tradeoff | Teardown axes | `(locked)` |
| Paths (Hunt, Destruction, …) | Role fantasy / kit framing | GDD combat | `(locked)` |
| Light Cones | Vertical weapon analog | Economy | `(locked)` |
| Relics | Infinite vertical sink | Economy | `(locked)` |
| Trailblaze Power | Stamina faucet | Economy | `(locked)` |
| Gacha + pity | Horizontal acquisition | Economy · [GI sister](../../case-studies/genshin-gacha-economy.md) | `(locked)` |
| Endgame cycles | Anti one-team | Teardown | `(locked)` |
| SU / variants | Build sandbox | Meta-in-mode | `(locked)` |

---

## 5. Progression & content

- **Horizontal:** New characters, cones, worlds, SU modes. `(locked)`
- **Vertical:** Levels, ascension, traces, relics, eidolons. `(locked)`
- **Soft gates:** Equilibrium / World Level; gear for story elites. `(locked)`
- **Hard-ish:** Endgame star thresholds; limited banner FOMO (account strength pacing). `(inferred)`
- **Buckets:** Trailblaze story · Companions · SU · Echo weekly · MoC/PF/AS · Events.

---

## 6. UX / controls / FTUE

- Turn menu + weakness icons + turn order bar + SP pips. `(locked)`
- First sessions: teach Break then SP greed then Auto for farm. `(assumed)`
- HUD: Toughness bar co-equal with HP for elites. `(observed)`

---

## 7. Narrative (structure)

- Episodic planet arcs on Express voyage; companion quests; lore codex heavy. `(locked)`
- Structure details → external wiki · [narrative-toolkit.md](../../game-design/narrative-toolkit.md)

---

## 8. A/V constraints

- Ultimate animation budget vs combat readability (numbers + bars). `(assumed)`
- Auto must remain trustable for farm. `(observed)`

---

## 9. Tech & live

- Online GaaS; account cloud; LiveOps calendar mandatory. `(locked)`
- See [live-ops-design.md](../../game-design/live-ops-design.md)

---

## 10. Milestones (study / inspired project)

| Gate | Exit criteria |
| --- | --- |
| Vertical slice | Break+SP readable; one stamina day loop; one pity fantasy explained |
| Soft launch | Dailies + one endgame mode + banner economy tuned |
| Live year-1 | Cycle cadence stable; roster tax without toxic FOMO floor `(proposed ethics)` |

---

## 11. Open questions

- Remembrance/summon impact on SP puzzle `(TBD patch)`  
- Relic QoL roadmap vs sink intentionality  
- Cross-title Hoyoverse fatigue  

---

## Optional — Combat (thin)

Team of 4; Basic/Skill/Ult/Technique; shared SP; Toughness Break; follow Path kits; Auto optional. Edge: crowd control, shields, DoT, summon extras. `(locked)` / verify kits `(TBD)`

---

Pack: [systems-teardown.md](./systems-teardown.md) · [systems-economy.md](./systems-economy.md) · Theory: [advanced-core-loops.md](../../game-design/advanced-core-loops.md) · [metagame-design.md](../../game-design/metagame-design.md)
