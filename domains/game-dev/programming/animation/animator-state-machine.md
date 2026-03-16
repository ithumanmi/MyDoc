---
title: "Animator State Machine"
description: "Unity Animator architecture, layers, sub-state machines, parameters & transitions."
tags:
  - animation
  - unity
  - state-machine
updated: 2026-03-11
---

# 🏗️ Animator State Machine (Unity)

## 1) Goals
- Rõ ràng layer/sub-SM: giảm transition chéo lộn xộn, dễ debug.
- Ít parameter, có debounce/threshold; tránh spam trigger gây stuck.

## 2) Kiến trúc đề xuất
- Layer tách: Base Locomotion, Upper-body (aim/fire), Additive (breathing/recoil), Facial nếu cần.
- Sub-state machine (SSM): Idle/Move, Combat, Hit/Death, Special (climb/vault).
- Entry flow: Any State tối thiểu; ưu tiên transition từ SSM cụ thể để tránh giật.

## 3) Parameters
- Core: speed (float, normalized 0..1 hoặc m/s), direction/strafe (float), isGrounded (bool), isAiming (bool), trigger Fire/Reload, hitReact (trigger/int).
- Debounce trigger: dùng Bool + reset trong code, hoặc Trigger + transition có Exit Time/hasExitTime off và cooldown.
- Normalize speed: map m/s → 0..1 cho blend tree; tránh logic trùng lặp.

## 4) Transitions & Conditions
- Hạn chế Any State; dùng từ Idle/Move SSM khi có thể.
- Transition duration ngắn cho action; 0 thời gian nếu dùng root motion cần bám sát.
- Interrupt: cho phép hit-react/breakout nhưng có priority; tránh vòng lặp hit-lock.
- Foot IK toggle: bật ở locomotion; tắt ở montage đặc biệt nếu gây kéo chân.

## 5) Debug & Perf
- Animator window: tránh >100 parameter; nhóm bằng prefix (Loc_, Cmb_, Sys_).
- Log mismatched param: guard code khi SetFloat/SetBool.
- Culling Mode: Based on Renderers; cho NPC off-screen.
- GC: Set by hash (Animator.StringToHash).

## ✅ Apply it
- [ ] Tách layer (locomotion/upper/additive) và SSM (idle-move/combat/hit/special).
- [ ] Giảm Any State; dùng điều kiện rõ + thời gian transition ngắn.
- [ ] Param tối thiểu, normalized; debounce trigger để tránh spam.
- [ ] Ưu tiên interrupt cho hit-react/breakout có kiểm soát.
- [ ] Bật foot IK nơi cần, culling cho NPC, set param bằng hash.