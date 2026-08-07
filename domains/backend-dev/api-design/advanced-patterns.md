# 📡 Các mẫu thiết kế API nâng cao

> [← Quay lại Backend Development](../README.md)

Module này giúp chọn đúng phong cách API và áp dụng thực hành tốt cho giao diện đạt chuẩn production.

## 1. So sánh các phong cách API

### **REST (Representational State Transfer)**
*   **Triết lý:** Tài nguyên (`/users`) + động từ (`GET`, `POST`).
*   **Ưu:** Chuẩn, đơn giản, hỗ trợ cache (HTTP GET), stateless.
*   **Nhược:** Over-fetching (lấy dư), Under-fetching (phải gọi nhiều request).
*   **Phù hợp:** Public API, CRUD đơn giản, ứng dụng định hướng tài nguyên.

### **GraphQL (Query Language)**
*   **Triết lý:** Client yêu cầu đúng dữ liệu cần, một endpoint duy nhất (`/graphql`).
*   **Ưu:** Lấy dữ liệu hiệu quả, schema mạnh (strong typing), DX tốt.
*   **Nhược:** Cache phức tạp (đa số `POST`), dễ dính N+1 query, kiểm soát độ sâu truy vấn cần cẩn trọng.
*   **Phù hợp:** Ứng dụng mobile, frontend phức tạp, hợp nhất nhiều nguồn dữ liệu.

### **gRPC (Google Remote Procedure Call)**
*   **Triết lý:** Gọi hàm từ xa dùng Protobuf (nhị phân) qua HTTP/2.
*   **Ưu:** Nhanh (nhị phân), hợp đồng chặt (.proto), hỗ trợ streaming hai chiều.
*   **Nhược:** Không thân thiện trình duyệt (cần proxy gRPC-Web), debug khó (nhị phân).
*   **Phù hợp:** Giao tiếp microservice (East-West), API nội bộ hiệu năng cao.

### **WebSocket**
*   **Triết lý:** Kết nối persistent full-duplex, real-time.
*   **Ưu:** Cập nhật tức thì (chat, game, live feed), overhead thấp hơn polling.
*   **Nhược:** Quản lý kết nối stateful, cân bằng tải cần sticky session.
*   **Phù hợp:** Ứng dụng real-time.

---

## 2. Mẫu API Gateway
Một điểm vào duy nhất cho mọi client.

### **Trách nhiệm cốt lõi**
1.  **Routing:** `/user/*` → User Service, `/order/*` → Order Service.
2.  **Authentication/Authorization:** Validate JWT tập trung, giảm tải auth khỏi services.
3.  **Rate limiting:** Bảo vệ backend khỏi lạm dụng.
4.  **Transformation:** Chuyển JSON → Protobuf, hoặc tổng hợp phản hồi.

### **BFF (Backend for Frontend)**
*   Tạo gateway/service riêng cho từng loại client:
    *   `Mobile-BFF` → tối ưu màn hình nhỏ, băng thông thấp.
    *   `Web-BFF` → dữ liệu phong phú.
    *   `Public-API-Gateway` → giới hạn tần suất nghiêm ngặt, tài liệu đầy đủ.

---

## 3. Chiến lược versioning
API sẽ thay đổi, cần tránh phá client.

1.  **URI Path:** `/api/v1/users` (Phổ biến nhất, rõ ràng).
2.  **Query Parameter:** `/api/users?v=1` (Dễ triển khai, có thể cache).
3.  **Header:** `Accept: application/vnd.myapi.v1+json` (Chuẩn REST thuần, khó test nhất).

---

## 4. Idempotency
Đảm bảo retry an toàn: nếu client gửi cùng request hai lần (ví dụ timeout mạng), kết quả phải như nhau.

*   **Phương thức an toàn:** `GET`, `PUT`, `DELETE` là idempotent theo định nghĩa.
*   **Phương thức không an toàn:** `POST` (tạo tài nguyên mới).
*   **Triển khai:** Client gửi header `Idempotency-Key` (UUID). Server kiểm tra Redis: “Đã xử lý UUID này chưa?”. Nếu rồi -> Trả kết quả cũ. Nếu chưa -> Xử lý và lưu.
