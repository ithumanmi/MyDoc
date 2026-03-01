# 🔍 Unity Profiler & Dev Build Mastery

> [← Back to Game Development Roadmap](../README.md)

Muốn tối ưu game, bạn phải đo được mọi thứ. Bài viết này hướng dẫn cách **làm chủ Unity Profiler** và tận dụng **Dev Build Mode** để phát hiện bottleneck sớm nhất.

---

## 1. Khi nào cần dùng Profiler?

| Tình huống | Công cụ Profiler | Câu hỏi cần trả lời |
| --- | --- | --- |
| FPS tụt bất thường | CPU/GPU Module | Có phải CPU hay GPU bottleneck? |
| Hệ thống loading chậm | Timeline + Memory | Có allocation spike hoặc IO blocking? |
| Lỗi hitch/lag ngắn | Hierarchy + Profiler Recorder | DrawCall tăng đột ngột? GC spike? |
| Game crash/ANR | Profiler + Dev Build logs | Có coroutine/blocking nào kéo dài? |

> **Rule of thumb:** Profile ngay từ prototype, đừng đợi build cuối cùng mới đo.

---

## 2. Thiết lập Dev Build chuẩn

### 2.1 Build Settings
* Bật **Development Build**: cho phép Profiler attach, bật define `DEVELOPMENT_BUILD`.
* Tick **Autoconnect Profiler** khi build để Profiler tự kết nối khi chạy.
* Bật **Deep Profiling Support** khi cần đo chi tiết (nhưng rất chậm, dùng cho QA).

### 2.2 Logging & Diagnostics
* `Application.SetStackTraceLogType(LogType.Error, StackTraceLogType.Full);`
* Kích hoạt **Script Debugging** nếu cần attach debugger C#.
* Tạo **Dev Console** trong game để bật/tắt overlay performance, log command.

### 2.3 Feature Flags
* Sử dụng define symbol `DEV_BUILD` để bật tính năng debug (telemetry overlay, skip tutorial) mà không xuất hiện ở release.

```csharp
#if DEV_BUILD
DebugHUD.Instance.Show();
#endif
```

---

## 3. Unity Profiler Modules cần nắm

| Module | Mục đích | Lưu ý |
| --- | --- | --- |
| Timeline | Toàn cảnh frame | Nhìn spike, double-click để drill down |
| CPU Usage | Phân rã theo subsystem | Bật Hierarchy để xem script cụ thể |
| GPU Usage | Render thread & GPU | Cần GPU profiling enabled trong Player Settings |
| Memory | Heap, Textures, Mesh, GC | So sánh snapshot trước/sau scene |
| Physics | Collision, Solver | Theo dõi số collider, Active bodies |
| Rendering | Batches, SetPass, Shadow casters | Đánh giá draw call, overdraw |
| Profiler Recorder | Thu thập metrics runtime (code) | Dùng cho log/telemetry tùy chỉnh |

> **Pro tip:** Kết hợp với **Frame Debugger** khi cần hiểu pipeline render.

---

## 4. Quy trình profiling 5 bước

1. **Tái hiện vấn đề**: Xác định scenário gây tụt FPS/lag/crash.
2. **Gắn nhãn**: Chạy Dev Build với Profiler, đánh dấu thời điểm (Profiler Markers hoặc log).
3. **Thu dữ liệu**: Capture 200–300 frame, ghi chú các spike.
4. **Phân tích**: Drill down tới script/function, đối chiếu với asset (shader, animation).
5. **Lặp lại**: Fix một thay đổi, profile lại để xác nhận hiệu quả.

### Marker bằng `ProfilerMarker`

```csharp
private static readonly ProfilerMarker CombatMarker = new("Combat.Update");

void Update() {
    using (CombatMarker.Auto()) {
        ResolveSkills();
    }
}
```

* Giúp bạn tra cứu nhanh vùng code trong Profiler.

---

## 5. Deep Profiling & Custom Profiler

### 5.1 Deep Profiling
* Đo từng call C#, nhưng overhead lớn (gấp 3–10 lần).
* Dùng cho QA scene nhỏ hoặc để khám phá call chain khó tìm.

### 5.2 Custom Profiler Recorder

```csharp
ProfilerRecorder recorder = ProfilerRecorder.StartNew(
    ProfilerCategory.Memory,
    "GC.Alloc"
);

void OnGUI() {
    GUILayout.Label($"GC Alloc: {recorder.LastValue / 1024f:F1} KB/frame");
}
```

* Thu thập dữ liệu liên tục ngay trong Dev Build, đồng bộ với telemetry.

---

## 6. Dev Build Tooling Stack

| Công cụ | Mô tả |
| --- | --- |
| **Build Automation** | `Unity -batchmode -executeMethod BuildPipeline.BuildPlayer` -> tạo Dev build nightly |
| **Symbol Upload** | Tự động tải `pdb/dSYM` để đọc stack trace |
| **Device Farm** | Xử lý QA với nhiều cấu hình (Android, iOS, PC) |
| **Profiler Data Store** | Lưu file `.data` vào S3/GCS để QA/dev cùng xem |

> **Workflow gợi ý:** QA tái hiện bug → upload Profiler capture + video + log → Dev mở bằng Profiler để phân tích.

---

## 7. Checklist thực chiến

- [ ] Dev Build bật Autoconnect Profiler + logging đầy đủ.
- [ ] Có HUD dev hiển thị FPS, GC alloc, draw call.
- [ ] QA có quy trình ghi lại Profiler capture khi phát hiện bug.
- [ ] Script sử dụng `ProfilerMarker` cho các hệ thống trọng yếu.
- [ ] Có script batch mode tạo Dev Build + upload symbol/log.
- [ ] Định kỳ so sánh Profiler snapshot giữa các bản build để phát hiện regression.

Làm chủ Unity Profiler và Dev Build Mode giúp bạn nhìn xuyên qua mọi lớp của game, bắt lỗi trước khi chúng ra mắt. Hãy biến profiling thành thói quen mỗi sprint! 🚀
