#!/usr/bin/env python3
"""After Telegram ok (pending status=writing): publish ready article or report blocker.

Used by GitHub Actions so ┬л╨Я╤А╨╕╨╜╤П╤В╨╛, ╨┐╨╕╤И╤ГтАж┬╗ is followed by a real URL.
"""
from __future__ import annotations

import json
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from excalibur_blog_docker_publish import publish_via_docker  # noqa: E402
from excalibur_blog_telegram_notify import (  # noqa: E402
    load_dotenv_local,
    load_pending,
    next_topic,
    propose_topic,
    require_creds,
    save_pending,
    send_text,
)
from excalibur_blog_wp_publish import load_article, load_env  # noqa: E402

PENDING = ROOT / "memory" / "topics" / "pending-approval.json"
PUBLISHED = ROOT / "shared" / "published-articles.md"
ARTICLES = ROOT / "memory" / "blog" / "articles"


def find_article_dir(topic_id: str) -> Path | None:
    topic_id = topic_id.upper()
    matches = sorted(ARTICLES.glob(f"{topic_id}-*"), key=lambda p: p.name)
    for d in matches:
        if (d / "article.html").is_file() and (d / "article.meta.json").is_file():
            return d
    return None


def qa_pass(article_dir: Path) -> bool:
    qa = article_dir / "article-qa.md"
    if not qa.is_file():
        return False
    text = qa.read_text(encoding="utf-8")
    return bool(re.search(r"(?im)^verdict:\s*PASS\b", text))


