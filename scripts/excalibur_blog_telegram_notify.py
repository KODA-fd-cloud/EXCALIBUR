#!/usr/bin/env python3
"""Send / poll Telegram for topic approval. Secrets from env or memory/site.env.local."""
from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.parse
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
        data = json.dumps(payload).encode("utf-8")
        headers["Content-Type"] = "application/json; charset=utf-8"
    req = urllib.request.Request(url, data=data, headers=headers, method="POST" if data else "GET")
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        raise SystemExit(f"❌ Telegram API {method}: HTTP {e.code} {body}") from e


def cmd_send(args: argparse.Namespace) -> None:
    token, chat_id = require_creds()
    text = args.text
    if args.file:
        text = Path(args.file).read_text(encoding="utf-8")
    if not text.strip():
        raise SystemExit("❌ empty message")
    r = api(token, "sendMessage", {"chat_id": chat_id, "text": text})
    if not r.get("ok"):
        raise SystemExit(f"❌ send failed: {r}")
    print(json.dumps({"ok": True, "message_id": r["result"]["message_id"]}, ensure_ascii=False))


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
    r = api(token, "sendMessage", {"chat_id": chat_id, "text": text})
    if not r.get("ok"):
        raise SystemExit(f"❌ send failed: {r}")
    pending = {
        "topic_id": topic_id,
        "h1": h1,
        "slug": slug,
        "status": "pending",
        "proposed_at": r["result"]["date"],
        "proposal_message_id": r["result"]["message_id"],
        "chat_id": str(chat_id),
    }
    PENDING.parent.mkdir(parents=True, exist_ok=True)
    PENDING.write_text(json.dumps(pending, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
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
    pending = json.loads(PENDING.read_text(encoding="utf-8"))
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

    if max_update_id >= offset:
        # hint for next poll; caller may persist
        print(
            json.dumps(
                {
                    "ok": True,
                    "decision": decision,
                    "matched_text": matched_text,
                    "next_offset": max_update_id + 1,
                    "topic_id": pending.get("topic_id"),
                    "pending_path": str(PENDING),
                },
                ensure_ascii=False,
            )
        )
    else:
        print(
            json.dumps(
                {
                    "ok": True,
                    "decision": decision,
                    "matched_text": matched_text,
                    "topic_id": pending.get("topic_id"),
                    "pending_path": str(PENDING),
                },
                ensure_ascii=False,
            )
        )


def cmd_resolve(args: argparse.Namespace) -> None:
    if not PENDING.is_file():
        raise SystemExit("❌ no pending file")
    pending = json.loads(PENDING.read_text(encoding="utf-8"))
    pending["status"] = args.status
    PENDING.write_text(json.dumps(pending, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"ok": True, "pending": pending}, ensure_ascii=False))


def main() -> None:
    load_dotenv_local()
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
    s.set_defaults(func=cmd_poll)

    s = sub.add_parser("resolve", help="Mark pending approved/rejected/cleared")
    s.add_argument("--status", required=True, choices=["approved", "rejected", "pending", "cleared"])
    s.set_defaults(func=cmd_resolve)

    args = p.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
