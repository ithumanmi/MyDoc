"""
Đối chiếu chi tiêu MoMo (chi_tieu_bi_tru / CostData) với sao kê ngân hàng
(bank_transactions_all.xlsx).

- Chi qua MoMo thường = bank ghi nợ MOMO/VNPAY CashIn (nạp ví) → không coi là thiếu
- Chi trực tiếp từ bank (QR, chuyển khoản, thẻ...) mà không có trên MoMo
  → append vào chi_tieu_bi_tru.xlsx với cột Note = thiếu trên MoMo / chỉ có trên bank
"""

from __future__ import annotations

import re
from pathlib import Path

import pandas as pd

REPO_ROOT = Path(__file__).resolve().parents[2]
DATA = REPO_ROOT / "data" / "expenses"
WORKING = DATA / "working"
BANK_FILE = WORKING / "bank_transactions_all.xlsx"
CHI_TIEU_FILE = WORKING / "chi_tieu_bi_tru.xlsx"
DATA_SHEET = "Chi tiêu bị trừ"
NOTE_COL = "Note"
NOTE_BANK_ONLY = "Thiếu trên MoMo — chỉ có trên ngân hàng"
NOTE_MOMO = "Từ MoMo"

# Nạp ví / trung gian: không phải khoản chi tiêu cần track thêm
WALLET_CASHIN_RE = re.compile(r"CashIn|MOMO|VNPAY|ZaloPay|ShopeePay|VNPay", re.I)


