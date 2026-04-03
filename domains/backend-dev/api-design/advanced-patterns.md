# 📡 Các Mẫu Thiết Kế API Nâng Cao

> [← Quay lại Backend Development](../README.md)

Module này giúp bạn chọn đúng phong cách API và áp dụng các thực hành tốt nhất cho các giao diện đạt chuẩn production.

## 1. So sánh các phong cách API

### **REST (Representational State Transfer)**
*   **Triết lý:** Tài nguyên (`/users`) + Động từ (`GET`, `POST`).
*   **Ưu điểm:** Chuẩn, đơn giản, hỗ trợ cache (HTTP GET có thể cache), stateless.
*   **Nhược điểm:** Over-fetching (lấy quá nhiều dữ liệu), Under-fetching (cần nhiều request).
*   **Phù hợp cho:** Public APIs, CRUD đơn giản, ứng dụng định hướng tài nguyên.

### **GraphQL (Query Language)**
*   **Triết lý:** Client yêu cầu chính xác dữ liệu nó cần. Một endpoint duy nhất (`/graphql`).
*   **Ưu điểm:** Lấy dữ liệu hiệu quả, strong typing (Schema), trải nghiệm dev tốt.
*   **Nhược điểm:** Cache phức tạp (mọi request đều `POST`), vấn đề N+1 query, bảo mật khó hơn (độ sâu truy vấn).
*   **Phù hợp cho:** Ứng dụng mobile, frontend phức tạp, tổng hợp nhiều nguồn dữ liệu.

### **gRPC (Google Remote Procedure Call)**
*   **Triết lý:** Gọi hàm từ xa dùng Protobuf (nhị phân) qua HTTP/2.
*   **Ưu điểm:** Rất nhanh (nhị phân), hợp đồng chặt chẽ (.proto), hỗ trợ streaming (Server/Client streaming).
*   **Nhược điểm:** Không thân thiện trình duyệt (cần proxy gRPC-Web), khó debug (định dạng nhị phân).
*   **Phù hợp cho:** Giao tiếp microservices (luồng East-West), API nội bộ hiệu năng cao.

### **WebSocket**
*   **Triết lý:** Kết nối persistent full-duplex. Real-time.
*   **Ưu điểm:** Cập nhật tức thì (Chat, Game, Live Feed), overhead thấp hơn polling.
*   **Nhược điểm:** Quản lý kết nối (stateful), cân bằng tải phức tạp (cần sticky sessions).
*   **Phù hợp cho:** Ứng dụng real-time.

---

## 2. Mẫu API Gateway
Một điểm vào duy nhất cho mọi client.

### **Trách nhiệm cốt lõi**
1.  **Routing:** `/user/*` -> User Service, `/order/*` -> Order Service.
2.  **Authentication/Authorization:** Validate JWT tập trung. Giảm tải auth khỏi services.
3.  **Rate Limiting:** Bảo vệ backend khỏi lạm dụng.
4.  **Transformation:** Chuyển JSON -> Protobuf, hoặc tổng hợp phản hồi.

### **BFF (Backend for Frontend)**
*   Tạo Gateway/Service riêng cho từng loại client.
    *   `Mobile-BFF` -> Tối ưu cho màn hình nhỏ, băng thông thấp.
    *   `Web-BFF` -> Dữ liệu phong phú.
    *   `Public-API-Gateway` -> Giới hạn tần suất nghiêm ngặt, tài liệu đầy đủ.

---

## 3. Chiến lược Versioning
API thay đổi. Đừng làm hỏng client.

1.  **URI Path:** `/api/v1/users` (Phổ biến nhất, rõ ràng).
2.  **Query Parameter:** `/api/users?v=1` (Dễ triển khai, có thể cache).
3.  **Header:** `Accept: application/vnd.myapi.v1+json` (Chuẩn REST thuần, khó test nhất).

---

## 4. Idempotency
Đảm bảo retry an toàn. Nếu client gửi cùng một request hai lần (vd: timeout mạng), kết quả phải như nhau.

*   **Phương thức an toàn:** `GET`, `PUT`, `DELETE` là idempotent theo định nghĩa.
*   **Phương thức không an toàn:** `POST` (tạo tài nguyên mới).
*   **Triển khai:** Client gửi header `Idempotency-Key` (UUID). Server kiểm tra Redis: “Đã xử lý UUID này chưa?”. Nếu rồi -> Trả kết quả cũ. Nếu chưa -> Xử lý và lưu.
