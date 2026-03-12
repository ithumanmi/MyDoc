# ☁️ Lab: Google Chronicle Detection Engineering

> Mục tiêu: ingest log từ GCP/AWS hoặc syslog, viết YARA-L ถrule và UDM search phát hiện credential stuffing & DNS tunneling.

---

## 1. Chronicle Primer
- Chronicle là SIEM/Security Analytics của Google, ingest log từ cloud + on-prem.
- Dữ liệu chuyển về qua **Forwarder** (Linux appliance) hoặc native connector.
- Hỗ trợ **YARA-L** (YARA for Logs) để viết detection cấu trúc.

### **Prerequisites**
- Chronicle sandbox hoặc tài khoản partner.
- 1 server syslog forwarding (Ubuntu) + AWS CloudTrail sample.

---

## 2. Ingest Syslog & CloudTrail

### **Syslog via Forwarder**
1. Cài Chronicle Forwarder: tải `.deb` từ console.
2. Config `/etc/chronicle/forwarder/forwarder.conf`
```yaml
input:
  - type: syslog
    listen_address: 0.0.0.0
    port: 514
output:
  - type: google
    customer_id: YOUR_ID
    credentials_file: /etc/chronicle/credentials.json
```
3. Forward log Linux auth: `*.* @<forwarder_ip>:514`

### **CloudTrail**
- Dùng `Cloud Storage bucket` + `Pub/Sub` pipeline.
- Trong Chronicle Data Ingestion → bật AWS CloudTrail connector, nhập ARN role.

---

## 3. YARA-L Rule: Credential Stuffing

```yaml
rule credential_stuffing_high_volume {
  meta:
    author = "blue_team"
    description = "Detect multiple login failures from same IP"
  events:
    $failed_login.event_type = "AUTHENTICATION_FAILURE"
    $failed_login.metadata.product_name = "linux"
    $failed_login.src_ip = $src
    $failed_login.count() >= 30 within 5 minutes
}
```

Deploy via Chronicle → Detection → Rules → New rule.

---

## 4. UDM Search: DNS Tunneling

```sql
FETCH threat FROM dns_lookup
  WHERE metadata.vendor_name = "bind"
    AND target.domain matches ".*\\.xyz" 
    AND udf.length(target.domain) > 50
  WINDOW 5 MINUTES
  GROUP BY target.domain, src.ip
```

> Tip: Dùng built-in hunting queries: `Suspicious DNS queries` và custom dimension.

### **Verification**
- Sinh traffic `iodine` (DNS tunnel) hoặc `dnscat2` từ lab VM.
- Quan sát detection firing + timeline.

---

## 5. Case Management
- Khi rule trigger → Incident trong Chronicle.
- Add context: WHOIS, VirusTotal.
- Export detection thành Chronicle SOAR hoặc gửi Slack webhook.

---

> ✅ Hoàn thành khi bạn có ít nhất 1 YARA-L rule chạy, 1 UDM hunt query bookmark, và log mẫu (hydra/dnscat) tạo alert.

---

# ☁️ Chronicle Advanced Lab: BigQuery + Looker Exploration

> Mục tiêu: xuất log từ Chronicle sang BigQuery để chạy query tuỳ biến, sau đó tạo dashboard Looker Studio cho leadership (failed login, DNS beacon heatmap).

## 1. Export Pipeline
- Trong Chronicle → `Data Flow` → bật **Forward to BigQuery**.
- Chỉ định project, dataset, table (VD: `chronicle_logs.security_events`).
- Kiểm tra job status trong Cloud Logging.

## 2. BigQuery SQL Samples

### **High-volume Authentication Failures**
```sql
SELECT
  metadata.event_timestamp,
  principal.email,
  target.hostname,
  COUNT(*) AS fail_count
FROM `chronicle_logs.security_events`
WHERE event.type = "AUTHENTICATION_FAILURE"
GROUP BY 1,2,3
HAVING fail_count > 50
ORDER BY fail_count DESC
```

### **DNS Beacon Clustering**
```sql
WITH dns AS (
  SELECT
    metadata.event_timestamp,
    network.src.ip AS src_ip,
    target.domain,
    LENGTH(target.domain) AS len
  FROM `chronicle_logs.dns_lookup`
)
SELECT src_ip, COUNT(*) cnt
FROM dns
WHERE len > 45
GROUP BY src_ip
HAVING cnt > 100
```

## 3. Looker Studio Dashboard
1. Tạo datasource → `BigQuery` → chọn dataset `chronicle_logs`.
2. Visualization đề xuất:
   - Combo chart: Failed logins theo user/time.
   - Geo map: nguồn DNS beacon theo region.
   - Scorecard: số YARA-L alert tuần này.
3. Chia sẻ dashboard cho SOC lead (view-only).

## 4. Automation
- Dùng **BigQuery scheduled query** → export CSV vào GCS, sau đó `Cloud Functions` gửi báo cáo email.

> ✅ Hoàn thành khi bạn có dashboard Looker hiển thị metrics từ Chronicle BigQuery export và scheduled query chạy định kỳ.

---

## 🤖 BigQuery ML Anomaly Detection Add-on

### 1. Dataset chuẩn bị
- Bảng `chronicle_logs.security_events` đã có các cột `event_timestamp`, `principal.email`, `geo.src_country`.
- Tạo view aggregate theo user/time:
```sql
CREATE OR REPLACE TABLE chronicle_logs.auth_hourly AS
SELECT
  TIMESTAMP_TRUNC(metadata.event_timestamp, HOUR) AS hour_bucket,
  principal.email,
  COUNTIF(event.type = "AUTHENTICATION_FAILURE") AS fail_count,
  APPROX_COUNT_DISTINCT(target.hostname) AS host_count
FROM `chronicle_logs.security_events`
GROUP BY 1,2;
```

### 2. Train BigQuery ML Model
- Sử dụng `ML.DETECT_ANOMALIES` với model ARIMA_PLUS_XREG.
```sql
CREATE OR REPLACE MODEL chronicle_logs.auth_anomaly
OPTIONS(MODEL_TYPE='ARIMA_PLUS_XREG', TIME_SERIES_TIMESTAMP_COL='hour_bucket', TIME_SERIES_ID_COL='principal.email') AS
SELECT hour_bucket, principal.email, fail_count, host_count
FROM `chronicle_logs.auth_hourly`;
```

### 3. Chạy Detection & Export
```sql
CREATE OR REPLACE TABLE chronicle_logs.auth_anomaly_scored AS
SELECT * FROM ML.DETECT_ANOMALIES(
  MODEL chronicle_logs.auth_anomaly,
  STRUCT(0.95 AS anomaly_prob_threshold)
);
```
- Export kết quả (anomaly = TRUE) về Chronicle hoặc Looker.

### 4. Automation
- Dùng Cloud Scheduler → BigQuery job → Cloud Function gọi Chronicle API tạo case khi anomaly.

> ✅ Hoàn thành khi có model ML chạy theo lịch và log anomaly được phản hồi (alert/dashboard).
