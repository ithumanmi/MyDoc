# 🗺️ AI Engineering Roadmap 2026

> [← Back to AI/ML Roadmap](./README.md)
>
> Lộ trình 9 bước từ nền tảng code đến AI production-ready, với **Agents & Orchestration** là bước then chốt sau RAG và trước MLOps.

---

## Tổng quan: 9 bước tuần tự

| # | Giai đoạn | Trọng tâm | Liên kết nội dung |
|:--|:----------|:----------|:------------------|
| 1 | **Foundation** | Production-ready Python & APIs | [Python Data Stack](./fundamentals/python-data-stack.md) |
| 2 | **Semantic Intelligence** | Embeddings & Vector Search | [Transformers & LLM](./nlp/transformers-llm.md), Vector DB / RAG cơ bản |
| 3 | **RAG Systems** | Grounded AI, giảm hallucination | [Graph RAG](./agents/advanced/graph-rag.md) |
| 4 | **Agents & Orchestration** | Multi-agent, Planning, Tool use | **[Agents](./agents/)** ⬅️ *Trọng tâm* |
| 5 | **MLOps & Production** | CI/CD, Containerization, IaC | [Deployment](./mlops/deployment-pipeline.md), [CI/CD for AI](./mlops/cicd-for-ai.md) |
| 6 | **Evaluation, Monitoring & Safety** | Metrics, Drift, Bias | [AI Monitoring](./mlops/ai-monitoring.md), [Evaluating Agents](./agents/advanced/evaluating-agents.md), [Responsible AI](./generative-ai/responsible-ai.md) |
| 7 | **Advanced Inference & Cost** | Serving, Quantization, Caching | MLOps, Optimization *(mở rộng sau)* |
| 8 | **Portfolio & Real Projects** | Dự án thực tế | [Agent Use Cases](./agents/agent-use-cases.md) |
| 9 | **Continuous Learning** | Cập nhật, nghiên cứu, chọn domain (CV, NLP, RL) | Roadmap chuyên sâu từng nhánh |

---

## 1. Foundation: Production-Ready Python & APIs

*Clean, scalable code, data structures, git.*

- Nền tảng để mọi pipeline AI (data, API, deployment) chạy ổn định.
- **Trong repo:** [Python Data Stack](./fundamentals/python-data-stack.md), [Math for ML](./fundamentals/math-for-ml.md).

---

## 2. Semantic Intelligence: Embeddings & Vector Search

*Vector DBs, Transformers.*

- Hiểu và biểu diễn ngữ nghĩa (embeddings), tìm kiếm theo nghĩa (vector search).
- Nền tảng cho RAG và cho Agent “hiểu” và truy vấn tri thức.
- **Trong repo:** [Transformers & LLMs](./nlp/transformers-llm.md).

---

## 3. RAG Systems: Grounded AI Outputs

*Reduce hallucinations, connect to external knowledge.*

- Retrieval-Augmented Generation: kết nối LLM với nguồn dữ liệu bên ngoài.
- **Trong repo:** [Graph RAG, Hybrid Search, Reranking](./agents/advanced/graph-rag.md).

---

## 4. Agents & Orchestration: Autonomous Workflows

*Multi-agent systems, planning, tool use.*

Đây là bước **trung tâm** của lộ trình AI Engineering 2026: từ “model gọi API” sang **hệ thống tự quyết định, lập kế hoạch và dùng công cụ**.

- **Kiến trúc:** [Agent Architecture](./agents/agent-architecture.md) — LLM + Memory + Planning + Tools.
- **Frameworks:** [Agent Frameworks](./agents/agent-frameworks.md) — LangChain, LangGraph, AutoGen, CrewAI.
- **Hợp tác:** [Multi-Agent Collaboration](./agents/multi-agent-collaboration.md).
- **Tự chủ:** [Autonomous Agents](./agents/autonomous-agents.md).
- **Nâng cao:** [Design Patterns](./agents/advanced/design-patterns.md), [Memory](./agents/advanced/memory-architecture.md), [Evaluation](./agents/advanced/evaluating-agents.md), [Human-in-the-loop](./agents/advanced/human-in-the-loop.md).

👉 **Mục lục đầy đủ:** [Agents — Mục lục & Lộ trình](./agents/README.md).

---

## 5. MLOps & Production Engineering

*CI/CD, Containerization, Infra as Code.*

- Đưa pipeline và Agent lên production, tái lập được, scale được.
- **Trong repo:** [Deployment Pipeline](./mlops/deployment-pipeline.md), [CI/CD for AI](./mlops/cicd-for-ai.md).

---

## 6. Evaluation, Monitoring & Safety

*Metrics, Drift detection, Bias auditing.*

- Đo chất lượng, phát hiện trôi dạt, kiểm tra thiên lệch.
- **Trong repo:** [AI Monitoring](./mlops/ai-monitoring.md), [Evaluating Agents](./agents/advanced/evaluating-agents.md), [Responsible AI](./generative-ai/responsible-ai.md).

---

## 7. Advanced Inference & Cost Optimization

*Efficient serving, Quantization, Caching.*

- Tối ưu latency và chi phí khi serve model (kể cả model trong Agent).

---

## 8. Portfolio & Real Projects

*Portfolio & real projects.*

- Áp dụng toàn bộ lộ trình vào sản phẩm/dự án thật.
- **Trong repo:** [Agent Use Cases](./agents/agent-use-cases.md).

---

## 9. Continuous Learning & Specialization

*Stay updated, explore research, pick a domain: CV, NLP, RL.*

- Cập nhật nghiên cứu mới, chọn chuyên sâu: Computer Vision, NLP, Reinforcement Learning (và Agents).

---

## 🔗 Liên kết nhanh

- **Bắt đầu từ Agents:** [Agents README](./agents/README.md)  
- **Roadmap tổng thể AI/ML:** [AI/ML Roadmap](./README.md)  
- **Visual roadmap (Mermaid):** Xem [README](./README.md#-visual-roadmap)
