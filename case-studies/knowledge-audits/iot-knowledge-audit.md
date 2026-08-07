# 🌐 IoT Knowledge Audit: Thử thách "Smart Factory & Smart Home Hybrid"

> **Mục đích:** Đo năng lực thiết kế, triển khai và vận hành hệ thống IoT end-to-end (Device ↔ Cloud ↔ Data) với yêu cầu bảo mật và độ tin cậy cao.
> **Phiếu trả lời:** Tạo bản sao từ template (gợi ý): `case-studies/answer-templates/ai-answer-template.md` và sửa cho IoT.
> 
> **Kịch bản:** Bạn là **IoT Solutions Architect** cho một tổ hợp nhà máy + khu dân cư thông minh. Hệ thống cần thu thập dữ liệu cảm biến môi trường, điều khiển thiết bị (đèn/relay/motor), bảo mật OTA firmware và hiển thị dashboard thời gian thực. Một số node dùng Wi-Fi/BLE, một số dùng NB-IoT/LoRa.

---

## 🔌 Thử thách 1: Embedded & Connectivity Foundations
*Đo nền tảng MCU, bus giao tiếp, và kết nối cơ bản.*

**Tình huống:** Bạn có 500 thiết bị ESP32 và 200 thiết bị STM32. Yêu cầu: đọc cảm biến nhiệt/độ ẩm, điều khiển relay, gửi dữ liệu về cloud qua MQTT.

**Câu hỏi:**
1) Thiết kế sơ đồ bus và chọn giao thức (UART/I2C/SPI) cho cảm biến và module radio. Khi nào ưu tiên I2C, khi nào SPI?
2) Làm sao debug lỗi kết nối Wi-Fi/BLE trên ESP32? Bạn sẽ log gì ở mức firmware để chẩn đoán? (gợi ý: event loop, RSSI, retry, backoff)
3) Trình bày quy trình cấu hình provisioning Wi-Fi/BLE an toàn cho thiết bị mới xuất xưởng (kiosk/QR/pincode?).

**Thước đo:**
* 🟢 Beginner: Flash được firmware mẫu, đọc cảm biến, publish MQTT.
* 🔴 Expert: Tối ưu pin, cấu hình watchdog, thiết kế backoff/throttle, và có kế hoạch safe-mode khi kết nối thất bại.

---

## ☁️ Thử thách 2: Cloud Ingestion & Device Twin
*Đo năng lực thiết kế tầng cloud cho ingest và quản lý trạng thái thiết bị.*

**Tình huống:** Bạn cần xây dựng backend nhận MQTT từ 700 thiết bị, hiển thị trạng thái thiết bị (online/offline, firmware version) và cho phép gửi lệnh xuống.

**Câu hỏi:**
1) Thiết kế topic MQTT và ACL cho 2 loại vai trò: `device` và `operator`. Cách bạn tách namespace theo tenant/site?
2) Giải thích mô hình **Device Shadow/Digital Twin**. Bạn đồng bộ `desired` vs `reported` state thế nào để tránh xung đột?
3) Nếu dùng EMQX self-host, bạn sẽ đặt rate limit và QoS như thế nào cho thiết bị yếu? Khi nào dùng QoS0 vs QoS1?

**Thước đo:**
* 🟢 Beginner: Thiết kế được topic tree cơ bản.
* 🔴 Expert: Có ACL chi tiết, giới hạn QoS/rate theo role, mapping Twin rõ ràng, xử lý idempotent khi command bị retry.

---

## 🛡️ Thử thách 3: Security & OTA
*Đo năng lực bảo mật thiết bị và pipeline cập nhật firmware.*

**Tình huống:** Cần phát hành OTA cho 700 thiết bị, yêu cầu mTLS, ký firmware và có rollback nếu lỗi.

**Câu hỏi:**
1) Thiết kế quy trình cấp phát cert cho thiết bị (per-device key, CA hierarchy). Bạn lưu key ở đâu? (Flash vs Secure Element/TPM)
2) Quy trình ký firmware và kiểm tra tính toàn vẹn khi boot (secure boot). Làm sao chống rollback attack?
3) Bạn thực hiện staged rollout và health check như thế nào để hạn chế brick thiết bị? Định nghĩa tiêu chí abort?

**Thước đo:**
* 🟢 Beginner: Bật TLS một chiều, OTA thủ công.
* 🔴 Expert: mTLS, per-device cert, ký/verify firmware, staged rollout, auto-rollback và logging đầy đủ.

---

## 📡 Thử thách 4: Data Pipeline & Observability
*Đo năng lực xử lý dữ liệu timeseries, alerting, và giám sát đội thiết bị.*

