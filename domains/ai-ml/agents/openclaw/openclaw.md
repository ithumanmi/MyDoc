---
title: "OpenClaw – Agent Orchestrator"
description: "Tổng quan, kiến trúc và thực hành nhanh với OpenClaw (agent orchestrator: planning, tool routing, safety guard)."
tags: [agents, orchestration, openclaw, planning]
updated: 2026-03-18
---

# 🦾 OpenClaw – Agent Orchestrator

> OpenClaw là một orchestrator tập trung vào **planning**, **tool routing** và **safety guard**. Bài này tóm tắt thành phần, use case, cách khởi động nhanh và checklist vận hành.

## TL;DR
- Thiết kế kiểu **graph/state machine**: task → planner → router → worker tools (LLM, retriever, API, code exec).
- **Safety-first**: policy check, budget guard (token/time), sandbox cho tool nguy hiểm.
- Phù hợp cho **multi-tool** / **multi-step** workflow (data agent, research agent, code-assist có kiểm soát).

## Kiến trúc lõi
1) **Planner**: phân rã goal thành bước (ReAct/ToT) + metadata (priority, deadline, budget).
2) **Router**: chọn worker/tool dựa trên `capability tags` (search, code, db, browser, ml-train…).
3) **Memory**: short-term (scratchpad), episodic (vector store), long-term (key-value / doc store).
4) **Safety Layer**: 
   - Content & tool policy (regex/LLM-based),
   - Budget guard (max tokens/time/tools),
   - Sandboxed exec (code, browser, shell -> allowlist + resource limit).
5) **Telemetry**: event log (plan, route, tool_call, error), traces (OpenTelemetry), run metadata (latency, cost, success rate).

```
User Task → Planner → Router ─┬─ Tool A (Search/RAG)
                              ├─ Tool B (Code Exec Sandbox)
                              └─ Tool C (API/DB)
           ↑ memory (scratchpad/vector)   ↑ safety/telemetry
```

## Khi nào chọn OpenClaw?
- Cần **kiểm soát an toàn**: sandbox code/browser, hạn mức tool call, policy trước/sau tool.
- Bài toán **multi-step, multi-tool** nhưng không muốn phụ thuộc nặng vào framework lớn (LangChain/LangGraph).
- Muốn **log & trace chuẩn** (OTel), dễ gắn vào pipeline CI/CD hoặc data platform.

So sánh nhanh:
- **OpenClaw**: nhẹ, kiểm soát tool/safety, log/trace rõ.
- **LangGraph/AutoGen/CrewAI**: giàu tính năng sẵn, cộng đồng lớn; phù hợp khi cần ecosystem plugin.
- **Swarm-like (minimal orchestrator)**: tối giản, nhưng phải tự làm safety/observability.

## Quickstart (pseudo-code, Python)

```python
from openclaw import Planner, Router, Memory, Safety, Tool

# Khai báo tool
search = Tool(name="search", fn=call_search, tags=["search"], cost_limit=0.01)
code   = Tool(name="code_exec", fn=run_in_sandbox, tags=["code"], sandbox=True)

memory = Memory(vector_store=vs, kv=kv_store)
safety = Safety(content_policy=allowlist_regex, budget_tokens=6000, max_tool_calls=8)

planner = Planner(model="gpt-4o", strategy="react")
router  = Router(capability_index={"search": search, "code": code})

def run(task: str):
    plan = planner.make_plan(task, memory=memory)
    for step in plan.steps:
        tool = router.pick(step, memory=memory)
        safety.check_before(tool, step)
        result = tool.run(step)
        safety.check_after(tool, result)
        memory.log(step, result)
    return memory.summarize()

print(run("Tạo báo cáo xu hướng LLM 2026, trích dẫn nguồn và tính chi phí inference"))
```

> Gợi ý: bọc `run` bằng trace decorator (OTel), lưu event vào lake/warehouse để đánh giá agent.

## Checklist triển khai
- [ ] Định nghĩa policy: content allow/deny, tool allowlist, sandbox resource limit.
- [ ] Thiết kế schema `Run → Steps → ToolCalls` + metadata (latency, tokens, cost, outcome).
- [ ] Chọn storage cho memory (vector + KV) và TTL cho scratchpad.
- [ ] Thêm evaluator (offline/online): success rate, factuality, latency, cost, coverage.
- [ ] Thiết lập canary: so sánh agent vs pipeline baseline (non-agent) trước khi mở rộng.

## Mẫu kiến trúc tham khảo
- **Retrieval Agent**: Planner → Router → (Search→Rerank→Read) → Synthesis → Guardrail.
- **Code/Tool Agent**: Planner → Router → (CodeExec Sandbox, API, DB) → Tests → Report.
- **Research Crew (multi-agent)**: Lead (planning) + Researcher (search) + Analyst (synthesis) + Reviewer (critique). OpenClaw giữ vai trò orchestrator + policy.

## Quan sát & Đo lường
- **Chỉ số chính:** task success %, factuality, hallucination rate, latency p95, cost/job, tool error rate.
- **Log chuẩn:** event-level (plan, route, tool_call, guard_fail), token usage, retries.
- **Replays:** lưu trace để replay với model mới → giảm chi phí A/B.

## Rủi ro & Lưu ý
- Guardrail không hoàn hảo: cần combine rule + LLM check, và luôn sandbox tool nguy hiểm.
- Kế hoạch dài dễ drift: giới hạn depth/steps; dùng summarization cho scratchpad.
- Với dữ liệu nhạy cảm: tách hạ tầng private, mã hóa dữ liệu trong log/trace.

## Tài nguyên đề xuất
- Blog/whitepaper về **agent orchestration & safety** (policy, sandbox, OTel tracing).
- Mẫu **OTel + LLM/Agents semantic conventions** để chuẩn hóa log/traces.
- **RAG & Memory**: xem [Graph RAG](./advanced/graph-rag.md), [Memory Architecture](./advanced/memory-architecture.md).
