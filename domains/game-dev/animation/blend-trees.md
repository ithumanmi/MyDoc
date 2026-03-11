---
title: "Blend Trees"
description: "1D/2D blend, locomotion systems, parameter smoothing, foot IK."
tags:
  - animation
  - unity
  - blend-tree
updated: 2026-03-11
---

# 🌳 Blend Trees (Unity)

## 1) Goals
- Locomotion mượt, không popping; param sạch, normalize tốc độ.
- 1D cho tốc độ; 2D (Freeform/Catmull-Rom) cho strafe/diagonal.

## 2) 1D Blend (Speed)
- Param: speedNormalized (0..1) hoặc m/s map vào 0..1.
- Clip: Idle, Walk, Run, Sprint; thêm Start/Stop optional (dùng transition). 
- Smoothing: damp SetFloat (Animator) hoặc dùng low-pass trong code để tránh jitter.

## 3) 2D Blend (Strafe/Diagonal)
- Param: moveX/moveY (đã normalized theo max speed); dùng 2D Freeform Directional.
- Thêm clip diagonal (Fwd-Right/Left, Back-Right/Left) để tránh kéo dài blend path.
- Center: Idle; tránh lỗ trống giữa space.

## 4) Foot IK & Root Motion
- Bật Foot IK cho locomotion tree; tắt ở montage đặc biệt nếu kéo chân.
- Root motion: đảm bảo tốc độ clip khớp gameplay speed; nếu in-place, sync speed bằng code (character controller/physics).

## 5) Param Hygiene
- Clamp 0..1; tránh noise input; deadzone nhỏ cho gamepad.
- Đừng set param mỗi frame nếu không đổi; giảm GC.
- Hash param: Animator.StringToHash.

## 6) Testing
- Quan sát chân trượt: mismatch speed hoặc root motion scaling.
- Frame-by-frame: check chuyển hướng chéo; tránh pose weird ở blend center.
- Device perf: blend tree lớn tốn CPU; cân nhắc đơn giản hóa cho NPC.

## ✅ Apply it
- [ ] Normalize speed và clamp param; damp để tránh jitter.
- [ ] 2D blend có clip diagonal, center Idle; không để lỗ trống.
- [ ] Foot IK bật cho locomotion; kiểm tra root motion vs in-place.
- [ ] Hash param, chỉ set khi đổi; tối ưu cho NPC.
- [ ] Playtest đổi hướng nhanh và sprint/stop xem có popping/foot slide.