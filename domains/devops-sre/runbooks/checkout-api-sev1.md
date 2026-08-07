# Runbook: Checkout API SEV1

> [← DevOps & SRE](../README.md) | [Incident basics](../reliability/incident-response.md)

## Symptom
Checkout error rate > 5% trong 5 phút hoặc p99 latency > 2s trên SLI checkout.

## Severity
**SEV1** nếu impact > 20% traffic toàn cục / một region chính.

## Immediate mitigates (first 15 min)
1. **Declare incident** — IC + comms channel
2. **Check dashboards:** error by version, pod restarts, dependency (payment/DB)
3. **Rollback** last deploy (blue/green flip hoặc `helm rollback`) nếu deploy < 60 phút
4. Nếu không phải deploy: enable feature flag degrade (skip non-critical upsell)
5. Scale pods nếu saturation CPU/mem rõ — không scale mù khi error = bug 500

## Triage tree
| Signal | Hướng |
| --- | --- |
| Errors chỉ trên version mới | Rollback |
| DB connection pool exhausted | Kill long queries / raise pool / rate-limit |
| Payment timeout | Circuit break + queue retry |
| Only 1 AZ/node | Reschedule / cordon bad node |

## Comms template
```
SEV1 Checkout — investigating
Impact: ~X% users failing pay
Mitigation: rolling back to vN-1
Next update: 15m
```

## After recover
- Blameless postmortem trong 48h
- Action item: add burn-rate alert + pre-prod checkout synthetic

**Practice lab:** [lab-blue-green-rollback](../labs/lab-blue-green-rollback.md)

> **Last Updated:** August 2026
