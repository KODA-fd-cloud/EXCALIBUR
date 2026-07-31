#!/usr/bin/env python3
"""CI Scout: find fresh utility-only topics for KODA blog and append to blog-topics.md.

Strategy (no LLM required):
  - Curated bank of KODA-niche utility angles (CFO + automation).
  - Web search (ddgs) scores which angles are «hot» right now.
  - Cannibalization guard vs published + pool.
  - Optional CURSOR_API_KEY → full Cloud Scout agent.

Usage:
  python scripts/excalibur_blog_scout_ci.py --count 3
  python scripts/excalibur_blog_scout_ci.py --min-unpublished 3 --notify
  python scripts/excalibur_blog_scout_ci.py --force --prefer-cursor
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request
from datetime import date, datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from excalibur_blog_scout_helper import (  # noqa: E402
    check_overlap,
    load_existing_topics,
    load_published_topics,
)
from excalibur_blog_telegram_notify import (  # noqa: E402
    load_dotenv_local,
    parse_topics,
    published_ids_and_slugs,
    require_creds,
    send_text,
)

TOPICS_PATH = ROOT / "memory" / "topics" / "blog-topics.md"
YEAR = datetime.now(timezone.utc).year

# Trend probes — only for scoring, not for raw H1 paste.
TREND_QUERIES = [
    f"n8n финансы автоматизация {YEAR}",
    f"cursor ai бухгалтер {YEAR}",
    f"автоматизация сверки банка excel {YEAR}",
    f"управленческий учет google sheets {YEAR}",
    f"1с odata google sheets",
    f"openai api финансы безопасность",
    f"make.com vs n8n бизнес",
    f"платёжный календарь автоматизация",
    f"дебиторская задолженность напоминания telegram",
    f"claude code финансы",
]

# Utility-only angles. Scout picks unpublished ones boosted by trend hits.
# Keep primary_query short RU phrases; slug kebab.
ANGLE_BANK: list[dict[str, str]] = [
    {
        "short": "Сверка банка и учёта через n8n",
        "h1": "Как сверить банковскую выписку с учётом через n8n и Google Sheets",
        "primary_query": "сверка банковской выписки n8n",
        "slug": "sverka-banka-n8n-google-sheets",
        "intent": "how_to",
        "tags": "n8n банк сверка sheets",
    },
    {
        "short": "Категоризация ДДС нейросетью локально",
        "h1": "Как категоризировать ДДС локальной нейросетью без отправки выписок в облако",
        "primary_query": "категоризация ддс нейросеть локально",
        "slug": "kategorizaciya-dds-lokalnaya-nejroset",
        "intent": "how_to",
        "tags": "ollama ддс категории безопасность",
    },
    {
        "short": "Бюджет vs факт в Sheets за вечер",
        "h1": "Как собрать бюджет vs факт в Google Sheets за один вечер: шаблон и формулы",
        "primary_query": "бюджет факт google sheets",
        "slug": "byudzhet-fakt-google-sheets",
        "intent": "how_to",
        "tags": "бюджет sheets управленческий",
    },
    {
        "short": "Cursor правит формулу Excel без магии",
        "h1": "Как попросить Cursor поправить Excel-формулу финансиста и не сломать файл",
        "primary_query": "cursor excel формулы финансист",
        "slug": "cursor-excel-formuly-bez-polomki",
        "intent": "how_to",
        "tags": "cursor excel формулы",
    },
    {
        "short": "Telegram-бот статусов оплат",
        "h1": "Как сделать Telegram-бот статусов оплат для финотдела на n8n",
        "primary_query": "telegram бот статусы оплат n8n",
        "slug": "telegram-bot-statusy-oplat-n8n",
        "intent": "workflow",
        "tags": "telegram n8n оплаты",
    },
    {
        "short": "Выгрузка банк→Sheets без 1С",
        "h1": "Как забирать банковскую выписку в Google Sheets без 1С: CSV, API, расписание",
        "primary_query": "банковская выписка google sheets",
        "slug": "bankovskaya-vypiska-google-sheets",
        "intent": "how_to",
        "tags": "банк sheets csv api",
    },
    {
        "short": "Чеклист безопасности ИИ в финотделе",
        "h1": "Чеклист безопасности: что нельзя скармливать ChatGPT из выгрузок 1С",
        "primary_query": "безопасность chatgpt финансы чеклист",
        "slug": "cheklist-bezopasnost-chatgpt-finotdel",
        "intent": "checklist",
        "tags": "chatgpt безопасность 1с пдн",
    },
    {
        "short": "Реестр договоров + сроки в Sheets",
        "h1": "Как вести реестр договоров и сроков оплаты в Google Sheets с напоминаниями",
        "primary_query": "реестр договоров google sheets",
        "slug": "reestr-dogovorov-google-sheets",
        "intent": "workflow",
        "tags": "договоры sheets напоминания",
    },
    {
        "short": "Power Automate для напоминаний оплат",
        "h1": "Как настроить напоминания об оплате через Power Automate и Excel Online",
        "primary_query": "power automate напоминание об оплате",
        "slug": "power-automate-napominanie-ob-oplate",
        "intent": "how_to",
        "tags": "power automate excel оплаты",
    },
    {
        "short": "Дашборд ДДС за час в Looker Studio",
        "h1": "Как собрать дашборд ДДС в Looker Studio из Google Sheets за час",
        "primary_query": "дашборд ддс looker studio",
        "slug": "dashbord-dds-looker-studio",
        "intent": "how_to",
        "tags": "looker ддс sheets дашборд",
    },
    {
        "short": "Сверка взаиморасчётов CSV+Python",
        "h1": "Как сверить взаиморасчёты контрагентов в Python по двум CSV за 15 минут",
        "primary_query": "сверка взаиморасчетов python csv",
        "slug": "sverka-vzaimoraschetov-python-csv",
        "intent": "how_to",
        "tags": "python csv сверка контрагенты",
    },
    {
        "short": "n8n: акты → папка → реестр",
        "h1": "Как автоматически класть сканы актов в папку и строку реестра через n8n",
        "primary_query": "n8n акты сверки автоматизация",
        "slug": "n8n-akty-papka-reestr",
        "intent": "workflow",
        "tags": "n8n акты диск реестр",
    },
    {
        "short": "Cursor Agent для еженедельного ДДС",
        "h1": "Как собрать еженедельный отчёт ДДС через Cursor Agent и шаблон Sheets",
        "primary_query": "cursor agent отчёт ддс",
        "slug": "cursor-agent-ezhenedelnyj-dds",
        "intent": "how_to",
        "tags": "cursor agent ддс отчёт",
    },
    {
        "short": "Разнести комиссию банка в ДДС",
        "h1": "Как автоматически разносить банковскую комиссию в статьи ДДС: правила и исключения",
        "primary_query": "разнести комиссию банка ддс",
        "slug": "raznesti-komissiyu-banka-dds",
        "intent": "how_to",
        "tags": "банк комиссия ддс правила",
    },
    {
        "short": "Сравнение: Apps Script vs n8n",
        "h1": "Apps Script или n8n для финотдела: когда хватает кнопки в Sheets",
        "primary_query": "apps script или n8n",
        "slug": "apps-script-ili-n8n-finotdel",
        "intent": "comparison",
        "tags": "apps script n8n сравнение",
    },
    {
        "short": "План счетов управленки в Sheets",
        "h1": "Как завести простой план счетов управленческого учёта в Google Sheets",
        "primary_query": "план счетов управленческий учет sheets",
        "slug": "plan-schetov-upravlencheskij-sheets",
        "intent": "how_to",
        "tags": "план счетов управленческий sheets",
    },
    {
        "short": "Контроль лимитов расходов в Telegram",
        "h1": "Как контролировать лимиты статей расходов и слать алерт в Telegram",
        "primary_query": "лимиты расходов telegram алерт",
        "slug": "limity-rashodov-telegram-alert",
        "intent": "workflow",
        "tags": "лимиты telegram бюджет алерт",
    },
    {
        "short": "Импорт 1С УНФ → Excel без выгрузок руками",
        "h1": "Как настроить регулярный импорт из 1С УНФ в Excel без ручных выгрузок",
        "primary_query": "импорт 1с унф excel регулярно",
        "slug": "import-1c-unf-excel-regulyarno",
        "intent": "how_to",
        "tags": "1с унф excel odata",
    },
    {
        "short": "Make: платёжка из таблицы",
        "h1": "Как собрать сценарий Make: строка в таблице → черновик платёжки в банк-клиент",
        "primary_query": "make платёжка из google sheets",
        "slug": "make-platezhka-iz-google-sheets",
        "intent": "workflow",
        "tags": "make платёжка sheets банк",
    },
    {
        "short": "Антидубли контрагентов в реестре",
        "h1": "Как найти дубли контрагентов в реестре дебиторки: Excel + простой скрипт",
        "primary_query": "дубли контрагентов excel",
        "slug": "dubli-kontragentov-excel-skript",
        "intent": "troubleshooting",
        "tags": "дубли контрагенты excel дебиторка",
    },
]


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


def next_topic_id() -> str:
    max_num = 0
    for t in parse_topics():
        m = re.match(r"B(\d+)", t["topic_id"])
        if m:
            max_num = max(max_num, int(m.group(1)))
    return f"B{max_num + 1:02d}"


def ddg_search(query: str, max_results: int = 5) -> list[dict[str, str]]:
    try:
        try:
            from ddgs import DDGS  # type: ignore
        except ImportError:
            from duckduckgo_search import DDGS  # type: ignore

        with DDGS() as ddgs:
            rows = list(ddgs.text(query, region="ru-ru", max_results=max_results))
        out = []
        for r in rows:
            out.append(
                {
                    "title": str(r.get("title") or ""),
                    "body": str(r.get("body") or r.get("snippet") or ""),
                    "href": str(r.get("href") or r.get("link") or ""),
                }
            )
        return out
    except Exception:
        url = "https://api.duckduckgo.com/?" + urllib.parse.urlencode(
            {"q": query, "format": "json", "no_html": 1, "skip_disambig": 1}
        )
        req = urllib.request.Request(url, headers={"User-Agent": "KODA-Scout/1.0"})
        with urllib.request.urlopen(req, timeout=20) as resp:
            data = json.loads(resp.read().decode("utf-8"))
        out = []
        if data.get("Heading"):
            out.append(
                {
                    "title": data["Heading"],
                    "body": data.get("Abstract", ""),
                    "href": data.get("AbstractURL", ""),
                }
            )
        for t in data.get("RelatedTopics", [])[:max_results]:
            if isinstance(t, dict) and t.get("Text"):
                out.append({"title": t["Text"][:120], "body": t["Text"], "href": t.get("FirstURL", "")})
        return out


def gather_trend_blob() -> str:
    chunks: list[str] = []
    for q in TREND_QUERIES:
        try:
            hits = ddg_search(q, max_results=4)
        except Exception as e:
            print(f"search fail {q}: {e}", file=sys.stderr)
            continue
        for h in hits:
            chunks.append(f"{h.get('title','')} {h.get('body','')}")
        time.sleep(0.6)
    return " ".join(chunks).lower()


def score_angle(angle: dict[str, str], trend_blob: str, salt: str) -> float:
    tags = angle.get("tags", "").lower().split()
    hit = sum(1 for t in tags if t and t in trend_blob)
    # Stable daily shuffle so we don't always pick the same top angles.
    h = hashlib.sha256(f"{salt}:{angle['slug']}".encode()).hexdigest()
    jitter = int(h[:6], 16) / 0xFFFFFF  # 0..1
    return hit * 2.0 + jitter


def append_card(topic_id: str, angle: dict[str, str], *, evidence: str = "") -> None:
    today = date.today().isoformat()
    card = f"""
