---
title: "Unity Optimization Playbook"
description: "Checklist 5 pha tối ưu hóa Unity: đo lường, tìm bottleneck, tối ưu code, đồ họa, memory và guardrail build."
tags:
  - unity
  - optimization
  - performance
updated: 2026-03-11
---

# 🚀 Unity Optimization Playbook

> TL;DR: **Đo đúng trước khi tối ưu.** Playbook này gom checklist 5 pha mà team có thể lặp lại mỗi sprint để giữ 60/120 FPS ổn định.

## 0. Chuẩn bị
- Bật `Development Build`, `Autoconnect Profiler`, `Deep Profiling Support` cho build QA.
- Thiết lập **Performance Budget Sheet** (CPU 6ms, GPU 8ms, Misc 2ms) và phân owner theo hệ thống.
- Tạo scene benchmark cố định để so sánh giữa các commit.

## 1. Measure – Instrument mọi thứ
| Công cụ | Khi nào dùng | Ghi chú |
| --- | --- | --- |
| **Unity Profiler** | Daily dev build | Gắn `ProfilerMarker` vào hệ thống quan trọng |
| **Frame Debugger** | Khi nghi ngờ render overload | Dò draw call, shader pass |
| **Memory Profiler** | Cuối sprint | Snapshot trước/sau gameplay dài |
| **Device Profiler (ADB/Xcode Instruments)** | Regression test | Phát hiện throttling, nhiệt, FPS drop thực tế |

**Logger mẫu:**
```csharp
using Unity.Profiling;

static class PerfMarkers
{
    public static readonly ProfilerMarker CombatUpdate = new("Combat.Update");
}

void Update()
{
    using (PerfMarkers.CombatUpdate.Auto())
    {
        // combat logic
    }
}
```

## 2. Find Bottleneck
1. So sánh `CPU.MainThread` vs `GPU` frame time.
2. Check GC Alloc spikes (`Profiler > Timeline > GC Alloc`).
3. Dùng **Module Chart** xem Physics, UI, Animation consumption.
4. Nếu spike khó tái hiện → record `.data` profilings và chia sẻ qua Slack.

| Tín hiệu | Bottleneck | Hành động |
| --- | --- | --- |
| CPU spike đều đặn mỗi 5s | GC collect | Truy tìm code tạo object trong Update/coroutine |
| GPU frame > 20ms, draw call > 2k | Render overload | Batch, giảm post-processing, atlas texture |
| Memory tăng liên tục | Leak/asset giữ lại | Addressables.Release, bỏ reference event |

## 3. Fix – Code & Gameplay Systems
- **Object Pooling:** Projectile, VFX, UI popup.
- **Burst + Jobs:** Cho math heavy (boids, path query). Luôn `Dispose()` NativeArray.
- **Async Loading:** Addressables + `AsyncOperationHandle`. Tránh block main thread khi load scene.
- **AI/Physics:** Giảm tần suất update (FixedUpdate 30hz), `Physics.BakeMesh` cho collider tĩnh.
- **UI:** Hạn chế layout rebuild, dùng `CanvasGroup` thay vì enable/disable Canvas lớn.

## 4. Polish – Graphics & Content Pipeline
| Hạng mục | Mục tiêu | Checklist |
| --- | --- | --- |
| **LOD / Imposters** | Giảm triangle count xa camera | Thiết lập LODGroup, imposters cho cây xa |
| **SRP Batcher + Instancing** | < 1,000 draw call | Đồng bộ shader variant, bật instancing cho FX |
| **Lighting** | Mixed/Baked cho static | Generate lighting trước build, hạn chế realtime shadow |
| **Texture Streaming** | RAM < 1.2GB (mobile) | ASTC/ETC compression, mipmap streaming |

## 5. Guardrail – Automation & Regression
- **CI hook:** `-batchmode -executeMethod BuildPipeline` tạo build benchmark và đo size.
- **Perf Regression Test:** Script chạy scene benchmark, log `Avg FPS`, `P95 frame time` vào dashboard.
- **Alert:** Nếu `FPS < target` >5s hoặc GC spike >10ms → fail build QA.
- **Documentation:** Update [Unity Impact Metrics](../metrics/unity-impact-metrics.md) + changelog perf.

## 6. Template Checklist cho Sprint Retro
- [ ] Có ít nhất 1 capture Profiler trước/sau tối ưu.
- [ ] GC Alloc trung bình < 1KB/frame.
- [ ] Đã test trên 3 thiết bị (low/mid/high tier).
- [ ] Performance Budget cập nhật (`/docs/perf-budget.md`).
- [ ] Lesson learned ghi lại trong retro.

## 7. Nguồn tham khảo nhanh
- [Optimization Techniques](./optimization-techniques.md) – Lý thuyết từng module.
- [Profiler Dev Build Mastery](./profiler-dev-build-mastery.md) – Cách lấy dữ liệu chính xác.
- [Game Quality Playbook](./game-quality-playbook.md) – Checklist QA/perf.
- Unity Learn: Performance Tuning, DOTS Sample Projects.