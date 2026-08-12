---
title: "Honkai: Star Rail — GDD (deep reconstructed)"
description: "Deep living bible: combat, Paths, endgame triad, LiveOps, progression, FTUE modules."
updated: "2026-08-10"
canonical: false
tags: [gdd, gaas, deep, analysis-pack]
audience: [intermediate, advanced]
related:
  - ./README.md
  - ./pitch.md
  - ./systems-economy.md
  - ./systems-teardown.md
sensitivity: public
---

# Honkai: Star Rail — GDD / design bible (deep)

> [← Pack](./README.md) · [Pitch](./pitch.md) · [Teardown](./systems-teardown.md) · [Economy](./systems-economy.md)  
> Thin-in-structure, **deep-in-modules**. Status: `(locked)` = ship-observed · `(proposed)` = study · `(TBD)` = patch-verify.

| Field | Value |
| --- | --- |
| Title | Honkai: Star Rail |
| Platforms | iOS / Android / PC (cloud adjacent) `(locked)` |
| Economy model | GaaS freemium + gacha `(locked)` |
| Doc owner | Docs reconstructed study |

---

## 1. Vision & pillars

**Vision:** Người chơi cảm thấy mình là **nhà chiến thuật du hành** — mỗi trận là puzzle tài nguyên (SP/Break), mỗi tuần là lịch vũ trụ LiveOps, mỗi patch là hành tinh/ý niệm Path mới. `(assumed)`

**Pillars:** Shared SP · Break phases · Roster breadth via multi-exam endgame.  
**Anti‑goals:** Mandatory twitch aim; single eternal team; story paywall tường minh.

---

## 2. Player fantasy & segments

| Segment | Fantasy | Core need |
| --- | --- | --- |
| Story tourist | Express voyage, cast | Readable combat, skippable farm |
| F2P clearer | “Tôi cũng clear cycle” | Fair exams + durable free units |
| Optimizer | Mirror / 0-cycle adjacent | Deep kits, relic EV |
| Collector | Path / aesthetics | Banners, skins/BP |

Session model: **short daily faucet** + **medium narrative** + **long exam blocks**. `(observed)`

---

## 3. Loops

| Layer | Chain | Win / fail |
| --- | --- | --- |
| Core | Weakness → SP → Break → Burst → Stabilize | Clear / wipe / timeout |
| Meta | Power → mats/relics → traces/sets → teams | Soft Equilibrium walls |
| Live | Version → events → banners → cycle exams | FOMO miss; jade left on table |
| Meta-in-mode | SU run → blessings → bosses | Experiment failure cheap |

---

## 4. Systems index

| System | Purpose | Owner lens | Deep doc |
| --- | --- | --- | --- |
| Elements | Matchup puzzle | Combat | §A |
| Toughness / Break | Phase gate | Combat | §A · Teardown |
| Skill Points (0–5 typical team pool) | Action economy | Combat | §A |
| Energy / Ult | Burst cadence | Combat | §A |
| Paths | Fantasy + design vocabulary | System | §A |
| Technique | Overworld opener | Combat/UX | §A |
| Light Cones | Vertical weapon | Progress | Economy |
| Relics (planar + cavern sets) | Infinite chase | Progress | Economy |
| Traces / ascension | Deterministic vertical | Progress | Economy |
| Gacha + pity | Horizontal acquire | LiveOps | Economy · GI sister |
| Trailblaze Power | Time faucet | LiveOps | Economy |
| Equilibrium / TB Level | Soft wall | Progress | §B |
| Simulated Universe family | Lab / rewards | Meta-mode | §C |
| Echo of War | Weekly boss sink | LiveOps | §C |
| MoC / PF / AS (+ Starward opt.) | Orthogonal exams | LiveOps | §C · Teardown |
| Events / BP | Jade & engagement | LiveOps | §C |
| Auto-battle | Farm contract | UX | §D |

---

## 5. Progression & content buckets

**Horizontal:** Characters, cones, Planar ornaments/sets, SU variants, story planets, Modes.  
**Vertical:** Level, ascension, traces, relics, eidolons, LC levels.  
**Soft gates:** Equilibrium enemies; underbuilt traces.  
**Exam gates:** Star thresholds / scores for jade.  
**Buckets:** Trailblaze Missions · companion · exploration puzzles · SU · weekly · endgame triad · limited events · Forgotten Hall predecessors / related memory content as evolves `(TBD naming history)`.

---

## 6. Module A — Combat (deep)

### A.1 Battle rules (structural)

- Party size **4**; turn order from SPD + modifiers `(locked)`.
- Actions: **Basic** (usually +SP), **Skill** (usually −SP), **Ultimate** (energy), **Technique** pre-fight `(locked)`.
- Shared **Skill Point** pool — core tradeoff axis `(locked)`.
- Enemies: HP + **Toughness** bar with element weaknesses; Break applies vulnerability / action delay class effects `(locked)`.
- Optional **Auto** toggles AI for actions `(locked)`.

