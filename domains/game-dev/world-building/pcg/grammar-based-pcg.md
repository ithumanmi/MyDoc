---
title: "Grammar-based PCG"
description: "L-systems, shape grammar, rule rewriting cho level/structure."
tags:
  - pcg
  - grammar
  - unity
updated: 2026-03-11
---

# 🧱 Grammar-based Procedural Generation

## 1) L-Systems
- String rewriting dựa trên rules (production).
- `axiom` → apply rules n lần → chuỗi ký tự điều khiển turtle graphics.
- 2D flora/tree: commands `F` (forward), `+/-` rotate, `[` push state, `]` pop.
- Parameters: angle, segment length, randomness trong rule selection.

### Extensions
- Stochastic L-system: nhiều rule cho 1 symbol với probability.
- Context-sensitive: rule phụ thuộc symbol láng giềng.
- 3D L-system: turtle có pitch/yaw/roll.

## 2) Shape Grammar
- Rule: `Shape -> sub-shapes` với transform (scale, rotate, translate).
- Dùng để generate building/city: start shape = lot, apply facade, window, roof.
- Constraint: limit height, align grid, adjacency rules.
- Use attributes: shape carry metadata (style, function) để rule condition.

## 3) Mission / Quest Grammar
- Symbol = mission beat (Start, Fetch, Boss). Rule expand beat thành sequence chi tiết.
- Example: `Quest -> Intro Travel Encounter Boss`, `Encounter -> Combat | Puzzle`.
- Mix với graph generation để tạo quest tree consistent.

## 4) Implementation Tips
- Represent rule bằng ScriptableObject: symbol, probability, output string/shape commands.
- L-system parser: stack state cho `[ ]`. Render mesh/line sau khi parse.
- Shape grammar: instantiate prefab per rule, apply transform matrix.
- Debug: visualize rule tree, log expansion depth.
- Deterministic seed: random state per expansion cho reproducible.

## 5) Use Cases
- Vegetation (trees, coral), architecture (modular building), quests/story structure, dialog branching.
- Combine grammar với noise/WFC: grammar cho macro skeleton, noise fill detail.

## ✅ Apply it
- [ ] Define axiom và rule set (stochastic/context-sensitive nếu cần).
- [ ] Implement parser (turtle stack, shape instancing) + determinism bằng seed.
- [ ] Constraint checking (height, collision) sau mỗi expansion.
- [ ] Visual debug tree/commands để tune rule.
- [ ] Mix grammar output với PCG khác (noise, WFC) để hoàn thiện level.