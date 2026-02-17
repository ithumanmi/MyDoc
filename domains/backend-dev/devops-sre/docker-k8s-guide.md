# 🐳 DevOps Mastery: Docker & Kubernetes (K8s)

> [← Back to Backend Roadmap](../README.md)

Bạn đã viết xong code Backend xịn xò. Nhưng làm sao để nó chạy ổn định trên mọi máy chủ, từ laptop của bạn đến Cloud AWS?
Đó là nhiệm vụ của **DevOps (Development + Operations)**.

---

## 1. Containerization với Docker 📦

### Tại sao cần Docker?
Vấn đề kinh điển: *"Code chạy ngon trên máy em, nhưng lên server lại lỗi!"* (Works on my machine problem).
Docker đóng gói code + thư viện + môi trường (OS) vào một **Container**. Chạy ở đâu cũng giống nhau.

### Core Concepts:
*   **Dockerfile:** Bản thiết kế (Blueprint) để xây nhà.
*   **Image:** Ngôi nhà đã xây xong (tĩnh).
*   **Container:** Ngôi nhà đang có người ở (đang chạy).

### Hướng dẫn viết Dockerfile (Node.js):
```dockerfile
# 1. Chọn Base Image (Hệ điều hành nhỏ gọn)
FROM node:18-alpine

# 2. Tạo thư mục làm việc
WORKDIR /app

# 3. Copy file package.json trước (Tận dụng Cache)
COPY package*.json ./

# 4. Cài đặt thư viện
RUN npm install --production

# 5. Copy toàn bộ code vào
COPY . .

# 6. Mở cổng 3000
EXPOSE 3000

# 7. Chạy ứng dụng
CMD ["node", "server.js"]
```

### Lệnh Docker cơ bản:
*   Build image: `docker build -t my-app .`
*   Chạy container: `docker run -p 3000:3000 my-app`
*   Xem container đang chạy: `docker ps`
*   Dừng container: `docker stop <container_id>`

---

## 2. Orchestration với Kubernetes (K8s) ☸️

Khi bạn có 1 container -> Dùng Docker.
Khi bạn có **100 containers** (Microservices) -> Dùng **Kubernetes**.
K8s giống như một "nhạc trưởng" điều khiển dàn nhạc containers: Tự động scale, tự động sửa lỗi (self-healing), cân bằng tải.

### Core Concepts (K8s Objects):
1.  **Pod:** Đơn vị nhỏ nhất. Chứa 1 hoặc nhiều containers (thường là 1). Pod chết là mất luôn, không hồi sinh.
2.  **Deployment:** Quản lý Pods. Đảm bảo luôn có X bản sao (Replicas) đang chạy. Nếu 1 Pod chết, Deployment tạo cái mới bù vào.
3.  **Service:** Cổng giao tiếp. Giúp các Pods tìm thấy nhau và public ra ngoài internet (Load Balancing).
4.  **Ingress:** Router thông minh. Điều hướng traffic dựa trên domain (VD: `api.example.com` -> Service A, `web.example.com` -> Service B).

### File cấu hình K8s (`deployment.yaml`):
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-app-deployment
spec:
  replicas: 3 # Luôn chạy 3 bản sao
  selector:
    matchLabels:
      app: my-app
  template:
    metadata:
      labels:
        app: my-app
    spec:
      containers:
      - name: my-app
        image: my-app:latest
        ports:
        - containerPort: 3000
```

---

## 3. CI/CD Pipeline (Tự động hóa) 🚀

**CI (Continuous Integration):** Tự động test và build code mỗi khi push lên Git.
**CD (Continuous Deployment):** Tự động deploy code mới lên server.

### Quy trình chuẩn (GitHub Actions):
1.  **Developer push code** lên nhánh `main`.
2.  **GitHub Action** kích hoạt:
    *   Chạy Unit Tests (Jest).
    *   Nếu Test pass -> Build Docker Image.
    *   Push Image lên Docker Hub.
3.  **Deploy:**
    *   SSH vào server -> Pull image mới về -> Restart container.
    *   Hoặc báo cho K8s cập nhật Deployment.

---

## 4. Thực Hành (Hands-on) 🛠️

### Bài tập 1: Dockerize ứng dụng
1.  Viết 1 server Node.js đơn giản (`Hello World`).
2.  Tạo `Dockerfile`.
3.  Build và chạy container. Truy cập `localhost:3000`.

### Bài tập 2: Docker Compose (App + Database)
Chạy ứng dụng Node.js kết nối với MongoDB mà không cần cài Mongo trên máy thật.
Tạo file `docker-compose.yml`:
```yaml
version: '3'
services:
  app:
    build: .
    ports:
      - "3000:3000"
    depends_on:
      - mongo
  mongo:
    image: mongo
    ports:
      - "27017:27017"
```
Lệnh chạy: `docker-compose up`

👉 **[Tải mẫu Dockerfile tối ưu (Multi-stage build)](../templates/dockerfile-nodejs.md)**
