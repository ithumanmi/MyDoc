---
title: "Honkai: Star Rail — Systems Teardown"
description: "Systems essay: Break/SP combat puzzle, Core/Meta/Live map, decision axes, GaaS economy & UX."
updated: "2026-08-10"
canonical: false
tags: [game-design, case-study, teardown, gaas, analysis-pack]
audience: [intermediate, advanced]
related:
  - ./README.md
  - ./pitch.md
  - ./gdd.md
  - ./systems-economy.md
  - ../../game-design/templates/game-systems-teardown.md
  - ../../case-studies/genshin-gacha-economy.md
  - ../triangle-strategy/systems-teardown.md
sensitivity: public
---

# Honkai: Star Rail — Systems Teardown

> [← Pack](./README.md) · [Pitch](./pitch.md) · [GDD](./gdd.md)  
> Skill: `.cursor/skills/game-systems-teardown/` · Template: [game-systems-teardown.md](../../game-design/templates/game-systems-teardown.md)

## Agent SUMMARY

- Thesis: combat-as-puzzle (Break / SP / turn order) wrapped in Hoyoverse GaaS cadence — not “Genshin turn-based.”
- Core chain: weakness → SP manage → spend turn → Break → burst → stabilize → clear.
- Agency curve: High manual early → hybrid mid (Auto farm) → late Manual endgame + Auto grind.
- Axes: Break vs raw damage · SP-positive vs SP-hungry · Character pull vs Cone/Eidolon.
- Anti–power-creep: cycle buffs + elemental coverage tax + relic RNG sink.
- Economy: Trailblaze Power sources; infinite relic / trace / gacha sinks.
- Transfer: shared team resource + break bar + Auto/Manual split; don’t clone IP/tone.

**Platform / model:** Mobile + PC · GaaS freemium / gacha (Hoyoverse) `(observed)`  
**Genre family:** Turn-based RPG + Live Ops · collection meta  
**Sources:** play patterns / design lộ thiên; **không** bịa D1/D7. Tags: `(observed)` · `(inferred)` · `(genre pattern)`

Theory: [advanced-core-loops.md](../../game-design/advanced-core-loops.md) · [metagame-design.md](../../game-design/metagame-design.md) · [game-economics-monetization.md](../../game-design/game-economics-monetization.md) · [player-psychology.md](../../game-design/player-psychology.md) · [live-ops-design.md](../../game-design/live-ops-design.md)

---

## 0. Thesis

HSR không “làm Genshin đánh theo lượt”. Nó **đảo vai trò combat** trong hệ Hoyoverse: từ skill expression real-time sang **combat-as-puzzle** (Break / weakness / Skill Point / turn order) — rồi nhúng puzzle đó vào máy GaaS quen thuộc (stamina, gacha, endgame cycle) để giữ session ngắn–dài song song. `(inferred)`

---

## 1. Loop physics & nhịp agency

**Core actions (trong trận):**  
`Scan weakness → Manage Skill Points → Spend turn (Basic/Skill/Ult) → Break toughness → Burst window → Stabilize (heal/shield/cleanse) → Clear`

HSR = **Knowledge + Composition snowball**: hiểu Break/SP/Path → ít micro hơn → Auto farm; endgame giữ High Agency. `(inferred)`

| Feedback | Cơ chế |
| --- | --- |
| **Positive** | Đúng weakness → Break → turn advantage → clear → farm hiệu quả `(observed)` |
| **Negative / brake** | Sai cover, hết SP, Toughness cứng, MoC sai team, TB Power cap `(observed)` |

| Phase | Agency | Hệ thống | Cảm xúc |
| --- | --- | --- | --- |
| Early | High manual | Dạy Break/SP/Ult | “Mỗi skill có ý” |
| Mid | Hybrid | Path identity, SU lab, Auto farm | Thử–lỗi đội |
| Late | Auto farm + Manual endgame | Cycles + relic RNG | Number spectacle + turn pressure |

---

## 2. Systems map

