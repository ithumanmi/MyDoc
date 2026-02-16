# 👑 Roadmap to Senior Game Server Engineer

> [← Back to Game Server Guide](./game-server-guide.md) | [← Back to Game Dev Roadmap](./README.md) | [Home](../../README.md)

Lộ trình chi tiết từ Junior đến Senior trong lĩnh vực Game Server/Multiplayer Engineering.

---

## 📊 Tổng quan: Junior vs Mid vs Senior

| Tiêu chí | 🟢 Junior (0-2 năm) | 🟡 Mid-level (2-5 năm) | 🔴 Senior (5+ năm) |
|----------|---------------------|------------------------|-------------------|
| **Kiến thức kỹ thuật** | Biết dùng Unity Netcode/Mirror, hiểu RPC cơ bản | Hiểu sâu về Prediction/Reconciliation, tự implement netcode | Master Distributed Systems, thiết kế protocol riêng |
| **Ngôn ngữ** | C# (Unity) | C# + Node.js/Go (Backend API) | C#/C++ + Go/Rust (Performance critical) |
| **DevOps** | Deploy lên VPS đơn giản | Docker, K8s cơ bản, CI/CD | Architect toàn bộ infra (Auto-scaling, Multi-region) |
| **Database** | Biết query SQL cơ bản | Index, Sharding, Redis patterns | Database architecture, Replication strategies |
| **Trách nhiệm** | Fix bug, implement feature theo spec | Thiết kế hệ thống nhỏ, mentor junior | Lead architecture, quyết định tech stack, review team |
| **Kinh nghiệm** | Game 10-50 CCU | Game 500-5000 CCU, xử lý incidents | Game 50k+ CCU, survive launch day chaos |
| **Mức lương (VN)** | $800-$1500 | $1500-$3000 | $3000-$6000+ |
| **Mức lương (Global Remote)** | $2000-$4000 | $4000-$8000 | $8000-$15000+ |

---

## 🎯 SENIOR GAME SERVER ENGINEER - Kỹ năng cần có

### 1. Kiến thức nền tảng vững chắc (Deep Fundamentals)

#### **A. Computer Science Hardcore**

**Networking (Tầng thấp):**
*   Hiểu rõ **TCP/IP Stack** (Layer 2-4): Ethernet Frame, IP Packet, TCP Segment.
*   **Blocking I/O vs Non-blocking I/O:** 
    *   Unix: `select()`, `epoll()`, `kqueue()`
    *   Windows: IOCP (I/O Completion Ports)
*   **QUIC Protocol:** HTTP/3 for games (Giảm latency, tốt hơn TCP trong môi trường mobile).
*   **NAT Traversal:** STUN, TURN, ICE (Quan trọng cho P2P games).

**Distributed Systems Theory:**
*   **CAP Theorem:** 
    *   Consistency: Tất cả nodes thấy data giống nhau.
    *   Availability: Mọi request đều nhận response.
    *   Partition Tolerance: Hệ thống hoạt động dù mạng bị chia cắt.
    *   *Game Server phải chọn: CP (Consistency + Partition) hay AP (Availability + Partition)?*
*   **Consensus Algorithms:**
    *   Raft, Paxos (Dùng khi cần sync state giữa nhiều server).
    *   Leaderless Replication (Cassandra, DynamoDB).
*   **Event Sourcing & CQRS:**
    *   Lưu Events thay vì State (VD: "Player A dealt 50 damage" thay vì "HP = 50").
    *   Replay events để recover khi crash.

**Algorithms & Data Structures:**
*   **Spatial Partitioning:**
    *   QuadTree (2D), Octree (3D): Tìm players gần nhau để sync.
    *   Interest Management: Chỉ gửi update cho players trong tầm nhìn.
*   **Lock-free Data Structures:** Concurrent Queue, Ring Buffer (Tránh lock contention trong multi-threading).
*   **Bloom Filters:** Kiểm tra "username có tồn tại?" nhanh mà không query DB.

#### **B. Backend Engineering (Meta-game)**

