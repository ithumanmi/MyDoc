# 🧪 DevOps/SRE Lab Pack (30-45 ngày)

> Hoàn thiện 4 nhóm lab này để chuyển từ “biết DevOps” sang “làm được DevOps”. Mỗi lab có **Objective → Steps → Deliverables → Verification**. Chọn stack quen thuộc (Node.js, C#, Go) và ghi log sau mỗi buổi.

## 1. Container & Kubernetes Track (Tuần 1)

### 🎯 Objective
Đóng gói app backend + database vào Docker, sau đó triển khai lên Kubernetes (local hoặc managed).

### 🧭 Steps
1. **Docker hóa** ứng dụng (multi-stage build, healthcheck).  
2. **Docker Compose**: app + PostgreSQL/Redis + admin UI.  
3. **K8s manifests**: Deployment, Service, ConfigMap/Secret.  
4. Bonus: Helm chart hoặc Kustomize overlay (prod vs staging).

### 📦 Deliverables
- Repo có `Dockerfile`, `docker-compose.yml`, `k8s/` (deployment/service/ingress).  
- Screenshot `kubectl get pods` với ≥3 replicas, health 100%.

### ✅ Verification
- `docker scout` hoặc `trivy` báo 0 critical vulnerabilities.  
- Check `kubectl describe` không còn CrashLoopBackOff.  
- App accessible qua `http://localhost` hoặc ingress domain mô phỏng.

### 🔗 Resources
- [docker-k8s-guide.md](./docker-k8s-guide.md)  
- [templates/dockerfile-nodejs.md](../templates/dockerfile-nodejs.md)  
- Minikube / kind / k3d hướng dẫn nhanh (tạo cluster local).

---

## 2. CI/CD Automation Track (Tuần 2)

### 🎯 Objective
Thiết lập pipeline tự động lint → test → build → publish image → deploy staging.

### 🧭 Steps
1. GitHub Actions/GitLab CI pipeline với matrix test (Node/C#).  
2. Build Docker image và push lên registry (GHCR, Docker Hub).  
3. Deploy staging: dùng SSH, Docker Compose, hoặc ArgoCD/FluxCD nếu dùng K8s.  
4. Thêm secret rotation & environment promotion (dev → staging → prod manual approval).

### 📦 Deliverables
- File workflow `.github/workflows/ci-cd.yml` (hoặc `.gitlab-ci.yml`).  
- Badge build status + release notes tự động (changelog).  
- Script rollback (VD: `kubectl rollout undo` hoặc `docker compose rollback`).

### ✅ Verification
- Pipeline chạy <10 phút, fail nếu test fail.  
- Docker image có tag `git-sha` và `latest`.  
- Release staging thành công với thông báo Slack/Email.

### 🔗 Resources
- [sre-practices.md](./sre-practices.md#1-cicd-pipelines)  
- Template GitHub Actions (Official marketplace).  
- Tool: Renovate/Dependabot để auto update dependencies.

---

## 3. Observability & Reliability Track (Tuần 3)

### 🎯 Objective
Thiết lập metrics + logs + traces + alert cho ứng dụng đã container hóa.

### 🧭 Steps
1. Metrics: Prometheus + Grafana (Docker Compose hoặc Helm).  
2. Logs: ELK stack hoặc Loki + Promtail.  
3. Tracing: OpenTelemetry SDK (in app) + Jaeger/Tempo.  
4. Đặt SLO: P95 latency <300ms, error rate <1%. Tạo alert rule (CPU >80% 5 phút, error budget burn >2%).

### 📦 Deliverables
- Dashboard Grafana (import JSON) + ảnh chụp.  
- Alert rule file (Prometheus alertmanager / Grafana alert).  
- Doc ngắn mô tả luồng trace (diagram).  
- Postman/Newman collection log ra trace id.

### ✅ Verification
- Trigger synthetic load (k6) → metric + log + trace đều hiển thị.  
- Alert gửi tới Slack/Email khi vượt ngưỡng.  
- Postmortem mini cho 1 sự cố giả lập (VD: DB timeout 5 phút).

### 🔗 Resources
- [sre-practices.md](./sre-practices.md#4-observability-o11y)  
- OpenTelemetry docs (Node.js, .NET, Go).  
- Grafana Cloud Free tier nếu không muốn tự host.

---

## 4. Incident, Cost & Governance Track (Tuần 4)

### 🎯 Objective
Rèn kỹ năng on-call, tối ưu chi phí, và quy trình chuẩn cho production.

### 🧭 Steps
1. **Incident Simulation:** Dùng `toxiproxy` hoặc `tc` để thêm latency/packet loss, log lại timeline phản ứng.  
2. **Runbook:** Viết checklist xử lý sự cố (API 5xx spike, DB connection pool exhausted).  
3. **Cost Guardrails:** Dùng AWS Budgets/Azure Cost Alerts hoặc Prometheus `container_cpu_usage_seconds_total` để ước lượng chi phí, thêm tag bắt buộc.  
4. **Security/Compliance:** Check Terraform security với `tfsec`, quét secrets (gitleaks), review IAM policy least privilege.

### 📦 Deliverables
- Incident report (MTTA/MTTR, nguyên nhân, action items).  
- Runbook template (Markdown) + flowchart.  
- Cost sheet (Google Sheet / Notion) ghi baseline + alert thresholds.  
- Checklist security trước release (mã hóa, secrets, audit log).

### ✅ Verification
- On-call drill <15 phút phát hiện sự cố (alert → acknowledge).  
- Budget alert gửi thông báo khi cost vượt 80% hạn mức.  
- Secrets scanning không phát hiện rò rỉ mới.

### 🔗 Resources
- AWS Budgets, Azure Cost Management, GCP Billing alerts.  
- Tools: `gitleaks`, `tfsec`, `Checkov`, `kubescape`.  
- Postmortem template tại `templates/project-post-mortem.md`.

---

## Hướng dẫn triển khai
1. **Timebox**: Mỗi track 1 tuần (5 buổi làm việc x 2h).  
2. **Pairing**: Rủ 1 backend/devops khác làm chung để mutual review.  
3. **Artifacts**: Lưu kết quả trong repo `devops-lab-pack/<track>/<lab>/README.md`.  
4. **Review**: Mỗi cuối tuần, viết recap 1 trang (wins, blockers, metric cải thiện).  
5. **Next steps**: Sau khi xong 4 track, chọn 1 hệ thống thật (pet project hoặc service nội bộ) áp dụng trọn bộ quy trình này.

> Khi cần hỗ trợ, mở issue trong repo để team đóng góp thêm script, template hoặc tài liệu tham khảo.

---

## 🔥 Bonus: Advanced Lab Cluster (Tuần 5-6)

> Dành cho team đã hoàn thành 4 track cơ bản và muốn chuẩn bị cho tình huống production phức tạp (đa cloud, traffic đột biến, yêu cầu bảo mật cao). Chọn ít nhất 2 lab dưới đây để thực hiện trong 2 tuần.

### 5A. Chaos & Resilience Engineering
- **Objective:** Đo độ bền hệ thống khi một phần hạ tầng gặp sự cố.
- **Steps:**  
  1. Dùng **LitmusChaos** hoặc **Gremlin** inject lỗi (kill pod, tăng latency DB).  
  2. Thiết lập **Steady State Hypothesis** (VD: P95 < 300ms, error rate < 1%).  
  3. Chạy chaos experiment, đo metric trước/sau, đưa ra remediation plan.
- **Deliverables:** Chaos manifest, dashboard metric, postmortem (có action items).  
- **Verification:** Runbook được cập nhật với threshold mới, alert không còn noise khi chaos chạy ngoài giờ.

### 5B. Multi-Cloud & Service Mesh Lab
- **Objective:** Deploy một workload trên 2 cloud khác nhau hoặc 2 cluster K8s, dùng Service Mesh để quan sát và điều phối traffic.
- **Steps:**  
  1. Tạo 2 cluster (EKS + GKE hoặc kind + k3d).  
  2. Cài **Istio/Linkerd** hoặc Cilium Service Mesh.  
  3. Thiết lập traffic shifting (80/20), mutual TLS, circuit breaker.  
  4. Tích hợp observability mesh (Kiali, Jaeger).
- **Deliverables:** Diagram multi-cluster, manifest mesh, video demo traffic shift.  
- **Verification:** Fail cluster A → traffic tự động chuyển sang B, metric + trace vẫn đầy đủ.

### 5C. Security Hardening as Code
- **Objective:** Chuẩn hóa bảo mật bằng automation trước khi release features mới.
- **Steps:**  
  1. Viết policy IaC (OPA, Conftest, Kyverno) để enforce rule (VD: không chạy container privilege, phải có resource limit).  
  2. Tích hợp `tfsec`/`Checkov`/`kubescape` vào CI pipeline.  
  3. Tạo secret zero-trust flow (Vault + dynamic secrets hoặc AWS IAM roles).  
  4. Review compliance checklist (GDPR/PDPA, PCI) và tạo automation check.
- **Deliverables:** Policy repo, pipeline screenshot, security report, checklist mapping controls → evidence.  
- **Verification:** Pipeline block nếu vi phạm policy, secrets rotation được log lại, audit trail đầy đủ.

### 5D. Traffic Surge & Cost Game Day
- **Objective:** Mô phỏng chiến dịch marketing lớn, tối ưu vừa hiệu năng vừa chi phí.
- **Steps:**  
  1. Dùng k6 hoặc Locust bắn traffic gấp 10 lần bình thường.  
  2. Auto scale horizontal + vertical, monitor cost bằng CloudWatch/Prometheus.  
  3. Áp dụng Spot instances / Savings plan / autoscale down-time để giữ chi phí < X$/ngày.  
  4. Viết recap: Trade-off hiệu năng vs chi phí, đề xuất tối ưu lâu dài.
- **Deliverables:** Benchmark report (TPS, latency, cost), autoscale policy, cost dashboard screenshot.  
- **Verification:** Traffic peak không làm error >2%, chi phí tăng <40% so với baseline.

### Gợi ý triển khai Advanced Lab
1. **Chia đội**: Mỗi lab phụ trách bởi 2 người (1 backend, 1 SRE) → pair review lẫn nhau.  
2. **Timeline**: 2 tuần, mỗi lab 3-4 buổi. Buổi cuối demo cho toàn team.  
3. **Success Criteria**: Có thể trình bày trong buổi postmortem hoặc brown bag talk, commit artifacts vào repo nội bộ.  
4. **Retrospective**: Sau mỗi lab, ghi lại 3 bài học lớn & 1 đề xuất cải tiến quy trình DevOps hiện tại.