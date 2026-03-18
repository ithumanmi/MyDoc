# Phẫu Thuật Động Cơ Big Data: Sự Tàn Lụi Của Hadoop & Kỷ Nguyên Vua Khỉ Apache Spark

> [← Back to Data Science Roadmap](../README.md)

Lưu trữ 1 MegaByte (MB) thì dùng SQL Server. 1 GigaByte (GB) dùng PostgreSQL. Nhưng khi một Tập Đoàn Công Nghệ phải phân tích **1 PetaByte (PB) = 1,000,000 GB** dữ liệu người dùng Click mỗi ngày, cắm thêm thanh RAM hay nắp ổ cứng SSD vào một con Server đắt tiền (Scale-up) là điều vô phương và lãng phí. 
Giải pháp là mua 10,000 con Laptop cùi bắp, ghép chúng lại thành một cụm (Cluster / Scale-out). 

---

## 🐘 1. Khởi Nguyên: Hadoop & Sự Tàn Lụi Của MapReduce

Doug Cutting tạo ra **Hadoop** (Con Voi Chết Chìm) vào năm 2006 mang lại bình minh cho Big Data. Hadoop chia làm 2 lá phổi chính:

### A. HDFS (Hadoop Distributed File System - Bộ Nhớ Vô Tận)
Thay vì nhét 1 file 1TB vào 1 máy (Không máy nào chứa nổi lúc bấy giờ, hoặc cháy ổ).
HDFS Cưa cái file 1TB đó ra thành các cục (Blocks) nhỏ 128MB. Rải đè 10,000 cục 128MB này lên hàng ngàn máy tính rẻ tiền (Data Nodes). Nếu 1 máy Cháy Ổ Cứng Khét Nghẹt? Không sao, HDFS đã lặng lẽ Copy 1 cục sang 3 máy khác nhau (Replication Factor = 3).
-> **HDFS Vẫn Là Vua Lưu Trữ Nháp Giá Rẻ (Cost-Effective) Đến Tận Bây Giờ.**

### B. MapReduce (Cái Máy Cày Sắt Cũ Kỹ Độ Trễ Cực Khủng)
Xong Dữ liệu, giờ đem Tính Toán Phân Tán (VD Đi đếm chữ cái).
*   **Map (Kiếm Hàng):** Sai 10,000 cái máy tự đếm chữ trên cái block 128MB mà tụi nó ôm.
*   **Reduce (Gom Hàng):** Gom kết quả 10,000 máy lại Rút Ra Cột Tổng Cuối Gọi Xuất Kho.

**🚨 Vì sao MapReduce Vã Chết Chìm Xó Bếp? (Căn Bệnh Disk I/O)**
Vì Mỗi Một Bước Tính Toán Khớp, Thằng MapReduce Đều Lôi Ghi Vào Ổ Khóa Cứng (Write to Disk) Trọng Trác Nhầm Đề Phòng Máy Cháy Chết Ngang! Gặp Tính Thuật Toán Tự Lặp Trả Dữ (Machine Learning Trả 100 Vòng Lặp Epoch), MapReduce Sẽ Ghi Ổ Cứng 100 Lần. Chết Trân Hệ Thống Toàn Chuỗi I/O (Đọc/Ghi Vật Lý Cực Chậm)!

---

## ✨ 2. Vua Phân Tán Mới Hệ Chớp Mắt: Apache Spark (In-Memory Kỷ Nguyên)

Năm 2014, một nghiên cứu sinh Đại Học UC Berkeley ra mắt chiếc Đũa Thần Spark Đập Chết MapReduce, hứa hẹn Tốc Độ **Gấp 100 Lần!** 
Làm Sao Đạt Cảnh Giới Đỉnh Tốc Đó?

### A. Ma Thuật RDD (Resilient Distributed Dataset) & Xử Lý In-Memory
Thay Vì Vừa Làm Vừa Chép Bài Xuống Ổ Cứng Như Thằng Ngốc MapReduce. 
Spark Táo Bạo Mang Phun Nhét Data Lỗ Cắn Vào **RAM (In-Memory)**. Nó Mở Kho Thao Luyện Cực Khủng Lấp Khoảng Hở CPU. Nếu Đi Đường Bị Mất Điện Lỗ RAM Sụp Thì Sao? Spark Chỉ Ghi Lại Hành Trình Nó Đã Cuốc Cào RDD (Lineage Graph - Sơ Đồ Chỉ Mục Lê Lệnh Vượt Mức). Tới Hồi Bật Điện Nó Vịn Hình Sơ Đồ Cày Trả Mạng Phục Khôi Vài Giây! Không Ép HDD Xuyên Chảy Xước Dĩa!

### B. Lazy Evaluation (Kế Hoạch Bùng Nổ Cuối Phút Chót)
Khi Bạn Viết Lệnh Spark `Lọc Data Nữ -> Tách Tuổi Trên 18 -> Gom Đếm Phân Vùng`.
Spark Đọc Thấy Code Của Bạn, Nhưng Nó **Cười Khẩy Không Thèm Làm** (Transformations). Nó Gom Nhét Các Lệnh Của Bạn Vào Nháp DAG Lưới Luồng. Rút Giảm Đường Dịch Cho Cực Ngắn! Cắt Số Xấp Rác.
Chỉ Khi Nào Bạn Chốt Gõ Kích Lệnh Rút Chó Cuối Đuôi Cắn Lấy: `show() đếm dòng, lấy dữ save xuống file` (Actions). Spark Mới Phóng Mìn Trigger Toàn Mạng Nâng Phủ Tác Rập Triệu Dòng Trong Vài Millisecond. Khái Niệm Ngủ Đông Và Đi Tắt Kiến Trúc Tối Siêu.

### C. DataFrame (Giao Diện Bọc Nghe Cấu Trúc Khối)
RDD Ban Đầu Gần Máy Viết Phức Khổ. Spark Đưa Ra DataFrame Giống Hệt Thư Viện SQL Hay Pandas Ai Cũng Code Biết Tiếng Của R/Python. 
Giờ Ta Kéo Data Ghi Kiểu `df.groupBy("Tuoi").count()`. Spark Tự Đuôi Dưới Biến Lệnh Này Xuống Máy Optimizer Khủng (Catalyst) Và Chạy!

> **Sự Nghiệp Mốc Kỷ Lục:** Bất cứ Kỹ Sư Data Nào Biết Dùng Spark Nắn Mạch Pipeline Đánh Kênh Vắt Chảy, Họ Không Còn Là Dev Code Bò Nút Nữa. Ngành Công Tech Gọi Họ Bằng: Hệ Ngũ Master Kiến Trúc Tính Trọng Cỗ Rỗng! Cả Mạch Hệ Thống Khai Thác Kỹ Cục.
