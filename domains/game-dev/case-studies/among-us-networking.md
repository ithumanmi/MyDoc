---
title: "Among Us Networking"
description: "Phân tích mô hình P2P, authority chia sẻ và chống cheat của Among Us."
tags:
  - networking
  - case-study
  - among-us
updated: 2026-03-11
---

# 👽 Among Us Networking Case Study

## Architecture
- **Peer-to-peer host**: 1 client làm host (authoritative) để giảm chi phí server.
- **Packets**: UDP custom protocol, reliable overlay cho event quan trọng.
- **State Replication**: host gửi snapshot đơn giản (positions, tasks) mỗi tick.

## Cheat Prevention
- **Host validation**: critical action (kill, vote) chỉ host xác thực → hạn chế client spoof.
- **Heartbeat & timeout**: phát hiện client sửa thời gian.
- **Obfuscation**: packet data pseudo-encrypted, giảm script kiddie.

## Scalability & Issues
- P2P dễ bị **host advantage** + lag khi host mạng yếu.
- DDoS/cheat bùng nổ buộc InnerSloth chuyển sang dedicated server (2021 update) với anti-cheat mạnh hơn.

## Lessons
1. P2P phù hợp team nhỏ launch nhanh nhưng phải chuẩn bị path chuyển sang dedicated.
2. Critical actions cần host authority + logging để điều tra cheat.
3. UX: cung cấp **Reconnect** và region selection để giảm frustration khi host leave.