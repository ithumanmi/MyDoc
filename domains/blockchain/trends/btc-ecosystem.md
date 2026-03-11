---
title: "Bitcoin Ecosystem"
description: "Ordinals, BRC-20, BitVM, emerging Bitcoin L2s."
tags:
  - bitcoin
  - ordinals
  - l2
updated: 2026-03-11
---

# ₿ Bitcoin Ecosystem (2024-2026)

## 1. Ordinals & BRC-20

- Inscribing arbitrary data onto sats.
- BRC-20 fungible tokens via inscriptions.
- Impact: blockspace demand, fee spikes.

## 2. BitVM & Smart Contracts

- Off-chain computation + on-chain fraud proofs.
- Enables more expressive logic without soft-fork.

## 3. Bitcoin L2 Landscape

- **Stacks sBTC:** peg-in, smart contracts (Clarity).
- **Liquid, Rootstock:** federated/merge-mined sidechains.
- **Rollkit on Bitcoin DA, Botanix Spiderchain.**

## 4. Checklist

- [ ] Understand trust assumptions (federated, zk, fraud proofs).
- [ ] Peg-in/out UX + time delays.
- [ ] Fee market sensitivity (ordinals congestion).
- [ ] Compliance for tokenized assets on Bitcoin.

## 🧪 Lab: Bridge BTC to L2 and Deploy App

**Goal:** trải nghiệm peg-in/out qua Stacks hoặc Botanix.

**Prerequisites:**
- Tooling: Bitcoin testnet wallet, Stacks CLI hoặc Botanix SDK, Clarity/Solidity compiler.
- Network: Bitcoin testnet + target L2 testnet.
- Skills: wallet ops, smart contract deployment, monitoring.

### Steps
1. Peg-in test BTC (testnet via faucet) sang L2 chọn, ghi lại confirmations & thời gian.
2. Deploy simple smart contract (swap hoặc lending) trên chain đó, chạy unit test.
3. Đo thời gian finality, phí, UX bridging → lập bảng so sánh.
4. Peg-out lại về Bitcoin, ghi chú rủi ro (timeouts, confirmations, custodian delays).

**Metrics to Track:** peg-in/out time, fee per tx, contract deploy cost, user confirmations.

**Deliverables:** tutorial steps, txn hashes, performance metrics dashboard.

## 🧾 Case Study: Ordinals Frenzy 2023-2024

- **Context:** Ordinals + BRC-20 làm network fee spike Q1-Q2 2024.
- **Key Metrics:** phí BTC >$20/tx, blockspace >50% chứa inscriptions, miner revenue tăng mạnh.
- **Architecture Snapshot:** inscription process → indexer (ord) → marketplaces (Magic Eden, OKX).
- **Key Insights:**
  - Miner incentives ↔ mempool congestion → fee market sensitive.
  - Wallet UX (Unisat) cần hỗ trợ inscription batching & fee estimator.
  - Fee volatility mở cơ hội cho Bitcoin L2 cung cấp ổn định.
- **Risks & Mitigations:** spam inscriptions → policy debate; L2 bridging risk → multi-sig attestation.
- **Takeaway:** Khi xây sản phẩm trên Bitcoin cần kế hoạch dynamic fee + fallback sang L2 khi blockspace bị chiếm.