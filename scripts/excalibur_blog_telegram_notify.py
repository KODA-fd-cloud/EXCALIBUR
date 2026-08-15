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
REJECTED = ROOT / "memory" / "topics" / "rejected-topics.json"
ACKED = ROOT / "memory" / "topics" / "acked-topics.json"
LAST_PROPOSAL = ROOT / "memory" / "topics" / "last-proposal.json"
TOPICS = ROOT / "memory" / "topics" / "blog-topics.md"
PUBLISHED = ROOT / "shared" / "published-articles.md"
OFFSET_FILE = ROOT / "memory" / "topics" / "telegram-updates.offset"
COOLDOWNS = ROOT / "memory" / "topics" / "telegram-cooldowns.json"

# Anti-spam: never hammer Telegram with the same system notice
EMPTY_QUEUE_COOLDOWN_SEC = 24 * 3600
REMIND_COOLDOWN_SEC = 12 * 3600


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


def load_rejected_file() -> list[str]:
    if not REJECTED.is_file():
        return []
    try:
        data = json.loads(REJECTED.read_text(encoding="utf-8"))
    except Exception:
        return []
    if isinstance(data, list):
        return [str(x).upper() for x in data]
    if isinstance(data, dict):
        return [str(x).upper() for x in (data.get("rejected_ids") or [])]
    return []


def save_rejected_file(ids: list[str] | set[str]) -> None:
    """Durable reject list — survives pending git races / failed pushes."""
    merged = sorted({str(x).upper() for x in ids if str(x).strip()})
    REJECTED.parent.mkdir(parents=True, exist_ok=True)
    REJECTED.write_text(
        json.dumps({"rejected_ids": merged, "updated_at": int(time.time())}, ensure_ascii=False, indent=2)
        + "\n",
        encoding="utf-8",
    )


def mark_rejected(*topic_ids: str) -> list[str]:
    merged = set(load_rejected_file())
    pending = load_pending() or {}
    merged |= {str(x).upper() for x in (pending.get("rejected_ids") or [])}
    for tid in topic_ids:
        if tid:
            merged.add(str(tid).upper())
    out = sorted(merged)
    save_rejected_file(out)
    return out


def load_acked_file() -> set[str]:
    if not ACKED.is_file():
        return set()
    try:
        data = json.loads(ACKED.read_text(encoding="utf-8"))
    except Exception:
        return set()
    if isinstance(data, list):
        return {str(x).upper() for x in data}
    if isinstance(data, dict):
        return {str(x).upper() for x in (data.get("acked_ids") or [])}
    return set()


def mark_acked(*topic_ids: str) -> list[str]:
    """Once a topic got «Тема принята» / published — never send ack again."""
    merged = set(load_acked_file())
    pub_ids, _ = published_ids_and_slugs()
    merged |= pub_ids
    for tid in topic_ids:
        if tid:
            merged.add(str(tid).upper())
    out = sorted(merged)
    ACKED.parent.mkdir(parents=True, exist_ok=True)
    ACKED.write_text(
        json.dumps({"acked_ids": out, "updated_at": int(time.time())}, ensure_ascii=False, indent=2)
        + "\n",
        encoding="utf-8",
    )
    return out


def drain_telegram_offset(token: str) -> int:
    """Advance offset to latest update so old ок/нет cannot be replayed after git rollback."""
    offset = read_offset()
    r = api(token, "getUpdates", {"offset": offset, "timeout": 0, "allowed_updates": ["message"]})
    if not r.get("ok"):
        return offset
    max_id = offset - 1
    for upd in r.get("result", []):
        max_id = max(max_id, int(upd["update_id"]))
    if max_id >= offset:
        write_offset(max_id + 1)
        return max_id + 1
    return offset


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


def load_cooldowns() -> dict:
    if not COOLDOWNS.is_file():
        return {}
    try:
        return json.loads(COOLDOWNS.read_text(encoding="utf-8"))
    except Exception:
        return {}


