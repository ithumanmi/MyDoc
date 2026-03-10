---
title: "Dev Task Estimation Playbook"
description: "Hướng dẫn developer ước lượng tasks đúng, hạn chế trễ hạn và giữ cam kết với team."
tags:
  - productivity
  - developer
  - estimation
updated: 2026-03-10
---

# ⏱️ Dev Task Estimation Playbook

> "Estimation không phải dự đoán tương lai, mà là tạo cam kết đáng tin dựa trên dữ liệu và disipline." – Delivery Chapter

Roadmap dành cho developer muốn nâng cấp kỹ năng estimate tasks, tránh under/over promise và phối hợp tốt với PM/Product.

---

## 1. Mindset & Principles

1. **Estimate ≠ Commitment:** Estimate là best guess có buffer. Commitment chỉ chốt sau khi cả team đồng thuận.
2. **Đo để cải thiện:** Theo dõi actual vs estimate giúp calibrate trong 2-3 sprint.
3. **Break it down:** Task càng nhỏ càng estimate chính xác.
4. **Communicate early:** Nếu thấy lệch >20% so với estimate ban đầu, báo PM ngay.
5. **Include hidden work:** QA, docs, infra, code review, meeting… đều cần tính vào.

---

## 2. Quy trình 5 bước

1. **Clarify Scope**
   - Hiểu use case, constraint, acceptance criteria.
   - Checklist: dữ liệu đầu vào, flow, error states, dependencies.

2. **Breakdown Task**
   - Chia thành unit nhỏ < 1 ngày.
   - Categorize: feature build, bug fix, infra, research spike.

3. **Select Estimation Technique**
   - Story points, t-shirt sizing, time range (PERT), bottom-up.
   - Chọn kỹ thuật theo loại công việc và maturity team.

4. **Apply Buffers & Risk Adjustment**
   - Risk score dựa vào complexity, dependency.
   - Buffer 20-30% cho task unknown hoặc cross-team.

5. **Review & Commit**
   - Sync với PM/Design/QA, confirm Definition of Done.
   - Cập nhật Jira/Linear + ghi chú assumption.

---

## 3. Kỹ thuật Estimation phổ biến

| Phương pháp | Khi dùng | Ưu điểm | Lưu ý |
| --- | --- | --- | --- |
| **Story Points** | Agile team, focus relative effort | Đo effort độc lập thời gian, dễ calibrate | Cần velocity history, dễ tranh luận nếu team chưa cùng chuẩn |
| **T-shirt Sizing (XS-XL)** | Discovery, roadmap high-level | Nhanh, phù hợp với PM/Product | Cần map sang giờ/point khi vào sprint |
| **Time Range (PERT)** | Task quan trọng cần thời gian cụ thể | Có optimistic/pessimistic, giảm bias | Yêu cầu kinh nghiệm + dữ liệu lịch sử |
| **Bottom-up Estimate** | Task phức tạp nhiều bước | Chi tiết, dễ tracking | Mất thời gian, cần breakdown kỹ |
| **Reference Class** | Team có repo task tương tự | Học từ historical actual | Phải maintain knowledge base |

### Công thức PERT
`Estimate = (Optimistic + 4 × Most Likely + Pessimistic) / 6`

### Quick heuristic
- Task UX/UI mới: buffer +25% cho iteration.
- Task đụng legacy: +2 Story Points hoặc +30% thời gian.
- Task có dependency cross-team: nhân hệ số 1.5.

---

## 4. Template bảng estimate

| Sub-task | Type | Estimate | Risk (L/M/H) | Owner | Notes |
| --- | --- | --- | --- | --- | --- |
| API: Create Order | Feature | 3 pts (~1d) | M | Dev A | Reuse OrderService v2 |
| Background job | Infra | 2 pts (~0.5d) | H | Dev A | Cần xác nhận queue | 
| UI Checkout | Feature | 5 pts (~1.5d) | M | Dev B | cần asset từ design |
| QA + Regression | QA | 1 pt (~0.5d) | L | QA | buffer 0.5d |

- **Total:** 11 pts ≈ 3.5-4 ngày effort.
- **Buffer:** +20% → Final commitment: 5 ngày.

> Dùng Notion/Spreadsheet hoặc Linear custom fields để track. Quan trọng là note assumption và signal risk sớm.

---

## 5. Checklist tránh lỗi thường gặp

- [ ] Scope đã rõ, có acceptance criteria và DoD?
- [ ] Đã tách sub-task < 1 ngày?
- [ ] Có tính effort cho code review, QA, docs, deployment?
- [ ] Đã review dependency với các team khác?
- [ ] Buffer được tính theo risk thực tế (không random)?
- [ ] Team agree chung một cách convert story point ↔ thời gian?
- [ ] Có ghi chú assumption để tránh blame?

---

## 6. Mini Case Study – Fix Payment Latency

**Bối cảnh:** Payment API phản hồi chậm, PM yêu cầu dev estimate thời gian fix.

1. **Clarify:** xác nhận logs, metric, phạm vi (chỉ checkout flow?).
2. **Breakdown:**
   - Investigate metric & logs (0.5d)
   - Optimize DB queries (1d)
   - Add caching (0.5d)
   - Load test + rollback plan (1d)
   - Update docs & comms (0.5d)
3. **Technique:** Bottom-up + buffer 30% vì đụng DB core.
4. **Commit:** 3.5d estimate × 1.3 buffer ≈ 4.5d. Communicate timeline + risk (có thể phát sinh schema change).
5. **Review:** Sau khi hoàn thành, note actual 5d và lessons learned vào knowledge base.

---

## 7. Continuous Improvement

- Track **Estimate Accuracy** = Actual / Estimate mỗi sprint.
- Nếu >1.3 trong 2 sprint liên tục ⇒ recalibrate.
- Dùng retro để cập nhật reference tasks: "Feature A (5 pts) mất 3 ngày".
- Pair estimation: dev chính + reviewer để giảm bias.
- Thử Planning Poker hoặc Async Estimation (Linear, Parabol) để tiết kiệm thời gian.

---

## 8. Resource gợi ý

- *Agile Estimating and Planning* – Mike Cohn
- Linear Guide: Estimation best practices
- Atlassian Playbook: Estimation workshop
- ThoughtWorks Tech Radar – "Ditch the estimate" debate (để hiểu trade-off)
- Engineering blog (Uber, Airbnb, Shopify) về capacity planning

> **Thông điệp cuối:** Estimation tốt giúp dev kiểm soát kỳ vọng và chủ động trong delivery. Hãy biến mỗi sprint thành một vòng lặp học hỏi, cập nhật dữ liệu và nâng cấp độ chính xác theo thời gian.