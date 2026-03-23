---
title: "Client Ops Checklist for Game Freelancers"
description: "Checklist vận hành khách hàng từ onboarding → delivery → gia hạn retainer cho freelance Game Dev."
tags:
  - freelance
  - operations
  - game-dev
updated: 2026-03-23
---

# 🧾 Client Ops Checklist (Game Freelance)

> **Goal:** Biến khách freelance thành retainer ổn định bằng quy trình rõ ràng, tránh scope creep và cashflow delay.
> **Deliverables:** CRM sheet, onboarding form, SOW template, invoice tracker, renewal script.

## 1. Pipeline Overview

| Stage | Purpose | Key Artifacts |
|-------|---------|---------------|
| Lead Intake | Qualified lead, nhu cầu cụ thể | Lead form, discovery notes |
| Proposal / SOW | Khóa scope, timeline, giá | `SOW_vX.docx`, proposal deck |
| Kickoff | Align expectation, milestone | Kickoff agenda, project workspace |
| Delivery | Build & ship, report | Weekly update email, milestone demo |
| Closure | Final invoice, retro | Offboarding doc, testimonial request |
| Renewal | Upsell tiếp tục | Retainer options, roadmap |

## 2. Lead Intake Checklist
- [ ] Capture thông tin trong CRM (Airtable/Notion): company, contact, budget, timeline.
- [ ] Discovery call (30’): xác định pain point, tech stack, success metric.
- [ ] Send follow-up email recap + next steps trong 12h.

## 3. Proposal & SOW
- [ ] Draft Scope of Work: deliverables, timeline, assumptions, out-of-scope.
- [ ] Pricing model: fixed fee vs milestone vs retainer.
- [ ] Payment terms: 50/50, net 15, late fee 5%/month.
- [ ] Legal: NDA, IP ownership, kill fee clause.

### Template Snippet
```
Deliverables:
1. Multiplayer prototype (Unity, Mirror)
2. Backend API integration (PlayFab)

Timeline:
Week 1: Architecture & network layer
Week 2: Gameplay loop + UI
Week 3: QA + handoff

Payment:
50% upfront, 50% on delivery. Late fee 5% after 10 days.
```

## 4. Kickoff Ritual
- [ ] Agenda gửi trước: goals, scope, stakeholders, communication.
- [ ] Create shared workspace (Notion/Trello) + invite client.
- [ ] Define RACI (Responsible, Accountable, etc.).
- [ ] Confirm channel chính: Slack/Email, response SLA (≤24h).

## 5. Delivery Cadence
- [ ] Weekly update email (status, blockers, next steps).
- [ ] Loom demo khi có build mới.
- [ ] Track scope changes -> change request doc + cost.
- [ ] Maintain source control (GitHub private repo) + access rules.
- [ ] Backup assets (GDrive/Dropbox) sau mỗi milestone.

### Weekly Update Template
```
Subject: [Project] - Week 2 Update

✅ Completed: networked inventory sync, UI polish
⚠️ Blockers: awaiting art assets for battle pass
🎯 Next: implement leaderboard + QA
📎 Links: Build v0.3, GitHub PRs, Loom demo
```

## 6. Finance & Compliance
- [ ] Invoice via Wave/Zoho → include bank/PayPal/Wise details.
- [ ] Track payments (Notion/Sheet). Follow up nếu >3 ngày trễ.
- [ ] Generate receipt khi nhận tiền (PDF).
- [ ] File tax record (invoice, contract) mỗi tháng.

## 7. Offboarding + Renewal
- [ ] Deliver final package (code, docs, credentials).
- [ ] Conduct retro call (what went well, improvements).
- [ ] Request testimonial + LinkedIn recommendation.
- [ ] Present roadmap đề xuất (Phase 2, LiveOps support, optimization).
- [ ] Offer retainer tiers:
  - Tier A: 20h/month support ($1k)
  - Tier B: 40h/month + LiveOps on-call ($2k)

## 8. Tooling Stack
- CRM: Notion, HubSpot free
- Contracts: PandaDoc, DocuSign
- Payments: Wise, Payoneer, Stripe Atlas
- Project Mgmt: Linear, ClickUp
- Automation: Zapier (intake form → Notion)

## 9. Checklist Summary
- [ ] Lead captured + discovery notes
- [ ] SOW signed + deposit received
- [ ] Kickoff meeting completed
- [ ] Weekly updates sent đúng hạn
- [ ] Deliverables approved
- [ ] Final invoice paid
- [ ] Testimonial collected
- [ ] Renewal/retainer pitched

## 🔗 References
- [Freelance Guide](./game-dev-freelance-guide.md)
- [Remote Game Dev Guide](./remote-game-dev-guide.md)
- [Templates/Contractor SOW](../../../templates/career/contractor-sow.md)