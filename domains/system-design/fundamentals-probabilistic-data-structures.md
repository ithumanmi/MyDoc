# Cấu Trúc Dữ Liệu Xác Suất (Probabilistic Data Structures)

> [← Back to System Design Index](./README.md)

Khi thiết kế hệ thống nhỏ (100,000 Users), bạn dùng HashMap, HashSet lưu vào RAM `Check_User_Hop_Le("Hiep") == True`. 

Nhưng nếu Google có 3 Tỷ Đường Dẫn Web Độc Hại (Malicious URLs)? Nếu dùng `HashSet` để lưu 3 Tỷ chuỗi String này, Chrome của bạn sẽ nổ RAM cần hơn **400GB Chỉ Để Chạy Trực Kiểm Tra**.

Giải pháp cho Cảnh Báo Big Data Ngập Tràn? **Chấp Nhận Cho Máy Trả Lời Sai Ở Mức Rủi Ro Khống Chế Được (% Error Rate).** Chào Cõi Không Gian (Probabilistic Data Structures).

---

## 🕷️ 1. Bloom Filter (Trình Lọc Rây Hạt Không Thể Thiếu)

Đừng Mơ Giữ Dữ Liệu String Gốc! Gắn Dấu Bằng Những Bit Cờ Đen Trắng 0 - 1.

### Cơ Chế Kỳ Bí Mạng Hash
Bạn Tạo Một Dải Array Array Chỉ Có 100 Câu Ô Chứa Nhị Phân (Từ 0 -> Đập Mặt Số 100 Toàn Trắng Bóc Sẵn `00000..0`).
Khi Cho Chuỗi Mật Mã `Zombies.com` Đi Vào Đưa 3 Cửa Hash Functions Xay Vụn Ra 3 Con Số: `14, 55, 99` -> Đánh Dấu Tick 3 Ô Đó Lên Đen (Biến Thành `1`).
Cho `PhimHay.com` Xay 3 Hàm Nó Ra `11, 23, 55` -> Đánh Dấu Đen (Thêm 2 Ô 11,23 Còn Ô 55 Dính Máy Bị Kia Phủ Đen Sắp Ghi Đè Kệ Hắn).

### Khi Nào Có Thằng Người Dùng Google Hỏi Mày: URL Này Có Phải Web Độc Không?
Hắn Kêu Xin Vào `HocGioi.com`. Đưa Xay Hash Ra Trùng Hàm `24, 60, 80`. 
Tra Trong Mảng Dải 100 Ô Coi: Thấy Ô 24 (Xóa Đứng Trắng Số 0).
=> **Tuyệt Đỉnh Chính Xác (100% Không Lừa Xạo): Mày Không Ở Kênh Độc! Vừa Gõ Mở Cửa.** Xin Đi Thoải Mái.

Hắn Xin Gõ Vào Kênh `TruyenDoi.com`. Máy Xay 3 Cái Hash Văng Hạt Nổ Văng Trúng Số `11, 14, 99`. Chết Rồi! Tra Bản Mảng Thấy Cả 3 Ô Này Đều Có Nhãn `1` Do Băng Đảng *PhimHay* Và *Zombies* Nó Vẽ Mực Trùng Quét Vét Trước Sáng Bóng!!
=> **Bloom Filter Lên Mõm Lỗi Xác Suất (False Positive): Hắn Bảo Vớ Vẩn Có Thể Đây Là Web Độc Mạng.** Dừng Trình Duyệt Bật Cảnh Cáo Đỏ! Mặc cho Thằng Trang Này Thật Ra Lành Đứt!

> 💎 **Hệ Trọng Báu Vật:** Tiêu Tốn Lượng RAM Chỉ Bằng $\frac{1}{10,000}$ RAM Lọc Mất HashMap. Chặn Được 100% Kẻ Xấu Không Thể Lọt Khỏi Khe Filter! Mà Đôi Khi Vấp Chặn Lỗi Vài Tên Méo Sạch Sẽ Tốt. (Cực Kỳ Đáng Đổi Trong Hệ Thống Redis Check Caching Lấp Thung Dòng Request Nạp).

---

## 📈 2. HyperLogLog (Ráp Đếm Lượng Rừng User YouTube Khủng Khiếp Unique)

Video Gangnam Style Lên 3 Tỷ Views Có Hơn Tới 600 Triệu Người Duy Nhất Xem Cùng (Unique Viewers - Đếm Loại Người Trùng). 
Nếu Cất IP/ID 600 Triệu Cái Tên Để Check Trọng Kẻ Coi Trùng: Lút Kín Redis Nạn Server Báo Dung Lượng GBs Giật Thát.

### Đếm Đoán Xả Rác:
Hắn Đếm Cảnh Số Chuỗi 0 Trồi Mặt Liền Sau Nét Hash Trả Vực Chuỗi Nhi Phân! (Sự Giả Lập Móc Đồng Xu Lặp Số Đỉnh Tung Mặt Sấp Ngửa).
Nếu Từng Gặp Hash Mới Có Ròng Cạnh Đếm `00001....` Hắn Mở Máy Ghi Nhận Số Maximum Số Dãy Hạt 0 Liên Tục Bị Trùng Đã Răng Tìm Lọc Bao Giờ! 
Qua Đó Toán Thống Kê Toán Đoán Chuyển Suy Ra Lãi Đám Rợp Đông Gần Khoảng Nhích (12KB RAM Cho Cả 1 Triệu Tên Định Danh)! 

> **Chốt Hồi Phỏng Vấn Big-TECH Lệ: Vung Ra HLL Rẻ Đột Xuyên Thống Lĩnh Mảng System Design Chắc Nịch Răng System Engineer Cứng Điển Đưa Tái View Tối Ưu Tốc Không Giật Đụng Nhắn Hệ Phá Data Rực Lửa.**

---

## 📊 3. Count-Min Sketch (Đếm Sóng Tweet Trend Twitter Hot Nhất)

Vẽ Array Khung Bảng Lớn Matrix Hàng Ngang Xoay Hash Hàm Cọc Chữ Chứa Tần Suất Xất Khối Count Cục Quẹt Hash. Dùng So Bước Từ Mảng Tìm Kiếm Trending 10 Hash Tags Đỉnh Cấu Trên Kênh Mà Không Gây Nặng Trầm Mệnh Dài Nhớ Rễ Hàng Tỷ Hạt Tần Chữ Trống Không. Tốc Kỵ Tính Cầm Heavy-Hitter!
