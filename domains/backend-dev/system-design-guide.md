# 🏗️ System Design & Distributed Systems: Deep Dive Guide

> [← Back to Backend Roadmap](./README.md) | [Home](../../README.md)
>
> **Also:** [`domains/system-design/`](../system-design/README.md) for interview-focused designs · challenges under `challenges/system-design/`

<!-- agent-summary -->
**Agent SUMMARY** (read this first; jump to numbered `##` needed):
- Canonical backend deep-dive for distributed systems (complements shorter `domains/system-design/` cases).
- Flow: Fundamentals → Core Patterns → Advanced → Real-world cases → Performance → Interview framework → Hands-on.
- New learners: §§1–2; interview prep: §§4+6; builders: §7 then §3 when stuck.
- TL;DR block immediately below lists key takeaways — use before dumping sections.
<!-- /agent-summary -->

Hướng dẫn toàn diện về System Design và Distributed Systems - Kỹ năng cốt lõi của Senior Backend Engineer và System Architect.

---

## TL;DR & Lộ trình đọc nhanh
> Bạn có thể đọc toàn bộ guide (~20 phút) hoặc theo hành trình ngắn bên dưới.

### TL;DR (Key takeaways)
- ✅ Hiểu nền tảng: Scalability (Vertical vs Horizontal), Load Balancing, CAP, Replication/Sharding.
- ✅ Thành thạo patterns: Caching, Message Queue, API Gateway, Circuit Breaker, CQRS/Event Sourcing.
- ✅ Biết đọc tình huống thực tế: URL shortener, Twitter feed, Netflix streaming, Uber dispatch, WhatsApp chat.
- ✅ Tập trung hiệu năng: Golden signals, profiling tools, autoscaling.
- ✅ Chuẩn bị interview: framework 4 bước, capacity planning, template câu hỏi.

### Lộ trình đọc gợi ý
1. **Mới bắt đầu?** Đọc `#1 Fundamentals` + `#2 Core Patterns` (15 phút).
2. **Chuẩn bị phỏng vấn?** Kết hợp `#4 Real-world Cases` + `#6 Interview Framework` + template ở `templates/system-design-interview-cheatsheet.md`.
3. **Muốn build thực tế?** Nhảy thẳng tới `#7 Hands-on Projects`, sau đó quay lại `#3 Advanced Concepts` khi gặp vấn đề.
4. **Cần recap nhanh?** Scroll đến cuối mỗi section để xem bullet key points, bookmark lại anchor để quay lại khi cần.

> 💡 Tip: sử dụng TOC của editor hoặc tính năng collapse headings để đi theo từng mục thay vì đọc liền mạch.

---

## 📋 Mục lục

