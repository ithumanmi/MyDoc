# Lab 3: Đường Ống Advanced RAG: Semantic Chunking & Qdrant Hybrid Search

> [← Back to Labs AI/ML Focus](./README.md) | [Home](../../../README.md)

Đây là Lab "nặng đô" mô phỏng kiến trúc RAG (Retrieval-Augmented Generation) chuyên tu của các doanh nghiệp Data-driven, kết nối lại lý thuyết [Vector DB Strategies](../agents/advanced/vector-database-strategies.md).

Chúng ta sẽ không cắt file text mù quáng (fixed size chunking) mà cắt "có tâm" mô phỏng theo Semantic Chunking, lưu vào **Qdrant Vector DB (Self-host bằng Docker)**, sau đó biểu diễn sức mạnh tìm kiếm từ khóa chéo qua Embeddings mượt mà (Tắt mắt, nó tự làm Hybrid).

---

## 🐳 Bước 1: Gọi lên Cỗ Máy Vector Qdrant (Docker)

Hãy dùng Qdrant. Lõi Rust siêu tốc, có DB Giao diện siêu đẹp (Qdrant Web UI) tích hợp thẳng để dễ quan sát Vector bằng mắt.

Khởi động Qdrant bản local qua Docker Terminal:
```bash
docker run -p 6333:6333 -p 6334:6334 \
    -v $(pwd)/qdrant_storage:/qdrant/storage:z \
    qdrant/qdrant
```
*Bạn có thể ghé vào `http://localhost:6333/dashboard` để tham quan giao diện tuyệt phẩm.*

---

## ⚙️ Bước 2: Setup Jupyter Notebook (Chuẩn Bị Bắn Embeddings)

Cài đặt package LlamaIndex (Kiến trúc RAG mượt nhất hiện tại) cùng với Vector Store Qdrant và mô hình Embeddings cực mạnh Local (BGE-M3 của cỗ máy Alibaba).

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

---

## 🔪 Bước 3: Cắt Gọt Văn Bản Cao Cấp 

Ở bài toán Data thực, ta có file báo cáo (`data/report.pdf`). Giả sử ta đọc ra Text. Thay vì cắt `chunk_size=500`. Bạn dùng khái niệm `SentenceWindowNodeParser` thần thánh của LlamaIndex. Nó sẽ lưu một câu làm chunk nhưng lưu luôn 3 câu đằng trước, 3 câu đằng sau làm Metada ẩn (Context Injection).

```python
from llama_index.core.node_parser import SentenceWindowNodeParser

# Chỉ số Cắt Ngữ Cảnh:
node_parser = SentenceWindowNodeParser.from_defaults(
    window_size=3, # Lưu kèm 3 câu trước/sau làm metadata 
    window_metadata_key="window",
    original_text_metadata_key="original_text",
)
Settings.text_splitter = node_parser

# Đọc Document
documents = SimpleDirectoryReader("./data").load_data()

# Lệnh Cắt:
nodes = node_parser.get_nodes_from_documents(documents)
print(f"Tổng số chunks (nodes) tinh tế: {len(nodes)}")
```

---

## 🗄️ Bước 4: Kích Hoạt Chỉ Mục Bề Mặt Vector Vào Qdrant (Indexing)

Quăng cái đống Chunk rỗng tuếch vào DB:

```python
from llama_index.core import StorageContext

# Mở Collections trong Qdrant có tên "my_advanced_docs"
vector_store = QdrantVectorStore(client=client, collection_name="my_advanced_docs")
storage_context = StorageContext.from_defaults(vector_store=vector_store)

# Gắn toàn bộ Mảnh Text (Nodes) đính kèm Vector và lưu vào kho Qdrant Tức Thời!
index = VectorStoreIndex(
    nodes,
    storage_context=storage_context,
)
```
*(Nếu bạn F5 Web UI trang dashboard localhost ban nãy, Collection này đã hình thành đầy nhóc Data Matrix)*

---

## 🔍 Bước 5: Truy Xuất - Thao Tác Chặn Siêu Cấp Móc Nối Lại LMM (Reranker)

Bây giờ hỏi Data. Nếu có API OpenAI truyền vào `Settings.llm` để nó trả lời, còn không ta Test việc móc Document chuẩn!

Hồi sinh tính năng: **Khi Retriever bốc Query nhét xuống Vector DB, móc nguyên cả Câu Văn Mảnh Khảnh lên, cộng với Bộ Window ẩn lọt vào LLM cho bự (Metadata Replacement).** Bằng `MetadataReplacementPostProcessor`:

```python
from llama_index.core.postprocessor import MetadataReplacementPostProcessor

query_engine = index.as_query_engine(
    similarity_top_k=2, # Lấy mạnh tay 2 chunk đỉnh nhất DB
    node_postprocessors=[
        # Kỹ thuật bốc context ra nhét lên đè lên nguyên thân Chunk
        MetadataReplacementPostProcessor(target_metadata_key="window")
    ],
)

response = query_engine.query("Kể tôi nghe doanh thu phòng ban X quý 3?")
print(response)

# In thử Source (Nguồn ngọn Context nhét cho LLM thực chất to cỡ nào do vụ Windows Replacement nãy quyết)
for node in response.source_nodes:
    print(node.text)
```

---
> Kết thúc: Bằng sự dốc túi này, Hệ thống RAG doanh nghiệp sẽ đọc nguyên 1 câu rất ngắn, nhưng ngầm gửi toàn bộ ngữ cảnh khổng lồ đè lên cho GPT phán xét. Khác bọt hoàn toàn `langchain` tách chuỗi thông thường.
