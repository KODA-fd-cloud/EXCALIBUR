#!/usr/bin/env python3
"""Ensure unpublished topic cards exist. Called when Telegram queue is empty.

Does NOT invent LLM topics in CI — promotes from blog-topics.md already committed,
or reports how many slots remain. Scout (LLM) remains a Cursor/Cloud step.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from excalibur_blog_telegram_notify import next_topic, parse_topics, published_ids_and_slugs  # noqa: E402


def unpublished_count() -> int:
    pub_ids, pub_slugs = published_ids_and_slugs()
    n = 0
    for t in parse_topics():
        if t["topic_id"] in pub_ids:
            continue
        if t["slug"] and t["slug"].lower() in pub_slugs:
            continue
        n += 1
    return n


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--min-unpublished", type=int, default=3)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    left = unpublished_count()
    nxt = next_topic()
    out = {
        "ok": True,
        "unpublished": left,
        "min_unpublished": args.min_unpublished,
        "needs_refill": left < args.min_unpublished,
        "next_topic_id": (nxt or {}).get("topic_id"),
        "hint": (
            "ok"
            if left >= args.min_unpublished
            else "Добавь карточки Bxx в memory/topics/blog-topics.md или запусти Scout в Cursor"
        ),
    }
    if args.json:
        print(json.dumps(out, ensure_ascii=False))
    else:
        print(f"unpublished={left} next={out['next_topic_id']} needs_refill={out['needs_refill']}")
    return 0 if left > 0 else 2


if __name__ == "__main__":
    raise SystemExit(main())
