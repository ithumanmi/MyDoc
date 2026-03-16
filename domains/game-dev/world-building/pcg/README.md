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
| [procedural-generation.md](./procedural-generation.md) | Noise cơ bản, tilemap pipeline, quản lý seed | Roguelike, endless runner, world builder |
| [pcg-algorithms.md](./pcg-algorithms.md) | BSP, drunkard walk, Poisson Disk, Marching, mission graph | Thêm thuật toán cụ thể cho dungeon, spawn, terrain |
| [noise-algorithms.md](./noise-algorithms.md) | Perlin, Simplex, Worley, compositing | Sinh heightmap, biome mask, texture procedural |
| [wave-function-collapse.md](./wave-function-collapse.md) | WFC pipeline, entropy, backtracking | Tilemap constraint-based (dungeon, city, voxel) |
| [dungeon-generation.md](./dungeon-generation.md) | BSP, cellular automata, mission graph | Roguelike, cave, mission-based dungeon |
| [terrain-generation.md](./terrain-generation.md) | Heightmap, erosion, biome layering, chunk streaming | Thế giới mở, terrain runtime |
| [grammar-based-pcg.md](./grammar-based-pcg.md) | L-systems, shape grammar, quest grammar | Cây cối, kiến trúc modular, quest/story generation |

**Notes:**
- Bắt đầu từ noise 2D → tilemap → rule-based.
- Khi scale lớn, cân nhắc job system/DOTS để sinh map realtime.

> Đo tác động lên FPS bằng [Metrics Module](../metrics/unity-impact-metrics.md) trước khi ship.