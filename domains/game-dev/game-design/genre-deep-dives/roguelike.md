---
title: "Roguelike Deep Dive"
description: "Loop structure, meta progression, KPI cho roguelike/roguelite."
tags:
  - game-design
  - roguelike
updated: 2026-03-11
---

# 🌀 Roguelike Deep Dive

## Pillars
- Procedural generation → mỗi run khác nhau.
- Permadeath/Reset with meta progression.
- High skill ceiling + knowledge retention.

## Core Loop
1. Chọn build (weapon, artifact).
2. Chạy dungeon (combat + loot).
3. Chết → nhận meta currency → upgrade hub.

## Meta
- Unlock weapon/character, upgrade stat (start HP, gold bonus).
- Narrative hub (NPC, quest) để tạo continuity.
- Challenge mode (boss rush, curse modifier).

## Economy
- In-run currency vs meta currency.
- Risk-reward: shop vs hoard, curse items.
- Randomness control: reroll, prophecy.

## KPI Benchmark
- Session length: 20-40 phút/run.
- D1 retention 40%+, D7 15%.
- Meta engagement: % player spend currency sau mỗi run >70%.
- Conversion: DLC/expansion adoption.

## Risks
- RNG quá cao → cảm giác bất công.
- Meta grind quá dài.
- Lack of novelty sau nhiều giờ.

## ✅ Apply it
- [ ] Kiểm tra balance RNG vs skill.
- [ ] Thiết kế meta progression meaningful mỗi 2-3 run.
- [ ] Telemetry track run outcome, artifact pick rate.
- [ ] Launch challenge mode để giữ core player.