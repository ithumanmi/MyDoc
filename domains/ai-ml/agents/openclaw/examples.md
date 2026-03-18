---
title: "OpenClaw Examples"
description: "Recipe end-to-end cho OpenClaw: research grounded, code/tool sandbox, data/API agent; kèm checklist đo lường."
tags: [agents, openclaw, examples, orchestration]
updated: 2026-03-18
---

# 🍳 Examples (OpenClaw Recipes)

Các recipe dưới đây được viết theo cùng một khuôn:

- **Goal**
- **Tools & Guards**
- **Plan template**
- **Output contract**
- **Telemetry & Metrics**
- **Failure modes** (để debug nhanh)

> Đây là pseudo-code + cấu trúc vận hành. Bạn có thể hiện thực bằng bất kỳ stack nào, miễn giữ đúng “shape” orchestrator: planner → router → tools + safety + telemetry.

---

## Recipe 1: Grounded Research Agent (Search → Read → Synthesize)

### Goal

Tạo báo cáo ngắn (1–2 trang) về một chủ đề, **có trích dẫn nguồn** và tách rõ:

- Insight chính
- Bằng chứng (quotes/URLs)
- Rủi ro/điểm chưa chắc

### Tools & Guards

- **Tools**
  - `search(query) -> [url]`
  - `read_url(url) -> {title, content, quotes}`
  - `rerank(passages) -> ranked_passages` (tuỳ chọn)
- **Guards**
  - content policy (chặn prompt injection từ web)
  - budget guard: `max_tool_calls`, `budget_time_ms`
  - evidence-first memory: chỉ lưu nếu có `source` + `quote`

### Plan template (gợi ý)

1) Xác định scope + câu hỏi con (3–5).
2) Search theo từng câu hỏi con (breadth có kiểm soát).
3) Read 3–8 URL (tuỳ budget) và trích quotes.
4) Tổng hợp: claims ↔ evidence.
5) Review: tìm mâu thuẫn / thiếu evidence.

### Output contract (JSON-friendly)

```json
{
  "topic": "string",
  "summary": "string",
  "insights": [
    {
      "claim": "string",
      "evidence": [
        { "source": "url-or-doc_id", "quote": "string" }
      ]
    }
  ],
  "risks_and_unknowns": ["string"],
  "sources": ["string"]
}
```

### Telemetry & Metrics

- **Metrics**
  - claim_with_evidence_rate
  - broken_source_rate
  - cost/job, latency p95
- **Key events**
  - `evidence_collected` (attributes: url, quote_count)
  - `claim_generated` (attributes: evidence_count)

### Failure modes

- **Hallucination**: claim không có evidence → bật done-criteria gating.
- **Prompt injection**: web content yêu cầu gọi tool nguy hiểm → treat content as untrusted, block by policy.
- **Runaway search**: search quá nhiều → giới hạn breadth/step + max URLs.

---

## Recipe 2: Code/Tool Agent (Sandboxed code_exec + tests)

### Goal

Nhận yêu cầu kỹ thuật nhỏ (viết function/patch nhỏ), chạy test trong sandbox, trả báo cáo:

- thay đổi gì
- test pass/fail
- rủi ro còn lại

### Tools & Guards

- **Tools**
  - `read_repo(path_glob) -> files`
  - `apply_patch(patch) -> diff` (nếu môi trường cho phép)
  - `code_exec(cmd, files) -> {stdout, stderr, exit_code}`
  - `run_tests() -> result`
- **Guards**
  - tool allowlist theo environment (prod không cho write)
  - sandbox: no network, time limit
  - action gating: “dry-run + diff” trước khi ghi

### Plan template (gợi ý)

1) Hiểu yêu cầu + xác định file liên quan.
2) Đề xuất patch nhỏ nhất có thể.
3) Run unit tests trong sandbox.
4) Nếu fail: debug tối đa N vòng.
5) Báo cáo + đề xuất bước tiếp theo.

### Output contract

```json
{
  "change_summary": ["string"],
  "tests": { "status": "pass|fail", "details": "string" },
  "diff_overview": "string",
  "remaining_risks": ["string"]
}
```

### Telemetry & Metrics

- **Metrics**
  - patch_attempts_per_task
  - test_pass_rate
  - time_in_sandbox_ms
- **Key events**
  - `patch_proposed`
  - `tests_run` (attributes: status, duration)

### Failure modes

- **Infinite debug loop**: cap retries; nếu còn fail → trả “partial” kèm diagnosis.
- **Tool overreach**: agent muốn chạy shell tuỳ ý → allowlist commands.

---

## Recipe 3: Data/API Agent (Fetch → Normalize → Export)

### Goal

Gọi một (hoặc vài) API, chuẩn hoá dữ liệu, xuất ra JSON/CSV; có kiểm soát rate limit và idempotency.

### Tools & Guards

- **Tools**
  - `http_get(url, headers) -> json`
  - `transform(json) -> rows`
  - `export_csv(rows) -> file_ref`
- **Guards**
  - rate limit guard + retry with backoff
  - schema validation (fail fast nếu thiếu field)
  - budget guard theo số request

### Plan template (gợi ý)

1) Khai báo schema đầu ra (cột nào).
2) Fetch dữ liệu (paginate nếu cần).
3) Normalize + validate.
4) Export + summary stats (row count, missing rate).

### Output contract

```json
{
  "output_files": ["string"],
  "row_count": 0,
  "missing_value_rate": { "field": 0.0 },
  "notes": ["string"]
}
```

### Telemetry & Metrics

- **Metrics**
  - requests_per_run
  - api_error_rate
  - rows_exported
- **Key events**
  - `api_fetch` (attributes: status_code, page)
  - `schema_validation_failed`

### Failure modes

- **API instability**: fallback endpoint, circuit breaker.
- **Schema drift**: versioned schema + alert.

---

## “Lộ trình áp dụng recipe” (khuyến nghị)

- **Tuần 1**: Recipe 1 (Research) để hoàn thiện evidence-first + logging.
- **Tuần 2**: Recipe 3 (Data/API) để hoàn thiện budget/rate-limit + schema validation.
- **Tuần 3–4**: Recipe 2 (Code/Tool) để hoàn thiện sandbox + action gating + test loop.

