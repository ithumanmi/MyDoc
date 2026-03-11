---
title: "Real-time Flash Sale Inventory"
description: "Cách TMĐT hiển thị tồn kho flash sale (còn 2 sản phẩm) cho hàng triệu người dùng mà không làm sập database."
tags:
  - backend
  - system-design
  - ecommerce
updated: 2026-03-11
---

# ⚡ Real-time Flash Sale Inventory

> “Còn đúng 2 sản phẩm!" – Làm sao một sàn thương mại điện tử hiển thị con số này cho hàng triệu người cùng tranh mua trong flash sale mà database không cháy? Bài này mô tả kiến trúc inventory service, cơ chế đếm tồn tức thời, và chiến lược bảo vệ DB.

## 1. Bài toán & Ràng buộc
- Peak: hàng triệu request/giây truy cập 1 SKU.
- Tồn kho cần **nhất quán** ở mức hiển thị (không thể bán vượt quá).
- Delay chấp nhận: < 100–200ms để update số lượng.
- Không được bắn trực tiếp mọi request vào database giao dịch.

## 2. Kiến trúc tổng quan

```
Client → Edge Cache → Inventory Gateway → (Redis Cluster Counter) ↔ Inventory Service ↔ Primary DB
                                                      ↓
                                                   Event Bus (Kafka/PubSub)
                                                      ↓
                                            Stream Processor / Analytics
```

- **Inventory Gateway**: rate limiting, auth, chống bot.
- **Redis Cluster / In-memory counter**: giữ số tồn khả dụng theo SKU.
- **Primary DB** (SQL) lưu sổ cái inventory, bảo đảm ACID.
- **Event Bus** đồng bộ hóa với các dịch vụ khác (order, fulfillment).

## 3. Chiến lược đếm tồn
### 3.1. Preload Counter
- Trước giờ mở sale, preload số lượng SKU vào Redis (`stock_available`).
- Redis dùng `INCRBY/DECRBY` atomic, replication + persistence (AOF) để tránh mất dữ liệu.

### 3.2. Reservation Window
- Khi user bấm “Đặt mua”, hệ thống **reserve** 1 đơn vị (decrement counter).
- Order phải thanh toán trong T phút; nếu hết hạn, counter +1 lại (release).
- Reservation lưu vào DB hoặc Redis Hash `reservation:{orderId}` với TTL.

### 3.3. Two-phase Commit Light
1. **Phase 1**: Redis decrement, emit event `RESERVED`.
2. **Phase 2**: Payment thành công → Inventory Service ghi vào DB và emit `LOCKED`. Nếu payment fail → emit `RELEASED`.

## 4. Hiển thị “Còn 2 sản phẩm” theo thời gian thực
- Frontend subscribe vào WebSocket/Server-Sent Events channel `inventory:SKU123`.
- Mỗi khi counter thay đổi, Inventory Service publish message.
- Đối với traffic cực lớn, dùng **fan-out qua Kafka + Redis Pub/Sub + CDN edge** để cache snapshot 1–2s.
- UI hiển thị `max(real_time_counter, 0)` và có thể “floor” (VD: <5 hiển thị “Còn rất ít”).

## 5. Bảo vệ database
- Database chỉ ghi nhận **cuối cùng** (order thành công) chứ không xử lý mọi lượt click.
- Batch writer: gom các event `LOCKED` mỗi vài ms → `UPDATE inventory SET reserved = reserved + n`.
- Optimistic locking hoặc stored procedure `UPDATE ... WHERE stock >= requested` cho các trường hợp bypass Redis.
- Sử dụng **logical sharding** theo SKU hoặc seller để chia tải.

## 6. Giảm gian lận & load
- **Bot Mitigation**: token bucket per user/IP, CAPTCHA, device fingerprint.
- **Fair Queue**: xếp hàng (queue service) trước khi vào buy flow.
- **Shadow Stock**: giữ một buffer (1–2%) không bán để cover race condition.
- **Consistency Mode**: khi Redis lỗi → fallback sang degraded mode hiển thị “Hết hàng” để bảo vệ hệ thống.

## 7. Observability & Alert
- Metric: Redis latency, key hit rate, reservation vs payment success, oversell count.
- Alert khi: counter <0, release rate > threshold, queue lag, DB write spike.
- Replay event log để audit oversell.

## 8. 🧪 Lab gợi ý
1. Setup Redis Cluster + Lua script để reduce inventory atomic với TTL.
2. Build demo Gateway (Go/Node) expose `/reserve` (decrement) và `/release`.
3. Push event vào Kafka → consumer update Postgres table `inventory_ledger`.
4. WebSocket service subscribe Redis Pub/Sub, broadcast real-time counter.
5. Chaos test: kill Redis node, kiểm tra failover & degraded mode.

## 9. Checklist
- [ ] Preload stock vào Redis/Aerospike trước flash sale.
- [ ] Áp dụng reservation TTL + release logic rõ ràng.
- [ ] Event-driven flow giữa Redis ↔ DB để reconcile.
- [ ] Websocket/long polling hiển thị số lượng theo thời gian thực.
- [ ] Rate limiting & bot mitigation tại gateway.
- [ ] Alert & audit log để phát hiện oversell.

## 10. Liên kết hữu ích
- [System Design Universe](./system-design-universe.md)
- [Search Engine Architecture](./search-engine-architecture.md)
- [Real-time Chat System](./realtime-chat-system.md) – tham khảo mô hình WebSocket.
- Redis Labs blog: “Atomic counters for flash sales”.