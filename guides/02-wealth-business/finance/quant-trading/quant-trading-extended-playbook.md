---
title: "Quant Trading Extended Playbook"
description: "Triển khai chi tiết tech stack, chiến lược, operating model, case study và checklist đào tạo cho quant desk."
tags:
  - finance
  - quant
  - trading
updated: 2026-03-10
---

# 🚀 Quant Trading Extended Playbook

> "Edge = Data + Process + People. Bỏ sót một biến, toàn bộ hệ thống sẽ gãy." – Quant Operating Creed

Tài liệu này mở rộng các nội dung trọng tâm cho việc xây dựng và vận hành một quant desk: Tech Stack chi tiết, chiến lược StatArb/CTA/Options, Operating Model & nhân sự, case study sâu, cùng checklist đào tạo.

---

## 1. Tech Stack chi tiết (Data → Engine → Execution)

### 1.1 Data Ingestion & Processing
- **Market Data:**
  - Vendor: Polygon.io, Intrinio, Bloomberg B-PIPE, Refinitiv.
  - Transport: WebSocket streaming (real-time), batch S3 parquet.
  - Storage: S3 + Lakehouse (Delta/Apache Iceberg) + ClickHouse cho query nhanh.
- **Alt Data:**
  - Sources: RavenPack (news), SpaceKnow (satellite), TokenTerminal (on-chain), Credit-card aggregators.
  - Pipeline: ETL bằng Airbyte/Fivetran → dbt transform → feature store (Feast).
- **Quality Control:**
  - Auto anomaly detection (Great Expectations), duplicate check, timezone normalization.

### 1.2 Research & Modeling Engine
- **Environment:**
  - JupyterLab + VSCode remote container.
  - Conda/Poetry quản lý package.
- **Backtest Framework:**
  - Custom engine (vectorized) hoặc open-source: Backtrader, Zipline, QuantConnect LEAN.
  - Requirement: hỗ trợ multi-asset, corporate actions, transaction cost modeling.
- **ML Stack:**
  - Feature pipeline: pandas + Featuretools + MLflow tracking.
  - Models: XGBoost/CatBoost, Temporal Fusion Transformer, Prophet (macro), reinforcement learning (FinRL).
- **Simulation:**
  - Monte Carlo scenario, bootstrapping, block bootstrap theo regime.

### 1.3 Execution & Infrastructure
- **Architecture:**
  - Microservices: signal service → order router → execution engine → risk monitor.
  - Message bus (Kafka/Redpanda) để đảm bảo decoupling.
- **Execution Engine:**
  - Viết bằng Go/C++/Rust để tối ưu latency.
  - Smart Order Routing: chia order theo venue, TWAP/VWAP implementation.
- **Broker/Exchange Integration:**
  - Interactive Brokers, Tradestation, Alpaca, Crypto venues (Binance, Deribit) qua FIX/REST/WebSocket.
- **Deployment:**
  - Kubernetes/EKS hoặc bare metal + Nomad. Canary release cho chiến lược mới.
- **Monitoring:**
  - Prometheus + Grafana dashboard cho latency, fill ratio, reject rate.
  - Alert via PagerDuty/Slack khi error > threshold.

> **Tip:** Dù scale nhỏ, nên chuẩn hóa logging (JSON structured log) để dễ audit.

---

## 2. Deep Dive Chiến lược

### 2.1 Statistical Arbitrage
- **Core Idea:** Mean reversion giữa các tài sản có quan hệ thống kê.
- **Pipeline:**
  1. Universe selection (liquidity filter, sector grouping).
  2. Cointegration test (Johansen), rolling z-score, Kalman filter dynamic hedge ratio.
  3. Signal generation: spread > kσ ⇒ short spread, < -kσ ⇒ long spread.
  4. Risk overlay: stop khi regime change (ADF test > threshold), limit per pair.
- **Key Metrics:** Half-life, hit rate, time-in-trade, slippage impact.

### 2.2 CTA / Trend Following
- **Markets:** Futures (commodities, rates, indices), FX, crypto perpetual.
- **Signal:**
  - Breakout (Donchian 55-day), moving average crossover (50/200), volatility-adjusted momentum.
- **Risk:** Volatility scaling (target 15% annualized), dynamic position size theo ATR.
- **Execution:** Use synthetic orders (stop-limit) để tránh false breakout.
- **Stress Test:** Check performance trên các regime (inflation spike, policy shift).

### 2.3 Options Volatility Strategies
- **Playbooks:**
  - Long/short volatility (straddle/strangle) dựa trên implied vs realized spread.
  - Dispersion trade: short index vol, long constituent vol.
  - Skew arbitrage: khai thác skew giữa maturities hoặc strikes.
