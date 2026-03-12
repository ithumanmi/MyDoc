# 🧠 LLMOps Playbook

> [← Back to MLOps](./README.md)

MLOps cho Large Language Models cần thêm lớp quản lý prompt, context, cost và guardrails.

---

## 1. Khác biệt LLMOps vs MLOps truyền thống

- **Prompt & Context:** Prompt như "source code" mới, cần version control.
- **Evaluation khó:** Không chỉ accuracy — cần đánh giá factuality, toxicity.
- **Observability:** Log prompt/response, token usage, latency, user feedback.
- **Cost control:** Theo dõi token/s request, batch inference.

---

## 2. Pipeline tổng quan

1. **Prompt Engineering:** thiết kế template, system prompt, guardrails.
2. **Retrieval / Context:** RAG, tool selection, memory.
3. **Evaluation:** offline (Ragas, GPT Judge) + online A/B testing.
4. **Deployment:** serverless (vLLM, Triton), autoscaling.
5. **Monitoring:** latency, hallucination, harmful content, cost.

---

## 3. Prompt Management

- Lưu prompt template trong repo (YAML/JSON) + git history.
- Tạo prompt library theo use case (support, coding, analytics).
- Tích hợp **prompt version** vào request để trace.
- Tools: PromptLayer, Humanloop, OpenPipe.

---

## 4. Evaluation & A/B

- **Offline:** human-labeled dataset (question, reference answer) → dùng LLM judge (GPT-4, Claude) chấm điểm.
- **Metrics:** relevance, groundedness, style, safety.
- **Online:** multi-armed bandit, holdout traffic cho model/prompt mới.

```python
from ragas.metrics import context_precision, faithfulness
score = context_precision().score(dataset)
```

---

## 5. Observability & Guardrails

- Log toàn bộ request: prompt, response, latency, tokens.
- Detect PII, profanity, jailbreak bằng policy engine (OpenAI moderation, Azure Content Safety, Llama Guard).
- Feedback loop: nút 👍/👎 trong UI → gửi về system để retrain/promote prompt.

---

## 6. Cost & Performance

- Batch requests (vLLM), streaming response để tăng UX.
- Cache kết quả (Redis, SQLite) cho câu lặp lại.
- Theo dõi chi phí theo team/use case, cảnh báo khi vượt budget.
- Tận dụng mô hình local/quantized (Llama.cpp, GPTQ) cho workload nhạy cảm.

---

## 7. Tooling đề xuất

| Layer | Công cụ |
| --- | --- |
| Prompt Mgmt | PromptLayer, Humanloop, OpenPipe |
| Eval | Ragas, DeepEval, Promptfoo |
| Deployment | vLLM, TensorRT-LLM, AWS Bedrock, Vertex AI, Azure OpenAI |
| Monitoring | Langfuse, Arize LLM, HoneyHive, Helicon |

> 🎯 Tip: thiết lập "LLM Runbook" mô tả quy trình khi model trả lời sai/harmful (rollback prompt, khởi động review team).
