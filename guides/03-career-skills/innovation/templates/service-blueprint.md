# 🗺️ Service Blueprint Template

> [← Back to Service Design Guide](../service-design.md)

## Dịch vụ: [Tên Dịch Vụ, VD: Quy trình Đặt phòng Khách sạn]
**Persona:** [Tên khách hàng mục tiêu]

---

| Tầng (Layer) | Giai đoạn 1: Trước khi đến (Before) | Giai đoạn 2: Trong khi dùng (During) | Giai đoạn 3: Sau khi dùng (After) |
| :--- | :--- | :--- | :--- |
| **Physical Evidence**<br>*(Bằng chứng hữu hình)* | Website, Email xác nhận | Sảnh lễ tân, Chìa khóa phòng | Hóa đơn, Email cảm ơn |
| **Customer Actions**<br>*(Khách hàng làm gì?)* | Tìm kiếm khách sạn -> Đặt phòng | Đến khách sạn -> Check-in -> Nhận phòng | Check-out -> Trả tiền -> Rời đi |
| **--- LINE OF INTERACTION ---** | *(Ranh giới tương tác)* | | |
| **Frontstage Actions**<br>*(Nhân viên tiếp xúc trực tiếp)* | (Chatbot trả lời tự động) | Lễ tân chào đón -> Kiểm tra ID -> Giao chìa khóa | Lễ tân in hóa đơn -> Tạm biệt |
| **--- LINE OF VISIBILITY ---** | *(Ranh giới tầm nhìn)* | | |
| **Backstage Actions**<br>*(Nhân viên hậu cần)* | Nhân viên sale kiểm tra phòng trống | Bellman mang hành lý lên phòng | Buồng phòng dọn dẹp phòng |
| **--- LINE OF INTERNAL ACTION ---** | *(Ranh giới nội bộ)* | | |
| **Support Processes**<br>*(Hệ thống hỗ trợ)* | Hệ thống Booking Engine (PMS) | Hệ thống khóa từ | Hệ thống kế toán, CRM gửi email |

---

## Phân Tích (Analysis) 🔍
*   **Fail Points (Điểm dễ lỗi):** [Ví dụ: Hệ thống PMS bị treo lúc check-in] -> *Giải pháp:* [Quy trình check-in thủ công dự phòng].
*   **Wait Points (Điểm chờ đợi):** [Ví dụ: Chờ dọn phòng] -> *Giải pháp:* [Mời nước uống miễn phí tại sảnh].
