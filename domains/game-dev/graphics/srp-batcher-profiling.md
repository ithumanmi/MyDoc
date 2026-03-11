---
title: "SRP Batcher Profiling"
description: "Đo lường Scriptable Render Pipeline Batcher, capture frame profiler."
tags:
  - graphics
  - srp-batcher
  - profiling
updated: 2026-03-11
---

# 📊 SRP Batcher Profiling

## 1) Chuẩn Bị
- Dự án URP/HDRP bật `SRP Batcher` trong Graphics Settings.
- Shader phải hỗ trợ SRP Batcher (sử dụng Shader Graph/URP Lit). Kiểm tra keyword `SRPBatcher` trong inspector.
- Sử dụng build target giống platform (PC, console).

## 2) Frame Debugger Script

**SRPBatcherStats.cs**

```csharp
#if UNITY_EDITOR
using UnityEditor;
#endif

public class SRPBatcherStats : MonoBehaviour
{
#if UNITY_EDITOR
    [ContextMenu("CaptureSRPBatcherStats")]
    void Capture()
    {
        var report = new StringBuilder();
        var stats = UnityEditor.Rendering.SRPBatcherProfiler.FetchStats();
        report.AppendLine($"SRP Batcher Enabled: {stats.srpBatcherEnabled}");
        report.AppendLine($"Compatible Materials: {stats.numCompatibleMaterials}");
        report.AppendLine($"Batched Draws: {stats.numSRPBatcherDrawCalls}");
        report.AppendLine($"Non-Batched Draws: {stats.numRegularDrawCalls}");

        string path = Path.Combine(Application.dataPath, "SRPBatcherReport.txt");
        File.WriteAllText(path, report.ToString());
        Debug.Log($"Saved {path}");
    }
#endif
}
```

- Dùng context menu trong Editor để ghi log stats hiện tại.
- `UnityEditor.Rendering.SRPBatcherProfiler` có từ Unity 2022+ (URP/HDRP).

## 3) Runtime Profiler Marker

```csharp
public class SRPBatcherRuntimeHUD : MonoBehaviour
{
    GUIStyle style;

    void Awake()
    {
        style = new GUIStyle
        {
            fontSize = 16,
            normal = new GUIStyleState { textColor = Color.white }
        };
    }

    void OnGUI()
    {
#if UNITY_2022_2_OR_NEWER
        var stats = UnityEngine.Rendering.SRPBatcherProfiler.GetStats();
        GUILayout.BeginArea(new Rect(10, 10, 400, 120));
        GUILayout.Label($"SRP Batcher Enabled: {stats.srpBatcherEnabled}", style);
        GUILayout.Label($"Batched Draws: {stats.numSRPBatcherDrawCalls}", style);
        GUILayout.Label($"Regular Draws: {stats.numRegularDrawCalls}", style);
        GUILayout.Label($"Materials Compatible: {stats.numCompatibleMaterials}", style);
        GUILayout.EndArea();
#endif
    }
}
```

- Build-in overlay hiển thị stats runtime (đặt vào dev build).

## 4) Workflow Profiling
1. Bật Frame Debugger (Editor) → filter `SRP Batcher` events.
2. Dùng `GPU Profiler` để xem draw call grouping.
3. Capture RenderDoc frame → inspect draw call order.
4. Kiểm tra material/shader: bỏ keyword dynamic, enable SRP Batcher.

## 5) Checklist
- Shader Graph: bật `Support SRP Batcher` (default).
- Material property block: tránh update per-frame nếu không cần.
- Mesh Renderer batching: combine layers/culling.
- Profiling log commit: `SRPBatcherReport_<date>.txt`.

## ✅ Apply it
- [ ] Bật SRP Batcher trong project settings.
- [ ] Viết script capture stats (Editor + runtime HUD).
- [ ] Capture frame (Frame Debugger/RenderDoc) và note draw calls.
- [ ] Tối ưu shader/material để tăng compatible count.
- [ ] Lưu báo cáo và share với team trước milestone.