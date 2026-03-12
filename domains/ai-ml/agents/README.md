# 🤖 AI Agents & Orchestration

> [← Back to AI/ML Roadmap](../README.md) | [🗺️ AI Engineering Roadmap 2026](../ai-engineering-roadmap-2026.md)
>
> **Vị trí trong lộ trình 2026:** Bước **4** — sau Semantic Intelligence & RAG, trước MLOps & Evaluation.  
> *Multi-agent systems, planning, tool use.*

---

## Agents trong AI Engineering Roadmap 2026

Agents & Orchestration là bước nối **RAG (grounded outputs)** với **production (MLOps, monitoring)**. Ở đây bạn học cách xây hệ thống AI **tự quyết định**, **lập kế hoạch** và **dùng công cụ** thay vì chỉ gọi một lần LLM.

---

## 📚 Mục lục

### Core (Kiến trúc & Công cụ)
*   **[Agent Architecture](./agent-architecture.md):** Giải phẫu Agent = LLM + Memory + Planning + Tools.
*   **[Agent Frameworks](./agent-frameworks.md):** LangChain, LangGraph, AutoGen, CrewAI.
*   **[Multi-Agent Collaboration](./multi-agent-collaboration.md):** Nhiều Agent hợp tác giải quyết bài toán phức tạp.
*   **[Autonomous Agents](./autonomous-agents.md):** AutoGPT, BabyAGI và hướng phát triển AI tự chủ.
*   **[Agent Use Cases](./agent-use-cases.md):** Ứng dụng thực tế.

### Advanced (Chuyên sâu)
*   **[Graph RAG](./advanced/graph-rag.md):** GraphRAG, Hybrid Search, Reranking — RAG cho Agent.
*   **[Memory Architecture](./advanced/memory-architecture.md):** MemGPT, bộ nhớ dài hạn.
*   **[Design Patterns](./advanced/design-patterns.md):** Reflection, Planning (ToT), Tool Selection.
*   **[Local Agents](./advanced/local-agents.md):** Chạy Agent offline (Ollama, Llama.cpp).
*   **[Evaluating Agents](./advanced/evaluating-agents.md):** RAGAS, AgentBench.
*   **[Human-in-the-Loop](./advanced/human-in-the-loop.md):** Tương tác người–máy, streaming, UX.

---

## 🧭 Học theo thứ tự gợi ý

1. **[Agent Architecture](./agent-architecture.md)** → Hiểu LLM + Memory + Planning + Tools.
2. **[Agent Frameworks](./agent-frameworks.md)** → Chọn stack (LangChain/LangGraph, AutoGen, CrewAI).
3. **[Design Patterns](./advanced/design-patterns.md)** → ReAct, Planning, Tool use.
4. **[Graph RAG](./advanced/graph-rag.md)** & **[Memory](./advanced/memory-architecture.md)** → Nâng cấp RAG và bộ nhớ.
5. **[Multi-Agent](./multi-agent-collaboration.md)** & **[Autonomous](./autonomous-agents.md)** → Hệ nhiều Agent và tự chủ.
6. **[Evaluating Agents](./advanced/evaluating-agents.md)** & **[Human-in-the-Loop](./advanced/human-in-the-loop.md)** → Chất lượng và vận hành.

---

## 🔗 Xem thêm

*   **Lộ trình 9 bước đầy đủ:** [AI Engineering Roadmap 2026](../ai-engineering-roadmap-2026.md).
*   **RAG trước khi vào Agents:** [Graph RAG](./advanced/graph-rag.md), [Transformers & LLMs](../nlp/transformers-llm.md).
*   **Sau Agents:** [MLOps](../mlops/deployment-pipeline.md), [Evaluating Agents](./advanced/evaluating-agents.md), [Responsible AI](../generative-ai/responsible-ai.md).
*   **Automation patterns ngoài AI:** [MMO Engineering](../../mmo-engineering/README.md) — mô hình điều phối bot/fleet giúp học pattern tự động hoá quy mô lớn.
