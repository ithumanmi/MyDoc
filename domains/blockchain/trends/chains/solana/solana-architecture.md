---
title: "Solana Architecture Deep Dive"
description: "Proof of History, Turbine, Gulf Stream, Sealevel, Firedancer roadmap."
tags:
  - solana
  - architecture
updated: 2026-03-11
---

# ⚡ Solana Architecture

## 1. Proof of History (PoH)

- Verifiable delay function (VDF) tạo global clock.
- Validators sử dụng PoH để xác minh order mà không cần đồng bộ thời gian phức tạp.

## 2. Turbine & Gulf Stream

- **Turbine:** block propagation chia data thành packets → layer tree → giảm băng thông.
- **Gulf Stream:** tx forwarding trước leader slot, hỗ trợ prefetching state.

## 3. Sealevel Parallel Runtime

- Accounts model + read/write locks cho phép song song hóa.
- CPIs (Cross Program Invocations) chia nhỏ logic.

## 4. Firedancer & Scaling Roadmap

- Client validator mới (Jump Crypto) written in C/Assembly.
- Target >1M TPS, giảm latency, đa dạng hóa implementation.

## 5. Checklist

- [ ] Thiết lập monitoring leader schedule & slot health.
- [ ] KPIs: TPS thực tế, block finality, dropped tx.
- [ ] Policy cho state bloat (rent, pruning).