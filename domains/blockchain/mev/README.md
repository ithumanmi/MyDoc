---
title: "MEV & PBS"
description: "Maximal Extractable Value, Flashbots, searcher workflow, proposer-builder separation."
tags:
  - mev
  - flashbots
  - ethereum
updated: 2026-03-11
---

# ⚡ MEV (Maximal Extractable Value)

> **Goal:** Hiểu pipeline MEV, giảm tác động xấu (front-run, sandwich) và tận dụng Flashbots/PBS.
> **Deliverables:** MEV mitigation plan, builder/searcher architecture, monitoring playbook.
> **Success Criteria:** Giảm slippage do sandwich, block production hợp lý, share MEV minh bạch.

## 1. Modules

- [MEV Fundamentals](mev-fundamentals.md)
- [Flashbots Protect & Private Mempools](flashbots-protect.md)
- [PBS & MEV-Boost](pbs-mev-boost.md)
- [MEV Strategies & Bots](mev-strategies.md)
- [MEV Searcher Lab](labs.md)
- [MEV Audit Exercises](mev-audit-exercises.md)

## 2. Flashbots Stack

| Attack | Mitigation |
| --- | --- |
| Sandwich | Use `MEV protection` RPC (Flashbots Protect, Eden), set `maxPriorityFee` low, use private mempool |
| Front-run | Submit via `eth_sendPrivateTransaction` |
| Liquidation Sniping | Increase gas to compete, or use keeper network |
| Censor | Multi-relay, fallback to local block builder |

### Relay/Builder Comparison

| Relay/Builder | Strengths | Limits |
| --- | --- | --- |
| **Flashbots** | Dominant market share, mev-share, Protect RPC | OFAC filtering (depending policy), reliance on single org |
| **Ultra Sound (Builder0x69)** | Open relay, high inclusion rate | Less tooling for retail |
| **bloXroute** | BDN acceleration, multiple tiers (Max, Ultra) | Paid subscription, config phức tạp |
| **Agnostic / Aestus** | Censorship-resistant stance | Smaller market share |
| **Manifold** | Vertical stack (relay+builder), fast adoption | Still centralized operator |

> Tip: Validators nên kết nối 3-4 relay để cân bằng performance và censorship resistance.

## 3. Searcher Workflow

1. **Data ingestion:** mempool, on-chain state.
2. **Simulation:** Tenderly, geth call, `hardhat_fork`.
3. **Bundle building:** specify `blockNumber`, `minTimestamp`, `bribe`.
4. **Submission:** send to Flashbots relay, track success.

## 4. Monitoring

- **Metrics:** MEV revenue per block, builder share, relay inclusion rate.
- **Alert:** spike sandwich activity, failing builder connection.
- **Tools:** mev-inspect, EigenPhi, Flashbots dashboard.

### Benchmarking Performance

- **KPIs:**
  - `avg_mev_reward`: trung bình MEV block reward/validator.
  - `relay_inclusion_rate`: % block accepted từ mỗi relay.
  - `bundle_success_rate`: % bundle được inclusion.
  - `latency_ms`: round-trip submit bundle → relay ack.
- **Method:**
  1. Collect logs từ `mev-boost` và searcher bot theo block height.
  2. Lưu vào time-series DB (Prometheus, InfluxDB).
  3. So sánh giữa relay/builder theo tuần.
- **Visualization:** Grafana dashboard hiển thị revenue trending, failure spike.
- **Action:** Khi relay latency tăng → rollback sang relay khác hoặc enable local builder.

> Xem thêm: [MEV Audit Exercises](mev-audit-exercises.md) để luyện tập kiểm tra cấu hình và benchmark.

## 5. Checklist

- [ ] Chọn relay/builder (Flashbots, bloXroute, Manifold) và cấu hình validator.
- [ ] Thiết kế protection RPC cho người dùng (private tx, slippage guard).
- [ ] Theo dõi MEV distribution và detect attack pattern.
- [ ] Cập nhật roadmap PBS/in-protocol, plan fallback khi relay down.
- [ ] Document searcher workflow (data, simulation, submission, monitoring).