### A.2 Path vocabulary (design roles — kits may mix)

| Path (examples) | Design intent (simplified) |
| --- | --- |
| Hunt | Single-target pressure |
| Destruction | Blast / big hits |
| Erudition | AoE / PF affinity |
| Harmony | Buff / SP ecology |
| Nihility | Debuff / DoT |
| Preservation | Shields / mitigation |
| Abundance | Heal / cleanse |
| Remembrance / others | Summon / new verbs — evolving cast `(TBD)` |

Paths là **ngôn ngữ fantasy**, không phải cast iron class — kit thực tế có hybrid. `(inferred)`

### A.3 Win conditions by content

| Content | Focus |
| --- | --- |
| Story / calyx | Survive + clear |
| MoC | Clear both (or more) sides within **cycle** budget `(observed)` |
| PF | Maximize **points** via waves/kills in cycle budget `(observed)` |
| AS | Exploit **Break** on specific bosses for score `(observed)` |

### A.4 Edge cases

CC chains, cleanse races, summons/follow-ups diverting SP, Break efficiency vs HP races, Energy starvation, Toughness lock on wrong element.

---

## 7. Module B — Account progression

| Gate | Player sees | Design job |
| --- | --- | --- |
| Trailblaze Level | Account XP | Unlock systems |
| Equilibrium | Enemy scaling | Force Power sinks before story |
| Ascension materials | Planet/dungeon gated | Travel fantasy + Power |
| Trace nodes | Skill trees | Deterministic invest |
| Relic main → sub | RNG layers | Long-tail engagement |

Rule of thumb study: **finish traces for exam cores before bottomless relic** for most F2P clears. `(assumed)`

---

## 8. Module C — LiveOps & endgame triad

### C.1 Calendar spine

Version patches → story/event banner → endgame line-up rotate (~**six-week** phase commonly documented) → jade income pulse. `(observed)` Confirm server timers in UI.

### C.2 Exam design goals

| Mode | Skill exam | Rewards job |
| --- | --- | --- |
| Memory of Chaos | Dual-core ST + sustain under cycle buffs | Recurring jade |
| Pure Fiction | AoE / follow-up clear speed & points | Recurring jade |
| Apocalyptic Shadow | Break precision | Recurring jade |

**Starward (optional evolution):** adds extra node / scoring lane → **third team tax** for players chasing extra rewards — optional, increases whale/optimizer ceiling without mandatory wipe of base jade path (verify live). `(observed` community explainers`)`

### C.3 Simulated Universe

Roguelite blessings + planar rewards + narrative segments — **sandbox** trước khi mang build vào exams. `(observed)`

### C.4 Ethics notes for inspired projects

Cycle FOMO OK if: (1) base jade reachable without pay, (2) skip banners without soft-lock story, (3) multiple valid comps including older units for mid tiers. `(proposed)`

---

## 9. Module D — UX / FTUE / Auto

**FTUE beat sheet (study):** Move/attack → weakness icon → Skill costs SP → Basic refunds → Elite Toughness → first Break celebration → introduce Ult → later teach Auto for farm. `(assumed)`

**HUD priorities:** Turn order · SP · Toughness · HP · enemy intent.  
**Auto policy:** Allowed farm; endgame prefer Manual for mastery/jade honesty. `(observed)`

---

## 10. Narrative (structure only)

Episodic **planet/arc** storytelling; Aeon/Path mythology; companion quests; Express as hub. Tone often switches humor ↔ tragedy. Details → wikis · [narrative-toolkit.md](../../game-design/narrative-toolkit.md).

---

## 11. A/V constraints

Ult animations = fantasy payoff but must not obscure Toughness/SP state forever (skip Ult options matter). `(assumed)` Density of floating numbers vs readability.

---

## 12. Tech & platform

Always-online account; shared progress mobile↔PC; LiveOps remote config; performance for Autobattle idle. `(locked)`

---

## 13. Milestones (for inspired clone)

| Gate | Exit |
| --- | --- |
| Slice | Players name Break + SP unprompted |
| Soft launch | One exam mode + Power day + pity explained |
| Live Year-1 | ≥2 orthogonal exams; FOMO policy doc signed |

---

## 14. Open questions / changelog

| Date | Note |
| --- | --- |
| 2026-08-10 | Deep GDD pass; Starward noted as optional layer — verify exact rules per mode `(TBD)` |

**Open:** Exact Path list live · SU product renaming · relic QoL patches · summon meta SP.

---

Pack: [systems-teardown.md](./systems-teardown.md) · [systems-economy.md](./systems-economy.md) · Theory [metagame-design.md](../../game-design/metagame-design.md) · [live-ops-design.md](../../game-design/live-ops-design.md)