**Database chuyên sâu:**
*   **SQL Mastery:**
    *   Query Optimization: EXPLAIN ANALYZE, Index types (B-Tree, Hash).
    *   Transactions: ACID, Isolation Levels (Read Committed, Serializable).
    *   Sharding: Horizontal Partitioning (VD: User ID % 10 → 10 shards).
*   **NoSQL Patterns:**
    *   MongoDB: Document modeling, Denormalization.
    *   DynamoDB: Partition Key design, GSI (Global Secondary Index).
*   **Redis Advanced:**
    *   Pub/Sub cho Real-time messaging.
    *   Lua scripting cho Atomic operations.
    *   Redis Cluster (Sharding + Replication).

**API Design:**
*   **REST:** Idempotency, Versioning (`/v1/users`).
*   **gRPC:** Protocol Buffers (Binary, nhanh hơn JSON 3-5 lần).
*   **GraphQL:** Flexible queries, tránh Over-fetching.

---

### 2. Kỹ năng chuyên môn sâu (Deep Technical Skills)

#### **A. Performance Engineering**

Senior không chỉ làm "nó chạy", mà làm "nó chạy **nhanh**".

**Profiling & Optimization:**
*   **Tools:**
    *   Unity Profiler: CPU, Memory, Rendering.
    *   Rider Memory Profiler: Tìm Memory Leaks.
    *   Linux `perf`, `flamegraph`: Tìm CPU bottleneck.
    *   Wireshark: Analyze network packets.
*   **Metrics:**
    *   Tick Rate: Server xử lý được bao nhiêu frames/giây? (Target: 60Hz)
    *   Latency: P50, P95, P99 (Không chỉ nhìn Average).
    *   Throughput: Requests/second.

**Memory Management:**
*   **GC (Garbage Collector):**
    *   Hiểu Gen0, Gen1, Gen2 trong .NET.
    *   Minimize allocations: Dùng `Span<T>`, `ArrayPool<T>`.
*   **Object Pooling mọi thứ:**
    *   Không chỉ Bullets, mà cả Packets, Events, Temporary Collections.
*   **Memory Leaks:**
    *   Event subscriptions không unsubscribe.
    *   Static references giữ objects.

**Concurrency:**
*   **Multi-threading:**
    *   Khi nào dùng `async/await` vs `Task.Run()`?
    *   Data Races, Deadlocks: Dùng `lock`, `Semaphore`, `Mutex` đúng cách.
*   **Unity Job System & Burst Compiler:**
    *   DOTS (Data-Oriented Technology Stack) cho performance cực đỉnh.

#### **B. Security & Anti-Cheat**

**Server-side Validation (Must):**
*   **Never Trust Client:**
    *   Client: "Tao ở vị trí (100, 0, 0)".
    *   Server: "Cái lồn! Lần trước mày ở (0,0,0), giờ teleport 100m trong 1 frame? BAN!"
*   **Validate Everything:**
    *   Position: Speed check (`distance/deltaTime > maxSpeed`).
    *   Damage: "Súng này chỉ gây 10 damage, sao client báo 100?"
    *   Items: "Mày có key để mở cái chest này không?"

**Advanced Techniques:**
*   **Packet Encryption:**
    *   AES-256, ChaCha20 (Ngăn packet sniffing).
*   **DDoS Mitigation:**
    *   Rate Limiting: Max 100 requests/giây/IP.
    *   Cloudflare, AWS Shield.
*   **Behavioral Analysis:**
    *   Machine Learning: Phát hiện bot qua click pattern, movement pattern.
    *   Heuristics: Aimbot detection (Headshot rate > 90% = suspicious).

---

### 3. Kinh nghiệm thực chiến (Battle-tested Experience)

Senior = Người đã "chết" nhiều lần và học được từ sai lầm.

#### **A. "Chiến tranh" Production (Launch Day Hell)**

