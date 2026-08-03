#!/usr/bin/env python3
"""Helper for Excalibur BLOG Scout: next IDs + semantic cannibalization guard.

Compares not only primary_query tokens, but h1+slug+query with synonym collapse
and explicit theme_key clusters (job-to-be-done). Paraphrases of the same job
must be blocked even when wording differs.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


STOP = {
    "в", "на", "и", "или", "с", "по", "для", "как", "что", "это", "без", "из",
    "к", "от", "за", "а", "не", "то", "же", "ли", "бы", "через", "при", "под",
    "the", "a", "an", "to", "of", "vs", "или", "чтобы", "который", "которые",
}

# Collapse paraphrases to the same stem before Jaccard.
SYNONYMS: dict[str, str] = {
    "выписка": "bankstmt",
    "выписки": "bankstmt",
    "выписку": "bankstmt",
    "банковская": "bank",
    "банковской": "bank",
    "банковскую": "bank",
    "банка": "bank",
    "банк": "bank",
    "сверка": "reconcile",
    "сверить": "reconcile",
    "сверки": "reconcile",
    "взаиморасчет": "reconcile",
    "взаиморасчётов": "reconcile",
    "взаиморасчетов": "reconcile",
    # не мапить голое «план» → иначе «план счетов» = plan-fakt
    "планфакт": "planfakt",
    "план-факт": "planfakt",
    "бюджет": "budget",
    "факт": "fact",
    "выгрузка": "export1c",
    "выгрузить": "export1c",
    "импорт": "export1c",
    "odata": "export1c",
    "формула": "excelformula",
    "формулы": "excelformula",
    "формулу": "excelformula",
    "нейросеть": "ai",
    "chatgpt": "ai",
    "claude": "ai",
    "ollama": "localllm",
    "дебиторка": "ar",
    "дебиторкой": "ar",
    "дебиторской": "ar",
    "дебиторку": "ar",
    "просрочки": "ar",
    "напоминание": "remind",
    "напоминания": "remind",
    "напомнить": "remind",
    "календарь": "paycal",
    "платёжный": "paycal",
    "платежный": "paycal",
    "staging": "bankstmt",
    "категор": "ddscat",
    "категории": "ddscat",
    "категоризация": "ddscat",
    "справочник": "ddscat",
    "дайджест": "digest",
    "отчёт": "report",
    "отчет": "report",
    "собственнику": "owner",
    "google": "sheets",
    "sheets": "sheets",
    "excel": "excel",
    "cursor": "cursor",
    "n8n": "n8n",
    "make": "make",
    "apps": "appsscript",
    "script": "appsscript",
    "power": "powerquery",
    "query": "powerquery",
    "закрытия": "monthclose",
    "месяца": "monthclose",
    "акт": "actrecon",
    "акты": "actrecon",
    "договор": "contract",
    "договоров": "contract",
    "комиссию": "bankfee",
    "комиссия": "bankfee",
    "лимит": "budgetlimit",
    "лимиты": "budgetlimit",
    "looker": "looker",
    "дашборд": "dashboard",
    "dashboard": "dashboard",
    "обезличивание": "privacy",
    "безопасность": "privacy",
    "пдн": "privacy",
}

# Hard job clusters: if any token set matches existing theme → block.
# Keys are stable theme_ids used in ANGLE_BANK and inferred from cards.
THEME_RULES: list[tuple[str, set[str]]] = [
    ("bank_statement_ingest", {"bankstmt", "sheets"}),
    ("bank_statement_ingest", {"bankstmt", "excel"}),
    ("bank_statement_ingest", {"bankstmt", "staging"}),
    ("bank_reconcile", {"bankstmt", "reconcile"}),
    ("bank_reconcile", {"bank", "reconcile", "1c"}),
    ("bank_reconcile", {"bank", "reconcile", "1с"}),
    ("bank_reconcile", {"bank", "reconcile", "учет"}),
    ("bank_reconcile", {"bank", "reconcile", "учёта"}),
    ("plan_fakt", {"planfakt"}),
    ("plan_fakt", {"budget", "fact"}),
    ("plan_fakt", {"budget", "dds"}),
    ("plan_fakt", {"fact", "dds", "sheets"}),
    # Только явный контур выгрузки/импорта 1С↔Excel/OData (не любое упоминание «выгрузки 1С»).
    ("export_1c_excel", {"odata"}),
    ("export_1c_excel", {"export1c", "унф", "excel"}),
    ("export_1c_excel", {"export1c", "excel", "регуляр"}),
    ("ai_excel_formulas", {"excelformula", "ai"}),
    ("ai_excel_formulas", {"excelformula", "cursor"}),
    ("ar_reminders", {"ar", "remind"}),
    ("payment_calendar", {"paycal"}),
    ("dds_categories", {"ddscat"}),
    ("owner_digest", {"digest"}),
    ("owner_digest", {"owner", "telegram"}),
    ("make_vs_n8n", {"make", "n8n"}),
    ("apps_script_vs_n8n", {"appsscript", "n8n"}),
    ("act_reconciliation_registry", {"actrecon", "reestr"}),
    ("act_reconciliation_registry", {"actrecon", "реестр"}),
    ("power_query_refresh", {"powerquery"}),
    ("local_llm_finance", {"localllm"}),
    ("chatgpt_privacy_checklist", {"privacy", "ai"}),
    ("chatgpt_privacy_checklist", {"privacy", "chatgpt"}),
]


def project_root() -> Path:
    return Path(__file__).resolve().parents[1]


def load_published_topics(root: Path) -> set[str]:
    ledger_path = root / "shared/published-articles.md"
    published = set()
    if not ledger_path.is_file():
        return published
    for line in ledger_path.read_text(encoding="utf-8").splitlines():
        if line.startswith("| 20"):
            cells = [c.strip() for c in line.split("|")]
            if len(cells) >= 3:
                published.add(cells[1].upper())
    return published


def load_existing_topics(root: Path) -> list[dict[str, str]]:
    topics_path = root / "memory/topics/blog-topics.md"
    topics: list[dict[str, str]] = []
    if not topics_path.is_file():
        return topics
    text = topics_path.read_text(encoding="utf-8")
    for match in re.finditer(r"##\s+(B\d+)\s+—\s*([^\n]*)\n(.*?)(?=\n---|\n##\s+B|\Z)", text, re.DOTALL):
        topic_id = match.group(1).upper()
        short = match.group(2).strip()
        block = match.group(3)

        def field(name: str) -> str:
            m = re.search(rf"(?:-|\*)\s*\*\*{re.escape(name)}:\*\*\s*(.+)", block, re.IGNORECASE)
            if not m:
                m = re.search(rf"\*\*{re.escape(name)}:\*\*\s*(.+)", block, re.IGNORECASE)
            return m.group(1).strip() if m else ""

        topics.append(
            {
                "topic_id": topic_id,
                "short": short,
                "h1": field("h1"),
                "primary_query": field("primary_query"),
                "slug": field("slug"),
                "theme_key": field("theme_key"),
                "priority": field("priority"),
            }
        )
    return topics


def _stem_token(w: str) -> str:
    w = w.strip().lower()
    if not w or w in STOP:
        return ""
    if w in SYNONYMS:
        return SYNONYMS[w]
    # prefix synonym match (категор*, дебитор*)
    for src, dst in SYNONYMS.items():
        if len(src) >= 4 and w.startswith(src[:5]):
            return dst
    return w[:6] if len(w) > 5 else w


def normalize_and_tokenize(text: str) -> set[str]:
    text = (text or "").lower().replace("ё", "е")
    text = text.replace("-", " ")
    text = re.sub(r"[^\w\s]", " ", text, flags=re.UNICODE)
    tokens = set()
    for w in text.split():
        st = _stem_token(w)
        if st:
            tokens.add(st)
    return tokens


def fingerprint(topic: dict[str, str]) -> set[str]:
    blob = " ".join(
        [
            topic.get("h1", ""),
            topic.get("short", ""),
            topic.get("primary_query", ""),
            (topic.get("slug") or "").replace("-", " "),
            topic.get("theme_key", ""),
        ]
    )
    return normalize_and_tokenize(blob)


def infer_theme_keys(tokens: set[str]) -> set[str]:
    found: set[str] = set()
    for theme, need in THEME_RULES:
        if need.issubset(tokens):
            found.add(theme)
    return found


def theme_keys_for(topic: dict[str, str]) -> set[str]:
    keys: set[str] = set()
    explicit = (topic.get("theme_key") or "").strip().lower()
    if explicit:
        keys.add(explicit)
    keys |= infer_theme_keys(fingerprint(topic))
    return keys


def jaccard(a: set[str], b: set[str]) -> float:
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


def check_overlap(
    new_query: str,
    existing_topics: list[dict[str, str]],
    published_ids: set[str],
    *,
    h1: str = "",
    slug: str = "",
    theme_key: str = "",
    short: str = "",
) -> list[dict[str, Any]]:
    """Block paraphrases of the same job, not only exact primary_query matches."""
    candidate = {
        "h1": h1,
        "short": short,
        "primary_query": new_query,
        "slug": slug,
        "theme_key": theme_key,
    }
    new_fp = fingerprint(candidate)
    # If only query passed (CLI --check-query), still fingerprint it.
    if not new_fp:
        new_fp = normalize_and_tokenize(new_query)
    new_themes = theme_keys_for(candidate)
    warnings: list[dict[str, Any]] = []

    for t in existing_topics:
        status = "published" if t["topic_id"] in published_ids else "in_pool"
        ext_fp = fingerprint(t)
        ext_themes = theme_keys_for(t)
        theme_hit = sorted(new_themes & ext_themes)
        sim = jaccard(new_fp, ext_fp)
        pq_exact = (
            (t.get("primary_query") or "").strip().lower() == (new_query or "").strip().lower()
            and bool(new_query.strip())
        )
        slug_exact = (
            (t.get("slug") or "").strip().lower() == (slug or "").strip().lower() and bool(slug.strip())
        )

        if theme_hit or pq_exact or slug_exact or sim >= 0.42:
            sev = "CRITICAL" if (theme_hit or pq_exact or slug_exact or sim >= 0.55) else "WARNING"
            warnings.append(
                {
                    "severity": sev,
                    "topic_id": t["topic_id"],
                    "similarity": round(sim, 2),
                    "status": status,
                    "theme_collision": theme_hit,
                    "message": (
                        f"{'THEME '+','.join(theme_hit)+' / ' if theme_hit else ''}"
                        f"overlap {round(sim*100)}% with {t['topic_id']} ({status}). "
                        f"Existing: '{t.get('h1') or t.get('primary_query')}'"
                    ),
                }
            )
        elif sim >= 0.30:
            warnings.append(
                {
                    "severity": "WARNING",
                    "topic_id": t["topic_id"],
                    "similarity": round(sim, 2),
                    "status": status,
                    "theme_collision": [],
                    "message": (
                        f"Soft overlap ({round(sim*100)}%) with {t['topic_id']} ({status}). "
                        f"Query/H1 may be too close: '{t.get('h1') or t.get('primary_query')}'"
                    ),
                }
            )
    return warnings


def is_blocked(warnings: list[dict[str, Any]], *, soft_block: float = 0.36) -> bool:
    for w in warnings:
        if w.get("severity") == "CRITICAL":
            return True
        if w.get("severity") == "WARNING" and float(w.get("similarity") or 0) >= soft_block:
            return True
        if w.get("theme_collision"):
            return True
    return False


def main() -> int:
    ap = argparse.ArgumentParser(description="Helper for Excalibur BLOG Scout Agent")
    ap.add_argument("--suggest-next", action="store_true", help="Print next available Topic ID and summary")
    ap.add_argument("--check-query", type=str, default="", help="Check primary query (legacy)")
    ap.add_argument("--h1", type=str, default="", help="Optional H1 for semantic check")
    ap.add_argument("--slug", type=str, default="", help="Optional slug for semantic check")
    ap.add_argument("--theme-key", type=str, default="", help="Optional theme_key / job cluster")
    ap.add_argument("--dump-themes", action="store_true", help="Print inferred themes for all cards")
    args = ap.parse_args()

    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8")

    root = project_root()
    published = load_published_topics(root)
    existing = load_existing_topics(root)

    if args.dump_themes:
        for t in existing:
            print(f"{t['topic_id']}: {sorted(theme_keys_for(t))} | {t.get('h1','')[:70]}")
        return 0

    if args.suggest_next:
        print("=== EXCALIBUR SCOUT HELPER ===")
        max_num = 0
        for t in existing:
            m = re.match(r"B(\d+)", t["topic_id"])
            if m:
                max_num = max(max_num, int(m.group(1)))
        next_id = f"B{max_num + 1:02d}"
        print(f"Next available topic ID: {next_id}")
        print(f"Total topics in pool (blog-topics.md): {len(existing)}")
        print(f"Total articles written/in_progress: {len(published)}")
        unwritten = [t["topic_id"] for t in existing if t["topic_id"] not in published]
        print(f"Unwritten topic IDs in pool: {unwritten}")
        return 0

    if args.check_query or args.h1 or args.slug or args.theme_key:
        warnings = check_overlap(
            args.check_query,
            existing,
            published,
            h1=args.h1,
            slug=args.slug,
            theme_key=args.theme_key,
        )
        if warnings:
            print("❌ OVERLAP DETECTED:")
            for w in warnings:
                print(f"  [{w['severity']}] Similarity: {w['similarity']} | Topic: {w['topic_id']} ({w['status']})")
                if w.get("theme_collision"):
                    print(f"  Theme: {w['theme_collision']}")
                print(f"  Message: {w['message']}")
            return 1 if is_blocked(warnings) else 0
        print("✅ NO CANNIBALIZATION RISK: Query is clean and unique.")
        return 0

    ap.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
