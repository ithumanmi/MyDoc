# Cuộc Chiến Giao Thức (REST vs GraphQL vs gRPC)

> [← Quay lại API Design](../README.md)

REST (Representational State Transfer) đã thống trị Web suốt một thập kỷ qua với định dạng JSON dễ đọc, tính chất stateless và bộ quy tắc URL rõ ràng (GET/POST/PUT/DELETE).

Tuy nhiên, khi hệ thống mở rộng thành **Microservices** hoặc frontend cần giao diện phức tạp, REST bộc lộ hạn chế. gRPC và GraphQL xuất hiện để giải quyết các vấn đề đó.

---

## 🌐 1. Hạn chế của REST API

REST hoạt động tốt cho thao tác CRUD cơ bản, nhưng có **2 điểm nghẽn lớn**:

1.  **Over-fetching & Under-fetching:**
    *   *Under-fetching:* Ứng dụng mobile cần Tên người dùng, Đơn hàng mới nhất và Đánh giá của từng đơn. Với REST, frontend phải gọi 3 request: `GET /user`, `GET /orders`, `GET /reviews`. Mạng yếu sẽ khiến thời gian tải tăng đáng kể.
    *   *Over-fetching:* Ứng dụng desktop chỉ cần `email` để điền vào form. Gọi `GET /user` trả về toàn bộ JSON gồm `Address`, `Preferences`, `Avatar_URL`... gây dư thừa payload.

2.  **Độ trễ giữa microservices (HTTP/1.1 bottleneck):**
    *   Service A (Thanh toán) gọi Service B (Kiểm kho) để kiểm tra tồn. REST dùng JSON text qua HTTP/1.1; việc parse chuỗi trên nhiều service gây tốn CPU và tăng độ trễ. Nếu gọi tuần tự, hệ thống microservices có thể chậm hơn monolith.

---

## 🔮 2. GraphQL (Giải pháp cho frontend)

GraphQL được Facebook tạo ra để cải thiện lấy dữ liệu trên mobile app.

`GraphQL` là **ngôn ngữ truy vấn (Query Language)** cho API. Client có thể yêu cầu đúng dữ liệu cần, không dư thừa.

### Một endpoint duy nhất (One Endpoint To Rule Them All)
Thay vì cung cấp `/users`, `/posts`, `/comments`, backend chỉ mở **`POST /graphql`**.
Frontend gửi truy vấn (query):
```graphql
query BắtThằngNàyThôi {
  user(id: 123) {
    name
    email
    orders(limit: 5) {
      id
      total_price
      items {
        product_name
      }
    }
  }
}
```
**Kết quả trả về đúng nhu cầu:**
Backend xử lý query, truy vấn các nguồn dữ liệu và trả về JSON đúng phần frontend yêu cầu, loại bỏ over/under-fetching.

> 🛠️ **Khi nào dùng?** Public API cho mobile app, web SPA lớn, hoặc khi client cần dữ liệu linh hoạt/phức tạp.

---

## 🚀 3. gRPC (Tối ưu cho giao tiếp backend-backend) 

Nếu GraphQL phục vụ frontend, thì **gRPC** (Google Remote Procedure Call) tối ưu cho tốc độ giao tiếp giữa các backend service.

### A. HTTP/2.0 và multiplexing
REST chạy trên HTTP/1.1. gRPC sử dụng HTTP/2, hỗ trợ multiplexing nhiều cuộc gọi trên một kết nối, giảm độ trễ.

### B. Protocol Buffers (nhỏ gọn hơn JSON)
Một JSON 200 bytes `{ "id": 1, "name": "Nam" }` khi dùng Protobuf có thể xuống dưới 40 bytes. Dữ liệu nhị phân giải mã nhanh hơn chuỗi JSON, giúp giảm băng thông và CPU.

```protobuf
// Định nghĩa cấu trúc trong file .proto
message UserRequest {
  int32 id = 1; 
  string name = 2; 
}
```

### C. Sinh mã (code generation)
File `.proto` có thể tự động sinh client/server stub cho TypeScript, Go, C#, v.v. Giảm lỗi chính tả trường dữ liệu và giúp tích hợp an toàn hơn giữa các service.

> 🛠️ **Khi nào dùng?** Giao tiếp nội bộ giữa các microservice. Ưu tiên gRPC khi cần thông lượng cao và độ trễ thấp.
