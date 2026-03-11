---
title: "Oracle Audit Exercises"
description: "Scenario-based checklist để audit oracle integration và circuit breaker."
tags:
  - audit
  - oracle
  - security
updated: 2026-03-11
---

# 🔎 Oracle Audit Exercises

## Exercise 1: Lending Protocol Price Feed

- **Scenario:** Protocol dùng Chainlink feed cho collateral ratio.
- **Tasks:**
  1. Kiểm tra contract lấy giá, validate decimals, timestamp.
  2. Review fallback logic khi feed stale.
  3. Viết test case inject stale data, verify liquidation pause.
- **Deliverable:** Audit report section nêu rủi ro + remediation.

## Exercise 2: Perpetual DEX Dual Oracle

- **Scenario:** Protocol dùng Pyth + DEX TWAP.
- **Tasks:**
  1. Kiểm tra weighting/median logic.
  2. Verify TWAP window > 30 phút, flash loan resistant.
  3. Simulate price manipulation attack (foundry test) và verify circuit breaker.
- **Deliverable:** Proof-of-Concept script cho attack + fix.

## Exercise 3: Cross-chain Messaging via CCIP

- **Scenario:** Bridge dùng Chainlink CCIP để gửi giá.
- **Tasks:**
  1. Đánh giá rate limit, allowlist config.
  2. Check emergency pause + governance delay.
  3. Verify monitoring/tracing logs.
- **Deliverable:** Checklist compliance (rate limit thresholds, incident response).

## Exercise 4: Optimistic Oracle (UMA)

- **Scenario:** Prediction market rely on UMA optimistic oracle.
- **Tasks:**
  1. Review liveness window vs market volatility.
  2. Ensure dispute bond đủ lớn.
  3. Simulate delayed dispute.
- **Deliverable:** Risk rating + recommended bond size.

## Exercise 5: API3 Airnode Integration

- **Scenario:** Insurance protocol dùng API3 first-party data.
- **Tasks:**
  1. Kiểm tra serverless Airnode config (API key, endpoint).
  2. Review signature verification on-chain.
  3. Audit incident response khi provider offline.
- **Deliverable:** Architecture diagram + mitigation plan.

## General Checklist

- [ ] Timestamp & staleness guard.
- [ ] Fallback/Manual override documented.
- [ ] Monitoring (alert channel, on-call).
- [ ] Economic security (stake/slash, dispute bond).
- [ ] Incident runbook tested.