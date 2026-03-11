---
title: "Animation Rigging"
description: "Runtime rigging, IK, procedural aim, order, perf."
tags:
  - animation
  - unity
  - rigging
updated: 2026-03-11
---

# 🦴 Animation Rigging (Unity)

## 1) Goals
- Bổ sung procedural control (aim/IK/two-bone) mà không phá base anim.
- Giữ perf: order đúng, limit constraint, tránh GC.

## 2) Constraints Thường Dùng
- Two-Bone IK: tay/chân bám vũ khí/điểm bám; set hint để tránh gập sai.
- Multi-Aim: điều khiển xương spine/neck/weapon để aim theo camera.
- Multi-Parent/Position: attach props (arrow, shield) runtime.
- Chain IK/CCD: rope/tail; dùng tiết kiệm.

## 3) Order & Layers
- Rig Builder order: base anim → additive → rig constraints → VFX/override.
- Layer hóa: Rig cho Aim, Rig cho Hands IK, Rig cho Props; có thể bật/tắt rig layer.
- Weight blending: lerp weight thay vì bật/tắt ngay; tránh snap.

## 4) Data & Control
- Driven by gameplay: lấy target từ camera raycast/weapon socket.
- Limit: clamp angle, damp/lerp để tránh jitter khi camera rung.
- Author reference pose chuẩn, reset rig khi mất target.

## 5) Performance
- Giảm số constraint; disable rig khi off-screen/NPC xa.
- Burst/Jobs: bật nếu dùng Animation Rigging package phiên bản hỗ trợ.
- Pool targets (Transform) thay vì tạo/destroy.

## 6) Debug
- Gizmo/hitbox: hiển thị target aim; kiểm tra clip-through.
- Foot IK conflict: đảm bảo order; tắt rig nếu additive gây trượt chân.

## ✅ Apply it
- [ ] Tách rig theo chức năng (aim/hands/props), blend weight mượt.
- [ ] Clamp/damp target để tránh jitter; reset khi mất target.
- [ ] Bật Burst/Jobs, disable rig cho NPC xa; hạn chế constraint dư.
- [ ] Kiểm tra foot IK vs rig order, tránh snap.
- [ ] Pool target transform, không spawn/destroy liên tục.