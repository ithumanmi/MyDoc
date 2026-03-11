---
title: "Solidity Deep Dive"
description: "Advanced patterns, gas optimization, assembly, security pitfalls."
tags:
  - solidity
  - evm
  - smart-contracts
updated: 2026-03-11
---

# 🧠 Solidity Deep Dive

## 1. Advanced Patterns

- **Access Control:** `Ownable`, `AccessControl`, role-based guards.
- **Pull payments:** tránh reentrancy bằng withdraw pattern.
- **Pausable + Circuit Breaker:** emergency stop.
- **Upgradeable Storage:** `StorageSlot`, `ERC-7201` namespace.
- **Meta-transactions:** ERC-2771 trusted forwarder.

## 2. Gas Optimization

- Use `unchecked` for overflow when safe.
- Prefer `uint256` packing, short-circuit `if`.
- Cache storage into memory.
- `immutable`/`constant` to avoid SLOAD.
- Emit fewer events; avoid dynamic arrays in events.

## 3. Low-level & Assembly

```solidity
assembly {
  let ptr := mload(0x40)
  mstore(ptr, 0x20)
  mstore(add(ptr, 0x20), 0x2a)
  return(ptr, 0x40)
}
```

- Use for custom `abi.encodePacked`, calldata parsing.
- Beware of memory clobbering, free memory pointer.

## 4. Security Pitfalls

- Reentrancy (use checks-effects-interactions).
- Delegatecall storage collision.
- Signature replay (domain separator).
- Oracle manipulation (TWAP, circuit breaker).

## 5. Tooling

- **Static analysis:** Slither, MythX.
- **Invariant testing:** Foundry, Echidna.
- **Formal verification:** Certora, Scribble.

## 6. Checklist

- [ ] Storage layout documented for upgrades.
- [ ] Gas benchmark by function.
- [ ] Assembly reviewed + fuzz tested.
- [ ] Critical invariants enforced.

## 🧪 Lab: Gas & Security Hardening

**Goal:** tối ưu một contract ERC-20 + test reentrancy guard.

1. Implement ERC-20 with `mint` and `burn`.
2. Add `Pausable` + `AccessControl`.
3. Run gas snapshot before/after optimizations.
4. Add Foundry fuzz test for `transfer` + `approve` invariants.

**Deliverables:** gas report (table), test logs, summary improvements.