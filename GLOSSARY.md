# 📖 Master Glossary - Từ điển thuật ngữ A-Z

> [← Back to Home](./README.md) | [Quick Start Guide](./QUICK-START.md)

**Tra cứu nhanh 100+ khái niệm quan trọng** trong repository này. Mỗi thuật ngữ có:
- ✅ Định nghĩa ngắn gọn (1-2 câu)
- 📍 Link đến guide chi tiết (nếu có)
- 🏷️ Tags: Domain liên quan

**Cách dùng:** `Ctrl/Cmd + F` để tìm kiếm.

---

## A

### **ACID (Database Transactions)** 🗄️
*Tags: #Backend #Database*

Bộ 4 thuộc tính đảm bảo database transactions an toàn:
- **Atomicity**: All or nothing (Tất cả hoặc không gì)
- **Consistency**: Valid state (Trạng thái hợp lệ)
- **Isolation**: Concurrent transactions không conflict
- **Durability**: Committed data survives crashes

📖 Chi tiết: [Database Fundamentals](./domains/backend-dev/database-fundamentals.md)

---

### **Adaptive Bitrate Streaming** 📹
*Tags: #Backend #SystemDesign*

Kỹ thuật streaming video tự động điều chỉnh chất lượng dựa trên bandwidth của user. Netflix, YouTube dùng để tránh buffering.

📖 Chi tiết: [System Design Case Studies](./domains/backend-dev/system-design/case-studies.md)

---

### **API (Application Programming Interface)** 🔌
*Tags: #Backend #WebDev*

Interface cho phép applications communicate với nhau. RESTful API dùng HTTP methods (GET, POST, PUT, DELETE) và JSON format.

📖 Chi tiết: [API Design Guide](./domains/backend-dev/api-design-guide.md)

---

### **Anti-Slip System** 🛡️
*Tags: #Growth #Habits*

Hệ thống phòng ngừa việc bỏ cuộc giữa chừng khi học kỹ năng mới. Bao gồm: Accountability, Progress tracking, Habit stacking, Emergency protocols.

📖 Chi tiết: [Anti-Slip System](./guides/growth/anti-slip-system.md) ⭐ **Must Read**

---

### **Authentication vs Authorization** 🔐
*Tags: #Security #Backend*

- **Authentication**: "Bạn là ai?" (Login, verify identity)
- **Authorization**: "Bạn có quyền làm gì?" (Permissions, roles)

📖 Chi tiết: [Backend Security](./domains/backend-dev/backend-security.md)

---

### **Autoscaling** 📈
*Tags: #DevOps #Cloud*

Tự động tăng/giảm số instances dựa trên traffic. VD: Black Friday traffic tăng 5x → Auto scale từ 5 → 25 servers → Sau đó scale down.

📖 Chi tiết: [System Design Guide](./domains/backend-dev/system-design-guide.md)

---

## B

### **Behavioral Economics** 🧠
*Tags: #Investing #Psychology*

Nghiên cứu về tâm lý và thiên kiến ảnh hưởng đến quyết định tài chính. VD: Loss aversion (Sợ lỗ hơn thích lời), FOMO, Herding behavior.

📖 Chi tiết: [Behavioral Economics](./guides/investing/advanced/behavioral-economics.md)

---

### **Burnout** 🔥
*Tags: #WellBeing #Mental*

Trạng thái kiệt sức thể chất và tinh thần do stress kéo dài. 3 giai đoạn: Honeymoon → Onset of Stress → Chronic Burnout → Crisis.

📖 Chi tiết: [Burnout Prevention](./guides/well-being/mental-resilience/burnout-prevention.md) ⭐ **Must Read**

---

## C

### **Caching** 💾
*Tags: #Backend #Performance*

Lưu trữ data thường xuyên truy cập ở memory (Redis) thay vì query database mỗi lần. Giảm latency từ 100ms → 1ms.

📖 Chi tiết: [Backend Performance](./domains/backend-dev/monitoring-observability.md)

---

### **CAP Theorem** ⚖️
*Tags: #DistributedSystems #Backend*

Distributed system chỉ đạt được 2/3:
- **C**onsistency (Nhất quán)
- **A**vailability (Sẵn sàng)
- **P**artition tolerance (Chịu lỗi mạng)

VD: MongoDB (CP), Cassandra (AP).

📖 Chi tiết: [Distributed Systems](./domains/backend-dev/architecture/distributed-systems.md)

---

### **CI/CD (Continuous Integration/Continuous Deployment)** ♾️
*Tags: #DevOps #Backend*