def save_cooldowns(data: dict) -> None:
    COOLDOWNS.parent.mkdir(parents=True, exist_ok=True)
    COOLDOWNS.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def cooldown_touch(key: str) -> None:
    data = load_cooldowns()
    data[key] = int(time.time())
    # Keep sibling starve keys in sync so Scout+tick don't double-spam same day
    if key in {"empty_queue", "scout_exhausted", "queue_starve"}:
        now = int(time.time())
        data["empty_queue"] = now
        data["scout_exhausted"] = now
        data["queue_starve"] = now
    save_cooldowns(data)


def cooldown_ready(key: str, seconds: int) -> bool:
    data = load_cooldowns()
    # Any starve notice blocks all starve notices
    if key in {"empty_queue", "scout_exhausted", "queue_starve"}:
        last = max(
            int(data.get("empty_queue") or 0),
            int(data.get("scout_exhausted") or 0),
            int(data.get("queue_starve") or 0),
        )
        return (time.time() - last) >= seconds
    last = int(data.get(key) or 0)
    return (time.time() - last) >= seconds


def rejected_ids() -> set[str]:
    pending = load_pending() or {}
    merged = {str(x).upper() for x in (pending.get("rejected_ids") or [])}
    merged |= set(load_rejected_file())
    return merged


def proposeable_count() -> int:
    """Unpublished topics that are NOT rejected — real queue depth for Scout/tick."""
    pub_ids, pub_slugs = published_ids_and_slugs()
    skip = pub_ids | rejected_ids()
    n = 0
    for t in parse_topics():
        if t["topic_id"] in skip:
            continue
        if t["slug"] and t["slug"].lower() in pub_slugs:
            continue
        n += 1
    return n


def next_topic(*, skip_ids: set[str] | None = None) -> dict | None:
    skip_ids = {x.upper() for x in (skip_ids or set())}
    pub_ids, pub_slugs = published_ids_and_slugs()
    skip_ids |= pub_ids
    skip_ids |= rejected_ids()
    candidates = []
    for t in parse_topics():
        if t["topic_id"] in skip_ids:
            continue
        if t["slug"] and t["slug"].lower() in pub_slugs:
            continue
        candidates.append(t)
    candidates.sort(key=lambda t: (0 if t["priority"] == "P0" else 1, t["topic_id"]))
    return candidates[0] if candidates else None


def autofill_topics(count: int = 5) -> list[dict]:
    """Force Scout web refill when queue is exhausted (incl. all-rejected case)."""
    sys.path.insert(0, str(ROOT / "scripts"))
    from excalibur_blog_scout_ci import scout_web  # noqa: WPS433

    return scout_web(count)


def normalize_reply(text: str) -> str:
    t = text.strip().lower().replace("ё", "е")
    if t in {"ok", "ок", "да", "yes", "+", "👍", "✅"}:
        return "approve"
    if t in {"net", "нет", "no", "-", "👎", "❌", "skip"}:
        return "reject"
    return "unknown"


def load_last_proposal() -> dict | None:
    if not LAST_PROPOSAL.is_file():
        return None
    try:
        return json.loads(LAST_PROPOSAL.read_text(encoding="utf-8"))
    except Exception:
        return None


def save_last_proposal(data: dict) -> None:
    LAST_PROPOSAL.parent.mkdir(parents=True, exist_ok=True)
    LAST_PROPOSAL.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def sync_pending_to_last_proposal(pending: dict | None) -> dict | None:
    """If git pending drifted from what was actually sent to Telegram — trust last-proposal."""
    last = load_last_proposal()
    if not pending or not last:
        return pending
    last_tid = str(last.get("topic_id") or "").upper()
    pend_tid = str(pending.get("topic_id") or "").upper()
    if not last_tid or last_tid == pend_tid:
        return pending
    # Stale pending (e.g. B44) while chat shows B45
    pending["topic_id"] = last_tid
    pending["h1"] = last.get("h1") or pending.get("h1") or ""
    pending["slug"] = last.get("slug") or pending.get("slug") or ""
    if last.get("proposal_message_id"):
        pending["proposal_message_id"] = last["proposal_message_id"]
    if last.get("proposed_at"):
        pending["proposed_at"] = last["proposed_at"]
    pending["status"] = "pending"
    save_pending(pending)
    return pending


