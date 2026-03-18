# Cuộc Chiến Giao Thức (REST vs GraphQL vs gRPC)

> [← Back to API Design](../README.md)

REST (Representational State Transfer) đã thống trị Web suốt một thập kỷ qua với định dạng JSON dễ đọc, tính chất Stateless và bộ quy tắc URL rõ ràng (GET/POST/PUT/DELETE).

Tuy nhiên, khi các hệ thống phình to ra thành **Microservices** hoặc Frontend cần hiển thị giao diện phức tạp, REST bắt đầu đuối sức. Chào mừng gRPC và GraphQL bước vào hàng ngũ Senior Engineers.

---

## 🌐 1. Sự Hụt Hơi Của REST API

REST hoạt động tuyệt vời cho các thao tác CRUD cơ bản. Nhưng nó nảy sinh **2 điểm nghẽn trí mạng**:

1.  **Over-fetching & Under-fetching (Bệnh ăn quá nhiều hoặc quá ít của Frontend):**
    *   *Under-fetching:* App báo Mobile cần Tên User, Các Đơn Hàng Mới Nhất, và Review của từng Đơn. Với REST, Frontend phải gọi Độc lập 3 HTTP Requests: `GET /user`, `GET /orders`, `GET /reviews`. Mạng 3G chập chờn? App load mất 5 giây!
    *   *Over-fetching:* App Desktop chỉ cần mỗi `Email` của User để điền vào Form Mật khẩu. Khi gọi `GET /user`, REST Server trả về hẳn 1 Cục JSON có `Address`, `Preferences`, `Avatar_URL`... nặng 20KB rác mạng (Payload Bloat).

2.  **Chậm Nhịp Chờ Nhau Của Microservices (Chai Cổ Bottle-neck HTTP/1.1):**
    *   Service A (Thanh Toán) muốn hỏi Service B (Kiểm Kho) xem còn iPhone không. REST dùng Text String (JSON) và gửi trên đường ống HTTP/1.1. Parse chuỗi JSON trên 2 máy mất vài mili-giây, cực kỳ tốn CPU ở cấp độ hệ thống. Cứ hỏi nhau tuần tự - Tự nhiên Microservice chậm hơn Monolith!

---

## 🔮 2. GraphQL (Vị Cứu Tinh Của Frontend)

Được Facebook đẻ ra rải quyết việc lấy Data trên Mobile App chậm. 

`GraphQL` là **Ngôn Ngữ Truy Vấn (Query Language)** cho API của bạn. Khách (Frontend) toàn quyền Kêu Gọi Đúng Món Họ Cần, Không Mua Kèm Hàng. 

### Sức Mạnh Tuyệt Đối Đầu Cuối (One Endpoint To Rule Them All):
Thay vì cung cấp`/users`, `/posts`, `/comments`, Backend Mở Đúng 1 Cửa Đi Vào: **`POST /graphql`**.
Frontend bắn gửi yêu cầu (Query):
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
**Nhận Lại Ngay Mạch Chuẩn Không Lệch Nửa Byte Nhu Cầu:**
Backend gỡ cái Query đó, tự đi lục Lõng các Database và gom Lép lại Trả Đáng Sát Bằng Đúng cái Cục JSON mỏng lét với Data Frontend Lần Vừa Nãy Chấm! Đứt Under/Over-fetching Máy.

> 🛠️ **Khi nào dùng?** API Hướng Ra Ngoài Cho Mobile App, Web SPA Cực Lớn Tần Suất Xoắn Khai (Public API cho Client Cần Dữ Liệu Chuyên Môn Biến Dị). 

---

## 🚀 3. gRPC (Sát Thủ Bắn Cao Phân Microservices Gốc) 

Nếu GraphQL chiều lòng Frontend, thì **gRPC** (Google Remote Procedure Call) là Vua Của Tốc Độ Giao Thức Backend Truyền Cùng Backend (Máy Vây Máy).

### A. HTTP/2.0 Bẩm Sinh Và Multi-plexing
REST nằm trên HTTP 1.1 Kêu Chặn Gửi Điền Rớt Từng Mảng. gRPC Bay Mạch Mở Lên Đường Truyền HTTP/2. Cho Phép Luồng Đi Sông Và Cây Cầu Rộng Mở Cầm (Multiplexing) 100 Cuốc Trò Chuyện 2 Máy Bắn Lệnh Vào 1 Luồng Socket Chống Dữ.

### B. Protocol Buffers (Bóp Thịt JSON) 
1 File JSON Rộng 200 Bytes Toàn Chữ `{ "id": 1, "name": "Nam" }`. 
gRPC vứt thẳng JSON. Dùng `ProtoBuf` nén mã hóa Nhị Phân (Binary File). Trả Truyền Chỉ Còn Khoảng Dưới 40 Bytes. Mã Hóa Máy Tính Nhận Chỉ Quá Là Bit 0101 Cột Thẳng Biến RAM Trong C Tốc Độ x10 Lần Việc Giải Mã String Sang Object Của REST!

```protobuf
// Định Hình Form Giao Gước Hẹn Nhau (File .proto)
message NguoiDungHoi {
  int32 id = 1; 
  string name = 2; 
}
```

### C. Mất Cửa Chống Kẹt Phân (Stubs Code Generation)
Sợ Sai Lỗi Đánh Chữ `nema` thay vì `name` Lúc Coder Đánh String JSON Mù Giữa 2 Team Code? 
File `.proto` Gốc Tự Động Gen Ra Gói Code Typescript, Gói Code Golang, Gói Code C#. Team Gọi Cứ Móc Theo Hàm Ráp Code Bật IntelliCode Xanh Lên. An Toàn Cữ Lực Giữa Service.

> 🛠️ **Khi nào dùng?** Bất cứ lúc nào 2 cái Microservices Nóc Đuôi Gọi Cho Nhau Trong Nội Mạng (Internal Service-to-Service Communication). Bỏ REST Ngay và Mãi Mãi Nếu Build Micro-System Chịu Tải Triệu RPS! Dùng Chống Tường Gọi Chặn Backend Bủa Lưới!
