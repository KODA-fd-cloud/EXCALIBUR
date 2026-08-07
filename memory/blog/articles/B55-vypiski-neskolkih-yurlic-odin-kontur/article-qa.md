# QA: B55 vypiski-neskolkih-yurlic-odin-kontur

date: 2026-08-07
score_total: 90/100
core_eeat_lite: 18/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 18 | 5 actionable H2 + «Что дальше» + FAQ 7; primary в лиде; WARN title_seo без «учет» |
| GEO / citability | 25 | 24 | Answer-first lead, 3 таблицы (инвентаризация/staging/маршруты), workflow blockquote, pre×1, FAQ 7 |
| CORE-EEAT lite | 15 | 14 | 18/20; −1 без Wordstat MCP (infra offline) |
| Human voice | 15 | 15 | 0 slop hits, режим B Ольга, отделение ЕГРЮЛ vs банковская выписка |
| Fact safety | 15 | 13 | ст. 29 ФЗ № 402-ФЗ (5 лет); 6/9 метрик unverified — примеры р/с и сроки внедрения |
| Contract HTML | 10 | 10 | linter PASS, объём 9060 ✓, CTA ≤3 ✓, без TOC/TL;DR/Fact Check |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate pass — **выполнен**.

## Hard bans (KODA)

| Проверка | Результат |
|----------|-----------|
| TL;DR | нет |
| Fact Check блок | нет |
| «—» (emdash U+2014) | 0 |
| «мы в KODA» | нет |
| salebot / koda_salebot | нет |
| article_mode | B |
| char_count | 9060 ✓ |
| CTA | t.me/finance_modern ×1 + club.koda-fd.ru ×1 |

## CORE-EEAT lite: 18/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | Title/meta + lead закрывают «выписки нескольких юрлиц один учёт» |
| C02 | ✓ | Первый абзац — direct answer (боль + staging + результат) |
| C03 | ✓ | Финдиректор группы 2–8 ООО, собственник, cash-взгляд |
| C04 | ✓ | entity_id, is_intercompany, DirectBank, staging, hash |
| O01 | ✓ | H2 по карточке B55 |
| O02 | ✓ | Outline читается без body |
| O03 | ✓ | FAQ 7 пар |
| O04 | ✓ | ol 7+5+5 шагов, table×3, blockquote×1, pre×1 |
| R01 | ✓ | Таблица маршрутов A/B/C/D, workflow, сверка недели 1 |
| R02 | ✓ | ФЗ 402-ФЗ, 51/52/55, DirectBank multi-org |
| R03 | ✓ | Нет фейковых Wordstat; сроки — оценочные |
| R04 | ✓ | FAQ answer-first |
| E01 | ✓ | RU no-code + 1С + без сырых ПДн в LLM |
| E02 | ✓ | «Сделайте / Не делайте» в when-needed, prep-security, verify-errors |
| E03 | ✓ | CTA club + Telegram (без salebot) |
| Exp01 | ✓ | article_mode B, olga-kondratskaya |
| Exp02 | ✓ | Практичный тон, не generic AI |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | ПДн, токены, обезличивание LLM |
| Ept02 | ✓ | Internal links avtomatizaciya + obezlichivanie |
| — | ✗ | Wordstat infra offline (−1) |

## Script reports

| Скрипт | Verdict | Файл |
|--------|---------|------|
| fact_checker | PASS | fact-check-report.json (9 facts, 3 verified) |
| link-verify | PASS | link-verify.json (4 links, 0 failed) |
| html-linter | PASS | html-linter-report.json |
| slop_detector | PASS | slop-detector-report.json (0 cliches, 5 over-long) |
| cannibalization_guard | PASS | cannibalization-report.json (0 issues) |
| utility gate (article) | PASS | utility-gate-report.json (WARN title_seo) |

## Link verify

- total: 4, failed: 0
- OK: `/obezlichivanie-dannyh-chatgpt-finansist/`, `/avtomatizaciya-finansov-no-code/`, club.koda-fd.ru, t.me/finance_modern

## Fixes applied

Нет — article.html без правок после прогона скриптов.

## Notes

- utility gate WARN: `meta_ab.title_seo` не содержит «учет» из primary_query — не блокер, title_aeo/title покрывают intent.
- slop: 5 предложений >25 слов — допустимо для workflow-таблиц в тексте парсера.
- fact-check: unverified — маскированные р/с (...4521 и т.д.) и оценочные сроки внедрения.
