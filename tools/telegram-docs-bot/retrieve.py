"""Catalog-first retrieval over Docs markdown."""
from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

import yaml

from config import (
    ALLOW_PERSONAL,
    CATALOG_PATH,
    DOCS_ROOT,
    MAX_CHARS_PER_FILE,
    MAX_CONTEXT_CHARS,
    MAX_FILES,
)


@dataclass
class Chunk:
    path: str
    text: str
    score: float


def _load_catalog() -> list[dict]:
    data = yaml.safe_load(CATALOG_PATH.read_text(encoding="utf-8")) or {}
    return list(data.get("topics") or [])


def _norm(s: str) -> str:
    return re.sub(r"\s+", " ", s.lower()).strip()


def _tokens(q: str) -> set[str]:
    return {t for t in re.split(r"[^\w+#./-]+", _norm(q)) if len(t) >= 2}


def _allowed_path(rel: str) -> bool:
    rel = rel.replace("\\", "/").lstrip("./")
    if rel.startswith("personal/") and not ALLOW_PERSONAL:
        return False
    return True


def _score_topic(query: str, topic: dict) -> float:
    q = _norm(query)
    qt = _tokens(query)
    score = 0.0
    tid = _norm(str(topic.get("id", "")))
    if tid and tid in q:
        score += 8
    for part in tid.split("."):
        if part and part in qt:
            score += 2
    for alias in topic.get("aliases") or []:
        a = _norm(str(alias))
        if not a:
            continue
        if a in q:
            score += 10
        else:
            at = _tokens(a)
            overlap = len(qt & at)
            if overlap:
                score += overlap * 1.5
    canon = _norm(str(topic.get("canonical", "")))
    for part in Path(canon).parts:
        p = _norm(part.replace(".md", ""))
        if p and p in qt:
            score += 1.2
    return score


def _pick_paths(query: str) -> list[tuple[str, float]]:
    topics = _load_catalog()
    ranked: list[tuple[float, dict]] = []
    for t in topics:
        s = _score_topic(query, t)
        if s > 0:
            ranked.append((s, t))
    ranked.sort(key=lambda x: x[0], reverse=True)

    paths: dict[str, float] = {}
    for s, t in ranked[:8]:
        canon = str(t.get("canonical") or "").replace("\\", "/")
        if canon and _allowed_path(canon):
            paths[canon] = max(paths.get(canon, 0), s + 5)
        for rel in t.get("related") or []:
            r = str(rel).replace("\\", "/")
            if r and _allowed_path(r):
                paths[r] = max(paths.get(r, 0), s)

    # Filename / path token boost across a shallow walk of key trees
    qt = _tokens(query)
    roots = ["guides", "domains", "meta", "chapters", "templates"]
    if ALLOW_PERSONAL:
        roots.append("personal")
    for root_name in roots:
        root = DOCS_ROOT / root_name
        if not root.is_dir():
            continue
        for p in root.rglob("*.md"):
            rel = str(p.relative_to(DOCS_ROOT)).replace("\\", "/")
            if not _allowed_path(rel):
                continue
            name_tokens = _tokens(p.stem.replace("-", " ") + " " + rel)
            overlap = len(qt & name_tokens)
            if overlap >= 2 or (overlap == 1 and len(next(iter(qt & name_tokens), "")) >= 5):
                paths[rel] = max(paths.get(rel, 0), overlap * 2.0)

    # Always include AGENTS + routing lightly when asking about repo
    if any(k in _norm(query) for k in ("repo", "docs", "điều hướng", "routing", "agents")):
        for extra in ("AGENTS.md", "meta/routing.md", "OVERVIEW.md"):
            if _allowed_path(extra):
                paths[extra] = max(paths.get(extra, 0), 3.0)

    ordered = sorted(paths.items(), key=lambda x: x[1], reverse=True)
    return ordered[:MAX_FILES]


def _read_excerpt(abs_path: Path, budget: int) -> str:
    try:
        raw = abs_path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return ""
    # Prefer title + first headings chunk
    if len(raw) <= budget:
        return raw
    head = raw[: budget // 2]
    # try keep a ## section mentioning little
    return head + "\n\n…[truncated]…\n"


def retrieve(query: str) -> list[Chunk]:
    picks = _pick_paths(query)
    chunks: list[Chunk] = []
    used = 0
    for rel, score in picks:
        abs_path = DOCS_ROOT / rel
        if not abs_path.is_file():
            continue
        room = min(MAX_CHARS_PER_FILE, MAX_CONTEXT_CHARS - used)
        if room < 400:
            break
        text = _read_excerpt(abs_path, room)
        if not text.strip():
            continue
        chunks.append(Chunk(path=rel, text=text, score=score))
        used += len(text)
    return chunks


def format_context(chunks: list[Chunk]) -> str:
    parts = []
    for c in chunks:
        parts.append(f"### SOURCE: {c.path}\n{c.text}")
    return "\n\n---\n\n".join(parts)
