# Telegram Docs Bot

Ask your local **Docs** markdown corpus via Telegram — retrieval follows `AGENTS.md` / `meta/catalog/topics.yaml` (not a blind full-folder dump).

## What it does

1. You send a message on Telegram.
2. Bot checks your user id against `TELEGRAM_ALLOWED_USER_IDS`.
3. Retriever picks canonical + related paths from the catalog (+ light filename / heading match).
4. Reads those files (chunk-budgeted), calls an OpenAI-compatible chat API.
5. Replies with an answer that should **cite repo paths**.

`personal/` is **excluded by default**. Set `ALLOW_PERSONAL=1` only if you accept private logs in the bot context.

## Setup (Windows)

```powershell
cd c:\Projects\Docs\scripts\telegram-docs-bot
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
copy .env.example .env
# edit .env — token, user id, API key
python bot.py
```

### Telegram

1. Talk to [@BotFather](https://t.me/BotFather) → `/newbot` → copy token.
2. Message your bot once, then open `https://api.telegram.org/bot<TOKEN>/getUpdates` and read `message.from.id` → put in `TELEGRAM_ALLOWED_USER_IDS`.

### LLM

Any OpenAI-compatible endpoint:

| Provider | `OPENAI_BASE_URL` | Notes |
| --- | --- | --- |
| OpenAI | (default) | `OPENAI_API_KEY` |
| OpenRouter | `https://openrouter.ai/api/v1` | set model e.g. `openai/gpt-4o-mini` |
| Local (Ollama) | `http://localhost:11434/v1` | `OPENAI_API_KEY=ollama`, model e.g. `llama3.2` |

## Commands

| Command | Meaning |
| --- | --- |
| `/start` | help |
| `/ping` | health |
| (any text) | ask Docs |

## Privacy

- Whitelist only — strangers get ignored / denied.
- Do not commit `.env`.
- Prefer excluding `personal/` unless you need life-log Q&A.

## Limits (scaffold)

- No vector DB yet (catalog + keyword; good enough with your routing files).
- Long answers may hit Telegram 4096-char limit (bot splits).
- Process must stay running (or use Task Scheduler / a VPS later).

## Optional next steps

- Embeddings + Chroma for semantic search.
- Webhook + Cloudflare/Fly instead of long-polling.
- Hook `/week` → `scripts/personal_week_summary.py` (personal OS).
