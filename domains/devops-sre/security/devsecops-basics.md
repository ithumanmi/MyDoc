# DevSecOps Basics

> [← DevOps & SRE](../README.md)

## Shift-left checklist
| Gate | Tooling ý tưởng | Block merge? |
| --- | --- | --- |
| SAST / lint security | Semgrep, CodeQL | High findings |
| Dependency CVE | Dependabot / Trivy fs | Critical/High fixable |
| Container scan | Trivy / Grype | Critical base CVEs |
| IaC policy | OPA/Conftest, tfsec | Public SG / * IAM |
| Secrets | gitleaks | Always |

## Runtime
- Least privilege IAM / IRSA
- NetworkPolicy mặc định deny
- Image signing + admission (optional advanced)

## Liên hệ security domain
Deep-dive offense/defense: [`domains/network-security/`](../../network-security/README.md)

> **Last Updated:** August 2026
