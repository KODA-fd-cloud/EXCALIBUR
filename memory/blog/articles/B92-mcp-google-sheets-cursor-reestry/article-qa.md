# QA: B92 mcp-google-sheets-cursor-reestry

date: 2026-09-12
score_total: 95/100
core_eeat_lite: 19/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 18 | primary в лиде; FAQ 7; H2 how-to ×8; таблица Path A/B; meta_ab OK |
| GEO / citability | 25 | 24 | Answer-first lead 425; blockquote workflow; ol×3; pre/code mcp.json + промпт |
| CORE-EEAT lite | 15 | 14 | 19/20; −1 Wordstat MCP-KV offline |
| Human voice | 15 | 15 | 0 slop hits, Flesch RU 100, режим B Ольга, «Сделайте/Не делайте» |
| Fact safety | 15 | 14 | fact-check PASS; unverified = HTTP-коды/длительности из research, не market-claims |
| Contract HTML | 10 | 10 | linter PASS; CTA club+TG ✓; plain **9280** в банде 8500–9500; meta.char_count = plain |

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
| char_count (plain, без тегов) | **9280 — PASS** (8500–9500) |
| char_count в meta | 9280 = plain ✓ |
| CTA | club.koda-fd.ru ×1 + t.me/finance_modern ×1 |
| TOC с якорями | нет |

## CORE-EEAT lite: 19/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | Title/meta + lead: MCP Google Sheets Cursor + реестр без копипаста |
| C02 | ✓ | Первый абзац — direct answer (doc_key, 1–2 ч, MCP Logs) |
| C03 | ✓ | Аудитория: финансист/CFO с реестром в Sheets |
| C04 | ✓ | MCP / Path A OAuth / Path B SA / vs B82 — объяснены |
| O01 | ✓ | H2: когда → security → Path B → Path A → сценарий → verify → next + FAQ |
| O02 | ✓ | Outline читается без body |
| O03 | ✓ | FAQ 7 пар |
| O04 | ✓ | ol, ul, table, blockquote×2, pre×2 |
| R01 | ✓ | ≥3 citability (таблица, workflow, mcp.json, промпт) |
| R02 | ✓ | квоты 300/60, Error 400 cursor://, Path B freema — research-notes 2026-09-12 |
| R03 | ✓ | Нет фейкового Wordstat/процентов |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: финреестры doc_key, не dev-обзор MCP |
| E02 | ✓ | «Сделайте / Не делайте» в H2-секциях |
| E03 | ✓ | CTA: TG + клуб KODA (без salebot) |
| Exp01 | ✓ | Режим B, author_id olga-kondratskaya |
| Exp02 | ✓ | Тон practice/DoD |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | ПДн, Share SA, approval write, injection |
| Ept02 | ✓ | Internal ×4: mcp-cursor…, google-sheets-api…, no-code, обезличивание |
| — | ✗ | Wordstat infra offline (−1) → 19/20 |

## Script reports

| Скрипт | Verdict | Файл |
|--------|---------|------|
| fact-check | PASS | fact-check-report.json |
| link-verify | PASS | link-verify.json |
| html-linter | PASS | html-linter-report.json |
| slop-detector | PASS | slop-detector-report.json |
| cannibalization | WARNING (portfolio B21↔B80) | cannibalization-report.json |
| utility gate (article) | PASS | utility-gate-report.json |

## Link verify

- total: 6, failed: 0
- OK: `/blog/mcp-cursor-finansist-instrumenty/`, `/blog/google-sheets-api-integraciya-finotdel/`, `/blog/avtomatizaciya-finansov-no-code/`, `/blog/obezlichivanie-dannyh-chatgpt-finansist/`, t.me/finance_modern, club.koda-fd.ru
- `--site-base https://koda-fd.ru`

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 2 (таблица + MCP-абзац)
- Flesch RU: 100.0 (Very Easy)
- verdict PASS

## Fact-check

- verdict: pass (extracted stats; verified in fact-bank «2026»; unverified = «2 часов», 300/400/403/429 — HTTP/длительности, не выдуманные % спроса)

## Cannibalization

- global verdict: warning (B21↔B80 overlap 75%, не затрагивает B92)
- B92: primary «mcp google sheets cursor» — не duplicate соседних

## Utility gate

- article: PASS (`action_markers`, numbered steps, faq_h3=7, tables=1)
- meta.char_count=9280 согласован с plain

## Fix cycle

- cycle 0 (writer 2026-09-12): trim HTML `len` → 9313; meta_ab OK
- cycle 1 (geo-qa): **FAIL** — plain ~7216 < 8500; meta считал `len(html)`
- cycle 1 (writer FIX): plain **9280**, meta.char_count = plain
- cycle 1 (geo-qa recheck): **PASS**

## GEO QA agent (2026-09-12 recheck)

- agent: excalibur-blog-geo-qa
- gates scripts: utility ✓ | linter ✓ | slop ✓ | link-verify ✓ | fact-check ✓ | cannibalization (B92) ✓
- contract volume: **PASS** (plain 9280)
- verdict: **PASS** — директор может запускать cover \|\| schema

## Schema ready (handoff для schema-агента)

BlogPosting: ready | FAQPage: yes (7) | HowTo: yes | Review: no | author_id: olga-kondratskaya
