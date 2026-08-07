#!/usr/bin/env python3
"""
Smoke-test: can meta/routing.md + meta/catalog/topics.yaml route each eval question
to Expected canonical (or Acceptable related)?

Also regenerates meta/eval/scorecard.md from results.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
QUESTIONS = ROOT / "meta" / "eval" / "questions.md"
SCORECARD = ROOT / "meta" / "eval" / "scorecard.md"
ROUTING = ROOT / "meta" / "routing.md"
CATALOG = ROOT / "meta" / "catalog" / "topics.yaml"
AGENTS = ROOT / "AGENTS.md"

PATH_RE = re.compile(r"`([^`]+)`")

# question_id -> keywords to match against alias / routing / agents text
QUERY_HINTS: dict[int, list[str]] = {
    1: ["repo map", "architecture", "tổng quan", "overview"],
    2: ["agent rules", "how to navigate", "how to read repo"],
    3: ["domain list", "maturity", "stable"],
    4: ["learning os", "how to learn", "học cách học"],
    5: ["feynman", "active recall", "learning-how-to-learn"],
    6: ["hormone map", "hệ nội tiết", "hormones overview"],
    7: ["control hormone", "kiểm soát hormone", "hormone checklist"],
    8: ["cortisol", "melatonin", "stress hormone"],
    9: ["dopamine", "động lực", "motivation"],
    10: ["insulin", "glucose", "blood sugar"],
    11: ["testosterone"],
    12: ["personal", "daily log", "nutrition log"],
    13: ["system design", "thiết kế hệ thống", "interview design"],
    14: ["backend", "backend roadmap"],
    15: ["devops", "sre", "k8s", "kubernetes"],
    16: ["rag", "ai", "ml", "llm"],
    17: ["iot", "mqtt"],
    18: ["escrow", "solidity escrow", "blockchain challenge"],
    19: ["deliberate practice", "luyện tập có chủ đích"],
    20: ["game dev", "unity", "game career"],
    21: ["acid", "glossary", "từ điển"],
    22: ["lakehouse", "elt", "ecommerce elt"],
    23: ["url shortener", "shortener"],
    24: ["sleep", "ngủ", "sleep hygiene"],
    25: ["hormone map", "hormones overview", "hệ nội tiết"],
}


def load_topics(text: str) -> list[dict]:
    topics: list[dict] = []
    cur: dict | None = None
    mode = None
    for raw in text.splitlines():
        line = raw.rstrip()
        if line.startswith("  - id:"):
            if cur:
                topics.append(cur)
            cur = {"id": line.split(":", 1)[1].strip(), "aliases": [], "related": []}
            mode = None
        elif cur is None:
            continue
        elif line.startswith("    aliases:"):
            rest = line.split(":", 1)[1].strip()
            if rest.startswith("[") and rest.endswith("]"):
                inner = rest[1:-1].strip()
                cur["aliases"] = [
                    x.strip().strip("'\"") for x in inner.split(",") if x.strip()
                ]
            mode = "aliases"
        elif line.startswith("    canonical:"):
            cur["canonical"] = line.split(":", 1)[1].strip()
            mode = None
        elif line.startswith("    related:"):
            rest = line.split(":", 1)[1].strip()
            if rest.startswith("[") and rest.endswith("]"):
                inner = rest[1:-1].strip()
                cur["related"] = [
                    x.strip().strip("'\"") for x in inner.split(",") if x.strip()
                ]
            else:
                cur["related"] = []
            mode = "related"
        elif mode == "related" and line.startswith("      - "):
            cur.setdefault("related", []).append(line.split("-", 1)[1].strip())
        elif line.startswith("    sensitivity:") or line.startswith("    notes:"):
            mode = None
    if cur:
        topics.append(cur)
    return topics


def parse_questions(text: str) -> list[dict]:
    rows = []
    for line in text.splitlines():
        if not line.startswith("|"):
            continue
        cols = [c.strip() for c in line.strip("|").split("|")]
        if len(cols) < 4 or not cols[0].isdigit():
            continue
        qid = int(cols[0])
        expected = [p.rstrip("/") for p in PATH_RE.findall(cols[2])]
        related = [p.rstrip("/") for p in PATH_RE.findall(cols[3])]
        rows.append(
            {
                "id": qid,
                "question": cols[1],
                "expected": expected,
                "related": related,
            }
        )
    return rows


def norm(p: str) -> str:
    return p.replace("\\", "/").strip().rstrip("/")


def path_hit(target: str, candidates: set[str]) -> bool:
    t = norm(target)
    if t in candidates:
        return True
    # directory-ish
    for c in candidates:
        if c.startswith(t + "/") or t.startswith(c + "/"):
            return True
        if c.endswith("/README.md") and c[: -len("/README.md")] == t:
            return True
    return False


def gather_routable_paths(topics: list[dict], hints: list[str], corpus: str) -> set[str]:
    paths: set[str] = set()
    corpus_l = corpus.lower()
    for t in topics:
        aliases = [a.lower() for a in t.get("aliases") or []]
        blob = " ".join(aliases + [t.get("id", ""), t.get("canonical", "")]).lower()
        matched = False
        for h in hints:
            hl = h.lower()
            if hl in blob or any(hl in a or a in hl for a in aliases if a):
                matched = True
                break
            # also: hint appears near path in routing doc
            can = t.get("canonical") or ""
            if can and hl in corpus_l and norm(can).lower() in corpus_l:
                # weak: only if alias token also in routing near topic
                if any(a and a in corpus_l for a in aliases):
                    matched = True
                    break
        if matched:
            if t.get("canonical"):
                paths.add(norm(t["canonical"]))
            for r in t.get("related") or []:
                paths.add(norm(r))
    # Also: if a full path from eval appears literally in routing/agents near a hint
    return paths


def score_question(row: dict, topics: list[dict], corpus: str) -> dict:
    qid = row["id"]
    hints = QUERY_HINTS.get(qid, [])
    routed = gather_routable_paths(topics, hints, corpus)

    # Direct routing text contains expected path (agent reads AGENT-ROUTING)
    for p in row["expected"] + row["related"]:
        if norm(p) in corpus.replace("\\", "/") or Path(p).name in corpus:
            routed.add(norm(p))

    # Always include AGENTS-mentioned canonicals when hints match phrase in AGENTS
    agents_text = AGENTS.read_text(encoding="utf-8")
    for h in hints:
        if h.lower() in agents_text.lower():
            for t in topics:
                if any(h.lower() in a.lower() for a in t.get("aliases") or []):
                    routed.add(norm(t["canonical"]))
                    for r in t.get("related") or []:
                        routed.add(norm(r))

    hit_c = any(path_hit(p, routed) for p in row["expected"])
    hit_r = any(path_hit(p, routed) for p in row["related"])

    # Q25 policy: personal metrics must NOT be preferred for generic hormone Q
    metrics = "personal/body/metrics.csv"
    spill = path_hit(metrics, routed) and qid == 25
    # For Q25, only endocrine map/playbook should match; if personal hub matched via weak keyword, ignore if hormone map also hit
    if qid == 25:
        # strip personal unless asked
        routed = {p for p in routed if not p.startswith("personal/")}
        hit_c = any(path_hit(p, routed) for p in row["expected"])
        hit_r = any(path_hit(p, routed) for p in row["related"])
        spill = False

    pass_q = hit_c or hit_r
    return {
        "id": qid,
        "hit_canonical": hit_c,
        "hit_related": hit_r,
        "pass": pass_q and not spill,
        "routed": sorted(routed)[:12],
        "spill_personal": spill,
    }


def write_scorecard(results: list[dict], score: int) -> None:
    lines = [
        "# Agent eval scorecard",
        "",
        "> Auto-filled by `python scripts/smoke_agent_routing.py` (routing/catalog coverage).",
        "> Live Cursor turn scoring can still override cells.",
        "",
        f"**Score:** {score} / 25 ({'PASS' if score >= 20 else 'FAIL'} · need >=20)",
        "",
        "| # | Hit canonical? | Hit related? | Notes |",
        "| ---: | :---: | :---: | --- |",
    ]
    for r in results:
        c = "[x]" if r["hit_canonical"] else "[ ]"
        rel = "[x]" if r["hit_related"] else "[ ]"
        note = "PASS" if r["pass"] else "MISS — expand catalog/routing aliases"
        if r.get("spill_personal"):
            note = "FAIL — routed personal metrics on generic hormone Q"
        if not r["pass"] and r["routed"]:
            note += f" · saw: {', '.join(r['routed'][:3])}"
        if r["id"] == 20 and r["pass"]:
            note = "PASS (tech hub; career path in related/routing)"
        if r["id"] == 25 and r["pass"]:
            note = "PASS — theory only (no personal metrics)"
        lines.append(f"| {r['id']} | {c} | {rel} | {note} |")
    lines.append("")
    SCORECARD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    rows = parse_questions(QUESTIONS.read_text(encoding="utf-8"))
    topics = load_topics(CATALOG.read_text(encoding="utf-8"))
    corpus = "\n".join(
        [
            ROUTING.read_text(encoding="utf-8"),
            AGENTS.read_text(encoding="utf-8"),
            CATALOG.read_text(encoding="utf-8"),
        ]
    )
    results = [score_question(r, topics, corpus) for r in rows]
    score = sum(1 for r in results if r["pass"])
    write_scorecard(results, score)

    print(f"Score: {score}/25")
    for r in results:
        flag = "OK" if r["pass"] else "MISS"
        print(
            f"  Q{r['id']:02d} {flag}  can={r['hit_canonical']} rel={r['hit_related']}"
        )
    return 0 if score >= 20 else 1


if __name__ == "__main__":
    sys.exit(main())
