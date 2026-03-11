---
title: "Staking & Restaking"
description: "Native PoS, liquid staking, EigenLayer restaking và risk management."
tags:
  - staking
  - ethereum
  - restaking
updated: 2026-03-11
---

# 🪙 Staking Playbook

> **Goal:** Hiểu cơ chế staking native, tối ưu thanh khoản bằng liquid staking, đánh giá restaking và kiểm soát rủi ro slashing.
> **Deliverables:** Validator setup guide, liquid staking comparison, EigenLayer AVS checklist, risk matrix.
> **Success Criteria:** Phân bổ staking hợp lý (native vs liquid vs restaking), vận hành validator an toàn, nhận diện rủi ro kịp thời.

## Modules

- [PoS Staking Mechanics](pos-staking.md)
- [Liquid Staking Ecosystem](liquid-staking.md)
- [Restaking & EigenLayer](restaking-eigenlayer.md)
- [Staking Risks & Penalties](staking-risks.md)
- [Staking Lab](labs.md)

## Quick Navigator

| Topic | Nội dung chính |
| --- | --- |
| Native Validator | Hardware, client, reward, monitoring |
| Liquid Staking | Lido, Rocket Pool, LSTfi use-case |
| Restaking | EigenLayer operator flow, AVS integration |
| Risk | Slashing, correlation, governance attack |

## APR Benchmarking

- **Metrics:** native staking APR, LST APR (stETH, rETH), restaking reward (EigenLayer points/AVS token).
- **Data Sources:** Beaconcha.in API (`/validator/{index}`), protocol subgraphs, Dune dashboards.
- **Script Outline:**
  ```python
  import requests, pandas as pd
  data = requests.get("https://beaconcha.in/api/v1/validator/INDEX/performance").json()
  apr = data["data"]["apr"]
  ```
- **Storage:** append to CSV/TSDB daily; columns: date, apr_native, apr_steth, apr_reth, apr_restaking.
- **Visualization:** Grafana/Observable plot multi-line trend, highlight events (withdrawals enabled, fee change).
- **Action:** khi APR < threshold → rebalance (switch operator, move to liquid staking).

## Checklist

- [ ] Đánh giá mục tiêu (yield, decentralization, liquidity).
- [ ] Quyết định tỷ lệ native staking vs liquid staking.
- [ ] Nếu restaking: chọn AVS, đánh giá reward vs risk.
- [ ] Triển khai monitoring & alert (uptime, slashing signals).
- [ ] Chuẩn hóa runbook khi validator gặp sự cố.