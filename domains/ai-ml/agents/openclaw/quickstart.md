---
title: "OpenClaw Quickstart"
description: "Dựng pipeline OpenClaw tối thiểu: planner → router → tools, kèm budget guard, sandbox và tracing."
tags: [agents, openclaw, orchestration, quickstart]
updated: 2026-03-18
---

# 🚀 OpenClaw Quickstart

Mục tiêu của quickstart này là dựng một “khung” orchestrator tối thiểu theo tinh thần OpenClaw:

- **Planner**: biến yêu cầu thành các bước thực thi.
- **Router**: chọn tool phù hợp cho từng bước.
- **Safety**: policy + budget + sandbox (ít nhất ở mức “khung cấu hình”).
- **Telemetry**: event log + trace để debug và đo lường.

> Lưu ý: repo hiện đang mô tả OpenClaw ở mức kiến trúc/pattern. Code dưới đây là **pseudo-code** để bạn có thể triển khai bằng framework bạn chọn.

## 1) Chọn “mục tiêu demo” có thể đo lường

Chọn bài toán nhỏ nhưng có “đầu ra kiểm chứng được”:

- **Research (grounded)**: tóm tắt 3 nguồn + trích dẫn + trả về dàn ý.
- **Data agent**: gọi 1 API + chuẩn hoá dữ liệu + xuất CSV/JSON.
- **Code/tool**: viết function + chạy unit test trong sandbox + báo cáo pass/fail.

Ví dụ task:

- “Tạo báo cáo xu hướng LLM 2026: có trích dẫn nguồn, kèm 5 bullet insight và 3 rủi ro triển khai.”

## 2) Định nghĩa schema chạy (Run/Step/ToolCall)

Schema này giúp bạn log/trace nhất quán và làm evaluator sau này.

**Run**
- `run_id`, `task`, `started_at`, `ended_at`
- `model`, `budget_tokens`, `budget_time_ms`, `max_tool_calls`
- `status` (success/failed/guard_blocked)

**Step**
- `step_id`, `intent`, `inputs`, `expected_output`
- `chosen_tool`, `tool_args`, `tool_result_ref`

**ToolCall**
- `tool_name`, `duration_ms`, `token_usage`, `cost_estimate`, `error`

## 3) Khai báo tool theo capability tags

Thiết kế tool theo hướng “rõ khả năng + rõ ràng ràng buộc”:

- `tags`: search, read, code, db, browser…
- `risk`: low/medium/high
- `sandboxed`: true/false
- `budget`: cost/time/token

Ví dụ:

```python
from openclaw import Tool

search = Tool(
    name="search",
    fn=call_search,
    tags=["search"],
    risk="low",
)

read = Tool(
    name="read_url",
    fn=fetch_and_extract,
    tags=["read"],
    risk="low",
)

code_exec = Tool(
    name="code_exec",
    fn=run_in_sandbox,
    tags=["code"],
    risk="high",
    sandboxed=True,
)
```

## 4) Lắp pipeline tối thiểu (Planner → Router → Tools)

```python
from openclaw import Planner, Router, Memory, Safety

memory = Memory(vector_store=vs, kv=kv_store, scratchpad_ttl_s=900)

safety = Safety(
    content_policy=policy_rules,
    tool_allowlist={"search", "read_url", "code_exec"},
    max_tool_calls=8,
    budget_tokens=6000,
    budget_time_ms=90_000,
)

planner = Planner(model="gpt-4o", strategy="react")
router  = Router(
    capability_index={
        "search": search,
        "read": read,
        "code": code_exec,
    }
)

def run(task: str):
    run_ctx = safety.new_run(task=task)

    plan = planner.make_plan(task, memory=memory, run_ctx=run_ctx)
    safety.check_plan(plan, run_ctx=run_ctx)

    for step in plan.steps:
        tool = router.pick(step, memory=memory, run_ctx=run_ctx)
        safety.check_before(tool, step, run_ctx=run_ctx)

        result = tool.run(step)
        safety.check_after(tool, result, run_ctx=run_ctx)

        memory.log(step, result, run_ctx=run_ctx)

    return memory.summarize(run_ctx=run_ctx)
```

## 5) Thêm event log + trace (tối thiểu)

Bạn cần “dấu vết” để trả lời 3 câu hỏi:

- Agent **đã lập kế hoạch gì** và có drift không?
- **Tool nào** được gọi, bao nhiêu lần, lỗi gì?
- **Chi phí/độ trễ** ở đâu (planner vs tool)?

Tối thiểu nên log theo event:

- `plan_created`
- `route_selected`
- `tool_call_started` / `tool_call_finished`
- `guard_blocked`
- `run_completed`

Với OpenTelemetry, quy ước đặt `span`:

- `openclaw.run`
  - `openclaw.plan`
  - `openclaw.step` (attributes: step_id, intent)
    - `openclaw.tool_call` (attributes: tool_name, sandboxed, duration)

## 6) Checklist “chạy được trong 1 ngày”

- [ ] Có `run_id` và log đủ event (plan/route/tool/guard).
- [ ] Có **max_tool_calls** và **budget_time_ms** (chặn runaway).
- [ ] Tool “nguy hiểm” (code/browser/shell) chạy trong sandbox/allowlist.
- [ ] Output có cấu trúc (JSON) để evaluator đọc được.

## 7) “Bước tiếp theo” sau quickstart

- Nếu bạn muốn nâng chất lượng: xem `patterns.md` (routing/memory/critique).
- Nếu bạn muốn productionize: xem `safety-observability.md` (policy, sandbox, OTel, evaluation).
- Nếu bạn muốn copy/paste recipe: xem `examples.md`.

