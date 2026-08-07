---
title: "Web Development Roadmap (Fullstack Focus)"
description: "Frontend/fullstack web curriculum with Next/React focus"
updated: "2026-08-07"
canonical: true
tags: [web, frontend, roadmap]
audience: [beginner, intermediate, advanced]
related:
  - ../../challenges/web-ui/README.md
  - ../README.md
sensitivity: public
---

# 🌐 Web Development Roadmap (Fullstack Focus)

> [← Domains hub](../README.md) | [Home](../../README.md) | [Challenges](../../challenges/web-ui/README.md)
>
> **Domain maturity:** 🟡 Drafting  
> **📊 Difficulty:** See [DIFFICULTY-GUIDE.md](../../meta/ops/DIFFICULTY-GUIDE.md)  
> **🧩 Knowledge Audit:** [Web Dev Knowledge Audit](../../case-studies/knowledge-audits/web-dev-knowledge-audit.md)

---

<!-- tech-career-nav -->
> **Tech vs Career:** this folder = technical how-to. **Web career / monetization:** [Web career / monetization](../../guides/03-career-skills/web-dev/README.md). Full map: [`meta/domain-guide-map.md`](../../meta/domain-guide-map.md).

## 📊 1. Reality Check: Web Dev vs The World

Web Development là con đường phổ biến nhất để gia nhập ngành IT, nhưng cũng là nơi cạnh tranh khốc liệt nhất.

| Tiêu chí | 🌐 Web Dev (Fullstack) | 📱 App Dev (Mobile) | 🎮 Game Dev (Unity) | 🤖 AI/ML Engineer |
| :--- | :--- | :--- | :--- | :--- |
| **Độ khó (Entry Barrier)** | ⭐⭐ (Dễ nhất - Tài liệu nhiều, dễ học) | ⭐⭐⭐ (Trung bình) | ⭐⭐⭐⭐ (Khá khó) | ⭐⭐⭐⭐⭐ (Rất khó) |
| **Cơ hội việc làm (VN)** | ⭐⭐⭐⭐⭐ (Rất nhiều - Từ Freelance đến Enterprise) | ⭐⭐⭐⭐ (Nhiều) | ⭐⭐⭐ (Vừa phải) | ⭐⭐⭐ (Ít slot Junior) |
| **Mức lương (Junior)** | 💰 Trung bình ($400 - $800) | 💰 Trung bình | 📉 Thấp hơn chút | 📈 Cao nhất |
| **Cạnh tranh** | 🔥 **Cực cao** (Hàng ngàn bootcamp grads mỗi năm) | ⚖️ Trung bình | 🔥 Cao | ⚖️ Thấp |
| **Tốc độ thay đổi** | ⚡ **Chóng mặt** (Framework mới mỗi tuần) | 🐢 Ổn định hơn | 🐢 Ổn định | ⚡ Rất nhanh (AI) |
| **Đặc thù** | 🛠️ Build SaaS, E-commerce, Internal Tools | 📱 Build App người dùng | 🎮 Build Game | 🧠 Build Models |

> **Verdict:** Web Dev là lựa chọn an toàn và linh hoạt nhất. Nhưng để nổi bật giữa đám đông, bạn không thể chỉ biết code, bạn phải biết **Build Product** và **Optimize Performance**.

> **Sitemap:** [INDEX.md](INDEX.md) · **Labs:** [labs/](./labs/README.md)

### Module map
| Level | Docs |
| --- | --- |
| Foundations | [foundations/](./foundations/README.md) · [responsive-tailwind](./foundations/responsive-tailwind.md) |
| Frontend | [frontend/](./frontend/README.md) · [react-performance](./frontend/react-performance.md) |
| Fullstack | [fullstack/](./fullstack/README.md) · [lab SaaS](./labs/lab-nextjs-saas-starter.md) |
| Career | [portfolio-career/](./portfolio-career/README.md) · [senior-paths/](./senior-paths/README.md) |

---

## 🗺️ 2. Visual Roadmap (Modern Web Path)