def propose_topic(token: str, chat_id: str, topic: dict, *, rejected_ids: list[str] | None = None) -> dict:
    tid = str(topic["topic_id"]).upper()
    # Anti-spam: don't re-send the same proposal if it is already the active last one
    last = load_last_proposal() or {}
    if (
        str(last.get("topic_id") or "").upper() == tid
        and last.get("proposal_message_id")
        and (time.time() - int(last.get("proposed_at") or 0)) < 6 * 3600
    ):
        pending = {
            "topic_id": tid,
            "h1": topic["h1"],
            "slug": topic.get("slug", ""),
            "status": "pending",
            "proposed_at": int(last.get("proposed_at") or time.time()),
            "proposal_message_id": last.get("proposal_message_id"),
            "chat_id": str(chat_id),
            "rejected_ids": list(rejected_ids or []),
        }
        save_pending(pending)
        return pending

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
        "topic_id": tid,
        "h1": topic["h1"],
        "slug": topic.get("slug", ""),
        "status": "pending",
        "proposed_at": int(result["date"]),
        "proposal_message_id": result["message_id"],
        "chat_id": str(chat_id),
        "rejected_ids": rejected_ids or [],
    }
    save_pending(pending)
    save_last_proposal(
        {
            "topic_id": tid,
            "h1": topic["h1"],
            "slug": topic.get("slug", ""),
            "proposed_at": int(result["date"]),
            "proposal_message_id": result["message_id"],
        }
    )
    return pending


def effective_proposed_at(pending: dict) -> int:
    now = int(time.time())
    ts = int(pending.get("proposed_at") or 0)
    if ts <= 0 or ts > now + 600:
        return now - 30 * 86400
    return ts


def remind_pending(token: str, chat_id: str, pending: dict) -> dict:
    # Silent if reminded recently — tick runs every 15m, don't spam
    last = int(pending.get("reminded_at") or 0)
    if last and (time.time() - last) < REMIND_COOLDOWN_SEC:
        return pending
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
    pending["reminded_at"] = int(time.time())
    save_pending(pending)
    return pending


