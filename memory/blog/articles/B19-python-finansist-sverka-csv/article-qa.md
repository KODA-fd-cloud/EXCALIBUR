# QA: B19 python-finansist-sverka-csv

date: 2026-07-22
score_total: 92/100
core_eeat_lite: 19/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 18 | title_seo ок; H2 how_to; FAQ 7; primary в лиде; −2 длинный H1 |
| GEO / citability | 25 | 24 | Answer-first, таблица Excel vs Python, схема →, ol×3, pre×3, FAQ; без TOC/TL;DR |
| CORE-EEAT lite | 15 | 14 | 19/20; −1 Wordstat MCP-KV offline |
| Human voice | 15 | 15 | 0 slop, режим B, Сделайте/Не делайте |
| Fact safety | 15 | 14 | fact-check PASS; merge/indicator по pandas docs |
| Contract HTML | 10 | 7 | linter PASS, 8928 ✓, CTA club+TG ≤2; −3 cover отдельно |

**Порог PASS:** ≥80 — **выполнен**.

## Hard bans (KODA)

| Проверка | Результат |
|----------|-----------|
| TL;DR | нет |
| Fact Check блок | нет |
| «—» (emdash) | 0 |
| «мы в KODA» | нет |
| salebot | нет |
| article_mode | B |
| char_count | 8928 ✓ |
| CTA | club ×1 + t.me/finance_modern ×1 |

## Script reports

| Скрипт | Verdict |
|--------|---------|
| fact-check | PASS |
| link-verify | PASS (ssl_unverified_recheck) |
| html-linter | PASS |
| slop-detector | PASS |
| cannibalization | PASS |
| utility gate | PASS |

## Final

verdict: **PASS** — ready for cover || schema → publish
