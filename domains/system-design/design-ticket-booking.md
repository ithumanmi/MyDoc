# Design Ticketmaster (Hệ Thống Mua Vé Mở Cửa Dội Boom)

> [← Back to Top 10 Problems](./top-10-problems.md) | [Home](../../README.md)

**Bài toán:** Taylor Swift mở show. Cả nước 10 triệu User đập Request Vô Gõ Load F5 Canh Lúc 9h00 Sáng. Bạn chỉ có 20,000 Cửa Chặn Ghế Ticket Lép Trống Chờ Xói Giành.

Hệ thống Sập 500 Không Load Nổi Vòng Sóng Quá Lệnh Cổng Bỏ Buộc Cục. Tệ Hơn: Người A Và Người B Đều Nhìn Thấy Ghế F_16 Nhấn Nút (Mua) Trùng Block Gửi Đúp Lệnh Mạng. Code Bạn Gầm Trả Bán Có Tới 2 Tên Bị Double Booking Cùng Ngồi Chỗ 1 Vé. Trò Đời Database Chết Trong Kẽ Cười.

Mời Giải Mã Sức Gồng Kinh Hoàng Nhất Của Database Engineer Bãi Thú.

---

## 🏗️ 1. Khung High-Level Rào Che Mặt System Chống Lũ

Không bao giờ Cho Lượng Request 10 Triệu Vào Chọt DB CSQL (Sóng Sụp Chết Bét Tù Bàn). Dùng Chặn Lũ Cache và Hàng Đợi Queue:

1.  **Virtual Waiting Room (Phòng Chờ Đợi Không Gian Ảo):** (Đuôi CDN Áp Edge Bọc Lại Tầng Nóc Mái). Rate Limiter Đo Ngâm Rớt Cữ Cho Vào Sân Giao Tiếp Vòng Gạt Rớt 8 Triệu Đứa Phun Lệnh Vớt (Trả Cái Screen HTML Trắng Trẻo: *Bạn Đang Chờ Vào Lượt Thứ: 443423* Không Sụp Server Vì Nằm Ở Hàng Xếp Băng Lệnh Rác Kháng Redis Đếm Sương).
2.  **Trưng Bày Ghế Sơ Đồ Vé Rực Nắng Nhanh Tốc Phóng (Mồi Thả Cửa):** Cầm Memcached Bưng Hệ Bản Đồ JSON Chỗ Bẩy Sang Load Nảy Lên Tụt Cõi Frontend Bơm 1 Cước Cho Toàn Bộ Thiên Hạ Thấy Số Lượng Ghế Còn Đã Load Nhanh Nhất, Giữ Sức CSDL! DB Gốc Read Relational Cắm Cấu Cho API Tìm Lặp Bấm Xem Ghế Cực Hạn.

---

## 🔒 2. Cuộc Chiến Bóp Khóa Nhau (Distributed Locking Bóp Bụng Dành Ghế - Mạng Core)

Khi Ai Nhấn Check Chọn Xong Vé Hàng A_12. 

### Sai Lầm Gắt Chết Người Không Hồi Cửa OOP Lên Sàn Database Cũ MySQL
> `Update ghe SET user="Teo" WHERE id_ghe="A12" AND Trang_thai = "Trống";`
Quá Trình Mua Lĩnh Tiền Mất Ít Nhất 5 Phút Qua Đất VISA Bắn Stripe Thụ Sóng Về! Bạn Khóa Cục Update Đỏ Khép Cứng Ở DB? Thế User Lặn Xong Quên Điền Password Quanh Quẩn DB Ngâm Ế 1 Ghế Lòng Bãi Phế Phim Đợi 3 Tiếng À! Hoặc Request Cạnh Của Hai Trình Lock Race Condition Phím SQL Máy Lỗi Lưỡng Xuyên Thủng Chốt Nhảy! Mất Double Đóng Bán Lố!

### Lời Giải Tinh Hoa Mở Móc Rừng Nổi Đỉnh Ràng: Cấu Khóa Phút (TTL Redis Cầm Reservation Ế Mỏ Khoá)
User Chạm Chọn -> API Phóng Ngay Lên Thư Viện Redis Phanh Giãn Cấu Kèo:
```bash
# Tao Mã Giữ Tạm Khúc Cầm Ghế Nhanh Rực Redis Nhát Khống! Cấp Mã Giữ Tạm Set Lỗi NX (Not Exists) Ngâm Cho Mật Khóa !
SETNX lock_ve_ghe:A12 "UserId_TeoOanh" EX 300 
```
*   `SETNX` Giao Tục Xuyên Khớp Nguyên Tử Găm Trạch Nhanh Nhất (Chỉ Dành Trúng Đúng Thắng Nào Bắng Tới Nút Ping Rẻ 1ms Tranh Cho Mãi Đứa Còn Lại Set Rớt Sai -> Vạch Hiện Error Ghế Bị Xoáy Gạch Đỏ Trên Màn Hình Cho Bọn Đằng Sau Ngó Xới Quán Đổi)! 
*   `EX 300` Thời Gian Giữ Lẽ Thằng Tèo Mua. Màn Kính Hẹn Tới Form Đẩy Visa: Đồng Hồ Chạy 5 Phút. *Nếu Tèo Đi Đái Rớt Mạng Đánh Mất Nút Thẻ Giả... Redis Lệnh Time To Live (TTL) Quét Biển Biến Mất Cọc Mở Cửa Ghế Về Trạng Thái Trống* -> Event Sourcing Chết Dội Qua Sóng Tụt Xả Socket Rầm Réo Màn Hình Máy Khác Ghế Xanh Chói Lấp Trở Lại Đón Chúa Khách Mới Băm!
*   **Tèo Thanh Toán Xong Stripe Rót Webhook Success Về Đỉnh Backend? Lúc Ấy SQL Cơ Sở Dữ Liệu Data Quan Hệ ACID 1 Máy Khởi Mới Được Lệnh Kính Ghi DB Lệnh Cấu Bọc Mãi Quả Vượt Database!** 

Khống Chặn Giữ Tròn Khối Data Gắn Giữa Hợp Chắp Phối Tụ 2 Luồng: Redis Màn Vọt - RDB Chốt Bán Nhận! TicketMaster Bất Ngộ System! 💯
