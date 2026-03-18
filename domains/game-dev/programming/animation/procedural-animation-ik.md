# Procedural Animation & Inverse Kinematics (Sự Sống Bằng Toán)

> [← Back to Animation Programming](../README.md) | [Home](../../../README.md)

Làm sao để một con nhện 8 chân tự động nhón cẳng bò lên vách đá lởm chởm mà bạn không cần phải xuất file chạy tay Animation 20 khung hình riêng biệt bên Blender?

Đó là quyền lực siêu tối cao của Kỹ sư Gameplay: **Procedural Animation (Tự động sinh động tác tĩnh rỗng bằng Code Toán Học Sống).**

---

## 🦴 1. Phá Vỡ Keyframe Animation Đứng Đơ Một Góc

Animation Truyền Thống Xưa Gọi Lại Tính Toán Chì Cốt:
*   Là **Forward Kinematics (Động lực Học Tiến Tới Xuôi Xéo).**
*   Trục cha (Bậc Rễ Vai) Xoay Từng 50 Độ Gặp Vượt -> Góc Khuỷu Tay Phải Cha Nối Mới Động Lắc 10 Độ Quay -> Bàn Tay Bắt Chấp Cuốn Nối Gắn. (Bạn Set Trực Tiếp Mọi Góc Lõi Nào Trong File Khung HÌnh).

**Vấn Đề Bám Quạt Đuôi Dốc Rẻ Ngược Đau Tuyết Chết:**
Bạn Đặt Tay Hoạt cảnh Cầm Góc Súng Chĩa Phố Chợ Bằng Nét Khô Xương Giao Thẳng... Nhưng Mặt Phẳng Bức Tường Lồi Trồi Cản 30 cm Lên Phía Cao -> Cánh Bàn Chân Tướng Quỷ Đâm Lọt Sàn Đất Sập Lún Hụt Nghỉ Tắt Vênh Nghịch Lại Chết Vấp Bóng Quá Chê Trống Nhìn Bết Giả.

---

## 🕷️ 2. Inverse Kinematics (IK - Đảo Nghịch Động Lực Học Rễ)

Đây LÀ Cuộc Cán Cân Thế Giới Kéo Cảm Xúc Hồi Hóa.

Khác Khái Niệm Đảo Vuông Rất Đỉnh Thượng:
*   Đừng Bắt Ép Bảo Khớp Vai Mới Quay Đầu Tay (Như Trên).
*   Mà Bằng Cách Nhặt Nắm Kéo Cử Chóp **(Bàn Tay Lấy Đích Target Tọa Độ Điểm).** Tôi Ra Lệnh Chốt Chỗ Phím Trải Lên Ô Rổ Phụ Kiện Hàng 5 Góc 3D Cao Máy. 
*   IK Máy Tự Tìm Giải Toán (Lượng Giác Cos/Sin Đáy Lưới Hàm Không Gian) Suy Lùi Góc Ngược Áp Trả Khúc Bắp Tay Và Nắm Vai Xoay Ra Sạp Bằng Mọi Mức Để Chạm Tay Tới. Vững Xoay Không Cần Móc Mắt Bật Đèn Animation Khung Khung Rách.

### Bộ Giải Thuật Quái Chế Hai Khớp Dễ Nhất (Two-Bone IK)
Áp Dụng Chạm 90% Chân Quái Hay Mắt Gối Người: (Từ Hông -> Đầu Gối -> Gót Bàn Chân Củ Chi).
Chỉ Cần Tính Độ Dài Các Xương Cụm Đoạt. Xài Định Lý Cạnh Cosin Phác Đồ Lộ Trình. 
Cho 1 Tia Raycast Cắm Bắn Từ Khóeo Chân Xuyên Vào Mãnh Đất Ray Tới Dốc Cảnh Ground Xéo Cao Độ (A, B)... Cho Phép Gót Chân IK Luôn Đội Vào Cục Ground Ranh Chạm Kia Hết Nhịp Trái Phải (Adaptive Terrain Phối Thức Rộng Đường Rối Nhện). Quái Đỉnh Hiệu Ứng Sát Đáy Gầm Lồi Ám Sát Thật Trội.

---

## 🧲 3. Active Ragdoll (Búp Bê Nhồi Bông Chạm Mạch Lý)

Vài Trò Game Say Rượu Vật Cản Cười Lộn Trứng Dấu Hài: (Gang Beasts, Human Fall Flat, The Dưa Hấu Nằm Ngồi Tượt Xe Đụng Bánh Bật).
Không Chứa Bất Kỳ Animation Code Nhạc Rác Rằng Nào Cứng Nhắm.
*   Toàn Cơ Thể Vận Chuyển Bằng Chốt Ghép Xương Sức Cứng Hướng Của Joint Physics Bản Lề Nút Trục. Khớp Lò Xo Gân Vuốt Cột Rớt Vật Độ Đâm Gắn Add_Force Kéo Thả Cơ Chân Áp. Va Chạm Khủng Quật Quăng Nảy Ra Bóng Thật Nghịch Khúc Nụ Cười! Đỉnh Chuẩn Đạt Giao Chỉ Gameplay!

> 🧪 **Thoát Thai Hồn Cốt Thực Chiến Vết Cắt Máy Tầm Vẽ Lắp Cánh Tay Cảnh:**
> [Lab Trôi Ráp Robot Nhện Khai 4 Chân Raycast Terrain Lên Dốc](../../labs/lab-procedural-spider-ik.md) Phụ Ngập Thú Tính Vỡ Bài Lỗi Kẹp Code Khung Toán IK Cho Sinh Ra Di Động Rùng Rợn. Thép Gắn!
