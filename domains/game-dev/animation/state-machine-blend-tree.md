---
title: "State Machine, Blend Tree & Root Motion"
description: "Thiết kế state machine, blend tree và root motion để animation mượt, phản hồi tốt."
tags:
  - animation
  - unity
updated: 2026-03-11
---

# 🧭 State Machine, Blend Tree & Root Motion

> [← Back to Animation Module](./README.md)

Mục tiêu: giảm jitter, loại bỏ popping, tăng tính phản hồi (responsiveness) của chuyển động nhân vật.

## 1) State Machine Design
**Nguyên tắc:** rõ entry/exit, ít nhánh chéo, có tầng locomotion riêng.

- **Phân tầng:** `Base Locomotion` (Idle/Walk/Run/Sprint) tách khỏi `Combat`/`Ability`. Dùng layer override để chồng vũ khí.
- **Transition clarity:** đặt **Exit Time** = 0 cho state phản ứng (hit-react, dodge), dùng `Has Exit Time` cho clip vòng lặp (idle).
- **Conditions tối thiểu:** 1–2 parameter chính (speed, isGrounded) + 1 parameter sự kiện (attackTrigger). Tránh >3 điều kiện/transition.
- **Any State:** chỉ dùng cho interrupt khẩn (stun/kill). Hạn chế dùng cho attack để tránh spam.
- **Buffer input:** lưu input trong 0.1–0.2s để transition mượt (combo, jump). 
- **Root motion vs code-driven:** hành động chính xác vị trí (vault, climb) dùng root motion + match target; di chuyển tự do dùng code-driven (character controller + animation driven speed).

### Checklist debug state machine
- [ ] Mỗi transition có condition rõ ràng, không trùng lặp logic.
- [ ] Không có vòng lặp vô hạn (idle → walk → idle trong 1 frame).
- [ ] Bật `Animator.LogWarnings` để bắt missing parameter.
- [ ] Dùng `Animator.SetFloat` với damping (`SmoothDamp`) để tránh jitter speed.

## 2) Blend Tree Essentials
**Mục tiêu:** trộn clip mượt khi đổi tốc độ/ hướng.

- **1D Blend (speed):** Idle ↔ Walk ↔ Run; giá trị speed lấy từ magnitude của velocity. Dùng **Start/Stop threshold** khớp thực tế.
- **2D Freeform Directional:** X/Z lấy từ input hoặc velocity đã xoay theo hướng nhân vật. Bảo đảm clip quay 45°/90° đủ để không đứt gãy.
- **Stride warping:** nếu có, dùng để giữ chân bám đất khi tốc độ thay đổi.
- **Turn-in-place:** thêm node turn-in-place 90°/180° cho camera-turn khi speed thấp.

### Checklist blend tree
- [ ] Tốc độ mô phỏng (root motion speed) khớp với tốc độ game (nav/char controller).
- [ ] Clip có chân khóa (foot lock) khi chuyển giữa Idle ↔ Walk.
- [ ] Đã bật `Foot IK` nếu phù hợp, hoặc tự kiểm soát trong rig.
- [ ] Test với gamepad + chuột để đảm bảo góc quay mượt.

## 3) Root Motion Best Practices
- **Match Target:** dùng `Animator.MatchTarget` cho vault/ledge grab để khớp vị trí tay/chân với môi trường.
- **Authoring:** dựng clip có root node sạch, không drift; bake root motion chuẩn.
- **Slope handling:** thêm curve chỉnh tốc và độ nghiêng; kết hợp foot IK để tránh trượt.
- **Network:** trong multiplayer, cân nhắc chạy simulation code-driven và dùng animation chỉ để hiển thị (authority ở server).

### Checklist root motion
- [ ] Clip root không bị drift, pivot đúng tâm.
- [ ] Match target có mask x/y/z đúng (tránh kéo sai trục).
- [ ] Ragdoll/physics chuyển đổi mượt (enable kinematic → non-kinematic).

## 4) Tooling & Debug
- **Animator Debug:** bật `Parameters` + `Layers` trong Game view; dùng `Debug.DrawRay` hiển thị hướng di chuyển vs hướng nhìn.
- **Playables/Graph:** với nhân vật phức tạp, cân nhắc dùng `PlayableGraph` để tổ hợp layer/stack dynamic.
- **Profiling:** check `Animator.Update` & `Animator.Render` trong Profiler; tránh dùng quá nhiều layer/IK job.

## 5) Apply It
1) Tạo base locomotion blend tree (Idle/Walk/Run) dùng velocity magnitude.
2) Thêm turn-in-place + start/stop để giảm chân trượt.
3) Thêm combat layer override; Any State chỉ cho stun/death.
4) Thử root motion cho vault/climb + MatchTarget; đo sai lệch vị trí < 5cm.
5) Bật foot IK + stride warp; review trên dốc 15°/30°.

## 🔗 Cross-reference
- [inverse-kinematics.md](./inverse-kinematics.md): Foot/hand IK phối hợp root motion.
- [../unity-deep-dive/character-controller.md](../unity-deep-dive/character-controller.md) (nếu có): sync physics + animation.