# Tech Day 67: Tech Interview Question (MLOps) – Triển khai model thành service

**Câu hỏi:** “Suppose you trained a machine learning model in a notebook. How would you turn that model into a production service that a web application can call?”

## 1) Ý chính cần nhấn mạnh
- ML deployment là **một hệ thống**: preprocessing + model artifact + API service + infrastructure + monitoring.
- Tính **tái lập** (reproducibility): cùng pipeline tiền xử lý, cùng version model & dependency.
- Tính **vận hành**: container, CI/CD, quan sát (latency, errors, drift), kế hoạch retrain/redeploy.

## 2) Flow trả lời gợi ý
1) **Đóng gói artifact & preprocessing**
   - Serialize model + preprocessing pipeline (`.pkl/.joblib` hoặc model registry như MLflow). 
   - Lưu kèm metadata: version, schema input, metrics, hash checksum.
2) **Xây dựng prediction service**
   - Dùng **FastAPI**/Flask → endpoint `/predict`.
   - Luồng: nhận request → validate schema → preprocess features → load model (tốt nhất load sẵn, cache) → inference → trả kết quả + confidence/metadata.
3) **Container hóa**
   - Viết `Dockerfile` pin version Python/lib; include model artifact. 
   - Chạy healthcheck endpoint (`/health`), log theo JSON.
4) **Triển khai hạ tầng**
   - Deploy lên **Kubernetes/ECS/EC2**; autoscale theo CPU/QPS; config resource (CPU/RAM) phù hợp model.
   - API Gateway/LB phía trước; HTTPS; auth (token/API key).
5) **Monitoring & Observability**
   - Metrics: latency, throughput, error rate; model metrics online (conversion/CTR nếu applicable).
   - Logs + traces; dashboard + alerting. 
   - Data monitoring: distribution shift, schema drift.
6) **Retraining & Redeploy**
   - Trigger retrain khi drift hoặc định kỳ; CI/CD cho model (bump version, canary/blue-green deploy).
   - Rollback nhanh nếu metric xấu; kiểm thử hồi quy (golden set).

## 3) Bullet trả lời ngắn gọn (template 30-60s)
- “Tôi serialize model + pipeline preprocessing để đảm bảo dữ liệu prod xử lý giống train. 
- Đóng gói vào FastAPI `/predict` với schema validation, load model sẵn, chạy inference và trả prediction. 
- Container hóa bằng Docker, pin dependency, healthcheck. 
- Deploy lên K8s/ECS sau API Gateway, bật HTTPS và auth. 
- Giám sát latency/error + data drift; khi drift/metrics xấu thì trigger retrain, triển khai model mới qua canary/blue-green.”

## 4) Đi sâu nếu bị hỏi thêm
- **Tải trọng cao**: autoscaling, model server chuyên dụng (vLLM/TensorRT-Serving), batch inference.
- **Feature parity**: dùng cùng feature store hoặc shared preprocessing library.
- **Versioning**: model registry + model signature; lưu lại training data hash.
- **Canary**: route 5-10% traffic để kiểm chứng online; A/B với metrics thực tế.
- **Security**: rate limit, authN/Z, secret management, PII masking/log redaction.
- **Cost**: chọn instance GPU/CPU theo mô hình; bật auto-shutdown/scale-to-zero với serverless.

## 5) Đoạn kết thúc nhấn mạnh (1 câu)
- “Điều quan trọng là biến notebook thành một pipeline reproducible, có API rõ ràng, chạy trong container trên hạ tầng có giám sát, và có vòng lặp retrain/redeploy khi dữ liệu thay đổi.”