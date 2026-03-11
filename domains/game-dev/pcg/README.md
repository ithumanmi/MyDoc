---
title: "Procedural Generation Module"
description: "Thuật toán tạo thế giới ngẫu nhiên: noise, WFC, dungeon pathing."
tags:
  - pcg
  - unity
updated: 2026-03-11
---

# 🧩 Procedural Generation Module

| File | Nội dung | Khi nào dùng |
| --- | --- | --- |
| [procedural-generation.md](./procedural-generation.md) | Noise, WFC, tilemap pipeline | Roguelike, endless runner, world builder |
| [pcg-algorithms.md](./pcg-algorithms.md) | BSP, drunkard walk, Poisson Disk, Marching, mission graph | Thêm thuật toán cụ thể cho dungeon, spawn, terrain |

**Notes:**
- Bắt đầu từ noise 2D → tilemap → rule-based.
- Khi scale lớn, cân nhắc job system/DOTS để sinh map realtime.

> Đo tác động lên FPS bằng [Metrics Module](../metrics/unity-impact-metrics.md) trước khi ship.