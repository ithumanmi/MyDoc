---
title: "Solidity Deep Dive"
description: "Storage layout, gas optimization, patterns cho senior smart contract engineer."
tags:
  - solidity
  - smart-contracts
updated: 2026-03-16
---

# 🧠 Solidity Deep Dive

> **Scope:** Từ kiến trúc contract production đến tối ưu gas, tránh lỗi thường gặp và pattern nâng cao.

## 1. Storage Layout & Memory
- Slot = 32 bytes, packing variables giúp tiết kiệm gas.
- `mapping` hash slot = `keccak256(key . slot)`.
- Struct trong storage vs memory: `storage` giữ tham chiếu, `memory` copy.
- **Tooling:** `forge inspect`, `slither-check-upgradeability`.

## 2. Upgradeable Contracts
- **Proxy Patterns:**
  - Transparent Proxy (OpenZeppelin) – admin can't call implementation.
  - UUPS – implementation chịu trách nhiệm upgrade.
  - Beacon Proxy – share logic cho nhiều instance.
- **Pitfalls:** Storage collision, initializer không guard, delegatecall reentrancy.

## 3. Gas Optimization Checklist
- [ ] Sử dụng `immutable` cho constant address/value.
- [ ] `unchecked` cho arithmetic nếu chắc chắn không overflow.
- [ ] `calldata` thay vì `memory` cho parameters không mutate.
- [ ] Event index tối đa 3 topics.
- [ ] Dùng custom errors `error Unauthorized(address caller);`.

## 4. Patterns & Architecture
- **Diamond Pattern (EIP-2535):** Modular hóa contract lớn.
- **Facet Cut:** Add/replace/remove function selectors động.
- **Registry Pattern:** Tách config vào contract riêng (AddressProvider).
- **Access Control:** Role-Based (OpenZeppelin) vs capability-based (Auth từ Solmate).

## 5. Security Gotchas
- **Reentrancy:** Dùng `checks-effects-interactions` + reentrancy guard.
- **Delegatecall:** validate target, no storage collision.
- **tx.origin:** Không dùng cho auth.
- **Unbounded loops:** Gas griefing.
- **Phantom function selectors:** Lưu ý fallback/receive.

## 6. Testing Focus
- Fuzz (Foundry `vm.assume`) để bắt edge-case.
- Fork testing trên mainnet state.
- Snapshot invariant: `handler` pattern.

## Resources
- Solidity docs, Secureum RACE, Solidity by Example advanced.
- [security/smart-contract-auditing.md](../security/smart-contract-auditing.md)