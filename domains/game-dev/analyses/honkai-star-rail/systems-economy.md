---
title: "Honkai: Star Rail — Systems map / economy"
description: "GaaS economy: Trailblaze Power, gacha pity, relics/traces sinks, endgame+BP sources."
updated: "2026-08-10"
canonical: false
tags: [game-design, economy, gaas, analysis-pack]
audience: [intermediate, advanced]
related:
  - ./README.md
  - ./gdd.md
  - ./systems-teardown.md
  - ../../case-studies/genshin-gacha-economy.md
  - ../../game-design/economy-systems.md
  - ../../game-design/game-economics-monetization.md
sensitivity: public
---

# Honkai: Star Rail — Systems map / economy

> [← Pack](./README.md) · Mode: `systems-economy`  
> Rates `(assumed)`. **Never invent ARPU / D7.**

| Field | Value |
| --- | --- |
| Project | Honkai: Star Rail (shipped study) |
| Status | reconstructed |
| Linked GDD / teardown | [gdd.md](./gdd.md) · [systems-teardown.md](./systems-teardown.md) |

---

## 0. Economy thesis

Scarcity = **time (TB Power) + banner currency + relic RNG**; fantasy = roster/Path collection and clear-time flex. Monetization accelerates **acquisition & ceiling**, not story chapter unlocks tường minh. `(inferred)`

## 1. Systems map

| Layer | Loop | Into economy |
| --- | --- | --- |
| Core | Fights / story / explore | Materials, XP, jades-adjacent soft rewards `(observed)` |
| Meta | Ascension, traces, LC, relics | Infinite sinks |
| Live | Dailies, events, MoC/PF/AS, BP, banners | Scheduled faucet + FOMO |

```text
TB Power → Calyx/Cavern/Echo → Upgrade mats/relics → Stronger teams → Endgame stars / story → More jades → Banners → Roster → New Power spends
```

## 2. Currency taxonomy

| Currency | Type | Sources | Sinks | Buyable? |
| --- | --- | --- | --- | --- |
| Trailblaze Power | Stamina | Regen, refill items | Farm nodes | Soft (refill packs) |
| Exp / character mats | Soft | Calyx, quests, events | Level/ascension/traces | Indirect |
| Relics | Gear RNG | Caverns, SU, etc. | Equip / salvage / craft QoL | No direct |
| Stellar Jade / tickets | Soft+Hard hybrid | Story, dailies, endgame, events, top-up | Gacha | Yes |
| Special tickets | Banner tokens | Conversion from jade | Limited/standard banners | Via jade |
| Nameless Honor BP currency | Track | BP progress | Cosmetics / mats / pulls | Pass purchase |
| Shop limited currencies | Event/rotating | Events, endgame shops | Selectors, cones, mats | Sometimes |

Exact names/rates edition-sensitive `(TBD verify)`.

## 3. Source → Sink matrix

| Source | Currency | Pressure if unbalanced |
| --- | --- | --- |
| TB Power regen | Mats/relics | Cap waste vs burnout |
| Endgame stars | Jade | Skill ceiling ↔ pull income |
| Events | Jade/mats | FOMO calendar |
| Top-up | Jade | Whale ceiling |
| Relic drops | Power vertical | Near-miss addiction `(genre pattern)` |

## 4. Progression curve

| Gate | Cost | Soft/Hard |
| --- | --- | --- |
| Equilibrium / World Level | Farm readiness | Soft |
| Character trace 80/skills | Mats + time | Soft |
| MoC star thresholds | Comp + relics | Soft skill+gear |
| Limited pity (~soft/hard pity pattern) | Jade | RNG soft with hard floor `(observed)` / see [GI pity sister](../../case-studies/genshin-gacha-economy.md) |

Session goal (F2P pacing): daily Power empty → small upgrade OR pity progress. `(assumed)`

## 5. Spend decision axes

| Axis | A | B |
| --- | --- | --- |
| Banner | New character (cover) | LC / eidolons (ceiling) |
| Power | Trace mats | Relic RNG |
| Endgame | Push stars now | Wait buff / build |

## 6. Anti‑inflation & brakes

- Daily Power cap  
- Weekly Echo bounds  
- Pity + selector events softens gacha cruelty `(observed)`  
- Relic still infinite sink (intentional) `(inferred)`  
- Cycle rotation brakes single hypercarry immortality `(observed)`

## 7. Monetization friction map

| Moment | F2P | Paid | Ethics |
| --- | --- | --- | --- |
| Banner FOMO | Save / skip | Top-up / packs | High FOMO risk `(genre pattern)` |
| BP | Free track | Paid track | Moderate |
| Power refill | Wait regen | Refill items | Convenience |
| Relics | Time | Same RNG | Time-pay wall feel |

Red line soft: no hard “pay to open next story door” — but power/time disparity is real. `(inferred)`

## 8. Telemetry & KPIs (instrumenting inspired game)

| Metric | Why |
| --- | --- |
| PowerCapWasteRate | Pacing |
| PityConversion / 50-50 if any | Fair-feel |
| RelicUpgradeNearMiss | Burnout |
| EndgameStarDistribution | Ceiling honesty |
| BannerSkipRate | FOMO pressure |

## 9. Spreadsheet todos

- [ ] Soft jade/month model F2P vs low-spend (public community sheets as input — cite when used)  
- [ ] Relic EV to “usable set”  
- [ ] Cycle coverage matrix (elements × Paths)

---

[economy-systems.md](../../game-design/economy-systems.md) · [game-economics-monetization.md](../../game-design/game-economics-monetization.md) · [systems-teardown.md](./systems-teardown.md)
