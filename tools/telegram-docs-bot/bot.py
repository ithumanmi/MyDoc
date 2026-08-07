"""Telegram entrypoint — long polling."""
from __future__ import annotations

import asyncio
import logging
import sys

from telegram import Update
from telegram.constants import ChatAction, ParseMode
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

import config
from answer import ask

logging.basicConfig(
    format="%(asctime)s %(levelname)s %(name)s %(message)s",
    level=logging.INFO,
)
log = logging.getLogger("telegram-docs-bot")

TG_MAX = 4000


def _allowed(update: Update) -> bool:
    user = update.effective_user
    return bool(user and user.id in config.ALLOWED_IDS)


async def cmd_start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not _allowed(update):
        await update.message.reply_text("Unauthorized.")
        return
    await update.message.reply_text(
        "Docs bot sẵn sàng.\n"
        "Gửi câu hỏi về knowledge trong repo (guides/domains/meta…).\n"
        f"personal/ hiện: {'BẬT' if config.ALLOW_PERSONAL else 'TẮT'}.\n"
        "Lệnh: /ping"
    )


async def cmd_ping(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not _allowed(update):
        await update.message.reply_text("Unauthorized.")
        return
    await update.message.reply_text(f"pong · docs={config.DOCS_ROOT.name} · model={config.OPENAI_MODEL}")


def _split(text: str) -> list[str]:
    if len(text) <= TG_MAX:
        return [text]
    parts: list[str] = []
    buf = text
    while buf:
        parts.append(buf[:TG_MAX])
        buf = buf[TG_MAX:]
    return parts


async def on_text(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not update.message or not update.message.text:
        return
    if not _allowed(update):
        await update.message.reply_text("Unauthorized.")
        return

    q = update.message.text.strip()
    if not q:
        return

    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
    try:
        # Run sync OpenAI + file IO off the event loop
        answer, _chunks = await asyncio.to_thread(ask, q)
    except Exception as e:
        log.exception("ask failed")
        await update.message.reply_text(f"Lỗi khi trả lời: {e}")
        return

    for part in _split(answer):
        try:
            await update.message.reply_text(part, disable_web_page_preview=True)
        except Exception:
            await update.message.reply_text(part)


def main() -> None:
    errs = config.validate()
    if errs:
        for e in errs:
            log.error("config: %s", e)
        sys.exit(1)

    log.info("DOCS_ROOT=%s ALLOW_PERSONAL=%s users=%s", config.DOCS_ROOT, config.ALLOW_PERSONAL, config.ALLOWED_IDS)
    app = Application.builder().token(config.TELEGRAM_BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", cmd_start))
    app.add_handler(CommandHandler("ping", cmd_ping))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, on_text))
    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
