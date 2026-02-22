# 🌍 Remote Backend Developer Guide: Làm việc cho công ty Global

> [← Back to Backend Roadmap](../../../domains/backend-dev/README.md) | [Remote Game Dev Guide](../game-dev/remote-game-dev-guide.md) | [Home](../../../README.md)

Hướng dẫn chiến lược để Backend Developer tại Việt Nam xin việc remote cho các công ty US/EU/Singapore với mức lương $2000-$8000+/tháng.

---

## 📋 Mục lục

1. [Why Backend is King of Remote?](#1-why-backend-is-king-of-remote)
2. [Market & Salary Reality](#2-market--salary-reality)
3. [Tech Stack Strategy](#3-tech-stack-strategy)
4. [Portfolio & Resume](#4-portfolio--resume)
5. [Sourcing Jobs](#5-sourcing-jobs)
6. [Interview Strategy (System Design)](#6-interview-strategy-system-design)
7. [Salary Negotiation](#7-salary-negotiation)
8. [Sample Roadmap (6 Months)](#8-sample-roadmap-6-months)

---

## 1. Why Backend is King of Remote?

### The "Black Box" Advantage
Khác với Frontend hay Game Dev cần review giao diện/trải nghiệm liên tục, Backend hoạt động dựa trên logic, APIs, và data.
- **Dễ define requirements:** "Input A → Output B", "API response < 100ms".
- **Ít cultural barriers:** Code là ngôn ngữ chung. Logic đúng là đúng.
- **Async friendly:** Không cần họp nhiều để chỉnh pixel.

### Demand Global
Mọi công ty đều cần Backend:
- **SaaS Startups:** Cần build APIs nhanh (Node.js/Python).
- **Fintech/Banking:** Cần security & reliability (Java/Go).
- **AI/ML Companies:** Cần data pipelines (Python/Go).

---

## 2. Market & Salary Reality

### Tier 1: US/UK Tech Companies (Silicon Valley level)
*Yêu cầu: Tiếng Anh native-level, Algorithms xuất sắc, System Design sâu.*
- **Junior:** $4,000 - $6,000/tháng
- **Senior:** $8,000 - $15,000+/tháng
- **Examples:** GitLab, Automattic, Startups series B/C.

### Tier 2: EU/Australia/Singapore/Canada
*Yêu cầu: Tiếng Anh giao tiếp tốt, Solid engineering skills.*
- **Junior:** $2,000 - $3,500/tháng
- **Senior:** $5,000 - $8,000/tháng
- **Examples:** Canva, Atlassian (remote roles), Tech companies in Berlin/London/Singapore.

### Tier 3: Global Outsourcing / Staffing Agencies
*Yêu cầu: Tiếng Anh đọc hiểu/giao tiếp cơ bản, Tech stack phổ biến.*
- **Junior:** $1,000 - $2,000/tháng
- **Senior:** $3,000 - $5,000/tháng
- **Examples:** Toptal, Turing, Andela, Crossover.

---

## 3. Tech Stack Strategy

Để cạnh tranh global, bạn cần combo skill "Sharp Knife" (Chuyên sâu) thay vì "Swiss Army Knife" (Biết mỗi thứ một ít).

### Combo 1: The Modern Startup (Cao nhất về số lượng jobs)
- **Language:** Node.js (TypeScript) hoặc Python (FastAPI/Django).
- **Database:** PostgreSQL.
- **Infra:** AWS (EC2, Lambda), Docker.
- **Why:** Startups cần tốc độ. JS/Python dev có thể làm fullstack nếu cần.

### Combo 2: The Performance Engineer (Lương cao nhất)
- **Language:** Go (Golang) hoặc Rust.
- **Database:** Cassandra, DynamoDB, Redis.
- **Infra:** Kubernetes (K8s), gRPC, Microservices.
- **Why:** Scale hệ thống lớn, Fintech, Blockchain. Nguồn cung nhân lực ít.

### Combo 3: The Enterprise (Ổn định nhất)
- **Language:** Java (Spring Boot) hoặc C# (.NET Core).
- **Database:** Oracle, SQL Server.
- **Infra:** Azure, GCP.
- **Why:** Ngân hàng, Bảo hiểm, Large Corporations.

**Lời khuyên:** Nếu đang làm PHP/Laravel hoặc Ruby, hãy cân nhắc học thêm **Go** hoặc **Node.js** để mở rộng pool job remote.

---

## 4. Portfolio & Resume

### CV "Chẩn" Global (ATS Friendly)
Khác CV Việt Nam:
- **KHÔNG:** Ảnh chân dung, Ngày sinh, Quê quán, Marital status.
- **CÓ:** LinkedIn, GitHub link, Tech Stack list rõ ràng.
- **Formula:** Action Verb + Task + Result (Numbers).
  > *❌ "Built API for user management."*
  >
  > *✅ "Designed and implemented RESTful APIs handling 10k req/s using Go and Redis, reducing latency by 40%."*

### GitHub: "Quality > Quantity"
Recruiter nước ngoài sẽ check code structure.
- **Project Must-Have:**
  1. **Clean Architecture:** Folder structure rõ ràng (Service, Repository, Handler layers).
  2. **Dockerized:** Có `Dockerfile` và `docker-compose.yml` để họ run thử ngay.
  3. **Unit Tests:** Ít nhất cover core logic.
  4. **README.md xịn:** Giới thiệu project, Tech stack, Cách run, API Docs (Swagger link).

### Blog Technical (Vũ khí bí mật)
Viết 2-3 bài deep dive bằng tiếng Anh trên Medium/Dev.to.
- *Ví dụ:* "How I optimized PostgreSQL query from 2s to 20ms".
- *Ví dụ:* "Handling concurrency in Go: Mutex vs Channels".
=> Chứng minh Tiếng Anh + Technical Depth.

---

## 5. Sourcing Jobs

### Các kênh hiệu quả nhất

1.  **Hacker News (Who is hiring):**
    - Vào ngày 1 hàng tháng. Search "Remote". Các job ở đây cực chất, ít rác.

2.  **Remote-focused Boards:**
    - **RemoteOK**, **WeWorkRemotely**: Filter "Backend", "Worldwide/Anywhere".
    - **Himalayas.app**: Filter rất tốt theo Timezone.

3.  **LinkedIn "Sniper" Strategy:**
    - Đừng chỉ Apply nút "Easy Apply".
    - Search: `("hiring" OR "looking for") AND "backend developer" AND "remote" AND ("Go" OR "Node.js")`
    - Connect với Recruiter/Founder -> Nhắn tin trực tiếp: *"Hi, I saw your post. I'm a Backend Dev with X years exp in Go/K8s. Here is my portfolio..."*

4.  **Agencies (Đường tắt):**
    - Apply vào **Toptal**, **Turing**. Pass bài test của họ -> Họ kiếm job cho mình. Khó vào nhưng lương ổn định.

---

## 6. Interview Strategy (System Design)

Đây là vòng "Kill boss" của các job lương cao.

### Quy trình phỏng vấn chuẩn
1.  **HR Screening (15-30p):** Check tiếng Anh, culture fit.
2.  **Coding Challenge (Take-home hoặc Live):** LeetCode Medium hoặc Build 1 API nhỏ.
3.  **System Design (45-60p):** Design URL Shortener, Chat System, E-commerce backend.
4.  **Behavioral:** STAR method.

### System Design Checklist
Bạn cần vẽ được diagram và giải thích:
- **Load Balancing:** Nginx, HAProxy.
- **Caching:** Redis, Memcached (Caching strategies: Write-through vs Look-aside).
- **Database Sharding/Replication:** Master-Slave.
- **Message Queues:** Kafka, RabbitMQ (Async processing).
- **Communication:** REST vs gRPC vs GraphQL.

*Tài liệu học:*
- Sách: *Designing Data-Intensive Applications* (Must read!).
- Github: *donnemartin/system-design-primer*.

---

## 7. Salary Negotiation

### Đừng nói con số trước!
- **Recruiter:** "What is your expected salary?"
- **You:** "I am flexible based on the total package and responsibilities. What is the budget range for this position?"

### Research kỹ
- Check Glassdoor, Levels.fyi cho vị trí tương đương tại quốc gia của công ty đó.
- Công thức tham khảo: Lương Net mong muốn tại VN * 1.5 ~ 2.0 (Để cover bảo hiểm, thuế, risk).

### Nhận tiền về VN
- **Wise (TransferWise):** Phí rẻ nhất, tỷ giá tốt.
- **Payoneer:** Phổ biến, có thẻ Master rút tiền.
- **Crypto (USDT/USDC):** Một số công ty Web3 trả qua đây. Nhanh gọn.
- **Contract:** Ký consultancy contract (Hợp đồng tư vấn) để đơn giản hóa thuế má. Tự đóng thuế TNCN tại VN.

---

## 8. Sample Roadmap (6 Months)

### Month 1-2: Foundation & English
- Cày tiếng Anh giao tiếp (Preply/Cambly).
- Chuẩn hóa LinkedIn, CV.
- Chọn 1 tech stack chính để deep dive.

### Month 3-4: Build & Polish
- Code 1 Pet Project "xịn" (Backend Golang/Node, Microservices, Docker, CI/CD).
- Viết 2 bài Blog technical tiếng Anh.
- Luyện LeetCode (Easy/Medium) mỗi ngày 1 bài.

### Month 5: Application Sprint
- Apply 5-10 jobs/ngày.
- Nhờ review CV trên các cộng đồng (Reddit r/cscareerquestions, Discord dev).
- Bắt đầu phỏng vấn thử để quen cảm giác.

### Month 6: Interview & Offer
- Tập trung ôn System Design.
- Review lại các failed interviews.
- Deal lương và chốt offer!

---

**Remember:** Làm remote là chạy marathon, không phải chạy nước rút. Kiên trì và nâng cao trình độ tiếng Anh là chìa khóa quan trọng nhất. Good luck! 🚀
