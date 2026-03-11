---
title: "Game Networking Terms"
description: "Glossary one-pager cho multiplayer/networking."
tags:
  - networking
  - multiplayer
  - cheatsheet
updated: 2026-03-11
---

# 🌐 Game Networking Terms (Quick Ref)

| Term | Meaning |
| --- | --- |
| RTT (Round Trip Time) | Thời gian packet đi từ client -> server -> client |
| Jitter | Dao động thời gian giữa các packet, gây lag spike |
| Tick Rate | Số lần/giây server cập nhật state (ví dụ 30Hz, 60Hz) |
| Authoritative Server | Server quyết định state cuối cùng để chống cheat |
| Client-side Prediction | Client tự dự đoán movement trước khi server trả về |
| Reconciliation | Điều chỉnh lại state client theo server update |
| Lag Compensation | Server rewind state để xét va chạm/hit dựa trên timestamp |
| Snapshot | Bản chụp state game được gửi đến client |
| Delta Compression | Chỉ gửi sự khác biệt giữa snapshot hiện tại và trước đó |
| Netcode | Layer xử lý replication, RPC, serialization |
| RPC (Remote Procedure Call) | Gửi lệnh từ client tới server hoặc ngược lại |
| Deterministic Simulation | Cùng input -> cùng output, dùng cho rollback |
| Rollback | Client chạy lại frame khi nhận state mới từ server |
| Matchmaking | Hệ thống ghép người chơi vào trận dựa trên MMR/ping |
| NAT Traversal | Kỹ thuật kết nối P2P xuyên qua router/NAT |

## Notes
- Theo dõi **p99 latency** và packet loss %.
- Netcode framework phổ biến: NGO, Mirror, Photon Fusion, Unreal Replication Graph.