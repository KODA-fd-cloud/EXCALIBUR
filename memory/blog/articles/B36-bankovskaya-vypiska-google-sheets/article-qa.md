# QA: B36 bankovskaya-vypiska-google-sheets

date: 2026-08-03
score_total: 89/100
core_eeat_lite: 17/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 18 | primary в лиде; 8 H2 action; FAQ 7 |
| GEO / citability | 25 | 23 | таблица маршрутов, 5×ol, pre/code, 2 blockquote |
| CORE-EEAT lite | 15 | 17 | практика CSV/T-API/Sber, без выдуманных метрик |
| Human voice | 15 | 14 | mode B, 0 slop, аналогии «курьер/сейф» |
| Fact safety | 15 | 13 | fact-check PASS; лимиты GAS/API с оговорками |
| Contract HTML | 10 | 8 | linter PASS; cover отдельно |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, utility gate pass — **выполнен**.

## Script reports

| Скрипт | Verdict |
|--------|---------|
| excalibur_blog_fact_checker.py | PASS |
| excalibur_blog_link_verify.py | PASS (5/5, site-base https://koda-fd.ru) |
| excalibur_blog_html_linter.py | PASS |
| excalibur_blog_slop_detector.py | PASS (0 cliches; 3 over-long sentences — допустимо) |
| excalibur_blog_cannibalization_guard.py | PASS (0 issues vs 26 articles) |
| excalibur_blog_utility_gate.py | PASS (19 ol items, 7 FAQ, 1 table) |

## Hard bans (KODA)

| Проверка | Результат |
|----------|-----------|
| em dash (—) | 0 |
| salebot | 0 |
| article_mode A | нет (B) |
| TL;DR / Fact Check блоки | нет |

## Notes

- CTA: club.koda-fd.ru + t.me/finance_modern + koda-fd.ru; salebot forbidden — соблюдено
- Internal links: /blog/avtomatizaciya-finansov-no-code/, /blog/obezlichivanie-dannyh-chatgpt-finansist/
- Cannibalization: отличие от B25 (staging-детали) — угол «маршруты + API + расписание без 1С»
- Fixes applied: none (first pass PASS)
