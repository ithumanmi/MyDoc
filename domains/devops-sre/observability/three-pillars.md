# Observability: Logs, Metrics, Traces

> [← DevOps & SRE](../README.md)

## Ba trụ
| Pillar | Trả lời câu hỏi | Stack phổ biến |
| --- | --- | --- |
| Metrics | Hệ thống có đang cháy SLO không? | Prometheus + Grafana |
| Logs | Event cụ thể nói gì? | Loki / ELK |
| Traces | Request đi qua service nào chậm? | Tempo / Jaeger / OTel |

## Quy tắc thực dụng
1. Metric trước (rẻ, alert được) → trace cho path quan trọng → log có structure + correlation id
2. High-cardinality labels (userId) sẽ giết Prometheus — dùng sparingly
3. RED/USE methods: Rate-Errors-Duration cho services; Utilization-Saturation-Errors cho resources

## Lab liên quan
[lab-k8s-observability.md](../labs/lab-k8s-observability.md)

> **Last Updated:** August 2026
