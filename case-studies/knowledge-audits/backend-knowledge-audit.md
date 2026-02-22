# ⚙️ Backend Knowledge Audit: Thử thách "E-commerce Scale-up"

> **Mục đích:** Đo lường năng lực thiết kế, vận hành và tối ưu hóa hệ thống Backend toàn diện.
> **Phiếu trả lời:** [Tải mẫu tại đây](../templates/backend-answer-template.md)
> 
> **Kịch bản:** Bạn là **Lead Backend Engineer** của "MegaStore" - một nền tảng thương mại điện tử đang tăng trưởng nóng. Hệ thống đang gặp khó khăn khi chuẩn bị cho sự kiện "Super Sale 11.11" với dự kiến traffic tăng gấp 20 lần ngày thường.

---

## 🗄️ Thử thách 1: Database & Data Consistency (Dữ liệu & Nhất quán)
*Đo lường năng lực thiết kế DB và xử lý tranh chấp dữ liệu.*

**Tình huống:** Hệ thống bán hàng Flash Sale thường xuyên xảy ra tình trạng "bán quá số lượng" (Over-selling). Hai người dùng cùng mua một món hàng cuối cùng tại cùng một thời điểm, và cả hai đều thanh toán thành công.

**Câu hỏi:**
1.  Làm thế nào để xử lý triệt để vấn đề **Race Condition** này ở cấp độ Database? Bạn sẽ chọn **Pessimistic Locking** hay **Optimistic Locking**? Tại sao?
2.  Nếu hệ thống sử dụng kiến trúc Microservices với Database riêng biệt (Inventory Service và Order Service), làm thế nào để đảm bảo tính nhất quán dữ liệu giữa hai service này (Distributed Transactions)?

**Thước đo:**
*   **🟢 Beginner:** Biết dùng `UPDATE SET stock = stock - 1`.
*   **🔴 Expert:** Giải thích được sự khác biệt giữa các **Isolation Levels** (Read Committed vs Serializable). Đề xuất được **Saga Pattern** (Choreography hoặc Orchestration) cho giao dịch phân tán.

---

## 🛡️ Thử thách 2: API Design & Security (Giao tiếp & Bảo mật)
*Đo lường năng lực thiết kế API chuẩn mực và an toàn.*

**Tình huống:** MegaStore muốn mở rộng API cho các đối tác bên thứ ba. Tuy nhiên, tuần trước hệ thống vừa bị tấn công **Credential Stuffing** và **DDoS** làm tê liệt service đăng nhập.

**Câu hỏi:**
1.  Bạn sẽ thiết kế cơ chế **Authentication** và **Authorization** như thế nào cho đối tác? (API Keys, OAuth2, hay JWT)? Ưu và nhược điểm của từng loại?
2.  Làm thế nào để bảo vệ hệ thống khỏi việc bị khai thác thông tin qua các lỗi **IDOR** (Insecure Direct Object Reference) và **SQL Injection**?
3.  Bạn sẽ triển khai cơ chế **Rate Limiting** ở đâu (API Gateway hay Service level) và dùng thuật toán nào (Token Bucket, Leaky Bucket)?

**Thước đo:**
*   **🟢 Beginner:** Biết dùng JWT cơ bản và dùng ORM để chống SQL Injection.
*   **🔴 Expert:** Thiết kế được luồng **OAuth2 Client Credentials**, áp dụng **RBAC/ABAC** chặt chẽ, và hiểu rõ cách dùng **Redis-based Rate Limiter** để bảo vệ hệ thống ở quy mô lớn.

---

## 🚀 Thử thách 3: System Design & Scalability (Kiến trúc & Mở rộng)
*Đo lường năng lực thiết kế hệ thống chịu tải cao.*

**Tình huống:** Trong đợt Sale, database bị nghẽn (bottleneck) do số lượng query "Read" quá lớn để xem thông tin sản phẩm. Hệ thống cũng bị chậm khi xử lý gửi email xác nhận và cập nhật điểm thành viên sau mỗi đơn hàng.

**Câu hỏi:**
1.  Bạn sẽ thiết kế chiến lược **Caching** như thế nào? Làm sao để xử lý vấn đề **Cache Aside**, **Cache Penetration**, và **Cache Stampede**?
2.  Làm thế nào để xử lý các tác vụ gửi email và cập nhật điểm một cách bất đồng bộ (Asynchronous)? Bạn chọn **Message Queue** nào (RabbitMQ, Kafka, hay SQS)?
3.  Khi nào bạn nên thực hiện **Database Sharding** thay vì chỉ dùng **Read Replicas**?

