# Lab 3: Advanced RAG với Qdrant (Semantic Chunking & Hybrid Search)

> [← Back to Labs AI/ML Focus](./README.md) | [Home](../../../README.md)

Mục tiêu: xây RAG với semantic chunking, lưu vào Qdrant self-host (Docker) và truy vấn hybrid (vector + keyword). Tham chiếu lý thuyết [Vector DB Strategies](../agents/advanced/vector-database-strategies.md).

---

## 🐳 Bước 1: Chạy Qdrant (Docker)

Chạy Qdrant local:
```bash
docker run -p 6333:6333 -p 6334:6334 \
    -v $(pwd)/qdrant_storage:/qdrant/storage:z \
    qdrant/qdrant
```
Dashboard: http://localhost:6333/dashboard

---
## ⚙️ Bước 2: Chuẩn bị notebook & embeddings

Cài LlamaIndex + Qdrant client + embedding (BGE):
```bash
pip install llama-index llama-index-vector-stores-qdrant qdrant-client
pip install llama-index-embeddings-huggingface
```

Trong Python/Jupyter Notebook:

```python
import qdrant_client
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.vector_stores.qdrant import QdrantVectorStore
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

# 1. Liên lạc với cục Docker Qdrant ban nãy
client = qdrant_client.QdrantClient(host="localhost", port=6333)

# 2. Định nghĩa Mô hình Ném Ngôn Từ Thành Vectors (Local BAAI)
# BGE-Small chạy cực lẹ trên CPU
embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")
Settings.embed_model = embed_model
```

## 🔪 Bước 3: Semantic chunking

Dùng `SentenceWindowNodeParser` để giữ thêm ngữ cảnh lân cận:

```python
from llama_index.core.node_parser import SentenceWindowNodeParser

node_parser = SentenceWindowNodeParser.from_defaults(
    window_size=3, # kèm 3 câu trước/sau làm metadata 
    window_metadata_key="window",
    original_text_metadata_key="original_text",
)
Settings.text_splitter = node_parser

documents = SimpleDirectoryReader("./data").load_data()
nodes = node_parser.get_nodes_from_documents(documents)
print(f"Chunks: {len(nodes)}")
```

---
## 🗄️ Bước 4: Index vào Qdrant
Đưa nodes vào Qdrant:

```python
from llama_index.core import StorageContext

vector_store = QdrantVectorStore(client=client, collection_name="my_advanced_docs")
storage_context = StorageContext.from_defaults(vector_store=vector_store)
index = VectorStoreIndex(nodes, storage_context=storage_context)
```

## 🔍 Bước 5: Truy vấn + thay metadata (context window)

Hồi sinh tính năng: **Khi Retriever bốc Query nhét xuống Vector DB, móc nguyên cả Câu Văn Mảnh Khảnh lên, cộng với Bộ Window ẩn lọt vào LLM cho bự (Metadata Replacement).** Bằng `MetadataReplacementPostProcessor`:

```python
from llama_index.core.postprocessor import MetadataReplacementPostProcessor

query_engine = index.as_query_engine(
    similarity_top_k=2,
    node_postprocessors=[MetadataReplacementPostProcessor(target_metadata_key="window")],
)

response = query_engine.query("Kể tôi nghe doanh thu phòng ban X quý 3?")
print(response)

for node in response.source_nodes:
    print(node.text)
```

---
Kết quả: chunk nhỏ nhưng được thay bằng cửa sổ ngữ cảnh rộng (metadata `window`), giúp LLM trả lời tốt hơn.
