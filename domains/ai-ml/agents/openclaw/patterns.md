---
title: "OpenClaw Patterns"
description: "Patterns thực chiến cho OpenClaw: planning, routing, memory, multi-agent, chống drift và nâng độ tin cậy."
tags: [agents, openclaw, orchestration, patterns]
updated: 2026-03-18
---

# 🧩 OpenClaw Patterns

Trang này gom các **pattern thực chiến** để bạn áp dụng ngay khi triển khai orchestrator kiểu OpenClaw. Mỗi pattern đều cố gắng trả lời:

- **Khi nào dùng** (signal)
- **Cách làm** (công thức)
- **Cần đo gì** (để biết có hiệu quả)

## 1) Planning: “Plan ít nhưng kiểm soát được”

### Pattern: Two-phase planning (Outline → Execute)

- **Khi nào dùng**: task dài, nhiều nhánh; dễ bị plan “viết cho hay” nhưng không thực thi.
- **Cách làm**:
  - Phase A: tạo outline 3–7 bước, mỗi bước có `intent`, `tool_tag`, `done_criteria`.
  - Phase B: execute step-by-step, mỗi step chỉ được “nhìn” bối cảnh cần thiết (giảm drift).
- **Đo lường**:
  - Tỉ lệ step “đạt done_criteria”
  - Số tool call/step và retry rate

Pseudo-schema step:

```json
{
  "step_id": "S3",
  "intent": "Thu thập 3 nguồn đáng tin",
  "tool_tag": "search",
  "done_criteria": "Có 3 URL + trích dẫn 1-2 câu/nguồn"
}
```

### Pattern: Budget-aware plan

- **Khi nào dùng**: chạy production, cần predictable cost/latency.
- **Cách làm**:
  - Planner phải nhận `budget` và gắn budget vào từng step.
  - Nếu plan vượt budget → planner phải “nén” plan (ít step hơn, giảm breadth).
- **Đo lường**:
  - p95 cost/job
  - tỉ lệ `guard_blocked` do vượt budget

## 2) Routing: “Chọn tool như chọn worker”

### Pattern: Capability tags + tool contracts

- **Khi nào dùng**: có nhiều tool tương tự (search vs internal_search; code_exec vs sql_exec).
- **Cách làm**:
  - Tool có `tags` + `contract` (input/output schema).
  - Router chọn tool bằng match `tool_tag` + constraints (risk, sandbox, latency).
- **Đo lường**:
  - Tỉ lệ tool chọn đúng ngay lần đầu
  - Tool error rate theo tool_name

Tool contract (ví dụ):

```json
{
  "tool": "read_url",
  "input": { "url": "string" },
  "output": { "title": "string", "quotes": ["string"], "content": "string" }
}
```

### Pattern: Router fallback (primary → secondary)

- **Khi nào dùng**: tool hay fail (timeout), hoặc nguồn dữ liệu không ổn định.
- **Cách làm**:
  - Router trả về list `(tool, confidence)` thay vì 1 tool.
  - Safety/budget layer quyết định retry với tool thứ 2/3.
- **Đo lường**:
  - Recovery rate sau fallback
  - Thời gian tăng thêm do fallback

### Pattern: “Don’t use tool” route

- **Khi nào dùng**: câu hỏi đơn giản, không cần tool, tránh lãng phí.
- **Cách làm**:
  - Router có option `tool = none` nếu step chỉ là synthesis.
  - Planner phải đánh dấu step `tool_tag = none`.
- **Đo lường**:
  - Tool calls/run giảm
  - Chất lượng output không giảm (A/B)

## 3) Memory: “Ghi đúng thứ cần nhớ”

### Pattern: Three-tier memory (Scratchpad → Episodic → Long-term)

- **Scratchpad** (TTL ngắn): trạng thái chạy, intermediate results.
- **Episodic** (vector): các “mẩu” tri thức theo lần chạy.
- **Long-term** (KV/doc): facts ổn định, config, preferences.

- **Khi nào dùng**: hầu hết hệ agent production.
- **Cách làm**:
  - Scratchpad luôn có TTL và bị summarize khi dài.
  - Episodic chỉ lưu “evidence” (trích dẫn, kết quả tool) + metadata.
  - Long-term có quy trình curate (không auto-write mọi thứ).
- **Đo lường**:
  - Retrieval hit-rate
  - Hallucination rate khi có/không memory

### Pattern: Evidence-first memory

- **Khi nào dùng**: research/RAG, cần grounded outputs.
- **Cách làm**:
  - Chỉ cho phép lưu vào memory nếu có `source` (URL/doc_id) và `quote`.
  - Output bắt buộc trích dẫn theo `evidence_ids`.
- **Đo lường**:
  - Tỉ lệ claim có evidence
  - Tỉ lệ “source not found”/broken links

## 4) Anti-drift & Quality: “Giữ agent đi đúng đường”

### Pattern: Done-criteria gating

- **Khi nào dùng**: agent hay “nhảy bước”.
- **Cách làm**:
  - Sau mỗi step, chạy `step_validator` (rule/LLM) để check `done_criteria`.
  - Fail → yêu cầu planner sửa step hoặc gọi tool lại.
- **Đo lường**:
  - Step completion rate
  - Số vòng lặp validator

### Pattern: Critic/Reviewer loop (nhẹ)

- **Khi nào dùng**: output cần chất lượng (report, proposal), nhưng không muốn multi-agent phức tạp.
- **Cách làm**:
  - Một pass “review” với rubric: factuality, completeness, structure.
  - Review chỉ được phép: yêu cầu bổ sung evidence, sửa cấu trúc, phát hiện mâu thuẫn.
- **Đo lường**:
  - Edit distance trước/sau review
  - Human rating tăng bao nhiêu

## 5) Multi-agent: “Crew có kỷ luật”

### Pattern: Lead + Specialists

- **Khi nào dùng**: task gồm research + analysis + writing + verification.
- **Cách làm**:
  - **Lead**: lập kế hoạch, phân công, tổng hợp.
  - **Specialists**: mỗi agent chỉ có 1 “vai” và tool set tối thiểu.
- **Đo lường**:
  - Latency/cost tăng bao nhiêu so với single-agent
  - Chất lượng tăng có đáng không (A/B)

Ví dụ vai:

- Researcher: search/read, không được code_exec
- Analyst: synthesis + math, không được browse rộng
- Verifier: check evidence, tìm mâu thuẫn

### Pattern: Shared memory nhưng phân vùng

- **Khi nào dùng**: nhiều agent ghi vào memory → dễ rác.
- **Cách làm**:
  - Mỗi agent có namespace riêng (`research/`, `analysis/`, `verification/`).
  - Lead chỉ “promote” evidence tốt sang `final/`.
- **Đo lường**:
  - Noise ratio trong retrieval
  - Thời gian tìm evidence

## 6) “Lộ trình áp dụng patterns” (khuyến nghị)

- **Giai đoạn 1 (1–2 ngày)**: Two-phase planning + capability tags + event log.
- **Giai đoạn 2 (1 tuần)**: Evidence-first memory + done-criteria gating.
- **Giai đoạn 3 (2–4 tuần)**: Critic loop + multi-agent Lead/Specialists + OTel traces đầy đủ.

> Khi bạn muốn đi vào policy/sandbox/tracing/evaluation nghiêm túc, xem `safety-observability.md`.

