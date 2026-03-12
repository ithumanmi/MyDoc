## 🎯 Project: Recommender System (Hybrid)

> [← Back to Labs](./README.md)

Xây dựng hệ thống gợi ý kết hợp collaborative filtering + content-based.

---

## 1. Business Context

- Domain: e-commerce, video, âm nhạc, học liệu.
- KPI: CTR, conversion, dwell time, revenue uplift.
- Constraint: cold-start user/item, latency, personalization vs diversity.

---

## 2. Data Pipeline

- Thu thập interaction logs (user_id, item_id, event_type, timestamp).
- Feature store: user features (demographics, embedding), item metadata.
- Offline store (Parquet/BigQuery) + online store (Redis/Feature Store service).

Checklist:

- [ ] Data quality validation (Great Expectations)
- [ ] Train/test split theo thời gian (avoid leakage)
- [ ] Negative sampling strategy

---

## 3. Modeling

### Collaborative Filtering

- ALS (Matrix Factorization) hoặc Neural CF.
- Implicit feedback → dùng implicit library (Hu et al. loss).

### Content-Based

- TF-IDF/embeddings từ metadata (title, tags, description).
- Similarity search (Faiss) hoặc cosine similarity.

### Hybrid Strategy

- Weighted blending (w1 * CF + w2 * Content).
- Stacking model (LightGBM/XGBoost) sử dụng features từ CF + content.

Evaluation: Recall@K, MAP@K, NDCG.

---

## 4. Serving Architecture

- Offline batch scoring → top-N per user (daily).
- Online re-ranking với context real-time (time of day, device).
- API: `/recommend?user_id=...` trả về danh sách items.

Infra đề xuất:

- Feature Store (Feast)
- Vector DB (Pinecone/Weaviate/Faiss)
- Model Serving (FastAPI, gRPC)

---

## 5. Experimentation & A/B Testing

- Chia traffic giữa baseline vs hybrid model.
- Theo dõi metrics online (CTR uplift, conversion).
- Thu thập feedback (explicit rating) để cải thiện personalization.

---

## 6. Deliverables

- Data schema + data validation scripts.
- Notebooks cho CF, content-based, hybrid blending.
- Deployment docs (infra diagram, scaling plan).
- Experiments dashboard (A/B metrics).

> 🎯 Bonus: Implement exploration (ε-greedy, Thompson Sampling) để tránh “filter bubble”.
