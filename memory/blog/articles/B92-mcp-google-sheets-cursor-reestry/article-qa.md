# QA: B92 mcp-google-sheets-cursor-reestry

date: 2026-09-07
score_total: 93/100
core_eeat_lite: 19/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 18 | primary в лиде; FAQ 7; H2 how-to ×6 + FAQ; таблица Path A/B/C |
| GEO / citability | 25 | 24 | Answer-first lead 396 симв; blockquote workflow; ol×2; pre/code mcp.json + промпт |
| CORE-EEAT lite | 15 | 14 | 19/20; −1 Wordstat MCP-KV offline |
| Human voice | 15 | 15 | 0 slop hits, Flesch RU 100, режим B Ольга, «Сделайте/Не делайте» ×6 |
| Fact safety | 15 | 14 | fact-check script PASS; 3 числа (400/300/100) не в fact-bank, но в research-notes с URL |
| Contract HTML | 10 | 8 | linter PASS, объём 9037 ✓, CTA club+TG ✓; −1 нет `<img>`; −1 link `/avtomatizaciya…` без `/blog/` (200 OK) |

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
| char_count | 9037 |
| CTA | club.koda-fd.ru ×1 + t.me/finance_modern ×1 |
| TOC `#` anchors | 0 |

## CORE-EEAT lite: 19/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | Title/meta + lead: MCP Google Sheets Cursor + реестр без копипаста |
| C02 | ✓ | Первый абзац — direct answer (doc_key, 1–2 ч, find→update→re-read) |
| C03 | ✓ | Аудитория: финансист/CFO с реестром в Sheets |
| C04 | ✓ | Path A/B/C; MCP vs B82 скрипт; SA vs OAuth |
| O01 | ✓ | H2: когда → подготовка → Path B → сценарий → ошибки → рост + FAQ |
| O02 | ✓ | Outline читается без body |
| O03 | ✓ | FAQ 7 пар (без программиста, время, OAuth/SA, риски, B82, Cloud, region) |
| O04 | ✓ | ol (14 li), ul (1), table (1), blockquote (1), pre/code (2) |
| R01 | ✓ | ≥3 citability-блока (таблица маршрутов, workflow, mcp.json, промпт) |
| R02 | ✓ | квоты 300/60, Error 400, 80–100 заявок, region caveat — research-notes |
| R03 | ✓ | Нет фейкового Wordstat; region без howto обхода |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: финреестры doc_key, Path B default, не dev-обзор MCP |
| E02 | ✓ | «Сделайте / Не делайте» в 6 H2-секциях |
| E03 | ✓ | CTA: Telegram finance_modern + клуб KODA (без salebot) |
| Exp01 | ✓ | Режим B, author_id olga-kondratskaya |
| Exp02 | ✓ | Тон practice/DoD, мост B21/B82/B51 |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | ПДн, SA share, approval write, 429, injection |
| Ept02 | ✓ | Internal: B21, B82, обезличивание, no-code |
| — | ✗ | Wordstat infra: MCP-KV offline (−1 lite → 19/20) |

## Script reports

| Скрипт | Verdict | Файл |
|--------|---------|------|
| fact-check | PASS | fact-check-report.json |
| link-verify | PASS | link-verify.json |
| html-linter | PASS | html-linter-report.json |
| slop-detector | PASS | slop-detector-report.json |
| cannibalization | WARNING (global B21↔B80; B92 OK) | cannibalization-report.json |
| utility gate (article) | PASS | utility-gate-report.json |

## Link verify

- total: 6, failed: 0
- OK: `/blog/mcp-cursor-finansist-instrumenty/`, `/blog/google-sheets-api-integraciya-finotdel/`, `/blog/obezlichivanie-dannyh-chatgpt-finansist/`, `/avtomatizaciya-finansov-no-code/`, t.me/finance_modern, club.koda-fd.ru
- `--site-base https://koda-fd.ru`

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 1 (table flatten artifact)
- Flesch RU: 100.0 (Very Easy)
- verdict PASS

## Fact-check

- verdict: pass (1/4 exact in fact-bank; 3 numbers backed by research-notes URLs: Error 400 forum, Sheets quotas 300/60, 80–100 заявок)
- Marketplace / region — honest notes, не blocker

## Cannibalization

- global verdict: warning (B80↔B21 overlap 75%, не затрагивает B92)
- B92 verdict: pass — primary «mcp google sheets cursor»; adjacent B21/B82, не duplicate

## Utility gate

- article: PASS (numbered steps 14, faq_h3=7, actionable H2=6, table, workflow)
- report: utility-gate-report.json

## Fix cycle

- cycle 0 (writer 2026-09-07): rewrite article.html wc-m 9037; meta_ab; FAQ 7; CTA club+TG
- cycle 1 (geo-qa 2026-09-07): перезапуск всех скриптов — PASS, правок article.html не потребовалось

## GEO QA agent (2026-09-07)

- agent: excalibur-blog-geo-qa
- gates: utility gate ✓ | html-linter ✓ | slop ✓ | link-verify ✓ | fact-check ✓ | cannibalization (B92) ✓
- verdict: **PASS** — cover/schema разрешены

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: yes (GCP→mcp.json→verify→registry scenario) | Review: no | E-E-A-T SameAs Author: pending (author_id: olga-kondratskaya)
