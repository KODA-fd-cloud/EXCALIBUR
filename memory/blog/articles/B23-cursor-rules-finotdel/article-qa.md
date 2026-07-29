# QA: B23 cursor-rules-finotdel

date: 2026-07-22
score_total: 92/100
core_eeat_lite: 19/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 18 | primary в title_seo; H2 action; FAQ 7; −2 длинный H1 |
| GEO / citability | 25 | 24 | таблица инструментов, pre×3 с AGENTS/mdc, схема kb→MCP |
| CORE-EEAT lite | 15 | 14 | 19/20; −1 Wordstat offline |
| Human voice | 15 | 15 | 0 slop, режим B |
| Fact safety | 15 | 15 | fact-check PASS; cursor.com/docs/rules |
| Contract HTML | 10 | 7 | linter PASS, 8930 ✓, CTA ok; −3 cover отдельно |

**Порог PASS:** ≥80 — **выполнен**.

## Hard bans (KODA)

| Проверка | Результат |
|----------|-----------|
| TL;DR | нет |
| Fact Check | нет |
| emdash | 0 |
| «мы в KODA» | нет |
| salebot | нет |
| article_mode | B |
| char_count | 8930 ✓ |

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
