---
title: "Intent-based Protocols"
description: "Intent layers, solvers, CoW Protocol, shared settlement."
tags:
  - intents
  - solvers
  - cow-protocol
updated: 2026-03-11
---

# 🎯 Intent-based Protocols

## 1. Concept

- Users express desired outcome (intent) thay vì cụ thể tx.
- Solvers cạnh tranh để thực thi intent tối ưu.

## 2. Architecture

- **Intent relayer:** collects signed intents.
- **Solver network:** proposes fulfillment paths (DEX, RFQ, RFQ).
- **Settlement layer:** CoW Protocol, Anoma, SUAVE.

## 3. Benefits

- Better execution (batching, MEV protection).
- Gas abstracted từ user.
- Cross-domain settlement (L1, L2, CeFi).

## 4. Checklist

- [ ] Intent schema + signing format.
- [ ] Solver incentives và slashing.
- [ ] Settlement finality + dispute window.
- [ ] UX: transparent routing + price guarantees.

## 🧪 Lab: Build a Solver Bot

**Goal:** triển khai solver tham gia CoW Protocol.

**Prerequisites:**
- Tooling: CoW Protocol solver kit, Rust/Go or TypeScript.
- Network: CoW Protocol mainnet sandbox hoặc testnet if available.
- Skills: DEX routing, MEV mitigation, monitoring.

### Steps
1. Tạo intent listener: subscribe CoW API/mempool, chuẩn hóa intent schema.
2. Implement solver strategy (batch auctions, RFQ, CeFi liquidity) + risk guardrails.
3. Submit solution, track fill rate, profit share, gas used.
4. Log các case bị reject để tinh chỉnh risk controls, update config.

**Metrics to Track:** fill rate, average slippage, solver revenue, rejection reasons.

**Deliverables:** solver repo, performance dashboard, post-mortem rejected intents.

## 🧾 Case Study: Anoma Intent Gossip

- **Context:** Anoma thiết kế intent gossip network + multi-domain settlement (2024 testnets).
- **Key Metrics:** hàng nghìn intents/ngày, latency gossip <1s, multi-domain finality <1 phút.
- **Architecture Snapshot:** user wallet → intent gossip mesh → solver selection → execution layer (L1/L2).
- **Key Insights:**
  - Partial fills + multi-hop settlement cần sequencing logic.
  - Privacy-preserving intents qua ZK giúp che route nhưng tăng chi phí.
  - Sybil-resistant reputation cho solvers để chống spam.
- **Risks & Mitigations:** spam intents → staking requirement; solver cartelization → random selection + audits.
- **Takeaway:** Intent layers đòi hỏi hạ tầng gossip + reputational scoring để chống spam đồng thời vẫn mở.