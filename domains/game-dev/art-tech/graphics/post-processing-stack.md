---
title: "Post Processing Stack"
description: "Cấu hình bloom, color grading, DOF, motion blur cho URP/HDRP."
tags:
  - graphics
  - post-processing
  - unity
updated: 2026-03-11
---

# ✨ Post Processing Stack

## 1) Bloom
- Mục tiêu: thêm glow highlight → scale intensity theo HDR value.
- Tham số chính: Threshold, Intensify, Scatter, Tint.
- URP: `Bloom` trong Volume Profile; dùng high quality để tránh flicker.
- HDRP: hỗ trợ anamorphic bloom (x/y stretch), dirt mask.
- Performance: ảnh hưởng fillrate → giảm resolution (upscale) hoặc dùng selective bloom (mask).

## 2) Color Grading
- Quy tắc: làm việc trong HDR linear, sau đó apply tone mapping (ACES, Neutral).
- LUT 32x32x32 (HDRP) hoặc 16x16x16 (URP). Export LUT từ Photoshop/LutCalc.
- Layer order: Exposure → White Balance → Color Adjustments → Channel Mixer → Shadows/Midtones/Highlights → Tone mapping.
- Tips: lock reference target, snapshot screenshot “before/after” để QA.

## 3) Depth of Field (DOF)
- URP: Gaussian DOF (Foreground/Background); HDRP: Advanced DOF (Bokeh shape, Aperture).
- Tham số: Focus Distance, Focal Length, Aperture.
- Sử dụng focus puller script để follow subject (Raycast camera → dynamic focus).
- Mobile: thay DOF bằng fake blur (UI overlay) để tiết kiệm.

## 4) Motion Blur
- URP: Camera Motion Blur; HDRP: cả Camera lẫn Object Motion Blur (per renderer velocity).
- Tối ưu: clamp max blur samples, disable cho UI camera.
- Gameplay: disable blur khi player hiện UI quan trọng (sniper zoom, menus).

## 5) Volume Workflow
- Sử dụng Global Volume (base look) + Local Volume (zone-specific: interior, boss arena).
- Stack: Global → Local (Blend Distance) → Camera override.
- Profile versioning: clone profile theo scene → gắn suffix `_profile_v2` khi tweak.
- Debug: `Window > Rendering > Debugger` xem active post stack.

## ✅ Apply it
- [ ] Thiết lập Volume Profile (Global/Local) với bloom, grading, DOF, blur.
- [ ] Tone mapping consistent (ACES/Neutral) + LUT workflow.
- [ ] Script focus puller/motion blur toggle cho gameplay critical moments.
- [ ] Benchmark GPU timing (RenderDoc/Unity Profiler) khi bật stack.
- [ ] Template profile lưu trong repo để tái sử dụng.