```mermaid
graph TD
    A[Start Here] --> B[🐣 Level 1: Frontend Basics]
    B --> B1(HTML/CSS/JS Mastery)
    B1 --> B2(Responsive Design & Tailwind)
    B2 --> B3(Git & GitHub Basics)
    
    B3 --> C[🔨 Level 2: Modern Frontend]
    C --> C1(React.js Ecosystem)
    C1 --> C2(State Management - Redux/Zustand)
    C1 --> C3(API Integration - Fetch/Axios)
    C3 --> C4(Project: E-commerce UI)
    
    C4 --> D[🕸️ Level 3: Fullstack Integration]
    D --> D1(Node.js / Next.js)
    D1 --> D2(Database - Postgres/MongoDB)
    D2 --> D3(Auth - NextAuth/Clerk)
    D3 --> D4(Project: Full SaaS App)
    
## 🚀 3. Detailed Roadmap (Modular)

Chi tiết từng level đã tách thành các thư mục/doc riêng:
- **Level 1 – Foundations:** [foundations/README.md](foundations/README.md)
- **Level 2 – Frontend:** [frontend/README.md](frontend/README.md)
  - [Design Systems](frontend/design-systems/README.md) · [14-day Sprint](frontend/design-systems/14-day-sprint.md)
  - [Testing Frontend](frontend/testing-frontend.md)
- **Level 3 – Fullstack:** [fullstack/README.md](fullstack/README.md)
  - [Data Fetching](fullstack/data-fetching.md)
  - [Auth & Security](fullstack/auth-security.md)
- **Level 4 – Senior Paths:** [senior-paths/README.md](senior-paths/README.md)
- **Portfolio & Career:** [portfolio-career/README.md](portfolio-career/README.md)
- **Resources:** [resources/README.md](resources/README.md)

Challenges: [challenges/web-ui](../../challenges/web-ui/README.md)
*   **Actions:**
    *   Build **Blog Platform**: CMS, Markdown rendering, SEO.
    *   Build **Trello Clone (SaaS)**: Drag & Drop, Database real-time, Auth.
*   **✅ Completion Criteria:**
    *   [ ] Hiểu sự khác biệt giữa Client Component và Server Component.
    *   [ ] Thiết kế được Database Schema (One-to-many, Many-to-many).
    *   [ ] Deploy project lên Vercel/Railway thành công.

### 👑 Level 4: Senior/Lead Architecture (18+ Tháng)
*Tập trung: System Design, Performance và Scalability.*

Bạn cần chọn chuyên sâu:

#### **🅰️ Path A: Frontend Architect**
*   **Keywords:** Web Performance (Core Web Vitals), Accessibility (a11y), Micro-frontends, Advanced Animations (Framer Motion/GSAP), Design Systems.
*   **Goal:** User Experience đỉnh cao, load time < 1s.

##### 🔁 Lộ trình 14 ngày khám phá Design System

| Ngày | Chủ đề | Deliverable |
| --- | --- | --- |
| 1 | Design System Overview + Case studies (Carbon, Material, Polaris) | Viết note so sánh 3 hệ thống (tokens, docs, governance) |
| 2 | Design Principles & Brand voice | Draft nguyên tắc thiết kế (tone, spacing, motion) |
| 3 | Design Tokens (Color, Typography, Spacing) | Tạo token file (JSON/Style Dictionary) |
| 4 | Accessibility foundations (WCAG, contrast, focus states) | Checklist a11y cho tokens + buttons |
| 5 | Figma Library setup (Auto-layout, variants) | Library core: button, input, badge |
| 6 | Component architecture + naming conventions | Quy ước đặt tên component + doc usage |
| 7 | Storybook / Ladle setup | Storybook chạy với tokens + controls |
| 8 | Theming & Dark mode strategy | Demo theme switcher (CSS vars/Tailwind tokens) |
| 9 | Iconography & Illustration guidelines | Bộ icon chuẩn (stroke, corner radius, grid) |
| 10 | Motion & Micro-interactions | Spec animation (duration, easing) + demo |
| 11 | Content design + localization rules | Bảng voice & tone + ví dụ multi-language |
| 12 | Documentation workflow (zeroheight, Notion, custom site) | Page mô tả component (props, code snippet, usage) |
| 13 | Governance model (DesignOps, contribution) | RACI + process đề xuất component mới |
| 14 | Integration sprint (React/Next demo) | Build mini app tiêu chuẩn hóa component + publish recap |

**Daily cadence đề xuất:**

1. 30’ đọc lý thuyết (Design System Handbook, Refactoring UI, blog Figma).
2. 60’ thực hành (Figma/Code). Ưu tiên output hữu hình (token file, component demo).
3. 30’ review với tiêu chí: a11y, consistency, reusability.

**Checklist hoàn thành:**

- [ ] Token JSON + Tailwind (hoặc CSS vars) đồng bộ.
- [ ] 6 component core (Button, Input, Dropdown, Card, Modal, Tooltip) có doc.
- [ ] Storybook deploy (Chromatic/Vercel) cho QA nội bộ.
- [ ] Governance doc + quy trình release version (semantic versioning).

#### **🅱️ Path B: Backend Architect**
*   **Keywords:** System Design, Microservices, Caching (Redis), Message Queues (RabbitMQ/Kafka), Database Sharding/Indexing.
*   **Goal:** Hệ thống chịu tải hàng triệu users.

#### **🅾️ Path C: DevOps / Platform Engineer**
*   **Keywords:** Docker, Kubernetes, Terraform (IaC), CI/CD Pipelines (GitHub Actions), AWS/GCP/Azure.
*   **Goal:** Automate everything.

---

## 💼 4. Portfolio & Career Strategy

Xem chi tiết tại [portfolio-career/README.md](portfolio-career/README.md).

## 📚 5. Resources (Tài nguyên chọn lọc)

Xem [resources/README.md](resources/README.md).

---

## 💡 6. Core Skills Example (CV Keywords)

Giữ nguyên ví dụ súc tích. Tham khảo thêm ở [portfolio-career/README.md](portfolio-career/README.md).
