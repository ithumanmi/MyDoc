## 🔡 Embeddings Deep Dive

> [← Back to NLP](./README.md)

Từ Word2Vec/FastText tới sentence embeddings hiện đại — hiểu cơ chế, cách huấn luyện và khi nào dùng.

---

## 1. Word2Vec

| Variant | Ý tưởng | Ghi chú |
| --- | --- | --- |
| **CBOW** | Dự đoán từ trung tâm từ context | Nhanh hơn, tốt với dataset lớn |
| **Skip-gram** | Dự đoán context từ từ trung tâm | Tốt cho từ hiếm |

* Negative sampling, hierarchical softmax để tối ưu.
* Embedding dimension ~100-300.

```python
from gensim.models import Word2Vec
model = Word2Vec(sentences, vector_size=200, window=5, sg=1, negative=10)
vector = model.wv["hanoi"]
```

---

## 2. FastText

* Thay vì chỉ học vector cho từ, FastText học n-gram ký tự → xử lý OOV tốt.
* Dùng cho ngôn ngữ giàu morphology (tiếng Việt, tiếng Đức).

---

## 3. GloVe

* Factorization co-occurrence matrix, optimized với weighting function.
* Có pretrained (Common Crawl, Wikipedia) → dùng làm init cho model downstream.

---

## 4. Contextual Embeddings

| Model | Đặc điểm |
| --- | --- |
| **ELMo** | BiLSTM language model, context-dependent |
| **BERT** | Transformer encoder, bidirectional |
| **GPT** | Decoder-only, autoregressive |

> Contextual embeddings thay đổi theo câu → giải quyết polysemy.

---

## 5. Sentence Embeddings

* **Sentence-BERT (SBERT):** siamese BERT + pooling, dùng cosine similarity.
* **Universal Sentence Encoder (USE):** Transformer + DAN architecture.
* **SimCSE:** contrastive learning không cần nhãn.

```python
from sentence_transformers import SentenceTransformer
model = SentenceTransformer('sentence-transformers/all-mpnet-base-v2')
emb = model.encode(["Xin chào"], normalize_embeddings=True)
```

---

## 6. Evaluation & Usage

- **Intrinsic:** analogy test, word similarity.
- **Extrinsic:** downstream tasks (classification, retrieval).
- **Indexing:** FAISS, Milvus, pgvector.

> Checklist: chuẩn hóa vector (L2), lưu version model, log drift khi embedding update.
