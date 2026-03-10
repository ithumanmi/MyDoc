# ✅ Backend Master Checklist

> Dùng bảng checklist này để tự đánh giá định kỳ (theo tháng/quý). Mỗi cấp độ gồm 5 nhóm năng lực: Kiến thức lý thuyết, coding/project, vận hành & DevOps, chất lượng & bảo mật, và hồ sơ/portfolio. Ghi lại minh chứng cụ thể (repo, số liệu, bài blog) trước khi tick.

| Cấp độ | Năng lực | Tiêu chí hoàn thành | Minh chứng / Link |
| --- | --- | --- | --- |
| **Level 1 – Foundations** | Kiến thức cốt lõi | Hiểu HTTP request/response, status code, CRUD DB, Git workflow cơ bản |  |
|  | Coding/Project | Ship 1 CRUD API (Todo/User) kết nối PostgreSQL/MySQL, có README hướng dẫn chạy |  |
|  | Testing & Quality | Viết tối thiểu 5 unit tests, dùng lint/prettier hoặc tương đương |  |
|  | Deploy & Ops | Deploy demo lên Render/Railway/Azure App Service, quản lý `.env` an toàn |  |
|  | Portfolio | README dự án mô tả kiến trúc + collection Postman hoặc Swagger |  |
| **Level 2 – Professional API** | Kiến thức | Nắm JWT/OAuth2, migration/indexing DB, background jobs, logging cơ bản |  |
|  | Coding/Project | Hoàn thành dự án e-commerce hoặc tương đương với auth, phân quyền, pagination |  |
|  | Testing & Quality | ≥20 unit/integration tests, coverage >60%, thêm contract test/snapshot |  |
|  | Deploy & Ops | CI/CD (GitHub Actions/GitLab CI), health-check endpoint, monitor error (Sentry/Raygun) |  |
|  | Security | Check OWASP Top 10 (SQLi, XSS, CSRF), secrets quản lý qua Secret Manager hoặc vault |  |
|  | Portfolio | Blog note hoặc case study “Tối ưu API X ms”, Link demo kèm credentials test |  |
| **Level 3 – Scalable Systems** | Kiến thức | Hiểu microservices vs modular monolith, messaging (RabbitMQ/Kafka), caching strategy |  |
|  | Coding/Project | Ít nhất 3 services giao tiếp (sync + async), dùng Redis cache + message queue, có diagram kiến trúc |  |
|  | Testing & Quality | Stress/load test (k6/JMeter), chaos/latency injection tối thiểu 1 lần, alert P95 |  |
|  | Deploy & Ops | Docker Compose/K8s manifests, môi trường staging, log/metrics/tracing tích hợp (ELK/OTel) |  |
|  | Security | Threat model cơ bản, rate limiting, audit log cho action quan trọng |  |
|  | Portfolio | Viết playbook incident hoặc postmortem, cập nhật README với SLO/SLA/SLA breach |  |
| **Level 4 – Senior / Architect Paths** | Kiến thức | Thành thạo system design (CAP, CQRS, event sourcing, partition strategy), hiểu chi tiết cloud provider |  |
|  | Coding/Project | Thiết kế & dẫn dắt 1 dự án multi-team (platform, SRE, hoặc system design case study lớn) |  |
|  | Testing & Quality | Thiết lập tiêu chuẩn chất lượng team (template test, review checklist, chaos runbook) |  |
|  | Deploy & Ops | GitOps/Progressive delivery, cost dashboard, incident response (on-call rotation có số liệu MTTR) |  |
|  | Security & Compliance | Triển khai security review định kỳ, hiểu GDPR/PDPA, có checklist release liên quan compliance |  |
|  | Portfolio & Leadership | Talk nội bộ/meetup, tài liệu mentoring, roadmap phát triển team |  |

### Cách sử dụng
1. Copy file này sang Notion/Obsidian hoặc in ra để tick theo tháng.
2. Với mỗi tiêu chí, ghi link bằng chứng (repo, dashboard, bài viết) → đảm bảo có thể chứng minh khi phỏng vấn.
3. Sau khi hoàn thành 1 cấp độ, cập nhật CV/LinkedIn để phản ánh kỹ năng mới.

### Liên kết nhanh
- 📘 Roadmap theo stack: [Node.js + TS](./nodejs-typescript-roadmap.md) · [C#/.NET](./csharp-dotnet-roadmap.md) · [Golang](./golang-roadmap.md) · [Rust](./rust-roadmap.md)
- 🛡️ Bảo mật & testing: [backend-security.md](./backend-security.md) · [testing-guide.md](./testing-guide.md)
- 🏗️ System Design: [system-design-guide.md](./system-design-guide.md) · thư mục [system-design/](./system-design/)
- ♾️ DevOps/SRE: thư mục [devops-sre/](./devops-sre/) · [monitoring-observability.md](./monitoring-observability.md)
- 🧭 Lộ trình chung & operating map: [README.md](./README.md)

> Cần thêm cấp độ hoặc muốn biến checklist này thành template tự đánh giá tự động? Mở issue hoặc tạo PR nhé!