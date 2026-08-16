# Chi tiêu & sao kê ngân hàng

> Thư mục **dữ liệu làm việc** (Excel/CSV). Code nằm ở [`scripts/expenses/`](../../scripts/expenses/).

[← Home](../../README.md) | [Scripts](../../scripts/expenses/README.md) | [Personal logs](../../personal/README.md)

## Cấu trúc

```
data/expenses/
├── raw/       ← sao kê ngân hàng tải về (ví dụ Vietcombank)
├── working/   ← file đang xử lý: CostData, chi_tieu_bi_tru, bank_transactions_all
└── powerbi/   ← bản sạch để nạp Power BI
```

| Thư mục | Đặt gì vào đây |
| --- | --- |
| `raw/` | File sao kê gốc (chưa gộp) |
| `working/` | `CostData.xlsx` (MoMo), `chi_tieu_bi_tru.xlsx`, `bank_transactions_all.*` |
| `powerbi/` | CSV/XLSX đã làm sạch — Get data trong Power BI Desktop |

Nội dung `raw/`, `working/`, `powerbi/` **không commit** (gitignore) vì chứa giao dịch cá nhân.

## Pipeline

```powershell
pip install -r scripts/expenses/requirements.txt
python scripts/expenses/merge_bank_statements.py   # raw → working/bank_transactions_all
python scripts/expenses/process_expenses.py         # CostData → chi_tieu (+ sync + export BI)
# hoặc từng bước:
python scripts/expenses/sync_bank_gaps.py
python scripts/expenses/export_powerbi.py
```

Log dinh dưỡng / ngủ / habit vẫn ở `personal/` — không trộn Excel chi tiêu vào đó.
