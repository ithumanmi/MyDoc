# 📡 Data Sources Comparison (Polygon vs Quandl vs Tiingo)

| Tiêu chí | Polygon | Quandl/Nasdaq Data Link | Tiingo |
| --- | --- | --- | --- |
| Asset coverage | US equities, options, forex, crypto | Nhiều bộ dữ liệu kinh tế, futures, equities (tùy gói) | US equities, crypto, IEX pricing |
| Intraday depth | Tick/quotes, NBBO, aggregates 1s/1m | Tùy bộ dataset, nhiều gói chỉ EOD | IEX top-of-book, 1m bars |
| Corporate actions | Splits/dividends | Có (tùy dataset) | Splits/dividends |
| Fundamental | X | Tùy dataset (Sharadar/others) | Tiingo fundamentals (paid) |
| Latency | Thấp (streaming WebSocket) | Không tối ưu latency (phần lớn batch) | Tương đối thấp, pull REST |
| Pricing | Theo message/req, multi-tier | Theo dataset, credit-based | Flat per month tiers |
| Backfill | Đầy đủ tick/agg lịch sử | Phụ thuộc dataset | 15+ years EOD, intraday từ IEX |

## Khuyến nghị theo use-case
- **Intraday US equities/crypto, cần tick & stream:** Polygon (ưu tiên WebSocket, limit rate theo tier).
- **Nghiên cứu đa tài sản, dữ liệu kinh tế/futures:** Quandl/Nasdaq Data Link (chọn dataset phù hợp, ví dụ FRED, ICE, Sharadar).
- **Backtest EOD đơn giản, chi phí thấp:** Tiingo (EOD + 1m bars, corporate actions tốt).

## Lưu ý vận hành
- Kiểm tra licensing cho redistrib/share nội bộ vs sản phẩm.
- Rate limit: implement backoff, caching layer.
- Đồng bộ timezone, corporate action adjustment (split/dividend) nhất quán.
- Với tick lớn: lưu ở parquet + partition theo ngày/symbol; dùng DuckDB/Polars để query.