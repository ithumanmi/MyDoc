#!/usr/bin/env python3
"""Summarize personal/ week + compute Lifestyle score /100.

Usage:
  python scripts/personal_week_summary.py
  python scripts/personal_week_summary.py --week 2026-W32
  python scripts/personal_week_summary.py --week 2026-W32 --write
"""
from __future__ import annotations

import argparse
import csv
import re
import sys
from dataclasses import dataclass
from datetime import date, datetime, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PERSONAL = ROOT / "personal"
CONFIG_PATH = PERSONAL / "config.yaml"


def load_config() -> dict:
    defaults = {
        "targets": {
            "sleep_h_min": 7.0,
            "sleep_h_max": 9.0,
            "sleep_quality_min": 6,
            "deep_work_h_week": 10.0,
            "workouts_week": 3,
            "nutrition_days_week": 7,
            "metrics_days_week": 7,
        },
        "weights": {
            "sleep": 25,
            "habits": 25,
            "deep_work": 20,
            "nutrition_days": 15,
            "metrics_days": 15,
        },
        "habit_marks": {
            "done": ["x", "X", "✅"],
            "partial": ["~", "≈"],
            "miss": ["-", "0"],
        },
    }
    if not CONFIG_PATH.exists():
        return defaults
    try:
        import yaml  # type: ignore

        data = yaml.safe_load(CONFIG_PATH.read_text(encoding="utf-8")) or {}
    except Exception:
        # minimal YAML subset: only nested keys we need via regex / line parse
        data = _parse_simple_yaml(CONFIG_PATH.read_text(encoding="utf-8"))
    # merge
    for k, v in defaults.items():
        if k not in data:
            data[k] = v
        elif isinstance(v, dict):
            merged = dict(v)
            merged.update(data[k] or {})
            data[k] = merged
    return data


def _parse_simple_yaml(text: str) -> dict:
    """Tiny fallback when PyYAML missing."""
    out: dict = {"targets": {}, "weights": {}, "habit_marks": {}}
    section = None
    for raw in text.splitlines():
        if not raw.strip() or raw.strip().startswith("#"):
            continue
        if re.match(r"^[a-z_]+:\s*$", raw):
            section = raw.split(":")[0].strip()
            continue
        if section and raw.startswith("  ") and ":" in raw:
            key, val = raw.strip().split(":", 1)
            key, val = key.strip(), val.strip()
            if val.startswith("["):
                inner = val.strip("[]")
                items = [x.strip().strip("'\"") for x in inner.split(",") if x.strip()]
                out.setdefault(section, {})[key] = items
            else:
                try:
                    if "." in val:
                        out.setdefault(section, {})[key] = float(val)
                    else:
                        out.setdefault(section, {})[key] = int(val)
                except ValueError:
                    out.setdefault(section, {})[key] = val
    return out


def iso_week_dates(year: int, week: int) -> list[date]:
    # Monday of ISO week
    monday = date.fromisocalendar(year, week, 1)
    return [monday + timedelta(days=i) for i in range(7)]


def parse_week_arg(s: str | None) -> tuple[int, int, list[date]]:
    if not s:
        today = date.today()
        y, w, _ = today.isocalendar()
        return y, w, iso_week_dates(y, w)
    m = re.fullmatch(r"(\d{4})-W(\d{2})", s.strip())
    if not m:
        raise SystemExit(f"Bad --week {s!r}; expected YYYY-Www")
    y, w = int(m.group(1)), int(m.group(2))
    return y, w, iso_week_dates(y, w)


def fnum(s: str | None) -> float | None:
    if s is None:
        return None
    s = str(s).strip()
    if not s or s.startswith("#"):
        return None
    try:
        return float(s)
    except ValueError:
        return None


