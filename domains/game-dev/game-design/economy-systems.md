---
title: "Economy Systems"
description: "Blueprint xây soft/hard currency, store, sink/source và LiveOps balancing."
tags:
  - game-design
  - economy
updated: 2026-03-11
---

# 💰 Economy Systems Blueprint

> Economy tốt = người chơi luôn có động lực kiếm/spend, team LiveOps dễ cân.

## 1. Currency Map
| Currency | Type | Source | Sink | Owner |
| --- | --- | --- | --- | --- |
| Gold | Soft | Daily quest, auto loot | Upgrade gear | Economy designer |
| Gem | Hard | IAP, event milestone | Premium chest | Monetization |
| Token | Event | Boss event | Event shop | LiveOps |

## 2. Source/Sink Balance
- Ratio soft currency source vs sink.
- Hard currency cap per day.
- Inflation guard: weekly cap, dynamic pricing.

## 3. Store & Offer Design
- Tiered store (Daily/Weekly/Event).
- Offer template: `Value Score = Value / Price`.
- Feature flag/Remote config cho A/B.

## 4. Progression Curve
- Level vs XP vs Cost table.
- Goal: session 10 phút = đủ upgrade nhỏ.
- Spreadsheet sandbox.

## 5. LiveOps Hooks
- Event currency expire.
- Rotating bundles (Battle Pass, Limited Shop).
- Telemetry: `CurrencyEarned`, `CurrencySpent`, `OfferPurchased`.

## 6. KPI Dashboard
- ARPPU, ARPDAU, Conversion%.
- Soft currency delta/day.
- Offer uptake (CTR, buy rate).
- Churn vs Net Worth.

## 7. Checklist
- [ ] Currency taxonomy rõ ràng.
- [ ] Bảng source/sink cân bằng.
- [ ] Offer có value score & owner.
- [ ] Telemetry và dashboard sẵn sàng.
- [ ] Scenario "rich get richer" mô phỏng.

## 8. Links
- [Core Loop Mastery](./core-loop-mastery.md)
- [Playtest Framework](./playtest-framework.md)
- [Unity Optimization](../unity-deep-dive/optimization-techniques.md)