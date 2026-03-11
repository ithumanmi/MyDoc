---
title: "AI x Crypto"
description: "On-chain AI agents, compute marketplaces, inference networks."
tags:
  - ai
  - crypto
  - agents
updated: 2026-03-11
---

# 🤖 AI x Crypto (2024-2026)

## 1. AI Agents On-chain

- Smart contracts trigger AI inference via off-chain compute.
- Autonomous agents manage positions, run arbitrage, governance voting.
- Examples: Autonolas, Fetch.AI, Ritual.

## 2. Compute Marketplaces

- Token incentives cho GPU providers.
- Decentralized inference clusters (Bittensor, Akash).
- Pay-per-inference via microtransactions.

## 3. Inference Networks

- Routing request → selecting model providers → verifying outputs.
- MEV-aware inference (prioritized bidding).

## 4. Checklist

- [ ] Define trust model (oracle vs attested hardware).
- [ ] Token rewards for inference accuracy.
- [ ] Monitor inference latency + cost.
- [ ] Governance for model updates.

## 🧪 Lab: Deploy an On-chain AI Agent

**Goal:** xây agent tự động gọi inference mạng Bittensor và phản hồi on-chain.

**Prerequisites:**
- Tooling: Hardhat/Foundry, Node.js agent SDK, Bittensor client.
- Network: Ethereum testnet (Sepolia) + Bittensor test subnet.
- Skills: Solidity, TypeScript/Python automation, oracle integration.

### Steps
1. Viết smart contract phát intent (function selector + payload) và lưu kết quả inference.
2. Dựng off-chain agent service kết nối Bittensor subnet → nhận reward → ký tx trả kết quả lên chain.
3. Thiết lập monitoring (Grafana/Prometheus) cho latency, reward share, thất bại.
4. Thử nhiều subnet để so sánh accuracy/cost, log kết quả trong bảng.

**Metrics to Track:** inference latency, cost per request (TAO/ETH), success rate, reward distribution.

**Deliverables:** contract + agent repo, monitoring dashboard screenshots, runbook xử lý lỗi/chậm.

## 🧾 Case Study: Ritual Compute Marketplace

- **Context:** Ritual (2024) xây inference network riêng, tích hợp với Uniswap hook + agent frameworks.
- **Key Metrics:** ~$50M valuation, hàng nghìn inference/ ngày, validator staking requirements.
- **Architecture Snapshot:** client SDK → router → inference providers → attesters → settlement layer.
- **Key Insights:**
  - Payment routing qua token + stablecoin để giảm biến động.
  - Staked validators xác thực inference outputs trước khi gửi on-chain.
  - Modular SDK giúp dev nối inference vào bất kỳ chain nào.
- **Risks & Mitigations:** attack mô phỏng inference → yêu cầu attestation + slashing; latency spike → multi-region providers.
- **Takeaway:** Thiết kế compute marketplace cần cân bằng bảo mật (attestation) với UX (latency, cost) và minh bạch reward.