@dataclass
class WeekStats:
    avg_sleep_h: float | None
    avg_sleep_quality: float | None
    metrics_days: int
    nutrition_days: int
    deep_work_h: float
    avg_energy: float | None
    habit_ratio: float | None  # 0–1
    habit_cells: int
    habit_score_sum: float
    workouts: int
    sleep_day_scores: list[float]


def load_metrics(days: list[date]) -> tuple[list[float], list[float], int, int]:
    path = PERSONAL / "body" / "metrics.csv"
    sleep_h: list[float] = []
    quality: list[float] = []
    metrics_days = 0
    workouts = 0
    want = {d.isoformat() for d in days}
    if not path.exists():
        return sleep_h, quality, 0, 0
    with path.open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            d = (row.get("date") or "").strip()
            if d not in want:
                continue
            sh = fnum(row.get("sleep_h"))
            w = fnum(row.get("weight_kg"))
            q = fnum(row.get("sleep_quality_1_10"))
            tr = (row.get("training") or "").strip()
            if sh is not None or w is not None:
                metrics_days += 1
            if sh is not None:
                sleep_h.append(sh)
            if q is not None:
                quality.append(q)
            if tr and not tr.startswith("#"):
                workouts += 1
    return sleep_h, quality, metrics_days, workouts


def sleep_day_score(h: float | None, q: float | None, cfg: dict) -> float:
    t = cfg["targets"]
    if h is None:
        return 0.0
    in_band = t["sleep_h_min"] <= h <= t["sleep_h_max"]
    near = (t["sleep_h_min"] - 1) <= h <= (t["sleep_h_max"] + 1)
    base = 1.0 if in_band else (0.5 if near else 0.2)
    if q is not None:
        if q >= t["sleep_quality_min"]:
            return base
        if q >= t["sleep_quality_min"] - 2:
            return base * 0.75
        return base * 0.5
    return base * 0.85  # missing quality slight discount


def nutrition_days_count(days: list[date]) -> int:
    n = 0
    for d in days:
        p = PERSONAL / "nutrition" / f"{d.year}" / f"{d.isoformat()}.md"
        if p.exists():
            n += 1
    return n


def parse_deep_work_and_energy(days: list[date]) -> tuple[float, float | None]:
    total_h = 0.0
    energies: list[float] = []
    for d in days:
        p = PERSONAL / "daily" / f"{d.year}" / f"{d.isoformat()}.md"
        if not p.exists():
            continue
        text = p.read_text(encoding="utf-8", errors="ignore")
        m = re.search(r"Deep work total \(h\):\s*([0-9]+(?:\.[0-9]+)?)", text, re.I)
        if m:
            total_h += float(m.group(1))
        # Energy only from Scores table (first numeric data row after header)
        if re.search(r"##\s*Scores", text, re.I):
            section = text.split(re.search(r"##\s*Scores.*", text, re.I).group(0), 1)[-1]
            section = section.split("##", 1)[0]
            for line in section.splitlines():
                if not line.strip().startswith("|"):
                    continue
                if re.search(r"Energy|---", line):
                    continue
                cells = [c.strip() for c in line.strip().strip("|").split("|")]
                if cells and fnum(cells[0]) is not None:
                    energies.append(float(cells[0]))
                    break
    avg_e = sum(energies) / len(energies) if energies else None
    return total_h, avg_e