- **CI**: Tự động test code mỗi lần commit
- **CD**: Tự động deploy lên production khi pass tests

📖 Chi tiết: [Deployment Guide](./domains/backend-dev/deployment-guide.md)

---

### **Core Skill (T-Shaped)** 🎯
*Tags: #Career #Growth*

Model kỹ năng chữ T:
- **Vertical (Depth)**: 1 skill cực sâu (World-class level)
- **Horizontal (Breadth)**: Nhiều skills cơ bản (Competent level)

Top 1% Engineers có Core Skill rõ ràng + Supporting skills.

📖 Chi tiết: [Becoming Top 1%](./guides/growth/becoming-top-1-percent.md)

---

### **CRUD Operations** 📝
*Tags: #Backend #Database*

4 thao tác cơ bản với data:
- **C**reate (INSERT)
- **R**ead (SELECT)
- **U**pdate (UPDATE)
- **D**elete (DELETE)

📖 Chi tiết: [Database Fundamentals](./domains/backend-dev/database-fundamentals.md)

---

## D

### **Database Index** 📇
*Tags: #Backend #Database*

Data structure (B-Tree) tăng tốc query bằng cách tạo "mục lục" cho columns. Trade-off: Faster reads, slower writes.

📖 Chi tiết: [Database Fundamentals](./domains/backend-dev/database-fundamentals.md)

---

### **Deep Work** 🎯
*Tags: #Productivity #Focus*

Làm việc tập trung tuyệt đối không distraction. 4 giờ deep work = 3 ngày làm việc bình thường. Cal Newport's framework.

📖 Chi tiết: [Deep Work Mastery](./guides/productivity/core-skills/deep-work-mastery.md)

---

### **Deliberate Practice** 🎯
*Tags: #Learning #Growth*

Luyện tập có chủ đích với feedback loops. Khác với "practice mindlessly". 3 yếu tố: Specific goal, Immediate feedback, Slightly beyond comfort zone.

📖 Chi tiết: [Chương 2: Luyện tập có chủ đích](./chapters/02-luyen-tap-co-chu-dich.md)

---

### **Dopamine System** 🧠
*Tags: #WellBeing #Biohacking*

Neurotransmitter điều khiển động lực, kỷ luật, focus. Optimize bằng: Cold exposure, Exercise, Dopamine detox (tránh quick hits từ social media).

📖 Chi tiết: [Dopamine System](./guides/well-being/biohacking/dopamine-system.md)

---

## E

### **Eisenhower Matrix** 📊
*Tags: #Productivity #TimeManagement*

Framework phân loại tasks:
- **Urgent + Important**: Do first
- **Not Urgent + Important**: Schedule
- **Urgent + Not Important**: Delegate
- **Not Urgent + Not Important**: Eliminate

📖 Chi tiết: [Quản lý thời gian](./chapters/06-quan-ly-thoi-gian.md)

---

### **Event-Driven Architecture** 📡
*Tags: #Backend #Architecture*

Hệ thống giao tiếp qua events thay vì direct calls. Services publish events → Other services subscribe → Loosely coupled.

📖 Chi tiết: [Microservices Patterns](./domains/backend-dev/architecture/microservices-patterns-deep-dive.md)

---

## F

### **Feedback Loop** 🔄
*Tags: #Growth #Learning*

Chu trình: Action → Measure → Learn → Adjust → Repeat. "You can't improve what you don't measure."

📖 Chi tiết: [Chương 4: Đo lường & Phản hồi](./chapters/04-do-luong-phan-hoi.md)

---

### **Flow State** 🌊
*Tags: #Productivity #Performance*

Trạng thái tập trung cao độ, mất cảm giác thời gian. Mihaly Csikszentmihalyi: "Challenge slightly beyond skill level."

📖 Chi tiết: [High Performance & Flow](./guides/well-being/high-performance.md)

---

## G

### **Game Theory** 🎮
*Tags: #Strategy #DecisionMaking*

Nghiên cứu ra quyết định chiến lược khi kết quả phụ thuộc vào người khác. Nash Equilibrium, Prisoner's Dilemma, Zero-sum games.

📖 Chi tiết: 
- [Game Theory Fundamentals](./guides/growth/game-theory.md)
- [Game Theory for Engineers](./guides/growth/game-theory-for-engineers.md)

---

### **Glucose & Insulin System** 🩸
*Tags: #WellBeing #Biohacking*

Quản lý năng lượng: Tránh glucose spikes (carbs đơn) → Ổn định insulin → Sustained energy cả ngày. CGM tracking.

