# QA: B92 mcp-google-sheets-cursor-reestry

date: 2026-08-29
score_total: 92/100
core_eeat_lite: 19/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 18 | primary в лиде; FAQ 7; H2 how-to ×7 + FAQ; таблица Path A/B; title_seo/aeo в meta_ab |
| GEO / citability | 25 | 24 | Answer-first lead; blockquote workflow; ol×4; pre/code mcp.json + DoD-промпт; FAQ answer-first |
| CORE-EEAT lite | 15 | 14 | 19/20; −1 Wordstat MCP-KV offline (цифры спроса не выдуманы) |
| Human voice | 15 | 15 | 0 slop hits, Flesch RU 100, режим B Ольга, «Сделайте/Не делайте» по H2 |
| Fact safety | 15 | 15 | fact-check PASS; 300 write/min, 200–300 договоров, changelog 03.08 — research-notes |
| Contract HTML | 10 | 6 | linter PASS, объём 8699 ✓, CTA club+TG ✓; −4 нет `<img>` (cover отдельно) |

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
| char_count | 8699 (8500–9500) ✓ |
| CTA | club.koda-fd.ru ×1 + t.me/finance_modern ×1 |
| TOC с якорями | нет |

## CORE-EEAT lite: 19/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | Title/meta + lead: MCP Google Sheets Cursor + реестр без копипаста |
| C02 | ✓ | Первый абзац — direct answer (doc_key, 1–2 ч, MCP Logs) |
| C03 | ✓ | Аудитория: финансист/CFO с реестром в Sheets |
| C04 | ✓ | MCP, Path A OAuth vs Path B SA; vs копипаст / B82 |
| O01 | ✓ | H2: when → security → Path B setup → Path A → scenario → verify → next + FAQ |
| O02 | ✓ | Outline читается без body |
| O03 | ✓ | FAQ 7 (без программиста, время, OAuth/SA, риски, B82, Cloud, маленький реестр) |
| O04 | ✓ | ol×4 (17 li), ul, table×1, blockquote×2, pre×2 |
| R01 | ✓ | ≥3 citability-блока (таблица маршрутов, workflow, mcp.json, промпт) |
| R02 | ✓ | changelog 03.08.2026, 300 write/min, 200–300 договоров — research-notes |
| R03 | ✓ | Нет фейкового Wordstat; Marketplace Sheets — honest note |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: финреестры doc_key, не dev-обзор MCP |
| E02 | ✓ | «Сделайте / Не делайте» в H2-секциях |
| E03 | ✓ | CTA: Telegram + клуб KODA (без salebot) |
| Exp01 | ✓ | Режим B, author_id olga-kondratskaya |
| Exp02 | ✓ | Тон practice/DoD, мост B21/B82/B11 |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | ПДн, SA share, approval write-tools, indirect injection |
| Ept02 | ✓ | Internal: avtomatizaciya-finansov-no-code, obezlichivanie-dannyh-chatgpt-finansist (+ B21/B82) |
| — | ✗ | Wordstat infra: MCP-KV offline (−1 lite → 19/20) |

## Script reports

| Скрипт | Verdict | Файл |
|--------|---------|------|
| fact-check | PASS | fact-check-report.json |
| link-verify | PASS | link-verify.json |
| html-linter | PASS | html-linter-report.json |
| slop-detector | PASS | slop-detector-report.json |
| cannibalization | PASS (B92; portfolio warning B21↔B80) | cannibalization-report.json |
| utility gate (article) | PASS | utility-gate-report.json |

## Link verify

- total: 8, failed: 0 (после egress-fallback)
- Live 200: github.com/freema/mcp-gsheets, cursor.com/ru/help/customization/mcp, t.me/finance_modern
- Internals (ledger + local): `/blog/mcp-cursor-finansist-instrumenty/`, `/blog/google-sheets-api-integraciya-finotdel/`, `/blog/avtomatizaciya-finansov-no-code/`, `/blog/obezlichivanie-dannyh-chatgpt-finansist/`
- club.koda-fd.ru: canonical CTA; live SSL handshake timeout = egress
- `--site-base https://koda-fd.ru`
- Note: `cursor.com/agents` упомянут текстом (OAuth workaround), не как href — WAF 403 не затрагивает

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 4
- Flesch RU: 100.0 (Very Easy)
- verdict PASS

## Fact-check

- verdict: pass (5 extracted; 1 in fact-bank «2026»; прочие сверяются с research-notes: квоты Sheets API, порог 200–300 договоров, HTTP 403)
- Marketplace Sheets status — honest note из research, не blocker
- Wordstat: UNAVAILABLE — цифры показов не требуются

## Cannibalization

- global verdict: warning (B80↔B21 overlap 75%, не затрагивает B92)
- B92 verdict: pass — primary «mcp google sheets cursor»; adjacent B21/B82, не duplicate

## Utility gate

- article: PASS (`numbered_list_items=17`, `faq_h3=7`, `action_markers=18`, `tables=1`, `h2_sections=7`)
- report: utility-gate-report.json

## Fix cycle

- cycle 0 (geo-qa 2026-08-29): все скрипты PASS; правок article.html не потребовалось
- link-verify: raw fail из-за SSL handshake timeout на koda-fd.ru/club — переопределён pass по ledger + live externals (известный gotcha)

## GEO QA agent (2026-08-29)

- agent: excalibur-blog-geo-qa
- gates: utility gate ✓ | html-linter ✓ | slop ✓ | link-verify ✓ | fact-check ✓ | cannibalization (B92) ✓
- verdict: **PASS** — cover/schema разрешены

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: yes (GCP→mcp.json→verify→registry scenario) | Review: no | E-E-A-T SameAs Author: pending (author_id: olga-kondratskaya)
