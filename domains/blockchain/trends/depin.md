---
title: "DePIN"
description: "Decentralized physical infrastructure: Helium, Hivemapper, wireless & mapping networks."
tags:
  - depin
  - infrastructure
  - hardware
updated: 2026-03-11
---

# 🛰️ DePIN (Decentralized Physical Infrastructure)

## 1. Overview

- Token incentives để bootstrap hạ tầng vật lý (network, storage, compute).
- Users cung cấp hardware → earn tokens.

## 2. Key Projects

- **Helium:** wireless hotspots (5G, IoT) + MOBILE/HNT rewards.
- **Hivemapper:** dashcam data → HD maps.
- **Render, Filecoin Saturn:** GPU render + CDN.

## 3. Economics

- Dual-token hoặc ve-model để align supply/demand.
- Burn-and-mint equilibrium (Helium).
- Demand aggregators (enterprise partners) trả bằng fiat/crypto.

## 4. Checklist

- [ ] Hardware BOM + logistics (shipping, onboarding).
- [ ] Anti-gaming & proof-of-coverage mechanisms.
- [ ] Regulatory (telecom licenses, data privacy).
- [ ] Token sink: convert rewards → demand fees.

## 🧪 Lab: Deploy a DePIN Node

**Goal:** vận hành thiết bị Helium hoặc Hivemapper trong 7 ngày.

**Prerequisites:**
- Tooling: Helium console, Hivemapper dashboard, Grafana/Telegraf.
- Hardware: Helium hotspot/5G radio hoặc Hivemapper dashcam.
- Skills: networking setup, basic scripting, compliance filing.

### Steps
1. Mua/thuê hotspot/dashcam → kích hoạt, đăng ký location, hoàn thành KYC nếu cần.
2. Theo dõi reward, chứng minh uptime, nộp report coverage mỗi ngày.
3. Tích hợp dashboard (Grafana) hiển thị earning vs opex, signal chất lượng data.
4. Thử chuyển token rewards qua DEX → fiat để đo liquidity và trượt giá.

**Metrics to Track:** uptime %, packets/data uploaded, token rewards vs điện/Internet cost, payout latency.

**Deliverables:** operations log, ROI calculator, compliance checklist, dashboard screenshot.

## 🧾 Case Study: Helium 5G Migration

- **Context:** Helium chuyển từ L1 riêng sang Solana, ra mắt MOBILE token (2023-2024).
- **Key Metrics:** >1M hotspots, hàng nghìn 5G radios, emission schedule dual-token.
- **Architecture Snapshot:** hotspot → Helium Console → Oracle Router → Solana + MOBILE/HNT mint/burn.
- **Key Insights:**
  - Migration cần tooling để map hotspots, hạn chế downtime.
  - Dual-token (HNT + MOBILE) align WiFi/5G incentive.
  - Telecom partnerships yêu cầu KYC/installer certification.
- **Risks & Mitigations:** supply chain delays → approved vendors; regulatory risk → FCC certifications.
- **Takeaway:** DePIN quy mô lớn đòi hỏi supply chain management và chính sách regulator-friendly song song với software upgrades.