# QA: B46 statusy-edo-google-sheets

date: 2026-08-05
score_total: 88/100
core_eeat_lite: 17/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 18 | primary в лиде; 5 H2 action; FAQ 7 |
| GEO / citability | 25 | 23 | 2 таблицы, 7×ol, pre/code, 2 blockquote; без TOC/TL;DR |
| CORE-EEAT lite | 15 | 17 | GetDocflowEvents, маппинг статусов, УПД 5.03/2026 |
| Human voice | 15 | 14 | mode B, аналогии «курьер/акт сверки», 0 slop |
| Fact safety | 15 | 13 | fact-check PASS; API-лимиты с оговорками |
| Contract HTML | 10 | 9 | linter PASS; char_count 8967 |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate pass — **выполнен**.

## Script reports

| Скрипт | Verdict |
|--------|---------|
| excalibur_blog_fact_checker.py | PASS |
| excalibur_blog_link_verify.py | PASS (5/5, site-base https://koda-fd.ru) |
| excalibur_blog_html_linter.py | PASS |
| excalibur_blog_slop_detector.py | PASS (0 cliches; 4 over-long sentences — допустимо) |
| excalibur_blog_cannibalization_guard.py | PASS (0 issues vs 28 articles) |
| excalibur_blog_utility_gate.py | PASS (7 ol items, 7 FAQ, 2 tables, 13 action markers) |

## Hard bans (KODA)

| Проверка | Результат |
|----------|-----------|
| em dash (—) | 0 |
| salebot | 0 |
| article_mode A | нет (B) |
| TL;DR / Fact Check блоки | нет |

## Notes

- CTA: club.koda-fd.ru + t.me/finance_modern; salebot forbidden — соблюдено
- Internal links: google-apps-script-finansist-obnovit-dannye, avtomatizaciya-finansov-no-code, obezlichivanie-dannyh-chatgpt-finansist (×2)
- Cannibalization: угол «ЭДО статусы + API GetDocflowEvents» — без пересечения с B25/B36 (выписка/staging)
- Fixes applied: none (first pass PASS)