**Thước đo:**
*   **🟢 Beginner:** Biết dùng Redis để cache đơn giản và dùng Cron job để xử lý task ngầm.
*   **🔴 Expert:** Thiết kế được hệ thống **Multi-level Caching**, sử dụng **Event-driven Architecture** với Kafka để handle hàng triệu events mỗi giây, và hiểu rõ các bài toán về **Data Sharding Key** và **Rebalancing**.

---

## 📊 Thử thách 4: Observability & Reliability (Giám sát & Tin cậy)
*Đo lường năng lực vận hành và xử lý sự cố.*

**Tình huống:** Hệ thống bỗng nhiên phản hồi chậm (High Latency) nhưng CPU và RAM của các services vẫn ở mức thấp. Bạn không biết lỗi bắt đầu từ service nào trong chuỗi 10 microservices.

**Câu hỏi:**
1.  Bạn cần những chỉ số (Metrics) nào để xác định vấn đề? (Xem xét mô hình **Golden Signals**).
2.  Làm thế nào để truy vết một request đi qua nhiều services khác nhau? (Sử dụng **Distributed Tracing**).
3.  Khi một service phía hạ nguồn (downstream) bị chậm, làm thế nào để ngăn chặn nó kéo sập toàn bộ hệ thống phía trên? (Áp dụng **Circuit Breaker**).

**Thước đo:**
*   **🟢 Beginner:** Check log file bằng lệnh `tail -f` và khởi động lại server khi có lỗi.
*   **🔴 Expert:** Thiết lập được **ELK Stack** hoặc **Loki** cho Centralized Logging, sử dụng **Prometheus/Grafana** cho Dashboard, và triển khai **Jaeger/Zipkin** cho Tracing. Hiểu rõ cách cấu hình **Circuit Breaker** (Hystrix/Resilience4j).

---

## 🧠 Thử thách 5: Applied Mental Models (Tư duy thực dụng)
*Đo lường năng lực ra quyết định và quản lý nợ kỹ thuật.*

**Tình huống:** CEO muốn ra mắt tính năng "Live Auction" (Đấu giá trực tiếp) trong vòng 1 tuần để bắt kịp trend. Team đang quá tải và code cũ đang khá rối.

**Câu hỏi:**
1.  Bạn sẽ áp dụng **Pareto Principle (80/20)** như thế nào để chọn ra những phần cốt lõi cần làm trước?
2.  Làm thế nào để quản lý **Technical Debt** khi phải chạy deadline gấp? Bạn sẽ chấp nhận đánh đổi gì và sẽ "trả nợ" như thế nào sau đó?
3.  Áp dụng **Inversion Thinking**: Những nguyên nhân nào có thể khiến tính năng "Live Auction" này làm sập toàn bộ hệ thống MegaStore hiện tại?

**Thước đo:**
*   **🟢 Beginner:** Cố gắng làm hết mọi thứ và OT xuyên đêm.
*   **🔴 Expert:** Biết cách nói "Không" hoặc đề xuất MVP tối giản. Thiết kế các **Feature Flags** để bật/tắt nhanh tính năng nếu có sự cố, và có kế hoạch **Refactoring** rõ ràng sau khi launch.

---

## 🌪️ Thử thách 6: Chaos Engineering & Resilience (Thử nghiệm hỗn loạn)
*Đo lường năng lực thiết kế hệ thống có khả năng tự phục hồi (Self-healing).*

**Tình huống:** MegaStore đã có kiến trúc tốt, nhưng CTO lo ngại về các sự cố "Black Swan" (thiên nga đen) - những lỗi hiếm gặp nhưng có thể gây sập hệ thống diện rộng (ví dụ: đứt cáp quang biển, lỗi trung tâm dữ liệu của AWS). Bạn được giao nhiệm vụ triển khai **Chaos Engineering**.

**Câu hỏi:**
1.  Bước đầu tiên trước khi "phá hoại" hệ thống là gì? Làm thế nào để bạn xác định được **Steady State** (Trạng thái ổn định) của MegaStore?
2.  Bạn sẽ thiết kế những thí nghiệm hỗn loạn nào? (Ví dụ: **Network Latency Injection**, **Resource Exhaustion**, hay **Region Failover**)? Thí nghiệm nào là ưu tiên số 1?
3.  Làm thế nào để kiểm soát **Blast Radius** (Bán kính thiệt hại) để đảm bảo thí nghiệm không làm sập hệ thống thật và ảnh hưởng đến khách hàng đang thanh toán?

