# QA: B92 mcp-google-sheets-cursor-reestry

date: 2026-09-04
score_total: 91/100
core_eeat_lite: 19/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 18 | title_seo 55, desc_seo 147; primary в лиде; FAQ 7; H2 how-to ×7 + FAQ; таблица Path A/B/C/B82 |
| GEO / citability | 25 | 24 | Answer-first lead 425 симв; blockquote workflow + вердикт; ol×4 (22 li); pre/code mcp.json + промпт; FAQ 7 |
| CORE-EEAT lite | 15 | 14 | 19/20; −1 Wordstat MCP-KV offline в research |
| Human voice | 15 | 15 | 0 slop hits, Flesch RU 100, режим B Ольга, «Сделайте/Не делайте» в H2 |
| Fact safety | 15 | 14 | fact-check PASS 6/6 extracted (1 verified fact-bank; 5 tech refs из research: 1-2 ч, 200-300, 429, 80-100, 403) |
| Contract HTML | 10 | 6 | linter PASS, объём 9494 ✓, CTA club+TG ✓; −4 нет `<img>` (cover отдельно) |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate pass — **выполнен**.

## Hard bans (KODA)

| Проверка | Результат |
|----------|-----------|
| TL;DR blockquote | нет |
| Fact Check блок | нет |
| «—» (emdash U+2014) | 0 |
| ««» / «»» (guillemets в body) | 0 |
| «мы в KODA» | нет |
| salebot / koda_salebot | нет |
| article_mode | B |
| char_count | 9494 (8500–9500) ✓ |
| CTA | club.koda-fd.ru ×1 + t.me/finance_modern ×1 |
| TOC с якорями | нет |

## CORE-EEAT lite: 19/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | Title/meta + lead: MCP Google Sheets Cursor + реестр без копипаста |
| C02 | ✓ | Первый абзац — direct answer (doc_key, 1-2 ч, MCP Logs) |
| C03 | ✓ | Аудитория: финансист/CFO с реестром в Sheets |
| C04 | ✓ | Path A OAuth vs Path B SA vs Path C remote; MCP vs B82 скрипт; vs копипаст |
| O01 | ✓ | H2: when → security → setup Path B → Path A/C → scenario → verify → next + FAQ |
| O02 | ✓ | Outline читается без body |
| O03 | ✓ | FAQ 7 пар (без программиста, время, OAuth/SA, риски, B82, Cloud, маленький реестр) |
| O04 | ✓ | ol (22 li в 4 блоках), ul (5), table (1), blockquote (2), pre/code (2) |
| R01 | ✓ | ≥3 citability-блока (таблица маршрутов, workflow blockquote, mcp.json, промпт DoD) |
| R02 | ✓ | 03.08.2026 changelog, 300/60 req/min, 200-300 договоров, 80-100 заявок — research |
| R03 | ✓ | Нет фейкового Wordstat; статус Marketplace — honest disclaimer |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: финреестры doc_key, Path B production-default; не dev-обзор MCP |
| E02 | ✓ | «Сделайте / Не делайте» в H2-секциях |
| E03 | ✓ | CTA: Telegram finance_modern + клуб KODA (без salebot) |
| Exp01 | ✓ | Режим B, author_id olga-kondratskaya |
| Exp02 | ✓ | Тон practice/DoD, мост B21/B82/B51/B58/B83 |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | ПДн: обезличивание, SA share, approval write-tools, prompt injection из ячеек |
| Ept02 | ✓ | Internal: mcp-cursor-finansist-instrumenty, google-sheets-api-integraciya-finotdel, avtomatizaciya-finansov-no-code, obezlichivanie-dannyh-chatgpt-finansist |
| — | ✗ | Wordstat infra: MCP-KV offline (−1 lite → 19/20) |

## Script reports

| Скрипт | Verdict | Файл |
|--------|---------|------|
| fact-check | PASS | fact-check-report.json |
| link-verify | PASS | link-verify.json |
| html-linter | PASS | html-linter-report.json |
| slop-detector | PASS | slop-detector-report.json |
| cannibalization | PASS (warning portfolio) | cannibalization-report.json |
| utility gate (article) | PASS | utility-gate-report.json |

## Link verify

- total: 6, failed: 0
- OK: `/blog/mcp-cursor-finansist-instrumenty/`, `/blog/google-sheets-api-integraciya-finotdel/`, `/blog/avtomatizaciya-finansov-no-code/`, `/blog/obezlichivanie-dannyh-chatgpt-finansist/`, t.me/finance_modern, club.koda-fd.ru
- `--site-base https://koda-fd.ru`

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 1 (склейка таблицы Path A/B/C — допустимо)
- Flesch RU: 100.0 (Very Easy)
- verdict: PASS

## Fact-check

- verdict: pass (6 extracted; 1 verified in fact-bank — «2026»)
- unverified tech refs (1-2 часов, 200-300, 429, 80-100, 403) — из research-notes / Google quotas / HTTP codes, не market-claims

## Cannibalization

- verdict: warning (portfolio; 0 issues для B92)
- note: глобальный warn B80↔B21 (MCP); B92 primary «mcp google sheets cursor» отделён углом Path B + реестры doc_key от B21 (обзор MCP) и B82 (скрипт API)

## Utility gate

- article: PASS (`action_markers=18`, numbered_list_items=17, faq_h3=7, tables=1, h2_sections=7)

## Fix cycle

- cycle 0: HTML без правок; все hard gates PASS с первого прогона

## Optional (не blocker)

- подключить MCP-KV Wordstat перед следующей семантикой
- `<img>` placeholder — cover отдельно

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: yes (SA → mcp.json → find-update-re-read) | Review: no | E-E-A-T SameAs Author: pending (author_id: olga-kondratskaya)
