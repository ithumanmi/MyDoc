# React Performance Essentials

> [← Frontend](./README.md) | [Web Dev](../README.md)

## CWV gắn frontend
| Metric | Việc hay gặp |
| --- | --- |
| LCP | Image hero, font, waterfall JS |
| INP | Heavy handlers, sync render |
| CLS | Ảnh không dimension, ads/banner |

## Patterns
1. Code-split route-level (`React.lazy` / Next dynamic)
2. Memo đúng chỗ — đo trước khi `useMemo` mọi thứ
3. Virtualize list dài
4. Cache server/client data (React Query) tránh refetch storm
5. Images: size + modern format + priority LCP

## Exercise
Profil một list 1k rows: trước/sau virtualization; ghi lại interaction latency.

**Practice:** [challenges/web-ui](../../../challenges/web-ui/README.md) (SPA performance / a11y)

> **Last Updated:** August 2026
