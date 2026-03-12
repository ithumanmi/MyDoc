## 🔍 Information Retrieval & Search Systems

> [← Back to NLP Roadmap](./README.md)

Thiết kế hệ thống search hiện đại: BM25 + dense retrieval + hybrid reranking.

---

## 1. Architecture Overview

```
Documents -> Indexing -> Retrieval -> Reranking -> Results
```

*   **Indexing:** tokenization, stopwords, inverted index, embedding store.
*   **Retrieval:** lexical (BM25), dense (ANN), hybrid fusion.
*   **Reranking:** cross-encoders, LLM-based scoring.

---

## 2. Lexical Retrieval (BM25)

```python
from rank_bm25 import BM25Okapi

tokenized_corpus = [doc.split() for doc in documents]
bm25 = BM25Okapi(tokenized_corpus)
scores = bm25.get_scores(query.split())
```

Tips:
* Custom analyzer (viet tokenizer) để cải thiện recall.
* Field-level boosting (title vs body).

---

## 3. Dense Retrieval

### Steps
1. Encode documents bằng Sentence-BERT/Instructor.
2. Index với FAISS/ScaNN.
3. Encode query và ANN search.

```python
from sentence_transformers import SentenceTransformer
import faiss, numpy as np

model = SentenceTransformer("sentence-transformers/multi-qa-mpnet-base-dot-v1")
embeddings = model.encode(documents, show_progress_bar=True)
index = faiss.IndexFlatIP(embeddings.shape[1])
index.add(embeddings)

query_vec = model.encode([query])
scores, ids = index.search(query_vec, k=10)
```

### Hybrid
* Reciprocal Rank Fusion (RRF): kết hợp ranking lexical + dense.

---

## 4. Reranking & QA

* Cross-encoder (e.g., `cross-encoder/ms-marco-MiniLM-L-6-v2`).
* LLM reranker (LlamaIndex, Cohere Rerank).
* Retrieval-Augmented Generation: pass top-k docs vào LLM.

---

## 5. Evaluation

| Metric | Ý nghĩa |
| --- | --- |
| MRR (Mean Reciprocal Rank) | Độ chính xác top-1 |
| nDCG | Consider vị trí & gain |
| Recall@k | Bao nhiêu relevant docs xuất hiện |

Offline evaluation: trec_eval, pytrec_eval.

Online: A/B test click-through, dwell time.

---

## 6. Infrastructure Tips

*   **Index lifecycle:** nightly rebuild, near-real-time update.
*   **Caching:** query cache, embedding cache.
*   **Observability:** log query, latency, success rate.
*   **Security:** permission-aware retrieval (filter per user).

---

## 7. Resources

*   [Elasticsearch BM25 Tuning](https://www.elastic.co/blog/practical-bm25-part-1-how-shards-affect-relevance)
*   [FAISS Wiki](https://github.com/facebookresearch/faiss/wiki)
*   [Dense Passage Retrieval Paper](https://arxiv.org/abs/2004.04906)

> 🧭 Tip: Với hybrid RAG, log metadata (source, timestamp) để tracing + audit câu trả lời của LLM.
