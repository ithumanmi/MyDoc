# 🧬 Data Science & Big Data Engineering Roadmap

> [← Back to Home](../../README.md)

Chào mừng bạn đến với vùng đất của Dữ Liệu Khổng Lồ (Petabytes Data). Nếu **[Data Analytics](../data-analytics/README.md)** dạy bạn cách dùng SQL và Excel để báo cáo doanh thu tháng trước, thì **Data Engineering** và **Data Science** gánh vác sứ mệnh tạo ra Hệ Thống Đường Ống Tự Động Rửa Data (ETL) và dự phóng Dự Đoán Tương Lai (Machine Learning).

---

## 🧭 1. Phân Định Nghề Nghiệp (Data Engineer vs Data Scientist vs ML Engineer)

Đừng nhầm lẫn 3 vai trò cực kỳ khác biệt này, múc đích rõ sẽ giúp bạn đi đúng Roadmap mà không bị ngộp:

| Tính Chất | 🛠️ Data Engineer (Kỹ Sư Hệ Thống DS) | 🔬 Data Scientist (Nhà Phân Tích DS) | 🤖 ML Engineer (Kỹ Sư Máy Học AI) |
| :--- | :--- | :--- | :--- |
| **Vai trò** | Thợ Ống Nước (Gánh Data Từ App Gốc Đổ Về Hồ Chứa) | Thợ Chế Biến Món (Lấy Nước Từ Hồ Chứa Lọc Insights) | Thợ Gắn Bơm (Đem Món Lấy Thành App Chạy Auto) |
| **Công Cụ Lõi** | Python, SQL, Apache Spark, Kafka, Airflow, Hadoop | Python, R, Pandas, Math, Jupyter Notebook | TensorFlow, PyTorch, Docker, MLOps |
| **Kiến trúc DB** | Data Lake, Data Warehouse (Snowflake, BigQuery) | ML Model, Statistical Models A/B Testing | Model Serving (FastAPI, ONNX) |
| **Điểm Khó Lớn Nhất** | System Design Phân Tán, Kẹt Dữ Liệu Lỗi Batch, Mất Data | Toán Học Dày Đặc, Thống Kê Ngụy Biện (Bias) | Triển Khai App Thực Tế Chết Máy RAM/VRAM CPU GPU Hư Rụng |

> **🔥 Lời Khuyên:** Hãy bắt đầu từ **Data Analytics** -> Chuyển Sang Bơm Rửa Hút Pipeline **Data Engineering** trước để Đắt Giá, sau đó hẵng Dấn Vào Giải Toán **Data Science**.

---

## 🏗️ 2. Lõi Kiến Trúc Kỹ Sư Dữ Liệu Khổng Lồ (Big Data Architecture)

SQL không thể SELECT trên 1 tỷ dòng dữ liệu mà không chết máy tính. Hãy Quên MySQL/PostgreSQL Đi! Nhập môn Big Data Storage & Computing Architectures:

1. **[Mổ Xẻ Động Cơ Dữ Liệu Hadoop & Bản Thay Thế Hoàn Hảo Apache Spark](./big-data/hadoop-spark-internals.md)** (⭐ **Must Read**). Tại Sao Kiến Trúc In-Memory Dataframes của Vua Phân Tán Spark Gấp 100 lần Tốc Độ Cuộn Disk I/O MapReduce Cũ Gỉ.
2. **[Kho Lưu Khổng Lồ: Data Warehouse vs Data Lake vs Lakehouse](./architecture/data-warehouse-lakehouse.md)** (⭐ **Must Read**). Hiểu rõ Khái Niệm ETL Cổ Điển Mỏng Yếu vs Sự Trỗi Dậy Của Hệ Thống Cải Tiến Dòng ELT Phi Định Hình.

---

## 🧪 3. Xưởng Kỹ Sư Khoa Học Thực Chiến (Data Engineering Labs)

Lý thuyết phân tán Cluster vô dụng nếu không viết Pipeline. Dưới đây là 2 Móng Nhà Bạn Phải Rành Rõ Trên Đôi Bàn Tay:

### 🐍 Lab 1: Vứt Bỏ Pandas Đồ Chơi, Đón Chào Cỗ Máy Phân Tán
*   **[Thực Chiến Xử Lý Data Khổng Lồ Bằng PySpark (In-Memory Computing)](./labs/lab-pyspark-big-data.md)**: Không Thể Load File CSV 50GB Lên RAM Laptop 16GB. Spark Chia Mảnh Data Trả Node Hướng Giải Quyết. Chuyển Form Lưu Thành File Apache Parquet Đứng Trên HDFS Rất Cao Chuẩn Nén Siêu Chót Vót!

### 🛫 Lab 2: Nữ Vương Tự Động Định Tuyến Ống Nước (Workflow Orchestration)
*   **[Lên Lịch ETL Pipeline Khét Lẹt Bằng Apache Airflow](./labs/lab-airflow-etl-pipeline.md)**: Dùng Khung Python Viết DAG (Directed Acyclic Graph). Tạo Cụm Bot tự Bò Dữ Liệu Mỗi 3h Sáng -> Rửa Rạch Lọc Data Bằng Pandas/Spark -> Bơm Tuột Xuống Kho Postgres Lõi Warehouse Mờ Rỉ Gọn Gàng! Cứu Thay Cho Trình Cronjob Mù Mờ Code Bash Shell Khập Khiễng.

---

> **🚀 Con Đường Lập Trình Viên Đạt Mức Lương Trăm Củ Tại Silicon Valley:** 
Bạn Vừa Cắt Mạch Đôi Tay Qua Backend Lập API CQRS Mạng. Chút Thiết Kế Hệ Thống Red Teaming C2 Security Chắn Trọ. Biết Kéo Nước Phân Tách Cluster Big Data Bằng Spark Tự Đổ Hàng ETL. Chúc Mừng, Bạn Không Còn Gì Để Sợ Trong Giới IT Lõi Cứng Staff Engineering Từng Bày Biên!
