# Feature Store Basics

> [← Data Science](../README.md) | [AI/ML domain](../../ai-ml/README.md)

## Vì sao cần
Train/serve skew: feature lúc train khác lúc inference → model “tốt” offline, kém online.

## Hai giao diện
| Store | Latency | Use |
| --- | --- | --- |
| Offline | batch/hours | Training sets |
| Online | ms | Realtime inference |

## Nguyên tắc
- Cùng transformation code path cho train & serve
- Point-in-time correct joins (no leakage)
- Ownership + monitoring drift trên feature

Deep MLOps: [`domains/ai-ml/`](../../ai-ml/README.md) (mlops / production docs).

> **Last Updated:** August 2026
