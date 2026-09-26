# QA: B92 mcp-google-sheets-cursor-reestry

date: 2026-09-13
score_total: 93/100
core_eeat_lite: 19/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 18 | primary в лиде; FAQ 7; H2 how-to ×7 + FAQ; таблица Path A/B/C/B82 |
| GEO / citability | 25 | 24 | Answer-first lead 461 симв; blockquote workflow×2; ol×3; pre/code mcp.json + промпт |
| CORE-EEAT lite | 15 | 14 | 19/20; −1 Wordstat MCP-KV offline |
| Human voice | 15 | 14 | 0 slop hits; WARNING 6 over-long (table/schema noise); Flesch RU 100; «Сделайте/Не делайте» ×6 |
| Fact safety | 15 | 14 | fact-check PASS (1/5 vs fact-bank; 200–300, 80–100, квоты 300/60, 1–2 ч — в research-notes) |
| Contract HTML | 10 | 9 | linter PASS, plain 8929 ✓ band, CTA club+TG ✓; −1 нет `<img>` (cover отдельно) |

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
| char_count (plain) | 8929 |
| CTA | club.koda-fd.ru ×1 + t.me/finance_modern ×1 |

## CORE-EEAT lite: 19/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | Title/meta + lead: MCP Google Sheets Cursor + реестр без копипаста |
| C02 | ✓ | Первый абзац — direct answer (doc_key, 1-2 ч, MCP Logs) |
| C03 | ✓ | Аудитория: финансист/CFO с реестром в Sheets |
| C04 | ✓ | Path A OAuth vs Path B SA; MCP vs B82 скрипт; vs копипаст |
| O01 | ✓ | H2: when → security → setup Path B → Path A/C → scenario → verify → next + FAQ |
| O02 | ✓ | Outline читается без body |
| O03 | ✓ | FAQ 7 пар (без программиста, время, OAuth/SA, риски, B82, Cloud, 429) |
| O04 | ✓ | ol (17 li), ul (1), table (1), blockquote (2), pre/code (2) |
| R01 | ✓ | ≥3 citability-блока (таблица маршрутов, workflow blockquote, mcp.json, промпт) |
| R02 | ✓ | 03.08.2026 changelog, квоты 300/60, 200–300 договоров, 80–100 заявок — research |
| R03 | ✓ | Нет фейкового Wordstat; Preview/Marketplace — honest notes |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: финреестры doc_key, не dev-обзор MCP |
| E02 | ✓ | «Сделайте / Не делайте» в 6 H2-секциях |
| E03 | ✓ | CTA: Telegram finance_modern + клуб KODA (без salebot) |
| Exp01 | ✓ | Режим B, author_id olga-kondratskaya |
| Exp02 | ✓ | Тон practice/DoD, мост B21/B82/B51/B58/B83 |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | ПДн: обезличивание, SA share, approval write-tools, injection |
| Ept02 | ✓ | Internal: mcp-cursor, sheets-api, no-code, обезличивание |
| — | ✗ | Wordstat infra: MCP-KV offline (−1 lite → 19/20) |

## Script reports

| Скрипт | Verdict | Файл |
|--------|---------|------|
| fact-check | PASS | fact-check-report.json |
| link-verify | PASS | link-verify.json |
| html-linter | PASS | html-linter-report.json |
| slop-detector | WARNING (0 cliches) | slop-detector-report.json |
| cannibalization | WARNING (не B92) | cannibalization-report.json |
| utility gate (article) | PASS | utility-gate-report.json |

## Link verify

- total: 6, failed: 0
- OK: `/blog/mcp-cursor-finansist-instrumenty/`, `/blog/google-sheets-api-integraciya-finotdel/`, `/blog/avtomatizaciya-finansov-no-code/`, `/blog/obezlichivanie-dannyh-chatgpt-finansist/`, t.me/finance_modern, club.koda-fd.ru
- `--site-base https://koda-fd.ru`

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 6
- Flesch RU: 100.0 (Very Easy)
- verdict WARNING (не blocker при 0 cliches)

## Fact-check

- script verdict: pass (1 verified vs fact-bank; 4 unverified numbers)
- research cross-check: 200–300, 80–100, квоты 300/60, 1–2 ч — в research-notes.md с URL
- 403 — HTTP-код в troubleshooting, не статистика спроса

## Cannibalization

- global verdict: warning (B80↔B21 overlap 75%, не затрагивает B92)
- B92 verdict: pass — primary «mcp google sheets cursor»; adjacent B21/B82, не duplicate

## Utility gate

- article: PASS (numbered steps 17, faq_h3=7, actionable H2=7, table, workflow)
- report: utility-gate-report.json

## Fix cycle

- cycle 0 (этот прогон): writer сдал plain 8929; все гейты PASS; правок article.html не потребовалось

## GEO QA agent (2026-09-13)

- agent: excalibur-blog-geo-qa (generalPurpose fallback)
- EXCALIBUR_RUN_DATE: 2026-09-13
- gates: utility ✓ | html-linter ✓ | slop ✓ | link-verify ✓ | fact-check ✓ | cannibalization (B92) ✓
- verdict: **PASS** — cover/schema разрешены

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: yes (GCP→mcp.json→verify→registry scenario) | Review: no | E-E-A-T SameAs Author: pending (author_id: olga-kondratskaya)