**Thước đo:**
*   **🟢 Beginner:** Nghĩ rằng Chaos Engineering chỉ là đi "tắt server" ngẫu nhiên.
*   **🔴 Expert:** Định nghĩa được các chỉ số sức khỏe (SLIs/SLOs), thiết lập được **Game Days** cho team, và tự động hóa việc tiêm lỗi (Fault Injection) vào môi trường Staging/Canary trước khi chạy trên Production.

---

## ☁️ Thử thách 7: Cloud Native & Kubernetes Optimization (Tối ưu đám mây)
*Đo lường năng lực điều phối container và quản lý chi phí hạ tầng.*

**Tình huống:** MegaStore đã chuyển lên Kubernetes (K8s) trên AWS (EKS). Tuy nhiên, hóa đơn tiền điện toán hàng tháng đang tăng vọt. Mặc dù hệ thống chạy ổn định, nhưng hiệu suất sử dụng tài nguyên (CPU/RAM Utilization) của các Node chỉ đạt khoảng 30%.

**Câu hỏi:**
1.  Làm thế nào để tự động tăng/giảm số lượng Pods dựa trên tải thực tế? Sự khác biệt giữa **HPA (Horizontal Pod Autoscaler)** và **VPA (Vertical Pod Autoscaler)** là gì? Khi nào nên dùng loại nào?
2.  Để giảm chi phí hạ tầng (EC2 instances), bạn sẽ cấu hình **Cluster Autoscaler** kết hợp với **Spot Instances** như thế nào để đảm bảo hệ thống không bị gián đoạn (Eviction)?
3.  Làm thế nào để tối ưu hóa việc phân bổ tài nguyên cho từng Container thông qua việc cấu hình **Requests** và **Limits**? Nếu đặt Limit quá cao hoặc quá thấp, hệ quả sẽ là gì?

**Thước đo:**
*   **🟢 Beginner:** Biết dùng `kubectl apply -f deployment.yaml` cơ bản.
*   **🔴 Expert:** Làm chủ các khái niệm **Taints & Tolerations**, **Node Affinity**, sử dụng các công cụ như **Karpenter** để scale cluster cực nhanh, và triển khai **Service Mesh** (như Istio) để quản lý traffic nội bộ hiệu quả.

---

## 🤖 Thử thách 8: AI Engineering & LLM Serving (Kỹ thuật AI)
*Đo lường năng lực tích hợp và tối ưu hóa các mô hình ngôn ngữ lớn (LLM).*

**Tình huống:** MegaStore ra mắt tính năng "AI Shopping Assistant" để hỗ trợ khách hàng. Bạn sử dụng kiến trúc **RAG (Retrieval-Augmented Generation)** kết hợp với một Vector Database. Tuy nhiên, chatbot thường xuyên "ảo tưởng" (hallucination), trả lời rất chậm (latency cao) và chi phí API đang tiêu tốn hàng nghìn USD mỗi ngày.

**Câu hỏi:**
1.  Làm thế nào để giảm thiểu tình trạng chatbot trả lời sai kiến thức về sản phẩm? Bạn sẽ tối ưu khâu **Chunking strategy** (phân đoạn dữ liệu) hay khâu **Retrieval** (truy xuất) như thế nào (ví dụ: Hybrid Search, Reranking)?
2.  Để giảm chi phí và độ trễ, bạn có đề xuất gì về việc sử dụng **Semantic Caching** hay chuyển sang sử dụng các mô hình **Open-source** (như Llama 3, Mistral) tự hosting?
3.  Nếu tự hosting mô hình, bạn sẽ quản lý và tối ưu hóa hiệu suất sử dụng **GPU** như thế nào? Bạn hiểu gì về các kỹ thuật như **Quantization** (định lượng mô hình) hay **Batching** (xử lý lô)?

**Thước đo:**
*   **🟢 Beginner:** Chỉ biết gọi API OpenAI đơn giản và nhồi toàn bộ dữ liệu vào Prompt một cách thủ công.
*   **🔴 Expert:** Làm chủ các kỹ thuật **Advanced RAG**, tối ưu hóa **Context Window**, biết cách sử dụng **vLLM** hoặc **TGI** để phục vụ mô hình với throughput cao, và hiểu rõ về **GPU Memory Orchestration**.

