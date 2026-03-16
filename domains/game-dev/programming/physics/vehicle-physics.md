---
title: "Vehicle Physics"
description: "Wheel Collider, arcade vs simulation, input smoothing, suspension."
tags:
  - physics
  - unity
  - vehicle
updated: 2026-03-11
---

# 🚗 Vehicle Physics (Unity)

## 1) Goals
- Điều khiển ổn định, phản hồi phù hợp thể loại (arcade vs sim).
- Giữ perf: tối ưu WheelCollider, hạn chế GC, LOD suspension.

## 2) Wheel Collider Basics
- WheelCollider = raycast-based; cần collider riêng (mesh) cho thân xe.
- **Suspension:** `Suspension Distance`, `Spring`, `Damper`; tune để tránh nhảy.
- **Forward/Sideways Friction:** dùng curve; `Extremum Slip/Value`, `Asymptote` cho drift/arcade.
- `Ackermann` steering: giảm góc bánh sau để tránh scrub.

## 3) Arcade vs Simulation
- **Arcade:**
  - Input smoothing mạnh, auto-stability (add counter yaw torque).
  - Boost/grip điều chỉnh runtime; phanh tay = tăng sideways slip.
  - Camera follow chặt; FOV tăng khi tốc độ cao.
- **Simulation:**
  - Dựa trên torque curve động cơ; gear ratio; clutch.
  - Weight shift (CG) quan trọng; tune suspension/balance.
  - ABS/Traction Control: clamp slip khi phanh/accelerate.

## 4) Custom Vehicles
- Rigidbody mass distributed; Center of Mass thấp (đặt transform).
- Anti-roll bar: apply lực đối xứng giữa bánh trái/phải.
- Downforce: AddForce theo tốc độ; clamp để không quá OP.

## 5) Input & Feel
- Đọc input Update, apply trong FixedUpdate; dùng smoothing `Mathf.MoveTowards`.
- Speed-based steering: giảm góc lái khi tốc độ cao.
- Camera sway/horizon lock để giảm say xe.

## 6) Perf & Debug
- Gizmo wheel ray, suspension length.
- Profiler: check `Physics.Simulate` cost khi nhiều wheel collider.
- LOD: disable wheel sim cho xe xa (chạy animation đơn giản).

## ✅ Apply it
- [ ] Tune WheelCollider (suspension, friction curve) phù hợp thể loại.
- [ ] Thiết lập mass/CoM, anti-roll, downforce.
- [ ] Arcade: thêm stability assist, input smoothing; Simulation: torque curve, ABS/TCS.
- [ ] Speed-based steering, camera feel; haptic rung khi drift/bump.
- [ ] LOD wheel sim, profile Physics.Update khi nhiều xe.