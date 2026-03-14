# Challenge: Deploy App lên K8s (minikube/kind)

- **Loại:** project
- **Mảng:** devops-sre
- **Mức:** Intermediate
- **Ước lượng thời gian:** 1-2 ngày
- **Prerequisites (tùy chọn):** K8s cơ bản; docker build; kubectl.

## Mục tiêu học tập
- Container hoá và deploy app lên K8s (minikube/kind).
- Viết Deployment, Service, Ingress; healthcheck/readiness.
- Kiểm tra triển khai (kubectl, port-forward, logs).

## Đề bài
Triển khai một web API đơn giản (có thể là hello API) lên **minikube** hoặc **kind**:
- Viết **Dockerfile**.
- Viết manifest: **Deployment**, **Service** (ClusterIP), **Ingress** (nếu dùng minikube ingress addon/kind ingress setup).
- Thêm **liveness** và **readiness** probes.

## Đầu vào (Input)
- Source app đơn giản (http server trả JSON).

## Đầu ra (Output)
- YAML manifests + Dockerfile.
- Hướng dẫn chạy: build image, load vào cluster (minikube/kind), apply manifests, kiểm tra.

## Tiêu chí chấm (Acceptance)
- **Deploy thành công:** Pod chạy, Service/Ingress truy cập được.
- **Healthcheck:** liveness/readiness chuẩn, pods không crash loop.
- **Tài liệu:** README hướng dẫn build/load/apply/test.

## Gợi ý / Hint
- Với minikube: `minikube image build` hoặc `docker-env` để build.
- Với kind: `kind load docker-image <image>`.
- Ingress: bật addon ingress (minikube) hoặc cài ingress-nginx cho kind.

## Reference solution (tùy chọn)
- (Tuỳ chọn) Đính kèm repo mẫu và lệnh kiểm tra.