---

## 📊 Bảng tự chấm điểm (Scoring Rubric)

| Lĩnh vực | Thang điểm (1-10) | Gợi ý tự vấn |
| :--- | :---: | :--- |
| **Database & Consistency** | ____ / 10 | Bạn có hiểu rõ ACID và các kỹ thuật Distributed Locking không? |
| **API & Security** | ____ / 10 | Bạn có thiết kế API theo chuẩn REST/gRPC và bảo mật theo OWASP Top 10? |
| **System Design** | ____ / 10 | Bạn có thể vẽ kiến trúc chịu tải 100k Req/s trên giấy không? |
| **Observability** | ____ / 10 | Bạn có biết dùng Metrics để dự đoán sự cố trước khi nó xảy ra không? |
| **Chaos Engineering** | ____ / 10 | Bạn có dám tự tay "phá" hệ thống của mình để làm nó mạnh hơn không? |
| **Cloud Native & K8s** | ____ / 10 | Bạn có làm chủ được việc điều phối container và túi tiền hạ tầng không? |
| **AI Engineering** | ____ / 10 | Bạn có biết cách làm chatbot "bớt ngáo" và chạy mượt mà trên hạ tầng riêng không? |
| **Strategic Thinking** | ____ / 10 | Bạn chọn giải pháp "đúng nhất" hay giải pháp "phù hợp nhất" với business? |

### 🏆 Xếp hạng năng lực Backend:
*   **0 - 30 điểm:** **Junior Developer**. Cần học chắc kiến thức nền tảng trong `domains/backend-dev/`.
*   **31 - 50 điểm:** **Mid-level Developer**. Có khả năng giải quyết task độc lập nhưng cần rèn luyện thêm về System Design.
*   **51 - 65 điểm:** **Senior/Lead Engineer**. Khả năng thiết kế và xử lý sự cố hệ thống phức tạp tốt.
*   **66 - 80 điểm:** **AI & Cloud Native Architect / CTO**. Bạn là người kiến tạo các hệ thống hiện đại, thông minh và tự động hóa hoàn toàn trên đám mây.

---

## 🔑 Answer Key: Góc nhìn Chuyên gia (Expert Guidelines)

### Thử thách 1: Database
*   **Race Condition:** Dùng **Pessimistic Locking** (`SELECT ... FOR UPDATE`) cho Flash Sale nếu số lượng hàng cực ít và traffic cô đặc. Dùng **Optimistic Locking** (Version field) nếu tranh chấp không quá cao.
*   **Distributed Transactions:** Tránh dùng 2PC (Two-Phase Commit) vì latency cao. Ưu tiên **Saga Pattern (Event-driven)**. Order Service tạo order ở trạng thái PENDING -> Gửi event đến Inventory -> Inventory trừ hàng thành công gửi event lại -> Order chuyển thành COMPLETED. Nếu Inventory thất bại -> gửi event REJECTED -> Order thực hiện **Compensating Transaction** để cancel.

### Thử thách 2: Security
*   **Auth:** Dùng **OAuth2 Client Credentials** cho M2M (Machine-to-Machine). Dùng **OpenID Connect (OIDC)** nếu cần thông tin user.
*   **IDOR:** Không bao giờ dùng ID tăng dần (`/api/orders/123`). Dùng **UUID** hoặc **HashID** kết hợp kiểm tra quyền sở hữu (`owner_id`) trong mọi query.
*   **Rate Limiting:** Dùng **Sliding Window Log** hoặc **Token Bucket** trên Redis để đảm bảo tính chính xác toàn hệ thống.

### Thử thách 3: System Design
*   **Cache Stampede:** Sử dụng **Mutex Locking** ở ứng dụng để chỉ 1 request đi xuống DB khi cache hết hạn, các request khác chờ. Hoặc dùng **Background Refresh** trước khi cache thực sự hết hạn.
*   **Kafka vs RabbitMQ:** Dùng **Kafka** cho Event Sourcing, Logging, Stream processing (high throughput, persistent). Dùng **RabbitMQ** cho các task cần routing phức tạp và độ tin cậy cao của từng message riêng lẻ.

### Thử thách 4: Observability
*   **Golden Signals:** Monitor 4 chỉ số: **Latency** (Độ trễ), **Traffic** (Lưu lượng), **Errors** (Lỗi), **Saturation** (Độ bão hòa tài nguyên).
*   **Circuit Breaker:** Khi service B chậm, service A sẽ "mở mạch" (Open) và trả về lỗi ngay lập tức hoặc dùng cache/default value thay vì chờ timeout, giúp hệ thống không bị hiệu ứng domino.

