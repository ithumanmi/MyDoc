# 🚨 Incident Response Playbook (Mass Ban)

> Quy trình khi farm bị checkpoint/banned hàng loạt.

## 1. Detection
- Trigger từ alert `checkpoint_rate > 10%/10 phút` hoặc `survival_drop > 5%/15 phút`.
- Grafana annotation tạo Incident ID.

## 2. Triage Checklist
1. Xác minh log aggregator (Loki/ELK) có thu log đầy đủ.
2. Kiểm tra proxy provider nào bị blacklist.
3. Review changelog CI/CD (tool mới deploy?).
4. Lấy mẫu screenshot/error từ 5 account đầu tiên.

## 3. Containment
- Auto-pause toàn bộ batch/farm bị ảnh hưởng.
- Forensic script lấy cookie/session để phân tích offline.
- Switch sang backup proxy range nếu nghi do IP.

## 4. Eradication
- Rollback code/tool version (giữ bản N-1).
- Reset device fingerprint nếu phát hiện pattern lộ diện.
- Update warm-up SOP nếu mass ban do hành vi lặp.

## 5. Recovery
- Re-enable từng wave (10% → 30% → 100%) với monitoring chặt.
- Bù account die bằng inventory dự phòng (check `case-studies.md` phone farm).

## 6. Post-Incident Review
- Root cause doc: proxy, script, payment? KPI ảnh hưởng?
- Update runbook, alert threshold nếu cần.
- Gửi báo cáo cho stakeholders (ops, finance).

## 7. Tooling
- Incident tracker (Notion/Jira) lưu timeline.
- Script `mass_pause.py`, `proxy_switcher.py`.
- Dashboard “Incident Mode” highlight survival/checkpoint per minute.