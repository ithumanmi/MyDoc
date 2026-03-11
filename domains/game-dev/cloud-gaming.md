---
title: "Cloud Gaming Architecture"
description: "Streaming stack, input latency, adaptive quality 2024-2026."
tags:
  - game-dev
  - cloud
updated: 2026-03-11
---

# ☁️ Cloud Gaming Architecture

## 1) Streaming Pipeline
- GPU blade render (NVidia A10/A16, AMD MI300) -> encode (NVENC/AV1) -> CDN edge -> client.
- Protocol: WebRTC (low latency), QUIC.
- Client: thin app/browser, decode H.264/AV1, send input via data channel.

## 2) Input Latency Budget
- Target <80ms total: controller -> client -> network -> server -> render.
- Techniques: client-side prediction overlay, local input sampling at 240Hz.
- Multi-region edge POP để giảm RTT.

## 3) Adaptive Quality
- Dynamic bitrate/resolution scaling, foveated streaming.
- Per-scene encoding presets (UI text vs motion heavy).
- Packet loss concealment, forward error correction.

## 4) Infrastructure
- Orchestrator: autoscale GPU nodes via Kubernetes + node pools.
- Session manager: allocate VM/container per player, warm pool.
- Storage streaming: mount asset bundle via cloud FS.

## 5) Business Models
- Subscription (Xbox Cloud, GeForce Now).
- BYOG (Bring your own game license) vs bundled catalog.
- Trials/demos streaming trực tiếp từ store page.

## 6) Testing
- Synthetic latency injection, jitter scenarios.
- Device matrix (TV, mobile, browser) + controller compatibility.

## ✅ Apply it
- [ ] Xác định region target và latency budget.
- [ ] Chọn protocol (WebRTC) + encoder (AV1/H.265).
- [ ] Thiết kế autoscale GPU cluster và session manager.
- [ ] Implement QoS telemetry + adaptive bitrate.