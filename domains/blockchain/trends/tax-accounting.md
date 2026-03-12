---
title: "Crypto Tax & Accounting"
description: "Cost basis methods, DeFi tax nuances, tooling."
tags:
  - investing
  - tax
updated: 2026-03-11
---

# 🧾 Crypto Tax & Accounting

## 1. Core Concepts

- **Taxable events:** Sell, swap, spend, convert to fiat, staking rewards, airdrops.
- **Cost basis methods:** FIFO, LIFO, Specific ID; check local regulation (VN, US, EU). 
- **Holding period:** Short-term vs long-term capital gains.

## 2. DeFi Nuances

- Liquidity provision → treated as asset swap (deposit) + withdrawal events.
- Lending/borrowing: Interest income vs capital gains.
- Derivatives: Perps funding, options premium, liquidation events.
- Restaking / liquid staking: reward classification (income vs staking reward).

## 3. Tooling

- **CoinTracking, Koinly, TokenTax, Accointing:** import CEX + DeFi data.
- **Rotki (self-hosted)** để đảm bảo privacy.
- **Subgraph-based trackers:** DeBank export, Zerion CSV.

## 4. Workflow

1. Consolidate addresses, exchange accounts.
2. Sync data định kỳ (monthly) để tránh backlog.
3. Reconcile anomalies (missing prices, dust tokens).
4. Export reports (Form 8949, VAT statements) và lưu trữ chứng từ.

## 5. Compliance Tips

- Giữ record source of funds (KYC, fiat onramp receipts).
- Hiểu nghĩa vụ thuế địa phương (ví dụ: tạm thời VN chưa có khung, nhưng nên chuẩn bị khi luật hoá).
- Sử dụng stablecoin/T-bill sản phẩm để set aside tax liabilities.

## 6. Checklist

- [ ] Đánh dấu ví dành riêng cho hoạt động đầu tư vs cá nhân.
- [ ] Theo dõi reward token price tại thời điểm nhận.
- [ ] Lưu bản backup CSV/JSON mỗi quý.