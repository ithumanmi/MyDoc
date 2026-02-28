# ⚡ Unity Performance Optimization: Tối ưu hiệu năng

> [← Back to Game Development Roadmap](../README.md)

Game chạy 60 FPS trên máy tính của bạn, nhưng chỉ 15 FPS trên điện thoại của user?
Đó là lúc bạn cần tối ưu.

---

## 1. Profiling (Đo lường)

Đừng đoán mò. Hãy đo.

*   **Unity Profiler:** Công cụ chính chủ. Xem biểu đồ sử dụng CPU, GPU, Memory.
*   **Deep Profile:** Bật chế độ này để xem chi tiết từng hàm C# nào đang ngốn thời gian.
*   **Frame Debugger:** Xem từng bước vẽ hình của GPU. Giúp phát hiện Draw Call thừa.

---

## 2. Memory Management (Quản lý bộ nhớ)

### **A. Garbage Collection (GC)**
*   C# tự động dọn rác bộ nhớ. Nhưng khi nó dọn (GC Spike), game sẽ bị khựng (Lag).
*   **Tránh:** Tạo object mới trong `Update()` (ví dụ: `new Vector3()`, `new List<>`).
*   **Giải pháp:** Cache lại object, dùng Object Pooling.

### **B. Memory Leaks (Rò rỉ)**
*   Object không dùng nữa nhưng vẫn bị tham chiếu -> Không được giải phóng.
*   Thường gặp khi đăng ký Event (`event += func`) mà quên hủy đăng ký (`event -= func`) khi object bị Destroy.

### **C. Asset Bundles / Addressables**
*   Tải asset theo nhu cầu, giải phóng bằng `Addressables.Release`/`Resources.UnloadUnusedAssets()` sau khi rời scene.
*   Với mobile, giữ tổng bộ nhớ < 1.2GB để tránh hệ điều hành kill app.
*   Sử dụng `Compression Format = LZ4` cho asset bundle để load nhanh hơn (đổi lại dung lượng lớn hơn một chút).

---

## 3. Graphics Optimization (Tối ưu đồ họa)

### **A. Draw Calls (Batches)**
*   Mỗi vật thể vẽ lên màn hình tốn 1 Draw Call. Quá nhiều -> CPU quá tải.
*   **Batching:** Gộp nhiều vật thể chung Material thành 1 lần vẽ. (Static Batching, GPU Instancing).
*   **Texture Atlasing:** Gộp nhiều ảnh nhỏ thành 1 ảnh lớn để dùng chung Material.

### **B. Texture Compression**
*   Ảnh 4K PNG nặng 20MB. Khi vào RAM có thể lên tới 100MB.
*   Luôn nén Texture (ASTC cho Mobile, DXT cho PC) để giảm dung lượng RAM và băng thông GPU.

### **C. LOD (Level of Detail)**
*   Vật ở xa -> Dùng model ít lưới (Low poly).
*   Vật ở gần -> Dùng model chi tiết (High poly).

### **D. Occlusion Culling**
*   Bật `Window > Rendering > Occlusion Culling` để Unity không render đối tượng bị che khuất.
*   Hữu ích cho cảnh trong nhà với nhiều phòng.

### **E. Light Baking & Mixed Lighting**
*   Baked lighting giảm số lượng light realtime.
*   Dùng **Mixed Light** cho các nguồn chính: ánh sáng direct baked + dynamic shadow gần camera.
*   Tránh dùng realtime shadow cho tất cả light—đặc biệt trên mobile.

---

## 4. Code Optimization

*   **Tránh `GetComponent`, `Find` trong `Update`.** (Cache nó trong `Start`).
*   **Dùng `StringBuilder` thay vì `string + string`** (để tránh tạo rác string).
*   **Dùng `Struct` thay vì `Class`** cho dữ liệu nhỏ (để không tạo rác trên Heap).

---

## 5. CPU vs GPU Bottleneck Checklist
| Dấu hiệu | Khả năng | Cách xử lý |
| --- | --- | --- |
| Profiler cho thấy `CPU.MainThread` spike | CPU bottleneck | Giảm logic C#, batch draw call, tối ưu physics/AI |
| Profiler GPU spike, Frame Debugger nhiều pass | GPU bottleneck | Giảm post-processing, LOD, giảm shadow, render scale |
| Memory sử dụng tăng liên tục | Memory leak hoặc load asset không giải phóng | Theo dõi `Profiler > Memory`, dùng Addressables/UnloadUnusedAssets |

---

## 6. Job System & Burst Compiler
- **C# Job System:** Chia nhỏ công việc chạy đa luồng (ví dụ xử lý AI, raycast batch).
- **Burst Compiler:** Biến job thành mã vector hóa cực nhanh. Thích hợp cho hệ thống cần tính toán nặng (boid, navigation).
- **Physics.RaycastCommand.ScheduleBatch:** Ví dụ điển hình: raycast hàng trăm tia async.

```csharp
NativeArray<RaycastHit> hits = new NativeArray<RaycastHit>(count, Allocator.TempJob);
NativeArray<RaycastCommand> cmds = new NativeArray<RaycastCommand>(count, Allocator.TempJob);

// Fill cmds...

JobHandle handle = RaycastCommand.ScheduleBatch(cmds, hits, 32);
handle.Complete();
```

---

## 7. Physics Optimization Recap
- Dùng `Physics.BakeMesh` cho mesh collider tĩnh.
- Giảm `Solver Iteration Count` nếu không cần độ chính xác cao.
- Tắt `Auto Sync Transforms` trừ khi cần đồng bộ transform thủ công.
- Gộp collider/rigidbody không cần thiết, tránh n+1 `OnCollisionEnter`.

---

## 8. Build Target Specific Tweaks
- **Mobile:** Hạn chế shader branch, tránh texture > 2K, bật ASTC compression, bật Multithreaded Rendering nếu GPU hỗ trợ.
- **PC:** Cho phép bật DLSS/FSR (HDRP). Tùy chọn Quality Settings (Low/Medium/High) với số shadow cascade, post-processing khác nhau.
- **VR:** Render scale 0.8-1.0, tắt tất cả post-processing nặng, dùng single-pass instanced rendering.

---

## 9. Tooling & Automation
- **Profile build thực tế:** Editor mode khác với build. Luôn build APK/EXE và profile trên thiết bị thật.
- **Performance Budget Sheet:** Đặt mục tiêu FPS và phân bổ ngân sách (ví dụ: CPU 6ms logic, GPU 8ms render, 2ms reserve).
- **CI:** Tự động chạy build với `-executeMethod` để đo kích thước asset, phát hiện tăng đột biến.
