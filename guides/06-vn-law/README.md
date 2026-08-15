---
title: "VN Law Hub"
description: "Kho kiến thức + catalog văn bản quy phạm pháp luật Việt Nam"
updated: "2026-08-14"
canonical: true
tags: [vn-law, phap-luat, vbqppl, hub]
audience: [beginner, intermediate, advanced]
related:
  - vn-law-map.md
  - catalog.yaml
  - legal-hierarchy.md
  - ../02-wealth-business/legal/README.md
  - ../04-lifestyle-os/politics/vietnam/README.md
sensitivity: public
---

# Luật Việt Nam — Hub

> [← Guides](../README.md) | [Map](./vn-law-map.md) | [Catalog](./catalog.yaml) | [Thứ bậc VBQPPL](./legal-hierarchy.md) | [Nguồn](./sources.md)
>
> **Pattern:** giống Games OS / Health OS — hub + map + database; playbook thực hành **không copy**, chỉ pointer.

<!-- agent-summary -->
**Agent SUMMARY**
- Canonical kho **kiến thức Luật VN**: catalog văn bản (`catalog.yaml`) + ghi chú (`notes/`).
- Tra cứu văn bản → `catalog.yaml` (database) → note nếu có. Thứ bậc hiệu lực → `legal-hierarchy.md`.
- Thực hành đời sống/startup (HĐLĐ, thuế, NDA) → `guides/02-wealth-business/legal/`.
- Quy trình làm luật / tư pháp / bộ máy → `guides/04-lifestyle-os/politics/vietnam/`.
- Không phải tư vấn pháp lý. Số hiệu, hiệu lực, điều khoản phải đối chiếu Công báo / VBPL trước khi dùng.
<!-- /agent-summary -->

## ⚠️ Phạm vi

Tài liệu **giáo dục / tra cứu cá nhân**. Không thay luật sư, không thay văn bản gốc. Catalog là chỉ mục — không phải toàn văn luật.

## Start here

| Nhu cầu | Doc |
| --- | --- |
| Bản đồ ngành luật | [vn-law-map.md](./vn-law-map.md) |
| Database văn bản | [catalog.yaml](./catalog.yaml) · schema [SCHEMA.md](./SCHEMA.md) |
| Hiến pháp → Luật → NĐ → TT | [legal-hierarchy.md](./legal-hierarchy.md) |
| Ghi chú đã có | [notes/](./notes/README.md) |
| Thêm một luật vào kho | [SCHEMA.md](./SCHEMA.md#them-mot-van-ban) + template [`templates/vn-law/law-note.md`](../../templates/vn-law/law-note.md) |
| Nguồn chính thức | [sources.md](./sources.md) |

## Ranh giới

| Ở đây (`06-vn-law`) | Không ở đây |
| --- | --- |
| Catalog VBQPPL, ghi chú điều/khoản, ngành luật | Hợp đồng mẫu, NDA, “làm sao khỏi bị ăn hiếp” → [`guides/02-wealth-business/legal/`](../02-wealth-business/legal/README.md) |
| Thứ bậc hiệu lực, cách đọc một đạo luật | Quy trình Quốc hội, Đảng, tư pháp → [`politics/vietnam/`](../04-lifestyle-os/politics/vietnam/README.md) |
| Index để agent/RAG tra số hiệu | Toàn văn luật (bản quyền + dễ lỗi thời) — link nguồn gốc |

## Thêm kiến thức

1. Thêm / sửa hàng trong [`catalog.yaml`](./catalog.yaml) theo [`SCHEMA.md`](./SCHEMA.md).
2. (Tuỳ chọn) Tạo `notes/<id>.md` từ template, gắn `note:` trong catalog.
3. Chạy `python scripts/check_vn_law_catalog.py`.
4. Nếu topic trở thành **canonical** cho agent → thêm hàng `meta/routing.md` + `meta/catalog/topics.yaml`.