📖 Chi tiết: [Glucose & Insulin System](./guides/well-being/biohacking/glucose-insulin-system.md)

---

### **gRPC** ⚡
*Tags: #Backend #API*

Google Remote Procedure Call - Protocol nhanh hơn REST (binary format, HTTP/2). Dùng cho microservices communication.

📖 Chi tiết: [API Design Guide](./domains/backend-dev/api-design-guide.md)

---

## H

### **Health OS** 🧬
*Tags: #WellBeing #Biohacking*

Framework debug cơ thể như debug code. Track: Dopamine, Glucose, Testosterone, Cortisol, Sleep, Movement.

📖 Chi tiết: [Health OS Overview](./guides/well-being/biohacking/health-os-overview.md) ⭐ **Unique**

---

### **Hexagonal Architecture** 💠
*Tags: #Backend #Architecture*

"Ports and Adapters" - Business logic độc lập với infrastructure. Easy to test, swap databases/frameworks.

📖 Chi tiết: [Hexagonal Architecture](./domains/backend-dev/architecture/hexagonal-architecture.md)

---

### **HTTP Status Codes** 📡
*Tags: #Backend #API*

- **2xx**: Success (200 OK, 201 Created)
- **4xx**: Client Error (400 Bad Request, 401 Unauthorized, 404 Not Found)
- **5xx**: Server Error (500 Internal Server Error, 503 Service Unavailable)

📖 Chi tiết: [API Design Guide](./domains/backend-dev/api-design-guide.md)

---

## I

### **Indie Hacker** 💼
*Tags: #Entrepreneurship #SideIncome*

Developer build & launch products solo/small team. Focus: Bootstrap, MRR (Monthly Recurring Revenue), Passive income.

📖 Chi tiết: [Indie Hacker Roadmap](./guides/career/indie-hacker-roadmap.md)

---

## J

### **JWT (JSON Web Token)** 🎫
*Tags: #Security #Backend*

Token format cho authentication. Structure: Header.Payload.Signature. Client lưu token, gửi trong `Authorization: Bearer <token>`.

📖 Chi tiết: [Backend Security](./domains/backend-dev/backend-security.md)

---

## K

### **Kubernetes (K8s)** ☸️
*Tags: #DevOps #Cloud*

Container orchestration platform. Auto-scaling, self-healing, rolling updates. Industry standard for microservices.

📖 Chi tiết: [Docker & K8s Guide](./domains/backend-dev/devops-sre/docker-k8s-guide.md)

---

## L

### **Life OS Framework** 🧠
*Tags: #Growth #SystemsThinking*

Hệ điều hành cuộc đời - 4 tầng: Hardware (Body), OS (Mind), Apps (Skills), Data (Knowledge). Optimize từng layer.

📖 Chi tiết: [Life OS Framework](./guides/growth/life-os-framework.md) ⭐ **Must Read**

---

### **Load Balancing** ⚖️
*Tags: #Backend #Scalability*

Phân phối requests đến multiple servers. Algorithms: Round Robin, Least Connections, IP Hash. Tools: Nginx, HAProxy.

📖 Chi tiết: [System Design Guide](./domains/backend-dev/system-design-guide.md)

---

## M

### **Macroeconomics** 🌍
*Tags: #Investing #Economics*

Kinh tế vĩ mô: GDP, Lạm phát, Lãi suất, Chu kỳ kinh tế. Ảnh hưởng đến investment strategy (Bull vs Bear markets).

📖 Chi tiết: [Macroeconomics](./guides/investing/advanced/macroeconomics.md)

---

### **Message Queue** 📬
*Tags: #Backend #Architecture*

Hàng đợi xử lý async tasks. Producer đẩy jobs → Queue → Consumer lấy ra. Tools: RabbitMQ, Kafka, Redis Queue.

📖 Chi tiết: [System Design Guide](./domains/backend-dev/system-design-guide.md)

---

### **Microeconomics** 🏪
*Tags: #Investing #Economics*

Kinh tế vi mô: Cung cầu, Định giá, Hành vi tiêu dùng. Apply vào career (Bạn = Product, Skills = Value proposition).

📖 Chi tiết: [Microeconomics](./guides/investing/advanced/microeconomics.md)

---

### **Microservices** 🧩
*Tags: #Backend #Architecture*

Chia application thành nhiều services nhỏ độc lập. Ưu điểm: Scale riêng, Deploy riêng. Nhược điểm: Phức tạp hơn.

📖 Chi tiết: [Microservices Patterns](./domains/backend-dev/architecture/microservices-patterns-deep-dive.md)

