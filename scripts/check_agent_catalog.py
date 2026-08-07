#!/usr/bin/env python3
"""Validate catalog/topics.yaml canonical (+ related) paths exist."""
from __future__ import annotations

import sys
from pathlib import Path

try:
    import yaml  # type: ignore
except ImportError:
    yaml = None

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "catalog" / "topics.yaml"


def load_topics(text: str) -> list[dict]:
    if yaml is not None:
        data = yaml.safe_load(text)
        return list(data.get("topics") or [])
    # Minimal fallback parser for our simple YAML subset
    topics: list[dict] = []
    cur: dict | None = None
    mode = None
    for raw in text.splitlines():
        line = raw.rstrip()
        if line.startswith("  - id:"):
            if cur:
                topics.append(cur)
            cur = {"id": line.split(":", 1)[1].strip(), "related": []}
            mode = None
        elif cur is None:
            continue
        elif line.startswith("    aliases:"):
            mode = "aliases"
            rest = line.split(":", 1)[1].strip()
            if rest.startswith("[") and rest.endswith("]"):
                inner = rest[1:-1].strip()
                cur["aliases"] = [x.strip().strip("'\"") for x in inner.split(",") if x.strip()] if inner else []
        elif line.startswith("    canonical:"):
            cur["canonical"] = line.split(":", 1)[1].strip()
            mode = None
        elif line.startswith("    related:"):
            mode = "related"
            rest = line.split(":", 1)[1].strip()
            if rest.startswith("[") and rest.endswith("]"):
                inner = rest[1:-1].strip()
                cur["related"] = [x.strip().strip("'\"") for x in inner.split(",") if x.strip()] if inner else []
            elif rest in ("", "[]"):
                cur["related"] = []
        elif mode == "related" and line.startswith("      - "):
            cur.setdefault("related", []).append(line.split("-", 1)[1].strip())
        elif line.startswith("    sensitivity:") or line.startswith("    notes:"):
            mode = None
    if cur:
        topics.append(cur)
    return topics


def main() -> int:
    if not CATALOG.exists():
        print(f"MISSING {CATALOG}")
        return 1
    topics = load_topics(CATALOG.read_text(encoding="utf-8"))
    missing = []
    for t in topics:
        tid = t.get("id", "?")
        paths = [t.get("canonical")] + list(t.get("related") or [])
        for p in paths:
            if not p:
                continue
            path = ROOT / p.replace("\\", "/")
            if not path.exists():
                missing.append((tid, p))
    if missing:
        print("Missing paths:")
        for tid, p in missing:
            print(f"  [{tid}] {p}")
        return 1
    print(f"OK — {len(topics)} topics, all canonical/related paths exist.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
