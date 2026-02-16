# 🎮 Unity Advanced: Tối ưu hiệu năng cực đại (Level 6)

> [← Back to Game Development Roadmap](../README.md)

Làm game nhỏ thì dễ. Nhưng khi bạn muốn tạo ra một chiến trường với 10.000 quân lính đánh nhau (RTS), cách code thông thường (OOP) sẽ làm máy tính "bốc khói".
Bạn cần **DOTS**.

---

## 1. DOTS (Data-Oriented Technology Stack)

Tư duy lập trình hướng dữ liệu, thay vì hướng đối tượng (Object-Oriented Programming - OOP).
Tối ưu hóa việc sử dụng CPU Cache và Đa luồng.

### **A. ECS (Entity Component System)**
*   **Entity:** Chỉ là một cái ID (Ví dụ: ID=100). Không chứa dữ liệu, không chứa logic.
*   **Component:** Chỉ chứa dữ liệu (Data). Ví dụ: `Position {x, y, z}`, `Health {hp}`.
*   **System:** Chỉ chứa logic. Ví dụ: `MovementSystem` sẽ tìm tất cả Entity có `Position` và cập nhật tọa độ.
*   **Lợi ích:** Dữ liệu được xếp liền nhau trong bộ nhớ (Contiguous Memory) -> CPU đọc cực nhanh.

### **B. Job System**
*   Chia nhỏ công việc thành các "Job" nhỏ để chạy song song trên nhiều lõi CPU (Multi-threading).
*   Tránh xung đột dữ liệu (Race Condition) một cách an toàn.

### **C. Burst Compiler**
*   Biên dịch code C# thành mã máy (Assembly) siêu tối ưu (SIMD instructions).
*   Làm code chạy nhanh hơn 10-100 lần so với C# thông thường.

---

## 2. Addressables (Quản lý tài nguyên)

Game của bạn nặng 10GB? Đừng bắt người dùng tải hết một lần.

*   **Load on Demand:** Chỉ tải màn chơi 1 khi người dùng chơi màn 1.
*   **Content Update:** Cập nhật nội dung game (Skin mới, Sự kiện mới) qua Cloud mà không cần update App trên Store.
*   **Memory Management:** Tự động giải phóng RAM khi không dùng đến asset nữa (Reference Counting).

---

## 3. Profiling & Optimization (Đo lường & Tối ưu)

"Premature optimization is the root of all evil". Hãy đo trước khi sửa.

*   **Unity Profiler:** Xem game đang ngốn CPU vào việc gì (Rendering, Scripts, Physics?).
*   **Frame Debugger:** Xem từng bước vẽ hình của GPU. Tại sao Draw Call lại cao?
*   **Memory Profiler:** Tìm rò rỉ bộ nhớ (Memory Leak).
