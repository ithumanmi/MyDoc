---
title: "OpenClaw Safety & Observability"
description: "Thiết kế safety guard và observability cho orchestrator kiểu OpenClaw: policy, sandbox, budget guard, OTel tracing, evaluation."
tags: [agents, openclaw, safety, observability, otel, evaluation]
updated: 2026-03-18
---

# 🛡️ Safety & Observability (OpenClaw)

Nếu bạn muốn OpenClaw “chạy production”, đây là 2 trụ:

- **Safety**: ngăn hành vi nguy hiểm (policy + sandbox + budget).
- **Observability**: nhìn thấy agent đang làm gì để debug, tối ưu, đánh giá.

## 1) Threat model nhanh (để biết mình đang bảo vệ cái gì)

### Rủi ro thường gặp

- **Runaway agent**: vòng lặp tool call, tốn chi phí, không kết thúc.
- **Tool misuse**: gọi tool sai mục đích (exfiltration, destructive actions).
- **Data leakage**: lộ PII/secret qua log/trace hoặc prompt.
- **Prompt injection**: doc/web content ép agent làm sai policy.
- **Supply chain**: tool “đọc web” kéo nội dung độc (JS, payload).

### Nguyên tắc

- **Default-deny** với tool nguy hiểm.
- **Sandbox** là bắt buộc với code/browser/shell.
- **Budget guard** phải ở cấp orchestrator, không dựa vào “LLM tự kiềm chế”.
- **Logs/traces** phải scrub/redact trước khi lưu lâu dài.

## 2) Safety layer: 4 lớp guard cần có

### (A) Content policy guard

Mục tiêu: chặn nội dung/ý định vi phạm (PII, tự hại, hướng dẫn phạm pháp… tuỳ hệ thống).

Gợi ý triển khai:

- Rule-based nhanh (regex/keyword) cho “hard deny”.
- LLM-based classifier cho vùng xám.
- Policy check ở 2 điểm:
  - **Pre-tool** (trước khi gọi tool)
  - **Post-tool** (sau khi nhận kết quả tool, trước khi đưa vào memory/output)

### (B) Tool allowlist + action gating

Mục tiêu: tool nguy hiểm chỉ được gọi khi đủ điều kiện.

- **Allowlist theo môi trường**: dev/staging/prod khác nhau.
- **Allowlist theo role**: agent role khác nhau (researcher không có code_exec).
- **Action gating**: tool “write/delete/transfer money” phải có:
  - human approval, hoặc
  - “dry-run + diff”, hoặc
  - idempotency key + rollback plan

### (C) Budget guard (tokens/time/tool calls)

Mục tiêu: giới hạn chi phí và tránh loop.

Nên có:

- `max_tool_calls`
- `budget_time_ms`
- `budget_tokens` (hoặc cost estimate)
- `max_retries_per_tool`
- `max_plan_steps`

Và chính sách khi chạm ngưỡng:

- “Stop & summarize progress”
- “Return partial result + missing items”
- “Ask user for narrow scope / increased budget” (nếu có UX)

### (D) Sandbox guard cho tool nguy hiểm

Mục tiêu: dù agent bị prompt injection, tool vẫn không thể phá hệ thống.

Sandbox tối thiểu:

- **CPU/memory/time limit**
- **No network** (hoặc egress allowlist)
- **Readonly filesystem** (trừ workspace temp)
- **Process isolation**

Nếu có browser automation:

- cấm download tuỳ tiện
- disable credential access
- network allowlist

## 3) Observability: bạn cần nhìn thấy gì?

### Event log (structured)

Log dạng event giúp query và replay dễ:

- `plan_created`
- `step_started` / `step_finished`
- `route_selected`
- `tool_call_started` / `tool_call_finished`
- `guard_blocked`
- `memory_write`
- `run_completed`

Thuộc tính tối thiểu:

- `run_id`, `step_id`
- `tool_name`, `tool_tags`, `sandboxed`
- `duration_ms`, `error_type`
- `token_usage`, `cost_estimate`

### OpenTelemetry traces (OTel)

Trace giúp bạn thấy critical path:

- `openclaw.run`
  - `openclaw.plan`
  - `openclaw.step`
    - `openclaw.route`
    - `openclaw.tool_call`
    - `openclaw.guard_check`

Các attribute nên có:

- `run.id`, `step.id`
- `llm.model`, `llm.tokens.prompt`, `llm.tokens.completion`
- `tool.name`, `tool.sandboxed`
- `guard.result` (pass/block), `guard.reason`

### Redaction / privacy

Trước khi log:

- scrub token/secret (API keys)
- hash/anonymize PII
- không log raw content của tài liệu nhạy cảm (log reference + excerpt có giới hạn)

## 4) Evaluation: đo agent như đo hệ thống

### Offline evaluation (replay)

- Lưu `run trace` + `inputs` + `expected outputs` (nếu có).
- Replay với model/tool phiên bản mới để so sánh:
  - success rate
  - latency/cost
  - safety violations

### Online evaluation (production)

Chỉ số nên có:

- **Task success %** (hoặc proxy: user resolved)
- **Factuality / groundedness** (tỉ lệ claim có evidence)
- **Hallucination rate**
- **Latency p95**
- **Cost/job**
- **Tool error rate**
- **Guard block rate** (chia theo lý do)

### Rubric gợi ý cho “report/research”

- Structure (đúng format yêu cầu)
- Evidence coverage (mỗi claim quan trọng có trích dẫn)
- Consistency (không mâu thuẫn)
- Actionability (khuyến nghị có bước tiếp theo)

## 5) Playbook xử lý sự cố (ngắn)

- **Agent loop / runaway**:
  - tăng strictness của `max_tool_calls`, `max_plan_steps`
  - thêm done-criteria gating (xem `patterns.md`)
  - log route/tool để tìm “step nào gây loop”
- **Tool timeouts**:
  - router fallback (primary → secondary)
  - circuit breaker theo tool
- **Prompt injection**:
  - pre/post tool policy checks
  - treat web/doc content là “untrusted input”
  - disable tool calls dựa trên instructions trong retrieved content

## 6) Checklist production-ready

- [ ] Tool allowlist theo environment + role.
- [ ] Budget guard đầy đủ (time/tokens/tool calls/retries).
- [ ] Sandbox cho tool nguy hiểm + egress allowlist.
- [ ] Log event structured + OTel traces.
- [ ] Redaction pipeline cho logs/traces.
- [ ] Offline replay evaluation + dashboard online metrics.

