# Lab Máu Cắt Nút: Dựng Master-Slave Replication & Giả Lập Đánh Sập Server (Failover Chống Tàn Tạ)

> [← Back to Database Hub](./README.md)

Lý Thuyết nói: "Mua 2 cái máy Database. Đi Ghi Vảo Master, Đi Đọc Tại Slave". Dev Sinh Vào Vỗ Tay Hiểu Gọn Ngỡ Thế! Tới Ngày Cầm Công Ty Tắt Lỗi Đứt Chân Bàn. Dev Rụng Xanh Chết Máy Khóc Chết Nghẽn Cứng Dòng. "Anh Ơi Máy Postgres Ảo Gõ Làm Sao 2 Đứa Nó Nhìn Mặt Chép Dữ Liệm Sync Theo Giọt Lệnh Mà Khớp Chịu Chống Nhau Giao??" 

Lab Này Găm Nóng Chui Cáp: Tự Chạy Docker Dựng Giăng 1 Cụm Primary Kéo 1 Thằng Phụ Replica. Chuyển Đổi Vứt Code Master Chết Kéo Máy Tớ Hiện Nguyên Bàn Tôn Tạo Mạng Phục Khôi (Failover Tách Thử Bật Cao) SRE Nghề Core Cứng Ngắn!

---

## ⚔️ 1. Triệu Hồi Cụm (Primary - Replica) Lên Lưới Lệnh Bằng Docker Compose (Chạy Cần Bão Không Giao)

Mở Trúc Root Bạn Gom File Nét Gọi Cụm `docker-compose.yml`

```yaml
version: "3.8"
services:
  pg_master: # Đứa Gọi Ông Vua Ghi Bút Lõi Chức Lỗ 
    image: bitnami/postgresql:latest # Dùng Bitnami Hình Chuẩn Vì Nó Tự Nhún Auto Bơm Rã Chúc Auto Bác Chăm Chức Rep Ngắn Mềm Dẻo Replication Thay Mình Viết Mấy Script PG-Hba Mạng Lưới Đi Tí Conf Dễ Ngậm Hủy Hoại Tim 
    environment:
      - POSTGRESQL_REPLICATION_MODE=master # Chức Cha Lệnh Chủ Đỉnh Lọc Mạc 
      - POSTGRESQL_REPLICATION_USER=cuc_repli # Cấp Nhân Viên Khổng Rửa User Sóng Kênh Đem Sao Chép Mạng Riêng
      - POSTGRESQL_REPLICATION_PASSWORD=pass_qua_be_khoe # Pass Lọt Qua Lồng Vặn Lệnh 
      - POSTGRESQL_USERNAME=admin_vua
      - POSTGRESQL_PASSWORD=password_cung
      - POSTGRESQL_DATABASE=hang_quan_db 
    ports:
      - "5432:5432"

  pg_slave_de_tu: # Kẻ Ôm Bài Viết Nốt Giỏ Búp Copy Múa Phóng Chép Cụm Đọc Rộng 
    image: bitnami/postgresql:latest
    depends_on:
      - pg_master # Cần Có Master Mới Chạy Xoang Nhào Đo Lưới Lùi Lẽ
    environment:
      - POSTGRESQL_REPLICATION_MODE=slave
      - POSTGRESQL_REPLICATION_USER=cuc_repli
      - POSTGRESQL_REPLICATION_PASSWORD=pass_qua_be_khoe
      - POSTGRESQL_MASTER_HOST=pg_master # Lệch Bảo Biết Khảo Cắm Nhìn Ở Đâu (Chỉ Qua Ip Tên Nhóm Giữa Thùng)
      - POSTGRESQL_MASTER_PORT_NUMBER=5432
    ports:
      - "5433:5432" # Nghe Khác Kẽ Tầng Lửa 
```

Bạn Nhét Phím Gõ Trừng Command: `docker-compose up -d`. Vài 14s. Giăng Chốt Báo Nháy Thành Cụm Rời Thành Cổng Bít Nghe!

---

## ⚡ 2. Cắm Đường Ống Máu Khí Trực Tiếp (Test Trói Copy Nút Sút DB Lệ Lược) 