| Layer | Loop / modes | Job |
| --- | --- | --- |
| Core | Combat puzzle + light explore + story | Skill + kit fantasy |
| Meta | Ascension · Traces · LC · Relics · comps · TB Level | Collection + vertical |
| Live | TB Power · Events · MoC/PF/AS · Echo · BP · Banners | Session diversity + FOMO |

SU = meta-in-mode roguelite. `(observed)`

---

## 3. Decision axes

### Axis 1 — Break vs Raw HP

| | Break-oriented | Raw / ignore Break |
| --- | --- | --- |
| Được | Turn adv, safer elites | Fast fodder / overkill |
| Mất | Need cover/breakers | Wall on high Toughness / timer |
| Khi nào | Elites, endgame | Weak farm `(inferred)` |

### Axis 2 — SP-positive support vs SP-hungry DPS

| | SP-gen kits | SP-hungry nukers |
| --- | --- | --- |
| Được | Stable rotation | Burst fantasy |
| Mất | Lower personal damage | Dead Basics if starved |
| Khi nào | Backbone | With battery `(observed)` |

### Axis 3 — Character pull vs Cone / Eidolon

| | New character | Cone / E1+ |
| --- | --- | --- |
| Được | New cover/archetype | Same-kit ceiling |
| Mất | Weaker signature gear | No new content type |
| Khi nào | Thin account | Whale/optimize `(genre pattern)` |

---

## 4. Escalation & anti–power-creep

| Tier | Role |
| --- | --- |
| Fodder | Tutorial |
| Elite + Toughness | Break discipline |
| Equilibrium | Soft farm wall |
| Weekly Echo | Bounded sink |
| MoC / PF / AS | Cycle composition tax `(observed)` |
| Relic substats | Infinite vertical |

**Lever:** cycle buffs + elemental coverage tax — không chỉ HP inflation. Contrast premium route exclusivity: [Triangle Strategy teardown](../triangle-strategy/systems-teardown.md). `(inferred)`

---

## 5. Economy & monetization friction

See detailed sheet: [systems-economy.md](./systems-economy.md).

Sources: TB Power, quests, events, endgame, dailies, BP. Sinks: traces, relics, gacha. Premium sells **roster speed & ceiling**, not literal stage skip. `(inferred)` Sister: [genshin-gacha-economy.md](../../case-studies/genshin-gacha-economy.md).

---

## 6. UI/UX & psychology

Weakness icons FTUE; turn order + SP + Toughness hierarchy; Auto for grind; theorycrafting externalized; FOMO banners + relic near-miss loss aversion → [player-psychology.md](../../game-design/player-psychology.md). `(observed)` / `(inferred)`

---

## 7. Transfer

| Portable | Don’t copy blind |
| --- | --- |
| Shared team SP | Free skills kill axis |
| Break bar vs HP | Cosmetic toughness |
| Cycle endgame | Toxic FOMO cadence |
| Auto farm / Manual skill | Auto endgame = no mastery |
| Stamina + gacha | Idle without puzzle core |

**Title-specific:** Hoyoverse IP, Ult production, tonal whiplash.

---

## 8. Open questions / verify

- [ ] % Auto by account age / MoC floor  
- [ ] Element cover vs 48h 3-star new cycle  
- [ ] Time-to-usable-relic-set vs first pity  
- [ ] ZZZ / GI agency curve compare  
- [ ] Remembrance/summon vs SP puzzle integrity `(patch)`

---

| Topic | Path |
| --- | --- |
| Pack siblings | [pitch.md](./pitch.md) · [gdd.md](./gdd.md) · [systems-economy.md](./systems-economy.md) |
| Core/meta | [advanced-core-loops.md](../../game-design/advanced-core-loops.md) |
| Gacha | [game-economics-monetization.md](../../game-design/game-economics-monetization.md) · [genshin-gacha-economy.md](../../case-studies/genshin-gacha-economy.md) |
| Live | [live-ops-design.md](../../game-design/live-ops-design.md) |
