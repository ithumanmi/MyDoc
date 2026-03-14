# Challenge: Fullstack SaaS Starter (Next.js / Node)

## Goal
Build một MVP SaaS với Next.js (hoặc tương đương) gồm auth, CRUD chính, và deploy production.

## Scope
- Frontend: React/Next.js, routing, form validation (React Hook Form + Zod).
- Backend: API routes hoặc server actions; DB Postgres/Mongo qua Prisma.
- Auth: Email+password hoặc OAuth; session cookie (NextAuth/Clerk tương đương).
- Features: CRUD đối tượng chính (vd: Projects/Tasks), pagination/filter/search.
- UX: Loading/error states rõ ràng; optimistic update tuỳ chọn.

## Deliverables
- Repo với README hướng dẫn chạy/dev/prod.
- Migration/seed DB mẫu.
- Demo deploy (Vercel/Render/Railway).
- 5–10 test (unit/component hoặc e2e tối thiểu 1 flow).

## Evaluation Checklist
- [ ] Auth an toàn (hash password nếu tự roll; cookie flags nếu dùng session).
- [ ] API trả lỗi chuẩn (status, message), validation ở server + client.
- [ ] DB schema có chỉ mục hợp lý (id, foreign keys, search fields).
- [ ] UI states: loading, empty, error; form validation UX tốt.
- [ ] Performance: tránh over-fetch; dùng caching/Revalidation hợp lý.
- [ ] CI/CD (tối thiểu lint/test) hoặc script check nhanh.

### Rubric chi tiết (self-review hoặc reviewer)
**Auth & Security**
- [ ] Password hashing (nếu tự roll) hoặc cấu hình OAuth/identity chuẩn.
- [ ] Session cookie flags: HttpOnly, Secure (prod), SameSite.
- [ ] Input validation server-side (Zod/validator) cho auth/signup/login.

**API & Validation**
- [ ] API trả status + message rõ, mã lỗi phù hợp.
- [ ] Schema validation ở server; client form validation đồng bộ.
- [ ] Error boundary/loading state cho fetch.

**DB & Data Model**
- [ ] Migration + seed chạy được.
- [ ] Index/key hợp lý (id, foreign keys, search fields).
- [ ] Tenant/ownership enforced (nếu multi-tenant/role-based).

**Features & UX**
- [ ] CRUD chính hoạt động; pagination/filter/search nếu có.
- [ ] UI states đầy đủ: loading, empty, error.
- [ ] Form UX: inline errors, disable submit khi đang gửi, optimistic/undo (tuỳ chọn).

**Performance & Caching**
- [ ] Tránh over-fetch; dùng revalidation/caching hợp lý (Next cache/React Query/SWR).
- [ ] Asset/code splitting phù hợp; kiểm tra Core Web Vitals cơ bản (tuỳ chọn).

**Testing & CI**
- [ ] 5–10 tests (unit/component/e2e ≥1 flow).
- [ ] Lint/format/test script hoặc CI tối thiểu.

**Deploy & Ops**
- [ ] README hướng dẫn dev/prod; .env.example đầy đủ.
- [ ] Deploy demo (Vercel/Render/Railway) kèm link.
- [ ] Healthcheck/logging tối thiểu; check migration chạy ở prod.

**Stretch (tuỳ chọn)**
- [ ] Realtime (pusher/socket), file upload, RBAC, multi-tenant, billing.

## Stretch Goals
- Realtime (pusher/socket) cho notifications.
- File upload (S3/Supabase) với presigned URL.
- Role-based access (admin/member).
- Multi-tenant (org/workspace): tách dữ liệu theo `tenant_id`, enforce ở mọi query.
- Billing (B2B/SaaS): Stripe/PayPal checkout, webhooks, plan limits (seat, usage).

### Variations (pick one)
- **B2B Billing SaaS:** Pricing tiers, seats, webhooks sync license; admin panel xem usage.
- **Multi-tenant Project Hub:** Org-level data isolation, invite members, RBAC per project.
- **Ops Dashboard:** Audit log, background jobs status, alerting (email/webhook).

## Hints
- Với Next.js 14: ưu tiên Server Components + React Query cho client states động.
- Tách layer: lib/db.ts (Prisma), lib/auth.ts, components/ui/, app/(routes).
- Dùng `.env.example` rõ ràng; script `npm run db:migrate && npm run seed`.

## Reference / Solution (tùy chọn)
- Next.js SaaS billing mẫu: https://github.com/vercel/nextjs-subscription-payments (Stripe, Next.js, Supabase auth)
- SaaS starter có RBAC + billing: https://github.com/chronark/chronark.com (Next.js + Stripe)
- Auth + Postgres starter: https://github.com/vercel/nextjs-postgres-auth-starter
- Anchor repo mẫu (bổ sung): https://github.com/example/nextjs-saas-starter (thay bằng repo của bạn nếu có)