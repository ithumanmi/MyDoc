"""Config for Telegram Docs bot."""
from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parent
load_dotenv(ROOT / ".env")

DOCS_ROOT = Path(os.getenv("DOCS_ROOT", ROOT.parent.parent)).resolve()
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "").strip()
ALLOWED_IDS = {
    int(x.strip())
    for x in os.getenv("TELEGRAM_ALLOWED_USER_IDS", "").split(",")
    if x.strip().isdigit()
}

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "").strip()
OPENAI_BASE_URL = os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1").rstrip("/")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini").strip()

MAX_FILES = int(os.getenv("MAX_FILES", "6"))
MAX_CHARS_PER_FILE = int(os.getenv("MAX_CHARS_PER_FILE", "4000"))
MAX_CONTEXT_CHARS = int(os.getenv("MAX_CONTEXT_CHARS", "18000"))
ALLOW_PERSONAL = os.getenv("ALLOW_PERSONAL", "0").strip() in {"1", "true", "TRUE", "yes"}

CATALOG_PATH = DOCS_ROOT / "meta" / "catalog" / "topics.yaml"
AGENTS_PATH = DOCS_ROOT / "AGENTS.md"


def validate() -> list[str]:
    errs: list[str] = []
    if not TELEGRAM_BOT_TOKEN:
        errs.append("TELEGRAM_BOT_TOKEN missing")
    if not ALLOWED_IDS:
        errs.append("TELEGRAM_ALLOWED_USER_IDS empty — bot would deny everyone")
    if not OPENAI_API_KEY:
        errs.append("OPENAI_API_KEY missing")
    if not DOCS_ROOT.is_dir():
        errs.append(f"DOCS_ROOT not a directory: {DOCS_ROOT}")
    if not CATALOG_PATH.is_file():
        errs.append(f"catalog missing: {CATALOG_PATH}")
    return errs