def _norm_cols(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    out.columns = [" ".join(str(c).split()) for c in out.columns]
    return out


def _is_blank(value: object) -> bool:
    if value is None or (isinstance(value, float) and pd.isna(value)):
        return True
    return str(value).strip() == ""


def _parse_bank_payee(content: str) -> str:
    """Rút tên người/đơn vị nhận từ nội dung Vietcombank."""
    text = " ".join(str(content).split())
    # CT tu ... toi <id?> <NAME> tai <BANK>
    m = re.search(
        r"toi\s+(?:#[^\s]+\s+)?(?:[A-Z0-9#]+\s+)?(.+?)\s+tai\s+[A-Z]+",
        text,
        flags=re.I,
    )
    if m:
        name = m.group(1).strip(" .")
        # bỏ mã đứng trước nếu còn
        name = re.sub(r"^[A-Z0-9#._\-]+\s+", "", name).strip()
        if name:
            return name

    m = re.search(r"Thanh toan cho\s+(.+?)(?:\s+tu tai khoan|$)", text, flags=re.I)
    if m:
        return m.group(1).strip()

    m = re.search(r"DV:\s*(.+?)\.\s*TranID", text, flags=re.I)
    if m:
        return m.group(1).strip()

    # fallback: rút gọn nội dung
    return text[:80]


def _is_wallet_topup(content: object) -> bool:
    text = str(content or "")
    if re.search(r"CashIn", text, re.I):
        return True
    if re.search(r"MOMO", text, re.I) and re.search(r"CashIn|Ecom\.EW", text, re.I):
        return True
    return bool(re.search(r"Ecom\.EW\d+.*\.(MOMO|VNPAY)\.", text, re.I))


def load_bank_direct_expenses(path: Path = BANK_FILE) -> pd.DataFrame:
    bank = pd.read_excel(path)
    bank = _norm_cols(bank)
    debit = bank[bank["Loại giao dịch"].astype(str).str.strip() == "Chi"].copy()
    debit["Nội dung"] = debit["Nội dung"].astype(str)
    direct = debit.loc[~debit["Nội dung"].map(_is_wallet_topup)].copy()
    direct["Tên định danh"] = direct["Nội dung"].map(_parse_bank_payee)
    direct["Số tiền"] = pd.to_numeric(direct["Số tiền"], errors="coerce")
    direct["Thời gian"] = pd.to_datetime(direct["Ngày giao dịch"], errors="coerce")
    return direct.reset_index(drop=True)


def load_chi_tieu(path: Path = CHI_TIEU_FILE) -> pd.DataFrame:
    try:
        df = pd.read_excel(path, sheet_name=DATA_SHEET)
    except ValueError:
        df = pd.read_excel(path, sheet_name=0)
    df = _norm_cols(df)
    mask_total = df.astype(str).apply(
        lambda col: col.str.contains(r"Tổng \(theo filter\)", na=False, regex=True)
    ).any(axis=1)
    if mask_total.any():
        df = df.loc[~mask_total].copy()
    return df.reset_index(drop=True)


def _chi_tieu_keys(df: pd.DataFrame) -> set[tuple]:
    """Khóa thô để tránh append trùng lần chạy lại."""
    if NOTE_COL not in df.columns:
        return set()
    bank_rows = df[df[NOTE_COL].astype(str).str.contains("ngân hàng", case=False, na=False)]
    keys = set()
    for _, row in bank_rows.iterrows():
        dt = pd.to_datetime(row.get("Thời gian"), dayfirst=True, errors="coerce")
        day = "" if pd.isna(dt) else dt.strftime("%Y-%m-%d")
        amt = pd.to_numeric(row.get("Số tiền"), errors="coerce")
        amt_s = "" if pd.isna(amt) else f"{float(amt):.0f}"
        name = "" if _is_blank(row.get("Tên định danh")) else str(row.get("Tên định danh")).strip()
        keys.add((day, amt_s, name))
    return keys


def build_missing_rows(direct: pd.DataFrame, existing_keys: set[tuple]) -> pd.DataFrame:
    rows = []
    for _, r in direct.iterrows():
        dt = r["Thời gian"]
        day = "" if pd.isna(dt) else pd.Timestamp(dt).strftime("%Y-%m-%d")
        amt = r["Số tiền"]
        amt_s = "" if pd.isna(amt) else f"{float(amt):.0f}"
        name = str(r["Tên định danh"]).strip()
        key = (day, amt_s, name)
        if key in existing_keys:
            continue
        rows.append(
            {
                "Thời gian": dt,
                "Loại giao dịch": "Chi trực tiếp ngân hàng",
                "Tên định danh": name,
                "Category": "",
                "SubCategory": "",
                "Số tiền": amt,
                "Nguồn file": "bank_transactions_all.xlsx",
                NOTE_COL: NOTE_BANK_ONLY,
                "Nội dung bank": r["Nội dung"],
                "Số chứng từ": r.get("Số chứng từ", ""),
            }
        )
    return pd.DataFrame(rows)


def ensure_note_column(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    if NOTE_COL not in out.columns:
        out[NOTE_COL] = ""
    # Đánh dấu dòng MoMo (chưa có note bank)
    is_bank_note = out[NOTE_COL].astype(str).str.contains("ngân hàng", case=False, na=False)
    empty = out[NOTE_COL].map(_is_blank)
    out.loc[empty & ~is_bank_note, NOTE_COL] = NOTE_MOMO
    return out


def merge_into_chi_tieu(
    chi: pd.DataFrame,
    missing: pd.DataFrame,
) -> pd.DataFrame:
    chi = ensure_note_column(chi)

    if missing.empty:
        # Vẫn chuẩn hóa cột Note
        cols = [c for c in chi.columns if c != NOTE_COL]
        if "Nguồn file" in cols:
            idx = cols.index("Nguồn file")
            cols = cols[:idx] + [NOTE_COL] + cols[idx:]
        elif NOTE_COL not in cols:
            cols.append(NOTE_COL)
        return chi[[c for c in cols if c in chi.columns]]

    for col in missing.columns:
        if col not in chi.columns:
            chi[col] = ""
    for col in chi.columns:
        if col not in missing.columns:
            missing[col] = pd.NA if col == "Số tiền" else ""

    cols = [c for c in chi.columns if c != NOTE_COL]
    if "Nguồn file" in cols:
        idx = cols.index("Nguồn file")
        cols = cols[:idx] + [NOTE_COL] + cols[idx:]
    else:
        cols.append(NOTE_COL)

    combined = pd.concat([chi[cols], missing[cols]], ignore_index=True)
    return combined


def finalize_and_write(df: pd.DataFrame, path: Path) -> Path:
    """Gán category + ghi Excel đầy đủ format (màu, SUBTOTAL, Tổng hợp, Dashboard)."""
    import process_expenses as pe

    updated = pe.ensure_category_columns(df)
    if NOTE_COL not in updated.columns:
        updated[NOTE_COL] = ""
    # Đưa Note trước Nguồn file
    cols = [c for c in updated.columns if c != NOTE_COL]
    if "Nguồn file" in cols:
        i = cols.index("Nguồn file")
        cols = cols[:i] + [NOTE_COL] + cols[i:]
    else:
        cols.append(NOTE_COL)
    # Giữ các cột phụ nếu có (Nội dung bank, Số chứng từ)
    for extra in df.columns:
        if extra not in cols:
            cols.append(extra)
            if extra not in updated.columns:
                updated[extra] = df[extra]
    updated = updated[[c for c in cols if c in updated.columns]]

    updated = pe.ensure_date_columns(updated)
    updated, new_sub = pe.fill_empty_subcategories(updated)
    updated, new_cat = pe.apply_categories(updated)

    parsed = pe.parse_time_series(updated[pe.COL_TIME])
    updated = updated.assign(_sort=parsed).sort_values("_sort", ascending=False)
    updated = updated.drop(columns=["_sort"]).reset_index(drop=True)

    try:
        pe._write_excel(updated, path)
        out = path
    except PermissionError:
        out = path.with_name(f"{path.stem}_out{path.suffix}")
        pe._write_excel(updated, out)
        print(f"File đang mở — đã ghi: {out.name}")

    print(f"SubCategory mới điền (sau sync): {new_sub}")
    print(f"Category gán từ rule (sau sync): {new_cat}")
    return out


def main() -> None:
    if not BANK_FILE.exists():
        raise FileNotFoundError(f"Thiếu {BANK_FILE.name}. Chạy merge_bank_statements.py trước.")
    if not CHI_TIEU_FILE.exists():
        raise FileNotFoundError(f"Thiếu {CHI_TIEU_FILE.name}. Chạy process_expenses.py trước.")

    print("1) Lấy chi trực tiếp từ ngân hàng (loại trừ nạp MoMo/VNPAY)...")
    direct = load_bank_direct_expenses(BANK_FILE)
    print(f"   → {len(direct)} giao dịch bank direct")

    print("2) Đọc chi_tieu_bi_tru...")
    chi = load_chi_tieu(CHI_TIEU_FILE)
    existing_keys = _chi_tieu_keys(chi)
    print(f"   → {len(chi)} dòng hiện có | bank-note sẵn: {len(existing_keys)}")

    print("3) Tìm khoản thiếu trên MoMo...")
    missing = build_missing_rows(direct, existing_keys)
    print(f"   → {len(missing)} dòng sẽ thêm (Note: {NOTE_BANK_ONLY})")

    if not missing.empty:
        print("   Mẫu:")
        for _, r in missing.head(8).iterrows():
            print(
                f"     - {pd.Timestamp(r['Thời gian']).date()} | "
                f"{r['Số tiền']:,.0f} | {r['Tên định danh'][:50]}"
            )

    print("4) Gộp + ghi lại full format (màu Category/SubCategory, SUBTOTAL, Dashboard)...")
    updated = merge_into_chi_tieu(chi, missing)
    out = finalize_and_write(updated, CHI_TIEU_FILE)

    bank_n = updated[NOTE_COL].astype(str).str.contains("ngân hàng", case=False, na=False).sum()
    momo_n = (updated[NOTE_COL].astype(str) == NOTE_MOMO).sum()
    print(f"Xong: {out}")
    print(f"Tổng dòng: {len(updated)} | Note MoMo: {momo_n} | Note bank-only: {bank_n}")
    if bank_n:
        total_gap = pd.to_numeric(
            updated.loc[
                updated[NOTE_COL].astype(str).str.contains("ngân hàng", case=False, na=False),
                "Số tiền",
            ],
            errors="coerce",
        ).sum()
        print(f"Tổng tiền thiếu trên MoMo (bank-only): {total_gap:,.0f}")

    try:
        import export_powerbi

        print("\n--- Export Power BI ---")
        export_powerbi.export_all()
    except Exception as exc:  # noqa: BLE001
        print(f"Bỏ qua export Power BI: {exc}")


if __name__ == "__main__":
    main()
