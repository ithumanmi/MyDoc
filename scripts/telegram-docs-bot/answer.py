"""LLM answer grounded in retrieved Docs chunks."""
from __future__ import annotations

from openai import OpenAI

from config import OPENAI_API_KEY, OPENAI_BASE_URL, OPENAI_MODEL
from retrieve import Chunk, format_context, retrieve

SYSTEM = """You are a retrieval assistant for a personal Docs knowledge repo.
Rules:
- Answer in the user's language (Vietnamese if they wrote Vietnamese).
- Use ONLY the provided SOURCE excerpts. If insufficient, say what is missing and suggest a path to open.
- Cite markdown paths like `guides/.../file.md` inline.
- Do not invent lab values, medical diagnoses, or facts not in sources.
- Treat personal/ lifestyle records as private; do not speculate about the owner's health.
- Prefer actionable, concise answers (bullet points OK).
"""


def ask(query: str) -> tuple[str, list[Chunk]]:
    chunks = retrieve(query)
    if not chunks:
        return (
            "Không tìm thấy nguồn phù hợp trong catalog/routing. "
            "Thử hỏi cụ thể hơn (vd. “core loop game”, “stoicism daily”, “bond presence”).",
            [],
        )

    client = OpenAI(api_key=OPENAI_API_KEY, base_url=OPENAI_BASE_URL)
    context = format_context(chunks)
    user = f"Question:\n{query}\n\nSources:\n{context}"
    resp = client.chat.completions.create(
        model=OPENAI_MODEL,
        messages=[
            {"role": "system", "content": SYSTEM},
            {"role": "user", "content": user},
        ],
        temperature=0.2,
    )
    text = (resp.choices[0].message.content or "").strip()
    cites = ", ".join(c.path for c in chunks)
    footer = f"\n\n_Sources used: {cites}_"
    return text + footer, chunks
