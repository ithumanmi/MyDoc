---
title: "Triangle Strategy — Systems map / economy"
description: "Premium SRPG economy: spoils, shop/smith sinks, Quietuses/Kudos, mock battles; no IAP."
updated: "2026-08-10"
canonical: false
tags: [game-design, economy, analysis-pack, tactical-rpg]
audience: [intermediate, advanced]
related:
  - ./gdd.md
  - ./systems-teardown.md
  - ../../game-design/templates/game-systems-map-economy.md
  - ../../game-design/economy-systems.md
sensitivity: public
---

# Triangle Strategy — Systems map / economy

> [← Pack](./README.md) · Skill: `game-design-docs` · Mode: `systems-economy`  
> Rates `(assumed)` until spreadsheet-backed. No fake ARPU.

| Field | Value |
| --- | --- |
| Project | Triangle Strategy (shipped study) |
| Owner | Docs study |
| Status | reconstructed `(proposed)` |
| Linked GDD | [gdd.md](./gdd.md) |

---

## 0. Economy thesis

Economy phục vụ **campaign readiness** (gear/level để đọc board), không phải live FOMO. Scarcity chính là **attention / Quietuses / conviction commits**, không phải hard currency IAP. `(inferred)`

## 1. Systems map

| Layer | Loop / modes | Rewards into economy |
| --- | --- | --- |
| Core | Grid battles | Spoils, XP, materials |
| Meta | Chapters, character stories, conviction recruits | Cast = horizontal “wealth”; shops/encampment |
| Live | Mental Mock Battles, NG+ | Optional farm / mastery sink — no season pass `(observed)` |

```text
Battle → Spoils/XP → Shop/Smith/Encampment → Stronger board presence → Harder chapter scripts
Dialogue/Choices → Convictions (meta currency, non-shop) → Roster/ending gates
```

## 2. Currency taxonomy

| Currency | Type | Sources | Sinks | Persist? | Buyable? |
| --- | --- | --- | --- | --- | --- |
| Soft money / materials | Soft | Battles, exploration | Shop, smith, upgrades | Campaign | No (premium) |
| XP / levels | Soft progress | Battles, mock | Implicit opportunity cost | Campaign / NG+ rules | No |
| Quietuses charges | Tactical resource | Progress / unlocks `(TBD exact)` | Emergency battle spend | Limited refill rules `(TBD)` | No |
| Convictions U/M/L | Hidden meta | Dialogue, conduct | Consumed as path identity (not spent in shop) | Campaign | No |
| Kudos-like / facility points | Soft meta | Play activities `(TBD name/edition)` | Encampment upgrades | Campaign | No |

Exact names/rates vary by edition — verify `(TBD)`.

## 3. Source → Sink matrix

| Source | Currency | Est. rate | Primary sink | Pressure if unbalanced |
| --- | --- | --- | --- | --- |
| Main battles | Soft + XP | Chapter-paced `(assumed)` | Gear for next script | Undergear → soft wall |
| Mock battles | Soft + XP | Optional `(assumed)` | Overlevel / mastery | Trivializes boards if unlimited `(inferred)` |
| Character stories | Cast / minor rewards | Finite | Horizontal depth | — |
| Dialogue choices | Convictions | Per choice | Route/recruit lock | “Wrong” fantasy / FOMO |

## 4. Progression curve

| Gate | Player power / unlock | Cost | Soft or hard |
| --- | --- | --- | --- |
| Chapter boss | Level/gear check | Time in battles | Soft |
| Conviction recruit | Axis threshold | Opportunity cost of other leans | Soft→Hard (miss forever this NG) |
| Scales branch | Story path | Lost alternate scenes | Hard content gate |
| Quietuses empty | Tactical options | Overspend early | Soft skill gate |

Session goal: one chapter segment ≈ meaningful upgrade or story beat — not daily stamina clear. `(assumed)`

## 5. Spend decision axes

| Axis | Option A | Option B | When A wins |
| --- | --- | --- | --- |
| Power | Farm mock battles | Push story undergeared | Learning / completionist |
| Tactical | Quietuses now | Hoard boss | Protect Serenoa / key unit |
| Meta | Commit conviction | Hedge choices | Clarity of ending fantasy |

## 6. Anti‑inflation & brakes

- Finite main story rewards; mock battles bounded optional `(observed)`
- Difficulty modes widen audience without selling power `(observed)`
- No gacha pity — inflation risk is **player overlevel**, braked by map scripts / Serenoa fail `(inferred)`

## 7. Monetization friction map

| Moment | F2P path | Paid acceleration | Ethical note |
| --- | --- | --- | --- |
| Entire campaign | N/A — premium purchase | Editions / catalog DLC adjacent `(assumed)` | No mid-story IAP wall `(observed)` |

Red lines: story progress gate behind microtransaction — not used. `(observed)`

## 8. Telemetry & KPIs (if instrumenting a inspired project)

| Event / metric | Why | Healthy signal `(TBD)` |
| --- | --- | --- |
| BattleRetry | Difficulty vs gear | … |
| QuietusesSpentByPhase | Axis health | … |
| MockBattleHours vs Chapter | Farm addiction | … |
| SecondRouteStart | Breadth success | … |

## 9. Spreadsheet / sim todos

- [ ] Quietuses economy per difficulty  
- [ ] Soft currency income vs smith costs mid-game  
- [ ] Conviction weight table for recruit thresholds  

---

## Theory footer

[economy-systems.md](../../game-design/economy-systems.md) · [systems-teardown.md](./systems-teardown.md) · [gdd.md](./gdd.md)
