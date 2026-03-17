---
title: "Art-Tech / Graphics"
description: "Hub: Graphics & Tech Art – shader, SRP, post, profiling."
tags: [graphics, shaders, unity, srp]
updated: 2026-03-17
---

# 🌈 Art-Tech / Graphics Hub

Tóm tắt: Chuẩn hóa pipeline đồ họa (URP/HDRP), shader, post-processing và profiling để đội Tech Art làm việc nhất quán.

## Nội dung chính
| File | Nội dung | Khi nào dùng |
| --- | --- | --- |
| [shader-programming.md](./shader-programming.md) | HLSL/Shader Graph + tips VFX | Làm nền tảng shader, style guide LUT/ramp |
| [render-pipelines.md](./render-pipelines.md) | So sánh URP vs HDRP, cấu hình | Chốt pipeline cho mobile/console/PC |
| [post-processing-stack.md](./post-processing-stack.md) | Bloom, color grading, DOF, motion blur | Thiết lập look & feel cinematic |
| [custom-render-passes.md](./custom-render-passes.md) | ScriptableRendererFeature, HDRP Custom Pass | Thêm effect đặc thù vào SRP |
| [art-direction-tech.md](./art-direction-tech.md) | Stylized/NPR, lighting pipeline | Đồng bộ hướng mỹ thuật + kỹ thuật |
| [shader-graph-capture.md](./shader-graph-capture.md) | Bắt output SG thành texture | Bake LUT/ramp/flowmap cho style guide |
| [srp-batcher-profiling.md](./srp-batcher-profiling.md) | Script capture stats, runtime HUD | Theo dõi hiệu quả SRP Batcher |
| [renderdoc-capture.md](./renderdoc-capture.md) | RenderDoc integration, CLI capture | Phân tích draw call, pipeline state |
| [ci-screenshot-automation.md](./ci-screenshot-automation.md) | Graphics test + RenderDoc automation | Screenshot regression trong CI |

## Playbook nhanh
1) Chọn pipeline (URP/HDRP) → khóa spec dự án.  
2) Dùng `shader-programming.md` để chuẩn hóa naming + LUT/ramp.  
3) Lặp effect theo checklist trong [../vfx/trig-shaders.md](../vfx/trig-shaders.md); log FPS trong [Unity Impact Metrics](../../production/metrics/unity-impact-metrics.md).

> Phối hợp với [Unity Deep Dive / VFX & Lighting](../../production/unity-deep-dive/vfx-lighting-mastery.md) để đồng bộ lighting + shader.