**Scenario 1: Server Crash 5 phút sau Launch**
*   **Tình huống:** Game ra mắt, 10,000 người vào cùng lúc → Server RAM đầy, CPU 100%, crash.
*   **Nguyên nhân:** Không Load Testing trước.
*   **Học được:**
    *   Dùng JMeter, Locust simulate 20k concurrent users.
    *   Vertical scaling (RAM, CPU) + Horizontal scaling (Thêm server).

**Scenario 2: Memory Leak**
*   **Tình huống:** Server chạy 2 giờ là RAM đầy, phải restart.
*   **Nguyên nhân:** Event subscription không unsubscribe, List không clear.
*   **Học được:**
    *   Profile memory trong 24h liên tục.
    *   Code review: Kiểm tra mọi `+=` event phải có `-=`.

**Scenario 3: Database Deadlock**
*   **Tình huống:** 2 transactions khóa nhau → Server đơ, timeout.
*   **Nguyên nhân:** 
    *   Transaction A: Lock Table Users → Lock Table Inventory.
    *   Transaction B: Lock Table Inventory → Lock Table Users.
*   **Học được:**
    *   Đặt timeout cho transactions.
    *   Retry logic với Exponential Backoff.
    *   Lock Order: Luôn lock theo thứ tự cố định.

**Scenario 4: DDoS Attack**
*   **Tình huống:** Hacker flood server bằng 100k UDP packets/giây.
*   **Học được:**
    *   Rate Limiting per IP.
    *   Firewall rules (iptables).
    *   CDN (Cloudflare) để filter traffic.

#### **B. Scaling: 100 CCU → 100,000 CCU**

**Phase 1: Single Server (0-100 CCU)**
*   1 server chạy tất cả: Game Logic + Database + Web API.
*   Chi phí: $20/tháng VPS.

**Phase 2: Separate Database (100-1000 CCU)**
*   Game Server riêng + Database Server riêng.
*   Lý do: Database queries blocking game loop.

**Phase 3: Horizontal Scaling (1000-10,000 CCU)**
*   Nhiều Game Servers + Load Balancer.
*   Stateless Servers: Session lưu Redis, không lưu RAM.
*   Database Replication: Master (Write) + Slaves (Read).

**Phase 4: Microservices (10k-100k CCU)**
*   Tách thành services nhỏ:
    *   **Auth Service** (Login, JWT).
    *   **Matchmaking Service** (Redis Queue).
    *   **Game Server Pool** (K8s manages).
    *   **Leaderboard Service** (Redis Sorted Set).
*   Communication: gRPC hoặc Message Queue (RabbitMQ, Kafka).

#### **C. Cross-team Collaboration**

Senior phải làm việc với nhiều teams:
*   **Game Designer:**
    *   "Feature PvP 1000v1000 này làm server phải handle bao nhiêu packets/giây?"
    *   "Không, feature này sẽ crash server. Giảm xuống 100v100."
*   **Client Engineer:**
    *   "Sao packet lại 2000 bytes? Network bandwidth tốn quá! Compress xuống 200 bytes."
*   **DevOps:**
    *   "Setup monitoring cho CCU, Latency P95, Server CPU."

---

### 4. Soft Skills (Quan trọng không kém Technical)

#### **A. System Design**

Khi PM hỏi: **"Làm Battle Royale 100 người như thế nào?"**

Senior phải vẽ được kiến trúc:

```
┌─────────────────────────────────────────────────────────┐
│                    CLIENT (Unity)                        │
└────────────────┬────────────────────────────────────────┘
                 │
                 ▼
         ┌───────────────┐
         │  Gateway/LB   │ (Nginx, HAProxy)
         └───────┬───────┘
                 │
       ┌─────────┴─────────┐
       ▼                   ▼
┌──────────────┐    ┌──────────────┐
│ Matchmaking  │    │   Auth API   │ (Node.js)
│   Service    │    └──────────────┘
│   (Redis)    │
└──────┬───────┘
       │
       ▼
┌──────────────────────┐
│  Game Server Pool    │ (Unity Headless + Agones/K8s)
│  (Dedicated Servers) │
└──────┬───────────────┘
       │
       ▼
┌──────────────────────────────────────┐
│  Postgres   MongoDB    Redis         │
│  (Account)  (Inventory)(Session/Cache)│
└──────────────────────────────────────┘
```

