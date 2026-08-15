---
title: "VN Law catalog schema"
description: "Schema catalog.yaml — database văn bản quy phạm pháp luật"
updated: "2026-08-14"
canonical: true
tags: [vn-law, schema, catalog]
audience: [intermediate]
related:
  - catalog.yaml
  - README.md
  - ../../templates/vn-law/law-note.md
sensitivity: public
---

# Schema catalog Luật VN

> Database: [`catalog.yaml`](./catalog.yaml) · Validate: `python scripts/check_vn_law_catalog.py`

## Trường bắt buộc (`instruments[]`)

| Field | Ý nghĩa |
| --- | --- |
| `id` | kebab-case unique (`bl-lao-dong-2019`) |
| `type` | `hien-phap` \| `bo-luat` \| `luat` \| `nghi-quyet-qh` \| `phap-lenh` \| `nghi-dinh` \| `quyet-dinh-ttg` \| `thong-tu` \| `an-le` |
| `title` | Tên đầy đủ |
| `year` | Năm ban hành (int) |
| `issued_by` | Cơ quan ban hành |
| `status` | `hieu-luc` \| `sua-doi-bo-sung` \| `het-hieu-luc` \| `chua-co-hieu-luc` \| `du-thao` |
| `verify_status` | `seed` (cần đối chiếu VBPL) \| `checked` (đã đối chiếu ngày `verified_on`) |
| `branches` | list id trong `branches` của file |

## Trường khuyến nghị

| Field | Ý nghĩa |
| --- | --- |
| `short` | Tên gọi tắt |
| `number` | Số hiệu (`45/2019/QH14`); Hiến pháp = `null` |
| `effective_from` | `YYYY-MM-DD` hoặc `null` |
| `supersedes` | list `id` văn bản bị thay |
| `amended_by` | list số hiệu / id luật sửa đổi |
| `related_instruments` | NĐ/TT/án lệ liên quan (id) |
| `note` | path tương đối `notes/….md` hoặc `null` |
| `official_hint` | Gợi ý tìm trên Công báo / VBPL |
| `summary` | ≤ 160 ký tự |

## Thêm một văn bản

1. Copy block mẫu trong catalog, đổi `id` (không trùng).
2. `verify_status: seed` cho đến khi đối chiếu Công báo/VBPL → `checked` + `verified_on`.
3. Nếu viết ghi chú: copy [`templates/vn-law/law-note.md`](../../templates/vn-law/law-note.md) → `notes/<id>.md`, set `note:`.
4. Chạy `python scripts/check_vn_law_catalog.py`.

Không dán toàn văn luật vào repo. Tóm tắt điều/khoản + link nguồn gốc.
