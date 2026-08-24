# QA: B92 mcp-google-sheets-cursor-reestry

date: 2026-08-24
score_total: 91/100
core_eeat_lite: 19/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 18 | primary в лиде; FAQ 7; H2 how-to ×6; таблица Path A/B |
| GEO / citability | 25 | 24 | Answer-first lead 425 симв; blockquote workflow; ol×3; pre/code mcp.json + промпт |
| CORE-EEAT lite | 15 | 14 | 19/20; −1 Wordstat MCP-KV offline |
| Human voice | 15 | 15 | 0 slop hits, Flesch RU 100, режим B Ольга, «Сделайте/Не делайте» ×6 |
| Fact safety | 15 | 15 | fact-check PASS 25/25; только research-notes + fact-check-report.json |
| Contract HTML | 10 | 9 | linter PASS, объём 8774 ✓, CTA club+TG ✓; −1 нет `<img>` (cover отдельно) |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate pass — **выполнен**.

## Hard bans (KODA)

| Проверка | Результат |
|----------|-----------|
| TL;DR blockquote | нет |
| Fact Check блок | нет |
| «—» (emdash U+2014) | 0 |
| «мы в KODA» | нет |
| salebot / koda_salebot | нет |
| article_mode | B |
| char_count | 8774 |
| CTA | club.koda-fd.ru ×1 + t.me/finance_modern ×1 |

## CORE-EEAT lite: 19/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | Title/meta + lead: MCP Google Sheets Cursor + реестр без копипаста |
| C02 | ✓ | Первый абзац — direct answer (doc_key, 1-2 ч, MCP Logs) |
| C03 | ✓ | Аудитория: финансист/CFO с реестром в Sheets |
| C04 | ✓ | Path A OAuth vs Path B SA; MCP vs B82 скрипт; vs копипаст |
| O01 | ✓ | H2: когда → безопасность → setup → Path A → сценарий → verify → next + FAQ |
| O02 | ✓ | Outline читается без body |
| O03 | ✓ | FAQ 7 пар (без программиста, время, OAuth/SA, риски, B82, Cloud, маленький реестр) |
| O04 | ✓ | ol (22 li в 3 блоках), ul (5), table (1), blockquote (2), pre/code (2) |
| R01 | ✓ | ≥3 citability-блока (таблица маршрутов, workflow blockquote, mcp.json, промпт) |
| R02 | ✓ | 03.08.2026 changelog, 300 write/min, 200-300 договоров, 80-100 заявок — research |
| R03 | ✓ | Нет фейкового Wordstat; статус Marketplace — honest note |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: финреестры doc_key, не dev-обзор MCP |
| E02 | ✓ | «Сделайте / Не делайте» в 6 H2-секциях |
| E03 | ✓ | CTA: Telegram finance_modern + клуб KODA (без salebot) |
| Exp01 | ✓ | Режим B, author_id olga-kondratskaya |
| Exp02 | ✓ | Тон practice/DoD, мост B21/B82/B51/B58/B83 |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | ПДн: обезличивание, SA share, approval write-tools |
| Ept02 | ✓ | Internal: avtomatizaciya-finansov-no-code, obezlichivanie-dannyh-chatgpt-finansist |
| — | ✗ | Wordstat infra: MCP-KV offline (−1 lite → 19/20) |

## Script reports

| Скрипт | Verdict | Файл |
|--------|---------|------|
| fact-check | PASS | fact-check-report.json |
| link-verify | PASS | link-verify.json |
| html-linter | PASS | html-linter-report.json |
| slop-detector | PASS | slop-detector-report.json |
| cannibalization | PASS | cannibalization-report.json |
| utility gate (article) | PASS | — |

## Link verify

- total: 6, failed: 0
- OK: `/blog/mcp-cursor-finansist-instrumenty/`, `/blog/google-sheets-api-integraciya-finotdel/`, `/blog/avtomatizaciya-finansov-no-code/`, `/blog/obezlichivanie-dannyh-chatgpt-finansist/`, t.me/finance_modern, club.koda-fd.ru
- `--site-base https://koda-fd.ru`

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 4
- Flesch RU: 100.0 (Very Easy)
- verdict PASS

## Fact-check

- verdict: pass (25 verified with URL)
- Marketplace Sheets status — honest note из research, не blocker

## Cannibalization

- verdict: pass (B92 primary «mcp google sheets cursor»; B21 «mcp cursor finansist» — adjacent, не duplicate)

## Utility gate

- article: PASS (numbered steps ≥5, faq_h3=7, actionable H2=6, table, workflow)
- article-qa.md: PASS (этот файл)

## Fix cycle

- cycle 0: trim 11687→8774; meta_ab добавлен; все скрипты PASS

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: yes (GCP→mcp.json→verify→registry scenario) | Review: no | E-E-A-T SameAs Author: pending (author_id: olga-kondratskaya)
