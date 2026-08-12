---
title: "Honkai: Star Rail — Systems teardown (deep)"
description: "Deep systems essay: Break/SP physics, MoC PF AS triad, axes, escalation, GaaS friction, UX."
updated: "2026-08-10"
canonical: false
tags: [teardown, gaas, deep, analysis-pack]
audience: [intermediate, advanced]
related:
  - ./README.md
  - ./systems-economy.md
  - ./gdd.md
  - ../_quality-bar.md
  - ../triangle-strategy/systems-teardown.md
  - ../infect-them-all/systems-teardown.md
sensitivity: public
---

# Honkai: Star Rail — Systems Teardown (deep)

> [← Pack](./README.md) · [Economy](./systems-economy.md) · [Quality bar](../_quality-bar.md)  
> Skill `game-systems-teardown`. Endgame triad MoC / Pure Fiction / Apocalyptic Shadow `(observed)`; cycle ~6 weeks community/guides `(observed)` — verify live UI.

## Agent SUMMARY

- Thesis: combat-as-puzzle (Break+SP) × Hoyoverse GaaS cadence — not GI turn-based.
- Core: weakness → SP budget → Break → burst → stabilize → clear.
- Agency: Manual FTUE → Auto farm mid → Manual endgame late.
- Axes: Break vs raw · SP+ vs SP− · pull char vs LC/E · **mode specialization MoC/PF/AS**.
- Anti-creep: cycle buffs + three orthogonal endgame skills + relic sink + Starward optional third team layer `(observed)` / evolving.
- Transfer: shared resource + break phase + Auto/Manual split + multi-exam endgame.

**Model:** Mobile+PC GaaS gacha · **Genre:** TB RPG + LiveOps  
Tags: `(observed)` · `(inferred)` · `(genre pattern)` · `(assumed)` · `(TBD)`

Theory: [advanced-core-loops.md](../../game-design/advanced-core-loops.md) · [live-ops-design.md](../../game-design/live-ops-design.md) · [player-psychology.md](../../game-design/player-psychology.md) · [game-economics-monetization.md](../../game-design/game-economics-monetization.md)

---

## 0. Thesis

HSR **đổi skill expression** trong hệ Hoyoverse từ real-time (aim/i-frame) sang **turn puzzle** với hai đồng tiền chiến đấu đồng hạng: **Toughness/Break** và **Skill Point đội**. Sau đó bọc puzzle ấy bằng máy retention quen thuộc — Power, banners, endgame exams xoay vòng — để một người chơi vừa “suy nghĩ 4 phút,” vừa “cày 40 ngày.” `(inferred)`

---

## 1. Loop physics & nhịp agency

### Core chain (một trận)

```text
Scout weaknesses / Toughness
        ↓
Allocate SP (Basic gen vs Skill spend)
        ↓
Apply Toughness damage → Break window
        ↓
Burst (Skill/Ult/follow-up/DoT snapshot…)
        ↓
Stabilize (heal/shield/cleanse/taunt)
        ↓
Clear or wipe / timer fail (endgame)
```

**Snowball type:** Knowledge + Composition (không phải unit-count tipping như [Infect Them All](../infect-them-all/systems-teardown.md)).

| Feedback | Cơ chế |
| --- | --- |
| **+** | Đúng element → Break sớm → enemy skip/debuff window → fewer turns → stars / lower Power waste `(observed)` |
| **−** | Sai cover, SP lock, Break reject, cycle buff mismatch, Power cap, timer `(observed)` |

### Phases of account life

| Phase | Agency | Systems hub | Cảm xúc |
| --- | --- | --- | --- |
| Early | High manual | FTUE weakness icons, SP pips, Ult energy | “Mỗi nút có nghĩa” |
| Mid | Hybrid | Path identity; SU lab; Auto Calyx | Theorycraft vui / farm êm |
| Late | Split brain | Auto relics; Manual MoC/PF/AS (+ optional Starward) | Number flex + FOMO roster |

**Vì sao mobile sống được:** Auto cắt mệt tay; Manual giữ ego mastery trên jade-gated exams. `(genre pattern)`

---

## 2. Systems map

| Layer | Nội dung | Job |
| --- | --- | --- |
| **Core** | Turn combat, Technique overworld, light explore | Moment-to-moment skill |
| **Meta** | Levels, ascension, Traces, LC, Relics, teams, TB Level / Equilibrium | Power schedule |
| **Live** | Dailies, events, BP, banners, Echo weekly, **MoC · PF · AS** | Cadence & FOMO |
| **Meta-in-mode** | Simulated Universe family (Divergence, etc. evolve) | Experiment builds without endgame wipe stigma `(observed)` |

```text
Story / Events ──► Soft jade & cast fantasy
       │
TB Power ──► Mats / Relics ──► Traces & sets ──► Endgame exams ──► Jade ──► Banners ──► New covers
       │                                                      ▲
       └────────────── Cycle buffs shape which covers matter ─┘
```

---

## 3. Decision axes

### A1 — Break focus vs Raw HP

| | Break-oriented | Raw / ignore Break |
| --- | --- | --- |
| Được | Phase skip, AS scoring, safer elites | Farm fodder speed |
| Mất | Slot tax (breakers), build Break Effect | MoC/AS walls |
| Khi | AS, high Toughness bosses | Calyx weak packs `(inferred)` |

