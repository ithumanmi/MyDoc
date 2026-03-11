---
title: "Designing Large Video Upload Backend"
description: "Hệ thống backend xử lý upload video 50GB+: chunked upload, storage tiering, pipeline transcode, CDN và bảo mật."
tags:
  - backend
  - system-design
  - video
updated: 2026-03-11
---

# 📼 Designing Large Video Upload Backend (50GB)

> Bài toán: người dùng upload video dung lượng cực lớn (50GB). Hệ thống phải đảm bảo trải nghiệm ổn định, tối ưu chi phí, hỗ trợ xử lý hậu kỳ (transcode, thumbnail, moderation) và phân phối toàn cầu.

## 1. Yêu cầu & Ràng buộc
- **Kỹ thuật**: upload resume, bảo toàn dữ liệu, transcode ra nhiều bitrate, streaming preview nhanh.
- **Phi chức năng**: throughput cao (hàng nghìn upload đồng thời), latency chấp nhận được, durability 11×9, tuân thủ bảo mật.
- **Product**: hỗ trợ pause/resume, tracking trạng thái, thông báo khi xử lý xong, quota/billing rõ ràng.

## 2. Luồng tổng quan
1. Client yêu cầu upload session → backend cấp credential tạm (STS) và metadata ID.
2. Client chunk video (5–100MB/chunk) và upload trực tiếp lên Object Storage (S3/GCS/MinIO) qua multipart API.
3. Backend nhận webhook/notification khi upload hoàn tất → trigger pipeline: validate, virus scan, transcode, generate thumbnail, moderation.
4. Thêm metadata vào DB (Postgres/DynamoDB) + index tìm kiếm (Elasticsearch).
5. Publish cập nhật trạng thái qua event bus (Kafka/SNS) tới client (websocket/email).
6. Nội dung được phân phối qua CDN sau khi transcode hoàn tất.

```
Client → Upload Service → (STS Credential) → Multipart Upload (Object Storage)
                           ↓                                   ↓
                    Metadata Service                 Event/Queue → Processing Workers → CDN
```

## 3. Thành phần kiến trúc
- **Upload Gateway**: API ký URL, xác thực user, enforce quota (rate limiter, RBAC).
- **Object Storage**: bucket riêng cho `raw` và `processed`, bật versioning.
- **Processing Pipeline**: hàng đợi (Kafka/SQS), worker dùng FFmpeg/MediaConvert, GPU cluster hoặc dịch vụ managed.
- **Metadata Store**: RDBMS (transaction) + search index (Elastic/OpenSearch).
- **Notification Layer**: Webhook, WebSocket, email, push.
- **Observability**: tracing (OpenTelemetry), metric (upload success rate, processing time), log correlation ID.

## 4. Thiết kế Upload 50GB
- **Multipart Upload**: chia nhỏ chunk 8–64MB → retry từng phần, client resume qua `uploadId`.
- **Client-side checksum** (MD5) + server-side integrity check.
- **Pre-signed URL**: TTL ngắn (15 phút), scope chỉ upload.
- **Upload acceleration**: dùng edge POP hoặc S3 Transfer Acceleration.
- **Resume/Recovery**: lưu state chunk đã hoàn thành vào local storage và metadata service.

## 5. Pipeline xử lý hậu kỳ
- **Virus scan** (ClamAV/Lambda) cho compliance.
- **Transcode**: adaptive bitrate (240p–4K), format HLS/DASH.
- **Thumbnail/Preview**: cắt frame ở t=5s, tạo animated preview.
- **Moderation**: AI model (Vision API) để phát hiện nội dung nhạy cảm.
- **Storage tiering**: raw video chuyển sang Glacier/Archive sau X ngày.

## 6. Metadata & Access Control
- Bảng `video_asset`: id, owner_id, status, storage_uri, duration, size, checksum.
- Dùng event sourcing + materialized view cho update liên tục.
- ACL: token download phải kiểm tra quyền (signed URL + policy).
- Logging/Audit cho mọi hành động (upload/delete/share).

## 7. Scaling & Cost Strategy
- Upload gateway stateless, auto-scale, tách khỏi worker.
- Dùng spot/preemptible instance cho transcode + queue buffer.
- CDN caching, storage tier (standard → IA → archive).
- Lifecycle policy xóa raw nếu không cần sau N ngày.

## 8. Bảo mật & Compliance
- IAM least privilege, token scope hạn chế.
- Encrypt in transit (TLS) & at rest (SSE-KMS).
- Rate limit + WAF chống abuse.
- Tuân thủ GDPR/CCPA: delete request, data residency.

## 9. Quan sát & Vận hành
- Metric: upload success rate, chunk retry, queue lag, transcode duration, CDN hit.
- Alert khi queue backlog cao, storage full, error rate tăng.
- Chaos test: fail storage region, drop worker, latency injection.

## 10. 🧪 Lab: PoC Multipart Upload + Processing Queue
1. Tạo bucket `videos-raw` (MinIO/S3) với versioning.
2. Viết API `/upload/session` (Node/Go) trả về pre-signed URL + uploadId.
3. Client (CLI/web) chunk 32MB, retry khi 5xx, lưu state.
4. Cấu hình event (S3 notification) → push message vào Kafka/SQS.
5. Worker (container FFmpeg) lấy file, transcode sample HLS.
6. Lưu metadata (Postgres) và phát event `VIDEO_READY` qua WebSocket.
7. Upload output sang bucket `videos-processed`, cấu hình CloudFront.

## 11. Checklist
- [ ] Hỗ trợ pause/resume upload (multipart API + state tracking).
- [ ] Pre-signed URL/STS credential TTL ngắn.
- [ ] Pipeline transcode queue + worker auto-scale.
- [ ] Metadata store log đầy đủ checksum, duration, status.
- [ ] Bật encryption, logging, audit trail.
- [ ] Lifecycle policy raw/processed storage + cost estimation.
- [ ] Diễn tập failover (region, worker) và cập nhật runbook.

## 12. Liên kết hữu ích
- [System Design Universe](./system-design-universe.md)
- [Design Instagram](./design-instagram.md)
- [Amazon S3 Architecture](./amazon-s3-architecture.md)
- AWS docs: Multipart Upload, MediaConvert, CloudFront Signed URL.