---
title: "Based Rollups"
description: "Based sequencing, shared sequencers, proposer-builder separation."
tags:
  - scaling
  - rollups
  - sequencing
updated: 2026-03-11
---

# ⚙️ Based Rollups

## 1. Concept

- Rollup sequencer piggybacks on L1 proposer.
- Based sequencing integrates rollup ordering into L1 block production.

## 2. Benefits

- Lower latency: no separate sequencer queue.
- Shared MEV capture with L1 (builder markets).
- Reduced reorg risk.

## 3. Architectures

- **OP Stack + Based Sequencer:** OP Labs research.
- **Shared Sequencer Networks:** Espresso, Radius, Astria.
- **PBS Integration:** proposer-builder separation aligns incentives.

## 4. Considerations

- Need L1 support (Ethereum PBS roadmap).
- How to handle downtime/fallback to centralized sequencer.
- MEV distribution to rollup users.

## 5. Checklist

- [ ] Define sequencing path (based, shared, centralized fallback).
- [ ] Integrate with builder (relays, commitments).
- [ ] Enforce data availability commitments.
- [ ] Monitor latency and inclusion guarantees.

## 🧪 Lab: Shared Sequencer Pilot

**Goal:** kết nối rollup devnet với shared sequencer (Espresso/Astria).

1. Deploy minimal rollup (OP Stack devnet).
2. Integrate shared sequencer SDK, configure commitment channel.
3. Send burst of tx, measure inclusion latency vs local sequencer.
4. Test fallback path: disable shared sequencer, revert to local.

**Deliverables:** integration notes, latency metrics, failover playbook.