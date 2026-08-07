# Lab: Terraform App Stack trên Kubernetes Local

> [← DevOps & SRE](../README.md) | [IaC theory](../architecture/terraform-ansible-iac.md)

## Mục tiêu
Dùng Terraform (kubernetes / helm provider) để khai báo namespace, deployment, service, configmap — apply/destroy tái lập được.

## Scope tối thiểu
```
terraform/
  main.tf          # provider kubernetes
  variables.tf
  outputs.tf
  modules/app/     # deployment + service
```

## Acceptance
- [ ] `terraform plan` sạch trên cluster trống
- [ ] `terraform apply` tạo app reachable qua NodePort/port-forward
- [ ] Đổi `replicas` bằng variable → apply cập nhật đúng
- [ ] `terraform destroy` dọn sạch resource lab
- [ ] Không clickOps; mọi thứ qua code + README

## Extension
- Thêm Helm release Prometheus (optional)
- Remote state local backend file + note khi nào cần remote thật

> **Last Updated:** August 2026
