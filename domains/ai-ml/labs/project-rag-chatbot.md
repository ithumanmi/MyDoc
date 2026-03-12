## 🧠 Project: RAG Chatbot from Scratch

> [← Back to Labs](./README.md)

Thiết kế hệ thống Retrieval-Augmented Generation (RAG) cho tài liệu nội bộ.

---

## 1. Problem Definition

- Use case: trợ lý tài liệu doanh nghiệp, FAQ sản phẩm, support agent.
- KPI: answer accuracy, latency, hallucination rate, user satisfaction.
- Scope dữ liệu: PDF, wiki nội bộ, ticket hệ thống.

---

## 2. Data & Indexing Pipeline

1. **Ingestion:** convert PDF/Docx → text, chunking (512-1,000 tokens) + overlap.
2. **Metadata:** lưu nguồn, timestamp, permission.
3. **Embeddings:** chọn model (text-embedding-3-large, bge, Instructor).
4. **Vector Store:** Pinecone, Weaviate, Postgres + pgvector.

Checklist:

- [ ] Deduplicate, remove boilerplate.
- [ ] Permission filter (per user/role).
- [ ] Quality assurance (manual spot check chunks).

---

## 3. Retrieval Strategies

- Hybrid search: dense + sparse (BM25) → rerank (Cross-Encoder, ColBERT).
- Maximal Marginal Relevance (MMR) giảm trùng lặp.
- Auto re-query: nếu confidence thấp, re-query với alias.

---

## 4. Generation Pipeline

- Prompt template: instructions + context + question.
- LLM choices: GPT-4, Claude, Llama 3 fine-tune.
- Guardrail: answer must cite sources, fallback "I don't know".

Pseudo-flow:

```python
context = retriever.retrieve(query, k=5)
prompt = template.render(context=context, question=query)
response = llm(prompt)
return format_answer(response, sources=context.sources)
```

---

## 5. Evaluation & Monitoring

- Metrics: precision@k (retrieval), groundedness, answer helpfulness.
- Tools: Ragas, DeepEval, human evaluation form.
- Monitor latency, cost per request, content filters triggered.

---

## 6. Deployment

- Backend: FastAPI/LangChain server hoặc GraphRAG pipeline.
- Frontend: chat UI (Next.js) hoặc Slack bot integration.
- Infra: Docker + autoscaling (Cloud Run, Azure Container Apps).

---

## 7. Deliverables

- Data ingestion scripts + vector store schema.
- Prompt templates + evaluation notebook.
- Deployment docs (architecture diagram, scaling plan).
- Demo video hoặc live URL.

> 🎯 Bonus: Thêm memory (conversation buffer) và logging để fine-tune future response.
