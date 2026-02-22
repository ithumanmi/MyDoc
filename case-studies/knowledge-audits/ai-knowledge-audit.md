# 🤖 AI & Machine Learning Knowledge Audit: Thử thách "Enterprise AI Transformation"

> **Mục đích:** Đo lường năng lực thiết kế, triển khai và tối ưu hóa các giải pháp Trí tuệ nhân tạo từ cơ bản đến nâng cao.
> **Phiếu trả lời:** [Tải mẫu tại đây](../templates/ai-answer-template.md)
> 
> **Kịch bản:** Bạn là **AI Solutions Architect** cho tập đoàn "GlobalLogistics". Nhiệm vụ của bạn là xây dựng hệ thống AI toàn diện: từ dự báo nhu cầu vận chuyển, tự động hóa kho bãi bằng thị giác máy tính, đến hệ thống trợ lý ảo thông minh phục vụ khách hàng toàn cầu.

---

## 📉 Thử thách 1: Machine Learning Fundamentals (Nền tảng & Dự báo)
*Đo lường năng lực xử lý dữ liệu bảng (tabular data) và các mô hình học máy truyền thống.*

**Tình huống:** Bạn cần xây dựng mô hình dự báo nhu cầu vận chuyển (demand forecasting) cho 100 kho hàng. Dữ liệu bị nhiễu, thiếu nhiều giá trị và có tính mùa vụ cao.

**Câu hỏi:**
1.  Làm thế nào để bạn xử lý dữ liệu thiếu (missing data) và các giá trị ngoại lai (outliers) mà không làm mất đi tính đặc trưng của dữ liệu?
2.  Bạn sẽ chọn thuật toán nào cho bài toán hồi quy (regression) này? Khi nào bạn dùng **Linear Regression**, và khi nào bạn chuyển sang các mô hình Ensemble như **XGBoost** hay **LightGBM**?
3.  Làm thế nào để đo lường độ chính xác của mô hình? Bạn sẽ dùng **MAE**, **RMSE** hay **MAPE**? Tại sao?

**Thước đo:**
*   **🟢 Beginner:** Biết dùng Scikit-learn để fit mô hình cơ bản và xử lý dữ liệu bằng Pandas.
*   **🔴 Expert:** Làm chủ kỹ thuật **Feature Engineering** (tạo đặc trưng), hiểu rõ về **Bias-Variance Trade-off**, và biết cách áp dụng **Time-series Cross-validation** để tránh leak dữ liệu từ tương lai.

---

## 👁️ Thử thách 2: Computer Vision (Thị giác máy tính & Tự động hóa)
*Đo lường năng lực xử lý hình ảnh và video.*

**Tình huống:** Kho hàng cần hệ thống tự động nhận diện và phân loại hàng hóa bị hư hỏng (móp méo, rách bao bì) qua camera giám sát.

**Câu hỏi:**
1.  Bạn sẽ chọn kiến trúc mạng CNN nào cho bài toán này? (Ví dụ: **ResNet**, **EfficientNet**, hay **YOLO** nếu cần nhận diện vật thể thời gian thực)?
2.  Nếu tập dữ liệu hình ảnh lỗi quá ít (Imbalanced data), bạn sẽ áp dụng những kỹ thuật nào để cải thiện hiệu năng mạng (ví dụ: **Data Augmentation**, **Transfer Learning**, hay **Synthetic Data**)?
3.  Làm thế nào để mô hình chạy mượt mà trên các thiết bị Edge (như camera thông minh) có tài nguyên tính toán hạn chế?

**Thước đo:**
*   **🟢 Beginner:** Biết cách dùng pretrained model để phân loại ảnh đơn giản.
*   **🔴 Expert:** Tối ưu hóa được **Object Detection Pipeline**, làm chủ kỹ thuật **Model Compression** (Quantization, Pruning), và hiểu rõ về các metrics như **mAP (mean Average Precision)**.

---

## 💬 Thử thách 3: NLP & Generative AI (Xử lý ngôn ngữ & GenAI)
*Đo lường năng lực ứng dụng LLM và RAG.*

**Tình huống:** Bạn xây dựng Chatbot hỗ trợ khách hàng đa ngôn ngữ. Chatbot cần truy xuất thông tin từ hàng nghìn tài liệu PDF về chính sách vận chuyển của tập đoàn.

**Câu hỏi:**
1.  Tại sao bạn nên chọn kiến trúc **RAG (Retrieval-Augmented Generation)** thay vì chỉ **Fine-tuning** một mô hình LLM lớn?
2.  Làm thế nào để chatbot không trả lời sai (hallucination) khi thông tin không có trong tài liệu? Bạn thiết kế **Prompt Engineering** và cơ chế **Verification** như thế nào?
3.  Bạn sẽ tối ưu hóa **Vector Database** như thế nào để tìm kiếm thông tin nhanh và chính xác nhất (ví dụ: chọn Embedding model, kỹ thuật Hybrid Search)?

