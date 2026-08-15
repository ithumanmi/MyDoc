#!/usr/bin/env python3
"""Validate guides/06-vn-law/catalog.yaml ids, required fields, and note paths."""
from __future__ import annotations

import sys
from pathlib import Path

try:
    import yaml  # type: ignore
except ImportError:
    yaml = None

ROOT = Path(__file__).resolve().parents[1]
HUB = ROOT / "guides" / "06-vn-law"
CATALOG = HUB / "catalog.yaml"

REQUIRED = (
    "id",
    "type",
    "title",
    "year",
    "issued_by",
    "status",
    "verify_status",
    "branches",
)

ALLOWED_TYPE = {
    "hien-phap",
    "bo-luat",
    "luat",
    "nghi-quyet-qh",
    "phap-lenh",
    "nghi-dinh",
    "quyet-dinh-ttg",
    "thong-tu",
    "an-le",
}

ALLOWED_STATUS = {
    "hieu-luc",
    "sua-doi-bo-sung",
    "het-hieu-luc",
    "chua-co-hieu-luc",
    "du-thao",
}

ALLOWED_VERIFY = {"seed", "checked"}


def load_catalog(text: str) -> dict:
    if yaml is None:
        print("MISSING PyYAML — pip install pyyaml", file=sys.stderr)
        sys.exit(2)
    data = yaml.safe_load(text)
    if not isinstance(data, dict):
        raise ValueError("catalog.yaml must be a mapping")
    return data


def main() -> int:
    if not CATALOG.exists():
        print(f"MISSING {CATALOG}")
        return 1
    data = load_catalog(CATALOG.read_text(encoding="utf-8"))
    instruments = list(data.get("instruments") or [])
    branch_ids = {b.get("id") for b in (data.get("branches") or []) if b.get("id")}
    ids: list[str] = []
    errors: list[str] = []

    if not instruments:
        errors.append("no instruments[]")

    for i, item in enumerate(instruments):
        loc = item.get("id") or f"#{i}"
        for key in REQUIRED:
            if key not in item or item[key] in ("", []):
                errors.append(f"[{loc}] missing {key}")
        iid = item.get("id")
        if iid:
            ids.append(iid)
        if item.get("type") not in ALLOWED_TYPE:
            errors.append(f"[{loc}] bad type {item.get('type')!r}")
        if item.get("status") not in ALLOWED_STATUS:
            errors.append(f"[{loc}] bad status {item.get('status')!r}")
        if item.get("verify_status") not in ALLOWED_VERIFY:
            errors.append(f"[{loc}] bad verify_status {item.get('verify_status')!r}")
        if item.get("verify_status") == "checked" and not item.get("verified_on"):
            errors.append(f"[{loc}] checked requires verified_on")
        for b in item.get("branches") or []:
            if b not in branch_ids:
                errors.append(f"[{loc}] unknown branch {b!r}")
        note = item.get("note")
        if note:
            path = HUB / str(note).replace("\\", "/")
            if not path.exists():
                errors.append(f"[{loc}] missing note {note}")

    dupes = sorted({x for x in ids if ids.count(x) > 1})
    for d in dupes:
        errors.append(f"duplicate id {d}")

    id_set = set(ids)
    for item in instruments:
        loc = item.get("id") or "?"
        for field in ("supersedes", "related_instruments"):
            for ref in item.get(field) or []:
                if ref not in id_set:
                    errors.append(f"[{loc}] {field} unknown id {ref!r}")

    if errors:
        print("Catalog errors:")
        for e in errors:
            print(f"  {e}")
        return 1
    print(f"OK — {len(instruments)} instruments, notes and ids valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
