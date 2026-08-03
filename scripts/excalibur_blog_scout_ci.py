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
    is_blocked,
    load_existing_topics,
    load_published_topics,
    theme_keys_for,
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

# Utility-only angles. Each theme_key = unique job-to-be-done.
# Do NOT add paraphrases of published jobs (bankstmt, reconcile, planfakt, 1c export, …).
ANGLE_BANK: list[dict[str, str]] = [
    {
        "theme_key": "contract_registry_reminders",
        "short": "Реестр договоров + сроки в Sheets",
        "h1": "Как вести реестр договоров и сроков оплаты в Google Sheets с напоминаниями",
        "primary_query": "реестр договоров google sheets",
        "slug": "reestr-dogovorov-google-sheets",
        "intent": "workflow",
        "tags": "договоры sheets напоминания",
    },
    {
        "theme_key": "looker_dds_dashboard",
        "short": "Дашборд ДДС за час в Looker Studio",
        "h1": "Как собрать дашборд ДДС в Looker Studio из Google Sheets за час",
        "primary_query": "дашборд ддс looker studio",
        "slug": "dashbord-dds-looker-studio",
        "intent": "how_to",
        "tags": "looker ддс sheets дашборд",
    },
    {
        "theme_key": "bank_fee_to_dds",
        "short": "Разнести комиссию банка в ДДС",
        "h1": "Как автоматически разносить банковскую комиссию в статьи ДДС: правила и исключения",
        "primary_query": "разнести комиссию банка ддс",
        "slug": "raznesti-komissiyu-banka-dds",
        "intent": "how_to",
        "tags": "банк комиссия ддс правила",
    },
    {
        "theme_key": "expense_limits_telegram",
        "short": "Контроль лимитов расходов в Telegram",
        "h1": "Как контролировать лимиты статей расходов и слать алерт в Telegram",
        "primary_query": "лимиты расходов telegram алерт",
        "slug": "limity-rashodov-telegram-alert",
        "intent": "workflow",
        "tags": "лимиты telegram бюджет алерт",
    },
    {
        "theme_key": "make_payment_draft",
        "short": "Make: платёжка из таблицы",
        "h1": "Как собрать сценарий Make: строка в таблице → черновик платёжки в банк-клиент",
        "primary_query": "make платёжка из google sheets",
        "slug": "make-platezhka-iz-google-sheets",
        "intent": "workflow",
        "tags": "make платёжка sheets банк",
    },
    {
        "theme_key": "counterparty_dedupe",
        "short": "Антидубли контрагентов в реестре",
        "h1": "Как найти дубли контрагентов в реестре дебиторки: Excel + простой скрипт",
        "primary_query": "дубли контрагентов excel",
        "slug": "dubli-kontragentov-excel-skript",
        "intent": "troubleshooting",
        "tags": "дубли контрагенты excel дебиторка",
    },
    {
        "theme_key": "cash_gap_forecast",
        "short": "Прогноз кассового разрыва на 14 дней",
        "h1": "Как собрать прогноз кассового разрыва на 14 дней в Google Sheets без 1С",
        "primary_query": "прогноз кассового разрыва google sheets",
        "slug": "prognoz-kassovogo-razryva-sheets",
        "intent": "how_to",
        "tags": "кассовый разрыв sheets прогноз",
    },
    {
        "theme_key": "payroll_bank_file",
        "short": "Зарплатная ведомость → файл в банк",
        "h1": "Как из зарплатной ведомости собрать файл для банк-клиента без копипаста",
        "primary_query": "зарплатная ведомость файл для банка",
        "slug": "zarplatnaya-vedomost-fail-bank",
        "intent": "how_to",
        "tags": "зарплата банк excel выгрузка",
    },
    {
        "theme_key": "expense_claims_control",
        "short": "Подотчёт: авансы и чеки в одном реестре",
        "h1": "Как вести подотчётные в Google Sheets: аванс, чеки, срок отчёта, эскалация",
        "primary_query": "учет подотчетных google sheets",
        "slug": "podotchet-reestr-google-sheets",
        "intent": "workflow",
        "tags": "подотчет sheets аванс чеки",
    },
    {
        "theme_key": "closing_docs_before_pay",
        "short": "Комплект закрывашек до оплаты",
        "h1": "Как не платить поставщику без комплекта закрывающих: чеклист и статус в таблице",
        "primary_query": "контроль закрывающих документов перед оплатой",
        "slug": "kontrol-zakryvayushchih-pered-oplatoj",
        "intent": "checklist",
        "tags": "закрывающие оплата реестр контроль",
    },
    {
        "theme_key": "multi_entity_bank",
        "short": "Несколько юрлиц: выписки в один контур",
        "h1": "Как свести банковские выписки нескольких юрлиц в один управленческий контур",
        "primary_query": "выписки нескольких юрлиц один учет",
        "slug": "vypiski-neskolkih-yurlic-odin-kontur",
        "intent": "workflow",
        "tags": "холдинг юрлица банк staging",
    },
    {
        "theme_key": "payment_purpose_rules",
        "short": "Разбор назначения платежа правилами",
        "h1": "Как разобрать назначение платежа правилами (не нейросетью) и проставить статью ДДС",
        "primary_query": "разбор назначения платежа правила ддс",
        "slug": "razbor-naznacheniya-platezha-pravila",
        "intent": "how_to",
        "tags": "назначение платежа правила ддс",
    },
    {
        "theme_key": "vendor_approval_sla",
        "short": "Очередь согласования оплат в Telegram",
        "h1": "Как собрать очередь согласования оплат поставщикам в Telegram с SLA",
        "primary_query": "согласование оплат telegram sla",
        "slug": "soglasovanie-oplat-telegram-sla",
        "intent": "workflow",
        "tags": "согласование оплаты telegram n8n",
    },
    {
        "theme_key": "upi_from_dds",
        "short": "Управленческий ОПиУ из ДДС",
        "h1": "Как собрать упрощённый управленческий ОПиУ из ДДС в Google Sheets",
        "primary_query": "управленческий опиу из ддс",
        "slug": "upravlencheskij-opiu-iz-dds",
        "intent": "how_to",
        "tags": "опиу ддс sheets управленческий",
    },
    {
        "theme_key": "fx_simple_mgmt",
        "short": "Курсовые разницы в управленке",
        "h1": "Как учитывать курсовые разницы в простой управленке на Google Sheets",
        "primary_query": "курсовые разницы управленческий учет sheets",
        "slug": "kursovye-raznicy-upravlencheskij-sheets",
        "intent": "how_to",
        "tags": "валюта курс sheets управленка",
    },
    {
        "theme_key": "salary_accrual_vs_pay",
        "short": "Сверка: начисление зарплаты ↔ банк",
        "h1": "Как сверить начисление зарплаты с выплатами из банка: таблица расхождений",
        "primary_query": "сверка зарплаты начисление и выплата",
        "slug": "sverka-zarplaty-nachislenie-vyplata",
        "intent": "troubleshooting",
        "tags": "зарплата сверка банк excel",
    },
    {
        "theme_key": "edo_status_to_sheets",
        "short": "Статусы ЭДО в Sheets",
        "h1": "Как забирать статусы ЭДО (отправлен/подписан) в Google Sheets без ручного мониторинга",
        "primary_query": "статусы эдо google sheets",
        "slug": "statusy-edo-google-sheets",
        "intent": "workflow",
        "tags": "эдо sheets статусы автоматизация",
    },
    {
        "theme_key": "ar_abc_analysis",
        "short": "ABC по дебиторке за час",
        "h1": "Как сделать ABC-анализ дебиторки в Excel/Sheets и решить, кому звонить первым",
        "primary_query": "abc анализ дебиторской задолженности",
        "slug": "abc-analiz-debitorki-excel",
        "intent": "how_to",
        "tags": "дебиторка abc excel приоритизация",
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


def proposeable_count() -> int:
    """Topics that tick can actually propose (unpublished and not rejected)."""
    from excalibur_blog_telegram_notify import proposeable_count as _pc  # noqa: WPS433

    return _pc()


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
    theme = (angle.get("theme_key") or "").strip() or "unset"
    card = f"""
---

## {topic_id} — {angle['short']}

- **priority:** P0
- **slug:** {angle['slug']}
- **theme_key:** {theme}
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
    used_themes: set[str] = set()
    for t in existing:
        used_themes |= theme_keys_for(t)

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
        theme = (angle.get("theme_key") or "").strip().lower()
        if slug in used_slugs or pq in used_q:
            print(f"SKIP slug/query used: {slug}", flush=True)
            continue
        if theme and theme in used_themes:
            print(f"SKIP theme_key used: {theme}", flush=True)
            continue
        warns = check_overlap(
            angle["primary_query"],
            existing,
            published,
            h1=angle["h1"],
            slug=angle["slug"],
            theme_key=theme,
            short=angle.get("short", ""),
        )
        if is_blocked(warns):
            hit = warns[0]["topic_id"] if warns else "?"
            print(f"SKIP semantic dup vs {hit}: {angle['h1'][:70]}", flush=True)
            continue

        topic_id = next_topic_id()
        tag_hits = [t for t in angle.get("tags", "").split() if t.lower() in trend_blob]
        evidence = "tags:" + ",".join(tag_hits) if tag_hits else "rotation"
        append_card(topic_id, angle, evidence=evidence)
        row_topic = {
            "topic_id": topic_id,
            "h1": angle["h1"],
            "primary_query": angle["primary_query"],
            "slug": angle["slug"],
            "theme_key": theme,
            "short": angle.get("short", ""),
            "priority": "P0",
        }
        existing.append(row_topic)
        used_slugs.add(slug)
        used_q.add(pq)
        used_themes |= theme_keys_for(row_topic)
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

КРИТИЧНО — анти-парафраз:
- Не предлагай ту же работу другими словами (job-to-be-done должен быть новым).
- Запрещены вариации уже закрытых кластеров: банковская выписка/staging, сверка банк↔учёт, план-факт/бюджет-факт, выгрузка 1С→Excel/OData, ИИ/Cursor для Excel-формул, дайджест собственнику, дебиторка+напоминания, Make vs n8n.
- Перед добавлением проверь:
  python scripts/excalibur_blog_scout_helper.py --check-query "..." --h1 "..." --slug "..." --theme-key "snake_case_job"
  Если exit code 1 / OVERLAP — тему НЕ добавляй.
- В карточке обязательно поле **theme_key:** уникальный snake_case job id.

Не дублируй опубликованные slug и карточки в blog-topics.md.
Используй web search по свежим трендам. Wordstat — если MCP доступен; иначе честно пометь demand: unknown.
Каждую тему добавь карточкой в конец memory/topics/blog-topics.md (перед секцией Архив, если есть).
article_mode только B. search_intent: how_to|checklist|comparison|troubleshooting|workflow.
После правок: git add/commit/push в master с сообщением "chore(blog): scout refill topics".
В финальном ответе JSON: {{"added":[{{"topic_id","h1","slug","primary_query","theme_key"}}]}}
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
    proposeable = proposeable_count()
    # Critical: rejected-but-unpublished used to fake a "full" queue and block Scout forever
    if not args.force and proposeable >= args.min_unpublished:
        print(
            json.dumps(
                {
                    "ok": True,
                    "action": "skip",
                    "unpublished": left,
                    "proposeable": proposeable,
                },
                ensure_ascii=False,
            )
        )
        return 0
    if proposeable == 0 and not args.force:
        # Always refill when tick has nothing to offer
        args.force = True

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
            from excalibur_blog_telegram_notify import cooldown_ready, cooldown_touch  # noqa: WPS433

            token, chat_id = require_creds()
            if added:
                lines = "\n".join(f"• {a['topic_id']}: {a['h1']}" for a in added)
                send_text(token, chat_id, f"🔎 Scout дозаправил очередь ({mode}):\n{lines}")
            elif mode == "cursor_cloud":
                send_text(token, chat_id, "🔎 Scout (Cursor Cloud) запущен — новые темы скоро в blog-topics.md")
            elif cooldown_ready("scout_exhausted", 24 * 3600):
                send_text(
                    token,
                    chat_id,
                    "🔎 Scout: банк углов исчерпан или всё в overlap. (не чаще 1×/сутки)",
                )
                cooldown_touch("scout_exhausted")
        except SystemExit:
            pass

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
