---
title: "Idle Game Deep Dive"
description: "Economy ramp, automation loop, KPI cho idle/incremental games."
tags:
  - game-design
  - idle
updated: 2026-03-11
---

# 💤 Idle Game Deep Dive

## Pillars
- Progression kể cả khi offline.
- Automation unlocks (workers, upgrades).
- Exponential growth cảm giác “power fantasy”.

## Core Loop
1. Thu thập resource (tap/auto).
2. Đầu tư vào upgrade để tăng production.
3. Prestige reset để mở multiplier.

## Economy
- Production formula: `Output = Base * (UpgradeMultiplier) * (PrestigeBonus)`.
- Balance sink: new building cost, research tree.
- Offline earnings: cap (8-12h) + catch-up pack.

## Meta
- Event (Factory theme) với currency riêng.
- Collection card buff production.
- Social competition: leaderboard, co-op multiplier.

## KPI
- Session frequency: 5-6 lần/ngày, 1-2 phút/lần.
- D1 retention >45%, D7 >20%.
- Monetization: time skip, premium currency bundle.

## Risks
- Chậm early game → churn.
- Paywall prestige.
- UI overload stats.

## ✅ Apply it
- [ ] Tune early ramp để unlock automation trong 10 phút.
- [ ] Thiết kế offline earning + cap.
- [ ] Xây prestige loop với reward thuyết phục.
- [ ] Event meta để tránh nhàm chán.