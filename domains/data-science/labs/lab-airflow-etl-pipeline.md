# Lab Lập Lịch Khống Chế Data Cực Đoan Mịn Màng: Xây Hệ Thống ETL Pipeline Bằng Apache Airflow

> [← Back to Data Science Labs](../README.md)

Làm Data Analytics xong, ra viết cái file `script_xu_ly.py`. Báo sếp "Thằng báo cáo hoàn thành". Sếp dặn: "Em ráng cài cho máy tính tự chạy mỗi 5h sáng kéo data xuống cho Sếp Coi lúc Vừa Thức Dậy Giáng Uống Cà Phê Nhé".
Thế là người Cùi (Data Analyst Mầm) Đụng: Cài Windows Task Scheduler Hay CronJob Linux cắn hàm gọi script Python. Được 3 Ngày Lấy Sót Mất Điện Đứt Mạng Script Đứng Đơ Tự LỖI MỊN, Khách Mất Sạch Data Mà Anh Analyst Chống Cột Ngủ Quên Ngây! Báo Cáo Sai Hoàn Toàn Tế Bào! 

Chào đón Vương Phi Orchestration Giám Sát Giành Bện Thẳng Mùa Trọng **Apache Airflow**. Công Cụ Python Tạo **DAG (Directed Acyclic Graph) Sơ Đồ Chiều Trình Dòng Chảy** Chặn Biết Bao Giờ Data Thảy Nhầm File Vớ Rơi Rớt, Báo Rung Slack Cấp Cứu Data Engineer Kịp Lúc Sáng Cứu Xoang Lưới!

---

## 🕸️ 1. Khai Cửa Thành Trì Airflow
Vì Airflow Xài Postgres Chống Ruột Làm Đầu Dữ Chơi Khá Nhọc. Standard Là Docker-Compose Văng Full Lộ Lõi Bù Vào.
Nhưng Động Tác Mock Up Nhanh Lập Trình Cho Các Data Engineer Rèn Tool Lắp Nhánh Khởi Lên Khá Đơn Gọn.
Trong Node Linux Của Bạn Tải:

```bash
pip install apache-airflow
airflow standalone
# Lệnh Này Mở Màn Ghi Password Admin Tối Tuyến Ra Dãy Terminal Phản Quay Chạy Trình Duyệt Go Localhost:8080 Coi Cụt Màn Nước Tưởng Điều Tàu Chú Airflow Nheo!
```

---

## Đúc Súng Ống Truy Bơm Rửa Hút Dữ SQL Kéo Dân Mạng Bằng Code Python Thuần 1 Mạch `etl_pipeline_dag.py`
Data Engineer KHÔNG GIÁM SÁT BẰNG MẮT, HỌ DÙNG CODE (Infrastructure as Code Workflow).
Code Kịch Bản: Sáng Kéo CSV Trễ Sale Về, Rã Xóa Rác NULL Giữa Chừng, Khớp Đâm Xuyên Vào Data Warehouse Kệ Tủ (Kho Trơn Data Mềm). Vất Vào Thư Mục `/airflow/dags/etl_hang_ngay_dau.py`:

```python
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
import pandas as pd # Gọi Anh Quét Rác Thuần Lên Mạch Xử Nhanh Data Khúc Nhỏ Xí 

# 1. Đặt Quy Tắc Vi Phạm Cực Hạn (Chạy Chết 3 Lần Thôi Báo Hỏng Cực Rớt Rễ Nghỉ Chờ Dev Cứu Cứng)
chuan_that_bai = {
    'owner': 'KySuDataLien',
    'retries': 3,
    'retry_delay': timedelta(minutes=5),
}

# 2. Rã Lệnh Sinh Học Khởi Mạch Gốc (DAG - Directed Acyclic Graph) (Hằng Ngày Bò Chạy Máy Bóc Chết Data Đi)
dag_hut_nuoc = DAG(
    'ETL_QuyTrinh_Hut_Data_Dem_Khuya',
    default_args=chuan_that_bai,
    description='Mấy Ống Lọc Thông Đổ Ngầm Thắt Pipeline 5H Sáng',
    schedule_interval='0 5 * * *', # Chạy Lịch Đúng 5H Sáng Cron Form Giao Mệnh 
    start_date=datetime(2025, 1, 1),
    catchup=False,
)

# ─── BƯỚC E (EXTRACT - BÓC NGUỒN TỰ NHIÊN) SẠCH RÚT ─────────
def chuc_nang_boc_rut_du_lieu_tu_api():
    print("🚁 TRỰC THĂNG ĐÃ KÉO. Đang dùng lệnh Kéo Nước Ra Hố Data Hồ S3 Hỗ Lốn Nháp Bóc Dòng Gốc Căng JSON Rời Tụ...")
    # Cắm Dummy Data Giả Thay Vì Web Lập Phá Network Làm Ví Dụ Phóng Kho!
    data_goc_rach = {'MaGiaoDich': [1, 2, None, 4], 'TienKhachMua': [150, -500, 300, 0]}
    df_nhap = pd.DataFrame(data_goc_rach)
    df_nhap.to_csv('/tmp/hut_tam_data_tho.csv', index=False)
    return "Xong Lệnh Bóc Lõi Hút Dạ Về Khạp Rỗng!"

# ─── BƯỚC T (TRANSFORM - QỤY ĐẬP TÂN TRANG LÀM RÕ TẮM SẠCH) ─────────
def chuc_nang_sua_bien_the_xuyen_mau():
    print("✨ ÉP RỬA CHẢY. Bóc Rách File Gốc CSV Kia Chuyển Tiền Âm Lừa Đảo Quăng Hủy Bóp Xén Rỗng...")
    df_dang_rua = pd.read_csv('/tmp/hut_tam_data_tho.csv')
    # Bấm Dập Cụt Thằng Null Văng
    df_sach = df_dang_rua.dropna()
    # Thằng Nào Dám Hack Chỉnh Khống Đơn Giá Tiền Bị Âm Vất Dạt Xa
    df_sach = df_sach[df_sach['TienKhachMua'] > 0]
    
    # Save Cục Vàng Tinh Chế Rớt Bọc Hoàn Mĩ
    df_sach.to_csv('/tmp/vien_ngoc_thu_data_sach.csv', index=False)
    return "Lưới Lọc Vàng Kẹt Tẩy Thành Công Tạp Rễ Đá !"


# ─── BƯỚC L (LOAD - RƯỚC HOÀN MỸ BỎ TÚI CẤT VÀO  DATABASE WAREHOUSE BÁO CÁO  TÓC SẾP MỊN MÀNG) ─────────
def chuc_nang_rot_kho_dua_vach_giau_tien():
     print("🛸 BẦU THỦY RƠI KHO. Nhúp Gương Cập Data Vàng Thổi Đẩy Nén Khung Insert Cúp Máy Postgres Lõi Data Warehouse !")
     # Ở Bước Cầm Chuyển Cứu Cánh Này Bạn Dùng SQL Alchemy Trút Pandas Hoặc Copy Ném Căng Ròn Database Khung SQL! Sắp Hiện Table Xuyên! (Đỡ Tốn Gõ Dòng Thêm DB Fake Ở Đây Giảm Nặng Lưới). 
     print("✅ Data Đã Tọa Lạc Binh Dinh Nhãn Khớp Chặt Report Bền Tận! ")

# 3. Chấn Quẩy Đầu Dây Trình Vệ Binh (TASKS Node)
lenh_boc = PythonOperator(
    task_id=' Extract_Bot_API',
    python_callable=chuc_nang_boc_rut_du_lieu_tu_api,
    dag=dag_hut_nuoc,
)

lenh_rua = PythonOperator(
    task_id='Transform_Rua_Dung_Vat',
    python_callable=chuc_nang_sua_bien_the_xuyen_mau,
    dag=dag_hut_nuoc,
)

lenh_nhap_kho = PythonOperator(
    task_id='Load_Kho_Warehouse_Vang',
    python_callable=chuc_nang_rot_kho_dua_vach_giau_tien,
    dag=dag_hut_nuoc,
)

# 4. TRÓI SỢI CƯỚC Sắp Đặt Khung Lưới Giao Trình Chiều Mũi Tên Đập Lọc Lắp Sạch Chảy Cuốn Thẳng Ống Xuyên Đỉnh 
lenh_boc >> lenh_rua >> lenh_nhap_kho

# NẾU Bước Extract Tạch (Data Source Lỗi API)! Nó Sẽ Dáng Chặn Tắt Lửa Ngay Chặn Thằng (Transformation) Nước Rửa Đang Chờ Báo Chuyển Đỏ App Gáy Kêu Data Enginner Cứu Code! Khép Chặt Kín Mệnh Mạch! Không Cản Dơ Phân! Ngạo Cứu Hóa Đại Hùng Lưới Nước Automation Nhựa Thành Không Điểm Lạc ! Đỉnh Tới Quá Tầm Với Data Nhà Cấp Tự Tại! 💯🚀
```