### Thử thách 5: Tư duy
*   **Technical Debt:** Chấp nhận nợ (ví dụ: thiếu unit test cho phần UI Auction) nhưng phải log lại vào **Tech Debt Backlog** và đặt lịch fix ngay trong sprint tiếp theo.
*   **Feature Flags:** Cực kỳ quan trọng để "Kill" nhanh tính năng lỗi mà không cần redeploy toàn bộ hệ thống.

### Thử thách 6: Chaos Engineering
*   **Steady State:** Phải đo lường được "Trạng thái bình thường" (ví dụ: Tỉ lệ thanh toán thành công là 99.9%, Latency trung bình là 200ms). Nếu sau khi tiêm lỗi mà các chỉ số này vẫn ổn định -> Hệ thống có tính Resilience cao.
*   **Experiments:** Ưu tiên **Dependency Failure** (giả lập một service bên thứ 3 hoặc DB bị sập). Đây là lỗi phổ biến nhất gây sập hệ thống dây chuyền.
*   **Blast Radius:** Luôn bắt đầu thí nghiệm trên một nhóm nhỏ người dùng (Canary) hoặc môi trường mô phỏng chính xác nhất. Phải có nút **"Abort Button"** để dừng thí nghiệm và rollback ngay lập tức nếu mọi thứ vượt tầm kiểm soát.

### Thử thách 7: Cloud Native & K8s
*   **HPA vs VPA:** Dùng **HPA** để scale "chiều ngang" (thêm Pods) - tốt cho web traffic. Dùng **VPA** để scale "chiều dọc" (tăng CPU/RAM cho Pod) - tốt cho các task xử lý data nặng. Lưu ý: Không nên dùng cả hai cùng lúc cho cùng một resource CPU/RAM.
*   **Cost Optimization:** Dùng **Spot Instances** cho các workload không trạng thái (stateless) và có thể chịu lỗi để giảm tới 70-90% chi phí. Sử dụng **Karpenter** thay vì Cluster Autoscaler truyền thống để cấp phát Node theo nhu cầu thực tế của Pod nhanh hơn.
*   **Resource Management:** **Requests** là mức tài nguyên được đảm bảo, **Limits** là mức trần. Nếu không đặt Limit -> một Pod lỗi có thể ngốn sạch CPU Node. Nếu đặt Request quá sát Limit -> Pod dễ bị kill (OOMKilled). Tốt nhất: Set Request sát thực tế và Limit khoảng 1.5 - 2 lần Request.

### Thử thách 8: AI Engineering
*   **Hallucination & RAG:** Để chatbot trả lời chính xác, cần tối ưu khâu **Retrieval**. Sử dụng **Hybrid Search** (kết hợp Keyword Search cho mã sản phẩm và Vector Search cho ngữ nghĩa). Áp dụng thêm bước **Re-ranking** (dùng mô hình như Cohere Rerank) để chọn ra Top-K tài liệu liên quan nhất trước khi đưa vào Prompt.
*   **Cost/Latency:** Triển khai **Semantic Caching** (như GPTCache). Nếu câu hỏi mới tương tự câu hỏi cũ đã có trong cache -> Trả về ngay kết quả mà không cần gọi LLM.
*   **GPU Hosting:** Sử dụng thư viện **vLLM** để tận dụng kỹ thuật **PagedAttention**, giúp tăng throughput lên gấp nhiều lần. Áp dụng **Quantization** (4-bit hoặc 8-bit) để giảm dung lượng mô hình, giúp chạy được các mô hình lớn trên GPU có VRAM thấp mà hiệu năng giảm không đáng kể.

---

## 🚀 Tài liệu bổ trợ để "Level Up"
*   **Nền tảng DB:** [Database Fundamentals](../../domains/backend-dev/database-fundamentals.md)
*   **Thiết kế API:** [API Design Guide](../../domains/backend-dev/api-design-guide.md)
*   **Kiến trúc hệ thống:** [System Design Guide](../../domains/backend-dev/system-design-guide.md)
*   **Bảo mật:** [Backend Security](../../domains/backend-dev/backend-security.md)
*   **Docker & K8s:** [Docker & Kubernetes Guide](../../domains/backend-dev/devops-sre/docker-k8s-guide.md)
