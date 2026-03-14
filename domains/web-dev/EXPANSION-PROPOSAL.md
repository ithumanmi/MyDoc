# 🌐 Web Dev Domain: Nhận xét & Đề xuất mở rộng

> Tài liệu nội bộ: đánh giá domain `domains/web-dev` và kế hoạch mở rộng nội dung/cấu trúc.

---

## 📋 1. Nhận xét hiện trạng

### Điểm mạnh
- **README.md rất rõ ràng:** Bảng so sánh Web Dev vs App/Game/AI, Mermaid roadmap 4 level, completion criteria từng level.
- **Gắn với thực tế:** Reality Check, mức lương, cạnh tranh, verdict "Build Product + Optimize Performance".
- **Lộ trình Design System 14 ngày:** Chi tiết từ tokens → Figma → Storybook → governance, rất phù hợp Frontend Architect.
- **Liên kết tốt:** Knowledge Audit (EduStream SaaS), `guides/03-career-skills/web-dev/` (career, portfolio, interview), DIFFICULTY-GUIDE.
- **CV keywords & Resources:** Phần cuối giúp người học biết cách "bán" kỹ năng và tìm tài liệu.

### Hạn chế
| Vấn đề | Chi tiết |
|--------|----------|
| **Cấu trúc phẳng** | Chỉ có 1 file `README.md`. Các domain khác (ai-ml, game-dev, backend-dev) có nhiều thư mục con và bài chi tiết. |
| **Thiếu INDEX/sitemap** | backend-dev có `INDEX.md` giúp điều hướng; web-dev chưa có. |
| **Nội dung chuyên sâu chưa tách** | Design System 14 ngày, Performance, Security, Testing nằm gọn trong README → khó tái sử dụng và cập nhật. |
| **React/Next-centric** | Vue, Svelte, Astro chưa được nêu như alternative path (dù có thể chỉ gợi ý ngắn). |
| **Testing chưa có tầm** | E2E (Playwright/Cypress), Unit (Vitest/Jest) chỉ xuất hiện ở challenges/web-ui, chưa nằm trong roadmap. |
| **API & Data layer** | REST vs GraphQL, tRPC, React Query/SWR chưa có mục riêng trong roadmap. |
| **Collected links** | Có `resources/collected_links/web-ui-ux.md` nhưng không có `web-dev.md`; một số doc (e.g. search-engine-101) tham chiếu `web-dev.md`. |
| **Challenges** | `challenges/web-ui` tồn tại độc lập; chưa có link rõ từ domain web-dev và chưa có challenge fullstack/backend. |

### So sánh nhanh với domain khác
- **backend-dev:** Nhiều file (README, INDEX, security, system-design, architecture, database, templates) → dễ tìm và mở rộng.
- **web-dev:** Một README toàn diện nhưng mọi thứ “dồn” vào một file → cần tách và bổ sung.

---

## 🚀 2. Đề xuất mở rộng

### 2.1 Cấu trúc thư mục đề xuất

```
domains/web-dev/
├── README.md                 # Giữ, rút gọn: overview + link ra các doc con
├── INDEX.md                  # [MỚI] Sitemap toàn bộ web-dev (giống backend-dev)
├── EXPANSION-PROPOSAL.md     # File này
│
├── foundations/              # [MỚI] Level 1
│   ├── README.md             # HTML/CSS/JS, DevTools, Git
│   └── responsive-tailwind.md
│
├── frontend/                 # [MỚI] Level 2
│   ├── README.md             # React ecosystem, state, routing, forms
│   ├── react-performance.md  # Memoization, CWV, bundle split
│   ├── design-systems/       # Tách từ 14-day table
│   │   ├── README.md
│   │   └── 14-day-sprint.md
│   └── testing-frontend.md   # Unit (Vitest/Jest), E2E (Playwright/Cypress)
│
├── fullstack/                # [MỚI] Level 3
│   ├── README.md             # Next.js, TS, DB, Auth
│   ├── data-fetching.md      # REST, GraphQL, tRPC, React Query/SWR
│   └── auth-security.md      # JWT, OAuth, OWASP, CSP (tóm tắt + link backend-dev)
│
├── senior-paths/             # [MỚI] Level 4
│   ├── README.md             # 3 path A/B/C
│   ├── frontend-architect.md # CWV, a11y, micro-frontends
│   └── backend-architect.md  # Cross-link backend-dev, cache, scale
│
├── portfolio-career/          # [MỚI] Tóm tắt + link guides
│   └── README.md             # Checklist portfolio, interview prep, link guides/03-career-skills/web-dev
│
└── resources/                # [MỚI] Tùy chọn
    └── README.md             # YouTube, courses, books (dời từ README gốc)
```

