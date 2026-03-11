---
title: "Prediction Markets"
description: "Polymarket, Azuro, on-chain betting infrastructure."
tags:
  - prediction-markets
  - polymarket
  - azuro
updated: 2026-03-11
---

# 📊 Prediction Markets & On-chain Betting

## 1. Platforms

- **Polymarket:** CLOB trên Polygon, USDC settlement.
- **Azuro Protocol:** liquidity layer cho betting apps.
- **Zeitgeist, Augur v2:** on-chain oracle resolution.

## 2. Design Components

- Market creation & resolution rules.
- Liquidity provisioning (LP shares, vAMM, AMM curves).
- Oracle disputes (UMA, Kleros, in-house committees).

## 3. Use Cases

- Event trading (politics, sports, crypto metrics).
- Insurance hedges.
- Advertising/engagement for media brands.

## 4. Checklist

- [ ] Jurisdictional compliance (KYC, geofencing).
- [ ] Oracle reliability + dispute bonds.
- [ ] Liquidity incentives vs profitability for LPs.
- [ ] UX: settlement time, payouts, limit orders.

## 🧪 Lab: Create & Resolve a Market

**Goal:** launch market trên testnet (Azuro sandbox hoặc Zeitgeist).

**Prerequisites:**
- Tooling: Azuro SDK/Zeitgeist CLI, Substrate/Polkadot.js wallet.
- Network: Azuro sandbox testnet hoặc Zeitgeist battery park.
- Skills: smart contract interaction, oracle resolution, dispute mechanics.

### Steps
1. Spin up local node/testnet wallet, deposit collateral, ghi lại txn hash.
2. Tạo market + mô tả chi tiết rule, resolution oracle, share schema cho users.
3. Provide liquidity + đo PnL sau khi kết thúc, export dữ liệu.
4. Thực hiện dispute flow nếu kết quả sai, test arbitration và resolution timeline.

**Metrics to Track:** TVL cung cấp, volume giao dịch, oracle resolution time, dispute outcomes.

**Deliverables:** market link, liquidity performance sheet, dispute transcript/kết quả cuối.

## 🧾 Case Study: Polymarket Election 2024

- **Context:** Polymarket trở thành nguồn dự báo chính xác cho bầu cử Mỹ 2024.
- **Key Metrics:** >$150M volume, hàng trăm nghìn users, phí giao dịch 2%.
- **Architecture Snapshot:** CLOB trên Polygon → USDC settlement → off-chain reporters + arbitration committee.
- **Key Insights:**
  - Cần compliance (CFTC scrutiny) → geofence + KYC cho user Mỹ.
  - Off-chain reporters + escrow multi-sig đảm bảo resolution, minimize disputes.
  - Liquidity mining theo sự kiện lớn boost TVL mạnh.
- **Risks & Mitigations:** regulatory action → geofencing + disclaimers; oracle manipulation → multiple reporters + bonded disputes.
- **Takeaway:** Thành công phụ thuộc vào trust của oracle + tuân thủ pháp lý song song với UX thân thiện.