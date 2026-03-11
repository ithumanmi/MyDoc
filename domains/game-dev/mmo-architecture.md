---
title: "MMO Architecture"
description: "Shard vs single world, zone server, world state replication."
tags:
  - multiplayer
  - architecture
updated: 2026-03-11
---

# 🏰 MMO Architecture Deep Dive

## 1) Sharding Strategy
- **Shard (Realm)**: Clone world nhiều bản (WoW). Dễ scale, nhưng người chơi bị chia nhỏ.
- **Mega Server**: Single logical world (EVE Online). Cần phân hoạch zone/region.
- **Hybrid**: Lobby shard + instanced dungeon.

## 2) Zone/Region Server
- Thế giới chia thành zone (map piece). Mỗi zone có server riêng.
- Transition: client handoff -> load neighbor zone server.
- Keep-alive ghosting (giữ data 2 zone để tránh teleport lag).

## 3) World State Replication
- Entity Component data sync qua pub/sub (Redis, Kafka).
- Snapshot vs event sourcing:
  - Snapshot: định kỳ lưu trạng thái (position, inventory).
  - Event: log action (loot, trade) -> rebuild state nếu cần.
- Consistency model: eventual consistency cho non-critical (chat), strong cho kinh tế.

## 4) Persistence Layer
- Character DB (SQL): Level, quest.
- Inventory/Trade: transactional DB (ACID) chống dup.
- Hot cache (Redis) để giảm read.

## 5) Scaling Patterns
- Auto-scale zone server theo population.
- Instance dungeon: spin up container khi party vào.
- Background worker cho AI/LLM NPC.

## 6) Monitoring
- CCU/Zone, latency inter-zone.
- Economy metrics (gold sink/source, inflation).
- Queue time khi login.

## Diagram (text)
```
[Login] -> [World Router] -> [Shard/Region]
                         -> [Zone Server A]
                         -> [Zone Server B]
Zone Server -> [State Bus] -> [Persistence]
```

## ✅ Apply it
- [ ] Chọn chiến lược shard phù hợp với player cap.
- [ ] Thiết kế zone boundaries + handoff protocol.
- [ ] Xác định data nào cần strong consistency.
- [ ] Automate scaling + monitoring alert.