**Thước đo:**
*   **🟢 Beginner:** Biết gọi API OpenAI và nhồi text vào prompt.
*   **🔴 Expert:** Thiết kế được luồng **Advanced RAG** (với Re-ranking, Query Transformation), hiểu rõ sự đánh đổi giữa **Context Window** và chi phí token, biết cách đánh giá chatbot bằng mô hình như **RAGAS**.

---

## 🤖 Thử thách 4: AI Agents & Orchestration (Tác vụ phức tạp)
*Đo lường năng lực thiết kế hệ thống AI tự trị.*

**Tình huống:** Tập đoàn muốn AI có thể tự động thực hiện các tác vụ phức tạp: "Kiểm tra đơn hàng bị chậm -> Liên hệ với kho -> Đề xuất giải pháp đền bù cho khách hàng".

**Câu hỏi:**
1.  Bạn sẽ thiết kế cấu trúc **Agentic Workflow** như thế nào? Sử dụng framework nào (ví dụ: **LangGraph**, **CrewAI**, hay **AutoGPT**)?
2.  Làm thế nào để kiểm soát quá trình suy nghĩ của Agent để nó không bị lặp vô tận (Infinite Loop) hoặc thực hiện các hành động sai lầm trên hệ thống thật?
3.  Cơ chế **Tool Use (Function Calling)** hoạt động như thế nào để Agent có thể tương tác với Database hay API của tập đoàn?

**Thước đo:**
*   **🟢 Beginner:** Biết viết script gọi Agent đơn giản thực hiện 1-2 bước.
*   **🔴 Expert:** Thiết kế được hệ thống **Multi-Agent** phối hợp nhịp nhàng, có cơ chế **Human-in-the-loop** để giám sát các hành động quan trọng, và tối ưu hóa được độ tin cậy của Agent.

---

## 🚀 Thử thách 5: MLOps & Production (Vận hành & Mở rộng)
*Đo lường năng lực đưa AI vào thực tế.*

**Tình huống:** Mô hình dự báo sau khi triển khai lên Production bắt đầu giảm độ chính xác sau 1 tháng (Concept Drift). Hệ thống Chatbot bị quá tải khi có hàng vạn user truy cập cùng lúc.

**Câu hỏi:**
1.  Bạn thiết kế hệ thống **Monitoring** như thế nào để phát hiện sớm hiện tượng **Data Drift** và **Concept Drift**?
2.  Làm thế nào để tự động hóa quy trình tái huấn luyện mô hình (**CI/CD/CT** - Continuous Training)?
3.  Khi phục vụ LLM cho số lượng lớn user, bạn tối ưu hóa hạ tầng như thế nào (ví dụ: **Batching**, **Model Parallelism**, hay dùng **vLLM**)?

**Thước đo:**
*   **🟢 Beginner:** Biết save model thành file `.pkl` và chạy trên Flask/FastAPI đơn giản.
*   **🔴 Expert:** Làm chủ các công cụ như **MLflow**, **Kubeflow**, triển khai được các chiến lược **A/B Testing** cho mô hình AI, và tối ưu hóa hạ tầng GPU (VRAM management).

---

## 🧠 Thử thách 6: Applied Mental Models & Ethics (Đạo đức & Chiến lược)
*Đo lường tư duy hệ thống và trách nhiệm của người làm AI.*

**Tình huống:** Hội đồng quản trị lo ngại về việc AI có thể gây ra phân biệt đối xử (Bias) hoặc lộ lọt dữ liệu khách hàng. Họ cũng muốn biết lợi nhuận (ROI) của dự án AI này là bao nhiêu.

**Câu hỏi:**
1.  Làm thế nào để bạn đo lường và giảm thiểu **Algorithmic Bias** trong các mô hình AI của tập đoàn?
2.  Bạn áp dụng mô hình **First Principles Thinking** như thế nào để xác định xem một vấn đề có THỰC SỰ cần AI để giải quyết hay không?
3.  Làm thế nào để cân bằng giữa độ chính xác (Accuracy) và tính giải thích được (**Explainable AI - XAI**) để sếp và khách hàng có thể tin tưởng vào kết quả của mô hình?

**Thước đo:**
*   **🟢 Beginner:** Bỏ qua vấn đề đạo đức, chỉ quan tâm đến độ chính xác (Accuracy).
*   **🔴 Expert:** Xây dựng được khung quản trị **AI Ethics**, tính toán được **ROI** dựa trên chi phí hạ tầng/nhân sự vs giá trị business mang lại, và biết cách giải thích mô hình bằng **SHAP** hoặc **LIME**.

---

## 📊 Bảng tự chấm điểm (Scoring Rubric)

