---
title: "Social Feature Architecture"
description: "Friend/guild system, chat service, moderation pipeline."
tags:
  - multiplayer
  - social
updated: 2026-03-11
---

# 🤝 Social Features Architecture

## 1) Friend System
- Service riêng lưu user graph.
- Features: request/accept/block, presence (online/offline), party invite.
- Data model: adjacency list (user_id, friend_id, status).

## 2) Guild/Clan
- Guild profile, roles (leader/officer/member).
- Storage: SQL + cache (Redis) cho membership list.
- Guild chat + announcement.
- Metrics: active member %, donations.

## 3) Chat Architecture
- Gateway → message broker (Kafka, RabbitMQ) → chat worker.
- Channel types: global, lobby, party, guild, whisper.
- Persistence: TTL storage (Mongo/Scylla) hoặc ephemeral (Redis Stream).
- Moderation: profanity filter, spam throttle.

## 4) Social Graph API
- REST/gRPC: `POST /friends/request`, `GET /friends`, `POST /guilds/{id}/invite`.
- Websocket cho real-time updates (presence, chat).

## 5) Moderation & Safety
- Automated filter (regex + ML) trước khi broadcast.
- Report pipeline: store evidence (chat log, replay snippet) → moderator dashboard.
- Rate limit: message/sec, friend request/day.
- Privacy: allow DM only from friends.

## 6) Telemetry
- DAU tham gia social features (% chat, % guild).
- Retention uplift khi trong guild vs solo.
- Toxicity metrics (# report, ban).

## ✅ Apply it
- [ ] Thiết kế service riêng cho friend/guild để scale độc lập.
- [ ] Chọn broker cho chat (Kafka/PubSub).
- [ ] Tích hợp moderation filter + report.
- [ ] Expose API + websocket presence.
- [ ] Dashboard theo dõi social engagement.