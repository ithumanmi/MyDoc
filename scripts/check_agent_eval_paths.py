#!/usr/bin/env python3
"""Verify expected/related paths listed in meta/eval/questions.md exist."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
QUESTIONS = ROOT / "meta" / "eval" / "questions.md"
PATH_RE = re.compile(r"`([^`]+)`")


def extract_table_paths(text: str) -> list[tuple[str, str]]:
    """Return list of (qid, path) from Expected + Acceptable columns."""
    found: list[tuple[str, str]] = []
    for line in text.splitlines():
        if not line.startswith("|") or "Question" in line or line.startswith("| ---"):
            continue
        cols = [c.strip() for c in line.strip("|").split("|")]
        if len(cols) < 4:
            continue
        qid, _q, expected, related = cols[0], cols[1], cols[2], cols[3]
        if not qid.isdigit():
            continue
        for cell in (expected, related):
            for m in PATH_RE.findall(cell):
                p = m.strip()
                # skip non-path tokens
                if p.endswith(".md") or "/" in p or p.endswith("/"):
                    found.append((qid, p.rstrip("/")))
    return found


def main() -> int:
    if not QUESTIONS.exists():
        print(f"MISSING {QUESTIONS}")
        return 1
    entries = extract_table_paths(QUESTIONS.read_text(encoding="utf-8"))
    missing = []
    checked = set()
    for qid, rel in entries:
        key = (qid, rel)
        if key in checked:
            continue
        checked.add(key)
        path = ROOT / rel
        # allow directory targets
        if path.exists() or (ROOT / (rel + "/README.md")).exists():
            continue
        # if path was meant as directory without README
        if (ROOT / rel).is_dir():
            continue
        missing.append((qid, rel))

    if missing:
        print("Missing paths:")
        for qid, rel in missing:
            print(f"  [Q{qid}] {rel}")
        return 1
    print(f"OK — {len(checked)} path refs in meta/eval/questions.md resolve.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