---

## {topic_id} — {angle['short']}

- **priority:** P0
- **slug:** {angle['slug']}
- **h1:** {angle['h1']}
- **primary_query:** {angle['primary_query']}
- **secondary_queries:** автоматизация финотдела, {angle['primary_query']}, {YEAR}
- **search_intent:** {angle.get('intent', 'how_to')}
- **article_mode:** B
- **author_id:** olga-kondratskaya
- **source_notes:** scout_ci {today} · trend-scored utility angle
- **h2_outline:**
  1. Когда это нужно финотделу (и когда нет)
  2. Подготовка данных и безопасность (без сырых ПДн в облако)
  3. Пошаговая настройка / скрипт / сценарий
  4. Проверка результата и типичные ошибки
  5. Что автоматизировать дальше
- **faq_hints:** можно ли без программиста; сколько займёт внедрение; какие риски для данных
- **internal_links:** /avtomatizaciya-finansov-no-code/, /obezlichivanie-dannyh-chatgpt-finansist/
- **cover_scene_hint:** abstract holographic finance automation dark #0a0a0f purple #8b5cf6, no text
"""
    if evidence:
        card = card.replace(
            "trend-scored utility angle",
            f"trend-scored · {evidence[:120]}",
        )
    text = TOPICS_PATH.read_text(encoding="utf-8")
    marker = "## Архив очереди"
    if marker in text:
        text = text.replace(marker, card.strip() + "\n\n" + marker, 1)
    else:
        text = text.rstrip() + "\n" + card
    TOPICS_PATH.write_text(text + ("\n" if not text.endswith("\n") else ""), encoding="utf-8")


def scout_web(count: int) -> list[dict[str, str]]:
    existing = load_existing_topics(ROOT)
    published = load_published_topics(ROOT)
    pub_ids, pub_slugs = published_ids_and_slugs()
    used_slugs = {t.get("slug", "").lower() for t in existing} | pub_slugs
    used_q = {t.get("primary_query", "").strip().lower() for t in existing}

    print("Gathering trend signals…", flush=True)
    trend_blob = gather_trend_blob()
    salt = date.today().isoformat()

    ranked = sorted(
        ANGLE_BANK,
        key=lambda a: score_angle(a, trend_blob, salt),
        reverse=True,
    )

    added: list[dict[str, str]] = []
    for angle in ranked:
        if len(added) >= count:
            break
        slug = angle["slug"].lower()
        pq = angle["primary_query"].strip().lower()
        if slug in used_slugs or pq in used_q:
            continue
        warns = check_overlap(angle["primary_query"], existing, published)
        if any(w.get("severity") == "CRITICAL" for w in warns):
            continue
        if any(w.get("severity") == "WARNING" and w.get("similarity", 0) >= 0.5 for w in warns):
            continue

        topic_id = next_topic_id()
        tag_hits = [t for t in angle.get("tags", "").split() if t.lower() in trend_blob]
        evidence = "tags:" + ",".join(tag_hits) if tag_hits else "rotation"
        append_card(topic_id, angle, evidence=evidence)
        existing.append(
            {
                "topic_id": topic_id,
                "primary_query": angle["primary_query"],
                "slug": angle["slug"],
                "priority": "P0",
            }
        )
        used_slugs.add(slug)
        used_q.add(pq)
        row = {"topic_id": topic_id, **angle}
        added.append(row)
        print(f"ADDED {topic_id}: {angle['h1']}", flush=True)
    return added


def scout_cursor_cloud(count: int) -> dict:
    api_key = os.environ.get("CURSOR_API_KEY", "").strip()
    if not api_key:
        raise RuntimeError("CURSOR_API_KEY missing")

    from cursor_sdk import Agent, AgentOptions, CloudAgentOptions, CloudRepository  # type: ignore

    prompt = f"""Ты excalibur-blog-scout для блога КОДА (финансист, который кодит).

