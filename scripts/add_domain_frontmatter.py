#!/usr/bin/env python3
"""Add/normalize frontmatter on domains/*/README.md."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "domains"

META = {
    "ai-ml": {
        "title": "Artificial Intelligence & Machine Learning Roadmap",
        "description": "ML, DL, NLP, CV, generative AI, agents, and MLOps curriculum hub",
        "tags": ["ai", "ml", "roadmap"],
        "related": ["../../challenges/ai-ml/README.md", "../README.md"],
    },
    "backend-dev": {
        "title": "Backend Development Roadmap",
        "description": "API, database, architecture, security, and labs for backend engineers",
        "tags": ["backend", "api", "roadmap"],
        "related": ["INDEX.md", "../../challenges/backend/README.md", "../README.md"],
    },
    "blockchain": {
        "title": "Blockchain Knowledge Base",
        "description": "Smart contracts, DeFi, MEV, staking, and blockchain security hub",
        "tags": ["blockchain", "web3", "roadmap"],
        "related": ["../../challenges/blockchain/README.md", "../README.md"],
    },
    "business-analytics": {
        "title": "Business Analytics & BI Roadmap",
        "description": "Metrics, experimentation, BI, and trading-oriented analytics hub",
        "tags": ["business-analytics", "bi", "roadmap"],
        "related": ["../../challenges/business-analytics/README.md", "../README.md"],
    },
    "data-analytics": {
        "title": "Data Analytics Domain",
        "description": "SQL, BI, and business-focused analytics curriculum hub",
        "tags": ["data-analytics", "sql", "roadmap"],
        "related": ["../../challenges/data-analytics/README.md", "../README.md"],
    },
    "data-science": {
        "title": "Data Science & Big Data Engineering Roadmap",
        "description": "Lakehouse, Spark, pipelines, and applied data science hub",
        "tags": ["data-science", "lakehouse", "roadmap"],
        "related": ["../../challenges/data-science/README.md", "../README.md"],
    },
    "devops-sre": {
        "title": "DevOps & Site Reliability Engineering Roadmap",
        "description": "K8s, IaC, CI/CD, and reliability practices for mid+ engineers",
        "tags": ["devops", "sre", "roadmap"],
        "related": ["../../challenges/devops-sre/README.md", "../README.md"],
    },
    "dsa": {
        "title": "Data Structures & Algorithms Roadmap",
        "description": "DSA and interview-oriented algorithms practice hub",
        "tags": ["dsa", "algorithms", "roadmap"],
        "related": ["../../challenges/dsa/README.md", "../README.md"],
    },
    "game-dev": {
        "title": "Game Development Roadmap (Unity Focus)",
        "description": "Unity/C#, gameplay, multiplayer, and portfolio tech track hub",
        "tags": ["unity", "game-dev", "roadmap"],
        "related": [
            "../../challenges/game-dev/README.md",
            "../../guides/03-career-skills/game-dev/README.md",
            "../README.md",
        ],
    },
    "iot": {
        "title": "Internet of Things (IoT) Roadmap",
        "description": "Embedded, networking, cloud, edge, and IoT security hub",
        "tags": ["iot", "embedded", "roadmap"],
        "related": ["../../challenges/iot/README.md", "../README.md"],
    },
    "mmo-engineering": {
        "title": "MMO Engineering Playbook",
        "description": "Automation, proxy, anti-detect with risk/ethics guidance",
        "tags": ["mmo", "automation", "roadmap"],
        "related": ["../../challenges/mmo-engineering/README.md", "../README.md"],
    },
    "mobile-dev": {
        "title": "Mobile App Development Roadmap",
        "description": "iOS, Android, and cross-platform mobile curriculum hub",
        "tags": ["mobile", "ios", "android", "roadmap"],
        "related": ["../../challenges/mobile/README.md", "../README.md"],
    },
    "network-security": {
        "title": "Network & Security Roadmap",
        "description": "Foundations through offense/defense security curriculum hub",
        "tags": ["security", "network", "roadmap"],
        "related": ["../../challenges/security/README.md", "../README.md"],
    },
    "system-design": {
        "title": "System Design & Architecture",
        "description": "Scalability and interview-oriented system design deep-dives hub",
        "tags": ["system-design", "architecture", "roadmap"],
        "related": ["../../challenges/system-design/README.md", "../README.md"],
    },
    "web-dev": {
        "title": "Web Development Roadmap (Fullstack Focus)",
        "description": "Frontend/fullstack web curriculum with Next/React focus",
        "tags": ["web", "frontend", "roadmap"],
        "related": ["../../challenges/web-ui/README.md", "../README.md"],
    },
}


def render_fm(m: dict) -> str:
    tags = ", ".join(m["tags"])
    related = "\n".join(f"  - {r}" for r in m["related"])
    return (
        "---\n"
        f'title: "{m["title"]}"\n'
        f'description: "{m["description"]}"\n'
        'updated: "2026-08-07"\n'
        "canonical: true\n"
        f"tags: [{tags}]\n"
        "audience: [beginner, intermediate, advanced]\n"
        "related:\n"
        f"{related}\n"
        "sensitivity: public\n"
        "---\n\n"
    )


def strip_frontmatter(text: str) -> str:
    s = text.lstrip("\ufeff")
    if not s.startswith("---"):
        return text
    rest = s[3:]
    end = rest.find("\n---")
    if end == -1:
        return text
    body = rest[end + 4 :]
    return body.lstrip("\n")


def main() -> int:
    updated = []
    for name, m in META.items():
        path = ROOT / name / "README.md"
        if not path.exists():
            print(f"MISSING {path}")
            return 1
        body = strip_frontmatter(path.read_text(encoding="utf-8"))
        path.write_text(render_fm(m) + body, encoding="utf-8", newline="\n")
        updated.append(name)
    print(f"OK — frontmatter on {len(updated)} domain READMEs")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