---

### **Middleware** ⚙️
*Tags: #Backend #API*

Functions chạy giữa request và response. Use cases: Logging, Auth check, Parse body, CORS, Error handling.

📖 Chi tiết: [API Design Guide](./domains/backend-dev/api-design-guide.md)

---

## N

### **Nash Equilibrium** ⚖️
*Tags: #GameTheory #Strategy*

Trạng thái mà không ai có lợi khi đổi chiến lược đơn phương. VD: Prisoner's Dilemma - Both confess là Nash Equilibrium.

📖 Chi tiết: [Game Theory](./guides/growth/game-theory.md)

---

### **NoSQL Database** 🗄️
*Tags: #Backend #Database*

Non-relational databases. Types: Document (MongoDB), Key-Value (Redis), Column (Cassandra), Graph (Neo4j). Use khi: Scale horizontal, Flexible schema.

📖 Chi tiết: [Database Fundamentals](./domains/backend-dev/database-fundamentals.md)

---

## O

### **OAuth 2.0** 🔑
*Tags: #Security #Backend*

Protocol cho authorization. "Login with Google/Facebook" - Cho phép apps truy cập data mà không chia sẻ password.

📖 Chi tiết: [OAuth 2.0 Deep Dive](./domains/backend-dev/security/oauth2-oidc-deep-dive.md)

---

### **OKR (Objectives & Key Results)** 🎯
*Tags: #Productivity #Goals*

Framework đặt mục tiêu:
- **Objective**: Mục tiêu định tính (VD: Become Backend expert)
- **Key Results**: 3 metrics đo lường (VD: Ship 5 microservices projects)

📖 Chi tiết: [OKR Planning Template](./templates/okr-planning.md)

---

### **ORM (Object-Relational Mapping)** 🔄
*Tags: #Backend #Database*