### 2.2 Nội dung cần bổ sung (ưu tiên)

1. **INDEX.md**  
   - Liệt kê toàn bộ doc trong `web-dev` theo level (Foundations → Senior) và theo chủ đề (Frontend, Fullstack, Security, Testing).  
   - Link tới Knowledge Audit, `challenges/web-ui`, `guides/03-career-skills/web-dev`.

2. **Design System**  
   - Tách bảng 14 ngày + daily cadence + checklist vào `frontend/design-systems/14-day-sprint.md`.  
   - README design-systems: overview, tokens, Storybook, governance.

3. **Testing**  
   - Một doc (ví dụ `frontend/testing-frontend.md`): Unit (Vitest/Jest), E2E (Playwright/Cypress), testing strategy trong React/Next.  
   - Link tới `challenges/web-ui` cho bài tập.

4. **Data & API**  
   - Một doc (ví dụ `fullstack/data-fetching.md`): REST vs GraphQL vs tRPC, React Query/SWR, Server Components data flow.  
   - Link tới `backend-dev` cho API design nâng cao.

5. **Security (góc Web)**  
   - Một doc ngắn (ví dụ `fullstack/auth-security.md`): XSS, CSRF, CSP, JWT storage, OAuth (high-level).  
   - Chi tiết OAuth/backend → link `backend-dev/security/oauth2-oidc-deep-dive.md`.

6. **Alternative stacks (ngắn)**  
   - Trong README hoặc `frontend/README.md`: 1–2 đoạn về Vue/Nuxt, Svelte/SvelteKit, Astro khi nào nên cân nhắc.

7. **Collected links**  
   - Tạo `resources/collected_links/web-dev.md` (hoặc thống nhất dùng `web-ui-ux.md` và đổi tên thành `web-dev.md` nếu muốn thống nhất với domain).  
   - Cập nhật mọi tham chiếu tới `web-dev.md` (e.g. search-engine-101).

8. **Liên kết Challenges**  
   - Trong `domains/web-dev/README.md` và `INDEX.md`: thêm mục “Challenges” link tới `challenges/web-ui` và (sau này) challenge fullstack nếu có.

### 2.3 Rút gọn README.md hiện tại

- Giữ: Reality Check, Mermaid roadmap, bảng level 1–4 (tóm tắt), Portfolio checklist, Interview prep (tóm tắt).  
- Chuyển: Chi tiết từng level → link tới `foundations/`, `frontend/`, `fullstack/`, `senior-paths/`.  
- Chuyển: Bảng 14 ngày Design System → `frontend/design-systems/14-day-sprint.md`.  
- Chuyển: Resources (YouTube, courses, books) → `resources/README.md` hoặc giữ 1 đoạn ngắn + link.

### 2.4 Cross-domain

- **backend-dev:** Dùng cho System Design, OAuth, DB, caching, DevOps (Path B, C).  
- **challenges/web-ui:** Frontend/UI challenges; thêm 1–2 challenge fullstack (API + DB + auth) nếu muốn.  
- **guides/03-career-skills/web-dev:** Giữ là “career & portfolio”; domain web-dev tập trung “technical roadmap”.

---

## ✅ 3. Checklist triển khai (gợi ý)

- [ ] Tạo `INDEX.md` và cập nhật README với link tới INDEX.
- [ ] Tạo `frontend/design-systems/14-day-sprint.md` (tách từ README).
- [ ] Tạo `frontend/testing-frontend.md` (Unit + E2E).
- [ ] Tạo `fullstack/data-fetching.md` và `fullstack/auth-security.md`.
- [ ] Tạo `senior-paths/README.md` (path A/B/C) + 1–2 file con nếu cần.
- [ ] Thêm mục Challenges trong README/INDEX (link `challenges/web-ui`).
- [ ] Tạo hoặc đổi tên `resources/collected_links/web-dev.md` và cập nhật link.
- [ ] (Tùy chọn) Tạo `foundations/`, `portfolio-career/`, `resources/` với README ngắn.

---

*Tài liệu này có thể cập nhật khi triển khai từng bước.*