1. [Fundamentals](#1-fundamentals-nền-tảng)
2. [Core Patterns](#2-core-patterns-các-mẫu-thiết-kế-cốt-lõi)
3. [Advanced Concepts](#3-advanced-concepts-khái-niệm-nâng-cao)
4. [Real-world System Design Cases](#4-real-world-system-design-cases)
5. [Performance & Optimization](#5-performance--optimization)
6. [Interview Framework](#6-interview-framework-khung-phỏng-vấn)
7. [Hands-on Projects](#7-hands-on-projects)
8. [Resources](#8-resources)

---

## 1. Fundamentals (Nền tảng)

### 1.1. Scalability Principles

#### **Vertical Scaling (Scale Up)**
Nâng cấp phần cứng của server hiện tại.

**Ví dụ:**
```
Server cũ: 4 CPU, 8GB RAM
↓ Upgrade
Server mới: 16 CPU, 64GB RAM
```

**Ưu điểm:**
- Đơn giản, không cần thay đổi code.
- Không có network latency (mọi thứ trong 1 máy).

**Nhược điểm:**
- Đắt (CPU/RAM tốt rất đắt).
- Có giới hạn vật lý (không thể lên vô hạn).
- Single Point of Failure (SPOF) - Server sập = Toàn bộ hệ thống sập.

---

#### **Horizontal Scaling (Scale Out)**
Thêm nhiều servers, phân tải công việc.

**Ví dụ:**
```
1 server (100 RPS) 
↓ Scale out
3 servers (300 RPS total, mỗi server 100 RPS)
```

**Ưu điểm:**
- Rẻ hơn (Dùng nhiều máy commodity thay vì 1 máy đắt).
- Không giới hạn (Cần thêm → Mua thêm server).
- High Availability (1 server sập, 2 server còn lại vẫn hoạt động).

**Nhược điểm:**
- Phức tạp: Cần Load Balancer, Distributed state.
- Network latency giữa servers.

**Kết luận:** Hầu hết hệ thống lớn đều dùng **Horizontal Scaling**.

---

### 1.2. Load Balancing

Phân phối requests đến nhiều servers.

#### **Algorithms:**

**1. Round Robin**
```
Request 1 → Server A
Request 2 → Server B  
Request 3 → Server C
Request 4 → Server A (lặp lại)
```
- **Đơn giản**, nhưng không tối ưu nếu servers có cấu hình khác nhau.

**2. Least Connections**
Gửi request đến server có ít connections nhất.
- Tốt cho **long-lived connections** (WebSocket).

**3. Consistent Hashing**
Dùng hash function để map request → server.
- **Use case:** Caching (Đảm bảo request của user X luôn đến server A để hit cache).

**Code Example (Consistent Hashing - TypeScript):**
```typescript
class ConsistentHash {
  private ring: Map<number, string> = new Map();
  private sortedKeys: number[] = [];
  
  addServer(server: string, virtualNodes: number = 150) {
    for (let i = 0; i < virtualNodes; i++) {
      const hash = this.hash(`${server}:${i}`);
      this.ring.set(hash, server);
      this.sortedKeys.push(hash);
    }
    this.sortedKeys.sort((a, b) => a - b);
  }
  
  getServer(key: string): string {
    const hash = this.hash(key);
    // Tìm server đầu tiên có hash >= request hash
    for (const serverHash of this.sortedKeys) {
      if (serverHash >= hash) {
        return this.ring.get(serverHash)!;
      }
    }
    // Wrap around
    return this.ring.get(this.sortedKeys[0])!;
  }
  
  private hash(key: string): number {
    // Simple hash (Production: dùng MD5/SHA1)
    let hash = 0;
    for (let i = 0; i < key.length; i++) {
      hash = ((hash << 5) - hash) + key.charCodeAt(i);
    }
    return Math.abs(hash);
  }
}

// Usage
const lb = new ConsistentHash();
lb.addServer('server-A');
lb.addServer('server-B');
lb.addServer('server-C');

console.log(lb.getServer('user:123')); // → server-B (consistent)
console.log(lb.getServer('user:123')); // → server-B (same server)
```

---

### 1.3. CAP Theorem

**Định lý:** Trong hệ thống phân tán, bạn chỉ có thể đảm bảo tối đa **2 trong 3** thuộc tính:

- **C - Consistency:** Mọi read đều thấy data mới nhất.
- **A - Availability:** Mọi request đều nhận response (kể cả khi 1 node sập).
- **P - Partition Tolerance:** Hệ thống hoạt động dù network bị chia cắt.

#### **Trade-offs:**

**CP Systems (Ưu tiên Consistency):**
- **MongoDB, HBase, Redis (with replication).**
- Khi network partition xảy ra → Từ chối writes để đảm bảo consistency.
- **Use case:** Banking (Số dư tài khoản phải chính xác 100%).

**AP Systems (Ưu tiên Availability):**
- **Cassandra, DynamoDB, Couchbase.**
- Khi network partition → Vẫn chấp nhận writes, dữ liệu có thể tạm thời inconsistent (Eventual Consistency).
- **Use case:** Social media feed (OK nếu bạn thấy post của bạn bè trễ 1-2 giây).

**CA Systems (Không Partition Tolerance):**
- **Không tồn tại trong distributed systems** (Network luôn có thể bị partition).
- Chỉ có trong single-node systems (PostgreSQL, MySQL trên 1 máy).

---

### 1.4. Database Scaling

#### **Replication (Nhân bản)**

**Master-Slave Replication:**
```
         ┌─────────────┐
         │   MASTER    │ (Writes)
         └──────┬──────┘
                │
       ┌────────┴────────┐
       ▼                 ▼
┌────────────┐    ┌────────────┐
│  SLAVE 1   │    │  SLAVE 2   │ (Reads)
└────────────┘    └────────────┘
```

- **Writes** → Master.
- **Reads** → Slaves (Phân tải read queries).
- **Replication Lag:** Slave có thể trễ vài ms/seconds so với Master.

**Multi-Master Replication:**
- Nhiều masters, mỗi master đều nhận writes.
- **Conflict Resolution** phức tạp (2 users cùng lúc update 1 row).

---

#### **Sharding (Horizontal Partitioning)**

Chia data thành nhiều partitions (shards).

**Example: User Table**
```
Shard 1: user_id % 3 == 0 → Server A
Shard 2: user_id % 3 == 1 → Server B
Shard 3: user_id % 3 == 2 → Server C
```

**Challenges:**
- **Cross-shard queries:** Query liên quan nhiều shards (SELECT * FROM users WHERE city = 'Hanoi') → Phải query cả 3 servers.
- **Resharding:** Khi thêm server mới, cần migrate data.

---

## 2. Core Patterns (Các mẫu thiết kế cốt lõi)

### 2.1. Caching Strategies

#### **Cache-Aside (Lazy Loading)**

**Flow:**
```
1. App check cache
2. If HIT → Return cached data
3. If MISS → Query DB → Store in cache → Return data
```

**Code Example (Node.js + Redis):**
```typescript
import Redis from 'ioredis';
const redis = new Redis();

async function getUser(userId: string) {
  const cacheKey = `user:${userId}`;
  
  // 1. Check cache
  const cached = await redis.get(cacheKey);
  if (cached) {
    console.log('Cache HIT');
    return JSON.parse(cached);
  }
  
  // 2. Cache MISS → Query DB
  console.log('Cache MISS');
  const user = await db.query('SELECT * FROM users WHERE id = ?', [userId]);
  
  // 3. Store in cache (TTL: 5 minutes)
  await redis.setex(cacheKey, 300, JSON.stringify(user));
  
  return user;
}
```

**Pros:** Đơn giản.  
**Cons:** Cache có thể stale nếu DB update mà không invalidate cache.

---

#### **Write-Through Cache**

**Flow:**
```
1. App writes → Cache
2. Cache writes → DB
3. Return success
```

**Pros:** Cache luôn consistent với DB.  
**Cons:** Chậm hơn (2 write operations).

---

#### **Cache Invalidation**

> *"There are only two hard things in Computer Science: cache invalidation and naming things." - Phil Karlton*

**Strategies:**
1. **TTL (Time To Live):** Cache tự hết hạn sau X giây.
2. **Event-driven:** Khi update DB → Gửi event → Invalidate cache.
3. **Manual:** Admin button "Clear cache".

---

### 2.2. Message Queues

Giải quyết **asynchronous processing**.

#### **Use Case: Email Notification**

**Without Queue (Bad):**
```typescript
app.post('/order', async (req, res) => {
  await db.insert('orders', req.body);
  await sendEmail(req.body.email); // User chờ 2-3s
  res.json({ success: true });
});
```

**With Queue (Good):**
```typescript
import Bull from 'bull';
const emailQueue = new Bull('email');

app.post('/order', async (req, res) => {
  await db.insert('orders', req.body);
  await emailQueue.add({ email: req.body.email }); // < 1ms
  res.json({ success: true }); // Instant response
});

// Worker process
emailQueue.process(async (job) => {
  await sendEmail(job.data.email);
});
```

---

#### **RabbitMQ vs Kafka**

| Feature | RabbitMQ | Kafka |
|---------|----------|-------|
| **Model** | Message Broker (Push) | Event Log (Pull) |
| **Throughput** | ~20k msg/s | ~1M msg/s |
| **Use case** | Task queues, RPC | Event streaming, Logs |
| **Retention** | Delete after consumed | Keep events (configurable) |
| **Order** | Per queue | Per partition |

---

### 2.3. API Gateway

Single entry point cho tất cả microservices.

**Responsibilities:**
1. **Routing:** `/users/*` → User Service, `/products/*` → Product Service.
2. **Authentication:** Verify JWT token.
3. **Rate Limiting:** Max 100 req/minute per user.
4. **Request Aggregation:** Client call 1 endpoint → Gateway gọi 3 services → Merge results.

**Tools:** Kong, AWS API Gateway, Nginx.

---

## 3. Advanced Concepts (Khái niệm nâng cao)

### 3.1. Consensus Algorithms

Làm sao để nhiều nodes "đồng ý" về 1 giá trị trong distributed system?

#### **Raft Algorithm**

**Use case:** etcd (Kubernetes), Consul.

**Core Idea:**
- **Leader Election:** 1 node trở thành Leader, còn lại là Followers.
- **Log Replication:** Leader nhận write → Gửi log đến Followers → Khi majority ACK → Commit.

**Safety:** Nếu Leader sập, election mới diễn ra.

---

### 3.2. Event Sourcing & CQRS

#### **Event Sourcing**

Thay vì lưu **State**, lưu **Events**.

**Example: Bank Account**

**Traditional (State):**
```sql
UPDATE accounts SET balance = 500 WHERE id = 123;
```

**Event Sourcing:**
```json
[
  { "event": "AccountCreated", "balance": 0 },
  { "event": "MoneyDeposited", "amount": 1000 },
  { "event": "MoneyWithdrawn", "amount": 500 }
]
```

**Current Balance:** Replay events → 0 + 1000 - 500 = **500**.

**Pros:**
- **Audit trail:** Biết chính xác lịch sử thay đổi.
- **Replay events:** Debug, recover data.

**Cons:**
- Queries chậm (phải replay events).

---

#### **CQRS (Command Query Responsibility Segregation)**

Tách **Write Model** và **Read Model**.

```
┌─────────┐        ┌───────────────┐
│ Command │───────>│  Write Model  │ (Event Sourcing)
└─────────┘        └───────────────┘
                           │
                           ▼ (Events)
                   ┌───────────────┐
                   │  Read Model   │ (Materialized View - SQL)
                   └───────────────┘
                           ▲
┌─────────┐               │
│  Query  │───────────────┘
└─────────┘
```

**Pros:** Optimize riêng cho read/write.  
**Cons:** Eventual consistency (Read model có thể stale).

---

### 3.3. Microservices Patterns

#### **Circuit Breaker**

Tránh cascade failures.

**Scenario:**
- Service A gọi Service B.
- Service B sập → Service A retry liên tục → Service A cũng sập.

**Solution:**
```typescript
enum CircuitState { CLOSED, OPEN, HALF_OPEN }

class CircuitBreaker {
  private state = CircuitState.CLOSED;
  private failureCount = 0;
  private threshold = 5;
  
  async call(fn: Function) {
    if (this.state === CircuitState.OPEN) {
      throw new Error('Circuit is OPEN');
    }
    
    try {
      const result = await fn();
      this.onSuccess();
      return result;
    } catch (error) {
      this.onFailure();
      throw error;
    }
  }
  
  private onSuccess() {
    this.failureCount = 0;
    this.state = CircuitState.CLOSED;
  }
  
  private onFailure() {
    this.failureCount++;
    if (this.failureCount >= this.threshold) {
      this.state = CircuitState.OPEN;
      setTimeout(() => {
        this.state = CircuitState.HALF_OPEN; // Try again
      }, 30000); // 30s
    }
  }
}
```

---

## 4. Real-world System Design Cases

### 4.1. URL Shortener (Bit.ly)

#### **Requirements:**
- **Functional:**
  - Given long URL → Return short URL.
  - Short URL redirect to long URL.
  - Custom aliases (optional).
- **Non-functional:**
  - High availability (99.99%).
  - Low latency (< 100ms).
  - Scale: 100M URLs, 10k writes/s, 100k reads/s.

#### **API Design:**
```
POST /api/shorten
Body: { "url": "https://example.com/very/long/url" }
Response: { "shortUrl": "https://bit.ly/abc123" }

GET /:shortCode
Response: 302 Redirect to long URL
```

#### **Core Algorithm: Base62 Encoding**

```typescript
const ALPHABET = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';

function encode(num: number): string {
  let encoded = '';
  while (num > 0) {
    encoded = ALPHABET[num % 62] + encoded;
    num = Math.floor(num / 62);
  }
  return encoded || '0';
}

function decode(str: string): number {
  let num = 0;
  for (let i = 0; i < str.length; i++) {
    num = num * 62 + ALPHABET.indexOf(str[i]);
  }
  return num;
}

// Example
const id = 123456789;
const shortCode = encode(id); // → "8M0kX"
console.log(decode(shortCode)); // → 123456789
```

#### **Database Schema:**
```sql
CREATE TABLE urls (
  id BIGSERIAL PRIMARY KEY,
  short_code VARCHAR(10) UNIQUE NOT NULL,
  long_url TEXT NOT NULL,
  created_at TIMESTAMP DEFAULT NOW(),
  INDEX idx_short_code (short_code)
);
```

#### **High-level Architecture:**
```
┌────────┐      ┌─────────────┐      ┌──────────┐
│ Client │─────>│ Load Balancer│─────>│ API Servers│
└────────┘      └─────────────┘      └──────┬───┘
                                            │
                             ┌──────────────┴───────────┐
                             ▼                          ▼
                      ┌────────────┐            ┌────────────┐
                      │   Redis    │            │ PostgreSQL │
                      │  (Cache)   │            │  (DB)      │
                      └────────────┘            └────────────┘
```

**Optimization:**
- **Cache:** Redis cache cho hot URLs (80/20 rule).
- **CDN:** Serve redirects from edge locations.

---

### 4.2. Twitter/X Feed

#### **Requirements:**
- User posts tweet → Followers see it in their timeline.
- Scale: 300M users, 500M tweets/day.

#### **Core Challenge: Fan-out**

**Approach 1: Fan-out on Write (Push)**
```
User A (1M followers) posts tweet
→ Insert tweet vào timeline của 1M followers
→ Slow write (1M writes), fast read
```

**Approach 2: Fan-out on Read (Pull)**
```
User B opens timeline
→ Query tweets của tất cả users B follows
→ Merge + Sort by time
→ Fast write, slow read
```

**Hybrid Approach (Twitter's solution):**
- Normal users: Fan-out on Write.
- Celebrities (>1M followers): Fan-out on Read.
- User timeline = Pre-computed feed + Real-time fetch từ celebrities.

#### **Database Schema:**
```sql
-- Tweets
CREATE TABLE tweets (
  id BIGSERIAL PRIMARY KEY,
  user_id BIGINT,
  content TEXT,
  created_at TIMESTAMP,
  INDEX idx_user_time (user_id, created_at DESC)
);

-- Timeline (Materialized)
CREATE TABLE timeline (
  user_id BIGINT,
  tweet_id BIGINT,
  created_at TIMESTAMP,
  PRIMARY KEY (user_id, created_at DESC, tweet_id)
);
```

---

### 4.3. Netflix Video Streaming

#### **Requirements:**
- Stream video với chất lượng tốt nhất dựa trên bandwidth.
- Scale: 200M users, 100M concurrent streams.

#### **Core Concepts:**

**1. Adaptive Bitrate Streaming (ABR)**
- Video được encode thành nhiều chất lượng: 240p, 480p, 720p, 1080p.
- Client tự động chuyển chất lượng dựa trên bandwidth hiện tại.

**2. CDN (Content Delivery Network)**
```
┌──────────┐      ┌──────────┐      ┌────────────┐
│  User    │─────>│ CDN Edge │─────>│ Origin Server│
│ (Vietnam)│      │ (Singapore)     │  (US)       │
└──────────┘      └──────────┘      └────────────┘
              (Cache video chunks)
```

**3. Video Encoding Pipeline:**
```
Upload MP4 → Transcode (FFmpeg) → Multiple bitrates → Chunk (HLS/DASH) → CDN
```

---

### 4.4. Uber Ride Matching

#### **Requirements:**
- Match rider với driver gần nhất trong < 5s.
- Scale: 10M drivers online, 100k matches/minute.

#### **Core: Geospatial Indexing**

**QuadTree:**
```
           ┌─────────────┐
           │   World     │
           └──────┬──────┘
                  │
     ┌────────────┼────────────┐
     ▼            ▼            ▼
┌─────────┐  ┌─────────┐  ┌─────────┐
│  NW     │  │   NE    │  │  SW     │
└─────────┘  └─────────┘  └─────────┘
```

**Algorithm:**
1. Rider request ở location (lat, lng).
2. QuadTree tìm drivers trong bán kính 5km.
3. Rank drivers (khoảng cách, rating).
4. Send request đến top 3 drivers.

**Database:**
- **Redis Geo:** `GEOADD drivers:online [lng] [lat] [driver_id]`.
- **Query:** `GEORADIUS drivers:online [lng] [lat] 5 km`.

---

### 4.5. WhatsApp/Chat System

#### **Requirements:**
- Real-time messaging.
- Read receipts, typing indicators.
- Scale: 2B users, 100B messages/day.

#### **Architecture:**
```
┌────────┐  WebSocket  ┌─────────────┐  AMQP   ┌────────────┐
│ Client │────────────>│ Chat Server │────────>│ RabbitMQ   │
└────────┘             └─────────────┘         └──────┬─────┘
                                                       │
                                              ┌────────▼────────┐
                                              │ Message Storage │
                                              │  (Cassandra)    │
                                              └─────────────────┘
```

**Flow:**
1. User A gửi tin → Chat Server (WebSocket).
2. Server → Đẩy vào Queue với `recipient_id`.
3. Worker consume queue → Check User B online?
   - Online: Push qua WebSocket.
   - Offline: Store in DB, send push notification.

**Database Schema (Cassandra):**
```sql
CREATE TABLE messages (
  conversation_id UUID,
  timestamp TIMESTAMP,
  sender_id UUID,
  message TEXT,
  PRIMARY KEY (conversation_id, timestamp)
) WITH CLUSTERING ORDER BY (timestamp DESC);
```

---

### 4.6. Rate Limiter

#### **Requirements:**
- Limit: 100 requests/minute per user.

#### **Algorithm: Token Bucket**

**Concept:**
- Bucket có capacity = 100 tokens.
- Mỗi giây thêm 100/60 ≈ 1.67 tokens.
- Mỗi request tiêu thụ 1 token.
- Bucket đầy → Không thêm tokens.

**Code (Redis + Lua):**
```typescript
async function isAllowed(userId: string): Promise<boolean> {
  const key = `rate_limit:${userId}`;
  const limit = 100;
  const window = 60; // seconds
  
  const luaScript = `
    local key = KEYS[1]
    local limit = tonumber(ARGV[1])
    local window = tonumber(ARGV[2])
    local current = redis.call('GET', key)
    
    if current and tonumber(current) >= limit then
      return 0
    else
      redis.call('INCR', key)
      redis.call('EXPIRE', key, window)
      return 1
    end
  `;
  
  const result = await redis.eval(luaScript, 1, key, limit, window);
  return result === 1;
}
```

---

## 5. Performance & Optimization

### 5.1. Profiling Tools

**Database:**
- `EXPLAIN ANALYZE` (PostgreSQL): Xem query plan.
- Slow Query Log (MySQL).

**Application:**
- **Node.js:** `clinic`, `0x` (flame graphs).
- **C#:** Visual Studio Profiler, dotTrace.

---

### 5.2. Metrics to Monitor

**Golden Signals (Google SRE):**
1. **Latency:** P50, P95, P99.
2. **Traffic:** Requests per second.
3. **Errors:** 5xx error rate.
4. **Saturation:** CPU, Memory, Disk usage.

**Tools:** Prometheus + Grafana, Datadog.

---

## 6. Interview Framework (Khung phỏng vấn)

### 4-Step Approach:

**Step 1: Clarify Requirements (5 phút)**
```
Q: "Design Instagram"
A: "Clarifying questions:
   - Scope: Just photo upload/feed? Or Stories/DM?
   - Scale: How many users? Photos per day?
   - Features: Filters? Recommendations?"
```

**Step 2: Capacity Estimation (5 phút)**
```
- 500M users, 10% DAU = 50M DAU
- Average 2 photos/user/day = 100M photos/day
- Photo size: 2MB → 200TB/day storage
- CDN bandwidth: 200TB * 8 / 86400s ≈ 18Gbps
```

**Step 3: High-level Design (10 phút)**
Draw diagram với major components.

**Step 4: Deep Dive (20 phút)**
- Database schema.
- API endpoints.
- Trade-offs discussion.

---

## 7. Hands-on Projects

### Project 1: Mini URL Shortener
**Tech:** Node.js + Redis + PostgreSQL  
**Features:** Shorten URL, Redirect, Analytics (click count).

### Project 2: Rate Limiter Middleware
**Tech:** Express.js + Redis  
**Algorithm:** Token Bucket hoặc Sliding Window.

### Project 3: Real-time Chat
**Tech:** Socket.io + Redis Pub/Sub + MongoDB  
**Features:** 1-1 chat, typing indicator, read receipts.

---

## 8. Resources

### **Books (Must Read)**
1. **"Designing Data-Intensive Applications"** - Martin Kleppmann  
   *Kinh thánh về Distributed Systems.*
2. **"System Design Interview Vol 1 & 2"** - Alex Xu  
   *Sách tốt nhất cho interview prep.*
3. **"Building Microservices"** - Sam Newman

### **Courses**
- **MIT 6.824: Distributed Systems** (Free on YouTube)
- **Grokking the System Design Interview** (educative.io)
- **ByteByteGo** (YouTube channel - Visual explanations)

### **Websites**
- [System Design Primer](https://github.com/donnemartin/system-design-primer) (GitHub)
- [High Scalability](http://highscalability.com/) (Blog)
- [AWS Architecture Center](https://aws.amazon.com/architecture/)

---

## 🎯 Kết luận

System Design không phải về việc "thuộc" câu trả lời, mà là **process**:
1. Hiểu requirements.
2. Break down problem.
3. Trade-offs discussion.
4. Iterate and improve.

**Practice:** Mỗi tuần design 1 system mới. Sau 3 tháng, bạn sẽ tự tin phỏng vấn bất kỳ company nào! 🚀