**Giải thích:**
1. Client connect → Gateway load balance.
2. Matchmaking Service tìm phòng phù hợp (Skill, Region).
3. Spin up Dedicated Game Server (K8s allocate pod).
4. 100 clients connect vào Game Server.
5. Game Server ghi kết quả xuống DB.

#### **B. Mentorship (Đào tạo Junior)**

*   **Code Review:**
    *   "Đoạn này sao lại dùng `foreach` trong `Update()`? Allocate GC đấy! Dùng `for` loop."
    *   "Function này 200 dòng, refactor thành 5 functions nhỏ đi."
*   **Viết Documentation:**
    *   "Coding Conventions cho Game Server team."
    *   "How to debug production issues."
*   **Knowledge Sharing:**
    *   Tech talk hàng tuần: "Cách tối ưu bandwidth."

#### **C. Incident Response (Xử lý khủng hoảng)**

**3h sáng, server sập:**
1.  **Keep Calm:** Đọc logs, monitoring dashboard.
2.  **Identify Root Cause:** 
    *   CPU 100%? Memory leak? Database timeout?
3.  **Quick Fix:**
    *   Restart server (tạm thời).
    *   Rollback deploy nếu bug từ release mới.
4.  **Long-term Fix:**
    *   Fix bug.
    *   Thêm test case.
    *   Viết **Post-mortem Report:**
        *   Tại sao sập?
        *   Impact: Bao nhiêu users bị ảnh hưởng?
        *   Action items: Làm gì để không tái diễn?

---

## 📚 Tài nguyên học để lên Senior

### **Books (Must Read)**

1.  **"Designing Data-Intensive Applications"** - Martin Kleppmann
    *   Kinh thánh về Backend, Database, Distributed Systems.
    *   Nội dung: Replication, Partitioning, Transactions, Consistency.
    
2.  **"Game Engine Architecture"** - Jason Gregory
    *   Hiểu engine sâu hơn, không chỉ dùng Unity như black box.
    *   Nội dung: Rendering, Physics, Animation, Networking.
    
3.  **"Multiplayer Game Programming"** - Joshua Glazer
    *   Networking cho games từ A-Z.
    
4.  **"Systems Performance"** - Brendan Gregg
    *   Linux performance tuning, profiling.

### **Courses**

*   **MIT 6.824: Distributed Systems** (Free trên YouTube)
    *   Lectures + Labs (Build Raft, MapReduce).
*   **Grokking the System Design Interview** (educative.io)
    *   Design Twitter, Uber, Netflix.
*   **Unity Multiplayer Networking** (Unity Learn Premium)

### **Real-world Practice**

*   **Contribute Open Source:**
    *   Mirror Networking (Fix bugs, add features).
    *   Unity Netcode for GameObjects.
*   **Read Production Code:**
    *   Unreal Engine source code (C++).
    *   Photon Server SDK.
*   **Build Side Projects:**
    *   Clone game .io nhỏ (Agar.io, Slither.io).
    *   Tự implement protocol từ scratch (Không dùng Unity Netcode).

---

## 🗺️ Roadmap cụ thể: Junior → Senior (5 năm)

### **Năm 1-2: Junior Game Server Engineer**

**Mục tiêu:** Nền tảng vững, làm quen production.

**Checklist:**
- [ ] **Projects:**
  - [ ] Làm 2-3 game Multiplayer nhỏ (10-50 CCU).
  - [ ] 1 game publish lên Steam hoặc Mobile.
- [ ] **Kỹ năng:**
  - [ ] Thành thạo Unity Netcode hoặc Mirror.
  - [ ] Hiểu RPC, NetworkVariable, ClientServerModel.
  - [ ] Biết deploy lên VPS (DigitalOcean, Vultr).
