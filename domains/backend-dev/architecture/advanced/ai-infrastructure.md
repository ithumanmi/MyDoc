---
title: "Hạ tầng AI"
description: "Vector DB, pipeline embedding, phục vụ LLM, kiến trúc RAG."
tags:
  - backend
  - architecture
  - ai
updated: 2026-03-11
---

# 🧠 Hạ tầng AI (2024-2026)

## 1. Cơ sở dữ liệu vector & lập chỉ mục
- **Use case:** semantic search, gợi ý, phát hiện bất thường.
- **Engine:** Pinecone, Weaviate, Qdrant, Milvus, PostgreSQL + pgvector.
- **Loại index:** IVF, HNSW, Product Quantization.
- **Tìm kiếm lai:** kết hợp BM25 + điểm vector.

### Thực hành
- Map số chiều (d) của embedding → chọn index phù hợp.
- Thiết lập khả năng phục vụ RPS, replication để HA.
- Theo dõi recall vs latency → tinh chỉnh `ef`, `nprobe`.

## 2. Pipeline embedding
- **Nguồn dữ liệu:** text, code, image/audio.
- **Bước:** chunking → làm sạch → embedding → lưu trữ.
- **Batch vs streaming:** làm mới offline vs cập nhật gần real-time.
- **Chất lượng dữ liệu:** khử trùng lặp, loại bỏ PII.

### Công cụ
- Mã nguồn mở: LangChain, LlamaIndex, Haystack.
- MLOps: điều phối Airflow/Prefect, Feature Store.

## 3. Mẫu phục vụ LLM
- **Single model endpoint:** REST/gRPC autoscaling (SageMaker, Vertex AI, vLLM).
- **Model routing:** Router chọn model theo loại prompt/chi phí.
- **Speculative decoding:** model nhỏ dự đoán, model lớn xác nhận → tăng throughput.
- **Continuous batching:** gom request tận dụng GPU (vLLM, Triton).

## 4. Retrieval-Augmented Generation (RAG)
- **Luồng:** user prompt → lấy ngữ cảnh (vector DB) → bổ sung prompt → LLM → guardrail.
- **Thành phần:** retriever, reranker, prompt template, caching.
- **Chỉ số chất lượng:** grounding accuracy, hallucination rate, latency.
- **Nâng cao:** multi-hop retrieval, tool calling, agentic workflow.

## ✅ Thực hành
- [ ] Thiết kế pipeline embedding (scheduler, chunk size, recursion depth) + sơ đồ.
- [ ] Chọn vector DB (managed/self-host) phù hợp compliance & ngân sách.
- [ ] POC stack phục vụ (vLLM + Triton + autoscaler) với tải thực tế.
- [ ] Đo metric RAG (retrieval recall, answer faithfulness) trong dashboard.
- [ ] Tích hợp guardrail (content filter, policy) trước khi trả kết quả.

## 🔗 Tham chiếu chéo
- [ai-ml/ai-engineering-roadmap-2026.md](../ai-ml/ai-engineering-roadmap-2026.md)
- [backend-dev/deployment-guide.md](../deployment-guide.md) – CI/CD cho model serving.
- [monitoring-observability.md](../monitoring-observability.md) – metric GPU, token latency.
- [security/zero-trust-architecture.md](./zero-trust-architecture.md) – bảo vệ endpoint AI.