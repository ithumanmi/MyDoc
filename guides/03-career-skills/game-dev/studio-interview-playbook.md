---
title: "Studio Interview Playbook"
description: "Checklist chuẩn bị portfolio, vòng phỏng vấn kỹ thuật/behaviour và deal offer cho Game Studio."
tags:
  - career
  - interview
  - game-dev
updated: 2026-03-23
---

# 🎤 Studio Interview Playbook (2026)

> **Goal:** Giúp Game Developer tại Việt Nam chuẩn bị bài bản trước khi apply studio (VN/SEA/Global) – từ portfolio → phỏng vấn kỹ thuật → vòng văn hoá → thương lượng offer.
> **Deliverables:** Portfolio link, case study PDF, rehearsal script, Q&A bank, negotiation plan.

## 1. Chuẩn bị trước khi apply

| Hạng mục | Checklist |
|----------|-----------|
| Portfolio | 1 flagship project (Tier 3+), video 30s, repo code sạch, doc highlight vai trò |
| Demo reel | ≤90s, chèn caption nhiệm vụ (AI, netcode, shader) |
| Resume | 1 trang, nêu metric (FPS tăng +30%, crash rate giảm -15%) |
| Recommendation | Liên hệ ex-lead/mentor viết testimonial (LinkedIn) |
| References | Chuẩn bị 2 người xác nhận (email + phone) |

**Self-audit:** chạy [Game Dev Knowledge Audit](../../../case-studies/knowledge-audits/game-dev-knowledge-audit.md) và note gap để kể trong interview.

## 2. Interview Loop tiêu chuẩn

1. **Recruiter Screen (15-30’):** Xác minh kinh nghiệm, động lực, lương mong muốn.
2. **Portfolio/Technical Interview (60’):** Deep dive vào dự án, whiteboard pseudo-code, design question.
3. **Practical Test/Take-home:** Unity project nhỏ (4-8h) hoặc onsite pair-programming.
4. **Culture/Behaviour (45’):** STAR method, conflict resolution, teamwork.
5. **Leadership/CTO loop:** Vision alignment, câu hỏi “trick” về scale, live service.
6. **Offer & Negotiation.**

## 3. Technical Interview Patterns

| Chủ đề | Sample Prompt | Gợi ý trả lời |
|--------|---------------|---------------|
| Architecture | “Thiết kế hệ thống quest modular?” | Nêu component, data-driven config, event bus |
| Performance | “Debug frame time spike 40ms?” | Quy trình profiling, capture metrics, hypothesis |
| Netcode | “Client prediction trong FPS?” | Thuật toán, edge cases (packet loss), rollback |
| AI/Gameplay | “FSM vs Behavior Tree khi nào dùng?” | So sánh + ví dụ dự án |
| Production | “Bạn xử lý bug blocker trước release?” | Escalation, war-room, comms |

**Pro tip:** chuẩn bị “wins” theo format `Problem → Action → Metric`. Ví dụ “Addressables refactor giảm boot time 8s → 3s”.

## 4. Behavioural & Culture Fit

- Dùng khung STAR: Situation, Task, Action, Result.
- Story bank tối thiểu 5 câu chuyện: conflict, failure, leadership, mentoring, crunch management.
- Nhấn mạnh khả năng hợp tác cross-discipline (Artist, Producer). Đưa ví dụ meeting/retro.

### Câu hỏi thường gặp
- “Khi disagree với game designer bạn làm gì?” → nói về data + prototype.
- “Làm sao cân bằng quality vs deadline?” → Discuss MoSCoW, risk log.
- “Bạn học kỹ năng mới như thế nào?” → Loop học → áp dụng → chia sẻ team.

## 5. Take-home Test Strategy

1. Đọc requirement, xác định scope (6-8h). Viết doc `ASSUMPTIONS.md`.
2. Ưu tiên clean code + README hướng dẫn build/run.
3. Ghi lại profiling/chỉ số (FPS, memory), log những gì chưa kịp làm.
4. Quay video 1-2 phút demo (Loom) để reviewer xem nhanh.

## 6. Negotiation & Offers

| Bước | Nội dung |
|------|----------|
| Benchmark | Collect range (Glassdoor, cộng đồng). Note thuế, phúc lợi. |
| Priorities | Xếp hạng tiền mặt, RSU, bonus, remote, visa, training budget. |
| Counter | Dùng dữ liệu: “Dựa vào market range 1,800-2,200 USD…”. |
| Non-monetary | Xin thêm: sign-on bonus, relocation, hardware, conference budget. |
| Close | Yêu cầu offer bằng văn bản, thời hạn 5 ngày.

**For remote contract:** kiểm tra `Net Deductions` (thuế, phí chuyển tiền). Nhắc studio support invoice/tool.

## 7. Mock Interview Checklist
- [ ] Portfolio rehearsal 3 lần (time box 10’).
- [ ] Code warm-up (C# patterns, LINQ, coroutine).
- [ ] Practice “System design” answer (whiteboard Figma/Miro).
- [ ] Behavioural Q&A recorded, tự review body language.
- [ ] Setup technical environment (Unity version, IDE, screen share test).

## 8. Tài liệu & Link hữu ích
- [Game Dev Career Ladder](./game-dev-career-ladder.md)
- [Salary Negotiation Guide](./game-dev-career-ladder.md#7-salary-negotiation)
- [Remote Game Dev Guide](./remote-game-dev-guide.md)
- [Templates/Interview-Prep Checklist](../../../templates/career/interview-log.md)