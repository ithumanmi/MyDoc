"""Cột + rubric cho sheet đánh giá performance (tuần/tháng/quý/năm)."""

from __future__ import annotations

# Cột chung cho Perf_* (period_key đổi theo sheet)
def perf_columns(period_key: str, period_meaning: str) -> list[tuple[str, str]]:
    return [
        (period_key, period_meaning),
        ("Items", "Số cụm việc trong kỳ (từ Metrics / Prod) — snapshot, không sửa tay trừ khi cần"),
        ("Done", "Số status=done"),
        ("Shipped", "Số outcome=shipped"),
        ("Ship_pct", "% shipped/items — gợi ý throughput"),
        ("Est_hours", "Giờ ước từ effort S/M/L/XL"),
        ("Reopen_sum", "Tổng reopen trong kỳ (ổn định / nợ kỹ thuật)"),
        ("Blockers", "blocked_by gộp — đọc trước khi chấm Stability"),
        ("Throughput_1_10", "Chấm: khối lượng / tốc độ ship hữu ích · 1 chậm · 10 rất nhanh đúng hướng"),
        ("Quality_1_10", "Chấm: tests/docs/playtest · ít reopen · ít unverified"),
        ("Focus_1_10", "Chấm: có bám P0/epic không · ít nhảy topic"),
        ("Stability_1_10", "Chấm: ít blocker kéo dài · ít firefight · ít reopen"),
        ("Overall_1_10", "Điểm tổng (có thể ≈ TB 4 cột trên)"),
        ("Wins", "1–3 thắng đáng nhớ trong kỳ"),
        ("Misses", "Miss / partial quan trọng"),
        ("Root_cause", "Vì sao miss/blocker (1–2 câu)"),
        ("Keep", "Giữ thói quen / cách làm nào"),
        ("Stop", "Bỏ hoặc giảm gì"),
        ("Start", "Thử gì kỳ sau (1 thí nghiệm)"),
        ("Energy", "Năng lượng làm việc kỳ này (chữ ngắn hoặc 1–10)"),
        ("Next_priority", "Ưu tiên #1 kỳ tới"),
        ("Reviewed_on", "Ngày bạn làm review (yyyy-mm-dd)"),
        ("Note", "Ghi chú thêm"),
    ]


PERF_RUBRIC_ROWS = [
    ("Throughput", "Khối lượng ship hữu ích", "Ít việc / chủ yếu WIP", "Đều đặn Feature+Fix đúng focus", "Nhiều shipped, ít dead-end"),
    ("Quality", "Độ tin cậy bản ship", "Unverified / thiếu test / docs lệch", "docs_synced + needs_playtest có kế hoạch", "tests_ok, ít reopen"),
    ("Focus", "Bám mục tiêu / epic", "Nhảy category liên tục", "Phần lớn giờ vào P0–P1", "Epic/story đóng đúng wave"),
    ("Stability", "Ít nợ kéo dài", "Blocker lặp / firefight", "Blocker có owner + hạn", "Ít blocked_by; closes nợ cũ"),
    ("Overall", "Cảm nhận hiệu suất kỳ", "Kỳ mệt, ít tiến", "Tiến ổn", "Kỳ mạnh, rõ thắng"),
]
