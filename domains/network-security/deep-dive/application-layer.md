# 🌐 Application Layer Deep Dive: Lớp Ứng dụng

> [← Back to Network Security](../README.md)

Lớp ứng dụng (Layer 7) là nơi giao tiếp giữa phần mềm và mạng.
90% công việc của Web Developer diễn ra ở đây.

---

## 1. Sự tiến hóa của HTTP (HyperText Transfer Protocol)

### **HTTP/1.1 (1997) - The Standard**
*   **Cơ chế:** Text-based. Mỗi request mở một kết nối TCP riêng (hoặc dùng Keep-Alive).
*   **Vấn đề:** Head-of-Line Blocking (HoL). Nếu request đầu tiên bị kẹt (ảnh to), các request sau (CSS/JS) phải chờ.

### **HTTP/2 (2015) - Speed Demon**
*   **Cơ chế:** Binary protocol (Nhị phân, không phải Text).
*   **Multiplexing:** Gửi nhiều request song song trên **MỘT** kết nối TCP duy nhất.
*   **Server Push:** Server chủ động gửi CSS/JS cho Client trước khi Client kịp hỏi.
*   **Header Compression (HPACK):** Giảm dung lượng Header.

### **HTTP/3 (2022) - QUIC & UDP**
*   **Vấn đề của HTTP/2:** Vẫn dùng TCP. Nếu mất 1 gói tin TCP, toàn bộ kết nối bị chậm lại (TCP HoL Blocking).
*   **Giải pháp:** HTTP/3 chạy trên **UDP** (giao thức QUIC của Google).
*   **Ưu điểm:** Kết nối cực nhanh (0-RTT), chuyển mạng (Wifi -> 4G) không bị rớt kết nối.

---

## 2. Architecture Patterns (Mô hình Kiến trúc)

### **A. Proxy – Hiểu ĐÚNG bản chất**
👉 **Proxy = Trung gian (Middleman) đứng giữa Client và Server.**
`Client → Proxy → Server`

**Proxy có thể:**
*   **Intercept:** Chặn bắt gói tin.
*   **Modify:** Thay đổi nội dung request/response.
*   **Cache:** Lưu lại dữ liệu để trả về nhanh hơn.
*   **Anonymize:** Ẩn danh tính người gửi.

### **B. Phân loại Proxy**

#### **1. Forward Proxy (Client-side Proxy)**
*   **Context:** Client **chủ động** cấu hình để đi qua Proxy này.
*   **Luồng:** `Browser → Forward Proxy → Internet`.
*   **Mục đích:**
    *   **Ẩn IP:** Server đích chỉ thấy IP của Proxy, không thấy IP thật của Client.
    *   **Vượt Firewall:** Truy cập các trang web bị chặn bởi nhà mạng hoặc công ty.
    *   **Crawl Web:** Dùng nhiều Proxy IP khác nhau để không bị chặn khi cào dữ liệu.
*   **Ví dụ:** Squid, Shadowsocks, HTTP/SOCKS5 Proxy.

#### **2. Reverse Proxy (Server-side Proxy) ⭐⭐⭐**
*   **Context:** Client **không biết** mình đang đi qua Proxy. Client nghĩ mình đang nói chuyện trực tiếp với Server.
*   **Luồng:** `Client → Reverse Proxy (Nginx) → App Server`.
*   **Mục đích (System Design):**
    *   **Load Balancing:** Chia tải cho nhiều Server con.
    *   **SSL Termination:** Proxy đảm nhận việc giải mã HTTPS, giảm tải CPU cho App Server.
    *   **Rate Limiting:** Chặn DDoS, giới hạn số request.
    *   **Routing:** Điều hướng request (`/api` vào Server A, `/static` vào Server B).
*   **Ví dụ:** Nginx, HAProxy, Traefik, Envoy.

### **C. Phân biệt các khái niệm dễ nhầm lẫn**

