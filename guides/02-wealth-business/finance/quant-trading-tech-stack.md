---
title: "Quant Trading Tech Stack Deep Dive"
description: "Kiến trúc end-to-end cho hệ thống quant trading từ dữ liệu đến execution & security."
tags:
  - finance
  - quant
  - architecture
updated: 2026-03-10
---

# 🛠️ Quant Trading Tech Stack Deep Dive

> "Không có tech stack kỷ luật, mọi chiến lược alpha đều biến thành noise" – Quant Infra Principle

Tài liệu này đào sâu từng lớp của tech stack cho một quant desk: từ data ingestion, feature store, research/ML, execution engine đến hạ tầng, bảo mật và vận hành.

---

## 1. Kiến trúc tổng thể

```
Data Sources → ETL/Streaming → Lakehouse + Feature Store → Research/Backtest → Strategy Service → Order Router/Execution → Broker/Exchange
                                          ↓                                         ↓
                                     Risk Engine ← Metrics & Monitoring ← Logging/Audit
```

Các nguyên tắc chính:
1. **Decouple:** mỗi layer chạy độc lập qua message bus/API.
2. **Replayable:** dữ liệu và tín hiệu phải replay được để audit.
3. **Observable:** log/metrics/traces chuẩn hóa.

---

## 2. Data Layer

### 2.1 Source Catalog

| Type | Ví dụ | Lưu ý |
| --- | --- | --- |
| Market Data (Tick/Level2) | Polygon, dxFeed, Exegy | Yêu cầu low-latency, chuẩn FIX/ITCH |
| End-of-day/Corporate Actions | Quandl/Nasdaq, Refinitiv | Điều chỉnh split/dividend |
| Macro & Economic | FRED, TradingEconomics | Đồng bộ timezone, lịch phát hành |
| Alternative Data | RavenPack, Thinknum, TokenTerminal | Kiểm chứng độ tin cậy, latency |
| Internal Logs | Execution, order book snapshot | Phục vụ backtest/slippage modeling |

### 2.2 Ingestion Pipeline
- **Batch ETL:** Airbyte/Fivetran → S3 → dbt transform.
- **Streaming:** Kafka/Redpanda ingest tick data, sử dụng schema registry (Avro/ProtoBuf).
- **Quality:** Great Expectations, anomaly detection (Median absolute deviation).
- **Metadata:** Data catalog (Amundsen/OpenMetadata) để tracking schema/version.

### 2.3 Storage Strategy
- **Raw Zone:** S3/MinIO (Parquet, partition theo date/symbol).
- **Lakehouse:** Delta Lake hoặc Apache Iceberg cho ACID + time travel.
- **Analytical Store:** ClickHouse/Druid cho query nhanh.
- **Feature Store:** Feast, Tecton hoặc custom (Redis + Postgres) để cung cấp feature online/offline.

---

## 3. Research & ML Layer

### 3.1 Environment & Tooling
- Kubernetes + JupyterHub cho multi-user notebook.
- Dockerized environment; dùng Nix/Poetry lock dependency.
- MLflow hoặc Weights & Biases để track experiment.

### 3.2 Backtesting Engine
- **Requirement:** multi-asset, corporate actions, transaction cost, slippage, borrow fee.
- **Options:**
  - Backtrader/Zipline (open-source) + custom patches.
  - QuantConnect LEAN self-hosted.
  - In-house vectorized engine (Numba, C++).
- **Enhancements:**
  - Event-driven simulation (matching engine giả lập order book).
  - Walk-forward module, regime segmentation.

### 3.3 Feature & Model Pipeline
- **Feature Engineering:** pandas, dask, Featuretools; use rolling windows, wavelet transform.
- **Modeling:**
  - Factor models (cross-sectional ranking).
  - ML models: XGBoost, CatBoost, LightGBM, Transformers (TSMixer, TFT), RL (FinRL).
  - Ensemble & stacking.
- **Validation:**
  - Time-series CV, purged k-fold.
  - Backtest vs live (shadow mode) để kiểm chứng drift.

---

## 4. Strategy & Execution Layer