def parse_habits(days: list[date], cfg: dict) -> tuple[float, int, float]:
    """Return ratio 0-1, cell count, score sum."""
    done = set(cfg["habit_marks"]["done"])
    partial = set(cfg["habit_marks"]["partial"])
    # group by month file
    by_month: dict[str, list[date]] = {}
    for d in days:
        key = f"{d.year:04d}-{d.month:02d}"
        by_month.setdefault(key, []).append(d)

    score_sum = 0.0
    cells = 0
    for ym, ds in by_month.items():
        path = PERSONAL / "habits" / f"{ym}.md"
        if not path.exists():
            continue
        lines = path.read_text(encoding="utf-8", errors="ignore").splitlines()
        grid: dict[int, list[str]] = {}
        for line in lines:
            m = re.match(r"^\|\s*(\d{1,2})\s*\|(.+)\|$", line.strip())
            if not m:
                continue
            day_n = int(m.group(1))
            rest = m.group(2)
            marks = [c.strip() for c in rest.split("|")]
            # drop trailing empty from ending |
            grid[day_n] = marks
        for d in ds:
            marks = grid.get(d.day)
            if not marks:
                continue
            for mark in marks:
                if mark == "":
                    continue  # future / not filled — skip from denominator
                cells += 1
                if mark in done:
                    score_sum += 1.0
                elif mark in partial:
                    score_sum += 0.5
                else:
                    score_sum += 0.0
    ratio = (score_sum / cells) if cells else None
    return ratio if ratio is not None else 0.0, cells, score_sum


def compute_score(stats: WeekStats, cfg: dict) -> dict[str, float]:
    w = cfg["weights"]
    t = cfg["targets"]

    sleep_part = 0.0
    if stats.sleep_day_scores:
        sleep_part = (sum(stats.sleep_day_scores) / 7.0) * w["sleep"]
    # average of day scores over 7 days (missing=0 already in list length?)
    # We stored only days with data in sleep_day_scores via padding below

    habit_part = (stats.habit_ratio or 0.0) * w["habits"]
    dw_ratio = min(1.0, stats.deep_work_h / float(t["deep_work_h_week"])) if t["deep_work_h_week"] else 0
    deep_part = dw_ratio * w["deep_work"]
    nutri_part = min(1.0, stats.nutrition_days / 7.0) * w["nutrition_days"]
    metrics_part = min(1.0, stats.metrics_days / 7.0) * w["metrics_days"]

    parts = {
        "sleep": round(sleep_part, 1),
        "habits": round(habit_part, 1),
        "deep_work": round(deep_part, 1),
        "nutrition_days": round(nutri_part, 1),
        "metrics_days": round(metrics_part, 1),
    }
    parts["total"] = round(sum(parts.values()), 1)
    return parts


def band(score: float) -> str:
    if score >= 85:
        return "Strong week"
    if score >= 70:
        return "Solid"
    if score >= 50:
        return "Needs focus"
    return "Reset week"


def build_stats(days: list[date], cfg: dict) -> WeekStats:
    sleep_h, quality, metrics_days, workouts = load_metrics(days)
    # per-day sleep scores (align by reading CSV again for simplicity)
    path = PERSONAL / "body" / "metrics.csv"
    by_date: dict[str, tuple[float | None, float | None]] = {}
    if path.exists():
        with path.open(encoding="utf-8", newline="") as f:
            for row in csv.DictReader(f):
                by_date[(row.get("date") or "").strip()] = (
                    fnum(row.get("sleep_h")),
                    fnum(row.get("sleep_quality_1_10")),
                )
    day_scores = []
    for d in days:
        sh, q = by_date.get(d.isoformat(), (None, None))
        day_scores.append(sleep_day_score(sh, q, cfg))

    nutri = nutrition_days_count(days)
    deep_h, avg_e = parse_deep_work_and_energy(days)
    habit_ratio, habit_cells, habit_sum = parse_habits(days, cfg)

    return WeekStats(
        avg_sleep_h=(sum(sleep_h) / len(sleep_h)) if sleep_h else None,
        avg_sleep_quality=(sum(quality) / len(quality)) if quality else None,
        metrics_days=metrics_days,
        nutrition_days=nutri,
        deep_work_h=deep_h,
        avg_energy=avg_e,
        habit_ratio=habit_ratio if habit_cells else None,
        habit_cells=habit_cells,
        habit_score_sum=habit_sum,
        workouts=workouts,
        sleep_day_scores=day_scores,
    )