def apply_decision(
    token: str,
    chat_id: str,
    pending: dict,
    decision: str,
    *,
    shown_topic_id: str | None = None,
) -> dict:
    out: dict = {"decision": decision, "topic_id": pending.get("topic_id")}
    if decision == "approve":
        tid = str(pending.get("topic_id") or "").upper()
        pub_ids, pub_slugs = published_ids_and_slugs()
        slug = str(pending.get("slug") or "").lower()
        already_done = tid in pub_ids or tid in load_acked_file() or (slug and slug in pub_slugs)

        # Idempotent: не спамить «Тема принята» при повторном poll / откате git
        if already_done:
            mark_acked(tid)
            pending["status"] = "published"
            save_pending(pending)
            out["status"] = "published"
            out["action"] = "already_published_skip_ack"
            return out
        if pending.get("status") in {"writing", "queued_write"} and pending.get("ack_message_id"):
            mark_acked(tid)
            out["status"] = pending.get("status")
            out["action"] = "already_approved"
            out["ack_message_id"] = pending.get("ack_message_id")
            return out
        if pending.get("ack_message_id") and pending.get("status") == "pending":
            pending["status"] = "writing"
            mark_acked(tid)
            save_pending(pending)
            out["status"] = "writing"
            out["action"] = "repaired_writing_no_ack"
            out["ack_message_id"] = pending.get("ack_message_id")
            return out
        if tid in load_acked_file():
            pending["status"] = "writing"
            save_pending(pending)
            out["status"] = "writing"
            out["action"] = "acked_file_skip_message"
            return out

        result = send_text(
            token,
            chat_id,
            f"✅ Тема принята: {pending['topic_id']}\n"
            f"{pending.get('h1', '')}\n\n"
            f"Дальше: очередь на написание → QA → обложка → публикация.\n"
            f"Ссылку пришлю, когда статья будет на сайте (это не мгновенно).",
        )
        pending["status"] = "writing"
        pending["missing_article_notified"] = False
        pending["ack_message_id"] = result["message_id"]
        pending["approved_at"] = int(time.time())
        mark_acked(tid)
        save_pending(pending)
        out["status"] = "writing"
        out["ack_message_id"] = result["message_id"]
        return out

    if decision == "reject":
        # Persist reject FIRST. Always kill pending + last-proposal + reply target
        # (git often lags behind Telegram → otherwise «пропускаю B44» while chat shows B45).
        skip_tid = str(pending.get("topic_id") or "").upper()
        shown = (shown_topic_id or "").upper()
        last = load_last_proposal() or {}
        last_tid = str(last.get("topic_id") or "").upper()
        kill = {x for x in (skip_tid, shown, last_tid) if x}
        rejected = mark_rejected(
            *kill,
            *[str(x) for x in (pending.get("rejected_ids") or [])],
        )
        pending["status"] = "rejected"
        pending["rejected_ids"] = rejected
        pending["rejected_at"] = int(time.time())
        save_pending(pending)

        label = "+".join(sorted(kill)) if kill else "?"
        send_text(token, chat_id, f"⏭ Ок, пропускаю {label}. Сразу следующая тема:")
        topic = next_topic(skip_ids=set(rejected))
        if not topic:
            try:
                autofill_topics(5)
            except Exception:
                pass
            topic = next_topic(skip_ids=set(rejected))
        if not topic:
            if cooldown_ready("empty_queue", EMPTY_QUEUE_COOLDOWN_SEC):
                send_text(
                    token,
                    chat_id,
                    "📭 После «нет» не осталось тем. Scout не дозаправил — попробую позже (не чаще 1×/сутки).",
                )
                cooldown_touch("empty_queue")
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


def topic_id_from_text(text: str) -> str | None:
    m = re.search(r"ID:\s*(B\d+)", text or "", re.I)
    return m.group(1).upper() if m else None


def _poll_once(token: str, chat_id: str, pending: dict, *, timeout: int = 0) -> tuple[str, str | None, int, str | None]:
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
    shown_topic_id = None
    max_id = offset - 1
    min_date = effective_proposed_at(pending)
    proposal_mid = pending.get("proposal_message_id")

    for upd in r.get("result", []):
        max_id = max(max_id, int(upd["update_id"]))
        msg = upd.get("message") or {}
        if str(msg.get("chat", {}).get("id")) != str(chat_id):
            continue
        reply_to_msg = msg.get("reply_to_message") or {}
        reply_to = reply_to_msg.get("message_id")
        if int(msg.get("date", 0)) < min_date and reply_to != proposal_mid:
            continue
        text = msg.get("text") or ""
        d = normalize_reply(text)
        if d == "unknown":
            continue
        decision = d
        matched = text
        # If user replies to a proposal, trust THAT id (fixes B41-file / B42-Telegram drift)
        shown_topic_id = topic_id_from_text(str(reply_to_msg.get("text") or ""))
        write_offset(int(upd["update_id"]) + 1)
        break
    else:
        if max_id >= offset:
            write_offset(max_id + 1)
    return decision, matched, max_id, shown_topic_id


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
            try:
                autofill_topics(5)
            except Exception:
                pass
            topic = next_topic()
        if not topic:
            if cooldown_ready("empty_queue", EMPTY_QUEUE_COOLDOWN_SEC):
                send_text(
                    token,
                    chat_id,
                    "📭 Очередь пуста даже после Scout. Сообщение не чаще 1×/сутки.",
                )
                cooldown_touch("empty_queue")
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
    prev = load_pending() or {}
    rejected = list(prev.get("rejected_ids") or [])
    pending = propose_topic(token, chat_id, topic, rejected_ids=rejected)
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
        try:
            autofill_topics(5)
        except Exception:
            pass
        topic = next_topic(skip_ids=set(rejected))
    if not topic:
        if cooldown_ready("empty_queue", EMPTY_QUEUE_COOLDOWN_SEC):
            send_text(
                token,
                chat_id,
                "📭 Очередь пуста даже после Scout. Сообщение не чаще 1×/сутки.",
            )
            cooldown_touch("empty_queue")
        print(json.dumps({"ok": False, "reason": "empty_queue"}, ensure_ascii=False))
        return
    pending = propose_topic(token, chat_id, topic, rejected_ids=rejected)
    print(json.dumps({"ok": True, **pending}, ensure_ascii=False))


