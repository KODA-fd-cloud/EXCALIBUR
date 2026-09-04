# QA: B92 mcp-google-sheets-cursor-reestry

date: 2026-09-04
score_total: 93/100
core_eeat_lite: 19/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 18 | primary в лиде; FAQ 7; H2 how-to ×7 (+FAQ H2); таблица Path A/B |
| GEO / citability | 25 | 24 | Answer-first lead 440 симв; Workflow blockquote; ol×4; pre/code mcp.json + промпт |
| CORE-EEAT lite | 15 | 14 | 19/20; −1 Wordstat MCP-KV offline (research) |
| Human voice | 15 | 15 | 0 slop hits, Flesch RU 100, режим B Ольга, «Сделайте»×6 / «Не делайте»×7 |
| Fact safety | 15 | 14 | fact-check PASS (1/5 в fact-bank; 300 write/min, 80–100, 1–2 ч, 403 — research-notes) |
| Contract HTML | 10 | 9 | linter PASS, объём 9415 ✓, CTA club+TG ✓; −1 нет `<img>` (cover отдельно) |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate pass — **выполнен**.

## Hard bans (KODA)

| Проверка | Результат |
|----------|-----------|
| TL;DR blockquote | нет |
| Fact Check блок | нет |
| «—» (emdash U+2014) | 0 |
| «мы в KODA» | нет |
| salebot / koda_salebot | нет |
| TOC href="#..." | нет |
| article_mode | B |
| char_count | 9415 |
| CTA | club.koda-fd.ru ×1 + t.me/finance_modern ×1 |

## CORE-EEAT lite: 19/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | Title/meta + lead: MCP Google Sheets Cursor + реестр без копипаста |
| C02 | ✓ | Первый абзац — direct answer (Path B, doc_key, 1–2 ч, MCP Logs) |
| C03 | ✓ | Аудитория: финансист/CFO с реестром в Sheets |
| C04 | ✓ | Path A OAuth vs Path B SA; MCP vs B82 скрипт; vs копипаст |
| O01 | ✓ | H2: when → security → setup → Path A → scenario → verify → next + FAQ |
| O02 | ✓ | Outline читается без body |
| O03 | ✓ | FAQ 7 пар |
| O04 | ✓ | ol (22 li в 4 блоках), ul (1), table (1), blockquote (1), pre/code (2) |
| R01 | ✓ | ≥3 citability-блока (таблица, workflow, mcp.json, промпт) |
| R02 | ✓ | 03.08.2026 changelog, 300 write/min, 80–100 заявок, Cursor 3.19 — research |
| R03 | ✓ | Нет фейкового Wordstat; OAuth/`cursor://` — honest note |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: финреестры doc_key, не dev-обзор MCP |
| E02 | ✓ | «Сделайте / Не делайте» в H2-секциях |
| E03 | ✓ | CTA: Telegram finance_modern + клуб KODA (без salebot) |
| Exp01 | ✓ | Режим B, author_id olga-kondratskaya |
| Exp02 | ✓ | Тон practice/DoD, мост B21/B82 |
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
| cannibalization | PASS (B92) | cannibalization-report.json |
| utility gate (article) | PASS | utility-gate-report.json |

## Link verify

- total: 6, failed: 0
- OK: `/blog/mcp-cursor-finansist-instrumenty/`, `/blog/google-sheets-api-integraciya-finotdel/`, `/blog/avtomatizaciya-finansov-no-code/`, `/blog/obezlichivanie-dannyh-chatgpt-finansist/`, t.me/finance_modern, club.koda-fd.ru
- `--site-base https://koda-fd.ru`
- Нет `cursor.com/agents` в href (только текстовый «dashboard Agents») — WAF 403 обойдён

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 2 (ложные склейки table/blockquote extractor)
- Flesch RU: 100.0 (Very Easy)
- verdict PASS

## Fact-check

- verdict: pass (1 exact fact-bank + 4 research-backed: 1–2 ч, 300 write/min, 80–100, HTTP 403)
- Marketplace Sheets / `cursor://` — honest note из research, не blocker

## Cannibalization

- global verdict: warning (B80↔B21 overlap 75%, не затрагивает B92)
- B92 verdict: pass — primary «mcp google sheets cursor»; adjacent B21/B82, не duplicate

## Utility gate

- article: PASS (numbered steps 17, faq_h3=7, h2=7, table=1, action_markers=19)
- report: utility-gate-report.json

## Fix cycle

- cycle 0 (writer 2026-09-04): re-fit 10889→9415; Path B production-default; все скрипты PASS
- cycle 1 (geo-qa 2026-09-04): перезапуск всех скриптов — PASS, правок article.html не потребовалось

## GEO QA agent (2026-09-04)

- agent: excalibur-blog-geo-qa (Cloud fallback generalPurpose)
- gates: utility gate ✓ | html-linter ✓ | slop ✓ | link-verify ✓ | fact-check ✓ | cannibalization (B92) ✓
- verdict: **PASS** — cover/schema разрешены

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: yes (GCP→mcp.json→verify→registry scenario) | Review: no | E-E-A-T SameAs Author: pending (author_id: olga-kondratskaya)