### 4.1 Strategy Service
- Microservice nhận dữ liệu từ feature store → tạo tín hiệu.
- Viết bằng Python/FastAPI hoặc Go.
- Output: order intent (symbol, size, direction, urgency, confidence).

### 4.2 Order Router & Execution Engine
- **Order Router:**
  - Ánh xạ chiến lược → tài khoản → broker.
  - Áp dụng risk limit (max position, daily loss).
  - Message bus (Kafka) hoặc gRPC để truyền order.
- **Execution Engine:**
  - Viết bằng Go/C++/Rust; hỗ trợ TWAP/VWAP, POV, iceberg, sniper.
  - Smart Order Routing: chọn venue theo liquidity/fee.
  - Simulation mode để test.
- **Connectivity:**
  - FIX 4.4/5.0, REST, WebSocket.
  - Co-location khi HFT.

### 4.3 Risk & Position Management
- Real-time PnL, Greeks, VaR.
- Kill-switch tự động khi vượt guardrail.
- Position server (Redis/Postgres) để đồng bộ holdings.

---

## 5. Infrastructure, Monitoring & Security

### 5.1 Infrastructure
- Cloud hybrid: AWS/GCP + on-prem colo.
- Container orchestration: Kubernetes (EKS/GKE); autoscaling node pools.
- IaC: Terraform + Helm; cấu hình bằng GitOps (ArgoCD).

### 5.2 Observability
- **Metrics:** Prometheus + Grafana; dashboards cho latency, fill ratio, CPU/memory.
- **Logs:** ELK (Elasticsearch, Logstash, Kibana) hoặc OpenSearch.
- **Tracing:** OpenTelemetry + Jaeger.
- **Alerting:** PagerDuty/Slack/Teams.

### 5.3 Security & Compliance
- Secrets: HashiCorp Vault, AWS Secrets Manager.
- Access: SSO + RBAC + MFA; audit log mọi hành động.
- Data encryption: at-rest (KMS) và in-transit (mTLS).
- Compliance: lưu trữ log 5-7 năm, backup geo-redundant.
- Pen-test định kỳ, tabletop exercise cho cyber incident.

---

## 6. Cost & Scaling Considerations

| Component | Starter Setup | Scale-up Notes |
| --- | --- | --- |
| Data | $2-5k/tháng (API + storage) | Alt data có thể $10-50k/tháng, cần ROI review |
| Compute | $1-3k/tháng (cloud spot) | Tối ưu bằng autoscaling, reserved instances |
| Execution | Broker fees + infra ~$2k/tháng | HFT cần co-location đắt (>$10k/tháng) |
| Monitoring/Security | $500-$1k/tháng | Enterprise SIEM có thể >$3k/tháng |

> Khuyến nghị: lập budget theo 3 mảng (Data, Compute, Ops) và review hàng quý.

---

## 7. Implementation Roadmap (90-180 ngày)

1. **Month 0-1:** Thiết kế kiến trúc, chọn vendor, thiết lập IaC.
2. **Month 1-2:** Xây data lake + ETL cơ bản, dựng Jupyter + backtest engine.
3. **Month 2-3:** Triển khai feature store, build strategy service mẫu, shadow execution.
4. **Month 3-4:** Productionize execution engine + risk dashboard, thiết lập observability.
5. **Month 4-6:** Tối ưu security (secrets, IAM), stress test, review cost, chuẩn hóa SOP.

---

## 8. Checklist đánh giá Tech Stack
- [ ] Data pipeline có versioning, chất lượng kiểm soát tự động.
- [ ] Feature store hỗ trợ online/offline parity.
- [ ] Backtest engine cover transaction cost, borrow fee, corporate actions.
- [ ] Strategy service decouple với execution, có replay tín hiệu.
- [ ] Execution engine có failover, retry, circuit breaker.
- [ ] Monitoring gồm metrics/logs/traces + alert on-call.
- [ ] Secrets quản lý tập trung, access theo principle of least privilege.
- [ ] Documentation đầy đủ: kiến trúc, SOP, runbook.

> **Thông điệp cuối:** Tech stack của một quant desk phải được thiết kế như sản phẩm mission-critical – ưu tiên tính tin cậy, khả năng kiểm soát và khả năng mở rộng trước khi nghĩ đến tốc độ.