**Tình huống:** Bạn cần ingest 50 msg/s ổn định. Dữ liệu phải lưu 90 ngày, có dashboard và alert offline/battery drop.

**Câu hỏi:**
1) Thiết kế pipeline: MQTT → Kafka → TimescaleDB (hoặc InfluxDB) → Grafana. Bạn partition Kafka theo gì? retention và compaction ra sao?
2) Bạn thiết kế schema Timeseries thế nào cho sensor (measurement, tags, fields)? Cần downsampling/retention gì?
3) Alerting: định nghĩa rule phát hiện thiết bị offline, pin tụt nhanh, cảm biến lỗi (spike). Bạn tính SLA/SLO cho ingest/latency thế nào?

**Thước đo:**
* 🟢 Beginner: Lưu được dữ liệu vào DB, có dashboard đơn giản.
* 🔴 Expert: Partitioning chuẩn, retention + downsampling, alerting meaningful, SLO cho latency & loss, có dead-letter cho message lỗi.

---

## 🔄 Thử thách 5: Command & Control (C2)
*Đo năng lực thiết kế luồng điều khiển xuống thiết bị an toàn và đáng tin cậy.*

**Tình huống:** Operator muốn bật/tắt relay và thay đổi cấu hình (sampling rate) từ cloud.

**Câu hỏi:**
1) Bạn thiết kế channel/command format thế nào? Cần ack/timeout/retry ra sao để tránh lặp lệnh?
2) Làm sao để command không bị re-play hoặc bị thực thi 2 lần? (idempotency key, version, exp time)
3) Bạn log/audit những gì để truy vết? (user, command, device, status, correlation-id)

**Thước đo:**
* 🟢 Beginner: Gửi được lệnh và nhận ack đơn giản.
* 🔴 Expert: Idempotent, timeout, replay protection, audit log, rate limit, mapping error code rõ ràng.

---

## 🧠 Thử thách 6: Performance, Power & Edge ML (Tuỳ chọn)
*Đo năng lực tối ưu tài nguyên thiết bị và edge inference.*

**Tình huống:** Bạn cần chạy keyword spotting (TinyML) trên ESP32, pin chạy 48h.

**Câu hỏi:**
1) Bạn tối ưu power thế nào (deep sleep, duty cycle, batch send, giảm TX power)?
2) Bạn đo/benchmark latency và memory footprint của model ra sao? Dùng công cụ nào?
3) Khi nào nên đẩy inference lên cloud/edge gateway thay vì chạy trên MCU?

**Thước đo:**
* 🟢 Beginner: Chạy được demo TinyML.
* 🔴 Expert: Power profiling, quantization (INT8), có ngưỡng quyết định offload lên edge/cloud.

---

## 📊 Bảng tự chấm điểm (Scoring Rubric)

| Lĩnh vực | Thang điểm (1-10) | Gợi ý tự vấn |
| :--- | :---: | :--- |
| Embedded & Connectivity | ____ / 10 | GPIO/bus/RTOS, reconnect/backoff, provisioning |
| Cloud Ingestion & Twin | ____ / 10 | Topic/ACL, Twin sync, QoS/rate limit |
| Security & OTA | ____ / 10 | mTLS, key mgmt, secure boot, staged rollout |
| Data Pipeline & Observability | ____ / 10 | Kafka partition, TSDB schema, alerting/SLO |
| Command & Control (C2) | ____ / 10 | Idempotent, timeout, replay protection |
| Performance & Edge ML | ____ / 10 | Power/latency profiling, offload strategy |

### 🏆 Xếp hạng năng lực IoT:
* **0 - 20 điểm:** **IoT Learner** — hoàn thiện Foundations + Connectivity.
* **21 - 40 điểm:** **IoT Engineer** — làm chủ ingest + security cơ bản.
* **41 - 55 điểm:** **IoT Solutions Architect** — thiết kế end-to-end, có SLO/observability.
* **56 - 60 điểm:** **IoT Strategist** — tối ưu fleet-scale, OTA an toàn, edge ML khi cần.

---

## 🚀 Tài liệu/Module gợi ý
* **Foundations:** `domains/iot/README.md` + `domains/iot/foundations/embedded-foundations.md`
* **Connectivity / Cloud / Security:** các module trong `domains/iot/{connectivity,cloud,security}/`
* **Labs:** `domains/iot/labs/` · Challenge: `challenges/iot/`
* **Security:** Secure boot, cert provisioning, OTA rollback.
* **Data:** Kafka/TimescaleDB/Grafana pipeline.
