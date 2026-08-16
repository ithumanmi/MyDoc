"""
Export dữ liệu sạch cho Power BI (1 bảng / file, không Dashboard, không SUBTOTAL).

Output mặc định trong data/expenses/powerbi/:
  - chi_tieu_powerbi.csv / .xlsx
  - bank_transactions_powerbi.csv / .xlsx
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd

REPO_ROOT = Path(__file__).resolve().parents[2]
DATA = REPO_ROOT / "data" / "expenses"
WORKING = DATA / "working"
OUT_DIR = DATA / "powerbi"
CHI_TIEU_FILE = WORKING / "chi_tieu_bi_tru.xlsx"
BANK_FILE = WORKING / "bank_transactions_all.xlsx"
DATA_SHEET = "Chi tiêu bị trừ"

CHI_TIEU_COLS = [
    "Thời gian",
    "Ngày",
    "Tuần",
    "Tháng",
    "Năm",
    "Loại giao dịch",
    "Tên định danh",
    "Category",
    "SubCategory",
    "Số tiền",
    "Số tiền tuyệt đối",
    "Note",
    "Nguồn",
    "Nguồn file",
    "Nội dung bank",
    "Số chứng từ",
]


def _norm_cols(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    out.columns = [" ".join(str(c).split()) for c in out.columns]
    return out


def _drop_total_rows(df: pd.DataFrame) -> pd.DataFrame:
    mask = df.astype(str).apply(
        lambda col: col.str.contains(r"Tổng \(theo filter\)|^Tổng cộng$", na=False, regex=True)
    ).any(axis=1)
    if mask.any():
        return df.loc[~mask].copy()
    return df.copy()


def load_chi_tieu(path: Path = CHI_TIEU_FILE) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(f"Thiếu {path}")
    try:
        df = pd.read_excel(path, sheet_name=DATA_SHEET)
    except ValueError:
        df = pd.read_excel(path, sheet_name=0)
    df = _norm_cols(df)
    df = _drop_total_rows(df)

    # Chuẩn hóa kiểu
    if "Thời gian" in df.columns:
        df["Thời gian"] = pd.to_datetime(df["Thời gian"], dayfirst=True, errors="coerce")
    if "Ngày" in df.columns:
        df["Ngày"] = pd.to_datetime(df["Ngày"], dayfirst=True, errors="coerce").dt.normalize()
    elif "Thời gian" in df.columns:
        df["Ngày"] = df["Thời gian"].dt.normalize()

    if "Số tiền" in df.columns:
        df["Số tiền"] = pd.to_numeric(df["Số tiền"], errors="coerce")
        df["Số tiền tuyệt đối"] = df["Số tiền"].abs()

    if "Năm" in df.columns:
        df["Năm"] = pd.to_numeric(df["Năm"], errors="coerce").astype("Int64")

    # Nguồn phân tích: MoMo / Ngân hàng
    note = df["Note"].astype(str) if "Note" in df.columns else pd.Series([""] * len(df))
    df["Nguồn"] = note.map(
        lambda v: "Ngân hàng"
        if "ngân hàng" in v.lower()
        else ("MoMo" if "momo" in v.lower() else "Khác")
    )

    for col in ("Category", "SubCategory", "Note", "Loại giao dịch", "Tên định danh"):
        if col in df.columns:
            df[col] = df[col].fillna("").astype(str).str.strip()
            df.loc[df[col].isin(["", "nan", "None"]), col] = "(chưa gán)"

    keep = [c for c in CHI_TIEU_COLS if c in df.columns]
    return df[keep].reset_index(drop=True)


def load_bank(path: Path = BANK_FILE) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(f"Thiếu {path}")
    df = pd.read_excel(path)
    df = _norm_cols(df)
    if "Ngày giao dịch" in df.columns:
        df["Ngày giao dịch"] = pd.to_datetime(df["Ngày giao dịch"], errors="coerce")
    if "Ngày" in df.columns:
        df["Ngày"] = pd.to_datetime(df["Ngày"], errors="coerce").dt.normalize()
    if "Số tiền" in df.columns:
        df["Số tiền"] = pd.to_numeric(df["Số tiền"], errors="coerce")
        df["Số tiền tuyệt đối"] = df["Số tiền"].abs()
    if "Năm" in df.columns:
        df["Năm"] = pd.to_numeric(df["Năm"], errors="coerce").astype("Int64")
    return df.reset_index(drop=True)


def _write_outputs(df: pd.DataFrame, stem: str, out_dir: Path) -> tuple[Path, Path]:
    out_dir.mkdir(parents=True, exist_ok=True)
    csv_path = out_dir / f"{stem}.csv"
    xlsx_path = out_dir / f"{stem}.xlsx"

    df.to_csv(csv_path, index=False, encoding="utf-8-sig")

    with pd.ExcelWriter(xlsx_path, engine="openpyxl") as writer:
        df.to_excel(writer, index=False, sheet_name="Data")
        ws = writer.sheets["Data"]
        ws.auto_filter.ref = ws.dimensions
        ws.freeze_panes = "A2"

    return csv_path, xlsx_path


def export_all(out_dir: Path = OUT_DIR) -> dict[str, Path]:
    results: dict[str, Path] = {}

    chi = load_chi_tieu()
    csv_p, xlsx_p = _write_outputs(chi, "chi_tieu_powerbi", out_dir)
    results["chi_tieu_csv"] = csv_p
    results["chi_tieu_xlsx"] = xlsx_p
    print(f"Chi tiêu: {len(chi)} dòng")
    print(f"  → {csv_p}")
    print(f"  → {xlsx_p}")
    if "Nguồn" in chi.columns:
        print("  Nguồn:", chi["Nguồn"].value_counts().to_dict())
    if "Số tiền" in chi.columns:
        print(f"  Tổng số tiền: {chi['Số tiền'].sum():,.0f}")

    if BANK_FILE.exists():
        bank = load_bank()
        csv_p, xlsx_p = _write_outputs(bank, "bank_transactions_powerbi", out_dir)
        results["bank_csv"] = csv_p
        results["bank_xlsx"] = xlsx_p
        print(f"Bank: {len(bank)} dòng")
        print(f"  → {csv_p}")
        print(f"  → {xlsx_p}")
    else:
        print("Bỏ qua bank (chưa có bank_transactions_all.xlsx)")

    return results


def main() -> None:
    print(f"Export Power BI → {OUT_DIR}")
    export_all()
    print("\nPower BI Desktop: Get data → Text/CSV → chọn file trong data/expenses/powerbi/")
    print("Gợi ý: dùng chi_tieu_powerbi.csv (nhẹ, refresh ổn định).")


if __name__ == "__main__":
    main()
