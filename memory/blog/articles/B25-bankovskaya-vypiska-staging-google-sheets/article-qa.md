# QA: B25 bankovskaya-vypiska-staging-google-sheets

date: 2026-07-31
score_total: 90/100
core_eeat_lite: 19/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 18 | primary в title_seo; H2 action; FAQ 6; −2 H1 угол staging, не дословный primary |
| GEO / citability | 25 | 23 | таблица 10 колонок, схема слоёв, ol×5, pre×1, FAQ citability-first |
| CORE-EEAT lite | 15 | 14 | 19/20; −1 Wordstat MCP-KV offline |
| Human voice | 15 | 14 | 0 slop; Сделайте/Не делайте; режим B |
| Fact safety | 15 | 14 | fact-check PASS; 1251/«30 дней» = кодировка + якорь legacy, без %/цен |
| Contract HTML | 10 | 7 | linter PASS, 9344 ✓, CTA club+TG; −3 cover отдельно |

**Порог PASS:** ≥80 — **выполнен**.

## Hard bans (KODA)

| Проверка | Результат |
|----------|-----------|
| TL;DR | нет |
| Fact Check блок | нет |
| «—» (emdash) | 0 |
| «мы в KODA» | нет |
| salebot | нет |
| TOC `#...` list | нет |
| article_mode | B |
| char_count | 9344 ✓ |
| CTA | club ×1 + t.me/finance_modern ×1 |

## Script reports

| Скрипт | Verdict | Отчёт |
|--------|---------|-------|
| fact-check | PASS | `fact-check-report.json` (2 extracted, 0 blockers) |
| link-verify | PASS | `link-verify.json` (8/8 ok) |
| html-linter | PASS | `html-linter-report.json` |
| slop-detector | PASS | `slop-detector-report.json` (0 cliches; Flesch RU 70.6) |
| cannibalization | PASS | `cannibalization-report.json` (0 issues) |
| utility gate | PASS | `utility-gate-report.json` (ol 27 items, tables 1, FAQ 6) |

## CORE-EEAT lite: 19/20

| ID | Результат | Комментарий |
|----|-----------|-------------|
| C01 | ✓ | title_seo = primary; H1 = угол staging |
| C02 | ✓ | лид = direct answer, без «в этой статье» |
| C03 | ✓ | финансист / выписка → отчёт без копипаста |
| C04 | ✓ | staging = промежуточный склад; слои raw→staging |
| O01 | ✓ | H2 ≈ action_outline research |
| O02 | ✓ | why → columns → import → dedup → next → today → FAQ |
| O03 | ✓ | FAQ 6 |
| O04 | ✓ | ol×5 + table + pre |
| R01 | ✓ | лид, DoD, граница с 1С, FAQ |
| R02 | ✓ | IMPORTDATA/URL, `;`, «не преобразовывать», 1251 — из research |
| R03 | ✓ | нет %/цен |
| R04 | ✓ | ответ в 1-м предложении FAQ |
| E01 | ✓ | staging Sheets, не PDF-SaaS / не DirectBank |
| E02 | ✓ | Сделайте/Не делайте в каждой H2 |
| E03 | ✓ | CTA ≤2 (TG + клуб) |
| Exp01 | ✓ | mode B, без fake «я сделал» |
| Exp02 | ✓ | тон research / utility |
| Exp03 | ✓ | slop 0 |
| Ept01 | ✓ | PDF/OCR, 1С отдельно, пароли/часовые пояса |
| Ept02 | ✓ | 6 internal published links |
| — | ✗ (−1) | Wordstat unavailable (цифры спроса не выдуманы) |

**Veto:** нет (R03/Exp01/slop ok).

## FIX

нет — точечные правки HTML не требуются.

## Final

verdict: **PASS** — ready for cover || schema → indexer → publish