def render(year: int, week: int, days: list[date], stats: WeekStats, parts: dict, cfg: dict) -> str:
    def fmt(x: float | None, nd: int = 1) -> str:
        return "—" if x is None else f"{x:.{nd}f}"

    label = band(parts["total"])
    lines = [
        f"## Lifestyle score (auto)",
        "",
        f"**Week:** {year}-W{week:02d} · **Range:** {days[0].isoformat()} -> {days[6].isoformat()}",
        "",
        f"| Component | Points | Max |",
        f"| --- | ---: | ---: |",
        f"| Sleep | {parts['sleep']} | {cfg['weights']['sleep']} |",
        f"| Habits | {parts['habits']} | {cfg['weights']['habits']} |",
        f"| Deep work | {parts['deep_work']} | {cfg['weights']['deep_work']} |",
        f"| Nutrition days | {parts['nutrition_days']} | {cfg['weights']['nutrition_days']} |",
        f"| Metrics days | {parts['metrics_days']} | {cfg['weights']['metrics_days']} |",
        f"| **Total** | **{parts['total']}** | **100** |",
        "",
        f"**Band:** {label}",
        "",
        "### Raw inputs",
        f"- Avg sleep (h): {fmt(stats.avg_sleep_h)} · quality: {fmt(stats.avg_sleep_quality)}",
        f"- Deep work (h): {fmt(stats.deep_work_h)} / target {cfg['targets']['deep_work_h_week']}",
        f"- Nutrition files: {stats.nutrition_days}/7 · Metrics rows: {stats.metrics_days}/7",
        f"- Habits: {fmt(stats.habit_ratio, 2)} of marked cells ({stats.habit_cells} cells) · Workouts logged: {stats.workouts}",
        f"- Avg energy (from daily): {fmt(stats.avg_energy)}",
        "",
        f"_Generated by `scripts/personal_week_summary.py` · rubric [`personal/SCORE.md`](../../SCORE.md)_",
        "",
    ]
    return "\n".join(lines)


def write_into_weekly(year: int, week: int, block: str) -> Path:
    path = PERSONAL / "weekly" / f"{year}" / f"{year}-W{week:02d}.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    marker_start = "<!-- lifestyle-score:start -->"
    marker_end = "<!-- lifestyle-score:end -->"
    section = f"{marker_start}\n{block.strip()}\n{marker_end}\n"
    if path.exists():
        text = path.read_text(encoding="utf-8")
        if marker_start in text and marker_end in text:
            text = re.sub(
                re.escape(marker_start) + r".*?" + re.escape(marker_end),
                section.strip(),
                text,
                count=1,
                flags=re.S,
            )
        else:
            text = text.rstrip() + "\n\n" + section
        path.write_text(text, encoding="utf-8", newline="\n")
    else:
        header = f"# Weekly personal review — {year}-W{week:02d}\n\n"
        path.write_text(header + section, encoding="utf-8", newline="\n")
    return path


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--week", help="ISO week YYYY-Www (default: current)")
    ap.add_argument("--write", action="store_true", help="Upsert into personal/weekly/…")
    args = ap.parse_args()

    cfg = load_config()
    year, week, days = parse_week_arg(args.week)
    stats = build_stats(days, cfg)
    # pad sleep scores: already 7 entries
    parts = compute_score(stats, cfg)
    # fix sleep_part to use average of 7 day_scores
    w = cfg["weights"]["sleep"]
    parts["sleep"] = round((sum(stats.sleep_day_scores) / 7.0) * w, 1)
    parts["total"] = round(
        parts["sleep"]
        + parts["habits"]
        + parts["deep_work"]
        + parts["nutrition_days"]
        + parts["metrics_days"],
        1,
    )

    md = render(year, week, days, stats, parts, cfg)
    if args.write:
        out = write_into_weekly(year, week, md)
        print(f"Wrote score block -> {out.relative_to(ROOT)}")
    try:
        sys.stdout.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]
    except Exception:
        pass
    print(md)
    return 0


if __name__ == "__main__":
    sys.exit(main())
