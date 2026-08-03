#!/usr/bin/env python3
"""After Telegram ok: kick article generation if html missing.

Paths:
1) CURSOR_API_KEY → Cursor Cloud Agent (full Excalibur write+cover)
2) else → mark queued_write, notify once (no spam)

GHA calls this before finish_approved.
"""
from __future__ import annotations

import json
import os
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from excalibur_blog_finish_approved import find_article_dir, qa_pass  # noqa: E402
from excalibur_blog_telegram_notify import (  # noqa: E402
    load_dotenv_local,
    load_pending,
    require_creds,
    save_pending,
    send_text,
)


def launch_cursor_write(topic_id: str, h1: str, slug: str) -> dict:
    from cursor_sdk import Agent, AgentOptions, CloudAgentOptions, CloudRepository  # type: ignore

    api_key = os.environ.get("CURSOR_API_KEY", "").strip()
    if not api_key:
        raise RuntimeError("CURSOR_API_KEY missing")

    prompt = f"""Ты оркестратор Excalibur BLOG в репо KODA-fd-cloud/EXCALIBUR.

Тема утверждена в Telegram:
- topic_id: {topic_id}
- h1: {h1}
- slug: {slug}

Сделай полный прогон для ЭТОЙ темы:
1) Прочитай AGENTS.md, shared/editorial-utility-only.md, memory/brief/conversion-map.md, карточку в memory/topics/blog-topics.md
2) Создай memory/blog/articles/{topic_id}-{slug}/ с article.html + article.meta.json + article-qa.md (verdict: PASS)
3) Обложка: abstract holographic CGI 16:9, БЕЗ текста/букв/watermark на картинке (как legacy gradient_abstract). Сохрани cover/cover.png + cover-registry.json. Можно Cursor GenerateImage / MCP; НЕ рисуй Montserrat-текст поверх.
4) git add/commit/push в master: "feat(blog): write {topic_id} {slug}"
5) В конце JSON: {{"topic_id","slug","article_dir","cover":true}}

Запрещено: salebot, emdash, article_mode A, публикация без cover.png.
"""

    result = Agent.prompt(
        prompt,
        AgentOptions(
            api_key=api_key,
            model="composer-2.5",
            cloud=CloudAgentOptions(
                repos=[
                    CloudRepository(
                        url="https://github.com/KODA-fd-cloud/EXCALIBUR",
                        starting_ref="master",
                    )
                ],
                auto_create_pr=False,
            ),
        ),
    )
    return {"status": getattr(result, "status", None), "result": getattr(result, "result", str(result))}


def main() -> int:
    load_dotenv_local()
    pending = load_pending()
    if not pending or pending.get("status") not in {"writing", "queued_write"}:
        print(json.dumps({"ok": True, "action": "skip", "reason": "not_in_write_queue"}, ensure_ascii=False))
        return 0

    topic_id = str(pending.get("topic_id") or "").upper()
    h1 = str(pending.get("h1") or "")
    slug = str(pending.get("slug") or "")
    token, chat_id = require_creds()

    article_dir = find_article_dir(topic_id)
    if article_dir and qa_pass(article_dir) and (article_dir / "cover" / "cover.png").is_file():
        pending["status"] = "writing"
        save_pending(pending)
        print(json.dumps({"ok": True, "action": "ready", "topic_id": topic_id, "dir": article_dir.name}, ensure_ascii=False))
        return 0

    # Already kicked a cloud write recently → don't spam / re-launch
    kicked = int(pending.get("write_job_started_at") or 0)
    if kicked and time.time() - kicked < 6 * 3600:
        print(
            json.dumps(
                {
                    "ok": True,
                    "action": "wait_write_job",
                    "topic_id": topic_id,
                    "started_at": kicked,
                },
                ensure_ascii=False,
            )
        )
        return 0

    if os.environ.get("CURSOR_API_KEY", "").strip():
        try:
            if not pending.get("write_launch_notified"):
                send_text(
                    token,
                    chat_id,
                    f"✍️ {topic_id}: запускаю Cloud Agent на написание статьи + обложку.\n"
                    f"Это не мгновенно. Ссылку пришлю после publish.",
                )
                pending["write_launch_notified"] = True
            pending["status"] = "queued_write"
            pending["write_job_started_at"] = int(time.time())
            pending["missing_article_notified"] = True
            save_pending(pending)
            out = launch_cursor_write(topic_id, h1, slug)
            print(json.dumps({"ok": True, "action": "cursor_write_started", "topic_id": topic_id, "cursor": out}, ensure_ascii=False, default=str))
            return 0
        except Exception as e:
            print(f"cursor write failed: {e}", file=sys.stderr)

    # No writer available — queue once, stop lying/spamming
    pending["status"] = "queued_write"
    if not pending.get("missing_article_notified"):
        send_text(
            token,
            chat_id,
            f"📥 {topic_id}: «ок» в очереди на написание.\n"
            f"Автопубликация ждёт готовые article.html + QA PASS + cover.png в репо.\n"
            f"GHA сам статьи не пишет (нет writer), пока нет CURSOR_API_KEY или ручного прогона.\n"
            f"H1: {h1}",
        )
        pending["missing_article_notified"] = True
    save_pending(pending)
    print(json.dumps({"ok": False, "action": "queued_write", "topic_id": topic_id}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
