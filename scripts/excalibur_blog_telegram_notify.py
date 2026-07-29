#!/usr/bin/env python3
"""Send / poll Telegram for topic approval. Secrets from env or memory/site.env.local."""
from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PENDING = ROOT / "memory" / "topics" / "pending-approval.json"


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
        key, val = key.strip(), val.strip().strip('"').strip("'")
        os.environ.setdefault(key, val)


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
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        raise SystemExit(f"❌ Telegram API {method}: HTTP {e.code} {body}") from e


def send_text(token: str, chat_id: str, text: str, *, disable_preview: bool = False) -> dict:
    payload: dict = {"chat_id": chat_id, "text": text}
    if disable_preview:
        payload["disable_web_page_preview"] = False
    r = api(token, "sendMessage", payload)
    if not r.get("ok"):
        raise SystemExit(f"❌ send failed: {r}")
    return r["result"]


def load_pending() -> dict:
    if not PENDING.is_file():
        raise SystemExit("❌ no pending file")
    return json.loads(PENDING.read_text(encoding="utf-8"))


def save_pending(pending: dict) -> None:
    PENDING.parent.mkdir(parents=True, exist_ok=True)
    PENDING.write_text(json.dumps(pending, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


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
    topic_id = args.topic_id.strip().upper()
    h1 = args.h1.strip()
    slug = (args.slug or "").strip()
    text = (
        f"📝 Тема на согласование (КОДА блог)\n\n"
        f"ID: {topic_id}\n"
        f"H1: {h1}\n"
        + (f"Slug: {slug}\n" if slug else "")
        + "\nОтветь одним словом:\n"
        "• ок — пишем и публикуем\n"
        "• нет — пропускаем, возьму другую в следующий слот"
    )
    result = send_text(token, chat_id, text)
    pending = {
        "topic_id": topic_id,
        "h1": h1,
        "slug": slug,
        "status": "pending",
        "proposed_at": result["date"],
        "proposal_message_id": result["message_id"],
        "chat_id": str(chat_id),
    }
    save_pending(pending)
    print(json.dumps({"ok": True, "pending": str(PENDING), **pending}, ensure_ascii=False))


def normalize_reply(text: str) -> str:
    t = text.strip().lower().replace("ё", "е")
    if t in {"ok", "ок", "да", "yes", "+", "👍", "✅"}:
        return "approve"
    if t in {"net", "нет", "no", "-", "👎", "❌", "skip"}:
        return "reject"
    return "unknown"


def cmd_poll(args: argparse.Namespace) -> None:
    token, chat_id = require_creds()
    if not PENDING.is_file():
        print(json.dumps({"ok": True, "decision": "none", "reason": "no_pending"}, ensure_ascii=False))
        return
    pending = load_pending()
    if pending.get("status") != "pending":
        print(json.dumps({"ok": True, "decision": pending.get("status"), "pending": pending}, ensure_ascii=False))
        return

    offset = int(os.environ.get("TELEGRAM_UPDATES_OFFSET", "0") or 0)
    r = api(token, "getUpdates", {"offset": offset, "timeout": 0, "allowed_updates": ["message"]})
    if not r.get("ok"):
        raise SystemExit(f"❌ getUpdates failed: {r}")

    decision = "pending"
    matched_text = None
    max_update_id = offset - 1
    for upd in r.get("result", []):
        max_update_id = max(max_update_id, int(upd["update_id"]))
        msg = upd.get("message") or {}
        if str(msg.get("chat", {}).get("id")) != str(chat_id):
            continue
        if int(msg.get("date", 0)) < int(pending.get("proposed_at", 0)):
            continue
        text = msg.get("text") or ""
        d = normalize_reply(text)
        if d == "unknown":
            continue
        decision = d
        matched_text = text
        break

    ack_message_id = None
    if args.ack and decision in {"approve", "reject"}:
        topic_id = pending.get("topic_id", "")
        h1 = pending.get("h1", "")
        if decision == "approve":
            ack = (
                f"✅ Принято, пишу…\n\n"
                f"{topic_id}: {h1}\n"
                f"Пришлю ссылку, когда статья будет на сайте."
            )
            pending["status"] = "writing"
        else:
            ack = f"⏭ Ок, пропускаю {topic_id}. В следующем слоте предложу другую тему."
            pending["status"] = "rejected"
        result = send_text(token, chat_id, ack)
        ack_message_id = result["message_id"]
        pending["ack_message_id"] = ack_message_id
        save_pending(pending)

    out = {
        "ok": True,
        "decision": decision,
        "matched_text": matched_text,
        "topic_id": pending.get("topic_id"),
        "pending_path": str(PENDING),
        "status": pending.get("status"),
    }
    if max_update_id >= offset:
        out["next_offset"] = max_update_id + 1
    if ack_message_id is not None:
        out["ack_message_id"] = ack_message_id
    print(json.dumps(out, ensure_ascii=False))


def cmd_ack(args: argparse.Namespace) -> None:
    """Explicit «Принято, пишу…» (if poll wasn't run with --ack)."""
    token, chat_id = require_creds()
    pending = load_pending() if PENDING.is_file() else {}
    topic_id = (args.topic_id or pending.get("topic_id") or "").strip().upper()
    h1 = (args.h1 or pending.get("h1") or "").strip()
    text = (
        f"✅ Принято, пишу…\n\n"
        f"{topic_id}: {h1}\n"
        f"Пришлю ссылку, когда статья будет на сайте."
    )
    result = send_text(token, chat_id, text)
    if pending:
        pending["status"] = "writing"
        pending["ack_message_id"] = result["message_id"]
        save_pending(pending)
    print(json.dumps({"ok": True, "message_id": result["message_id"]}, ensure_ascii=False))


def cmd_published(args: argparse.Namespace) -> None:
    """Send final URL after WP publish."""
    token, chat_id = require_creds()
    pending = load_pending() if PENDING.is_file() else {}
    topic_id = (args.topic_id or pending.get("topic_id") or "").strip().upper()
    h1 = (args.h1 or pending.get("h1") or "").strip()
    url = args.url.strip()
    if not url:
        raise SystemExit("❌ --url required")
    text = (
        f"🚀 Опубликовано\n\n"
        f"{topic_id}: {h1}\n"
        f"{url}"
    )
    result = send_text(token, chat_id, text)
    if pending:
        pending["status"] = "published"
        pending["published_url"] = url
        pending["published_message_id"] = result["message_id"]
        save_pending(pending)
    print(json.dumps({"ok": True, "message_id": result["message_id"], "url": url}, ensure_ascii=False))


def cmd_resolve(args: argparse.Namespace) -> None:
    pending = load_pending()
    pending["status"] = args.status
    save_pending(pending)
    print(json.dumps({"ok": True, "pending": pending}, ensure_ascii=False))


def main() -> None:
    load_dotenv_local()
    # Windows consoles: keep UTF-8 for Cyrillic CLI args when possible
    if hasattr(sys.stdout, "reconfigure"):
        try:
            sys.stdout.reconfigure(encoding="utf-8")
            sys.stderr.reconfigure(encoding="utf-8")
        except Exception:
            pass

    p = argparse.ArgumentParser(description="Excalibur BLOG Telegram approval helpers")
    sub = p.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("send", help="Send arbitrary text")
    s.add_argument("--text", default="")
    s.add_argument("--file")
    s.set_defaults(func=cmd_send)

    s = sub.add_parser("propose", help="Propose topic and write pending-approval.json")
    s.add_argument("--topic-id", required=True)
    s.add_argument("--h1", required=True)
    s.add_argument("--slug", default="")
    s.set_defaults(func=cmd_propose)

    s = sub.add_parser("poll", help="Poll for ok/нет on pending topic")
    s.add_argument(
        "--ack",
        action="store_true",
        help="On approve/reject immediately reply in Telegram (Принято, пишу… / пропускаю)",
    )
    s.set_defaults(func=cmd_poll)

    s = sub.add_parser("ack", help="Send «Принято, пишу…»")
    s.add_argument("--topic-id", default="")
    s.add_argument("--h1", default="")
    s.set_defaults(func=cmd_ack)

    s = sub.add_parser("published", help="Send published URL to Telegram")
    s.add_argument("--url", required=True)
    s.add_argument("--topic-id", default="")
    s.add_argument("--h1", default="")
    s.set_defaults(func=cmd_published)

    s = sub.add_parser("resolve", help="Mark pending approved/rejected/cleared/writing/published")
    s.add_argument(
        "--status",
        required=True,
        choices=["approved", "rejected", "pending", "cleared", "writing", "published"],
    )
    s.set_defaults(func=cmd_resolve)

    args = p.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
