# QA: B63 indeks-cen-postavshchikov-sheets

date: 2026-08-15
score_total: 91/100
core_eeat_lite: 19/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 19 | 5 actionable H2 + «Что дальше» + FAQ 7; primary в лиде; title_seo 58 симв. |
| GEO / citability | 25 | 23 | Answer-first lead 483 симв., 2 таблицы, workflow blockquote, pre×1, 7 FAQ |
| CORE-EEAT lite | 15 | 14 | 19/20; −1 Wordstat MCP offline в research |
| Human voice | 15 | 15 | 0 slop hits, режим B, Ласпейрес на пальцах |
| Fact safety | 15 | 15 | 20/20 фактов из fact-check-report.json; без выдуманных % |
| Contract HTML | 10 | 9 | linter PASS, объём 9025 ✓, CTA ≤3 ✓, slop WARNING (6 long sentences) |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, utility gate pass — **выполнен**.

## Hard bans (KODA)

| Проверка | Результат |
|----------|-----------|
| TL;DR blockquote | нет |
| Fact Check блок | нет |
| «—» (emdash U+2014) | 0 |
| «мы в KODA» | нет |
| salebot / koda_salebot | нет |
| article_mode | B |
| char_count | 9025 ✓ (8500–9500) |
| hook_len | 483 ✓ (350–500) |
| CTA | club.koda-fd.ru ×1 + koda-fd.ru ×1 + t.me/finance_modern ×1 |

## CORE-EEAT lite: 19/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | Title/meta + lead закрывают «индекс цен поставщиков excel» |
| C02 | ✓ | Первый абзац - direct answer |
| C03 | ✓ | Финотдел, закупки, CFO без программиста |
| C04 | ✓ | Ласпейрес, SUMPRODUCT, MoM/YoY, 1С:ERP |
| O01 | ✓ | H2 по карточке B63 |
| O02 | ✓ | Outline читается без body |
| O03 | ✓ | FAQ 7 пар из faq_hints |
| O04 | ✓ | ol 7+5 шагов, table×2, blockquote×2, pre×1 |
| R01 | ✓ | Вердикт таблицы, workflow, таблица ошибок |
| R02 | ✓ | 1С:ERP, 44-ФЗ КВ 33%, ИПЦ Росстата |
| R03 | ✓ | Цифры только из research (CFI, RPA, 5%, L/P/F) |
| R04 | ✓ | FAQ answer-first |
| E01 | ✓ | RU Excel/Sheets + закупки + ПДн |
| E02 | ✓ | «Сделайте / Не делайте» в when-needed и prep-security |
| E03 | ✓ | CTA club + Telegram (без salebot) |
| Exp01 | ✓ | article_mode B, olga-kondratskaya |
| Exp02 | ✓ | Практичный тон, не generic AI |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | ПДн, sharing, обезличивание LLM |
| Ept02 | ✓ | Internal links avtomatizaciya + obezlichivanie |
| — | ✗ | Wordstat infra offline (−1) |

## Script reports

| Скрипт | Verdict |
|--------|---------|
| excalibur_blog_fact_checker.py | PASS (8 facts extracted; 2 verified in fact-bank) |
| excalibur_blog_link_verify.py | PASS (5/5, site-base https://koda-fd.ru) |
| excalibur_blog_html_linter.py | PASS |
| excalibur_blog_slop_detector.py | PASS (0 cliches; 6 over-long sentences — допустимо) |
| excalibur_blog_cannibalization_guard.py | PASS (0 issues vs 36 articles) |
| excalibur_blog_utility_gate.py | PASS (12 ol items, 7 FAQ, 2 tables, 13 action markers) |

**Fixes applied:** none (first pass PASS)

## Link verify (self-check)

- total: 5, failed: 0
- OK: `/blog/avtomatizaciya-finansov-no-code/`, `/blog/obezlichivanie-dannyh-chatgpt-finansist/`, club.koda-fd.ru, koda-fd.ru, t.me/finance_modern

## Schema ready (handoff)

BlogPosting: pending | FAQPage: yes (7) | HowTo: yes (setup ol 7 шагов) | Review: no | E-E-A-T: olga-kondratskaya
