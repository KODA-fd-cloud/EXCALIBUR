# QA: B92 mcp-google-sheets-cursor-reestry

date: 2026-09-12
score_total: 94/100
core_eeat_lite: 19/20
link_verify: pass
utility_gate: pass
plain_char_count: 9244
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 19 | primary в лиде; FAQ 7; H2 how-to ×7 + FAQ; таблица Path A/B/C; meta_ab ✓ |
| GEO / citability | 25 | 24 | Answer-first lead 425; workflow/verdict blockquote; ol×3; pre/code mcp.json + промпт + remote URL |
| CORE-EEAT lite | 15 | 14 | 19/20; −1 Wordstat MCP-KV offline (цифры не выдуманы) |
| Human voice | 15 | 14 | 0 slop hits, Flesch RU 100, режим B Ольга, «Сделайте/Не делайте»; −1 slop WARNING (6 over-long, в т.ч. таблица) |
| Fact safety | 15 | 14 | fact-check PASS; 1/5 в fact-bank; длительности/пороги/403 — practice claims из research, не market % |
| Contract HTML | 10 | 9 | linter PASS, plain 9244 ✓ (band 8500–9500), CTA club+TG ✓; −1 нет `<img>` (cover отдельно) |

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
| char_count (plain) | 9244 (8500–9500) ✓ |
| CTA | club.koda-fd.ru ×1 + t.me/finance_modern ×1 |
| TOC с якорями | нет |

## CORE-EEAT lite: 19/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | Title/meta + lead: MCP Google Sheets Cursor + реестр без копипаста |
| C02 | ✓ | Первый абзац — direct answer (doc_key, 1-2 ч, MCP Logs) |
| C03 | ✓ | Аудитория: финансист/CFO с реестром в Sheets |
| C04 | ✓ | MCP объяснён во 2-м абзаце (~протокол / tools / курьер) |
| O01 | ✓ | H2: when → security → Path B setup → Path A/C → scenario → verify → next + FAQ |
| O02 | ✓ | Outline читается без body |
| O03 | ✓ | FAQ 7 пар (без программиста, время, OAuth/SA, риски, B82, Cloud, маленький реестр) |
| O04 | ✓ | ol (17 li), ul (5), table (1), blockquote (2), pre/code (3) |
| R01 | ✓ | ≥3 citability-блока (таблица маршрутов, workflow, mcp.json, промпт DoD) |
| R02 | ✓ | 03.08.2026 changelog, 300 write/min, Path C URL — research-notes |
| R03 | ✓ | Нет фейкового Wordstat; Marketplace status — honest note |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: финреестры doc_key, не dev-обзор MCP |
| E02 | ✓ | «Сделайте / Не делайте» в H2-секциях |
| E03 | ✓ | CTA: Telegram finance_modern + клуб KODA (без salebot) |
| Exp01 | ✓ | Режим B, author_id olga-kondratskaya |
| Exp02 | ✓ | Тон practice/DoD, мост B21/B82/B51/B58/B83 |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | ПДн: обезличивание, SA share, approval write-tools, indirect injection |
| Ept02 | ✓ | Internal: mcp-cursor-finansist, sheets-api B82, no-code, обезличивание |
| — | ✗ | Wordstat infra: MCP-KV offline (−1 lite → 19/20) |

## Script reports

| Скрипт | Verdict | Файл |
|--------|---------|------|
| fact-check | PASS | fact-check-report.json |
| link-verify | PASS | link-verify.json |
| html-linter | PASS | html-linter-report.json |
| slop-detector | WARNING | slop-detector-report.json |
| cannibalization | WARNING (portfolio) | cannibalization-report.json |
| utility gate (article) | PASS | utility-gate-report.json |

## Link verify

- total: 6, failed: 0
- OK: `/blog/mcp-cursor-finansist-instrumenty/`, `/blog/google-sheets-api-integraciya-finotdel/`, `/blog/avtomatizaciya-finansov-no-code/`, `/blog/obezlichivanie-dannyh-chatgpt-finansist/`, t.me/finance_modern, club.koda-fd.ru
- `--site-base https://koda-fd.ru`

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 6 (таблица маршрутов / длинные practice-абзацы)
- Flesch RU: 100.0 (Very Easy)
- verdict WARNING (не blocker: 0 cliches)

## Fact-check

- verdict: pass (5 extracted; 1 verified in fact-bank — «2026»)
- unverified: «2 часов», «300», «100», «403» — practice/threshold claims из research, не выдуманные % рынка

## Cannibalization

- global verdict: warning (B80↔B21 overlap 75%, не затрагивает B92)
- B92: pass — primary «mcp google sheets cursor»; adjacent B21/B82, не duplicate

## Utility gate

- article: PASS (numbered steps 17, faq_h3=7, action_markers=18, table=1, blockquotes=2)
- report: utility-gate-report.json

## Fix cycle

- cycle 0 (2026-09-12): перезапуск всех скриптов на свежем article.html (plain 9244) — PASS, правок article.html не потребовалось

## GEO QA agent (2026-09-12)

- agent: excalibur-blog-geo-qa
- gates: utility ✓ | html-linter ✓ | slop (0 cliches) ✓ | link-verify ✓ | fact-check ✓ | cannibalization (B92) ✓
- verdict: **PASS** — cover/schema разрешены

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: yes (GCP→mcp.json→verify→registry scenario) | Review: no | E-E-A-T SameAs Author: pending (author_id: olga-kondratskaya)
