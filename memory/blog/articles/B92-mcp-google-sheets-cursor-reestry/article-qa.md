# QA: B92 mcp-google-sheets-cursor-reestry

date: 2026-09-17
score_total: 93/100
core_eeat_lite: 19/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 18 | primary в лиде/H1; FAQ 7; H2 how-to ×7 + FAQ; таблица Path A/B/C/B82 |
| GEO / citability | 25 | 24 | Answer-first lead 425 симв; blockquote ×2; ol×4; pre/code ×3 (mcp.json Path B/C + промпт) |
| CORE-EEAT lite | 15 | 14 | 19/20; −1 Wordstat MCP-KV unavailable (research) |
| Human voice | 15 | 15 | 0 slop hits, Flesch RU 100, режим B Ольга, «Сделайте/Не делайте» по H2 |
| Fact safety | 15 | 15 | fact-check PASS (5 extracted; 1 fact-bank + operational thresholds/HTTP из research) |
| Contract HTML | 10 | 7 | linter PASS, char_count meta 9025 (band 8500–9500), CTA club+TG ✓; −1 нет `<img>` (cover отдельно); −2 keep_ws 9362 vs collapsed 9025 (meta = strip collapsed) |

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
| char_count | 9025 (meta / collapsed); keep_ws 9362 |
| CTA | club.koda-fd.ru ×1 + t.me/finance_modern ×1 |
| TOC href="#..." | 0 |

## CORE-EEAT lite: 19/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | Title/meta + lead: MCP Google Sheets Cursor + реестр без копипаста |
| C02 | ✓ | Первый абзац — direct answer (doc_key, 1–2 ч, MCP Logs, find-update-re-read) |
| C03 | ✓ | Аудитория: финансист/CFO с реестром в Sheets |
| C04 | ✓ | MCP vs копипаст; Path A OAuth / B SA / C remote Preview |
| O01 | ✓ | H2: when → security → Path B setup → A/C → scenario → verify → next + FAQ |
| O02 | ✓ | Outline читается без body |
| O03 | ✓ | FAQ 7 (без программиста, время, OAuth/SA, риски, B82, Cloud, Google MCP) |
| O04 | ✓ | ol×4, ul×1, table×1, blockquote×2, pre×3 |
| R01 | ✓ | ≥3 citability-блока (таблица маршрутов, workflow, mcp.json, промпт DoD) |
| R02 | ✓ | 03.08.2026 changelog; quotas 300/60; Preview 14.09.2026 — research-notes |
| R03 | ✓ | Нет фейкового Wordstat; 200–300 / 80–100 — operational thresholds из research |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: финреестры doc_key + Path B SA, не generic MCP overview |
| E02 | ✓ | «Сделайте / Не делайте» в рабочих H2 |
| E03 | ✓ | CTA: Telegram finance_modern + клуб KODA (без salebot) |
| Exp01 | ✓ | Режим B, author_id olga-kondratskaya; без fake «я сделал» |
| Exp02 | ✓ | Тон practice/DoD; мост B21/B82/B51 |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | ПДн, SA share, approval write-tools, prompt injection, Cloud Agents OAuth gap |
| Ept02 | ✓ | Internal: mcp-cursor…, google-sheets-api…, avtomatizaciya…, obezlichivanie… |
| — | ✗ | Wordstat infra unavailable (−1 lite → 19/20) |

## Script reports

| Скрипт | Verdict | Файл |
|--------|---------|------|
| fact-check | PASS | fact-check-report.json |
| link-verify | PASS | link-verify.json |
| html-linter | PASS | html-linter-report.json |
| slop-detector | PASS | slop-detector-report.json |
| cannibalization | WARNING (portfolio B21↔B80; B92 OK) | cannibalization-report.json |
| utility gate (article) | PASS | utility-gate-report.json |

## Link verify

- total: 6, failed: 0, verdict: pass
- OK: `/blog/mcp-cursor-finansist-instrumenty/`, `/blog/google-sheets-api-integraciya-finotdel/`, `/blog/avtomatizaciya-finansov-no-code/`, `/blog/obezlichivanie-dannyh-chatgpt-finansist/`, t.me/finance_modern, club.koda-fd.ru
- `--site-base https://koda-fd.ru`

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 4
- Flesch RU: 100.0 (Very Easy)
- verdict PASS

## Fact-check

- verdict: pass (5 extracted; 1 verified in fact-bank; 4 operational: «1–2 часов», 200–300, 80–100, HTTP 403 — из research-notes / типичные коды, не marketing invent)
- Wordstat volumes не выдуманы

## Cannibalization

- global verdict: warning (B21↔B80 overlap 75%, не затрагивает B92)
- B92: primary «mcp google sheets cursor» — adjacent B21/B82, не duplicate

## Utility gate

- article: PASS (numbered steps 17, faq_h3=7, tables=1, blockquotes=2, action_markers=18)
- report: utility-gate-report.json

## Fix cycle

- cycle 0 (2026-09-17 geo-qa): перезапуск всех скриптов после writer refresh (char_count 9025) — PASS, правок article.html не потребовалось

## GEO QA agent (2026-09-17)

- agent: excalibur-blog-geo-qa (generalPurpose fallback)
- gates: utility ✓ | html-linter ✓ | slop ✓ | link-verify ✓ | fact-check ✓ | cannibalization (B92) ✓
- verdict: **PASS** — cover/schema разрешены директору

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: yes (GCP→mcp.json→verify→registry scenario) | Review: no | E-E-A-T SameAs Author: pending (author_id: olga-kondratskaya)
