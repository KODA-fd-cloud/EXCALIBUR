# QA: B92 mcp-google-sheets-cursor-reestry

date: 2026-09-08
score_total: 92/100
core_eeat_lite: 19/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 18 | primary в лиде; FAQ 7; H2 how-to ×6 + FAQ; таблица Path A/B; title_seo 55 / desc_seo 162 |
| GEO / citability | 25 | 24 | Answer-first lead 391 симв; blockquote workflow×2; ol×3 (22 li); pre/code mcp.json + промпт; без TOC |
| CORE-EEAT lite | 15 | 14 | 19/20; −1 Wordstat MCP-KV offline |
| Human voice | 15 | 15 | 0 slop hits, Flesch RU 100, режим B Ольга, «Сделайте/Не делайте» в H2 |
| Fact safety | 15 | 14 | fact-check PASS (1/6 fact-bank; 5 unverified = research/HTTP/thresholds, не market-claims) |
| Contract HTML | 10 | 7 | linter PASS, объём ~8865 ✓, CTA club+TG ✓; −3 нет `<img>` (cover отдельно) |

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
| char_count | ~8865 collapsed / meta 8858 (8500–9500) ✓ |
| CTA | club.koda-fd.ru ×1 + t.me/finance_modern ×1 |
| TOC с якорями | нет |

## CORE-EEAT lite: 19/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | Title/meta + lead: MCP Google Sheets Cursor + реестр без копипаста |
| C02 | ✓ | Первый абзац — direct answer (doc_key, 1–2 ч, MCP Logs) |
| C03 | ✓ | Аудитория: финансист/CFO с реестром в Sheets |
| C04 | ✓ | Path A OAuth vs Path B SA; MCP vs B82 скрипт; vs копипаст |
| O01 | ✓ | H2: когда → безопасность → setup → сценарий → verify → next + FAQ |
| O02 | ✓ | Outline читается без body |
| O03 | ✓ | FAQ 7 пар (без программиста, время, Marketplace, OAuth/SA, риски, B82, 403) |
| O04 | ✓ | ol (22 li), ul (5), table (1), blockquote (2), pre/code (2) |
| R01 | ✓ | ≥3 citability-блока (таблица маршрутов, workflow, mcp.json, промпт DoD) |
| R02 | ✓ | 03.08.2026 changelog, 300 r/w/min, 200–300 договоров, 80–100 заявок — research-notes |
| R03 | ✓ | Нет фейкового Wordstat; статус Marketplace — honest note |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: финреестры doc_key + Path B, не dev-обзор MCP |
| E02 | ✓ | «Сделайте / Не делайте» в 6 H2-секциях |
| E03 | ✓ | CTA: Telegram finance_modern + клуб KODA (без salebot) |
| Exp01 | ✓ | Режим B, author_id olga-kondratskaya |
| Exp02 | ✓ | Тон practice/DoD, мост B21/B82/B51/B58/B83 |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | ПДн: обезличивание, SA share, approval write-tools, 403/429 |
| Ept02 | ✓ | Internal: mcp-cursor-finansist, sheets-api B82, no-code, обезличивание |
| — | ✗ | Wordstat infra: MCP-KV offline (−1 lite → 19/20) |

## Script reports

| Скрипт | Verdict | Файл |
|--------|---------|------|
| fact-check | PASS | fact-check-report.json |
| link-verify | PASS | link-verify.json |
| html-linter | PASS | html-linter-report.json |
| slop-detector | PASS | slop-detector-report.json |
| cannibalization | WARNING (portfolio; B92 PASS) | cannibalization-report.json |
| utility gate (article) | PASS | utility-gate-report.json |

## Link verify

- total: 6, failed: 0
- OK: `/blog/mcp-cursor-finansist-instrumenty/`, `/blog/google-sheets-api-integraciya-finotdel/`, `/blog/avtomatizaciya-finansov-no-code/`, `/blog/obezlichivanie-dannyh-chatgpt-finansist/`, t.me/finance_modern, club.koda-fd.ru
- `--site-base https://koda-fd.ru`

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 3 (таблица/схема — допустимо)
- Flesch RU: 100.0 (Very Easy)
- verdict PASS

## Fact-check

- verdict: pass (6 extracted; 1 verified in fact-bank — «2026»)
- Unverified: «2 часов», «300», «100», «429», «403» — пороги/HTTP из research-notes / Sheets API limits, не выдуманные ROI
- Marketplace Sheets status — honest note из research, не blocker

## Cannibalization

- global verdict: warning (B21↔B80 overlap 75%, не затрагивает B92)
- B92: pass — primary «mcp google sheets cursor»; adjacent B21/B82, не duplicate

## Utility gate

- article: PASS (`action_markers=18`, numbered steps=17, faq_h3=7, actionable H2=6, tables=1, blockquotes=2)
- report: utility-gate-report.json

## Fix cycle

- cycle 0 (geo-qa 2026-09-08): перезапуск всех скриптов на актуальном article.html — PASS; правок article.html не потребовалось
- optional (не blocker): синхронизировать `meta.char_count` (8858) с collapsed (~8865); при желании добавить 300/429 в fact-bank

## GEO QA agent (2026-09-08)

- agent: excalibur-blog-geo-qa
- gates: utility gate ✓ | html-linter ✓ | slop ✓ | link-verify ✓ | fact-check ✓ | cannibalization (B92) ✓
- verdict: **PASS** — cover/schema разрешены

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: yes (GCP→mcp.json→verify→registry scenario) | Review: no | E-E-A-T SameAs Author: pending (author_id: olga-kondratskaya)
