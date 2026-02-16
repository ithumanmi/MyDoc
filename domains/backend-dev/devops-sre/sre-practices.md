# ♾️ DevOps & SRE Practices

> [← Back to Backend Development](../README.md)

Modern backend engineering includes infrastructure, deployment, and reliability. "You build it, you run it."

## 1. CI/CD Pipelines
Automating the path from code commit to production.

### **Continuous Integration (CI)**
*   **Goal:** Validate code changes frequently.
*   **Steps:**
    1.  Linting (Check syntax/style).
    2.  Unit Tests (Fast).
    3.  Integration Tests (Slow, with DB/Redis mocks).
    4.  Build Artifact (Docker Image / JAR).
    5.  Scan for Vulnerabilities (Snyk/Trivy).

### **Continuous Deployment (CD)**
*   **Goal:** Deploy artifact to environments automatically.
*   **Strategies:**
    *   **Rolling Update:** Update 1 instance at a time. Zero downtime. (Kubernetes default).
    *   **Blue-Green:** Deploy new version (Green) alongside old (Blue). Switch traffic instantly. Easy rollback.
    *   **Canary:** Deploy to 1% of users. Monitor errors. Gradually increase to 100%.

---

## 2. Infrastructure as Code (IaC)
Managing servers like software.

### **Terraform (HashiCorp)**
*   **Declarative:** You say *what* you want ("I need an EC2 instance"), not *how* to do it.
*   **State:** Terraform keeps track of current infrastructure state.
*   **Provider Agnostic:** Supports AWS, Azure, GCP, Cloudflare using same syntax (HCL).

### **Ansible**
*   **Configuration Management:** Installing software, updating configs *inside* the servers.
*   **Agentless:** Uses SSH.

---

## 3. Kubernetes (K8s) Core Concepts
The operating system for the cloud.

*   **Pod:** Smallest unit. One or more containers sharing network/storage.
*   **Deployment:** Manages Pods (Scaling, Updates, Rollbacks).
*   **Service:** Stable network endpoint (Load Balancer) for a set of Pods.
*   **Ingress:** HTTP routing (Reverse Proxy) from outside world to Services.
*   **ConfigMap / Secret:** Injecting configuration/passwords into Pods.

---

## 4. Observability (O11y)
"Monitoring tells you the system is down. Observability tells you *why*."

### **The Three Pillars**
1.  **Metrics (Aggregatable Data):** "CPU usage is 80%", "Error rate is 5%".
    *   *Tools:* Prometheus, Grafana, Datadog.
2.  **Logs (Events):** "User X failed login at 10:00". Text-based.
    *   *Tools:* ELK Stack (Elasticsearch, Logstash, Kibana), Loki.
3.  **Traces (Request Context):** "Request A took 500ms (100ms in Service A, 400ms in DB)".
    *   *Tools:* Jaeger, Zipkin, OpenTelemetry.

### **Incident Management**
*   **SLO (Service Level Objective):** "99.9% requests succeed". The target.
*   **SLA (Service Level Agreement):** The contract (penalty if missed).
*   **Error Budget:** "We can fail 0.1% of requests". If budget exhausted -> Freeze features, fix stability.
*   **Post-Mortem:** Blameless analysis of outages. "What went wrong?" not "Who did it?".
