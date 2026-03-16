---
title: "World Building"
description: "Level design, pacing, procedural generation và môi trường sống động."
tags:
  - world-building
  - level-design
  - pcg
updated: 2026-03-16
---

# 🏞️ World Building

| Module | Nội dung | Khi nào dùng |
| --- | --- | --- |
| [level-design/](./level-design/README.md) | Layout, pacing, encounter flow | Thiết kế level nhanh có logic |
| [pcg/](./pcg/README.md) | Procedural generation playbooks | Làm roguelike, sandbox systems |

## Workflow gợi ý
1. Chốt pillar level (pacing, readability) → [level-design](./level-design/README.md).
2. Nếu cần scale content → áp dụng PCG, giữ rule set rõ → [pcg](./pcg/README.md).
3. Kết hợp telemetry (heatmap, death map) từ [metrics](../production/metrics/README.md) để lặp nhanh.

## Cross-links
- [Game Design](../game-design/README.md) – core loop & economy phải khớp pacing.
- [Programming / Physics](../programming/physics/README.md) – movement & collision ảnh hưởng feel level.
- [Art-Tech / Graphics](../art-tech/graphics/README.md) – lighting & readability.