Library map giữa objects và database tables. Viết code thay vì raw SQL. VD: Prisma (Node.js), Entity Framework (C#).

📖 Chi tiết: [Database Fundamentals](./domains/backend-dev/database-fundamentals.md)

---

## P

### **Personal Brand** 🎨
*Tags: #Career #Networking*

Thương hiệu cá nhân - Để cơ hội tự tìm đến bạn. Build qua: Blog, GitHub, LinkedIn, Speaking, Mentoring.

📖 Chi tiết: [Personal Brand](./chapters/08-personal-brand.md)

---

### **Pomodoro Technique** 🍅
*Tags: #Productivity #TimeManagement*

25 phút tập trung + 5 phút nghỉ. Sau 4 Pomodoros: Nghỉ dài 15-30 phút. Giảm burnout, tăng focus.

📖 Chi tiết: [Quản lý thời gian](./chapters/06-quan-ly-thoi-gian.md)

---

## R

### **Rate Limiting** 🚦
*Tags: #Backend #Security*

Giới hạn số requests từ 1 IP/user (VD: 100 requests/phút). Prevent DDoS attacks và abuse.

📖 Chi tiết: [Backend Security](./domains/backend-dev/backend-security.md)

---

### **Redis** 💎
*Tags: #Backend #Cache*

In-memory data store. Use cases: Caching, Session storage, Pub/Sub, Rate limiting. Cực nhanh (< 1ms latency).

📖 Chi tiết: [System Design Guide](./domains/backend-dev/system-design-guide.md)

---

### **REST API** 🔄
*Tags: #Backend #API*

Representational State Transfer - Architectural style cho APIs. Principles: Stateless, Resource-based URLs, HTTP methods.

📖 Chi tiết: [API Design Guide](./domains/backend-dev/api-design-guide.md)

---

### **Reverse Proxy** 🔁
*Tags: #Backend #Infrastructure*

Server nhận requests từ clients, forward đến backend. Use cases: Load balancing, SSL termination, Caching. Tool: Nginx.

📖 Chi tiết: [System Design Guide](./domains/backend-dev/system-design-guide.md)

---

## S

### **Sharding** 🔀
*Tags: #Backend #Database*

Horizontal partitioning - Chia database thành shards (servers) dựa trên key. VD: User ID % 10 → 10 shards.

📖 Chi tiết: [Advanced DB Optimization](./domains/backend-dev/database/advanced-db-optimization.md)

---

### **SMART Goals** 🎯
*Tags: #Productivity #Goals*

Framework đặt mục tiêu hiệu quả:
- **S**pecific (Cụ thể)
- **M**easurable (Đo được)
- **A**chievable (Khả thi)
- **R**elevant (Liên quan)
- **T**ime-bound (Có deadline)

📖 Chi tiết: [Chương 1: Xác định lĩnh vực](./chapters/01-xac-dinh-linh-vuc.md)

---

### **Stoicism** 🏛️
*Tags: #Philosophy #MentalResilience*

Triết lý Khắc kỷ: Focus vào những gì control được, chấp nhận những gì không. Dichotomy of Control, Amor Fati, Memento Mori.

📖 Chi tiết: [Stoicism for Modern Life](./guides/well-being/mental-resilience/stoicism-for-modern-life.md)

---

### **System Design** 🏗️
*Tags: #Backend #Architecture*

Thiết kế hệ thống scalable. Topics: Load balancing, Caching, Database scaling, Microservices, Message queues.

📖 Chi tiết: [System Design Guide](./domains/backend-dev/system-design-guide.md)

---

### **Systems Thinking** 🧠
*Tags: #Growth #Strategy*

Nhìn toàn bộ hệ thống thay vì parts riêng lẻ. Identify feedback loops, leverage points, unintended consequences.

📖 Chi tiết: 
- [Systems Thinking](./chapters/09-systems-thinking.md)
- [Systems Thinking in Life](./guides/growth/systems-thinking-in-life.md)

---

## T

### **T-Shaped Skills** 🎯
*Tags: #Career #Learning*

Xem [Core Skill](#core-skill-t-shaped)

---

### **TDD (Test-Driven Development)** 🧪
*Tags: #Backend #Testing*

Viết test trước, code sau. Flow: Red (Test fails) → Green (Make it pass) → Refactor (Clean up).

📖 Chi tiết: [Testing Guide](./domains/backend-dev/testing-guide.md)

---

### **Time Blocking** ⏰
*Tags: #Productivity #TimeManagement*

Chia ngày thành blocks cho tasks cụ thể. VD: 9-11 AM = Deep Work, 2-3 PM = Meetings. Elon Musk dùng 5-min blocks.

📖 Chi tiết: [Quản lý thời gian](./chapters/06-quan-ly-thoi-gian.md)

---

### **Top 1% Developer** 👑
*Tags: #Career #Excellence*

Developer thuộc top 1% về impact/lương. Đặc điểm: Ownership, Business mindset, Deep work, T-shaped skills, Communication.

📖 Chi tiết: [Becoming Top 1%](./guides/growth/becoming-top-1-percent.md) ⭐ **Must Read**

---

### **Tutorial Hell** 😈
*Tags: #Learning #AntiPattern*

Xem hết tutorial này đến khóa học khác nhưng không tự code cái gì. Escape bằng: Build projects, Stop passive learning.

📖 Chi tiết: [Chương 2: Luyện tập có chủ đích](./chapters/02-luyen-tap-co-chu-dich.md)

---

## W

### **WebSocket** 🔌
*Tags: #Backend #RealTime*

Protocol cho real-time bidirectional communication. Use cases: Chat apps, Live notifications, Multiplayer games.

📖 Chi tiết: [Real-time Chat System](./domains/backend-dev/system-design/realtime-chat-system.md)

---

### **Webhook** 🪝
*Tags: #Backend #API*

Callback HTTP POST triggered khi có event. VD: Payment processed → Stripe gửi POST đến `yoursite.com/webhooks`.

📖 Chi tiết: [API Design Guide](./domains/backend-dev/api-design-guide.md)

---

## Domains Quick Reference

### 🎮 **Game Development**
[Main Guide](./domains/game-dev/README.md) | Unity, Unreal, Multiplayer, Game Server

### 🔧 **Backend Development**
[Main Guide](./domains/backend-dev/README.md) | Node.js, C#, System Design, Microservices

### 🤖 **AI/ML**
[Main Guide](./domains/ai-ml/README.md) | Machine Learning, Deep Learning, LLMs

### 🌐 **Web Development**
[Main Guide](./domains/web-dev/README.md) | React, Vue, Frontend

### 🔗 **Blockchain**
[Main Guide](./domains/blockchain/README.md) | Smart Contracts, DeFi, NFT

### 🛡️ **Network & Security**
[Main Guide](./domains/network-security/README.md) | Penetration Testing, OWASP, Cryptography

---

## Contributing

Thiếu thuật ngữ nào? [Contribute here](./CONTRIBUTING.md) hoặc tạo Pull Request!

---

> [← Back to Home](./README.md) | [Quick Start](./QUICK-START.md) | [Content Roadmap](./CONTENT-ROADMAP.md)

**Last Updated:** February 17, 2026  
**Total Terms:** 70+ concepts
