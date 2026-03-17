---
title: "Programming / Physics"
description: "Hub: Physics gameplay, controller, vehicle, ragdoll, tối ưu."
tags: [physics, unity, gameplay]
updated: 2026-03-17
---

# ⚙️ Programming / Physics Hub

Tóm tắt: Thiết kế hệ vật lý gameplay thực dụng (controller, vehicle, ragdoll) và tối ưu collision/solver để giữ budget ổn định.

## Nội dung chính
| File | Nội dung | Khi nào dùng |
| --- | --- | --- |
| [simple-physics-engine.md](./simple-physics-engine.md) | Mini physics engine, collision/constraint cơ bản | Hiểu sâu/viết tool riêng hoặc gameplay cần tùy biến solver |
| [unity-physics-deep-dive.md](./unity-physics-deep-dive.md) | Rigidbody, collider, material, layer matrix, CCD | Chỉnh va chạm, tránh xuyên vật, tối ưu CPU/GPU |
| [character-controller.md](./character-controller.md) | Built-in vs custom controller, slope/step | Movement nhân vật chuẩn, tránh jitter/đâm tường |
| [vehicle-physics.md](./vehicle-physics.md) | Wheel Collider, arcade vs sim, input smoothing | Game đua xe/traversal cần feel chuẩn |
| [ragdoll-systems.md](./ragdoll-systems.md) | Active/partial ragdoll, blend với anim | Hit-react/death tự nhiên, kết hợp anim ↔ physics |
| [physics-optimization.md](./physics-optimization.md) | Fixed timestep, layer matrix, sleep, profiling | Giữ Physics.Update < budget, scale hàng trăm collider |

## Checklist nhanh
- [ ] Benchmark delta time & precision trước khi đổi thiết lập physics mặc định.
- [ ] Có test collision/penetration cho case quan trọng.
- [ ] Log performance bằng Profiler khi bật custom solver/CCD.
- [ ] Rõ layer matrix, collision filter để giảm broadphase.

> Link chéo: [Metrics / Unity Impact](../metrics/unity-impact-metrics.md) để đo crash/FPS khi thay đổi hệ physics.