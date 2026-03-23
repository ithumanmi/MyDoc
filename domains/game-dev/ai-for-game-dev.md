---
title: "AI for Game Development"
description: "AI-assisted content creation, procedural dialogue, NPC LLM integration 2024-2026."
tags:
  - game-dev
  - ai
updated: 2026-03-11
---

# 🤖 AI for Game Development (2024-2026)

## 1) AI-assisted Content Creation
- Texture/material generation (Stable Diffusion, SDXL, Adobe Firefly) → cần pipeline kiểm duyệt IP.
- Animation retargeting bằng ML (DeepMotion, RAD Gravity). Export FBX/clip trực tiếp.
- Level blockout bằng generative layout (Promethean AI, Luma).

## 2) Procedural Dialogue & Narrative
- LLM hỗ trợ branching dialogue: prompt = quest state + persona.
- Tools: Inworld AI, Charisma.ai, Convai.
- Guardrails: RAG với lore document, profanity filter, fallback scripted lines.

## 3) NPCs dùng LLM
- Architecture:
  - Memory store (vector DB) lưu lịch sử, personality.
  - Planning layer (GOAP + LLM) -> action.
  - Voice: TTS real-time (ElevenLabs) + lip sync.
- Latency target <1s: preload response template, streaming token.

### GenAI NPC System Blueprint (2026)

| Layer | Component | Notes |
|-------|-----------|-------|
| Prompt Orchestration | System prompt + lore context + player state | Sử dụng RAG (quest journal, relationship) + guardrail prompt |
| State Memory | Vector DB (Qdrant/Weaviate) + short-term buffer | TTL cho short-term (5 phút) tránh quá tải |
| Planner | Utility AI/GOAP kế hoạch hành động, LLM chỉ viết thoại | Ép LLM trả về JSON `{"emotion": "angry", "line": "..."}` |
| Safety | Profanity filter, toxicity classifier, fallback line | Khi LLM timeout → fallback script |
| Runtime Integration | Unity `NPCDialogueService` (Task-based, cancellation token) | Hiển thị typing indicator, voice layering |
| Hosting | Local (Ollama, LM Studio) hoặc Managed API (Inworld, Convai) | Local cần GPU 3090+, on-premise để giảm cost |

**Performance targets:** response < 1.2s, bandwidth < 15KB/s (text) hoặc 48kbps (voice). Cache persona/prompt tokens để giảm chi phí.

**Telemetry:** log `llm_latency_ms`, `fallback_rate`, `token_usage` → push vào [Unity Impact Metrics](./production/metrics/unity-impact-metrics.md).

### Labs đề xuất
- **Lab 9: Local LLM NPC Quest Giver** – Unity ↔ Ollama streaming, state machine fallback. (xem `labs/lab-local-llm-npc.md`).
- **Lab 10: Emotion-aware NPC** – blendshape/lip-sync driven by LLM emotion JSON.

## 4) AI-assisted Workflow
- Designer prompt → Unity Editor tool tạo prefab/layout.
- AI Code Copilot cho gameplay scripts (GitHub Copilot, Cursor).
- QA bot: playtest automation + bug triage.

## 5) Risks & Compliance
- Copyright/IP: lưu metadata nguồn asset.
- Rating/Trust & Safety: filter output.
- Cost: token usage, GPU hosting.

## ✅ Apply it
- [ ] Chọn use-case -> PoC (dialogue, level tool... ).
- [ ] Thiết kế guardrail/prompts với RAG.
- [ ] Đánh giá latency/cost (self-host vs API).
- [ ] Đào tạo team sử dụng tool + policy IP.