| Khái niệm | Bản chất (Core Concept) | Layer (OSI) | Mục đích chính |
| :--- | :--- | :--- | :--- |
| **Forward Proxy** | Trung gian phía Client | Layer 7 (App) | Ẩn danh, Vượt tường lửa. |
| **Reverse Proxy** | Trung gian phía Server | Layer 7 (App) | Bảo vệ Server, SSL Offloading. |
| **Load Balancer** | Cảnh sát giao thông | Layer 4 hoặc 7 | Phân phối traffic, Tăng khả năng chịu tải (Availability). |
| **API Gateway** | Reverse Proxy "thông minh" | Layer 7 (App) | Quản lý API (Auth, Rate Limit, Billing, Analytics). |
| **VPN** | Đường hầm bí mật (Tunnel) | Layer 3 (Network) | Mã hóa toàn bộ kết nối của thiết bị (OS Level), không chỉ Web. |
| **CDN** | Reverse Proxy phân tán | Layer 7 (App) | Cache nội dung tĩnh (Ảnh/Video) tại Edge Server gần người dùng nhất. |
| **Firewall** | Bức tường bảo vệ | Layer 3/4 (Packet) hoặc 7 (WAF) | Cho phép hoặc Chặn traffic dựa trên Rule (IP, Port, Protocol). |

### **D. Proxy trong thực tế (Use Cases)**

Bạn sẽ gặp Proxy ở đâu trong công việc?

#### **1. Debugging & Development (Dev Tools)**
*   **Mục đích:** Xem App Mobile/Web gửi API gì lên Server? Tại sao API lỗi?
*   **Cách dùng:** Cài Certificate của Proxy vào điện thoại -> Mọi traffic đi qua máy tính -> Bạn soi được hết (Man-in-the-Middle).
*   **Tools:** Charles Proxy (MacOS), Fiddler (Windows), Mitmproxy (CLI).

#### **2. Crawling & Data Mining (Bot)**
*   **Vấn đề:** Gửi 1000 requests/phút từ 1 IP -> Bị chặn ngay lập tức.
*   **Giải pháp:**
    *   **Rotating Proxy:** Tự động đổi IP sau mỗi request.
    *   **Residential Proxy:** Dùng IP mạng gia đình (ISP thật) -> Rất khó bị phát hiện (nhưng đắt).
    *   **Datacenter Proxy:** Dùng IP Server (AWS, Google) -> Rẻ, nhanh, nhưng dễ bị blacklist.

#### **3. Game & Realtime**
*   **Mục đích:** Giảm Ping (Latency), Fake IP để chơi game server nước ngoài (Region Lock).
*   **Kỹ thuật:**
    *   **TCP Proxy:** Cho game MMORPG.
    *   **UDP Relay:** Cho game bắn súng (FPS), MOBA.
    *   **Anti-DDoS:** Proxy giấu IP thật của Game Server để tránh bị tấn công.

#### **4. Advanced Security**
*   **Identity-Aware Proxy (IAP):** (Google Cloud). Thay thế VPN truyền thống. Cho phép nhân viên truy cập web nội bộ từ xa bằng cách đăng nhập Google (SSO) mà không cần cài VPN Client.
*   **Zero Trust Proxy:** Xác thực danh tính và thiết bị của người dùng trước khi cho phép kết nối đến bất kỳ ứng dụng nào.

### **E. Load Balancer**
*   **Layer 4 (Transport):** Cân bằng tải dựa trên IP/Port. Nhanh nhưng "ngu" (không biết nội dung gói tin).
*   **Layer 7 (Application):** Cân bằng tải dựa trên URL, Cookie, Header. Thông minh nhưng chậm hơn. (VD: URL `/video` -> Server mạnh, `/text` -> Server yếu).

### **D. API Gateway**
*   "Người gác cổng" cho Microservices.
*   **Chức năng:** Authentication, Rate Limiting, Routing, Protocol Translation (REST -> gRPC).
*   **Tools:** Kong, AWS API Gateway.

---

## 3. Các giao thức hiện đại khác

### **WebSocket**
*   **Đặc điểm:** Kết nối 2 chiều (Full-duplex). Server có thể gửi tin cho Client bất cứ lúc nào.
*   **Use case:** Chat app, Game online, Chứng khoán realtime.

### **gRPC (Google Remote Procedure Call)**
*   **Đặc điểm:** Dùng Protobuf (Binary) thay vì JSON (Text) -> Nhẹ hơn, nhanh hơn 10x. Chạy trên HTTP/2.
*   **Use case:** Giao tiếp giữa các Microservices (Backend-to-Backend).

### **GraphQL**
*   **Đặc điểm:** Client chỉ lấy đúng dữ liệu mình cần (No Over-fetching).
*   **Use case:** Mobile App, Frontend phức tạp cần lấy dữ liệu từ nhiều nguồn.
