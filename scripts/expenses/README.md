# Scripts chi tiêu

> Code xử lý chi tiêu / sao kê. Dữ liệu: [`data/expenses/`](../../data/expenses/).

[← data hub](../../data/expenses/README.md)

## Cài đặt

```powershell
pip install -r scripts/expenses/requirements.txt
```

Cần `pandas` và `openpyxl`.

## Script

| File | Việc |
| --- | --- |
| `merge_bank_statements.py` | Gộp `data/expenses/raw/*.xlsx` → `working/bank_transactions_all.*` |
| `process_expenses.py` | `working/CostData.xlsx` → `chi_tieu_bi_tru.xlsx` (phân loại + dashboard); gọi sync + export nếu có bank |
| `sync_bank_gaps.py` | Bổ sung khoản chỉ có trên ngân hàng vào chi tiêu |
| `export_powerbi.py` | Xuất bảng sạch ra `data/expenses/powerbi/` |

## Chạy nhanh

```powershell
python scripts/expenses/merge_bank_statements.py
python scripts/expenses/process_expenses.py
```

Power BI: **Get data → Text/CSV** → chọn `data/expenses/powerbi/chi_tieu_powerbi.csv`.
