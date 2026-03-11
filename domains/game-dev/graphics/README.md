---
title: "Graphics & Tech Art Module"
description: "Shader, render pipeline và workflow Technical Artist cho Unity."
tags:
  - graphics
  - shaders
  - unity
updated: 2026-03-11
---

# 🌈 Graphics & Tech Art Module

| File | Nội dung | Khi nào dùng |
| --- | --- | --- |
| [shader-programming.md](./shader-programming.md) | Nền tảng HLSL/Shader Graph + tips VFX | Bước vào con đường Technical Artist |
| [trig-shaders.md](./trig-shaders.md) | Water/Fire effect dùng lượng giác | Làm effect tùy biến high-fidelity |
| [render-pipelines.md](./render-pipelines.md) | So sánh URP vs HDRP, cấu hình pipeline | Quyết định pipeline cho dự án mobile/console |
| [post-processing-stack.md](./post-processing-stack.md) | Bloom, color grading, DOF, motion blur | Thiết lập look cinematic/tuning feel |
| [particle-systems.md](./particle-systems.md) | Shuriken vs VFX Graph, tối ưu | Lựa chọn pipeline VFX và quản lý performance |
| [custom-render-passes.md](./custom-render-passes.md) | ScriptableRendererFeature, HDRP Custom Pass | Inject effect đặc biệt vào SRP |
| [art-direction-tech.md](./art-direction-tech.md) | Stylization, NPR, lighting pipeline | Đồng bộ hướng mỹ thuật + kỹ thuật |
| [shader-graph-capture.md](./shader-graph-capture.md) | Bắt output Shader Graph thành texture | Bake LUT/ramp/flowmap cho style guide |
| [srp-batcher-profiling.md](./srp-batcher-profiling.md) | Script capture stats, runtime HUD | Theo dõi hiệu quả SRP Batcher |
| [renderdoc-capture.md](./renderdoc-capture.md) | RenderDoc integration, CLI capture | Phân tích draw call, pipeline state |
| [ci-screenshot-automation.md](./ci-screenshot-automation.md) | Graphics test + RenderDoc automation | Screenshot regression trong CI |

**Playbook:**
1. Chọn pipeline (URP/HDRP) → khóa spec.
2. Dùng `shader-programming.md` để chuẩn hóa naming + LUT.
3. Lặp effect theo checklist trong `trig-shaders.md`, log FPS trong [metrics](../metrics/unity-impact-metrics.md).

> Phối hợp với [Unity Deep Dive / VFX & Lighting](../unity-deep-dive/vfx-lighting-mastery.md) để đồng bộ lighting + shader.