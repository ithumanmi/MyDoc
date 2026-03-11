---
title: "Unity Physics Deep Dive"
description: "Rigidbody, Collider, layers, CCD, performance tuning cho gameplay mượt và chính xác."
tags:
  - physics
  - unity
updated: 2026-03-11
---

# 🛠️ Unity Physics Deep Dive

> [← Back to Physics Module](./README.md)

Mục tiêu: tránh jitter, xuyên vật (tunneling), tối ưu CPU khi số lượng collider lớn.

## 1) Rigidbody & Collider Setup
- **Rigidbody:** Dynamic cho vật di động; Kinematic cho vật di chuyển bằng script/animation; Static không có Rigidbody.
- **Interpolation:** bật cho nhân vật để mượt khi camera theo sau; tắt cho vật bị raycast nhiều (đỡ trễ). 
- **Collision Detection:** Discrete (rẻ), Continuous (nhanh vừa), Continuous Dynamic (đắt nhưng tránh xuyên vật cho vật nhanh).
- **Collider shape:** dùng primitive (Box/Sphere/Capsule) tối đa; Mesh Collider chỉ khi cần và nên là convex. 
- **Layers:** thiết lập Matrix va chạm, tắt các cặp không cần (UI, VFX, projectiles đồng phe…).

### Checklist setup
- [ ] Rigidbody trọng tâm hợp lý (Center of Mass) và tránh scale bất đối xứng.
- [ ] Collider khớp pose chính; có thể thêm child colliders cho chi tiết (hitbox head/limb).
- [ ] Continuous/CCD bật cho projectile nhanh; Discrete cho vật chậm/ít quan trọng.
- [ ] Layer Collision Matrix tối giản, không để mặc định mọi thứ va nhau.

## 2) Character & Movement
- **CharacterController vs Rigidbody:** 
  - CharacterController: dễ kiểm soát, không chịu lực vật lý tự nhiên; cần xử lý step offset/slope.
  - Rigidbody: tuân lực, cần code ổn định (AddForce/MovePosition) và constraint rotation.
- **Ground check:** Raycast/SphereCast với layer mask, đệm độ cao 0.05–0.1m; tránh dùng `OnCollisionStay` cho logic chính.
- **Slope limit:** chặn input khi vượt slope angle; bật slide có kiểm soát.
- **Step offset:** cho phép bước qua bậc thang nhỏ (0.3–0.4m) bằng capsule cast nâng nhẹ chân.

## 3) Contacts, Triggers, Queries
- **Queries Hit Backfaces:** tắt nếu không cần; bật khi cần bắn ray từ trong ra.
- **Reuse colliders:** tránh tạo/destroy collider runtime; bật/ tắt `enabled` hoặc pool object.
- **Physics Queries:** dùng `RaycastNonAlloc` hoặc `SphereCastNonAlloc` để giảm GC.
- **Continuous + Raycast:** với projectile, dùng raycast sweep + Rigidbody Continuous để giảm xuyên vật.

## 4) Performance Tuning
- **Fixed Timestep:** 50Hz (0.02s) mặc định; tăng lên 60–90Hz cho game combat nhanh, hoặc giảm nếu CPU căng. Giữ `Max Allowed Timestep` thấp để tránh spiral of death.
- **Solver Iterations:** `Default Solver Iterations` / `Velocity Iterations`: tăng khi cần rigidbody stack ổn định; giảm nếu quá tốn CPU.
- **Broadphase:** bật `Use Enhanced Determinism` nếu cần tính lặp lại (replay/netcode) nhưng tốn CPU.
- **Sleeping:** bật `Sleep Threshold` hợp lý để vật tĩnh không tốn CPU.

### Checklist perf
- [ ] Profile `Physics.Update` trong Profiler ở worst-case (nhiều collider).
- [ ] Dùng primitive collider; mesh collider được đánh dấu convex; static mesh nên Combine.
- [ ] FixedUpdate không chứa logic nặng; chuyển sang job/async nếu cần.
- [ ] Garbage free: dùng NonAlloc casts, tránh `new` trong FixedUpdate.

## 5) Stability & Netcode
- **Authority:** server là nguồn sự thật; client-side prediction cho movement, server reconciliation để sửa sai.
- **Determinism:** Unity PhysX không hoàn toàn deterministic giữa máy; lưu snapshot/rollback nếu cần netcode.
- **Tick vs Render:** Render mượt bằng interpolate/extrapolate transform; logic vật lý ở FixedUpdate.

## 6) Apply It
1) Audit layer matrix, tắt cặp không cần; chuyển collider sang primitive.
2) Bật Continuous/CCD cho projectile nhanh; giữ Discrete cho còn lại.
3) Chỉnh Fixed Timestep (0.016–0.02) và solver iteration theo thể loại game; đo CPU.
4) Dùng RaycastNonAlloc cho ground check & hit detection; tránh GC.
5) Profiling: Physics.Update < 2–3 ms/frame trên target hardware.

## 🔗 Cross-reference
- [simple-physics-engine.md](./simple-physics-engine.md): Hiểu sâu solver/collision.
- [../unity-deep-dive/character-controller.md](../unity-deep-dive/character-controller.md) (nếu có): So sánh controller vs Rigidbody.
- [../metrics/unity-impact-metrics.md](../metrics/unity-impact-metrics.md): Đo FPS/CPU khi chỉnh physics.