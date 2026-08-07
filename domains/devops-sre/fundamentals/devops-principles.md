# DevOps Principles

> [← DevOps & SRE](../README.md) | [Domains hub](../../README.md)
>
> **Domain maturity:** đang nâng từ 🟠 Stub → 🟡 Drafting

## Ba ý chính
1. **You build it, you run it** — team sở hữu deploy + pager, không ném sang “Ops bên kia tường”.
2. **Everything as code** — infra, pipeline, policy, dashboard-as-code khi được.
3. **Feedback loops nhanh** — commit → signal production trong phút, không ngày.

## Anti-patterns
| Anti-pattern | Thay bằng |
| --- | --- |
| ClickOps trên cloud console | Terraform/Pulumi + PR review |
| “Hero deploy” cuối tuần | Progressive delivery + rollback 1 click |
| Metric vanity (CPU average) | SLI gắn user journey |
| Secrets trong repo | Vault/SM + short-lived creds |

## Learning order trong domain này
1. Doc này + [SLI/SLO](./sli-slo-error-budgets.md)
2. [K8s & Helm](../architecture/kubernetes-helm-internals.md) + [IaC](../architecture/terraform-ansible-iac.md)
3. Labs CI/CD & observability
4. [Incident response](../reliability/incident-response.md)

> **Last Updated:** August 2026
