# QA: B92 mcp-google-sheets-cursor-reestry

date: 2026-09-16
score_total: 93/100
core_eeat_lite: 19/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 18 | primary в лиде; FAQ 7; H2 how-to ×7 + FAQ; таблица Path A/B/Marketplace/B82 |
| GEO / citability | 25 | 24 | Answer-first lead; blockquote workflow+вердикт; ol×3; pre/code mcp.json + промпт |
| CORE-EEAT lite | 15 | 14 | 19/20; −1 Wordstat MCP-KV offline (цифры спроса не выдуманы) |
| Human voice | 15 | 15 | 0 slop hits, Flesch RU 100, режим B Ольга, «Сделайте/Не делайте» ×6 |
| Fact safety | 15 | 14 | fact-check PASS; 5 извлечено / 1 в fact-bank; 200–300, 80–100, 300 r/w, Preview 14.09 — research-notes |
| Contract HTML | 10 | 8 | linter PASS, char_count 8741 ✓, CTA club+TG ✓; −2 нет `<img>` (cover отдельно) |

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
| char_count | 8741 (meta; band 8500–9500) |
| CTA | club.koda-fd.ru ×1 + t.me/finance_modern ×1 |

## CORE-EEAT lite: 19/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | Title/meta + lead: MCP Google Sheets Cursor + реестр без копипаста |
| C02 | ✓ | Первый абзац — direct answer (doc_key, 1–2 ч, MCP Logs) |
| C03 | ✓ | Аудитория: финансист/CFO с реестром в Sheets |
| C04 | ✓ | MCP; Path A SA vs Path B OAuth Preview; vs B82 скрипт; vs Marketplace |
| O01 | ✓ | H2: when → security → Path A → Path B → scenario → verify → next + FAQ |
| O02 | ✓ | Outline читается без body |
| O03 | ✓ | FAQ 7 (без программиста, время, OAuth/SA, риски, B82, Cloud, маленький реестр) |
| O04 | ✓ | ol (17 li), ul (6), table (1), blockquote (2), pre/code (2) |
| R01 | ✓ | ≥3 citability-блока (таблица маршрутов, workflow, mcp.json, промпт) |
| R02 | ✓ | Preview 14.09.2026, квоты 300 r/w, 200–300 договоров, 80–100 заявок — research |
| R03 | ✓ | Нет фейкового Wordstat; Marketplace Sheets — honest note |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: финреестры doc_key + Path A/B, не dev-обзор MCP |
| E02 | ✓ | «Сделайте / Не делайте» в секциях H2 |
| E03 | ✓ | CTA: Telegram finance_modern + клуб KODA (без salebot) |
| Exp01 | ✓ | Режим B, author_id olga-kondratskaya |
| Exp02 | ✓ | Тон practice/DoD, мост B21/B82/B51/B58/B83 |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | ПДн, SA share, approval write-tools, injection из ячеек, Preview ≠ production |
| Ept02 | ✓ | Internal: B21, B82, avtomatizaciya-finansov-no-code, obezlichivanie-dannyh |
| — | ✗ | Wordstat infra: MCP-KV offline (−1 lite → 19/20) |

## Script reports

| Скрипт | Verdict | Файл |
|--------|---------|------|
| fact-check | PASS | fact-check-report.json |
| link-verify | PASS | link-verify.json |
| html-linter | PASS | html-linter-report.json |
| slop-detector | PASS | slop-detector-report.json |
| cannibalization | WARNING (portfolio) / B92 PASS | cannibalization-report.json |
| utility gate (article) | PASS | utility-gate-report.json |

## Link verify

- total: 7, failed: 0
- OK: github.com/freema/mcp-gsheets, `/blog/mcp-cursor-finansist-instrumenty/`, `/blog/google-sheets-api-integraciya-finotdel/`, `/blog/avtomatizaciya-finansov-no-code/`, `/blog/obezlichivanie-dannyh-chatgpt-finansist/`, t.me/finance_modern, club.koda-fd.ru
- `--site-base https://koda-fd.ru`

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 4
- Flesch RU: 100.0 (Very Easy)
- verdict PASS

## Fact-check

- verdict: pass (5 extracted; 1 in fact-bank; unverified numbers backed by research-notes: 200–300, 80–100, 300 r/w, Preview date)
- Marketplace Sheets status — honest note из research, не blocker

## Cannibalization

- global verdict: warning (B21↔B80 overlap 75%, не затрагивает B92)
- B92 verdict: pass — primary «mcp google sheets cursor»; adjacent B21/B82, не duplicate

## Utility gate

- article: PASS (numbered steps 17, faq_h3=7, h2=7, table=1, blockquotes=2, action_markers=19)
- report: utility-gate-report.json

## Fix cycle

- cycle 0 (prior): trim + meta_ab; PASS
- cycle 1 (2026-09-16 writer refresh Path A/B): re-verify all scripts — PASS, правок article.html GEO QA не потребовалось

## GEO QA agent (2026-09-16)

- agent: excalibur-blog-geo-qa
- gates: utility gate ✓ | html-linter ✓ | slop ✓ | link-verify ✓ | fact-check ✓ | cannibalization (B92) ✓
- verdict: **PASS** — cover/schema разрешены

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: yes (GCP→mcp.json→verify→registry scenario) | Review: no | E-E-A-T SameAs Author: pending (author_id: olga-kondratskaya)
