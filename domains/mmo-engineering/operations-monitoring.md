# 📊 Operational Monitoring cho MMO Farm

> Xây dựng hệ thống giám sát farm account/proxy/phone theo thời gian thực để phát hiện account die, proxy lỗi, phone treo.

---

## 1. Telemetry Pipeline
- **Data Sources:**
  - Automation agent gửi heartbeat (status, account ID, proxy ID).
  - Device manager (ADB hub, 4G modem) report nhiệt độ, uptime.
  - Platform API (Facebook/TikTok) → webhooks khi checkpoint.
- **Collectors:**
  - MQTT/HTTP gateway nhận event từ client → push vào Kafka/Redis Stream.
  - Metric exporter (Prometheus node exporter, custom script) để track CPU/RAM/Network.

```
Agents → MQTT/Kafka → Stream Processor → Timeseries DB (Prometheus/Influx) → Dashboard (Grafana)
                     ↘ Alert Queue (PagerDuty/Telegram)
```

---

## 2. Dashboard Design
- **Grafana Panels:**
  - Account Health: % account đang online, checkpoint, ban.
  - Proxy Latency/Success Rate: RTT, error rate theo provider.
  - Phone Farm Status: nhiệt độ, FPS, battery (nếu dùng pin).
  - Task Throughput: số action/phút, queue backlog.
- **Heatmap:** account theo geo/proxy để thấy provider nào fail.
- **Annotations:** đánh dấu các sự kiện rollout script mới hoặc rotate SIM.

---

## 3. Alerting Playbook
- **Conditions:**
  - `Online accounts < 85%` trong 5 phút.
  - `Proxy error rate > 10%` hoặc latency vượt 2x baseline.
  - `Phone temperature > 50°C` liên tục 3 phút.
  - `Checkpoint burst > 20 account/10 phút`.
- **Channels:** Telegram bot, Slack, PagerDuty.
- **Action Runbook:**
  1. Auto-disable script/flow gây lỗi.
  2. Rotate proxy pool hoặc reset 4G modem.
  3. Trigger warm backup account.

---

## 4. Account Heartbeat Schema (JSON)
```json
{
  "account_id": "fb_123",
  "profile_id": "browser-42",
  "proxy_id": "res-nyc-01",
  "status": "active",
  "checkpoint": false,
  "last_action": "post_comment",
  "metrics": {
    "cpu_pct": 42,
    "mem_mb": 512,
    "network_rtt_ms": 230
  },
  "timestamp": "2026-03-12T10:45:00Z"
}
```

---

## 5. Tooling Stack
- **Metrics:** Prometheus + Grafana, hoặc InfluxDB + Chronograf.
- **Logs:** Loki/ELK để lưu automation logs/error screenshot.
- **Alert Engine:** Grafana Alerting, Kapacitor, hoặc custom Python gửi Telegram.
- **Device Control:** Ansible + ADB scripts để reboot phone, reload app.

---

## 6. Log Aggregation @1.000+ accounts
- Agent gửi log JSON → Fluent Bit/Vector.
- Pipeline: `Agent → Vector` (batch 1s) → `Kafka topic logs_farm` → sink ClickHouse/Loki.
- Partition theo `farm_id` + `day` để query nhanh.
- Alert nếu `ingestion_lag > 2 phút` hoặc volume giảm >30%.

## 7. Checklist
- [ ] Mỗi agent có heartbeat + retry logic.
- [ ] Dashboard hiển thị health theo tầng (account/proxy/device).
- [ ] Alert threshold định nghĩa rõ + runbook.
- [ ] Backup channel khi Telegram bot die.
- [ ] Lưu lịch sử ban/checkpoint để phân tích xu hướng.
- [ ] Log aggregator scale-out (Kafka partition, retention 30 ngày).