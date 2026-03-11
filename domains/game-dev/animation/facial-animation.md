---
title: "Facial Animation"
description: "Blend shapes, lip sync, emotions, LOD/perf."
tags:
  - animation
  - facial
  - unity
updated: 2026-03-11
---

# 🙂 Facial Animation

## 1) Goals
- Lip sync rõ, biểu cảm nhất quán, không uncanny.
- Tối ưu: LOD cho distant NPC; tránh tốn CPU/GPU không cần.

## 2) Blend Shapes vs Bones
- Blend shapes: dễ author, chính xác cho khuôn mặt; tốn memory/vertex morph.
- Bone-based: nhẹ hơn, phù hợp stylized; khó đạt chi tiết micro.
- Hybrid: shape cho miệng/mắt, bone cho jaw/brow lớn.

## 3) Lip Sync
- Pipeline: audio → phoneme → viseme mapping; dùng tool (Oculus Lipsync, Rhubarb, FaceFX) hoặc DNN.
- Curate viseme set (~12–15 viseme); smooth transition, tránh pop.
- Offset head motion nhỏ; sync với body timing; cắt tiếng thở/khóe miệng để tự nhiên.

## 4) Emotions & Posing
- Library emotion: neutral/happy/angry/sad/surprise/fear; intensity slider.
- Pose space: blend có clamp để tránh méo; additive layer cho micro-expression.
- Eye: blink random có noise; eye dart nhẹ; look-at target với clamp để tránh đảo mắt cực đoan.

## 5) Runtime & Perf
- LOD: tắt lip sync/eye dart cho NPC xa; giảm blend count; dùng impostor nếu cần.
- Update rate: giảm tick facial ở NPC nền (2–4 fps) thay vì mỗi frame.
- GPU skinning: kiểm tra cost blend shape; atlas/mesh split hợp lý.

## 6) Audio-VO Pipeline
- Voice-over: cần text + timecode; handle localization (viseme map ngôn ngữ khác).
- Cập nhật font/arabic/bidi nếu UI subtitle liên quan; giữ sync sub/VO.

## ✅ Apply it
- [ ] Chọn blend shape/bone/hybrid; số viseme hợp lý, smooth.
- [ ] Pipeline lip sync rõ (tool/NN) + emotion library.
- [ ] Eye blink/dart tự nhiên, clamp look-at.
- [ ] LOD facial: tắt/giảm tick NPC xa; kiểm tra GPU cost.
- [ ] VO pipeline: map viseme đa ngôn ngữ; đồng bộ subtitle/timecode.