def cmd_tick(args: argparse.Namespace) -> None:
    """Scheduled entrypoint: propose / remind (rate-limited) / handle ok|нет / autofill."""
    token, chat_id = require_creds()
    pending = load_pending()
    # Trust what was actually sent to Telegram over stale git pending
    pending = sync_pending_to_last_proposal(pending)
    # Merge durable rejects into pending every tick (survives failed pushes / stale checkout)
    durable = mark_rejected(*list((pending or {}).get("rejected_ids") or []))
    if pending is not None:
        pending["rejected_ids"] = durable
        save_pending(pending)
    rejected = list(durable)

    # If git rolled back pending to an already-published topic — advance, don't re-ack
    if pending and pending.get("topic_id"):
        tid = str(pending["topic_id"]).upper()
        pub_ids, pub_slugs = published_ids_and_slugs()
        slug = str(pending.get("slug") or "").lower()
        if tid in pub_ids or tid in load_acked_file() or (slug and slug in pub_slugs):
            if pending.get("status") in {"pending", "writing", "queued_write", "published"}:
                mark_acked(tid)
                rejected = mark_rejected(*rejected)  # keep file warm
                topic = next_topic(skip_ids=set(rejected) | {tid} | pub_ids)
                if topic and (
                    pending.get("status") == "published"
                    or tid in pub_ids
                    or (slug and slug in pub_slugs)
                ):
                    # Only auto-propose if this topic is truly done (ledger/slug), not merely acked mid-write
                    if tid in pub_ids or (slug and slug in pub_slugs):
                        pending = propose_topic(token, chat_id, topic, rejected_ids=list(rejected))
                        print(
                            json.dumps(
                                {
                                    "ok": True,
                                    "action": "repaired_stale_published_pending",
                                    "prev": tid,
                                    "topic_id": pending["topic_id"],
                                    "status": "pending",
                                },
                                ensure_ascii=False,
                            )
                        )
                        return

    if pending and pending.get("status") == "pending":
        now = int(time.time())
        if int(pending.get("proposed_at") or 0) > now + 600:
            pending["proposed_at"] = now - 3600
            save_pending(pending)

    if pending and pending.get("status") in {"writing", "queued_write"}:
        print(
            json.dumps(
                {
                    "ok": True,
                    "action": "continue_pipeline",
                    "decision": "approve",
                    "status": pending.get("status"),
                    "topic_id": pending.get("topic_id"),
                    "h1": pending.get("h1"),
                    "slug": pending.get("slug"),
                },
                ensure_ascii=False,
            )
        )
        return

    if pending and pending.get("status") == "pending":
        decision, matched, _, shown_tid = _poll_once(token, chat_id, pending, timeout=0)
        if decision in {"approve", "reject"}:
            # If Telegram proposal drifted from pending file — align before approve/reject
            if shown_tid and shown_tid != str(pending.get("topic_id") or "").upper():
                if decision == "reject":
                    pass  # apply_decision rejects both
                else:
                    # approve the topic user actually saw if it's in the pool
                    for t in parse_topics():
                        if t["topic_id"] == shown_tid:
                            pending["topic_id"] = t["topic_id"]
                            pending["h1"] = t["h1"]
                            pending["slug"] = t.get("slug", "")
                            break
            out = apply_decision(token, chat_id, pending, decision, shown_topic_id=shown_tid)
            out["ok"] = True
            out["matched_text"] = matched
            out["shown_topic_id"] = shown_tid
            out["action"] = "handled_reply"
            print(json.dumps(out, ensure_ascii=False))
            return
        before = int(pending.get("reminded_at") or 0)
        pending = remind_pending(token, chat_id, pending)
        action = "reminded" if int(pending.get("reminded_at") or 0) != before else "waiting_silent"
        print(
            json.dumps(
                {
                    "ok": True,
                    "action": action,
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

    # No active pending (missing / rejected / published) → propose next or autofill
    topic = next_topic(skip_ids=set(rejected))
    added: list[dict] = []
    if not topic:
        try:
            added = autofill_topics(5)
        except Exception as e:
            print(f"autofill failed: {e}", file=sys.stderr)
            added = []
        topic = next_topic(skip_ids=set(rejected))

    if not topic:
        notified = False
        if cooldown_ready("empty_queue", EMPTY_QUEUE_COOLDOWN_SEC):
            send_text(
                token,
                chat_id,
                "📭 Нет тем для согласования (все оставшиеся отклонены или банк углов пуст).\n"
                "Scout не смог дозаправить сейчас. Повторю попытку в фоне; это сообщение — не чаще 1 раза/сутки.",
            )
            cooldown_touch("empty_queue")
            notified = True
        print(
            json.dumps(
                {
                    "ok": False,
                    "action": "empty_queue" if notified else "empty_queue_silent",
                    "proposeable": proposeable_count(),
                    "rejected": rejected,
                },
                ensure_ascii=False,
            )
        )
        return

    pending = propose_topic(token, chat_id, topic, rejected_ids=rejected)
    out = {
        "ok": True,
        "action": "proposed_after_autofill" if added else "proposed",
        "decision": "pending",
        "status": "pending",
        "topic_id": pending["topic_id"],
        "h1": pending["h1"],
        "slug": pending.get("slug", ""),
        "autofilled": [{"topic_id": a.get("topic_id"), "slug": a.get("slug")} for a in added],
    }
    print(json.dumps(out, ensure_ascii=False))


def cmd_poll(args: argparse.Namespace) -> None:
    token, chat_id = require_creds()
    pending = load_pending()
    if not pending:
        print(json.dumps({"ok": True, "decision": "none", "reason": "no_pending"}, ensure_ascii=False))
        return
    if pending.get("status") != "pending":
        print(json.dumps({"ok": True, "decision": pending.get("status"), "pending": pending}, ensure_ascii=False))
        return
    decision, matched, _, shown_tid = _poll_once(token, chat_id, pending, timeout=0)
    out: dict = {
        "ok": True,
        "decision": decision,
        "matched_text": matched,
        "topic_id": pending.get("topic_id"),
        "shown_topic_id": shown_tid,
        "status": pending.get("status"),
    }
    if args.ack and decision in {"approve", "reject"}:
        out.update(apply_decision(token, chat_id, pending, decision, shown_topic_id=shown_tid))
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
        decision, matched, _, shown_tid = _poll_once(
            token, chat_id, pending, timeout=min(25, args.timeout_sec)
        )
        if decision == "approve":
            out = apply_decision(token, chat_id, pending, decision, shown_topic_id=shown_tid)
            print(json.dumps({"ok": True, "matched_text": matched, "h1": pending.get("h1"), "slug": pending.get("slug"), **out}, ensure_ascii=False))
            return
        if decision == "reject":
            skips += 1
            if skips > args.max_skips:
                send_text(token, chat_id, "⏹ Слишком много «нет» подряд. Остановлюсь до следующего слота.")
                print(json.dumps({"ok": False, "reason": "max_skips", "skips": skips}, ensure_ascii=False))
                return
            out = apply_decision(token, chat_id, pending, decision, shown_topic_id=shown_tid)
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
        f"✅ Тема принята: {topic_id}\n{h1}\n\n"
        f"Дальше: очередь на написание → QA → обложка → публикация.\n"
        f"Ссылку пришлю, когда статья будет на сайте.",
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
