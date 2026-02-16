# 🛠️ AI Agent Frameworks: Công cụ của Kiến trúc sư

> [← Back to AI/ML Roadmap](../README.md)

Bạn không cần code mọi thứ từ đầu (Prompt Engineering, Memory Management, Tool Calling). Framework lo hết.

---

## 1. LangChain (Huyền thoại)

Thư viện Python/JS phổ biến nhất để xây dựng LLM Apps.

### **Cấu trúc:**
*   **Chains:** Kết nối các bước xử lý (Prompt -> LLM -> Output Parser).
*   **Agents:** Một Chain đặc biệt có khả năng tự quyết định dùng Tool nào.
*   **VectorStore:** Tích hợp sẵn với Pinecone, Chroma, FAISS.

### **Nhược điểm:**
*   Khá cồng kềnh (Abstraction quá nhiều). Khó debug khi lỗi sâu bên trong.

---

## 2. LangGraph (Thế hệ mới)

LangChain tập trung vào **DAG (Directed Acyclic Graph)** - luồng đi thẳng một chiều.
LangGraph cho phép **Cycles (Vòng lặp)** - Agent có thể quay lại bước trước để sửa sai.

### **Stateful Agents:**
*   Lưu giữ trạng thái (State) của cuộc hội thoại qua các bước.
*   Ví dụ:
    1.  Agent viết code.
    2.  Chạy code -> Lỗi.
    3.  **Loop:** Quay lại bước 1 để sửa code dựa trên lỗi (Self-correction).

---

## 3. AutoGen (Microsoft)

Framework chuyên dụng cho **Multi-Agent Conversation**.

### **Cơ chế:**
*   Bạn định nghĩa các Agent (Coder, Reviewer, User Proxy).
*   Các Agent tự nói chuyện với nhau để giải quyết vấn đề.
*   **Human-in-the-loop:** Cho phép con người can thiệp vào cuộc hội thoại khi cần thiết.

---

## 4. CrewAI (Role-playing Orchestration)

Tập trung vào việc phân vai (Role-playing) cho các Agent.

### **Mô hình:**
*   **Crew (Đội ngũ):** Tập hợp các Agent.
*   **Tasks (Nhiệm vụ):** Công việc cụ thể cần làm.
*   **Process (Quy trình):** Tuần tự (Sequential) hoặc Phân cấp (Hierarchical).

> **Ví dụ:**
> *   **Researcher Agent:** Tìm kiếm thông tin về thị trường AI.
> *   **Writer Agent:** Viết bài blog dựa trên thông tin Researcher tìm được.
> *   **Manager Agent:** Giao việc và kiểm duyệt chất lượng.
