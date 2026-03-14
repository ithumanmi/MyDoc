# Challenge: RAG Pipeline End-to-End (Ingest → Vector Store → Query API)

- **Loại:** project
- **Mảng:** ai-ml
- **Mức:** Intermediate
- **Ước lượng thời gian:** 1-2 tuần
- **Prerequisites (tùy chọn):** [`domains/ai-ml/generative-ai/`](../../domains/ai-ml/generative-ai/) · kiến thức cơ bản về embeddings, vector DB, API server.

## Mục tiêu học tập
- Xây dựng pipeline RAG hoàn chỉnh: ingest tài liệu → index/vector store → query API.
- Thiết kế retrieval (chunking, top-k, rerank tùy chọn) và đánh giá nhanh.
- Đóng gói service với API/gateway đơn giản.

## Đề bài
Xây RAG service với các bước:
1) **Ingest**: đọc file (pdf/md/txt), chunk, sinh embedding, lưu vào vector store.
2) **Query API**: endpoint nhận câu hỏi, retrieve + optionally rerank + compose prompt + gọi LLM (mock hoặc real), trả câu trả lời kèm nguồn.
3) **Ops**: script/CLI để ingest; README hướng dẫn chạy; config (.env) cho khóa/model.

## Đầu vào (Input)
- Bộ tài liệu mẫu (có thể dùng docs mở hoặc tự chuẩn bị). Vector DB có thể dùng sqlite/faiss/chroma để đơn giản.

## Đầu ra (Output)
- Service chạy được: `/query` trả câu trả lời + nguồn; `/health` đơn giản.
- Script/CLI ingest.
- README chỉ dẫn cài đặt/chạy, mô tả kiến trúc (1 hình ascii cũng được).

## Tiêu chí chấm (Acceptance)
- **Đúng chức năng:** ingest thành công, query trả kết quả và nguồn; lỗi được bắt.
- **Retrieval hợp lý:** chunking hợp lý; top-k; có tham số điều chỉnh; (tùy chọn) rerank.
- **Code quality:** tách module (ingest/retrieval/api), cấu hình .env, log tối thiểu.

## Gợi ý / Hint
- Dùng sentence-transformers/embedding API; vector DB đơn giản (faiss/chroma).
- Prompt: cung cấp nguồn trong câu trả lời; hạn chế hallucination bằng system prompt.
- Đánh giá nhanh: manual check 3-5 câu hỏi; (tuỳ chọn) simple RAGAS/eval script.

## Reference / Solution (tùy chọn)
- (Tuỳ chọn) Repo mẫu: `https://github.com/example/rag-pipeline-sample` (thay bằng repo của bạn nếu có).