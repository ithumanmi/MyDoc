---
title: "Physics Optimization"
description: "Fixed timestep, layer matrix, sleep, batching, profiling."
tags:
  - physics
  - unity
  - optimization
updated: 2026-03-11
---

# ⚡ Physics Optimization

## 1) Fixed Timestep & Update Budget
- `Time.fixedDeltaTime`: 0.02s (50Hz) mặc định. Thay đổi phải đồng bộ input/animation.
- Combat/hit-scan nhanh: 0.0167 (60Hz) hoặc 0.01 (100Hz) nhưng tốn CPU.
- `Maximum Allowed Timestep`: 0.1s hoặc thấp hơn để tránh spiral of death.
- Logic nặng chuyển sang job, tránh trong FixedUpdate.

## 2) Layer Collision Matrix
- Tắt cặp collision không cần: UI, VFX, teammate projectiles.
- Sử dụng `Physics.IgnoreLayerCollision` runtime cho state đặc biệt (ghost, dash) thay vì toggle collider.
- Giảm sát collision = giảm broadphase/sap chi phí.

## 3) Sleep & Deactivation
- Set `Sleep Threshold` hợp lý; vật không cần active → `isKinematic` hoặc disable collider.
- Dynamic pool: khi object rời camera xa, disable rigidbody/ collider.
- Wake bằng `Rigidbody.WakeUp()` khi tái sử dụng.

## 4) Batching & Queries
- Raycast/SphereCast dùng `NonAlloc`; reuse array; tránh `new` mỗi frame.
- Combine static mesh collider bằng `StaticBatchingUtility.Combine` hoặc GPU instancing.
- Jobify queries (Unity Physics package) hoặc DOTS nếu cần scale lớn.

## 5) Profiling
- Unity Profiler: track `Physics.Update`, `Physics.Simulate`, `FixedUpdate.Physics`.
- Deep Profile off; dùng Profiler Marker `Physics.Step`.
- Capture worst-case: nhiều collider, ragdoll, vehicle.
- Sử dụng `Physics Debug` visualization (Window → Analysis → Physics Debug) xem layer/lỗi collision.

## 6) Platform-specific
- Mobile: giảm fixed timestep hoặc limit collider count; disable cloth/softbody.
- Console: chia layer cho CPU/GPU thread. PS5/XSX → 120Hz mode cần double-check fixed timestep.
- PC low-end: expose slider “Physics Quality” (solver iteration, ragdoll count).

## ✅ Apply it
- [ ] Điều chỉnh fixedDeltaTime & Max Allowed Timestep phù hợp thể loại và target FPS.
- [ ] Dọn Layer Collision Matrix, dùng IgnoreLayerCollision khi cần.
- [ ] Bật sleep/kinematic cho object idle; pool rigidbody.
- [ ] Queries dùng NonAlloc; batch static colliders.
- [ ] Profile Physics.Update < budget (ví dụ <3ms), capture worst-case.