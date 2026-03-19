# Lab: PostgreSQL replication & failover bằng Docker

> [← Back to Database Hub](./README.md)

Mục tiêu: dựng cụm Postgres primary + replica bằng Docker, kiểm tra replication, sau đó failover thủ công.

---

## ⚔️ 1. Dựng primary/replica bằng Docker Compose

Tạo `docker-compose.yml`:

```yaml
version: "3.8"
services:
  pg_master:
    image: bitnami/postgresql:latest
    environment:
      - POSTGRESQL_REPLICATION_MODE=master
      - POSTGRESQL_REPLICATION_USER=cuc_repli
      - POSTGRESQL_REPLICATION_PASSWORD=pass_qua_be_khoe
      - POSTGRESQL_USERNAME=admin_vua
      - POSTGRESQL_PASSWORD=password_cung
      - POSTGRESQL_DATABASE=hang_quan_db 
    ports:
      - "5432:5432"

  pg_slave_de_tu:
    image: bitnami/postgresql:latest
    depends_on:
      - pg_master
    environment:
      - POSTGRESQL_REPLICATION_MODE=slave
      - POSTGRESQL_REPLICATION_USER=cuc_repli
      - POSTGRESQL_REPLICATION_PASSWORD=pass_qua_be_khoe
      - POSTGRESQL_MASTER_HOST=pg_master
      - POSTGRESQL_MASTER_PORT_NUMBER=5432
    ports:
      - "5433:5432"
```

Chạy: `docker-compose up -d`.

---

## ⚡ 2. Kiểm tra replication

Đăng nhập `pg_master` (cổng 5432), tạo bảng và ghi dữ liệu:

```sql
CREATE TABLE Tui_Tien (id serial, tien integer);
INSERT INTO Tui_Tien (tien) VALUES (50000);
```

Truy cập replica (cổng 5433) và kiểm tra:
```sql
SELECT * FROM Tui_Tien; 
```
Replica sẽ đọc được giá trị, và chặn ghi (read-only).

---

## 💀 3. Failover thủ công

Dừng master:
```bash
docker stop pg_master  # NGÚT Tắt !
```

Chuyển replica lên primary (trigger của Bitnami):
```bash
docker exec -it pg_slave_de_tu bash
su postgres -c "touch /tmp/pg_failover_trigger"
```

Replica sẽ chuyển sang primary và cho phép ghi. Ứng dụng cần trỏ lại endpoint mới hoặc dùng proxy/pgpool để tự động hóa.
