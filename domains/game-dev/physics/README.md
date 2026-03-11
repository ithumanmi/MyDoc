---
title: "Physics Module"
description: "Tài liệu xây dựng core mechanic dựa trên vật lý và tự tạo physics engine."
tags:
  - physics
  - unity
updated: 2026-03-11
---

# ⚙️ Physics Module

| File | Nội dung | Khi nào dùng |
| --- | --- | --- |
| [simple-physics-engine.md](./simple-physics-engine.md) | Dùng lượng giác viết physics engine 3D mini | Khi cần hiểu sâu collision/constraint hoặc làm tool riêng |
| [unity-physics-deep-dive.md](./unity-physics-deep-dive.md) | Rigidbody/Collider, layer matrix, CCD, tối ưu PhysX | Khi tối ưu gameplay va chạm, tránh xuyên vật, tối ưu CPU |

**Checklist áp dụng:**
- [ ] Benchmark delta time và precision trước khi thay physics mặc định.
- [ ] Viết test cho collision/penetration.
- [ ] Log performance bằng Unity Profiler khi bật custom solver.

> Link chéo: [Metrics/Unity Impact](../metrics/unity-impact-metrics.md) để đo crash/FPS khi thay đổi hệ physics.