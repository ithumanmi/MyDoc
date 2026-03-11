---
title: "Modular Blockchain"
description: "Celestia, DA layers, execution layers, settlement separation."
tags:
  - scaling
  - modular
  - data-availability
updated: 2026-03-11
---

# 🧱 Modular Blockchain

## 1. Concept

- Tách các lớp: **Execution**, **Settlement**, **Data Availability (DA)**, **Consensus**.
- Mỗi lớp có thể dùng provider khác nhau.

## 2. Celestia (DA Layer)

- **Blobspace** cho rollups đăng dữ liệu.
- Light clients verify via data availability sampling (DAS).
- Sovereign rollups settle on Celestia.

## 3. Execution Layer Options

- General rollups (EVM, zkVM).
- App-specific VMs (Move, Cairo, Wasm).
- Settlement có thể là Ethereum, Bitcoin (via rollups), Solana (future).

## 4. Design Patterns

- **Sovereign rollup:** dùng DA + consensus riêng, không cần L1 settlement (Eclipse, Dym).
- **Settlement rollup:** vẫn gửi proof xuống Ethereum.

## 5. Checklist

- [ ] Chọn DA provider (Celestia, EigenDA, Ethereum blob).
- [ ] Decide settlement vs sovereign.
- [ ] Sequencer decentralization plan.
- [ ] Monitoring DA fees, inclusion delay.

## 🧪 Lab: Spin Up a Sovereign Rollup

**Goal:** triển khai rollup dùng Celestia làm DA.

1. Clone Celestia + Rollkit templates.
2. Configure rollup VM (EVM/Wasm) + DA endpoint.
3. Run local devnet: submit blocks, verify data availability sampling logs.
4. Measure blob fees vs Ethereum blob for comparison.

**Deliverables:** deployment guide, config files, fee comparison table.