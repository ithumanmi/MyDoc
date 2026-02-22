# 📊 Deep Dive: Design Logging & Monitoring System

> **"Mục tiêu: Thiết kế một hệ thống tập trung thu thập logs và metrics từ hàng nghìn server, hỗ trợ tìm kiếm thời gian thực và cảnh báo tự động khi có lỗi xảy ra."**

---

## 1. Clarify Requirements (Làm rõ yêu cầu)

Đây là bài toán rất rộng, hãy bắt đầu bằng việc phân loại dữ liệu:
*   **Logs:** Dữ liệu sự kiện chi tiết (ví dụ: "User A logged in at 10:00"). Nặng về lưu trữ và tìm kiếm văn bản.
*   **Metrics:** Dữ liệu định lượng (ví dụ: "CPU Usage is 80%"). Nặng về tính toán và vẽ biểu đồ.

### Functional Requirements
*   **Collection:** Thu thập dữ liệu từ nhiều nguồn khác nhau.
*   **Querying:** Tìm kiếm log theo từ khóa hoặc khoảng thời gian.
*   **Alerting:** Gửi tin nhắn/email khi một chỉ số vượt ngưỡng (ví dụ: tỷ lệ lỗi > 5%).
*   **Visualization:** Hiển thị biểu đồ (Dashboard).

---

## 2. Back-of-the-envelope Estimation (Ước lượng)
*   **Scale:** 1.000 services, mỗi service chạy trên 10 node -> 10.000 nodes.
*   **Write rate:** Giả sử mỗi node tạo ra 100 log lines/giây -> 1 triệu log lines/giây.
*   **Storage:** 1 log line ~ 500 bytes -> 500MB/giây -> ~43TB/ngày.
*   **Thách thức:** Hệ thống cực kỳ **Write-heavy**. Cần giải pháp ghi nhanh và nén dữ liệu tốt.

---

## 3. High-level Design

### Components
1.  **Log Agent:** Một phần mềm nhỏ (Sidecar) chạy trên từng node để bốc log và gửi đi.
2.  **Message Queue (Kafka):** Vùng đệm để hứng luồng dữ liệu khổng lồ, tránh làm sập hạ tầng lưu trữ.
3.  **Indexing Service (Logstash/Fluentd):** Tiền xử lý, lọc và format dữ liệu trước khi lưu.
4.  **Storage:**
    *   **Logs:** Elasticsearch hoặc OpenSearch (Tìm kiếm văn bản cực tốt).
    *   **Metrics:** InfluxDB hoặc Prometheus (Time-series DB chuyên biệt).
5.  **Alerting & Visualization:** Grafana (biểu đồ) và PagerDuty (cảnh báo).

---

## 4. Deep Dive: Ingestion & Storage Strategy

### Push vs Pull Model (metrics)
*   **Pull (Prometheus style):** Server giám sát chủ động đi hỏi từng service. 
    *   *Ưu điểm:* Dễ quản lý trạng thái các node (biết node nào chết).
*   **Push (Graphite style):** Service tự gửi dữ liệu đến server giám sát.
    *   *Ưu điểm:* Tốt cho các kiến trúc ngắn hạn (Serverless, Batch jobs).

### Lưu trữ phân tầng (Tiered Storage)
Với 43TB/ngày, ta không thể lưu mãi trong Elasticsearch (rất đắt).
*   **Hot Tier:** Dữ liệu 7 ngày gần nhất, lưu trên SSD để tìm kiếm nhanh.
*   **Warm Tier:** Dữ liệu từ 7-30 ngày, lưu trên HDD.
*   **Cold Tier:** Dữ liệu > 30 ngày, nén chặt và đẩy lên S3/GCS phục vụ việc tra soát (Audit) khi cần.

---

## 5. Deep Dive: Alerting System

Làm sao để không bị "nhiễu" cảnh báo (Alert fatigue)?
1.  **Aggregation:** Thay vì gửi 1.000 email khi 1.000 node cùng báo lỗi, hãy gộp lại thành 1 cảnh báo duy nhất cho toàn bộ service.
2.  **Deduplication:** Loại bỏ các cảnh báo trùng lặp.
3.  **Throttling:** Giới hạn số lượng cảnh báo gửi đi trong 1 phút.

---

## 6. Interview Pro-tips (Trade-offs)

1.  **Indexing Latency:** Log sau khi ghi vào Kafka sẽ mất khoảng vài giây mới xuất hiện trên Elasticsearch. Hãy thảo luận về đánh đổi giữa **Real-time** và **Throughput**.
2.  **Sampling:** Với logs thông thường (200 OK), ta có thể chỉ lưu 1% dữ liệu để tiết kiệm bộ nhớ. Với logs lỗi (500 Error), ta phải lưu 100%.
3.  **Kafka Partitioning:** Sharding dữ liệu trong Kafka theo `service_id` để đảm bảo thứ tự các dòng log của cùng một service.

---

## 🏁 Kết thúc Series Top 10
Bạn đã hoàn thành việc tìm hiểu 10 bài toán System Design kinh điển. Chìa khóa thành công không nằm ở việc học thuộc lòng sơ đồ, mà là ở khả năng **giải trình các đánh đổi (Trade-offs)**.

---

## 📚 Tài liệu tổng kết
*   [Top 10 Problems Overview](./top-10-problems.md)
*   [How Redis Works (Cốt lõi của Distributed Cache)](./how-redis-works.md)
