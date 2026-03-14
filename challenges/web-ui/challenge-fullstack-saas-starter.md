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