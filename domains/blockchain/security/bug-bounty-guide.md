---
title: "Bug Bounty Guide"
description: "Immunefi, Code4rena và cách tham gia audit contests."
tags:
  - bug-bounty
  - security
  - audits
updated: 2026-03-11
---

# 🏆 Bug Bounty Guide

## 1. Platforms

- **Immunefi:** large bounties, real-world programs.
- **Code4rena:** competitive audit contests.
- **Hats Finance:** permissionless audit competitions.

## 2. How to Start

1. Pick protocol you understand.
2. Read docs + architecture.
3. Build threat model: assets, trust boundaries.
4. Review critical paths (withdraw, mint, upgrade).

## 3. Reporting

- Provide PoC + reproduction steps.
- Impact analysis (loss, griefing, denial).
- Suggest patch / mitigation.

## 4. Tips

- Focus on access control + accounting.
- Check upgradeable patterns.
- Look for missing validation of oracle/bridge.

## 5. Deliverables

- Report template + PoC repo.
- Contest notes + issue severity.

## 🧪 Lab: Mini Bounty Submission

**Goal:** tham gia một contest nhỏ và nộp report.

1. Chọn program trên Code4rena/Hats với scope nhỏ.
2. Lọc component critical, đọc spec + code.
3. Viết PoC cho 1 bug (logic hoặc access control).
4. Soạn report theo template và submit draft (mock nếu không public).

**Deliverables:** PoC repo + report + retro (time spent, lessons).