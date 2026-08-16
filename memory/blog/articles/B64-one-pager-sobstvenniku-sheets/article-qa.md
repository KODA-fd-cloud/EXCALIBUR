# QA: B64 one-pager-sobstvenniku-sheets

date: 2026-08-16
score_total: 90/100
core_eeat_lite: 19/20
link_verify: pass (self-check)
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 19 | 5 actionable H2 + "Что дальше" + FAQ 7; primary в лиде |
| GEO / citability | 25 | 23 | Answer-first lead 409 симв., 2 таблицы, workflow blockquote, pre×1, 7 FAQ |
| CORE-EEAT lite | 15 | 14 | 19/20; −1 Wordstat MCP offline в research |
| Human voice | 15 | 15 | 0 slop hits, режим B, staging на пальцах |
| Fact safety | 15 | 15 | 20 фактов из fact-check-report.json; 63%, 6 млн, 3–7 дней, 2–4 ч из research |
| Contract HTML | 10 | 9 | linter PASS, объём 8676 ✓, CTA ≤3 ✓, 4 long sentences |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, utility gate pass — **выполнен**.

## Hard bans (KODA)

| Проверка | Результат |
|----------|-----------|
| TL;DR blockquote | нет |
| Fact Check блок | нет |
| emdash U+2014 | 0 |
| guillemets «» | 0 |
| salebot / koda_salebot | нет |
| article_mode | B |
| char_count | 8676 ✓ (8500–9500) |
| hook_len | 409 ✓ (350–500) |
| CTA | club.koda-fd.ru ×1 + koda-fd.ru ×1 + t.me/finance_modern ×1 |

## CORE-EEAT lite: 19/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | Title/meta + lead закрывают "one pager для собственника финансы" |
| C02 | ✓ | Первый абзац - direct answer |
| C03 | ✓ | CFO, финотдел, собственник без BI |
| C04 | ✓ | staging, SUMIFS, metric_key, ADPASS 10–12 метрик |
| O01 | ✓ | H2 по карточке B64 |
| O02 | ✓ | Outline читается без body |
| O03 | ✓ | FAQ 7 пар из research faq_hints |
| O04 | ✓ | ol 7+5+5 шагов, table×2, blockquote×2, pre×1 |
| R01 | ✓ | Вердикт таблицы, workflow, таблица ошибок |
| R02 | ✓ | 152-ФЗ, Sheets API batch, ADPASS, genad 5 мин |
| R03 | ✓ | Цифры только из research (63%, 6 млн, 2–4 ч, 3–7 дней) |
| R04 | ✓ | FAQ answer-first |
| E01 | ✓ | RU Sheets + one-pager + ПДн |
| E02 | ✓ | "Сделайте / Не делайте" в when-needed, prep, choose-five |
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
| excalibur_blog_html_linter.py | PASS |
| excalibur_blog_slop_detector.py | PASS (0 cliches; 4 over-long sentences) |
| excalibur_blog_utility_gate.py | PASS (pending meta - created) |

**Fixes applied:** trim guillemets → straight quotes; expand body 7019 → 8676

## Link verify (self-check)

- total: 5, failed: 0
- OK: `/blog/avtomatizaciya-finansov-no-code/`, `/blog/obezlichivanie-dannyh-chatgpt-finansist/`, club.koda-fd.ru, koda-fd.ru, t.me/finance_modern

## Schema ready (handoff)

BlogPosting: pending | FAQPage: yes (7) | HowTo: yes (setup ol 7 шагов) | Review: no | E-E-A-T: olga-kondratskaya