- [ ] **Học tập:**
  - [ ] Đọc xong "Multiplayer Game Programming".
  - [ ] Xem hết Unity Multiplayer tutorials.

---

### **Năm 3-4: Mid-level Game Server Engineer**

**Mục tiêu:** Tự chủ, handle complexity.

**Checklist:**
- [ ] **Projects:**
  - [ ] Làm 1 game 500-1000 CCU, survive Launch Day.
  - [ ] Xử lý được ít nhất 1 production incident (Crash/Leak).
- [ ] **Kỹ năng:**
  - [ ] Học Node.js/Go, làm backend API riêng (Login, Leaderboard).
  - [ ] Setup CI/CD Pipeline (GitHub Actions).
  - [ ] Docker, Kubernetes cơ bản.
  - [ ] Database Optimization (Index, Query tuning).
- [ ] **Học tập:**
  - [ ] Đọc "Designing Data-Intensive Applications" (Ít nhất 50%).
  - [ ] Học Redis advanced (Pub/Sub, Lua).
  - [ ] System Design: Practice 10 bài trên Leetcode/Pramp.

---

### **Năm 5+: Senior Game Server Engineer**

**Mục tiêu:** Lead, Architect, Mentor.

**Checklist:**
- [ ] **Projects:**
  - [ ] Lead architecture cho 1 game lớn (10k+ CCU).
  - [ ] Thiết kế Multi-region Infrastructure.
  - [ ] Viết Custom Protocol (không dùng Unity Netcode nữa).
- [ ] **Kỹ năng:**
  - [ ] Master Kubernetes (Auto-scaling, Rolling updates).
  - [ ] Performance tuning: Giảm latency từ 100ms xuống 30ms.
  - [ ] Security: Implement anti-cheat system.
  - [ ] Monitoring: Setup Grafana + Prometheus dashboard.
- [ ] **Leadership:**
  - [ ] Mentor 2-3 Junior/Mid engineers.
  - [ ] Conduct 50+ code reviews.
  - [ ] Present 5+ tech talks.
- [ ] **Học tập:**
  - [ ] Đọc xong "Designing Data-Intensive Applications".
  - [ ] Hoàn thành MIT 6.824 course.
  - [ ] Contribute 10+ PRs vào Open Source projects.

---

## 🎯 Interview Questions cho Senior

Khi phỏng vấn vị trí Senior, expect những câu hỏi này:

**System Design:**
*   "Thiết kế hệ thống Matchmaking cho MOBA (LoL, Dota)."
*   "Làm thế nào để server handle 1 triệu concurrent connections?"

**Performance:**
*   "Server bị lag khi có 100 người cùng bắn. Debug như thế nào?"
*   "Giải thích Garbage Collection hoạt động thế nào trong C#?"

**Distributed Systems:**
*   "CAP Theorem là gì? Game server nên chọn CP hay AP?"
*   "Eventual Consistency vs Strong Consistency, khi nào dùng cái nào?"

**Behavioral:**
*   "Kể về lần server sập production và bạn xử lý thế nào?"
*   "Conflict với teammate về tech decision, bạn giải quyết ra sao?"

---

## 💰 Mức lương kỳ vọng

**Việt Nam:**
*   Junior: $800-$1500/tháng
*   Mid: $1500-$3000/tháng
*   Senior: $3000-$6000/tháng
*   Staff/Principal: $6000-$10000/tháng

**Global Remote (Làm cho công ty US/EU):**
*   Junior: $2000-$4000/tháng
*   Mid: $4000-$8000/tháng
*   Senior: $8000-$15000/tháng
*   Staff/Principal: $15000-$25000/tháng

---

## 🚀 Kết luận

Lên Senior không chỉ là "code giỏi", mà là:
*   **Kiến thức sâu:** Hiểu từng layer của hệ thống.
*   **Kinh nghiệm:** Đã "chết" và học từ sai lầm.
*   **Leadership:** Mentor, dẫn dắt team.
*   **Business Sense:** Hiểu impact của tech decision lên product.

**Chúc bạn thành công trên con đường lên Senior! 🎮**
