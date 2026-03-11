---
title: "MEV Audit Exercises"
description: "Scenario-based checklist cho validator, searcher và dApp bảo vệ người dùng."
tags:
  - audit
  - mev
  - flashbots
updated: 2026-03-11
---

# 🔍 MEV Audit Exercises

## Exercise 1: Validator Relay Configuration

- **Scenario:** Validator chạy mev-boost, kết nối 1 relay.
- **Tasks:**
  1. Review config file, ensure multi-relay + fallback local block.
  2. Simulate relay downtime, verify validator không miss block.
  3. Audit logging/alert setup (PagerDuty, Grafana).
- **Deliverable:** Hardening checklist + incident response playbook.

## Exercise 2: Searcher Bundle Safety

- **Scenario:** Searcher arbitrage bot gửi bundle bị revert khi market move.
- **Tasks:**
  1. Review simulation engine (fork block, state override).
  2. Add guard: max gas per bundle, revert reason handling.
  3. Test conflict scenario (another bundle wins) → ensure retry logic.
- **Deliverable:** Report mô tả failure mode + fix.

## Exercise 3: DApp User Protection

- **Scenario:** DEX muốn giảm sandwich với Flashbots Protect.
- **Tasks:**
  1. Audit frontend RPC selector: ensure default private RPC khi swap > 10k USD.
  2. Verify contract supports `permit` để users không leak approve tx.
  3. Simulate fallback khi private submission fail.
- **Deliverable:** UX checklist + telemetry plan (track sandwich attempts).

## Exercise 4: Relay Censorship

- **Scenario:** Relay A (OFAC) từ chối tx từ Tornado sanction.
- **Tasks:**
  1. Verify validator connect non-censoring relay.
  2. Check compliance policy + communication to community.
  3. Provide metrics on censorship %.
- **Deliverable:** Transparency report + remediation plan.

## Exercise 5: MEV Revenue Benchmark

- **Scenario:** Validator muốn chứng minh share MEV công bằng cho staking pool.
- **Tasks:**
  1. Collect `executionPayload.value` vs `consensus reward`.
  2. Compare vs baseline (non-mev boost) block.
  3. Publish dashboard to delegators.
- **Deliverable:** Dashboard snapshot + commentary.

## General Checklist

- [ ] Multi-relay, fallback builder.
- [ ] Simulation + revert handling cho searcher.
- [ ] User-facing MEV protection (private tx, slippage guard).
- [ ] Monitoring + benchmark (revenue, inclusion rate).
- [ ] Transparency report về MEV distribution.