- **Modeling:**
  - Construct vol surface, SABR/Heston calibration.
  - Greeks management (Delta, Gamma, Vega neutrality).
- **Risk:**
  - Liquidity risk (wide spreads), gap risk, margin calls.
  - Use scenario Greeks (shock ±2σ) và pre-trade margin simulation.

---

## 3. Operating Model & Nhân sự

### 3.1 Team Structure (10 người)
| Role | Số lượng | Trách nhiệm |
| --- | --- | --- |
| Head of Quant | 1 | Định hướng chiến lược, quản lý risk, investor relations |
| Quant Researcher | 3 | Alpha research, backtest, ML |
| Quant Developer | 2 | Build platform, data, execution engine |
| Data Engineer | 1 | Ingestion pipeline, feature store |
| Risk & Compliance | 1 | Daily risk report, audit, regulatory |
| DevOps/SRE | 1 | Infra, monitoring, deployment |
| Operations Analyst | 1 | PnL reconciliation, broker liaison |

### 3.2 Operating Rhythm
- **Daily:** Morning risk stand-up, market brief, end-of-day PnL 6 risk report.
- **Weekly:** Strategy review, research demo, incident review.
- **Monthly:** Investor update, infra maintenance, stress test simulation.
- **Quarterly:** Portfolio rebalance, vendor evaluation, audit checklist.

### 3.3 SOP highlights
- **Change Management:** PR → code review → staged deploy → monitoring post-release.
- **Incident Response:** Severity levels, on-call rotation, post-mortem template.
- **Compliance:** Trade logs lưu 5+ năm, kiểm tra short locate, wash trade prevention.

---

## 4. Case Study – DeltaWave Quant Fund

- **Context:** Fund mini 50M USD, multi-strategy (StatArb equities, CTA macro, Options vol). Team 12 người.
- **Process:**
  1. Data platform trên AWS Lake Formation, ETL bằng Airflow, feature store Feast.
  2. Research dùng Qlib + custom risk model, backtest distributed trên Ray.
  3. Execution engine Go, kết nối FIX tới broker, latency ~3ms.
  4. Risk team dùng Kubernetes CronJob chạy stress test (2008, 2020, flash crash) hàng tuần.
- **Performance (2024-2025):** CAGR 21%, Sharpe 1.9, Max DD 8.5%, Correlation S&P 0.15.
- **Lessons Learned:**
  - Overfit guardrail: yêu cầu minimum 3 regime test trước deploy.
  - Alt data ROI: chỉ 2/7 dataset mang lại alpha → cần framework evaluate vendor.
  - Talent: cross-training giữa researcher và developer giúp giảm bottleneck khi on-call.

---

## 5. Checklist đào tạo & đánh giá thành viên

### 5.1 Onboarding (30-60 ngày)
- [ ] Understand architecture: data → backtest → execution → risk.
- [ ] Học quy trình code review, runbook, incident response.
- [ ] Rebuild ít nhất 1 chiến lược cũ để hiểu pipeline end-to-end.
- [ ] Viết research note + demo kết quả cho team.

### 5.2 Technical Competency Matrix

| Skill | L1 (Associate) | L2 (Senior) | L3 (Lead) |
| --- | --- | --- | --- |
| Statistical Modeling | Hiểu ADF, cointegration | Thiết kế factor mới | Định nghĩa risk model đa thị trường |
| Programming | Python thành thạo, biết unit test | Tối ưu code, parallel computing | Thiết kế framework, code review chuẩn |
| Execution Systems | Biết gọi API broker | Build module routing đơn giản | Kiến trúc OMS/EMS, tối ưu latency |
| Risk Management | Biết đọc Sharpe, drawdown | Thiết kế guardrail chiến lược | Xây risk policy, scenario planning |
| Communication | Viết note rõ ràng | Điều phối cross-team | Giao tiếp với investor, regulator |

### 5.3 Evaluation Cycle
- **Quarterly:** 360 feedback, review KPI (research impact, stability, collaboration).
- **Metrics:** Số lượng strategy shipped, chất lượng post-mortem, thời gian xử lý incident.

---

## 6. Action Items để mở rộng đội quant

1. Audit hiện trạng tech stack: xác định gap ở data, research, execution.
2. Xây hiring plan dựa trên Operating Model (ưu tiên data + quant dev).
3. Chuẩn hóa playbook đào tạo (Onboarding, runbook, checklist).
4. Thiết lập performance dashboard (strategy metrics + ops metrics).
5. Định kỳ cập nhật case study nội bộ: lessons learned, ROI của từng chiến lược.

> **Thông điệp cuối:** Mở rộng Quant Trading không chỉ là thêm chiến lược – đó là quá trình đồng bộ hóa con người, quy trình và công nghệ để bảo toàn edge trong môi trường biến động.