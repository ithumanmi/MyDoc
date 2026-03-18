---
title: "OpenClaw Benchmarks"
description: "Khung so sánh OpenClaw với LangGraph/AutoGen/CrewAI: tiêu chí, bài test, metrics và cách A/B."
tags: [agents, openclaw, benchmarks, evaluation]
updated: 2026-03-18
---

# 📊 Benchmarks (OpenClaw)

Mục tiêu của trang này là đưa ra **khung benchmark** để bạn so sánh:

- OpenClaw (orchestrator “nhẹ”, safety/observability-centric)
- LangGraph
- AutoGen
- CrewAI

> Thay vì cố khẳng định “cái nào tốt hơn”, benchmark tập trung vào: **đúng use case**, **chi phí/độ trễ**, **độ tin cậy**, **an toàn**, và **vận hành**.

## 1) Tiêu chí so sánh (decision matrix)

### A. Orchestration & Control

- Graph/state machine có rõ ràng không?
- Có hỗ trợ step schema + done-criteria gating không?
- Router có capability tags + fallback không?
- Có multi-agent “role isolation” không?

### B. Safety

- Tool allowlist / role-based permissions
- Budget guards (time/tokens/tool calls)
- Sandbox integration (code/browser/shell)
- Prompt injection mitigations (pre/post tool policy checks)

### C. Observability

- Event log (structured) có sẵn không?
- OpenTelemetry traces có dễ gắn không?
- Replay runs (offline eval) có workflow không?
- Có cost/tokens accounting không?

### D. DX & Ecosystem

- Dễ bắt đầu (quickstart) đến mức nào?
- Plugin/tool ecosystem
- Tài liệu, community, examples
- Khả năng mở rộng (custom tools, custom routing)

### E. Production concerns

- Determinism / reproducibility (seed, run capture)
- Versioning (prompts/tools/policies)
- Error handling (timeouts, retries, circuit breakers)
- Security posture (secret handling, redaction logs)

## 2) Bài benchmark đề xuất (3 mức)

### Level 1: “Single-agent + multi-tool” (baseline)

- Task: Research grounded (search/read/summarize, evidence required).
- Tool set: search + read_url.
- Output: claims có evidence.

**Metrics**
- claim_with_evidence_rate
- latency p95
- cost/job
- tool_error_rate

### Level 2: “Tool risk + sandbox” (safety stress test)

- Task: Code/tool agent chạy test trong sandbox.
- Tool set: code_exec + run_tests.
- Output: patch summary + test result.

**Metrics**
- sandbox_time_ms
- test_pass_rate
- guard_block_rate (theo lý do)
- retry_count

### Level 3: “Multi-agent crew” (coordination)

- Task: Research crew (Lead/Researcher/Verifier) tạo báo cáo có review.
- Tool set: search/read + verifier rubric.

**Metrics**
- quality score (rubric/human)
- coordination overhead (latency/cost delta vs single-agent)
- contradiction_rate

## 3) Cách thiết kế A/B test công bằng

- **Cố định tool set**: cùng endpoints, cùng rate limit.
- **Cố định budget**: cùng max_tool_calls, budget_time_ms, budget_tokens/cost.
- **Cố định dataset**:
  - 20–50 tasks “chuẩn hoá” (có expected output/rubric).
  - phân nhóm theo độ khó.
- **Ghi lại run artifacts**:
  - plan, route decisions, tool calls, outputs, errors.
- **Đánh giá blind** (nếu có human eval): che framework.

## 4) Bảng so sánh (template)

| Nhóm | Tiêu chí | OpenClaw | LangGraph | AutoGen | CrewAI |
|------|----------|----------|-----------|---------|--------|
| Control | Graph/state machine rõ | TBD | TBD | TBD | TBD |
| Control | Done-criteria gating | TBD | TBD | TBD | TBD |
| Safety | Tool allowlist/roles | TBD | TBD | TBD | TBD |
| Safety | Sandbox integration | TBD | TBD | TBD | TBD |
| Obs | Event log structured | TBD | TBD | TBD | TBD |
| Obs | OTel tracing | TBD | TBD | TBD | TBD |
| Prod | Replay runs | TBD | TBD | TBD | TBD |
| DX | Ecosystem/tools | TBD | TBD | TBD | TBD |

> Điền “TBD” bằng kết quả đo thực tế trong môi trường của bạn. Thường khác biệt lớn nhất nằm ở safety/observability và DX.

## 5) Kết quả nên trình bày thế nào (để ra quyết định)

- 1 trang summary:
  - framework nào đạt target quality
  - framework nào rẻ hơn/nhanh hơn ở p95
  - framework nào dễ vận hành (logs/traces, replay, policy)
- 1 trang appendix:
  - dataset + rubric
  - cấu hình budget/guard
  - hạn chế của benchmark

