# 🌐 Web Development Knowledge Audit: Thử thách "SaaS Transformation"

> **Mục đích:** Đo lường năng lực thiết kế, xây dựng và tối ưu hóa ứng dụng web hiện đại (Fullstack), từ hiệu năng Frontend (UX/Performance) đến độ tin cậy Backend (Scalability/Security).
> **Phiếu trả lời:** [Tải mẫu tại đây](../templates/web-dev-answer-template.md)
> 
> **Kịch bản:** Bạn là **Fullstack Architect** cho "EduStream" - một nền tảng học trực tuyến quy mô lớn. Hệ thống đang gặp khó khăn khi số lượng người dùng đồng thời tăng từ 10.000 lên 100.000, gây ra tình trạng lag giao diện, server quá tải và lỗi bảo mật dữ liệu.

---

## 🎨 Thử thách 1: Frontend Performance & UX (Trải nghiệm người dùng)
*Đo lường năng lực tối ưu hóa giao diện và hiệu năng trình duyệt.*

**Tình huống:** Trang danh sách khóa học của EduStream mất 5 giây để load trên mobile mạng 4G yếu. Điểm Lighthouse Performance chỉ đạt 45.

**Câu hỏi:**
1.  Nêu 3 kỹ thuật cụ thể để giảm **First Contentful Paint (FCP)** và **Largest Contentful Paint (LCP)** cho một trang web dùng React/Next.js? (Ví dụ: **Code Splitting**, **Image Optimization**, **Streaming SSR**).
2.  Làm thế nào để xử lý **Cumulative Layout Shift (CLS)** khi trang web có nhiều quảng cáo hoặc hình ảnh được load động?

**Thước đo:**
*   **🟢 Beginner:** Biết dùng `useEffect` gọi API và hiển thị loading cơ bản.
*   **🔴 Expert:** Thành thạo tối ưu **Core Web Vitals**, biết cách dùng **Debouncing/Throttling**, **Memoization** (`useMemo`, `useCallback`) và hiểu cơ chế **Reconciliation** của React để tránh re-render thừa.

---

## 🕸️ Thử thách 2: Fullstack Architecture & Data Flow (Kiến trúc hệ thống)
*Đo lường năng lực thiết kế luồng dữ liệu và tích hợp hệ thống.*

**Tình huống:** Hệ thống cần tính năng "Thanh toán khóa học" và "Cấp chứng chỉ tự động". Dữ liệu phải được đồng bộ giữa Frontend, Backend và Database mà không xảy ra tình trạng "Double Charge" (thu tiền 2 lần).

**Câu hỏi:**
1.  Bạn sẽ chọn mô hình Rendering nào cho trang chi tiết khóa học: **Client-Side Rendering (CSR)**, **Server-Side Rendering (SSR)** hay **Static Site Generation (SSG)**? Tại sao?
2.  Làm thế nào để đảm bảo tính **Atomic** (nguyên tử) khi thực hiện giao dịch thanh toán? Bạn sẽ xử lý lỗi thế nào nếu tiền đã trừ nhưng Database chưa kịp cập nhật (Saga pattern hay Distributed Transactions)?

**Thước đo:**
*   **🟢 Beginner:** Biết viết API Route cơ bản, dùng `fetch` từ client.
*   **🔴 Expert:** Thiết kế được hệ thống **Event-driven**, hiểu sâu về **Hydration**, **Server Actions** và các kỹ thuật **Data Fetching** nâng cao (Parallel vs Sequential fetching).

---

## 🔐 Thử thách 3: Web Security & Authentication (Bảo mật)
*Đo lường năng lực bảo vệ dữ liệu người dùng và chống tấn công.*

**Tình huống:** Hacker vừa thực hiện một cuộc tấn công **XSS** và đánh cắp hàng ngàn Session Cookie của người dùng EduStream.

**Câu hỏi:**
1.  Nêu 3 lớp phòng thủ để chống lại tấn công **XSS (Cross-Site Scripting)**? Tại sao việc dùng `dangerouslySetInnerHTML` trong React lại cực kỳ nguy hiểm?
2.  Để lưu trữ **JWT (JSON Web Token)** an toàn, bạn sẽ chọn lưu ở `localStorage` hay `HttpOnly Cookie`? Giải thích lý do bảo mật đằng sau lựa chọn đó.

**Thước đo:**
*   **🟢 Beginner:** Biết dùng thư viện Auth (Clerk, NextAuth) nhưng chưa hiểu bản chất JWT.
*   **🔴 Expert:** Hiểu sâu về **OAuth2/OIDC**, cơ chế **CSRF protection**, **Content Security Policy (CSP)** và biết cách audit lỗ hổng bảo mật định kỳ.

