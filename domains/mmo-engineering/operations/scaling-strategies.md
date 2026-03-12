# 📡 Scaling Strategies (Farm Ops)

> Khi farm đạt 1.000+ account, cần chiến lược scale ổn định.

## 1. Horizontal vs Vertical
- **Horizontal:** thêm phone rack/proxy mới, scale out region khác.
  - Pros: giảm blast radius khi bị ban.
  - Cons: cần monitoring/log aggregator multi-region.
- **Vertical:** tăng số account/device trên hạ tầng hiện tại.
  - Pros: tận dụng infra sẵn.
  - Cons: dễ tạo single point of failure.

## 2. Capacity Planning
- Metric chính: `accounts_per_proxy`, `CPU per automation host`, `network throughput`.
- Set `max_accounts_per_farm = floor(proxy_success_rate * automation_capacity)`.
- Reserve 15% buffer cho incident.

## 3. Scaling Workflow
1. Dựa trên dashboard `Account Survival` & `Queue Backlog` để xác định bottleneck.
2. Spin-up cluster mới (Ansible/Terraform) → register vào monitoring.
3. Clone config (feature flags, tool version) từ farm chuẩn.
4. Smoke test 20 account trước khi mở rộng.

## 4. Log Aggregation 1.000+ accounts
- Dùng Fluent Bit/Vector agent gửi log về Kafka → ClickHouse/S3 (parquet) để tối ưu chi phí.
- Partition theo `farm_id` + `day`.
- Alert nếu log ingestion < expected (có thể agent chết).

## 5. Auto-Scaling Hooks
- Sử dụng queue depth (RabbitMQ/Kafka lag) → trigger lambda/script tạo thêm worker.
- Phone farm: robot arm/công tắc IoT để bật thêm device tự động.

## 6. Scaling Checklist
- [ ] Observability có trước khi scale.
- [ ] Runbook cập nhật cho farm mới.
- [ ] Budget (CapEx/OpEx) align với ROI target.