### A2 — SP economy (Bite/Eat của HSR)

| | SP-positive kits | SP-hungry carries |
| --- | --- | --- |
| Được | Team breathes | Burst fantasy |
| Mất | Lower personal DPS | Dead Basics / stalled Ult |
| Khi | Backbone Harmony/Abundance… | After battery locked `(observed)` |

### A3 — Banner: Character vs LC / Eidolon

| | New character | Signature / E1+ |
| --- | --- | --- |
| Được | New exam cover | Same-kit ceiling |
| Mất | Incomplete LC | No new Mode coverage |
| Khi | Missing element/Path for cycle | Whale / mirror `(genre pattern)` |

### A4 — Endgame specialization (orthogonal exams)

| Mode | Tests primarily | Build bias |
| --- | --- | --- |
| **Memory of Chaos** | Two-side (→ optional 3 with Starward) DPS + sustain under **cycle count** | ST burst, sustain, two+ cores `(observed)` |
| **Pure Fiction** | Wave clear / points in limited cycles | AoE, follow-up, blast clears `(observed)` |
| **Apocalyptic Shadow** | Boss Toughness + Break windows | Break Effect, weakness match, dump in Break `(observed)` |

Đây là trục chống “one team forever” mạnh hơn chỉ tăng HP — **ba bài kiểm tra khác kỹ năng**. `(inferred)`

### A5 — Power spend: Traces vs Relics

| | Finish traces | Relic RNG |
| --- | --- | --- |
| Được | Deterministic power | Cap chase |
| Mất | Lower ceiling fashion | Near-miss addiction |
| Khi | New DPS online | Already traced `(assumed)` |

---

## 4. Escalation & anti–power-creep

| Tier | Role | Player answer |
| --- | --- | --- |
| Trash mobs | Auto fodder | Overlevel |
| Elites + Toughness | Break school | Element cover |
| Equilibrium walls | Soft story pace | Farm mats |
| Echo of War weekly | Bounded sink | Calendar |
| MoC / PF / AS cycles | Skill exams + jade | Roster breadth |
| Starward optional nodes | Extra team tax / flex | Third premium core `(observed)` mode evolution — verify live |
| Relic subs | Infinite vertical | Time / whale |

**Levers chống one-team:** (1) cycle line-up + buffs, (2) three orthogonal modes, (3) optional Starward third node, (4) relic EV wall. Không chỉ HP creep. Contrast premium branch tax: [Triangle Strategy](../triangle-strategy/systems-teardown.md).

---

## 5. Economy & monetization friction

Chi tiết đầy đủ: [systems-economy.md](./systems-economy.md).

Tóm tắt: Power = faucet thời gian; jade = pull oxygen từ story/events/endgame; relics = sink vô hạn; banners = FOMO. Bán tốc độ roster & ceiling; pity làm dịu, không xóa extractiveness. `(inferred)` Sister: [genshin-gacha-economy.md](../../case-studies/genshin-gacha-economy.md).

---

## 6. UI/UX & psychology

| Topic | |
| --- | --- |
| **FTUE** | Weakness icons trên đầu; SP pips; turn order bar `(observed)` |
| **Hierarchy** | Toughness co-visible với HP trên elite — nếu không, Break chết `(inferred)` |
| **Auto contract** | Players trust Auto on farm only if AI không phá Break/SP quá tệ `(assumed)` |
| **External brain** | Relic/theorycraft đẩy ra wiki — giảm in-game cognitive nhưng tăng community dependency `(observed)` |
| **Psyche** | Path identity · Ult cinema · FOMO · relic near-miss loss aversion · mode star flex ([player-psychology.md](../../game-design/player-psychology.md)) |
| **Fatigue** | Story wall-of-voice vs daily loop tension `(assumed)` |

---

## 7. Transfer (port sang game khác)

| Portable | Don’t copy blind |
| --- | --- |
| Shared team action point | Skills free → no axis |
| Break as **phase** | Cosmetic bar |
| **≥2 orthogonal endgame exams** | One Abyss only → one meta forever |
| Auto farm / Manual exam | Auto exams → no mastery |
| Pity + skip dignity selectors | Pity without skip culture still toxic |

**Title-specific:** Hoyoverse IP, Ult production, tonal whiplash, multi-year Path kit library.

---

## 8. Open questions / verify

- [ ] Auto% by content type × account age  
- [ ] Correlation element coverage ↔ 48h full jade from new cycle  
- [ ] Time-to-first-usable-4pc vs first limited pity  
- [ ] Starward adoption vs third-team ownership  
- [ ] Remembrance/summon / Elation-style kits vs SP integrity `(patch)`  
- [ ] ZZZ vs HSR agency curve same studio  

---

| | Path |
| --- | --- |
| Pack | [gdd.md](./gdd.md) · [systems-economy.md](./systems-economy.md) · [pitch.md](./pitch.md) |
| LiveOps theory | [live-ops-design.md](../../game-design/live-ops-design.md) |
| Contrast | [infect-them-all](../infect-them-all/systems-teardown.md) · [triangle-strategy](../triangle-strategy/systems-teardown.md) |
