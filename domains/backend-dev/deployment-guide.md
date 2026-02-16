# 🚢 Deployment & DevOps: The Art of Shipping Code

> [← Back to Backend Roadmap](./README.md) | [Home](../../README.md)

Code xong chưa phải là xong. Code phải chạy ổn định trên Production mới là xong. DevOps không chỉ là việc của SysAdmin, mà là mindset của mọi Modern Developer. "You build it, you run it."

---

## 📋 Mục lục

1. [Docker & Containerization](#1-docker--containerization-gói-gém-ứng-dụng)
2. [CI/CD Pipelines](#2-cicd-pipelines-tự-động-hóa-quy-trình)
3. [Deployment Strategies](#3-deployment-strategies-chiến-lược-triển-khai)
4. [Kubernetes (K8s) Basics](#4-kubernetes-k8s-basics-điều-phối-container)
5. [Infrastructure as Code (IaC)](#5-infrastructure-as-code-iac-hạ-tầng-là-code)
6. [Action Plan](#6-action-plan-con-đường-devops)

---

## 1. Docker & Containerization: Gói gém ứng dụng

### 1.1. Tại sao cần Docker?

"It works on my machine" ¯\\_(ツ)_/¯.
Docker đóng gói code + dependencies + OS config vào 1 Container. Chạy giống hệt nhau trên Laptop, Server, và Cloud.

### 1.2. Dockerfile Best Practices

*   **Multi-stage Builds:** Giảm size image từ 1GB xuống 50MB.
    ```dockerfile
    # Stage 1: Build
    FROM node:18 AS builder
    WORKDIR /app
    COPY . .
    RUN npm ci && npm run build

    # Stage 2: Run (Chỉ lấy kết quả build)
    FROM node:18-alpine
    WORKDIR /app
    COPY --from=builder /app/dist ./dist
    COPY --from=builder /app/package*.json ./
    RUN npm ci --production
    CMD ["node", "dist/main.js"]
    ```
*   **.dockerignore:** Đừng copy `node_modules` hay `.git` vào image!
*   **User:** Đừng chạy container bằng `root`. Tạo user `node` hoặc `app`.

---

## 2. CI/CD Pipelines: Tự động hóa quy trình

*   **CI (Continuous Integration):** Push code → Run Test → Build Docker Image.
*   **CD (Continuous Delivery/Deployment):** Deploy Image lên Server.

### 2.1. GitHub Actions Example

```yaml
name: CI/CD Pipeline
on: [push]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - run: npm ci
      - run: npm test

  deploy:
    needs: test
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    steps:
      - run: docker build -t myapp .
      - run: docker push myregistry/myapp
      # Trigger webhook deploy on server
```

---

## 3. Deployment Strategies: Chiến lược triển khai

Làm sao update code mới mà user không bị disconnect?

### 3.1. Rolling Update (Mặc định của K8s)

Server có 3 instances (v1).
1.  Tắt 1 instance v1, bật 1 instance v2.
2.  Chờ v2 healthy.
3.  Lặp lại cho đến khi hết v1.
*   **Ưu điểm:** Zero downtime.
*   **Nhược điểm:** Tồn tại song song v1 và v2 (Phải backward compatible).

### 3.2. Blue-Green Deployment

*   **Blue (Production):** Chạy v1 (Live traffic).
*   **Green (Staging):** Deploy v2. Test kỹ.
*   **Switch:** Đổi Router trỏ traffic sang Green.
*   **Ưu điểm:** Rollback tức thì (Switch lại Blue).
*   **Nhược điểm:** Tốn gấp đôi resources.

### 3.3. Canary Deployment

*   Deploy v2 cho 1% user (hoặc user nội bộ).
*   Monitor lỗi.
*   Tăng dần lên 10% → 50% → 100%.

---

## 4. Kubernetes (K8s) Basics: Điều phối container

Khi bạn có 100 containers, bạn không thể quản lý bằng tay (`docker run`). K8s giúp:
*   **Self-healing:** Container chết → Tự khởi động lại.
*   **Auto-scaling:** CPU cao → Thêm Pods.
*   **Load Balancing:** Chia traffic đều.

**Key Concepts:**
*   **Pod:** Đơn vị nhỏ nhất (thường chứa 1 container).
*   **Deployment:** Quản lý version, update pods.
*   **Service:** Load balancer nội bộ, giúp các pods nói chuyện với nhau.
*   **Ingress:** Cửa ngõ đón traffic từ Internet.

---

## 5. Infrastructure as Code (IaC): Hạ tầng là Code

Đừng click chuột trên AWS Console! Hãy viết code để tạo Server.

### 5.1. Terraform

```hcl
resource "aws_instance" "app_server" {
  ami           = "ami-12345678"
  instance_type = "t2.micro"
}
```
*   `terraform apply` → Tạo server.
*   `terraform destroy` → Xóa server.

---

## 6. Action Plan: Con đường DevOps

1.  **Level 1 (Docker):** Viết Dockerfile cho dự án cá nhân. Chạy `docker-compose up` (App + DB).
2.  **Level 2 (CI/CD):** Setup GitHub Actions. Mỗi lần push code tự động chạy test.
3.  **Level 3 (Cloud):** Thuê VPS (DigitalOcean/AWS Lightsail). Setup Docker Swarm hoặc K3s (K8s nhẹ) để deploy.

> **Tư duy:** "Automate everything." Nếu bạn phải làm gì đó thủ công 2 lần, hãy viết script cho lần thứ 3.
