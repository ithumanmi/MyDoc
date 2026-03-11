---
title: "PBS & MEV-Boost"
description: "Cấu trúc proposer-builder separation, relay, rủi ro censorship."
tags:
  - mev
  - pbs
  - ethereum
updated: 2026-03-11
---

# 🧱 Proposer-Builder Separation & MEV-Boost

## 1. Background

- Ethereum post-Merge: validators đề xuất block.
- MEV-Boost cho phép proposer outsource building cho builders để tối ưu MEV.
- PBS mục tiêu đưa cơ chế này vào protocol để giảm trung gian.

## 2. MEV-Boost Flow

1. Validator chạy `mev-boost` bên cạnh client.
2. Validator nhận bids từ nhiều relay (Flashbots, bloXroute, Manifold...).
3. Chọn bid giá trị cao nhất (block payload + fee).
4. Relay gửi block payload → validator sign → broadcast.

## 3. Relay Components

- **Builder:** assemble block & compute value.
- **Relay:** verify block, ensure validity trước khi gửi proposer.
- **Proposer:** validator sign block.

## 4. Risks

- **Censorship:** Relay có thể loại tx (OFAC compliance).
- **Centralization:** ít builder mạnh → risk monopoly.
- **Outage:** Relay downtime khiến validator mất reward → cần fallback block local.

## 5. Best Practices for Validators

- Connect nhiều relay (Flashbots, Ultra Sound, Agnostic, bloXroute).
- Configure fallback block builder (local execution client) nếu relay fail.
- Monitor `mev-boost` logs, inclusion rate.
- Update client để hỗ trợ future enshrined PBS.

## 6. Future: Enshrined PBS

- Đưa logic builder selection vào protocol.
- Có thể yêu cầu proposer nhận commitment trước khi biết block content (reduce MEV leakage).
- Research topics: SUAVE, Shared Sequencer, inclusion lists.

## 7. Checklist

- [ ] Chạy `mev-boost` với multi-relay config.
- [ ] Thiết lập alert khi relay connection fail.
- [ ] Document policy (censorship, fallback local block).
- [ ] Theo dõi cập nhật EIP liên quan PBS (ePBS, inclusion list).