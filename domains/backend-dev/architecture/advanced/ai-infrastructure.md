---
title: "AI Infrastructure"
description: "Vector DB, embedding pipeline, LLM serving, RAG architecture."
tags:
  - backend
  - architecture
  - ai
updated: 2026-03-11
---

# 🧠 AI Infrastructure (2024-2026)

## 1. Vector Databases & Indexing
- **Use cases:** semantic search, recommendation, anomaly detection.
- **Engines:** Pinecone, Weaviate, Qdrant, Milvus, PostgreSQL+pgvector.
- **Index types:** IVF, HNSW, Product Quantization.
- **Hybrid search:** combine BM25 + vector score.

### Apply
- Map dimension (d) các embedding → chọn index phù hợp.
- Thiết lập RPS capacity, replication for HA.
- Theo dõi recall vs latency → tuning ef, nprobe.

## 2. Embedding Pipeline
- **Sources:** text, code, image/audio.
- **Steps:** chunking → cleaning → embedding → storing.
- **Batch vs streaming:** offline refresh vs near-real-time update.
- **Data quality:** dedup, remove PII.

### Tooling
- Open-source: LangChain, LlamaIndex, Haystack.
- MLOps: Airflow/Prefect orchestration, Feature Store.

## 3. LLM Serving Patterns
- **Single model endpoint:** REST/gRPC autoscaling (SageMaker, Vertex AI, vLLM).
- **Model routing:** Router chọn model theo prompt type/cost.
- **Speculative decoding:** model nhỏ dự đoán, model lớn xác nhận → tăng throughput.
- **Continuous batching:** gom request để tận dụng GPU (vLLM, Triton).

## 4. Retrieval-Augmented Generation (RAG)
- **Flow:** user prompt → retrieve context (vector DB) → augment prompt → LLM → guardrail.
- **Components:** retriever, reranker, prompt template, caching.
- **Quality metrics:** grounding accuracy, hallucination rate, latency.
- **Advanced:** multi-hop retrieval, tool calling, agentic workflow.

## ✅ Apply it
- [ ] Thiết kế pipeline embedding (scheduler, chunk size, recursion depth) + diagram.
- [ ] Chọn vector DB (managed/self-host) phù hợp compliance & budget.
- [ ] POC serving stack (vLLM + Triton + autoscaler) với load thực tế.
- [ ] Đo metric RAG (retrieval recall, answer faithfulness) trong dashboard.
- [ ] Tích hợp guardrail (content filter, policy) trước khi trả kết quả.

## 🔗 Cross-reference
- [ai-ml/ai-engineering-roadmap-2026.md](../ai-ml/ai-engineering-roadmap-2026.md)
- [backend-dev/deployment-guide.md](../deployment-guide.md) – CI/CD cho model serving.
- [monitoring-observability.md](../monitoring-observability.md) – metric GPU, token latency.
- [security/zero-trust-architecture.md](./zero-trust-architecture.md) – bảo vệ endpoint AI.