| Lĩnh vực | Thang điểm (1-10) | Gợi ý tự vấn |
| :--- | :---: | :--- |
| **ML Fundamentals** | ____ / 10 | Bạn có hiểu toán học đằng sau các thuật ngữ như Gradient Descent hay Regularization không? |
| **Computer Vision** | ____ / 10 | Bạn có thể tùy chỉnh một mạng Neural cho một bài toán đặc thù không? |
| **NLP & GenAI** | ____ / 10 | Bạn có biết cách làm cho RAG thực sự hiệu quả thay vì chỉ là "gọi API"? |
| **AI Agents** | ____ / 10 | Bạn có thể thiết kế một Agent có khả năng tự giải quyết vấn đề phức tạp không? |
| **MLOps & Scaling** | ____ / 10 | Bạn quản lý mô hình bằng thủ công hay bằng pipeline tự động hoàn toàn? |
| **Ethics & Strategy** | ____ / 10 | Bạn là "thợ chạy model" hay là người giải quyết vấn đề business bền vững? |

### 🏆 Xếp hạng năng lực AI:
*   **0 - 20 điểm:** **AI Learner**. Hãy tập trung vào `domains/ai-ml/fundamentals/`.
*   **21 - 40 điểm:** **ML Engineer**. Có khả năng triển khai mô hình tốt nhưng cần mở rộng chiều rộng hệ thống.
*   **41 - 55 điểm:** **AI Solutions Architect**. Khả năng thiết kế giải pháp tổng thể và kết nối đa ngành tốt.
*   **56 - 60 điểm:** **AI Visionary / Chief AI Officer (CAIO)**. Bạn là người định hướng tương lai của AI trong doanh nghiệp.

---

## 🔑 Answer Key: Góc nhìn Chuyên gia (Expert Guidelines)

### Thử thách 1: ML Fundamentals
*   **Xử lý dữ liệu:** Ưu tiên dùng **Median Imputation** cho dữ liệu lệch hoặc **KNN Imputer**. Dùng **Robust Scaler** nếu có nhiều ngoại lai.
*   **Mô hình:** Linear Regression chỉ dùng cho baseline. XGBoost/LightGBM vượt trội cho dữ liệu bảng nhờ khả năng handle non-linear và auto-handling missing values. Cần dùng **SHAP values** để giải thích tầm quan trọng của các feature.

### Thử thách 2: Computer Vision
*   **Imbalanced Data:** Sử dụng **Focal Loss** để tập trung vào các case khó nhận diện. Áp dụng **Class Weighting**.
*   **Edge Optimization:** Dùng **TensorRT** (cho NVIDIA) hoặc **OpenVINO** (cho Intel). Chuyển mô hình về định dạng **INT8** hoặc **FP16** để tăng tốc độ inference.

### Thử thách 3: NLP & GenAI
*   **RAG vs Fine-tuning:** Fine-tuning giúp học style/format, RAG giúp cập nhật kiến thức mới mà không cần train lại. RAG rẻ và ít hallucination hơn cho các dữ liệu thay đổi liên tục.
*   **Optimization:** Dùng **Recursive Character Text Splitter** để chunking thông minh. Sử dụng **HyDE (Hypothetical Document Embeddings)** để cải thiện kết quả tìm kiếm.

### Thử thách 4: AI Agents
*   **Control:** Sử dụng mô hình **ReAct (Reason + Act)**. Cần có cơ chế **Token Budget** để ngắt Agent nếu chạy quá lâu.
*   **Tools:** Định nghĩa rõ ràng JSON Schema trong Tool description để LLM hiểu chính xác cách truyền tham số.

### Thử thách 5: MLOps
*   **Monitoring:** Monitor các chỉ số phân phối đầu vào (Input distribution) vs Training distribution. Dùng **Prometheus** để track latency và throughput.
*   **Scaling:** Dùng **KServe** hoặc **BentoML**. Áp dụng **Continuous Integration for ML (CIML)** để tự động test hiệu năng mô hình mới trước khi merge.

### Thử thách 6: Ethics & Strategy
*   **ROI:** AI không phải là "viên thuốc thần". Phải bắt đầu từ bài toán kinh doanh. Nếu dùng Logic If-Else mà giải quyết được 90% vấn đề với giá 0đ, thì đừng dùng LLM tốn 1000$.

---

## 🚀 Tài liệu bổ trợ để "Level Up"
*   **Nền tảng AI:** [AI Fundamentals](../../domains/ai-ml/fundamentals/)
*   **Học máy chuyên sâu:** [Machine Learning Path](../../domains/ai-ml/machine-learning/)
*   **Thế giới GenAI:** [Generative AI Masterclass](../../domains/ai-ml/generative-ai/)
*   **Vận hành mô hình:** [MLOps Guide](../../domains/ai-ml/mlops/)
*   **Hệ điều hành trí tuệ:** [Systems Thinking](../chapters/09-systems-thinking.md)
