---
title: "FPS Mastery – Đo & Tối Ưu Frame Rate"
description: "Hướng dẫn theo dõi FPS, thiết lập ngưỡng mục tiêu và xử lý bottleneck trong Unity."
tags:
  - metrics
  - fps
  - optimization
updated: 2026-03-11
---

# ⚡ FPS Mastery – Đo & Tối Ưu Frame Rate

## 1. Vì sao FPS quan trọng?
- **Input latency** tỉ lệ nghịch với FPS: 30 FPS ≈ 33ms/frame, 60 FPS ≈ 16.6ms.
- **Retention & monetization**: user rời bỏ game mobile nếu FPS < 45 trong combat.
- **Store requirement**: Apple/Google yêu cầu game ổn định ≥ 30 FPS cho submission.

## 2. Ngưỡng mục tiêu theo nền tảng
| Platform | Target FPS | Hard floor |
| --- | --- | --- |
| Mobile casual/hybrid | 60 | 45 |
| Mobile midcore / competitive | 90 (120 nếu flagship) | 60 |
| PC/Console | 60 (Campaign) / 120 (Shooter) | 60 |
| VR | 90 / 120 | 72 |

> **Tip:** đặt `QualitySettings.vSyncCount = 0` khi benchmark để tránh bị lock theo monitor.

## 3. Quy trình đo FPS trong Unity
1. **Dev Build + Profiler:** bật Deep Profile khi cần phân rã function.
2. **Frame Debugger:** xem render pipeline, draw call per frame.
3. **Unity Analytics/Backend:** log `Application.targetFrameRate`, `Time.deltaTime`, GPU time.
4. **Device farm:** dùng Android Profiler/Xcode Instruments để đo real device.

```csharp
using UnityEngine;

public class FpsCounter : MonoBehaviour
{
    [SerializeField] int sampleSize = 60;
    float timer;
    int frames;

    void Update()
    {
        frames++;
        timer += Time.unscaledDeltaTime;
        if (frames >= sampleSize)
        {
            var fps = Mathf.RoundToInt(frames / timer);
            Debug.Log($"FPS: {fps}");
            frames = 0;
            timer = 0f;
        }
    }
}
```

## 4. Phân tích bottleneck
| Dấu hiệu | Nguyên nhân | Hướng xử lý |
| --- | --- | --- |
| CPU frame time cao (>16ms) | Physics, GC alloc, script nặng | Job/Burst, Object Pooling, giảm `Update` allocations |
| GPU frame time cao | Shader phức tạp, overdraw, post-processing | Batching, LOD, giảm transparency |
| Thời gian loading dài | Asset lớn, chưa dùng Addressables | Streaming asset, compress texture |
| Spike bất thường | Serialization, async chưa await đúng | Profiler Timeline, đặt marker |

## 5. Playbook tối ưu
1. **Budget frame:** chia 16ms thành Gameplay (6ms) + Render (8ms) + Misc (2ms).
2. **Instrumentation:** gắn Custom Profiler Marker (`ProfilerMarker marker = new("Combat.Update");`).
3. **Giảm GC alloc:** dùng `List<T>.Clear()` thay vì tạo mới, tránh `string.Format` trong Update.
4. **Batching:** bật SRP Batcher, dùng instancing cho FX.
5. **Adaptive Quality:** scale VFX/LOD dựa trên real-time FPS (xem `Adaptive Performance`).

## 6. Báo cáo KPI
- Export từ Profiler → CSV, đính kèm vào [Unity Impact Metrics](./unity-impact-metrics.md).
- Theo dõi chỉ số: `Avg FPS`, `P95 FPS`, `FPS < Target (%)`.
- Đặt alert khi `FPS < 50` kéo dài 5s.

## 7. Checklist trước khi ship
- [ ] Test trên 3 cấu hình thiết bị đại diện.
- [ ] FPS log tích hợp vào build QA.
- [ ] Ghi chú thay đổi ảnh hưởng FPS trong changelog.
- [ ] Có kế hoạch hotfix nếu FPS tụt sau update.

---
**Resources:**
- Unity Profiler Docs
- Adaptive Performance Samples
- DOTS & Burst Optimization Guide