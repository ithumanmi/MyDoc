# Lab Dữ Liệu Khổng Lồ: Phân Rã & Lọc 1 Triệu Dòng Data Bằng PySpark

> [← Back to Data Science Labs](../README.md)

Làm Data Analyst bằng thư viện `Pandas` (Python) rất sướng, cho đến khi File CSV bạn tải về nặng **50GB**. Máy Laptop bạn 16GB RAM lập tức văng `MemoryError` sập nát màn hình xanh. Mọi nỗ lực của Pandas là vô vọng vì nó bị khóa ở Cấu trúc Đơn Nhân (Single Node Computation / Đứng Chết 1 Máy).

Hôm nay, ta sẽ mời Vũ Khí Hạng Nặng **PySpark** của các Vị Thần Data Engineer. Mảnh code nhỏ bé này vứt lên Cluster 1,000 Máy Tính, nó tự Chia Khối (Partitioning) Cấp Gấp Nhau Đánh Sạch Hàng PB Data Mượt Như 1 Máy Mình Đang Cầm!

---

## 🌩️ 1. Khởi Động Động Cơ Máy Kéo Spark (Local Mode)

Cài đặt Thư Viện (Trong máy tính chạy Demo Dùng Hết Lõi CPU Laptop):
```bash
pip install pyspark
```

Chúng ta sẽ mở một Kết Nối Nhánh Mạng (Session) Vào Động Cơ Tàng Hình Phân Tán:
```python
# test_pyspark.py
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, desc

# 1. Gọi Đứng Máy Cày Spark Lên Đầu Tiên 
# '.master("local[*]")' - Tao Cho Phép Mày Ăn Hết Sạch Số Lõi CPU Thằng Laptop Này Có !
spark = SparkSession.builder \
    .appName("Sieu_May_Nghien_Du_Lieu") \
    .master("local[*]") \
    .config("spark.driver.memory", "4g") \
    .getOrCreate()

print("⚡ VUA KHỈ BIG DATA ĐÃ TỈNH GIẤC:", spark.version)
```

---

## 🗃️ 2. Đọc File CSV Hàng Cục Chục GB (Lazy Evaluation)

Tạo thử 1 file cực lớn (Bạn tự tưởng tượng hoặc dùng Script Python sinh Dummy Data 1 triệu dòng nhé). 
Sự Khác Biệt Giữa Pandas vs Spark:
- **Pandas Dataframe `pd.read_csv()`**: Lôi File Nặng 10GB Tự Bóp Cổ Nhét Cố Xác Vào RAM Máy Nóng Cháy Quạt Kêu Cáu Đứt Cầu Chì Màn Mất!
- **Spark Dataframe `spark.read.csv()`**: Chớp mắt Dưới 1s Ra Kết Quả! Nó Không Load Rác Lên Ram! Nó Tạo Con Trỏ Dò (Pointer) Ghi Map Dòng Xuống Đĩa Ảo Chờ Sai Bảo Đếm Đít. Gọi là **Lazy Evaluation**. 

```python
# 2. Đọc Đập Mỏ Cố Vào Đống Đất Data Thô
df_khong_lo = spark.read.csv(
    "du_lieu_ban_hang_2030_sieu_nang_1M_dong.csv", 
    header=True, 
    inferSchema=True # Đoán Từ Khóa Type ID/Tiền
)

# Chỉ in ra bộ mặt sườn khung Schema Table. Chưa Chạm Vào Data Cắn Ram:
df_khong_lo.printSchema()
```

---

## 🧨 3. Trút Transform (Rửa & Nắn Bóp Dữ Liệu)
Mệnh Lệnh "Này Nhánh Lính Spark Máy Con! Lũ Chúng Mày Lọc Cắt Mảng Dữ Liệu Dành Cho Tao Tập Khách Nữ Gái Tuổi Cao Hơn 20 Nhưng Mua Hàng Xa Xỉ Hơn Tiền Triệu Đổ Bật Bỏ Đám Mua Bậy Tạp Hoá Vứt Nhỏ Nhanh Nào!"

```python
# Kéo Gạch Sắp Mạch Bằng Lưỡi Cưa SQL Filter Phân Tán
df_khach_hang_vip = df_khong_lo.filter(
    (col("age") > 20) & (col("gender") == "Female") & (col("total_spend") >= 1000000)
).select("user_id", "city", "total_spend") \
 .groupBy("city") \
 .sum("total_spend") \
 .withColumnRenamed("sum(total_spend)", "tong_tien_thang_dai_gia_mua") \
 .orderBy(desc("tong_tien_thang_dai_gia_mua"))

print("Khâu Chốt Nối Các Đường Ống Lọc Xong Gọn Sạch.")
```
> Ở Bước Này, Vẫn Không Hề Tốn Lượng Lớn RAM. Spark Mới Dựng Đứng Cái Sơ Đồ Khối Thực Thi Kế Hoạch Đánh Bóp (DAG Execution Plan) Tối Ưu Quăng Vào Backend Catalyst Chạy Chờ! Sợi Luồng Nhanh Trút Quả Tối Sốc. Mượt Máy! Tránh Được Mù Code Tối!

---

## 🔥 4. Khai Hỏa Súng Ống (Action & Rút Đổ Tàu Biển Parquet)
Chỉ Khi Gọi Hàm Mệnh Lệnh Định Cố Sát Gút Data (Action): `show()`, `count()`, hay `write`. Cả Hệ Thống 10,000 Mảng Máy Cụm Cày Mới Thể Hiện Sức Căng Sóng Lọc Màn Tí Hon 1ms Data Sạch Bưng Bỏ Túi Mình 1 Triệu Khung Dữ Liệu Mức Đại Bàng Nhanh Như Kẻ Vạch Đất: 

```python
# Cho Tao Xem Tạm 5 Kết Quả Giàu Nhất Vừa Tìm Ra Chốt Đầu
df_khach_hang_vip.show(5)

# 🎇 ĐỘT PHÁ TÀNG HÌNH FILE GIÁ TRỊ: Lưu Từ File CSV Cục Mịch Nặng Kịch Xuống File Siêu Nén Chuyên Dùng Cho Thế Giới Big Data: Dịnh Dạng Data Lake PARQUET !! Khách Nhẹ Mãng Load Khúc Nhanh Quái Mực Gấp X200 Lần.
df_khach_hang_vip.write.mode("overwrite").parquet("KetQua_BaoCao_VIP_Tuoi_Gai.parquet")

# Đỉnh Tốc Data Engineer Ký Dấu Sóng Chôn Spark Lụi Lặn Giải Tán Số Máy Vờ Nháp RAM Máy Đủ Lành Mát Kéo Tay Nhẹ Quạ!
spark.stop()  
```

> **Hết Labs:** Code Python Pandas Của Analyst Trông Như Chiếc Xe Quét Rác Điện. Còn Gắn Từ Ngữ Dataframe Kèm Ký Tự Mạng Lưới Nhành Móc Tụ *PySpark* Vào, Code Của Bạn Mang Sức Máy Ủi Gầu Xúc Thiết Giáp Đại Công Trường Xé Phạt Petabytes Phút Kinh Hoàng Của Sân Chơi Big Data Engineer Máu Khủng!💯
