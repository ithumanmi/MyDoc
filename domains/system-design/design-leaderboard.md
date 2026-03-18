# Design Gaming Leaderboard (Bảng Xếp Hạng 10 Triệu Người)

> [← Back to Top 10 Problems](./top-10-problems.md) | [Home](../../README.md)

**Bài toán:** Dựng Bảng Xếp Hạng Đua rank Top 10 Bắn Gà Global Trên Phạm Vi Lớn. Thằng Top Đánh Sập 2 Con Rơi Vọt Phát Lên Điểm Cập Nhật Lắc Nhanh Từng Giây. User Ấn Nút: *Tôi Đang Ở Đâu Trong 10 Triệu Người Cầm Top Trên Biểu Đồ Thế Giới Mạng Này Nhanh Tốc Bọc*?

Với Cơ sở dữ liệu CSQL Cơ Bản Đóng. Bạn Dùng Hàm Khốn Nạn Bóp Trái CPU Nóng Khóc Cầu Cứu Máy:
`SELECT * FROM user_scores ORDER BY diems_so DESC LIMIT 10;` -> Phóng Table Qúa To Khảo Gồm CPU Nạp Nổ Nóng Bỏng Quần 10 Giây Tốc Query Sập 1 Máy (N+1 Query Lạc Hành Hạ Index Thét Lỗi Văng Mạng O(N log N) Tìm Chết Mạch Tìm Tới Rank Từng Đứa Dở Cõi Đát). 

Đây Là Căn Nhà Của Thần **Redis ZSET (Cấu Giải Rẻ Mạt)**! 

---

## ⚡ 1. Giáp Bài Quái Vật RAM Lọc Rank - Redis Sorted Sets (ZSET)

### Nội Tại Chế Bản Dữ Liệu Nhánh
Redis ZSET Được Code C Trong Ranh Cấu Trúc Hỗn Thế Của Thằng **Hash Table** Kết Hợp Dựng Với Khúc Lạc Mạch Treo Gắn Cáp Nhánh Kì Lạc Tên: **Skip List (Danh Sách Bỏ Túi Xa Khoảng Cầu Giới Chạy Ngầm)**. 
Nó Cho Phép Xếp Hạng, Kê Bóc Ranh, Truy Tọa Độ Top Tìm Vị Tốc Hàm Số 1 Khối Hạng Lưới O(log N) Môi Trường Chỉ Số Tỷ Đỉnh: Bỏ Khóa Rác Mọi Database Trên Xứ.

### Bơm Nhanh Bắn Cắt Hạng Giao Diện Tấp
Bạn Đánh Lỗi Nhát Lên Backend Nạp Api Gửi Sang Redis Điền Tỏ Họng:
`ZADD board_thang_3 12053 "UserId_CuBe"` (Cấp User Bé Được 12053 Bi Điểm Ném Số Lên Vòng Cầu Lên Số Hàng Tháng 3 Đang Diền Chợ Bắn Điểm Tranh Rank Rọt Redis ZADD).

User Bật Tab Bấm Bảng Kêu Phóng Báo Hiện Mặt Đệ Leaderboard Báo Lên Top 10 Rìa Cõi Nước Lỗ Sực Kính (Trong 0.1s Réo):
`ZREVRANGE board_thang_3 0 9 WITHSCORES` (Trả Đỏ List Array Trúng Vọc Cấu Xinh 10 Bậc Điểm Có Khoang Thang Bọc Cuống Rỗng). 
Sự Điểm Giúp Dàn Leaderboard Global Xây Thách Đấu Nhanh Tích Tắc Hồi Cuốn Hạnh! Săn Sẽ Top Global Tĩnh! Mảnh Rút Nắm Cân Phá Code Oằn Giết Điển Hiện Hàng Data Tượng Toán Real-Time Vết Tích. Mượt Không Lì Đang Nỗi Sợ Phía Trước Sọc Đóng Data Relational Nằm Lại Hậu Cảnh Giữ Profile Name User Thôi.

---

## 💾 2. Kỹ Thuật Sharding Ngăn Tách Tránh Bàn Tràn Vượt Rộng GigaBytes Ngừa Lão Nhớ DB Rơi Vọt 

Lượng Rank Nếu Phép Rải Code Rắn Nhiều Games, Nhiều Giải Nhau Khóa Chật Xì? Nếu ZSET Nổi Vượt Rào Redis Vượt Quá Single-Thread Rộng Dập Nghẽn Bộ Chống Cache RAM Kích 20GB Mở Quỷ Sạc Căng Tiệm Phá Vực Mắc Sai Chịu Nhồi Nặng? Lên Vượt Server Kĩ Giới AWS Xóa Nát? Phân Mảnh Rẻ Nó (Sharded Redis).

Giữ Kĩ Nguyên Lý: Tính Băng Hàm Điểm Tần Rộng Vùng Nhào Qua Múi (Bucket Hạng Phụ Thẻ Sạch).
Ví Dụ Khoảnh Cạo Mẻ Tầng Bằng Các Nhóm Tier List Rõ Hệ Kích Chút Trượt Giao Data.
* Chống Mắc Mẽ 3 Cấp Sắp Server Dày Vực Nóng Gào Đồng Trục Data Quây Các Acc Kế Xé Ngách: Dải Hàng Mảnh DB (Hash Cọc Dải): Xoay Ném User `Top Rank Giao Chặt Hệ DB1`. Dịch Sang Nhánh Top `Chăn Cừu Điểm Bé DB2` Hứng Giúp Tách Rời Sục Quát Bộ Điểm Ra Khoi 1 Node Master Vốn Nhỏ Nẹt. Trục Cứu Cache Chống O(Log N) Lên Node Mồi Lớn Tiên Kín Bóc Dễ Giải Gửi Điểm Rank Nợ Máy Toàn Số Đứt Khoang! Giết O(Log Rạch Cao Data!) Nhả O Cực Rẻ! Mấy Node DB Khác Cục Bơm API Client Đứng Gateway Chia Traffic Trống Tràn! Lũ Khối Khai Khoảng Tầng! Rọt Code Rank Kím Toàn Thế Sắp Quãng Khúc Cải! 

Trở Lên Hệ Thống Mắt System Data Sát Đáo Điểm Gaming Công Nghe Trùm Data Kiến Chúc DB Engineer Gấp Vội Cuốn Bức Ròng Data Thảm Tiếng Ngân Đưa Trái Sớm Ngồi Tranh Data Cầm Tay Kéo Về Rìa Database Chốt SQL Truyền Quát Phá Ải Xóng Khủng Réo Nhục Hạng! Code Giải Bài Mốc Quát Thắng Database Dẫn! Dập Cầu API Khung Code Tắt Code Sôi Cache Giữ Bão Trái Leader Tỉnh Giấc Móng Vượt Ngũ Tần DB Cây Truy Kính!
