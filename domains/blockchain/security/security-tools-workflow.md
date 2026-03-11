---
title: "Security Tools Workflow"
description: "Slither, Mythril, Foundry fuzz workflow thực tế."
tags:
  - security-tools
  - auditing
  - fuzzing
updated: 2026-03-11
---

# 🧰 Security Tools Workflow

## 1. Workflow Overview

1. **Static analysis:** Slither.
2. **Symbolic execution:** Mythril.
3. **Fuzz/invariant:** Foundry + Echidna.
4. **Manual review:** business logic + access control.

## 2. Slither Checklist

- Run `slither .` and resolve:
  - reentrancy, tx-ordering, uninitialized storage.
- Generate report: `slither . --sarif`.

## 3. Foundry Fuzz Workflow

1. Write invariants in `Invariant.t.sol`.
2. Run `forge test --fuzz-runs 1000`.
3. Save seeds for reproducibility.

## 4. Mythril Tips

- Use `myth analyze` to check paths.
- Focus on access control + arithmetic.

## 5. Deliverables

- Slither + Mythril reports.
- Fuzz logs + invariant results.
- Manual findings summary.

## 🧪 Lab: Toolchain Runbook

**Goal:** chạy full toolchain trên một repo và ghi lại kết quả.

1. Clone sample protocol (e.g., Uniswap v2 fork).
2. Run `slither .` + export SARIF.
3. Configure Foundry invariants + run fuzz tests.
4. Use Mythril on critical contracts.

**Deliverables:** runbook + tool outputs + prioritized issue list.