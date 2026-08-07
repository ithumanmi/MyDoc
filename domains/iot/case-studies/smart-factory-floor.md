# Case Study: Smart Factory Floor

> [← IoT Roadmap](../README.md) | [Home](../../../README.md)
>
> **Level:** 🟡 Intermediate

## Bối cảnh
500 thiết bị STM32/ESP32 đo nhiệt/độ ẩm/rung tại 5 xưởng. Yêu cầu: alert quá nhiệt, offline, pin yếu; C2 quạt; OTA an toàn; SLO ingest < 2s, mất gói < 0.1%.

## Kiến trúc
```
Devices --MQTT QoS1--> EMQX --bridge--> Kafka (iot.sensors)
Kafka Connect JDBC --> TimescaleDB --> Grafana/Alert
Operator API --> cmd/{deviceId}
ack/{deviceId} --> UI
OTA HTTPS (signed) + status callbacks
```

## Topic map
- Telemetry: `devices/{deviceId}/telemetry`
- Shadow: `devices/{deviceId}/state`, `desired/{deviceId}`
- Command / Ack: `cmd/{deviceId}`, `ack/{deviceId}`
- OTA: `ota/{deviceId}/status`

## Incident playbook (rút gọn)
1. **MQTT backlog:** giảm QoS thừa, scale Kafka partition, rate-limit device chatty  
2. **Offline hàng loạt:** check power/RSSI; bật local buffer + resend  
3. **C2 lặp:** idempotency key + TTL + ACL  
4. **Latency >2s:** đo từng hop EMQX→Kafka→DB; tăng connector parallelism  
5. **OTA brick:** dual-partition rollback; abort wave nếu error >3%

## Deliverable tự học
- [ ] Vẽ topology + topic ACL
- [ ] Viết 4 alert rule trong Grafana
- [ ] Mô tả staged OTA 5%→20%→100%
- [ ] So sánh với [Cold Chain](../README.md) / Smart Home trong roadmap gốc

**Related:** [Cloud ingest](../cloud/ingest-shadow-timeseries.md) · [Security & OTA](../security/device-security-ota.md)

> **Last Updated:** August 2026
