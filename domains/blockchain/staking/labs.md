---
title: "Staking Lab"
description: "Hands-on: triển khai validator testnet, theo dõi APR, và loop liquid staking."
tags:
  - staking
  - lab
  - ethereum
updated: 2026-03-11
---

# 🧪 Staking Lab

## Lab A: Ethereum Testnet Validator

1. **Setup:**
   - Hardware: 4c CPU, 16GB RAM, 200GB SSD.
   - Install clients: `sudo apt install geth`, download consensus (Lighthouse).
2. **Keys:**
   ```bash
   git clone https://github.com/ethereum/staking-deposit-cli
   ./deposit new-mnemonic --chain holesky --num_validators 1
   ```
3. **Deposit:**
   - Use Holesky faucet (32 ETH) → deposit contract.
4. **Run Clients:**
   ```bash
   lighthouse bn \
     --network holesky \
     --execution-endpoint http://localhost:8551 \
     --graffiti "Docs Lab"
   ```
5. **Monitoring:**
   - Enable Prometheus metrics `--metrics`.
   - Dashboards: Grafana `beaconchain.json`.
6. **Exercise:** Simulate outage, observe missed attestation penalty, document recovery.

## Lab B: Liquid Staking Loop

1. **Goal:** Stake trên Lido testnet, dùng stETH làm collateral Aave testnet.
2. **Steps:**
   - Mint test stETH → deposit vào Aave → borrow ETH.
   - Restake borrowed ETH, monitor health factor.
3. **Exercise:** Calculate effective leverage and liquidation threshold.

## Lab C: EigenLayer Operator Dry-Run

1. Join EigenLayer testnet (if available).
2. Deploy operator node, connect to AVS sample client.
3. Send mock tasks, ensure logs capture latency.

## Deliverables

- [ ] Validator node up & monitored.
- [ ] APR tracker script (see benchmark section).
- [ ] Report cho liquid staking loop (leverage, risk).
- [ ] EigenLayer operator checklist.