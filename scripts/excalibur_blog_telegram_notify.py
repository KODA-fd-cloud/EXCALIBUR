#!/usr/bin/env python3
"""Telegram topic approval for Excalibur BLOG.

Flow:
  tick (по расписанию) → всегда исходящее сообщение
  ok  → «Принято, пишу…» → pipeline → «Опубликовано» + URL
  нет → следующая тема, пока не ok
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PENDING = ROOT / "memory" / "topics" / "pending-approval.json"
TOPICS = ROOT / "memory" / "topics" / "blog-topics.md"
PUBLISHED = ROOT / "shared" / "published-articles.md"
OFFSET_FILE = ROOT / "memory" / "topics" / "telegram-updates.offset"


def load_dotenv_local() -> None:
    path = ROOT / "memory" / "site.env.local"
    if not path.is_file():
        return
    raw = path.read_bytes()
    text = None
    for enc in ("utf-8-sig", "utf-8", "cp1251"):
        try:
            text = raw.decode(enc)
            break
        except UnicodeDecodeError:
            continue
    if text is None:
        text = raw.decode("utf-8", errors="replace")
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, val = line.partition("=")
        os.environ.setdefault(key.strip(), val.strip().strip('"').strip("'"))


def require_creds() -> tuple[str, str]:
    token = os.environ.get("TELEGRAM_BOT_TOKEN", "").strip()
    chat_id = os.environ.get("TELEGRAM_CHAT_ID", "").strip()
    if not token or not chat_id:
        print("❌ TELEGRAM_BOT_TOKEN / TELEGRAM_CHAT_ID missing", file=sys.stderr)
        sys.exit(2)
    return token, chat_id


def api(token: str, method: str, payload: dict | None = None) -> dict:
    url = f"https://api.telegram.org/bot{token}/{method}"
    data = None
    headers = {}
    if payload is not None:
        data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        headers["Content-Type"] = "application/json; charset=utf-8"
    req = urllib.request.Request(url, data=data, headers=headers, method="POST" if data else "GET")
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        raise SystemExit(f"❌ Telegram API {method}: HTTP {e.code} {body}") from e


def send_text(token: str, chat_id: str, text: str) -> dict:
    r = api(token, "sendMessage", {"chat_id": chat_id, "text": text})
    if not r.get("ok"):
        raise SystemExit(f"❌ send failed: {r}")
    return r["result"]


def load_pending() -> dict | None:
    if not PENDING.is_file():
        return None
    return json.loads(PENDING.read_text(encoding="utf-8"))


def save_pending(pending: dict) -> None:
    PENDING.parent.mkdir(parents=True, exist_ok=True)
    PENDING.write_text(json.dumps(pending, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def read_offset() -> int:
    if OFFSET_FILE.is_file():
        try:
            return int(OFFSET_FILE.read_text(encoding="utf-8").strip() or "0")
        except ValueError:
            return 0
    return int(os.environ.get("TELEGRAM_UPDATES_OFFSET", "0") or 0)


def write_offset(value: int) -> None:
    OFFSET_FILE.parent.mkdir(parents=True, exist_ok=True)
    OFFSET_FILE.write_text(str(value) + "\n", encoding="utf-8")


def published_ids_and_slugs() -> tuple[set[str], set[str]]:
    ids: set[str] = set()
    slugs: set[str] = set()
    if not PUBLISHED.is_file():
        return ids, slugs
    for line in PUBLISHED.read_text(encoding="utf-8").splitlines():
        if not line.startswith("|") or "topic_id" in line or re.match(r"^\|\s*-+", line):
            continue
        parts = [p.strip() for p in line.strip("|").split("|")]
        if len(parts) < 3:
            continue
        ids.add(parts[1].upper())
        slugs.add(parts[2].lower())
    if TOPICS.is_file():
        m = re.search(r"Уже на блоге[^\n]*:\s*(.+)", TOPICS.read_text(encoding="utf-8"))
        if m:
            for slug in re.split(r"[,\s]+", m.group(1)):
                slug = slug.strip().rstrip(",")
                if slug:
                    slugs.add(slug.lower())
    return ids, slugs


def parse_topics() -> list[dict]:
    if not TOPICS.is_file():
        return []
    text = TOPICS.read_text(encoding="utf-8")
    topics: list[dict] = []
    blocks = re.split(r"(?m)^##\s+(B\d+)\s+[—-]\s+", text)
    for i in range(1, len(blocks), 2):
        topic_id = blocks[i].strip().upper()
        body = blocks[i + 1] if i + 1 < len(blocks) else ""
        slug_m = re.search(r"\*\*slug:\*\*\s*(\S+)", body)
        h1_m = re.search(r"\*\*h1:\*\*\s*(.+)", body)
        pri_m = re.search(r"\*\*priority:\*\*\s*(\S+)", body)
        topics.append(
            {
                "topic_id": topic_id,
                "slug": (slug_m.group(1).strip() if slug_m else ""),
                "h1": (h1_m.group(1).strip() if h1_m else topic_id),
                "priority": (pri_m.group(1).strip().upper() if pri_m else "P1"),
            }
        )
    return topics


def next_topic(*, skip_ids: set[str] | None = None) -> dict | None:
    skip_ids = {x.upper() for x in (skip_ids or set())}
    pub_ids, pub_slugs = published_ids_and_slugs()
    skip_ids |= pub_ids
    pending = load_pending()
    rejected = set(pending.get("rejected_ids", []) if pending else [])
    skip_ids |= {x.upper() for x in rejected}
    candidates = []
    for t in parse_topics():
        if t["topic_id"] in skip_ids:
            continue
        if t["slug"] and t["slug"].lower() in pub_slugs:
            continue
        candidates.append(t)
    candidates.sort(key=lambda t: (0 if t["priority"] == "P0" else 1, t["topic_id"]))
    return candidates[0] if candidates else None


def normalize_reply(text: str) -> str:
    t = text.strip().lower().replace("ё", "е")
    if t in {"ok", "ок", "да", "yes", "+", "👍", "✅"}:
        return "approve"
    if t in {"net", "нет", "no", "-", "👎", "❌", "skip"}:
        return "reject"
    return "unknown"


def propose_topic(token: str, chat_id: str, topic: dict, *, rejected_ids: list[str] | None = None) -> dict:
    text = (
        f"📝 Тема на согласование (КОДА блог)\n\n"
        f"ID: {topic['topic_id']}\n"
        f"H1: {topic['h1']}\n"
        + (f"Slug: {topic['slug']}\n" if topic.get("slug") else "")
        + "\nОтветь одним словом:\n"
        "• ок — пишем и публикуем\n"
        "• нет — сразу пришлю следующую тему"
    )
    result = send_text(token, chat_id, text)
    pending = {
        "topic_id": topic["topic_id"],
        "h1": topic["h1"],
        "slug": topic.get("slug", ""),
        "status": "pending",
        "proposed_at": int(result["date"]),
        "proposal_message_id": result["message_id"],
        "chat_id": str(chat_id),
        "rejected_ids": rejected_ids or [],
    }
    save_pending(pending)
    return pending


def effective_proposed_at(pending: dict) -> int:
    now = int(time.time())
    ts = int(pending.get("proposed_at") or 0)
    if ts <= 0 or ts > now + 600:
        return now - 30 * 86400
    return ts


def remind_pending(token: str, chat_id: str, pending: dict) -> dict:
    text = (
        f"⏰ Напоминание — тема ждёт решения\n\n"
        f"ID: {pending.get('topic_id')}\n"
        f"H1: {pending.get('h1')}\n"
        + (f"Slug: {pending.get('slug')}\n" if pending.get("slug") else "")
        + "\nОтветь одним словом: ок / нет"
    )
    result = send_text(token, chat_id, text)
    pending["status"] = "pending"
    pending["proposed_at"] = int(result["date"])
    pending["proposal_message_id"] = result["message_id"]
    save_pending(pending)
    return pending


def apply_decision(token: str, chat_id: str, pending: dict, decision: str) -> dict:
    out: dict = {"decision": decision, "topic_id": pending.get("topic_id")}
    if decision == "approve":
        result = send_text(
            token,
            chat_id,
            f"✅ Принято, пишу…\n\n{pending['topic_id']}: {pending.get('h1', '')}\n"
            f"Пришлю ссылку, когда статья будет на сайте.",
        )
        pending["status"] = "writing"
        pending["ack_message_id"] = result["message_id"]
        save_pending(pending)
        out["status"] = "writing"
        out["ack_message_id"] = result["message_id"]
        return out

    if decision == "reject":
        rejected = list(pending.get("rejected_ids") or [])
        if pending["topic_id"] not in rejected:
            rejected.append(pending["topic_id"])
        send_text(token, chat_id, f"⏭ Ок, пропускаю {pending['topic_id']}. Сразу следующая тема:")
        topic = next_topic(skip_ids=set(rejected))
        if not topic:
            send_text(
                token,
                chat_id,
                "📭 Очередь пуста. В следующем слоте Scout сам дозаправит актуальными темами (web + cannibalization guard).",
            )
            pending["status"] = "rejected"
            pending["rejected_ids"] = rejected
            save_pending(pending)
            out["status"] = "rejected"
            out["next"] = None
            return out
        new_pending = propose_topic(token, chat_id, topic, rejected_ids=rejected)
        out["status"] = "pending"
        out["decision"] = "reject_then_next"
        out["next"] = {
            "topic_id": new_pending["topic_id"],
            "h1": new_pending["h1"],
            "slug": new_pending.get("slug", ""),
        }
        out["topic_id"] = new_pending["topic_id"]
        return out

    out["status"] = pending.get("status")
    return out


def _poll_once(token: str, chat_id: str, pending: dict, *, timeout: int = 0) -> tuple[str, str | None, int]:
    offset = read_offset()
    r = api(
        token,
        "getUpdates",
        {"offset": offset, "timeout": timeout, "allowed_updates": ["message"]},
    )
    if not r.get("ok"):
        raise SystemExit(f"❌ getUpdates failed: {r}")

    decision = "pending"
    matched = None
    max_id = offset - 1
    min_date = effective_proposed_at(pending)
    proposal_mid = pending.get("proposal_message_id")

    for upd in r.get("result", []):
        max_id = max(max_id, int(upd["update_id"]))
        msg = upd.get("message") or {}
        if str(msg.get("chat", {}).get("id")) != str(chat_id):
            continue
        reply_to = (msg.get("reply_to_message") or {}).get("message_id")
        if int(msg.get("date", 0)) < min_date and reply_to != proposal_mid:
            continue
        text = msg.get("text") or ""
        d = normalize_reply(text)
        if d == "unknown":
            continue
        decision = d
        matched = text
        write_offset(int(upd["update_id"]) + 1)
        break
    else:
        if max_id >= offset:
            write_offset(max_id + 1)
    return decision, matched, max_id


def cmd_send(args: argparse.Namespace) -> None:
    token, chat_id = require_creds()
    text = args.text
    if args.file:
        text = Path(args.file).read_text(encoding="utf-8")
    if not text.strip():
        raise SystemExit("❌ empty message")
    result = send_text(token, chat_id, text)
    print(json.dumps({"ok": True, "message_id": result["message_id"]}, ensure_ascii=False))


def cmd_propose(args: argparse.Namespace) -> None:
    token, chat_id = require_creds()
    if args.auto or not args.topic_id:
        topic = next_topic()
        if not topic:
            send_text(
                token,
                chat_id,
                "📭 Очередь карточек пуста. Новые темы — только из blog-topics.md (дозаправка / Scout), не «из воздуха».",
            )
            print(json.dumps({"ok": False, "reason": "empty_queue"}, ensure_ascii=False))
            return
    else:
        topic = {
            "topic_id": args.topic_id.strip().upper(),
            "h1": args.h1.strip(),
            "slug": (args.slug or "").strip(),
        }
        if not topic["h1"]:
            for t in parse_topics():
                if t["topic_id"] == topic["topic_id"]:
                    topic["h1"] = t["h1"]
                    topic["slug"] = topic["slug"] or t["slug"]
                    break
            if not topic["h1"]:
                raise SystemExit("❌ --h1 required if topic not in blog-topics.md")
    pending = propose_topic(token, chat_id, topic)
    print(json.dumps({"ok": True, "pending": str(PENDING), **pending}, ensure_ascii=False))


def cmd_next(args: argparse.Namespace) -> None:
    token, chat_id = require_creds()
    pending = load_pending() or {}
    rejected = list(pending.get("rejected_ids") or [])
    if pending.get("topic_id") and pending.get("status") in {"pending", "rejected", "writing"}:
        if pending["topic_id"] not in rejected:
            rejected.append(pending["topic_id"])
    topic = next_topic(skip_ids=set(rejected))
    if not topic:
        send_text(
            token,
            chat_id,
            "📭 Очередь карточек пуста. Бот предлагает только темы из blog-topics.md — "
            "новые карточки нужно дозаправить (Scout / B24+).",
        )
        print(json.dumps({"ok": False, "reason": "empty_queue"}, ensure_ascii=False))
        return
    pending = propose_topic(token, chat_id, topic, rejected_ids=rejected)
    print(json.dumps({"ok": True, **pending}, ensure_ascii=False))


def cmd_tick(args: argparse.Namespace) -> None:
    """Scheduled entrypoint — never silent: propose, remind, or continue pipeline."""
    token, chat_id = require_creds()
    pending = load_pending()

    if pending and pending.get("status") == "pending":
        now = int(time.time())
        if int(pending.get("proposed_at") or 0) > now + 600:
            pending["proposed_at"] = now - 3600
            save_pending(pending)

    if pending and pending.get("status") == "writing":
        print(
            json.dumps(
                {
                    "ok": True,
                    "action": "continue_pipeline",
                    "decision": "approve",
                    "status": "writing",
                    "topic_id": pending.get("topic_id"),
                    "h1": pending.get("h1"),
                    "slug": pending.get("slug"),
                },
                ensure_ascii=False,
            )
        )
        return

    if pending and pending.get("status") == "pending":
        decision, matched, _ = _poll_once(token, chat_id, pending, timeout=0)
        if decision in {"approve", "reject"}:
            out = apply_decision(token, chat_id, pending, decision)
            out["ok"] = True
            out["matched_text"] = matched
            out["action"] = "handled_reply"
            print(json.dumps(out, ensure_ascii=False))
            return
        pending = remind_pending(token, chat_id, pending)
        print(
            json.dumps(
                {
                    "ok": True,
                    "action": "reminded",
                    "decision": "pending",
                    "status": "pending",
                    "topic_id": pending.get("topic_id"),
                    "h1": pending.get("h1"),
                    "slug": pending.get("slug"),
                },
                ensure_ascii=False,
            )
        )
        return

    topic = next_topic()
    if not topic:
        send_text(
            token,
            chat_id,
            "📭 Очередь карточек пуста.\n"
            "Я не придумываю темы на лету — только шлю следующую из blog-topics.md.\n"
            "Очередь пуста — Scout дозаправит в следующем cron (или: python scripts/excalibur_blog_scout_ci.py --force --notify).",
        )
        print(json.dumps({"ok": False, "action": "empty_queue"}, ensure_ascii=False))
        return
    pending = propose_topic(token, chat_id, topic)
    print(
        json.dumps(
            {
                "ok": True,
                "action": "proposed",
                "decision": "pending",
                "status": "pending",
                "topic_id": pending["topic_id"],
                "h1": pending["h1"],
                "slug": pending.get("slug", ""),
            },
            ensure_ascii=False,
        )
    )


def cmd_poll(args: argparse.Namespace) -> None:
    token, chat_id = require_creds()
    pending = load_pending()
    if not pending:
        print(json.dumps({"ok": True, "decision": "none", "reason": "no_pending"}, ensure_ascii=False))
        return
    if pending.get("status") != "pending":
        print(json.dumps({"ok": True, "decision": pending.get("status"), "pending": pending}, ensure_ascii=False))
        return
    decision, matched, _ = _poll_once(token, chat_id, pending, timeout=0)
    out: dict = {
        "ok": True,
        "decision": decision,
        "matched_text": matched,
        "topic_id": pending.get("topic_id"),
        "status": pending.get("status"),
    }
    if args.ack and decision in {"approve", "reject"}:
        out.update(apply_decision(token, chat_id, pending, decision))
    print(json.dumps(out, ensure_ascii=False))


def cmd_await(args: argparse.Namespace) -> None:
    token, chat_id = require_creds()
    pending = load_pending()
    if not pending or pending.get("status") != "pending":
        topic = next_topic()
        if not topic:
            print(json.dumps({"ok": False, "reason": "empty_queue"}, ensure_ascii=False))
            return
        pending = propose_topic(token, chat_id, topic)

    deadline = time.time() + args.timeout_sec
    skips = 0
    while time.time() < deadline:
        decision, matched, _ = _poll_once(token, chat_id, pending, timeout=min(25, args.timeout_sec))
        if decision == "approve":
            out = apply_decision(token, chat_id, pending, decision)
            print(json.dumps({"ok": True, "matched_text": matched, "h1": pending.get("h1"), "slug": pending.get("slug"), **out}, ensure_ascii=False))
            return
        if decision == "reject":
            skips += 1
            if skips > args.max_skips:
                send_text(token, chat_id, "⏹ Слишком много «нет» подряд. Остановлюсь до следующего слота.")
                print(json.dumps({"ok": False, "reason": "max_skips", "skips": skips}, ensure_ascii=False))
                return
            out = apply_decision(token, chat_id, pending, decision)
            if out.get("status") == "rejected":
                print(json.dumps({"ok": False, "reason": "empty_queue", **out}, ensure_ascii=False))
                return
            pending = load_pending() or pending
            continue
    print(json.dumps({"ok": True, "decision": "timeout", "topic_id": pending.get("topic_id")}, ensure_ascii=False))


def cmd_ack(args: argparse.Namespace) -> None:
    token, chat_id = require_creds()
    pending = load_pending() or {}
    topic_id = (args.topic_id or pending.get("topic_id") or "").strip().upper()
    h1 = (args.h1 or pending.get("h1") or "").strip()
    result = send_text(
        token,
        chat_id,
        f"✅ Принято, пишу…\n\n{topic_id}: {h1}\nПришлю ссылку, когда статья будет на сайте.",
    )
    if pending:
        pending["status"] = "writing"
        pending["ack_message_id"] = result["message_id"]
        save_pending(pending)
    print(json.dumps({"ok": True, "message_id": result["message_id"]}, ensure_ascii=False))


def cmd_published(args: argparse.Namespace) -> None:
    token, chat_id = require_creds()
    pending = load_pending() or {}
    topic_id = (args.topic_id or pending.get("topic_id") or "").strip().upper()
    h1 = (args.h1 or pending.get("h1") or "").strip()
    url = args.url.strip()
    if not url:
        raise SystemExit("❌ --url required")
    result = send_text(token, chat_id, f"🚀 Опубликовано\n\n{topic_id}: {h1}\n{url}")
    if pending:
        pending["status"] = "published"
        pending["published_url"] = url
        pending["published_message_id"] = result["message_id"]
        pending["rejected_ids"] = []
        save_pending(pending)
    print(json.dumps({"ok": True, "message_id": result["message_id"], "url": url}, ensure_ascii=False))


def cmd_resolve(args: argparse.Namespace) -> None:
    pending = load_pending()
    if not pending:
        raise SystemExit("❌ no pending file")
    pending["status"] = args.status
    save_pending(pending)
    print(json.dumps({"ok": True, "pending": pending}, ensure_ascii=False))


def main() -> None:
    load_dotenv_local()
    if hasattr(sys.stdout, "reconfigure"):
        try:
            sys.stdout.reconfigure(encoding="utf-8")
            sys.stderr.reconfigure(encoding="utf-8")
        except Exception:
            pass

    p = argparse.ArgumentParser(description="Excalibur BLOG Telegram approval helpers")
    sub = p.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("send")
    s.add_argument("--text", default="")
    s.add_argument("--file")
    s.set_defaults(func=cmd_send)

    s = sub.add_parser("propose")
    s.add_argument("--topic-id", default="")
    s.add_argument("--h1", default="")
    s.add_argument("--slug", default="")
    s.add_argument("--auto", action="store_true")
    s.set_defaults(func=cmd_propose)

    s = sub.add_parser("next")
    s.set_defaults(func=cmd_next)

    s = sub.add_parser("tick", help="Scheduled slot: propose / remind / handle ok|нет")
    s.set_defaults(func=cmd_tick)

    s = sub.add_parser("poll")
    s.add_argument("--ack", action="store_true")
    s.set_defaults(func=cmd_poll)

    s = sub.add_parser("await")
    s.add_argument("--timeout-sec", type=int, default=900)
    s.add_argument("--max-skips", type=int, default=20)
    s.set_defaults(func=cmd_await)

    s = sub.add_parser("ack")
    s.add_argument("--topic-id", default="")
    s.add_argument("--h1", default="")
    s.set_defaults(func=cmd_ack)

    s = sub.add_parser("published")
    s.add_argument("--url", required=True)
    s.add_argument("--topic-id", default="")
    s.add_argument("--h1", default="")
    s.set_defaults(func=cmd_published)

    s = sub.add_parser("resolve")
    s.add_argument("--status", required=True, choices=["approved", "rejected", "pending", "cleared", "writing", "published"])
    s.set_defaults(func=cmd_resolve)

    args = p.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
