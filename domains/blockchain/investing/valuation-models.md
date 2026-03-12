---
title: "Crypto Valuation Models"
description: "Toolkit: DCF-like flows, network multiples, token-specific metrics."
tags:
  - investing
  - valuation
updated: 2026-03-12
---

# 📐 Crypto Valuation Models

## 1. Narrative vs Numbers

- Token price = Function (Cash flow, Utility, Scarcity, Narrative premium).
- Dù crypto khó định giá tuyệt đối, vẫn cần khung để tránh FOMO.

## 2. Cash-Flow Based (Pseudo DCF)

- Áp dụng với protocol có **real yield** (GMX, Maker, EigenLayer restaking) hoặc token có revenue share.
- Steps:
  1. Ước tính **Protocol Revenue** (fees, MEV share, service fees).
  2. Xác định **take rate cho token holder** (buyback/burn, staking reward, fee rebate).
  3. Xây dựng kịch bản Base / Bull / Bear cho 3-5 năm.
  4. Chiết khấu với rate cao (20-40%) vì rủi ro.
- Output: **Implied Token Value** = PV of distributed cash flow / circulating supply.

## 3. Usage Multiples

- **P/S (Price-to-Sales)**: Market Cap / Annualized Revenue (e.g., Uniswap, Lido).
- **TVL Multiples:** FDV / TVL (DeFi), useful để so sánh hệ cùng narrative.
- **Users / Transactions:** Market Cap / MAU, Market Cap / Tx count (L2, Social).
- **Benchmarks:**
  - DeFi bluechip P/S 5-15x
  - L2 FDV/TVL 1-3x
  - CEX-like infra 10-20x earnings

## 4. Network & Utility Metrics

- **Metcalfe variants:** Value ∝ N^2, so track Active addresses, daily tx.
- **Monetary premium models:** Stock-to-flow (BTC), scarcity adjusted metrics.
- **NVT / NVTS:** Network Value / Tx Volume (daily). High NVT → overvalued vs usage.

## 5. Token-specific Considerations

- **Supply Schedule:** Unlocks, staking emissions, burn schedule.
- **Velocity:** High turnover reduces utility of holding (payment tokens).
- **Governance power:** Value depends vào treasury size, protocol control.
- **Real yield vs inflation:** Check net reward (APR – emissions).

## 6. Practical Workflow

1. **Data sources:** Token Terminal, DefiLlama Revenues, Messari, project transparency report.
2. **Model sheet:** Google Sheet/Notion + scenario toggles (volumes, fees, take rate).
3. **Sensitivity analysis:** ΔRevenue, ΔTake Rate, ΔEmission.
4. **Comparables deck:** Build table so sánh multiples vs peers.

## 7. Case Snapshots

- **GMX:** Revenue share 30% to stakers → pseudo dividend; model fees per open interest.
- **EigenLayer restaking token (future):** Value driver = AVS payments * take rate.
- **Base/OP tokens:** Sequencer revenue share; track net margin after L1 data cost.

## 8. Checklist

- [ ] Có dữ liệu doanh thu minh bạch? Nếu không -> speculative only.
- [ ] Tính đến token unlock + dilution trong model.
- [ ] Compare nhiều mô hình (DCF + multiples) để tránh biased.