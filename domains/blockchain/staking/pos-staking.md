---
title: "PoS Staking Mechanics"
description: "Validator lifecycle, hardware, client setup và reward model."
tags:
  - staking
  - ethereum
  - validator
updated: 2026-03-11
---

# 🧱 Native PoS Staking Mechanics

## 1. Validator Lifecycle (Ethereum)

1. **Deposit:** gửi 32 ETH vào deposit contract (Launchpad).
2. **Activation queue:** phụ thuộc tổng số validator (churn limit).
3. **Proposal/Duties:** propose block (~1/`#validators`), attestation mỗi epoch (6.4m).
4. **Exit:** voluntary exit hoặc forced (slash/offline).
5. **Withdrawal:** partial (over 32 ETH) hoặc full sau exit.

## 2. Hardware & Software

- **Execution Client:** Geth/Nethermind/Erigon.
- **Consensus Client:** Lighthouse/Prysm/Teku/Nimbus.
- **Specs:** 4c CPU, 16GB RAM, 1TB SSD NVMe, UPS + backup internet.
- **OS:** Ubuntu LTS, hardened (UFW, fail2ban).
- **Monitoring:** Prometheus + Grafana, Lodestar dashboard, SSV DVT.

## 3. Reward Model

- Base reward ∝ `1/√total_active_balance`.
- Sources: block proposal (~12%), attestation (~84%), sync committees, MEV tips.
- Penalties: missed attestation, inactivity leakage if network failure.

## 4. Diversification

- **Clients:** chạy combo minority (e.g., Execution: Nethermind, Consensus: Lighthouse) để tránh client bug slash.
- **Geography:** multi-region nodes hoặc remote signer (Web3Signer, Horcrux).

## 5. Tooling

- `ethdo`, `staking-deposit-cli` cho key management.
- DVT (SSV, Obol) giảm single operator risk.
- Validator-as-a-service (Kiln, Staked.us) cho enterprise.

## 6. Checklist

- [ ] Chuẩn hóa key management (mnemonic offline, slashing protection).
- [ ] Chọn client diversity (>= 2 minority clients).
- [ ] Cấu hình monitoring + alert (Grafana, PagerDuty).
- [ ] Testing voluntary exit + withdrawal flow.
- [ ] Runbook sự cố (loss internet, client bug, slash event).