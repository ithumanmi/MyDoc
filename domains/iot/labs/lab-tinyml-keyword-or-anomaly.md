# Lab: TinyML Keyword or Anomaly (ESP32-class)

> [← Labs](./README.md) | [TinyML guide](../edge/tinyml-anomaly-detection.md)

## Mục tiêu
Chạy 1 model INT8 on-device (keyword spotting **hoặc** vibration anomaly) với latency đo được và deep sleep giữa các lần infer (nếu pin).

## Options (chọn 1)
**A. Keyword:** “yes/no” hoặc wake-word demo TFLite Micro  
**B. Anomaly:** threshold/autoencoder nhỏ trên feature RMS

## Acceptance
- [ ] Infer on-device (không gửi audio/raw stream liên tục)
- [ ] Log latency p50/p95 trên serial
- [ ] Khi detect → MQTT event `devices/{id}/events` QoS1
- [ ] Ghi RAM/flash footprint trong README
- [ ] Fallback: nút physical vẫn trigger event (fail-safe)

## Tips
- Bắt đầu Edge Impulse / official TFLite Micro examples trước khi tự train
- Giữ model < ngân sách arena của board

> **Last Updated:** August 2026
