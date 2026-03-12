---
title: "On-chain Analysis Guide"
description: "Dune dashboards, Nansen labels, whale tracking tactics."
tags:
  - investing
  - analytics
updated: 2026-03-11
---

# 🧠 On-chain Analysis Guide

## 1. Tooling Stack

- **Dune Analytics:** SQL dashboarding cho Ethereum + L2/L3, dùng forking query để tùy chỉnh.
- **Nansen:** Labeled wallets (Smart Money, Fund, CEX), alerts, token god mode.
- **Arkham, Breadcrumbs:** Graph analysis cho luồng tiền.

## 2. Signals & Metrics

- **Exchange inflow/outflow:** theo dõi whales deposit lên CEX → bán.
- **Stablecoin flows:** đo sentiment (mint/redeem USDC, USDT, FDUSD).
- **Liquidity movements:** TVL shifts (DefiLlama), pool depth thay đổi.
- **Developer activity:** GitHub commits, contract deployments (Token Terminal, Artemis).

## 3. Whale Tracking Playbook

1. Thiết lập danh sách địa chỉ trọng yếu (funds, project treasuries, insiders) từ Nansen labels.
2. Sử dụng Dune / Arkham alerts để push notification khi địa chỉ tương tác.
3. Đối chiếu luồng funds với lịch unlock/token vesting.
4. Backtest phản ứng giá sau khi theo dõi whale move để xác định độ tin cậy.

## 4. Alerting & Automation

- **nansen.ai alerts**, **Dune alerts**, **EigenPhi** cho MEV + sandwich detection.
- Webhook vào Slack/Telegram, integrate với Notion database.

## 5. Checklist

- [ ] Xác thực dữ liệu (đôi khi labels sai hoặc chậm cập nhật).
- [ ] Tránh overfit: so sánh signal on-chain với macro/CEX data.
- [ ] Thiết lập SOP khi nhận alert (verify, size trade, risk). 