def append_ledger(topic_id: str, slug: str, url: str) -> None:
    if not PUBLISHED.is_file():
        return
    text = PUBLISHED.read_text(encoding="utf-8")
    if slug in text:
        return
    row = f"| {date.today().isoformat()} | {topic_id} | {slug} | {url} | published |"
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if line.startswith("|------"):
            lines.insert(i + 1, row)
            break
    PUBLISHED.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    load_dotenv_local()
    pending = load_pending()
    if not pending or pending.get("status") not in {"writing", "queued_write"}:
        print(json.dumps({"ok": True, "action": "skip", "reason": "not_writing"}, ensure_ascii=False))
        return 0

    topic_id = str(pending.get("topic_id") or "").upper()
    h1 = str(pending.get("h1") or "")
    slug = str(pending.get("slug") or "")
    token, chat_id = require_creds()
    env = load_env(ROOT)

    article_dir = find_article_dir(topic_id)
    if article_dir is None:
        # Do NOT spam Telegram every 15 min тАФ write_approved owns the one-shot notice.
        pending["status"] = "queued_write"
        save_pending(pending)
        # exit 0 тАФ ╨╕╨╜╨░╤З╨╡ GHA ╤Б set -e ╨║╤А╨░╤Б╨╜╤Л╨╣ ╨║╨░╨╢╨┤╤Л╨╡ 15 ╨╝╨╕╨╜ ╨┐╤А╨╕ ╨╛╤З╨╡╤А╨╡╨┤╨╕ ╨╜╨░ ╨╜╨░╨┐╨╕╤Б╨░╨╜╨╕╨╡
        print(json.dumps({"ok": False, "action": "missing_article", "topic_id": topic_id}, ensure_ascii=False))
        return 0

    if not qa_pass(article_dir):
        if not pending.get("qa_fail_notified"):
            send_text(
                token,
                chat_id,
                f"тЪая╕П {topic_id}: ╤Б╤В╨░╤В╤М╤П ╨╡╤Б╤В╤М, ╨╜╨╛ GEO QA ╨╜╨╡ PASS тАФ ╨┐╤Г╨▒╨╗╨╕╨║╨░╤Ж╨╕╤О ╨┐╤А╨╛╨┐╤Г╤Б╨║╨░╤О.\n"
                f"╨Я╨░╨┐╨║╨░: {article_dir.name}",
            )
            pending["qa_fail_notified"] = True
            save_pending(pending)
        print(json.dumps({"ok": False, "action": "qa_not_pass", "topic_id": topic_id, "dir": article_dir.name}, ensure_ascii=False))
        return 3

    cover_png = article_dir / "cover" / "cover.png"
    if not cover_png.is_file():
        if not pending.get("missing_cover_notified"):
            send_text(
                token,
                chat_id,
                f"тЪая╕П {topic_id}: ╤Б╤В╨░╤В╤М╤П ╨╡╤Б╤В╤М, ╨╜╨╛ ╨╜╨╡╤В ╨╛╨▒╨╗╨╛╨╢╨║╨╕ cover/cover.png тАФ ╨▒╨╡╨╖ ╨╜╨╡╤С ╨╜╨╡ ╨┐╤Г╨▒╨╗╨╕╨║╤Г╤О.",
            )
            pending["missing_cover_notified"] = True
            save_pending(pending)
        print(json.dumps({"ok": False, "action": "missing_cover", "topic_id": topic_id}, ensure_ascii=False))
        return 7

    if env.get("EXCALIBUR_BLOG_ALLOW_PUBLISH", "").strip().lower() != "yes":
        send_text(token, chat_id, "тЭМ ╨Я╤Г╨▒╨╗╨╕╨║╨░╤Ж╨╕╤П ╨╖╨░╨▒╨╗╨╛╨║╨╕╤А╨╛╨▓╨░╨╜╨░: EXCALIBUR_BLOG_ALLOW_PUBLISH != yes")
        print(json.dumps({"ok": False, "action": "publish_blocked"}, ensure_ascii=False))
        return 4

    send_text(token, chat_id, f"тП│ {topic_id}: ╤Б╤В╨░╤В╤М╤П ╨│╨╛╤В╨╛╨▓╨░, ╨┐╤Г╨▒╨╗╨╕╨║╤Г╤О ╨╜╨░ ╤Б╨░╨╣╤ВтАж")

    try:
        out = publish_via_docker(article_dir, env)
    except Exception as e:
        send_text(token, chat_id, f"тЭМ {topic_id}: ╨┐╤Г╨▒╨╗╨╕╨║╨░╤Ж╨╕╤П ╤Г╨┐╨░╨╗╨░: {e}")
        print(json.dumps({"ok": False, "action": "publish_error", "error": str(e)}, ensure_ascii=False))
        return 5

    payload = load_article(article_dir)
    permalink = ""
    for line in out.splitlines():
        if line.startswith("permalink="):
            permalink = line.split("=", 1)[1].strip()
    if not permalink:
        base = (env.get("PUBLIC_SITE_URL") or "https://koda-fd.ru/blog").rstrip("/")
        permalink = f"{base}/{payload['slug']}/"

    result = {
        "slug": payload["slug"],
        "topic_id": payload.get("topic_id") or topic_id,
        "permalink": permalink,
        "raw_output": out,
        "verdict": "pass" if "OK post=" in out else "fail",
        "method": "ssh_docker_exec",
    }
    (article_dir / "wp-publish-result.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    if result["verdict"] != "pass":
        send_text(token, chat_id, f"тЭМ {topic_id}: publish ╨╜╨╡ ╨▓╨╡╤А╨╜╤Г╨╗ OK post=\n{out[:500]}")
        print(json.dumps({"ok": False, "action": "publish_fail", "out": out[:1000]}, ensure_ascii=False))
        return 6

    append_ledger(topic_id, payload["slug"], permalink)
    rejected = list(pending.get("rejected_ids") or [])
    pending["status"] = "published"
    pending["published_url"] = permalink
    # Keep rejected_ids тАФ ╨╕╨╜╨░╤З╨╡ ╨┐╨╛╤Б╨╗╨╡ publish ╤Б╨╜╨╛╨▓╨░ ╨┐╤А╨╡╨┤╨╗╨╛╨╢╨╕╤В ╤В╨╡╨╝╤Л, ╨║╨╛╤В╨╛╤А╤Л╨╡ ╤Г╨╢╨╡ ┬л╨╜╨╡╤В┬╗
    pending["rejected_ids"] = rejected
    save_pending(pending)

    send_text(token, chat_id, f"ЁЯЪА ╨Ю╨┐╤Г╨▒╨╗╨╕╨║╨╛╨▓╨░╨╜╨╛\n\n{topic_id}: {h1 or payload.get('h1', '')}\n{permalink}")

    # Immediately propose next topic so queue doesn't stall until next cron
    nxt = next_topic(skip_ids={topic_id})
    if nxt:
        propose_topic(token, chat_id, nxt, rejected_ids=rejected)
        action_next = "proposed_next"
    else:
        send_text(
            token,
            chat_id,
            "ЁЯУн ╨Я╨╛╤Б╨╗╨╡ ╨┐╤Г╨▒╨╗╨╕╨║╨░╤Ж╨╕╨╕ ╨╛╤З╨╡╤А╨╡╨┤╤М ╨║╨░╤А╤В╨╛╤З╨╡╨║ ╨┐╤Г╤Б╤В╨░.\n"
            "╨С╨╛╤В ╨╜╨╡ ╨│╨╡╨╜╨╡╤А╨╕╤А╤Г╨╡╤В ╤В╨╡╨╝╤Л ╤Б╨░╨╝ тАФ ╤В╨╛╨╗╤М╨║╨╛ ╨┐╤А╨╡╨┤╨╗╨░╨│╨░╨╡╤В ╨╕╨╖ blog-topics.md.\n"
            "╨Ф╨╛╨╖╨░╨┐╤А╨░╨▓╤М Bxx ╨╕╨╗╨╕ ╨╖╨░╨┐╤Г╤Б╤В╨╕ Scout.",
        )
        action_next = "queue_empty"

    print(
        json.dumps(
            {
                "ok": True,
                "action": "published",
                "topic_id": topic_id,
                "url": permalink,
                "next": action_next,
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