---

## 🏗️ Thử thách 4: Backend Scalability & Caching (Khả năng mở rộng)
*Đo lường năng lực xử lý tải cao và tối ưu hóa tài nguyên server.*

**Tình huống:** Vào giờ cao điểm, Database của EduStream bị "treo" do hàng triệu request truy vấn thông tin khóa học giống nhau.

**Câu hỏi:**
1.  Bạn sẽ thiết lập chiến lược **Caching** như thế nào (Browser Cache, CDN, Redis)? Phân biệt giữa **Cache-Aside** và **Write-Through**.
2.  Làm thế nào để xử lý **N+1 Query Problem** khi lấy danh sách khóa học kèm theo thông tin của hàng trăm giáo viên?

**Thước đo:**
*   **🟢 Beginner:** Biết dùng `SELECT *` và lưu cache đơn giản vào biến toàn cục.
*   **🔴 Expert:** Thành thạo **Database Indexing**, **Query Optimization**, triển khai được mô hình **Microservices** (nếu cần) và hiểu về **Load Balancing**.

---

## 📊 Bảng tự chấm điểm (Scoring Rubric)

| Lĩnh vực | Thang điểm (1-10) | Gợi ý tự vấn |
| :--- | :---: | :--- |
| **Frontend & UI/UX** | ____ / 10 | App của bạn có load mượt ở tốc độ 3G không? UI có bị "nhảy" (Layout shift) không? |
| **Fullstack Logic** | ____ / 10 | Bạn có hiểu rõ luồng dữ liệu từ Client -> Server -> DB và ngược lại không? |
| **Security Mastery** | ____ / 10 | Bạn có dám khẳng định hệ thống của mình an toàn trước OWASP Top 10 không? |
| **Performance & Scale** | ____ / 10 | Hệ thống của bạn có "sống sót" được khi có 100k users cùng lúc không? |
| **Modern Tooling** | ____ / 10 | Bạn có làm chủ TypeScript, Next.js và các công cụ CI/CD hiện đại không? |

### 🏆 Xếp hạng năng lực Web Dev:
*   **0 - 15 điểm:** **Junior Web Developer**. Cần học chắc kiến thức nền tảng tại `domains/web-dev/`.
*   **16 - 30 điểm:** **Mid-level Developer**. Có khả năng build sản phẩm nhưng chưa tối ưu về bảo mật và hiệu năng.
*   **31 - 45 điểm:** **Senior Fullstack Developer**. Khả năng dẫn dắt technical cho một dự án SaaS phức tạp.
*   **46 - 50 điểm:** **Web Architect / Technical Lead**. Bạn có thể thiết kế các hệ thống quy mô hàng triệu người dùng.

---

## 🔑 Answer Key: Góc nhìn Chuyên gia (Expert Guidelines)

### Thử thách 1: Performance
*   **LCP:** Dùng `Priority Hints` cho ảnh chính, nén ảnh sang định dạng `WebP/AVIF`, sử dụng CDN.
*   **CLS:** Luôn khai báo `width/height` cho ảnh và video, dành sẵn khoảng trống cho quảng cáo (Skeleton Screens).

### Thử thách 2: Architecture
*   **Rendering:** Chi tiết khóa học nên dùng **SSG with ISR (Incremental Static Regeneration)** để vừa nhanh vừa cập nhật dữ liệu mới.
*   **Transaction:** Dùng Database Transactions để đảm bảo tính toàn vẹn. Với hệ thống lớn, dùng Message Queue (Kafka/RabbitMQ) để xử lý thanh toán bất đồng bộ.

### Thử thách 3: Security
*   **Auth:** Luôn dùng `HttpOnly, Secure, SameSite=Strict` Cookie để chống XSS đánh cắp token. Sử dụng `Helmet.js` cho Express hoặc cấu hình `security headers` cho Next.js.

### Thử thách 4: Scalability
*   **N+1:** Sử dụng `Dataloader` hoặc viết câu lệnh `JOIN` chính xác trong SQL.
*   **Index:** Tạo Index cho các cột thường xuyên `WHERE` hoặc `JOIN` nhưng không được lạm dụng vì sẽ làm chậm quá trình `INSERT/UPDATE`.

---

## 🚀 Tài liệu bổ trợ để "Level Up"
*   **Lộ trình toàn diện:** [Web Dev Roadmap](../../domains/web-dev/README.md)
*   **Hiểu sâu về JS:** [You Don't Know JS](https://github.com/getify/You-Dont-Know-JS)
*   **Thiết kế hệ thống:** [System Design Primer](https://github.com/donnemartin/system-design-primer)
*   **Bảo mật web:** [OWASP Top 10](https://owasp.org/www-project-top-ten/)
