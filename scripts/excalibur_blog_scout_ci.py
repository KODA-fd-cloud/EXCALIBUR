#!/usr/bin/env python3
"""CI Scout: find fresh utility-only topics for KODA blog and append to blog-topics.md.

Strategy:
  1) Optional Cursor Cloud Scout (Excalibur Scout skill: WebSearch + Wordstat + cards)
     — auto when queue empty or --prefer-cursor
  2) Local web Scout: curated ANGLE_BANK scored by live DDG trends
     (SERP titles are signals ONLY — never pasted as H1)
  3) Cannibalization guard (theme_key + semantic overlap)

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
    f"вайб кодинг финансы {YEAR}",
    f"cursor ai mcp финансы {YEAR}",
    f"mcp сервер 1с api",
    f"интеграция google sheets api финансы",
    f"http сервис 1с веб сервис финансы",
    f"cursor api автоматизация финотдел",
    f"приложение для финансиста no code {YEAR}",
    f"управленческий учет google sheets {YEAR}",
    f"1с odata google sheets",
    f"claude code финансы вайбкодинг",
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
        "theme_key": "mcp_1c_fin_read",
        "short": "MCP: чтение данных 1С из Cursor",
        "h1": "Как подключить MCP к 1С: читать остатки и обороты прямо из Cursor",
        "primary_query": "mcp 1с cursor финансы",
        "slug": "mcp-1c-cursor-ostatki-oboroty",
        "intent": "how_to",
        "tags": "mcp 1с cursor api интеграция",
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
        "tags": "согласование оплаты telegram интеграция",
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
    # --- refill 2026-08 (после выгорания банка) ---
    {
        "theme_key": "ap_aging_report",
        "short": "Aging кредиторки в Sheets",
        "h1": "Как собрать aging кредиторской задолженности в Google Sheets за вечер",
        "primary_query": "aging кредиторской задолженности excel",
        "slug": "aging-kreditorki-google-sheets",
        "intent": "how_to",
        "tags": "кредиторка aging sheets оплата",
    },
    {
        "theme_key": "corp_card_to_dds",
        "short": "Корпоративные карты → ДДС",
        "h1": "Как разносить выписку корпоративных карт в статьи ДДС без ручного копипаста",
        "primary_query": "корпоративные карты ддс google sheets",
        "slug": "korporativnye-karty-dds-sheets",
        "intent": "workflow",
        "tags": "корпоративные карты ддс sheets",
    },
    {
        "theme_key": "tax_calendar_alerts",
        "short": "Налоговый календарь с алертами",
        "h1": "Как вести налоговый календарь малого бизнеса в Google Sheets с напоминаниями",
        "primary_query": "налоговый календарь google sheets",
        "slug": "nalogovyj-kalendar-google-sheets",
        "intent": "workflow",
        "tags": "налоги календарь sheets напоминания",
    },
    {
        "theme_key": "margin_by_project",
        "short": "Маржа по проектам в Sheets",
        "h1": "Как считать маржу по проектам в Google Sheets: выручка, прямые, вклад",
        "primary_query": "маржа по проектам google sheets",
        "slug": "marzha-po-proektam-google-sheets",
        "intent": "how_to",
        "tags": "маржа проекты sheets управленка",
    },
    {
        "theme_key": "unit_economics_services",
        "short": "Unit-экономика услуг",
        "h1": "Как собрать unit-экономику услуг в Google Sheets без сложной BI",
        "primary_query": "unit экономика услуг google sheets",
        "slug": "unit-ekonomika-uslug-sheets",
        "intent": "how_to",
        "tags": "unit экономика услуги sheets",
    },
    {
        "theme_key": "expense_request_forms",
        "short": "Заявки на расход через Forms",
        "h1": "Как принимать заявки на расход через Google Forms в реестр Sheets",
        "primary_query": "заявка на расход google forms",
        "slug": "zayavka-na-rashod-google-forms",
        "intent": "workflow",
        "tags": "заявки forms sheets согласование",
    },
    {
        "theme_key": "capex_opex_tracker",
        "short": "Трекер CAPEX vs OPEX",
        "h1": "Как разделить CAPEX и OPEX в управленке на Google Sheets",
        "primary_query": "capex opex google sheets",
        "slug": "capex-opex-google-sheets",
        "intent": "how_to",
        "tags": "capex opex sheets управленческий",
    },
    {
        "theme_key": "weekly_cash_pack",
        "short": "Пакет к cash-meeting за 30 минут",
        "h1": "Как собрать пакет к еженедельному cash-meeting за 30 минут из Sheets",
        "primary_query": "подготовка к cash meeting финансы",
        "slug": "paket-k-cash-meeting-sheets",
        "intent": "checklist",
        "tags": "cash meeting sheets cfo чеклист",
    },
    {
        "theme_key": "vibe_coding_payment_registry",
        "short": "Вайб-кодинг: реестр оплат из PDF",
        "h1": "Как вайбкодингом в Cursor собрать из PDF счёта строку реестра оплат",
        "primary_query": "вайб кодинг cursor pdf счет реестр",
        "slug": "vibe-coding-pdf-schet-v-reestr",
        "intent": "workflow",
        "tags": "вайбкодинг cursor pdf реестр api",
    },
    {
        "theme_key": "http_service_1c_apps",
        "short": "HTTP-сервис 1С под своё приложение",
        "h1": "Как опубликовать HTTP-сервис 1С и дергать его из своего приложения финотдела",
        "primary_query": "http сервис 1с приложение финансы",
        "slug": "http-servis-1c-prilozhenie-finotdel",
        "intent": "how_to",
        "tags": "http веб-сервис 1с api приложение",
    },
    {
        "theme_key": "sheets_api_integration",
        "short": "Google Sheets API в контуре финотдела",
        "h1": "Как интегрировать Google Sheets API: сервисный аккаунт, scopes, запись из скрипта",
        "primary_query": "google sheets api сервисный аккаунт финансы",
        "slug": "google-sheets-api-integraciya-finotdel",
        "intent": "how_to",
        "tags": "sheets api интеграция сервисный аккаунт",
    },
    {
        "theme_key": "travel_expense_table",
        "short": "Командировки: таблица расходов",
        "h1": "Как вести расходы по командировкам в Google Sheets: суточные, билеты, лимиты",
        "primary_query": "учет командировочных расходов google sheets",
        "slug": "komandirovochnye-rashody-google-sheets",
        "intent": "workflow",
        "tags": "командировки sheets суточные лимиты",
    },
    {
        "theme_key": "vat_upd_registry",
        "short": "Реестр УПД / счетов-фактур",
        "h1": "Как вести реестр УПД и счетов-фактур в Google Sheets без потери комплекта",
        "primary_query": "реестр упд google sheets",
        "slug": "reestr-upd-google-sheets",
        "intent": "workflow",
        "tags": "упд счет-фактура sheets реестр",
    },
    {
        "theme_key": "finance_folder_acl",
        "short": "Права на финпапки Drive",
        "h1": "Как настроить права доступа к финансовым папкам Google Drive без утечек",
        "primary_query": "права доступа google drive финотдел",
        "slug": "prava-dostupa-drive-finotdel",
        "intent": "checklist",
        "tags": "drive права безопасность финотдел",
    },
    {
        "theme_key": "supplier_price_index",
        "short": "Индекс цен поставщиков",
        "h1": "Как считать индекс изменения цен поставщиков в Excel/Sheets",
        "primary_query": "индекс цен поставщиков excel",
        "slug": "indeks-cen-postavshchikov-sheets",
        "intent": "how_to",
        "tags": "поставщики цены индекс sheets",
    },
    {
        "theme_key": "deferred_revenue_simple",
        "short": "Отложенная выручка упрощённо",
        "h1": "Как учитывать отложенную выручку в простой управленке на Google Sheets",
        "primary_query": "отложенная выручка управленческий учет sheets",
        "slug": "otlozhennaya-vyruchka-sheets",
        "intent": "how_to",
        "tags": "отложенная выручка sheets управленка",
    },
    {
        "theme_key": "board_one_pager",
        "short": "One-pager для собственника",
        "h1": "Как собрать one-pager для собственника из Sheets: 1 экран, 5 цифр",
        "primary_query": "one pager для собственника финансы",
        "slug": "one-pager-sobstvenniku-sheets",
        "intent": "how_to",
        "tags": "one pager собственник sheets cfo",
    },
    {
        "theme_key": "leasing_schedule_sheets",
        "short": "График лизинга в Sheets",
        "h1": "Как вести график лизинговых платежей в Google Sheets и не пропустить дату",
        "primary_query": "график лизинговых платежей excel",
        "slug": "grafik-lizinga-google-sheets",
        "intent": "workflow",
        "tags": "лизинг график sheets платежи",
    },
    {
        "theme_key": "employee_loan_registry",
        "short": "Реестр займов сотрудникам",
        "h1": "Как вести реестр займов сотрудникам в Google Sheets: выдача, % , остаток",
        "primary_query": "реестр займов сотрудникам excel",
        "slug": "reestr-zajmov-sotrudnikam-sheets",
        "intent": "workflow",
        "tags": "займы сотрудники sheets реестр",
    },
    {
        "theme_key": "chatgpt_dds_rules_only",
        "short": "Промпт правил ДДС без сырых выписок",
        "h1": "Как описать правила категоризации ДДС для ChatGPT без сырых выписок",
        "primary_query": "правила категоризации ддс chatgpt",
        "slug": "pravila-kategorizacii-dds-chatgpt",
        "intent": "how_to",
        "tags": "chatgpt ддс правила безопасность",
    },
    # --- refill 2026-08-19 after killing DDG-title invent ---
    {
        "theme_key": "vendor_scorecard_sheets",
        "short": "Скоркард поставщиков в Sheets",
        "h1": "Как вести скоркард поставщиков в Google Sheets: сроки, брак, цена",
        "primary_query": "оценка поставщиков google sheets",
        "slug": "skorkard-postavshchikov-google-sheets",
        "intent": "workflow",
        "tags": "поставщики scorecard sheets закупки",
    },
    {
        "theme_key": "cash_in_forecast_30d",
        "short": "Прогноз поступлений на 30 дней",
        "h1": "Как спрогнозировать поступления на 30 дней в Google Sheets по открытым счетам",
        "primary_query": "прогноз поступлений google sheets",
        "slug": "prognoz-postuplenij-30-dnej-sheets",
        "intent": "how_to",
        "tags": "поступления прогноз sheets дебиторка",
    },
    {
        "theme_key": "approval_matrix_payments",
        "short": "Матрица согласования платежей",
        "h1": "Как завести матрицу согласования платежей в Google Sheets по суммам и ролям",
        "primary_query": "матрица согласования платежей excel",
        "slug": "matrica-soglasovaniya-platezhej-sheets",
        "intent": "workflow",
        "tags": "согласование матрица платежи sheets",
    },
    {
        "theme_key": "bank_statement_rules_engine",
        "short": "Движок правил для выписки",
        "h1": "Как настроить таблицу правил разнесения выписки: приоритет, исключения, тест",
        "primary_query": "правила разнесения банковской выписки",
        "slug": "pravila-razneseniya-vypiski-sheets",
        "intent": "how_to",
        "tags": "выписка правила ддс sheets",
    },
    {
        "theme_key": "cfo_weekly_metrics",
        "short": "5 метрик CFO на неделю",
        "h1": "Как собрать еженедельные 5 метрик CFO в одной вкладке Google Sheets",
        "primary_query": "еженедельные метрики cfo google sheets",
        "slug": "ezhenedelnye-metriki-cfo-sheets",
        "intent": "checklist",
        "tags": "cfo метрики sheets неделя",
    },
    {
        "theme_key": "refund_registry",
        "short": "Реестр возвратов покупателям",
        "h1": "Как вести реестр возвратов покупателям в Google Sheets без потери статусов",
        "primary_query": "реестр возвратов покупателям excel",
        "slug": "reestr-vozvratov-pokupatelyam-sheets",
        "intent": "workflow",
        "tags": "возвраты реестр sheets продажи",
    },
    {
        "theme_key": "prepaid_expense_tracker",
        "short": "Учёт авансов выданных поставщикам",
        "h1": "Как контролировать авансы поставщикам в Google Sheets: выдача, зачёт, остаток",
        "primary_query": "учет авансов поставщикам google sheets",
        "slug": "avansy-postavshchikam-google-sheets",
        "intent": "workflow",
        "tags": "авансы поставщики sheets контроль",
    },
    {
        "theme_key": "inventory_writeoff_finance",
        "short": "Списания ТМЦ глазами финансиста",
        "h1": "Как учитывать списания ТМЦ в управленке на Google Sheets",
        "primary_query": "списание тмц управленческий учет sheets",
        "slug": "spisanie-tmc-upravlencheskij-sheets",
        "intent": "how_to",
        "tags": "тмц списание sheets управленка",
    },
    {
        "theme_key": "subscription_saas_costs",
        "short": "Реестр SaaS-подписок компании",
        "h1": "Как вести реестр SaaS-подписок и не платить за мёртвые лицензии",
        "primary_query": "реестр saas подписок компания",
        "slug": "reestr-saas-podpisok-sheets",
        "intent": "workflow",
        "tags": "saas подписки sheets затраты",
    },
    {
        "theme_key": "dividend_calendar_owner",
        "short": "Календарь дивидендов / изъятий",
        "h1": "Как вести календарь изъятий собственника в Google Sheets без путаницы с ДДС",
        "primary_query": "календарь дивидендов собственника sheets",
        "slug": "kalendar-izyatiy-sobstvennika-sheets",
        "intent": "workflow",
        "tags": "дивиденды собственник sheets ддс",
    },
    # --- refill 2026-08-22: vibe-coding / MCP / API / apps (bank was empty) ---
    {
        "theme_key": "cursor_rules_finotdel",
        "short": "Cursor Rules под финотдел",
        "h1": "Как написать Cursor Rules для финотдела: чтобы агент не трогал ПДн и не ломал таблицы",
        "primary_query": "cursor rules финансы",
        "slug": "cursor-rules-finotdel-pdn",
        "intent": "how_to",
        "tags": "cursor rules вайбкодинг финотдел",
    },
    {
        "theme_key": "mcp_sheets_cursor",
        "short": "MCP Google Sheets в Cursor",
        "h1": "Как подключить MCP к Google Sheets в Cursor и править реестры без копипаста",
        "primary_query": "mcp google sheets cursor",
        "slug": "mcp-google-sheets-cursor-reestry",
        "intent": "how_to",
        "tags": "mcp sheets cursor api интеграция",
    },
    {
        "theme_key": "telegram_bot_expense_app",
        "short": "Telegram-бот заявок на расход",
        "h1": "Как сделать Telegram-бота заявок на расход: бот → Google Sheets через API",
        "primary_query": "telegram бот заявки на расход google sheets",
        "slug": "telegram-bot-zayavki-rashod-sheets-api",
        "intent": "workflow",
        "tags": "telegram bot api sheets приложение",
    },
    {
        "theme_key": "fastapi_odata_proxy",
        "short": "Прокси OData 1С на FastAPI",
        "h1": "Как сделать тонкий FastAPI-прокси к OData 1С: токен, лимиты, без пароля в Sheets",
        "primary_query": "fastapi odata 1с прокси",
        "slug": "fastapi-odata-1c-proxy-token",
        "intent": "how_to",
        "tags": "fastapi odata api веб-сервис 1с",
    },
    {
        "theme_key": "apps_script_webapp_approve",
        "short": "Web App согласования в Apps Script",
        "h1": "Как собрать Web App на Google Apps Script: кнопка «согласовать оплату» без n8n",
        "primary_query": "google apps script web app согласование оплаты",
        "slug": "apps-script-webapp-soglasovanie-oplaty",
        "intent": "workflow",
        "tags": "apps script webapp api приложение",
    },
    {
        "theme_key": "claude_code_csv_reconcile_app",
        "short": "Claude Code: локальная сверка CSV",
        "h1": "Как вайбкодингом в Claude Code собрать локальный скрипт сверки двух CSV без облака",
        "primary_query": "claude code сверка csv локально",
        "slug": "claude-code-lokalnaya-sverka-csv",
        "intent": "how_to",
        "tags": "claude code вайбкодинг csv сверка",
    },
    {
        "theme_key": "streamlit_dds_miniapp",
        "short": "Streamlit-миниапп ДДС",
        "h1": "Как за вечер собрать Streamlit-приложение: ДДС из Google Sheets с фильтрами",
        "primary_query": "streamlit google sheets ддс",
        "slug": "streamlit-dds-iz-google-sheets",
        "intent": "how_to",
        "tags": "streamlit приложение sheets ддс api",
    },
    {
        "theme_key": "http_service_1c_telegram_push",
        "short": "HTTP-сервис 1С → Telegram",
        "h1": "Как из HTTP-сервиса 1С слать алерт в Telegram при просроченной дебиторке",
        "primary_query": "http сервис 1с telegram дебиторка",
        "slug": "http-servis-1c-telegram-debitorka",
        "intent": "workflow",
        "tags": "http веб-сервис 1с telegram api",
    },
    {
        "theme_key": "cursor_skill_1c_export",
        "short": "Cursor Skill под выгрузки 1С",
        "h1": "Как оформить Cursor Skill «выгрузка из 1С»: чеклист, OData, типичные ошибки",
        "primary_query": "cursor skill 1с odata",
        "slug": "cursor-skill-vygruzka-1c-odata",
        "intent": "checklist",
        "tags": "cursor skill вайбкодинг 1с odata",
    },
    {
        "theme_key": "service_account_sheets_rotate",
        "short": "Ротация ключа service account",
        "h1": "Как ротировать ключ сервисного аккаунта Google Sheets API без простоя обновлений",
        "primary_query": "ротация ключа service account google sheets",
        "slug": "rotaciya-service-account-sheets-api",
        "intent": "how_to",
        "tags": "sheets api security интеграция",
    },
    {
        "theme_key": "mcp_filesystem_finance_vault",
        "short": "MCP filesystem для финфайлов",
        "h1": "Как настроить MCP filesystem к папке финотчётов: Cursor видит файлы, наружу не утекает",
        "primary_query": "mcp filesystem cursor финансы",
        "slug": "mcp-filesystem-finotchety-cursor",
        "intent": "how_to",
        "tags": "mcp filesystem cursor безопасность",
    },
    {
        "theme_key": "bank_api_statement_python",
        "short": "Выписка через API банка",
        "h1": "Как забрать банковскую выписку через API банка в Python и положить в Sheets",
        "primary_query": "api банка выписка python google sheets",
        "slug": "api-banka-vypiska-python-sheets",
        "intent": "how_to",
        "tags": "банк api python sheets интеграция",
    },
    {
        "theme_key": "webhook_receiver_fin_events",
        "short": "Webhook-приёмник финсобытий",
        "h1": "Как поднять простой webhook-приёмник: статусы оплат → строка в Google Sheets",
        "primary_query": "webhook оплата google sheets",
        "slug": "webhook-status-oplaty-google-sheets",
        "intent": "workflow",
        "tags": "webhook api приложение sheets",
    },
    {
        "theme_key": "vibe_coding_dash_plotly",
        "short": "Вайбкодинг: дашборд plotly",
        "h1": "Как вайбкодингом собрать дашборд ДДС на Plotly из CSV выгрузки за один вечер",
        "primary_query": "plotly дашборд ддс csv cursor",
        "slug": "vibe-coding-plotly-dds-dashboard",
        "intent": "how_to",
        "tags": "вайбкодинг plotly ддс cursor",
    },
    {
        "theme_key": "1c_http_json_post_invoice",
        "short": "HTTP POST счёта в 1С",
        "h1": "Как через HTTP-сервис создать черновик счёта в 1С из JSON своего приложения",
        "primary_query": "http сервис 1с создать счет json",
        "slug": "http-servis-1c-chernovik-scheta-json",
        "intent": "how_to",
        "tags": "http веб-сервис 1с api приложение",
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


def gather_trend_hits() -> list[dict[str, str]]:
    hits: list[dict[str, str]] = []
    for q in TREND_QUERIES:
        try:
            hits.extend(ddg_search(q, max_results=4))
        except Exception as e:
            print(f"search fail {q}: {e}", file=sys.stderr)
            continue
        time.sleep(0.5)
    return hits


def is_junk_h1(h1: str) -> bool:
    """Reject SERP paste / course roundups / brand tails — never publish as topic H1."""
    h = (h1 or "").strip()
    if len(h) < 20:
        return True
    low = h.lower()
    deny_sub = (
        "wikipedia",
        "udemy",
        "habr",
        "habab",
        "dtf",
        "flowframe",
        "sacra",
        "n8n.io",
        "make.com",
        "zapier",
        "топ-7",
        "top-7",
        "must-have",
        "q&a",
        " | ",
        " — top ",
        "revenue, funding",
        "statistics 2026",
        "(company)",
        "онлайн-курс",
        "журнал «",
        "ваш путь",
        "полный туториал",
    )
    if any(x in low for x in deny_sub):
        return True
    # Out of editorial focus
    if re.search(r"\b(n8n|make\.com|zapier)\b", low):
        return True
    # Broken invent grammar: «Как » + noun/brand, not verb how-to
    if re.match(r"^как\s+(автоматизация|обучение|система|ии|cursor|google|odata|n8n)\b", low):
        return True
    body = re.sub(r"^как\s+", "", low, flags=re.I)
    cyr = len(re.findall(r"[а-яё]", body))
    lat = len(re.findall(r"[a-z]", body))
    # Mostly English SERP title glued after «Как»
    if lat >= 25 and lat > cyr * 1.5:
        return True
    return False


def try_add_angle(
    angle: dict[str, str],
    *,
    existing: list[dict[str, str]],
    published: set[str],
    used_slugs: set[str],
    used_q: set[str],
    used_themes: set[str],
    evidence: str,
) -> dict[str, str] | None:
    if is_junk_h1(angle.get("h1", "")):
        print(f"SKIP junk H1: {angle.get('h1', '')[:70]}", flush=True)
        return None
    blob = f"{angle.get('h1','')} {angle.get('primary_query','')} {angle.get('slug','')} {angle.get('tags','')}".lower()
    if re.search(r"\b(n8n|zapier|make\.com)\b", blob) or re.search(r"(^|[\s:])make([\s:]|$)", blob):
        print(f"SKIP out-of-focus stack: {angle.get('h1', '')[:70]}", flush=True)
        return None
    slug = angle["slug"].lower()
    pq = angle["primary_query"].strip().lower()
    theme = (angle.get("theme_key") or "").strip().lower()
    if slug in used_slugs or pq in used_q:
        print(f"SKIP slug/query used: {slug}", flush=True)
        return None
    if theme and theme in used_themes:
        print(f"SKIP theme_key used: {theme}", flush=True)
        return None
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
        return None

    topic_id = next_topic_id()
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
    print(f"ADDED {topic_id}: {angle['h1']}", flush=True)
    return row


def scout_web(count: int) -> list[dict[str, str]]:
    existing = load_existing_topics(ROOT)
    published = load_published_topics(ROOT)
    pub_ids, pub_slugs = published_ids_and_slugs()
    used_slugs = {t.get("slug", "").lower() for t in existing} | pub_slugs
    used_q = {t.get("primary_query", "").strip().lower() for t in existing}
    used_themes: set[str] = set()
    for t in existing:
        used_themes |= theme_keys_for(t)

    print("Gathering live trend hits (DDG)…", flush=True)
    trend_hits = gather_trend_hits()
    trend_blob = " ".join(f"{h.get('title','')} {h.get('body','')}" for h in trend_hits).lower()
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
        tag_hits = [t for t in angle.get("tags", "").split() if t.lower() in trend_blob]
        evidence = "bank+tags:" + ",".join(tag_hits) if tag_hits else "bank+rotation"
        row = try_add_angle(
            angle,
            existing=existing,
            published=published,
            used_slugs=used_slugs,
            used_q=used_q,
            used_themes=used_themes,
            evidence=evidence,
        )
        if row:
            added.append(row)

    # SERP titles are competitor pages / course roundups — NEVER mint H1 from them.
    # Fresh topics: ANGLE_BANK + Cursor Cloud Scout (rewrites into utility cards).
    if len(added) < count:
        print(
            f"Bank filled {len(added)}/{count} — no DDG-title invent "
            f"(use Cloud Scout / expand ANGLE_BANK).",
            flush=True,
        )
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

Задача: найти {count} НОВЫЕ актуальные utility-only темы ({YEAR}), релевантные CFO/финотделу.

Фокус стека (только это):
- вайб-кодинг / Cursor / Claude Code
- интеграции (1С ↔ Sheets/Excel/Telegram/банк)
- MCP
- API
- веб-сервисы / HTTP-сервисы 1С
- свои приложения для финотдела
НЕ предлагай темы про Make, n8n, Zapier и подобные no-code оркестраторы.

КРИТИЧНО — H1 пишешь ТЫ, не копируешь выдачу:
- ЗАПРЕЩЕНО вставлять title страницы из SERP/DTF/Habr/Udemy/агентств как H1.
- ЗАПРЕЩЕНО: «Как » + чужой заголовок, «| бренд», «— Хабр», «ТОП-7 курсов», англ. clickbait без переписывания.
- H1 = нормальный русский how-to голос КОДА: «Как …», без мусора, без названия чужого сайта.
- SERP только как сигнал боли/спроса → ты формулируешь свою utility-карточку.

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

    # Cloud Scout = реальный Excalibur Scout (WebSearch + Wordstat + карточки).
    # Включаем автоматически при пустой очереди или по --prefer-cursor.
    use_cursor = bool(args.prefer_cursor) or proposeable == 0
    if use_cursor and os.environ.get("CURSOR_API_KEY", "").strip():
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

    # Локальный web Scout: ТОЛЬКО ANGLE_BANK (SERP titles = scoring signal, never H1)
    if mode == "web" or proposeable_count() < args.min_unpublished:
        web_added = scout_web(args.count)
        added.extend(web_added)
        if mode == "cursor_cloud" and web_added:
            mode = "cursor_cloud+web"
        elif mode != "cursor_cloud":
            mode = "web"
        print(
            json.dumps(
                {
                    "ok": True,
                    "action": "web_scout" if mode == "web" else "hybrid_scout",
                    "mode": mode,
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
                    "proposeable_after": proposeable_count(),
                },
                ensure_ascii=False,
            )
        )

    if args.notify:
        try:
            from excalibur_blog_telegram_notify import cooldown_ready, cooldown_touch  # noqa: WPS433

            token, chat_id = require_creds()
            if added:
                clean = [a for a in added if not is_junk_h1(a.get("h1", ""))]
                if not clean:
                    print("notify skipped: all added H1 failed junk gate", flush=True)
                else:
                    lines = "\n".join(f"• {a['topic_id']}: {a['h1']}" for a in clean)
                    send_text(token, chat_id, f"🔎 Scout дозаправил очередь ({mode}):\n{lines}")
            elif mode == "cursor_cloud":
                send_text(token, chat_id, "🔎 Scout (Cursor Cloud) запущен — новые темы скоро в blog-topics.md")
            elif cooldown_ready("scout_exhausted", 7 * 24 * 3600):
                # Одно starve-сообщение в сутки (синхрон с empty_queue)
                send_text(
                    token,
                    chat_id,
                    "🔎 Scout: свободных углов не осталось — дозаправка в коде/Cloud. "
                    "Это сообщение не чаще 1×/сутки.",
                )
                cooldown_touch("scout_exhausted")
        except SystemExit:
            pass

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
