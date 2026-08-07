# Data Roles & Pipeline Mindset

> [← Data Science](../README.md) | [Domains hub](../../README.md)

## Ai làm gì
Giữ bảng trong README chính; rule thực dụng:
- **Engineer** ưu tiên reliability + schema evolution
- **Scientist** ưu tiên valid inference + experiment design
- **ML Eng** ưu tiên serving + monitoring drift

## Pipeline tối thiểu
```
Source → Ingest → Validate → Transform → Serve (warehouse/feature/API) → Observe
```

## Contract giữa team
- Schema owner là ai?
- SLA freshness?
- Breaking change đi qua PR + version?

**Next:** [Dimensional modeling primer](./dimensional-modeling-primer.md)

> **Last Updated:** August 2026
