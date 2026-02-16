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

---

## 4. Code Optimization

*   **Tránh `GetComponent`, `Find` trong `Update`.** (Cache nó trong `Start`).
*   **Dùng `StringBuilder` thay vì `string + string`** (để tránh tạo rác string).
*   **Dùng `Struct` thay vì `Class`** cho dữ liệu nhỏ (để không tạo rác trên Heap).
