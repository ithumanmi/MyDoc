---
title: "DevOps & Site Reliability Engineering Roadmap"
description: "K8s, IaC, CI/CD, and reliability practices for mid+ engineers"
updated: "2026-08-07"
canonical: true
tags: [devops, sre, roadmap]
audience: [beginner, intermediate, advanced]
related:
  - ../../challenges/devops-sre/README.md
  - ../README.md
sensitivity: public
---

# ♾️ DevOps & Site Reliability Engineering (SRE) Roadmap

> [← Domains hub](../README.md) | [Home](../../README.md) | [Challenges](../../challenges/devops-sre/README.md)
>
> **Domain maturity:** 🟡 Drafting · **Audience:** mid+ (đã quen backend/Linux)

Lập trình viên (Backend/Frontend/Data) chỉ tập trung viết ra Code. Nhóm kỹ sư Vận Hành (Ops) truyền thống thì cầm một con Server Linux rỗng và phải đọc Docs để gõ lệnh Deploy bằng tay mất 3 ngày.
**DevOps (Development & Operations)** ra đời để phá bỏ bức tường ngăn cách này. Thay vì gõ tay, mọi thao tác Cài đặt Mạng, Server, Load Balancer, Deploy đều được định nghĩa thành CODE và được **Tự Động Hóa (Automation)** hoàn toàn. 

> Đẳng cấp cao nhất của DevOps là **SRE (Site Reliability Engineering)** - Đảm bảo hệ thống FAANG đạt chuẩn Uptime 99.999% (5 Nines - Nhanh như chớp, Không bao giờ chết).

---

## 🌱 Foundations (mới bổ sung)

1. **[DevOps Principles](./fundamentals/devops-principles.md)**
2. **[SLI / SLO / Error Budgets](./fundamentals/sli-slo-error-budgets.md)**
3. **[Observability: Logs · Metrics · Traces](./observability/three-pillars.md)**
4. **[Incident Response](./reliability/incident-response.md)**
5. **[DevSecOps Basics](./security/devsecops-basics.md)**

---

## 🧭 Kiến Trúc & Cẩm Nang Lý Thuyết (Core Cloud Native)

Đã qua cái thời dùng File Transfer (FTP) ném code lên hosting. Thế giới Backend hiện tại xoay quanh Container (Docker) xếp chồng lên Vành Đai Điều Phối (Kubernetes).

1. **[Kiến Trúc Vua Điểu Phối: Kubernetes (K8s) & Helm Packages](./architecture/kubernetes-helm-internals.md)** (⭐ **Must Read**). Khám phá Master Nodes/Worker Nodes. Làm sao K8s có thể tự bắt mạch Pod chết và tự bơm Pod mới (Self-Healing)? Khái niệm Ingress, Service Load Balancer và gói Helm Chart. Tạm biệt Docker-Compose!
2. **[Hạ Tầng Như Là Code (Infrastructure As Code - IaC)](./architecture/terraform-ansible-iac.md)** (⭐ **Must Read**). Quản trị 10,000 con Server AWS EC2 ra sao? Tại sao Click chuột trên Web AWS Console (ClickOps) lại là điều Tối Kỵ Của Nhà Nghề? Triển khai định danh với Terraform (Declarative) và nhồi Cấu hình bằng Ansible (Imperative).

---

## 🧪 Xưởng Thực Hành Tự Động Hóa (DevOps & SRE Labs)

Lý thuyết K8s trên giấy không thể biến bạn thành Cloud Engineer Mức Lương \$4,000+. Hãy cầm bàn phím lên và biến những cấu hình YAML thành Cụm Server Bất Tử:

### ⚙️ Lab 1: Dòng Chảy Thần Tốc (Continuous Integration / Delivery)
*   **[Thiết Lập Mạch Máu CI/CD Pipeline Bằng GitHub Actions](./labs/lab-github-actions-cicd.md)**: Cách để Dev cứ ấn `git push origin main` là Hệ Thống tự động chạy Unit Test -> Đóng gói Container Image Ném Lên DockerHub Registry -> Bắn Cú Đâm (Webhook) Triển Phóng Thẳng Lên Mạng (Deploy to Prod) mà Con Người đang ngủ không buồn để ý. Không Lỗi - Liên Tục Dòng Chảy Code!

### 🌍 Lab 2: Nền Tảng Chỉ Huy Đám Mây Mắt Thần (Cluster Observability)
*   **[Lắp Đặt Quái Vật Kubernetes & Máy Đo Sóng Prometheus/Grafana](./labs/lab-k8s-observability.md)**: Cài Minikube chạy nguyên 1 Cụm Node K8s Nội Bộ. Đẩy App Chịu Lỗi Lên Master. Xây Dựng Râu Ăng-ten (Prometheus Node Exporter) Khám CPU/RAM và Đổ Vẽ Biểu Đồ Soi Tải Giao Thức Tuyệt Mĩ Của SRE Qua Grafana Dashboards Alert. Đạt Trình Giới Quản Lý Hầm Tàu Mạng!

### 🔁 Lab 3–4 & Runbook (E2E reliability)
*   **[Blue/Green Deploy + Instant Rollback](./labs/lab-blue-green-rollback.md)**
*   **[Terraform App Stack trên K8s local](./labs/lab-terraform-k8s-app.md)**
*   **[Runbook: Checkout API SEV1](./runbooks/checkout-api-sev1.md)**

---

> **Lưu ý Thang Bậc:** DevOps không dành cho Entry-Level. Nên có nền **Backend/System Design** trước. Challenges: [`challenges/devops-sre`](../../challenges/devops-sre/README.md). 
