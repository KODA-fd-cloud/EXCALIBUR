# QA: B92 mcp-google-sheets-cursor-reestry

date: 2026-08-26
score_total: 94/100
core_eeat_lite: 19/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 19 | title_seo 55, desc_seo 148; primary в лиде; FAQ 7; H2 how-to ×7 + FAQ; Path B default в meta |
| GEO / citability | 25 | 24 | Answer-first lead 429; таблица Path A/B; blockquote workflow; ol×4 (17 li); pre×2 (mcp.json + промпт) |
| CORE-EEAT lite | 15 | 14 | 19/20; −1 Wordstat MCP-KV offline (цифры спроса не выдуманы) |
| Human voice | 15 | 15 | 0 slop hits, Flesch RU 100, режим B Ольга, «Сделайте/Не делайте» в H2 |
| Fact safety | 15 | 14 | fact-check PASS; Marketplace Not Found подтверждён (title/og 26.08); 200–300 / 80–100 / 300 write/min — research URLs; −1 4 stats вне fact-bank (operational) |
| Contract HTML | 10 | 8 | linter PASS, объём 9073 ✓, CTA club+TG ×1; −2 нет `<img>` (cover отдельно) |

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
| char_count | 9073 (8500–9500) ✓ |
| CTA | club.koda-fd.ru ×1 + t.me/finance_modern ×1 |
| TOC с якорями | нет |

## CORE-EEAT lite: 19/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | Title/meta + lead: MCP Google Sheets Cursor + реестр без копипаста |
| C02 | ✓ | Первый абзац — direct answer (Path B default, Not Found, find→update→re-read) |
| C03 | ✓ | Аудитория: финансист/CFO с реестром в Sheets |
| C04 | ✓ | Path B SA default vs Path A optional; MCP vs B82 скрипт; vs копипаст |
| O01 | ✓ | H2: when → security → Path B setup → Path A check → scenario → verify → next + FAQ |
| O02 | ✓ | Outline читается без body |
| O03 | ✓ | FAQ 7 пар (без программиста, время, OAuth/SA, риски, B82, Cloud, Path B vs Marketplace) |
| O04 | ✓ | ol (17 li), ul (1), table (1), blockquote (2), pre/code (2) |
| R01 | ✓ | ≥3 citability-блока (таблица маршрутов, workflow, mcp.json, промпт DoD) |
| R02 | ✓ | 03.08/04.08.2026, 300 write/min, 200–300 договоров, 80–100 заявок — research-notes |
| R03 | ✓ | Нет фейкового Wordstat; Marketplace Sheets = Not Found (honest, re-verified) |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: финреестры doc_key + Path B default 26.08, не dev-обзор MCP |
| E02 | ✓ | «Сделайте / Не делайте» в H2-секциях |
| E03 | ✓ | CTA: Telegram finance_modern + клуб KODA (без salebot) |
| Exp01 | ✓ | Режим B, author_id olga-kondratskaya |
| Exp02 | ✓ | Тон practice/DoD, мост B21/B82/B51/B58/B83/B93 |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | ПДн: обезличивание, SA share, approval write-tools, injection |
| Ept02 | ✓ | Internal: mcp-cursor-finansist, sheets-api, no-code, обезличивание |
| — | ✗ | Wordstat infra: MCP-KV offline (−1 lite → 19/20) |

## Script reports

| Скрипт | Verdict | Файл |
|--------|---------|------|
| fact-check | PASS | fact-check-report.json |
| link-verify | PASS | link-verify.json |
| html-linter | PASS | html-linter-report.json |
| slop-detector | PASS | slop-detector-report.json |
| cannibalization | WARNING (portfolio; B92 ok) | cannibalization-report.json |
| utility gate (article) | PASS | utility-gate-report.json |

## Link verify

- total: 8, failed: 0
- OK: github.com/freema/mcp-gsheets, `/blog/mcp-cursor-finansist-instrumenty/`, `/blog/google-sheets-api-integraciya-finotdel/`, `/blog/avtomatizaciya-finansov-no-code/`, `/blog/obezlichivanie-dannyh-chatgpt-finansist/`, cursor.com/marketplace/mcp/google-sheets, t.me/finance_modern, club.koda-fd.ru
- `--site-base https://koda-fd.ru`

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 3 (лид/таблица — допустимо)
- Flesch RU: 100.0 (Very Easy)
- verdict PASS

## Fact-check

- verdict: pass (5 extracted; 1 verified in fact-bank «2026»; 4 operational: 1–2 часа, 200–300, 80–100, 403 — grounded in research-notes)
- Marketplace Sheets: title/og «MCP server Not Found» подтверждён 26.08.2026 (HTTP 200 soft-404 SPA)
- Path B (`freema/mcp-gsheets` + SA) = default — согласовано с research

## Cannibalization

- global verdict: warning (B80↔B21 overlap 75%, не затрагивает B92)
- B92 verdict: pass — primary «mcp google sheets cursor»; adjacent B21/B82, не duplicate

## Utility gate

- article: PASS (`action_markers=19`, numbered steps=17, faq_h3=7, h2=7, tables=1, blockquotes=2)
- report: utility-gate-report.json

## Fix cycle

- cycle 0 (2026-08-26 geo-qa): HTML без правок; все hard gates PASS с первого прогона после writer refresh (Path B default, char 9073)

## GEO QA agent (2026-08-26)

- agent: excalibur-blog-geo-qa (Cloud fallback generalPurpose)
- gates: utility gate ✓ | html-linter ✓ | slop ✓ | link-verify ✓ | fact-check ✓ | cannibalization (B92) ✓
- verdict: **PASS** — cover/schema разрешены

## Optional (не blocker)

- подключить MCP-KV Wordstat перед следующей семантикой
- `<img>` placeholder — cover отдельно

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: yes (GCP→SA→mcp.json→verify→registry scenario) | Review: no | E-E-A-T SameAs Author: pending (author_id: olga-kondratskaya)
