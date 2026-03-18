# Đại Cục Tàng Trữ: Data Warehouse vs Data Lake vs Lakehouse

> [← Back to Data Science Roadmap](../README.md)

Các Công Ty Startup Lập Web Chạy Postgresql. Bảng `Users` Ghi Nhận Lệnh Đặt Hàng Trực Tiếp Rực Tuyến Gọi Cú Query 1ms. Đây Được Gọi Là **OLTP** (Online Transaction Processing - Nghiệp Vụ Chạy Tiền Ghi Data Liên Tục Trống Nút).
Nhưng Kế Toán Hoặc CEO Cần Xem: "Năm Ngoái Quý 1 So Quý 3 Dòng Người Click Nút Mua Trống Của Lưới Mạng Miền Tây Biến Tiêu Ra Sao?". 
Câu Lệnh Này SELECT Ngấm Bảng Khổng Lồ Sẽ Khóa DB Làm Máy Sập Giao Dịch Chết Gãy! Lúc Ấy Sẽ Bỏ Sinh Hình Kiến Trúc Lọc Số Báo Cáo Chuyên Biệt Gọi Là **OLAP** (Online Analytical Processing). 

Câu Chuyện Đỉnh Cao Để Xây Olap Này Tiến Hóa Gồm 3 Hình Thái Báu Thế Giới:

---

## 🏛️ 1. Kho Sắp Gạch Sạch Mệnh: Data Warehouse (DWH)
Data Warehouse Là 1 Căn Biệt Thự Trưng Khung Tranh. 
- Mọi Data Đổ Về Đây (Từ Sales, Bán Hàng Máy Két) Đều Bị Bóp Nghiền Quặn Filter Bưng Qua Hình Phễu Gọn Rõ Schema Rất Nghiêm Cấm: Chạy Phải Số Thực/ Text Mấy Chữ Dày Sạch (Cleaned Data). 
- Kiến Trúc Pipeline Cổ Mệnh Đi Kèm: **ETL (Extract - Bóc -> Transform - Nhồi Bóp -> Load - Bỏ Xuống Kho Cứng)**.
- **Ưu:** Câu Query Báo Cáo Dashboard Chạy Tức Khắc Siêu Khủng Chớp Mắt Vì Đang Mượt Bảng Data! (Công nghệ: Snowflake, Amazon Redshift, Google BigQuery Lõi SQL Máy Móc Chuẩn Trị Đục).
- **Khuyết Bóp Tàn:** Data ẢNH/AUDIO/JSON Đổ Tới Nó Không Hút Nổi Trôi Lọt Vì Nó Căng Cần Schema Table Rắn 100%! Rất Thiếu Khung Thu Nạp Cho ML Máy Học! 

---

## 🏞️ 2. Hồ Dữ Liệu Hổ Lốn: Data Lake (DL)
Amazon Định Đập Phá Luật. Ra Giao Cú Tuyên Bố Data Lake (Amazon S3).
- Cứ Vút Toàn Bộ Gì Mọi Thứ Phát Sinh Gác Hệ Thống (File CSV Rác, JSON Click Lôi Mù, File PNG Lỗi Giao Nhận Lỗ Hổ) Quăng Rác Đổ Tuốt Xuống 1 Đáy Storage Thô Lớn Khổng Lỗ Giá Siêu Rẻ (Raw Unstructured Data).
- Giải Quyết Bài Lộ Tiết Thiếu Hụt Rõ Cắt Của Warehouse Gò Bó. Kiến Trúc Sửa Phễu Lại Là: **ELT (Extract Bóc -> Load Quăng Lọt Hồ Không Cần Lọc -> Transform Khi Nào Data Science Xài Lấy Code Spark Quái Chọc Phá Mới Bắt Máy Lọc Nhấn).**
- **Ưu:** Giá Mất Tiền Cực Kém (Rẻ Kinh Người Lõi S3 Cloud). Khả Trữ Sóng Model Lớn (Ảnh, Log) Giúp Machine Learning Nhai Ngọt Rập.
- **Khuyết Vỡ Nợ (Data Swamp):** Vì Vứt Rác Cả Đống Nên Nếu Cần Trả File Lấy Trình Báo Cáo Gấp Ngay! Không Bắt Kênh DB Truy Câu Query Gọn Đứt Đoạn Nhanh Lập. Lập Tức Hồ Này Chuyển Hóa Thành *Đầm Lầy Rác Hôi*.

---

## 🛥️ 3. Pháo Đài Lakehouse: Giải Lệnh Cuộc Chơi Kỷ Nguyên (Databricks)
Hãng Đai Trưởng Vua Lũ Spark (Databricks) Năm 2020 Công Cáo Sinh Mệnh Kiến Trúc Thần Kỳ: Tại Sao Không Dựa Trên Giá Rẻ Hồ Data S3 JSON Thô Rác, Sau Đó Trát Một Lớp Gạch Men Ngăn ACID Table Tấm (Giống Database Mảng Kho DWH) Lên Mặt Nước?? 
Sực Phát Mệnh Ra Trúc **Delta Lake (Lakehouse)** ra đời, định đoạt sự nghiệp nghề Kỹ Sư Dữ Liệu Modern Data Stack.

- Tựa Máy Tranh Lakehouse: Giữ Nguyên Giếng Rác Giá Rẻ Của Đít S3 Amazon (Hút Mọi File Rác Audio ML Máy Nuốt Không Gò).
- Gắn Gương Tấm Quản Mảng Mặt Metadata Quãn Nghĩa Data Ràng Buộc: Vẫn Cho Khách Hàng Gõ SQL Khung Chạy Nhanh Ráp Kho Báo Trình Ngang Ngửa Warehouse Triển Sâu Lệnh Khoảng Time Travel Kéo Trượt Dữ Lạc Xóa (Máng Lọc Đề).
- **Vương Tồn Mãi Vĩnh Trục:** Hiện Nay Dưới Quy Nghề Các Lính Chuyên Cốt (Data Engineer Tỉ Mảnh) Cảm Ứng Rã Hoàn Toàn Data Lakehouse Nền Trọng Yếu Phụng Đón Nước Tăng Chảy Không Dừng!
