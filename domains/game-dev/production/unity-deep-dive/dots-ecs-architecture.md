# Unity DOTS & ECS: Kiến Trúc Hiệu Năng Tối Thượng

> [← Back to Unity Deep Dive](../README.md) | [Home](../../../README.md)

Khi bạn muốn hiển thị 20 con thây ma, GameObject/MonoBehaviour là vua. Dễ xài, kéo thả Inspector trực quan.
Khi bạn muốn hiển thị **20,000 con thây ma, 10,000 hạt bụi va chạm Vật Lý, và 500 chiếc thuyền nã Pháo**... CPU của bản sẽ nổ tung cháy đen ở 3 FPS.

Chào mừng Mở Rương Kiến Trúc Hiệu Năng Vô Địch Thế Hệ Cuối Của Unity: **Data-Oriented Technology Stack (DOTS)**.

---

## 🪓 1. ECS (Entity Component System) Khác OOP Chỗ Nào?

Lập trình hướng đối tượng (OOP - Object Oriented Programming) được thiết kế cho Sự Thuận Tiện của Con Người đọc, chứ KHÔNG TỐT cho RAM Máy tính xử lý.

### Tại Sao Lập Trình Game Truyền Thống Xài `Update()` Bị Lủng Bụng?
**OOP Cổ Điển:** Có 5000 con Quái (`GameObject`). Mỗi con dán 1 script `EnemyThongMinh.cs` Chứa Biến (Máu, Giáp, Tính Cách) Trộn Lẫn Với Hàm (Hàm Nhạy Cảm, Hàm Mất Máu, Gọi Transform Hằng Vòng).
Mọi thứ nhét chung 1 Rổ. Khi cái Máy Tính Mở Ram Đọc Cục Dữ Liệu Gọi Render. Nó phải đào qua Hàng Ngàn Class Lộn Xộn Rác Nhện Ngổn Ngang Ở Mọi Nơi Trong Ổ RAM (Cache Misses Khét lẹt). Máy Đơ.

### Data-Oriented (Mệnh Lệnh Tổ Chức Array Thẳng Đuộc Theo Nết ECS)
Xẻ dọc cục GameObject ra Thành 3 Ranh Giới Sắt Đá Quyết Liệt:
1.  **Entity (Cái Định Danh):** Chỉ là một con số Integer Căn Cước Công Dân (ID: 15). Hoàn toàn Trống Rỗng! Chả làm cái mẹ gì.
2.  **Component (The Data - Kho Thịt):** Mảnh Dữ liệu Siêu Nhỏ. VD Cục Thịt Data `Health { value = 100 }`. Đắp Lên Thực Thể Entity 15 Ở trên.
3.  **System (Các Nhà Máy Nhồi Cơ Học):** Code Lập Trình Thao Tác Chạy Song Song Đóng Lại Tại Đây.

**Cách Nó Chạy Khác Tràn Trề:**
Bọn `MoveSystem` Chạy Hàng Vòng: Nó Không Đi TÌm Mọi Con Đối Tượng Để Kêu Mày Di Chuyển Đi. Nó Kêu Rằng: *"Tao Cần Tất Cả Dải Array Danh Sách Dữ Liệu `PositionComponent` và `VelocityComponent` Tụ Lại 1 Cho Tao".*
Vì Tất Cả Thịt Data Trực Diện Tọa Độ Nằm CHUNG 1 LIỀN MẠCH RAM Bộ Nhớ Gần Nhau Lít Nhít Tít Gọn. CPU Gắp Vào Tính Toán NHANH Gấp 1500% Lần (Cache Alignment Hoàn Mỹ!).

---

## ⚡ 2. Job System & Burst Compiler (Siêu Sayyan)

ECS Tổ chức được Dữ liệu Gọn gàng Cạnh Nhau. Nhờ vậy Nó Mở Khóa Đai Phong Ấn Của 2 Bùa Mệnh Tuyệt Đỉnh Phía Dưới Chèn Sông:

1.  **C# Job System (Đa Luồng Hoàn Hải Tuyệt Đối):** Viết Code Để Game Chĩa Sức Gánh Tính Toán Của Enemy Rành Rọt Cho Lõi Cores khác (Multithreading/Worker Threads). Main Thread Nhẹ Tênh Render Tối. Code Lỗi Race Condition Đụng chạm Rào Gân Giới Tự Động Chặn.
2.  **Burst Compiler:** (Dịch Sâu Xuống Mã Máy Đỉnh Cấp Cuối). Bạn Viết C# Kéo Code Kèm Rào Ánh Sáng Mác `[BurstCompile]`. Unity Phù Phép Biến Đoạn Toán Đó Không Chạy Bằng C# Chập Chững Mà Trổ Rễ Thẳng Ra Hợp Ngữ Máy Cấp Thấp Nhất SSE/AVX CPU Xử Lý Như C - C++ Lõ Lại Vượt!

### Khi Nào Thì Sờ Tới DOTS ECS?
*   Đừng bao giờ động vào nó để làm Menu Lịch Sử, Hành Lang Phế Liệu. Game Bạn là Flappy Bird? Nhả ECS ra. Dev Cực, Nặng Khóc, Khó Hiểu Khỉ Cò.
*   **Use Case Siêu Hợp:** Xây Trạm Tycoon, Game Sàn Trận Age of Empire Lịch Sử 10 Triệu Con Giun Vận Lộn. Vật Lý Simulation Va Đập Đất Nặng nề. 

> 🧪 **Thực Tế:** [Lab DOTS Zombie Xông Lên Màn Hình 10k Con Chó Săn](../../labs/lab-dots-zombie-swarm.md) Cắn Xé Từng Tọa Độ Khung Hiện Vật Lý Cổ Xưa Khóc Thét 144FPS!
