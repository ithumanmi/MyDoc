# Lab: Blue/Green Deploy + Instant Rollback

> [← DevOps & SRE](../README.md) | [Incident response](../reliability/incident-response.md)

## Mục tiêu
Deploy app 2 màu (blue/green) trên Minikube/kind, chuyển traffic bằng Service/Ingress, rollback < 60s khi bad release.

## Setup giả định
- Cluster local (Minikube)
- Image `demo-api:v1` (healthy) và `demo-api:v2` (mock 500 trên `/checkout`)
- Manifest: Deployment blue, Deployment green, Service `demo-api` selector đổi màu

## Steps
1. Deploy blue (`version=v1`), Service trỏ `color=blue`
2. Smoke: `curl /health` + `/checkout` → 200
3. Deploy green (`v2`) song song, **chưa** chuyển Service
4. Canary thủ công: port-forward green, verify fail
5. Nếu canary pass (lab: giả lập pass rồi fail): flip Service → green
6. Detect error rate tăng → flip Service về blue (rollback)

## Acceptance
- [ ] Hai Deployment cùng tồn tại trong ≥1 lần chuyển
- [ ] Rollback chỉ bằng đổi selector/label Service (không rebuild)
- [ ] Runbook 5 bước ghi trong README lab
- [ ] Đo thời gian rollback (target < 60s)

## Deliverable
- Thư mục `k8s/` + script `flip.sh` / `rollback.sh`
- Timeline giả lập SEV2 trong [runbook](../runbooks/checkout-api-sev1.md)

**Challenge:** [challenge-k8s-deploy-minikube](../../../challenges/devops-sre/challenge-k8s-deploy-minikube.md)

> **Last Updated:** August 2026
