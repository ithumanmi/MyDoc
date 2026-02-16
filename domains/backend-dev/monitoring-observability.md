# 📊 Monitoring & Observability: Eyes on Production

> [← Back to Backend Roadmap](./README.md) | [Home](../../README.md)

Code chạy trên máy bạn là một chuyện. Code chạy trên Production với 10k users là chuyện khác. Làm sao biết server đang sống hay chết? User có bị lỗi không? API chậm ở đâu? Đây là lúc cần **Observability**.

---

## 📋 Mục lục

1. [Logging](#1-logging-nhật-ký-hệ-thống)
2. [Metrics](#2-metrics-đo-lường-sức-khỏe)
3. [Tracing](#3-tracing-theo-dấu-request)
4. [Alerting](#4-alerting-cảnh-báo-thông-minh)
5. [Performance Profiling](#5-performance-profiling-tìm-điểm-nghẽn)
6. [Action Plan](#6-action-plan-setup-như-thế-nào)

---

## 1. Logging: Nhật ký hệ thống

### 1.1. Structured Logging (JSON)

Đừng log text (`User 123 logged in`). Hãy log JSON để máy có thể query.

*   ❌ **Bad:** `console.log("Error: " + err);`
*   ✅ **Good (Winston/Pino):**
    ```javascript
    logger.error("Login failed", {
      userId: 123,
      reason: "Invalid password",
      ip: "192.168.1.1"
    });
    ```

### 1.2. Log Levels

Dùng đúng level để dễ filter:
*   **DEBUG:** Thông tin chi tiết cho dev (SQL query, params). *Tắt trên Prod.*
*   **INFO:** Sự kiện bình thường (App started, Job completed).
*   **WARN:** Có vấn đề nhưng app vẫn chạy (Retry DB connection).
*   **ERROR:** Lỗi ảnh hưởng 1 request (API 500).
*   **FATAL:** Lỗi sập app (Out of memory).

### 1.3. Centralized Logging (ELK Stack)

Đừng SSH vào server đọc file log! Hãy gom log về một chỗ.
*   **Elasticsearch:** Lưu trữ log.
*   **Logstash:** Thu thập & xử lý log.
*   **Kibana:** Giao diện xem log.
*   **Alternative:** Loki + Grafana (Lightweight hơn).

---

## 2. Metrics: Đo lường sức khỏe

Metrics là các con số theo thời gian (Time-series data).

### 2.1. The Golden Signals (Google SRE)

4 chỉ số vàng cần monitor:
1.  **Latency:** Thời gian phản hồi (ms). Quan tâm P95, P99.
2.  **Traffic:** Số lượng request (RPS).
3.  **Errors:** Tỷ lệ lỗi (HTTP 5xx / Total requests).
4.  **Saturation:** Tài nguyên hệ thống (CPU %, Memory %, Disk I/O).

### 2.2. Tools: Prometheus + Grafana

*   **Prometheus:** Kéo (Pull) metrics từ app mỗi 15s.
*   **Grafana:** Vẽ biểu đồ đẹp mắt.

**Example (Node.js + prom-client):**
```javascript
const counter = new client.Counter({
  name: 'http_requests_total',
  help: 'Total HTTP requests',
  labelNames: ['method', 'status']
});
// Inc: counter.inc({ method: 'GET', status: 200 });
```

---

## 3. Tracing: Theo dấu Request

Trong Microservices, 1 request đi qua 5 services. Lỗi ở đâu?

### 3.1. Distributed Tracing

Gắn một `Trace ID` duy nhất cho mỗi request ngay từ Gateway. ID này được truyền qua các services (HTTP Headers).

*   **Tools:** Jaeger, Zipkin, OpenTelemetry.
*   **Visualization:** Waterfall chart cho thấy request tốn bao nhiêu ms ở Service A, bao nhiêu ms ở DB.

---

## 4. Alerting: Cảnh báo thông minh

### 4.1. Alert Fatigue (Bội thực cảnh báo)

Nếu điện thoại reo cả ngày vì "CPU > 50%", bạn sẽ ignore nó. Đến khi "DB Down" thật thì bạn lỡ mất.

**Quy tắc:** Chỉ Alert khi **User bị ảnh hưởng**.
*   ❌ Alert: CPU > 80%. (Kệ nó, Auto-scaling lo).
*   ✅ Alert: Error Rate > 5% trong 5 phút. (User đang gặp lỗi!).

### 4.2. Runbooks

Mỗi Alert phải kèm theo Link đến Runbook (Hướng dẫn xử lý).
*   Alert: "Disk Full".
*   Runbook: "Bước 1: SSH vào server. Bước 2: Chạy lệnh clean log..."

---

## 5. Performance Profiling: Tìm điểm nghẽn

Khi code chạy chậm mà không biết tại sao (CPU cao nhưng không làm gì).

*   **Flame Graph:** Biểu đồ thể hiện hàm nào chiếm nhiều CPU nhất.
*   **Memory Leak:** Heap dump snapshot để tìm object không được giải phóng.
*   **Tools:**
    *   Node.js: `clinic.js`, Chrome DevTools.
    *   C#: `dotTrace`, `dotMemory`.

---

## 6. Action Plan: Setup như thế nào

1.  **Level 1 (Basic):** Cài **Winston/Serilog**. Log ra Console (JSON format). Dùng CloudWatch/Datadog để xem.
2.  **Level 2 (Standard):** Setup **Prometheus + Grafana** (via Docker Compose). Đo 4 Golden Signals.
3.  **Level 3 (Advanced):** Setup **OpenTelemetry** + **Jaeger** cho Distributed Tracing.

> **Tư duy:** "Không đo lường thì không cải thiện được." (Peter Drucker).