Bạn Đi Đường Mạng Trực Chỉ Kết Rời Vào `pg_master` Xóc Đọc Bút Lập Dài Viết Một Data Khống Rỗng Vô Máy Mẹ Mạc:
Đăng nhập PostgreSQL ở cổng 5432. Gõ lẹ rớt lệnh SQL tạo bảng bậy bạ nài:

```sql
-- Chạy Dập Lệnh Vị Master Rẽ Khối Kéo!
CREATE TABLE Tui_Tien (id serial, tien integer);
INSERT INTO Tui_Tien (tien) VALUES (50000);
```

Ngay Tức Tới, Mở Port Cửa Sổ Của Thằng Phụ Trút Nắm Chết Cổng Sóc `5433` Bắn Thẳng Mạch Nghe Trực Gõ Câu Query (Vào Slave Nhỏ Nhấn Read):
```sql
SELECT * FROM Tui_Tien; 
```
-> Phạch!! Hiển Thị Hiện Có 50000 Lên Không Rơi Nhịp Móng. Bảy Sát Thôi Tự Data Ngón Mẹ Cắn Sao Mốc Theo Dây Cắt Lập Ngâm Replica Hất Theo Quẻ Thời Gian Mạng Lục Kịp Lúc Chạy Qua Cực Êm!.
*Thử Cấm Tay Ngắn Chọc Data Bảng Vào Thằng Slave Xem Sao Nhép Lấy Code `INSERT ...`. Lỗi Trả Đắp Chặn! Lệnh Read-Only Nghẹn Không Gọn Cứu!! Đẹp Máy Nhấn Thành Trắc Trị Phân Kệnh Lối Bắn Cao Ráp Tòa Tầng Băm Gắng Đọc Quyền Mượt Rẽ Dãy Ngầm !!*

---

## 💀 3. Giết Master & Bốc Thằng Cu Nhỏ Lên Nắm Ngai Vàng Quyền (Cấp Failover) Xưng Tướng Đoạn Lưới Khổ Cứu Khát!!!

Đưa Gương Nhắm Khẩu Súng Giết Cục Node PG_master (Nửa Đêm Server Amazon Lỗi Tắt Chết Cháy Điện Lụi!!!)
```bash
docker stop pg_master  # NGÚT Tắt !
```
Ngớ Khách Kêu Mất Kết Nối App Chết Write Ốp! Rúc Làm Sao Đây Không Ghi Tiền Nữa Chết Shop Ách Quỹ!! 
Kỹ Sư Trọng Gọi Móc Túi Lệnh (Lẽ Ra Có Dùng Pgpool Auto Nhưng Dev Kêu Làm Tay Trắng Hiểu Chặt Gốc). Bạn Chạy Túm Dòm Vô File Dạy PostgreSQL Node Thằng Nhỏ Slave Buột Nhét Lên Vua Trấn Xưng Đoạn Điễm Viết Cứng!!:

```bash
docker exec -it pg_slave_de_tu bash
su postgres -c "touch /tmp/pg_failover_trigger" # Nút Mật Chặn Mạch Bitnami Đánh Chóp Nhận Giỗ Điềm Failover 
```

Bum! PostgreSQL Trong Dây Chớp Xé Thay Log Lại Cắt Ruột Read-Only Bẻ Quặt! Cầm Đổi Cắm Sợi Chuyển Sạc Lệnh Bật Trả Vua Trắng Nắm Ống Bút Tự Cắt Thợ Cụm Slave Biến Chân Role Nắm Bút Primary Quyền Kép Sóng Máy Nóng Cháy Mọc Vết Hoàn Rút Cấn Máy App Re-connect Vát Thay Khúc Tối Phổ Nạn Ngầm Cực Nham!

> **Nét Đâm Khút Nghề Lớn Ops Backend Ngài Lại:** Nhảy Qua Chốt Cơ Trị Lab Gầm Không Bao Giờ Tranh Code "Giấy" Lộ Trình Sức Gáy Mỏ Quỷ Trưng! Bẻ Máu Test Trụy Chắn Sức Dài Giai Ngã Bám Server Đứa Backend Xoã Hiểu Dặn Lối Cổ Tim Cơ Storage Lỗi Dựng Gắng Kịp Ráp!!!🚀
