---
title: "Danksharding & EIP-4844"
description: "Blob transactions, proto-danksharding, roadmap to full danksharding."
tags:
  - scaling
  - danksharding
  - eip-4844
updated: 2026-03-11
---

# 🧊 Danksharding & EIP-4844

## 1. Proto-Danksharding (EIP-4844)

- Introduces **blob transactions** for cheap DA space.
- Blob data not accessible to EVM; only commitments stored.
- Reduces L2 fees 10-100x.

## 2. Blob Market

- Separate fee market for blobs.
- Sequencers post batches as blobs; pay in ETH.
- Clients prune blob data after ~2 weeks.

## 3. Roadmap to Full Danksharding

1. Proto-danksharding (4844).
2. Data availability sampling (DAS) for validators.
3. Full danksharding: 64 data shards, proposer-builder separation (PBS).

## 4. Implications for Rollups

- Need blob submission infrastructure.
- Batch size tuning based on blob fees.
- Monitoring expiration of blob data (availability windows).

## 5. Checklist

- [ ] Implement blob poster service + fallback.
- [ ] Monitor blob fee market metrics.
- [ ] Ensure proofs reference blob commitments.
- [ ] Plan for full danksharding (DAS-compatible light clients).

## 🧪 Lab: Blob Poster Service

**Goal:** xây dịch vụ đăng blob cho rollup devnet.

1. Spin up Ethereum devnet với hỗ trợ EIP-4844 (e.g., Geth prototype).
2. Viết service (Node/Python) bundle tx thành blob + gửi `blob_tx`.
3. Track blob fee market, auto adjust batch size.
4. Simulate blob expiry và đảm bảo dữ liệu đã được chứng thực trước khi hết hạn.

**Deliverables:** service repo, monitoring dashboard, incident log khi blob full.