# Kafka for Data Engineers

> [← Data Science](../README.md)

## Khái niệm lõi
- Topic / partition / offset
- Consumer group
- At-least-once vs exactly-once (hiểu trade-off, đừng thần thánh hóa EOS)

## Pattern phổ biến
| Pattern | Dùng cho |
| --- | --- |
| Pub/sub log | Decouple producer/consumer |
| CDC → Kafka | Sync DB → lake |
| Stream enrich | Join dimension nhỏ trên stream |

## Thực hành an toàn
- Key = entity id để giữ ordering trong partition
- Monitor lag consumer
- Schema registry / contract cho payload

**Lab liên quan:** pipeline tư duy trong [Airflow ETL lab](../labs/lab-airflow-etl-pipeline.md)

> **Last Updated:** August 2026
