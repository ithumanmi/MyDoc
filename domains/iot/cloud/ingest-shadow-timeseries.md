# Cloud Ingest, Device Shadow & Timeseries

> [← IoT Roadmap](../README.md) | [Home](../../../README.md)
>
> **Level:** 🟡 Intermediate

## Pipeline chuẩn
```
Device --MQTT QoS1--> Broker (EMQX/IoT Core)
                  --> Kafka/Kinesis
                  --> Timeseries DB
                  --> Grafana / Alertmanager
```

## Device Shadow / Digital Twin
- **Reported:** thiết bị khai báo trạng thái thật (relay=on, fw=1.4.2)
- **Desired:** cloud muốn thiết bị đạt tới
- Device reconcile desired→reported; UI không “đoán” trạng thái từ lệnh đã gửi

## Timeseries schema tối thiểu
```sql
CREATE TABLE readings (
  device_id text,
  ts timestamptz NOT NULL,
  temp double precision,
  hum double precision,
  battery double precision,
  PRIMARY KEY (device_id, ts)
);
SELECT create_hypertable('readings', 'ts');
SELECT add_retention_policy('readings', INTERVAL '90 days');
```

## Alert rules nên có từ ngày 1
| Alert | Điều kiện | Ý nghĩa |
| --- | --- | --- |
| Offline | No data 5 phút | Mất điện / mất mạng / brick |
| Battery low | `< 20%` | Kế hoạch thay pin |
| Over-threshold | Temp vượt ngưỡng N mẫu liên tiếp | Process/anomaly |
| Ingest lag | p95 publish→DB > SLO | Connector/Kafka chậm |

## SLO gợi ý (fleet vừa)
- Ingest latency p95 < 2s
- Packet loss < 0.1% (sau reconnect buffer)
- OTA success rate > 97% mỗi wave

**Practice:** [Lab cloud ingest + Grafana](../labs/lab-cloud-ingest-grafana.md) · [Case: Smart Factory](../case-studies/smart-factory-floor.md)

> **Last Updated:** August 2026
