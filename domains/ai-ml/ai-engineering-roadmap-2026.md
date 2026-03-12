# 🗺️ AI Engineering Roadmap 2026

> [← Back to AI/ML Roadmap](./README.md)
>
> Lộ trình 9 bước từ nền tảng code đến AI production-ready, với **Agents & Orchestration** là bước then chốt sau RAG và trước MLOps.

---

## Tổng quan: 9 bước tuần tự

| # | Giai đoạn | Trọng tâm | Liên kết nội dung |
|:--|:----------|:----------|:------------------|
| 1 | **Foundation** | Production-ready Python & APIs | [Python Data Stack](./fundamentals/python-data-stack.md) |
| 2 | **Classic ML Systems** | Supervised/Unsupervised, Feature & Ensemble workflow | [Supervised](./machine-learning/supervised-learning.md), [Unsupervised](./machine-learning/unsupervised-learning.md), [Ensemble](./machine-learning/ensemble-methods.md) |
| 3 | **Semantic Intelligence** | Embeddings & Vector Search | [Transformers & LLM](./nlp/transformers-llm.md), Vector DB / RAG cơ bản |
| 4 | **RAG Systems** | Grounded AI, giảm hallucination | [Graph RAG](./agents/advanced/graph-rag.md) |
| 5 | **Agents & Orchestration** | Multi-agent, Planning, Tool use | **[Agents](./agents/)** ⬅️ *Trọng tâm* |
| 6 | **MLOps & Production** | CI/CD, Containerization, IaC | [Deployment](./mlops/deployment-pipeline.md), [CI/CD for AI](./mlops/cicd-for-ai.md) |
| 7 | **Evaluation, Monitoring & Safety** | Metrics, Drift, Bias | [AI Monitoring](./mlops/ai-monitoring.md), [Evaluating Agents](./agents/advanced/evaluating-agents.md), [Responsible AI](./generative-ai/responsible-ai.md) |
| 8 | **Advanced Inference & Cost** | Serving, Quantization, Scaling | [Efficient Inference](./advanced/efficient-inference.md), [Cost Optimization](./machine-learning/cost-optimization.md), [Distributed Training](./advanced/distributed-training.md) |
| 9 | **Portfolio & Continuous Learning** | Dự án thực tế + chọn domain (CV, NLP, RL) | [Agent Use Cases](./agents/agent-use-cases.md), [Labs & Projects](./labs/README.md), roadmap chuyên sâu |

---

## 1. Foundation: Production-Ready Python & APIs

*Clean, scalable code, data structures, git.*

- Nền tảng để mọi pipeline AI (data, API, deployment) chạy ổn định.
- **Trong repo:** [Python Data Stack](./fundamentals/python-data-stack.md), [Math for ML](./fundamentals/math-for-ml.md).

---

## 2. Classic ML Systems: Supervised → Feature → Ensemble

*Regression/classification, clustering, feature workflow, model selection.*

- Xây nền tảng pipeline Machine Learning truyền thống trước khi sang LLM.
- Thực hành đầy đủ từ feature engineering, selection đến ensemble & deployment template.
- **Trong repo:** [Supervised Learning](./machine-learning/supervised-learning.md), [Unsupervised Learning](./machine-learning/unsupervised-learning.md), [Ensemble Methods](./machine-learning/ensemble-methods.md), [Feature Engineering](./machine-learning/feature-engineering.md), [Feature Selection](./machine-learning/feature-selection.md).

---

## 3. Semantic Intelligence: Embeddings & Vector Search

*Vector DBs, Transformers.*

- Hiểu và biểu diễn ngữ nghĩa (embeddings), tìm kiếm theo nghĩa (vector search).
- Nền tảng cho RAG và cho Agent “hiểu” và truy vấn tri thức.
- **Trong repo:** [Transformers & LLMs](./nlp/transformers-llm.md).

---

## 4. RAG Systems: Grounded AI Outputs

*Reduce hallucinations, connect to external knowledge.*

- Retrieval-Augmented Generation: kết nối LLM với nguồn dữ liệu bên ngoài.
- **Trong repo:** [Graph RAG, Hybrid Search, Reranking](./agents/advanced/graph-rag.md).

---

## 5. Agents & Orchestration: Autonomous Workflows

*Multi-agent systems, planning, tool use.*

Đây là bước **trung tâm** của lộ trình AI Engineering 2026: từ “model gọi API” sang **hệ thống tự quyết định, lập kế hoạch và dùng công cụ**.

- **Kiến trúc:** [Agent Architecture](./agents/agent-architecture.md) — LLM + Memory + Planning + Tools.
- **Frameworks:** [Agent Frameworks](./agents/agent-frameworks.md) — LangChain, LangGraph, AutoGen, CrewAI.
- **Hợp tác:** [Multi-Agent Collaboration](./agents/multi-agent-collaboration.md).
- **Tự chủ:** [Autonomous Agents](./agents/autonomous-agents.md).
- **Nâng cao:** [Design Patterns](./agents/advanced/design-patterns.md), [Memory](./agents/advanced/memory-architecture.md), [Evaluation](./agents/advanced/evaluating-agents.md), [Human-in-the-loop](./agents/advanced/human-in-the-loop.md).

👉 **Mục lục đầy đủ:** [Agents — Mục lục & Lộ trình](./agents/README.md).

---

## 6. MLOps & Production Engineering

*CI/CD, Containerization, Infra as Code.*

- Đưa pipeline và Agent lên production, tái lập được, scale được.
- **Trong repo:** [Deployment Pipeline](./mlops/deployment-pipeline.md), [CI/CD for AI](./mlops/cicd-for-ai.md).

---

## 7. Evaluation, Monitoring & Safety

*Metrics, Drift detection, Bias auditing.*

- Đo chất lượng, phát hiện trôi dạt, kiểm tra thiên lệch.
- **Trong repo:** [AI Monitoring](./mlops/ai-monitoring.md), [Evaluating Agents](./agents/advanced/evaluating-agents.md), [Responsible AI](./generative-ai/responsible-ai.md).

---

## 8. Advanced Inference & Cost Optimization

*Efficient serving, Quantization, Caching.*

- Tối ưu latency, throughput và chi phí khi serve model (kể cả Agent tools).
- **Trong repo:** [Efficient Inference](./advanced/efficient-inference.md), [Distributed Training](./advanced/distributed-training.md), [Cost Optimization](./machine-learning/cost-optimization.md).
- Mở rộng: [Continual Learning](./advanced/continual-learning.md) & [Synthetic Data](./advanced/synthetic-data.md) cho workflow scale.

---

## 9. Portfolio & Continuous Learning

*Portfolio, real projects & chọn hướng chuyên sâu.*

- Áp dụng toàn bộ lộ trình vào sản phẩm/dự án thật, sau đó duy trì nhịp cập nhật kiến thức.
- **Trong repo:** [Agent Use Cases](./agents/agent-use-cases.md), [AI/ML Labs & Projects](./labs/README.md).
- Chọn domain nâng cao: [Computer Vision](./computer-vision/cv-applications.md), [NLP](./nlp/nlp-labs.md), [Reinforcement Learning](./reinforcement-learning/README.md).

---

## 🔗 Liên kết nhanh

- **Bắt đầu từ Agents:** [Agents README](./agents/README.md)  
- **Roadmap tổng thể AI/ML:** [AI/ML Roadmap](./README.md)  
- **Visual roadmap (Mermaid):** Xem [README](./README.md#-visual-roadmap)
