## ☁️ Cloud-Specific Guides (Classic ML)

> [← Back to AI/ML Roadmap](../README.md)

Tùy nền tảng cloud (AWS, Azure, GCP) có dịch vụ hỗ trợ training, deployment và MLOps khác nhau. Dưới đây là cheat-sheet để chọn stack phù hợp.

---

## 1. AWS

| Use Case | Dịch vụ | Ghi chú |
| --- | --- | --- |
| Training/Notebook | **SageMaker Studio**, SageMaker Processing | Support spot training, built-in algorithms.
| Deployment | SageMaker Endpoints, Elastic Beanstalk, Lambda + API Gateway | Multi-model endpoints tối ưu chi phí.
| Data | S3, Glue, Athena | Glue Data Catalog + Lake Formation.
| Pipelines | Step Functions, SageMaker Pipelines | CI/CD ML native.
| Monitoring | CloudWatch, SageMaker Model Monitor | Drift detection tự động.

**Best practices:**
*   Sử dụng `ml.m5` hoặc `ml.c5` instance cho tabular ML.
*   Dùng SageMaker Clarify cho bias/fairness.
*   Autoscaling endpoint và bật data capture để audit.

---

## 2. Azure

| Use Case | Dịch vụ | Ghi chú |
| --- | --- | --- |
| Training | **Azure Machine Learning (AML) Compute**, Azure Databricks | Hỗ trợ AutoML, pipeline Designer.
| Deployment | Azure ML Managed Online Endpoint, AKS, Functions | Blue/green deployment built-in.
| Data | Azure Data Lake Storage, Synapse | Dataflow Gen2 kết nối AML dễ dàng.
| Monitoring | Application Insights, Azure Monitor | Log metrics, latency.

**Best practices:**
*   Dùng AML environments để quản lý dependencies.
*   Kết hợp với MLflow tracking native trong AML.
*   Đặt Policy đảm bảo resource tagging/cost.

---

## 3. Google Cloud (GCP)

| Use Case | Dịch vụ | Ghi chú |
| --- | --- | --- |
| Training | **Vertex AI Workbench**, Vertex AI Training, Dataproc | Tích hợp BigQuery ML.
| Deployment | Vertex AI Endpoints, Cloud Run, Cloud Functions | Auto-scaling và A/B testing.
| Data | BigQuery, Cloud Storage, Dataplex | BigQuery ML chạy trực tiếp SQL.
| Pipelines | Vertex AI Pipelines (Kubeflow), Cloud Composer | Managed metadata store.
| Monitoring | Vertex AI Model Monitoring, Cloud Logging | Drift detection + explainability.

**Best practices:**
*   Dùng Vertex AI Feature Store cho tabular.
*   Tranh thủ BigQuery ML để thử nghiệm nhanh mà không phải provisioning cluster.
*   Cloud Run phù hợp mô hình nhẹ (scikit-learn) với traffic bursty.

---

## 4. Multi-Cloud Tips

*   **Infrastructure as Code:** Terraform/ Pulumi để tái sử dụng giữa cloud.
*   **Containerization:** Docker + ONNX giúp portability.
*   **Monitoring stack chung:** Prometheus/Grafana + OpenTelemetry collector.
*   **Secrets & Credentials:** HashiCorp Vault hoặc cloud secret manager tương ứng.

> 🌐 Tip: Bắt đầu với cloud bạn đã có dữ liệu/infra sẵn. Dù dịch vụ khác nhau, workflow chung vẫn là: data lake → feature store → training → registry → deployment → monitoring.
