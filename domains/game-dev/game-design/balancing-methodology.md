---
title: "Balancing Methodology"
description: "Excel modeling, Monte Carlo simulation, playtest metrics cho balancing."
tags:
  - game-design
  - balancing
updated: 2026-03-11
---

# ⚖️ Balancing Methodology

## 1) Spreadsheet Modeling
- Dùng Excel/Google Sheets để mô phỏng economy/combat.
- Input: base stats, level curve, damage formula.
- Output: TTK, DPS, resource flow, payback day.
- Tips: lock cell unit (per minute/per session), highlight breakpoints.

### Example Formula

```
DPS = (BaseDamage + Attack * Scale) / Cooldown
TTK = EnemyHP / DPS
CurrencyFlow = EarningPerSession - SpendingPerSession
```

- Scenario analysis: Data Table/hash check.
- Data validation: slider cho level, rarity.

## 2) Monte Carlo Simulation
- Khi hệ thống có randomness (crit, loot), dùng Monte Carlo (Python/Excel) để chạy 10k iteration.
- Metric: Expected value, variance, percentile.
- Example pseudo:

```python
import random
def simulate_damage(attack, crit_rate, crit_mult, runs=10000):
    total = 0
    for _ in range(runs):
        dmg = attack
        if random.random() < crit_rate:
            dmg *= crit_mult
        total += dmg
    return total / runs
```

- Kết hợp distribution graph để xem tail events.

## 3) Playtest Metrics
- Define KPI: Win rate (PvP), level completion time, fail count, resource delta.
- Use telemetry to gather per session stats; visualize heatmap.
- Compare actual vs spreadsheet predictions.

## 4) Iteration Loop
1. Hypothesis (buff hero X +10% HP).
2. Model impact (sheet + sim).
3. Patch internal build.
4. Playtest + telemetry.
5. Evaluate metrics vs target range (e.g., win rate 48-52%).

## 5) Tooling
- Excel add-ons: Solver (optimize stat), Data Table.
- Python/R: Jupyter notebook cho sim phức tạp.
- Unity: script capture combat logs, output CSV cho sheet.

## ✅ Apply it
- [ ] Xây spreadsheet template (combat/economy) với assumption rõ.
- [ ] Thiết lập Monte Carlo tool cho hệ thống random.
- [ ] Định nghĩa KPI balancing và log trong telemetry.
- [ ] Chạy iteration loop: hypothesis → model → playtest → metrics.
- [ ] Document patch note + kết quả balancing để trace lịch sử.