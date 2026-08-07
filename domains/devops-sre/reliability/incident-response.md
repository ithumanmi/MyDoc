# Incident Response Basics

> [← DevOps & SRE](../README.md)

## Vòng đời sự cố
```
Detect → Triage → Mitigate → Recover → Review (postmortem)
```

## Roles tối thiểu
- **Incident commander:** quyết định ưu tiên, không nhất thiết người sửa code
- **Comms:** cập nhật stakeholder / status page
- **Ops/ Eng on-call:** mitigate

## Severity (mẫu)
| Sev | Ví dụ | Response |
| --- | --- | --- |
| SEV1 | Checkout down toàn cục | War room ngay |
| SEV2 | Một region chậm | On-call + escalate 30m |
| SEV3 | Tool nội bộ lỗi | Ticket giờ hành chính |

## Postmortem blameless
- Timeline sự kiện (UTC)
- Impact (users, $$, SLO burn)
- Root cause + contributing factors
- Action items có owner + due date

**Challenge:** mở rộng từ [K8s deploy challenge](../../../challenges/devops-sre/challenge-k8s-deploy-minikube.md) bằng bảng runbook rollback.

> **Last Updated:** August 2026
