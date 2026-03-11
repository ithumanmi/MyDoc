---
title: "Smart Contract Testing"
description: "Unit tests, fuzzing, invariant testing, CI strategy."
tags:
  - testing
  - smart-contracts
  - security
updated: 2026-03-11
---

# ✅ Smart Contract Testing

## 1. Test Pyramid

- **Unit:** từng function, revert, event.
- **Integration:** fork mainnet, simulate DeFi flows.
- **Property/Fuzz:** random inputs to break assumptions.
- **Invariant:** trạng thái không bao giờ sai (e.g., sum balances).

## 2. Tools

- **Hardhat:** Mocha/Chai, ethers.js.
- **Foundry:** `forge test`, fuzz/invariant native.
- **Echidna:** property-based fuzzing.
- **Slither:** static analysis.

## 3. Example Invariant

```solidity
function invariant_totalSupplyMatchesBalances() public {
  assertEq(token.totalSupply(), token.balanceOf(alice) + token.balanceOf(bob));
}
```

## 4. CI Pipeline

1. `forge fmt` / `hardhat compile`.
2. `slither .` + `forge test`.
3. `forge test --fuzz-runs 1000`.
4. Coverage + gas snapshot.

## 5. Checklist

- [ ] Unit tests cover >= 90% critical paths.
- [ ] Invariant testing for core accounting.
- [ ] Fork tests for integration w/ external protocols.
- [ ] Regression test on upgrade/deploy.

## 🧪 Lab: Fuzz + Invariant Suite

**Goal:** build fuzz & invariant test suite for a vault contract.

1. Create vault with `deposit`, `withdraw`, `shares`.
2. Write unit tests for edge cases (0 amount, max amount).
3. Add invariant: `totalAssets >= sum(userBalances)`.
4. Run `forge test --fuzz-runs 1000` and log failing seeds.

**Deliverables:** test suite + report of any invariant violations.