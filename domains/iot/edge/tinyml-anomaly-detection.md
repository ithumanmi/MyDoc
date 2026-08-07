# TinyML on the Edge: Anomaly Detection

> [← IoT Roadmap](../README.md) | [Embedded foundations](../foundations/embedded-foundations.md)

## Ý tưởng
Thay vì gửi raw accelerometer 1 kHz lên cloud, MCU tính feature (RMS, peak) và/hoặc chạy model INT8 nhỏ để cờ “rung bất thường” → chỉ uplink event.

## Trade-offs
| Approach | Pros | Cons |
| --- | --- | --- |
| Threshold rules | Đơn giản, giải thích được | Dễ false alarm |
| TinyML classifier | Bắt pattern phức tạp | Dataset + quantize + RAM |
| Cloud inference | Model lớn | Bandwidth/latency/cost |

## Pipeline học
1. Thu thập 10–30 phút data “normal” + vài đoạn “fault”
2. Feature hoặc train small network (TFLite Micro / Edge Impulse)
3. Quantize INT8, đo arena size + latency trên board
4. Gate uplink: chỉ publish khi score > threshold
5. Cloud vẫn giữ raw mẫu khi debug (duty-cycle)

**Lab:** [lab-tinyml-keyword-or-anomaly](../labs/lab-tinyml-keyword-or-anomaly.md)

> **Last Updated:** August 2026