Прочитай:
- skills/scout-excalibur-blog/SKILL.md
- shared/editorial-utility-only.md
- shared/published-articles.md
- memory/topics/blog-topics.md
- memory/brief/site-brief.md

Задача: найти {count} НОВЫЕ актуальные utility-only темы ({YEAR}), релевантные CFO/финотделу + автоматизация (n8n/Make/Cursor/1С/Sheets/Python).
Не дублируй опубликованные slug и карточки в blog-topics.md.
Используй web search по свежим трендам. Wordstat — если MCP доступен; иначе честно пометь demand: unknown.
Каждую тему добавь карточкой в конец memory/topics/blog-topics.md (перед секцией Архив, если есть).
article_mode только B. search_intent: how_to|checklist|comparison|troubleshooting|workflow.
После правок: git add/commit/push в master с сообщением "chore(blog): scout refill topics".
В финальном ответе JSON: {{"added":[{{"topic_id","h1","slug","primary_query"}}]}}
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
    if hasattr(sys.stdout, "reconfigure"):
        try:
            sys.stdout.reconfigure(encoding="utf-8")
        except Exception:
            pass

    ap = argparse.ArgumentParser()
    ap.add_argument("--count", type=int, default=3, help="How many new topic cards to add")
    ap.add_argument("--min-unpublished", type=int, default=3, help="Scout only if unpublished below this")
    ap.add_argument("--force", action="store_true", help="Scout even if queue is full enough")
    ap.add_argument("--notify", action="store_true", help="Telegram summary")
    ap.add_argument("--prefer-cursor", action="store_true", help="Use Cursor Cloud Agent when API key present")
    args = ap.parse_args()

    left = unpublished_count()
    if not args.force and left >= args.min_unpublished:
        print(json.dumps({"ok": True, "action": "skip", "unpublished": left}, ensure_ascii=False))
        return 0

    mode = "web"
    added: list[dict] = []

    if args.prefer_cursor and os.environ.get("CURSOR_API_KEY", "").strip():
        try:
            cursor_out = scout_cursor_cloud(args.count)
            mode = "cursor_cloud"
            print(
                json.dumps(
                    {
                        "ok": True,
                        "action": "cursor_scout",
                        "unpublished_before": left,
                        "cursor": cursor_out,
                    },
                    ensure_ascii=False,
                    default=str,
                )
            )
        except Exception as e:
            print(f"cursor scout failed, fallback web: {e}", file=sys.stderr)
            mode = "web"

    if mode == "web":
        added = scout_web(args.count)
        print(
            json.dumps(
                {
                    "ok": True,
                    "action": "web_scout",
                    "added": [
                        {
                            "topic_id": a["topic_id"],
                            "h1": a["h1"],
                            "slug": a["slug"],
                            "primary_query": a["primary_query"],
                        }
                        for a in added
                    ],
                    "unpublished_after": unpublished_count(),
                },
                ensure_ascii=False,
            )
        )

    if args.notify:
        try:
            token, chat_id = require_creds()
            if added:
                lines = "\n".join(f"• {a['topic_id']}: {a['h1']}" for a in added)
                send_text(token, chat_id, f"🔎 Scout дозаправил очередь ({mode}):\n{lines}")
            elif mode == "cursor_cloud":
                send_text(token, chat_id, "🔎 Scout (Cursor Cloud) запущен — новые темы скоро в blog-topics.md")
            else:
                send_text(
                    token,
                    chat_id,
                    "🔎 Scout: банк углов исчерпан или всё в overlap. Допиши ANGLE_BANK / Cloud Scout.",
                )
        except SystemExit:
            pass

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
