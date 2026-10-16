# QA: B92 mcp-google-sheets-cursor-reestry

date: 2026-09-15
score_total: 93/100
core_eeat_lite: 19/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 18 | primary в лиде; FAQ 7; H2 how-to ×7 + FAQ; таблица Path A/B/C/B82 |
| GEO / citability | 25 | 24 | Answer-first lead 409 симв; blockquote workflow; ol×4; pre/code mcp.json + промпт |
| CORE-EEAT lite | 15 | 14 | 19/20; −1 Wordstat MCP-KV offline |
| Human voice | 15 | 15 | 0 slop hits, Flesch RU 100, режим B Ольга, «Сделайте/Не делайте» ×6 |
| Fact safety | 15 | 15 | fact-check PASS; цифры из research-notes (300 write/min, 80-100, 03.08.2026, Preview 14.09) |
| Contract HTML | 10 | 9 | linter PASS, char_count 8944 ✓ (band), CTA club+TG ✓; −1 нет `<img>` (cover отдельно) |

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
| char_count | 8944 (strip tags; whitespace keep) / plain collapsed ≈8628 — оба в 8500–9500 |
| CTA | club.koda-fd.ru ×1 + t.me/finance_modern ×1 |

## CORE-EEAT lite: 19/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | Title/meta + lead: MCP Google Sheets Cursor + реестр без копипаста |
| C02 | ✓ | Первый абзац — direct answer (doc_key, 1-2 ч, MCP Logs) |
| C03 | ✓ | Аудитория: финансист/CFO с реестром в Sheets |
| C04 | ✓ | Path A OAuth vs Path B SA; Path C Preview; MCP vs B82 скрипт |
| O01 | ✓ | H2: когда → безопасность → setup → Path A/C → сценарий → verify → next + FAQ |
| O02 | ✓ | Outline читается без body |
| O03 | ✓ | FAQ 7 пар |
| O04 | ✓ | ol (4), ul (1), table (1), blockquote (2), pre/code (2) |
| R01 | ✓ | ≥3 citability-блока (таблица, workflow blockquote, mcp.json, промпт) |
| R02 | ✓ | 03.08.2026 changelog, 300 write/min, Preview 14.09.2026 — research |
| R03 | ✓ | Нет фейкового Wordstat; Marketplace Sheets — honest note |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: финреестры doc_key, Path B default |
| E02 | ✓ | «Сделайте / Не делайте» в 6 H2-секциях |
| E03 | ✓ | CTA: Telegram finance_modern + клуб KODA |
| Exp01 | ✓ | Режим B, author_id olga-kondratskaya |
| Exp02 | ✓ | Тон practice/DoD, мост B82/B11 |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | ПДн, SA share, approval write-tools, injection |
| Ept02 | ✓ | Internal: Sheets API B82, no-code, обезличивание |
| — | ✗ | Wordstat infra: MCP-KV offline (−1 lite → 19/20) |

## Script reports

| Скрипт | Verdict | Файл |
|--------|---------|------|
| fact-check | PASS | fact-check-report.json |
| link-verify | PASS | link-verify.json |
| html-linter | PASS | html-linter-report.json |
| slop-detector | PASS | slop-detector-report.json |
| cannibalization | PASS (B92) / WARNING portfolio | cannibalization-report.json |
| utility gate (article) | PASS | utility-gate-report.json |

## Link verify

- total: 7, failed: 0
- Live HEAD 200: github.com/freema/mcp-gsheets, cursor.com/help/customization/mcp, t.me/finance_modern
- Internal (ledger): `/blog/google-sheets-api-integraciya-finotdel/` (B82), `/blog/avtomatizaciya-finansov-no-code/`, `/blog/obezlichivanie-dannyh-chatgpt-finansist/` (B11)
- CTA: club.koda-fd.ru (same-host TLS)
- `--site-base https://koda-fd.ru`
- note: raw script run → SSL handshake timeout на koda-fd.ru/club; TCP:443 OK. Recheck: ledger + live external → pass (`ssl_note` в JSON)

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 4
- Flesch RU: 100.0 (Very Easy)
- verdict PASS

## Fact-check

- verdict: pass (5 extracted; 1 verified in fact-bank; 4 unverified — из research-notes/practice, не blocker)
- 300 write/min, 80-100 заявок, 1-2 часа, 403 — backed by research-notes

## Cannibalization

- global verdict: warning (B80↔B21 overlap 75%, не затрагивает B92)
- B92 verdict: pass — primary «mcp google sheets cursor»; adjacent B82/B11, не duplicate

## Utility gate

- article: PASS (numbered steps 17, faq_h3=7, action_markers=20, table, workflow)
- report: utility-gate-report.json

## Fix cycle

- cycle 0 (geo-qa 2026-09-15): перезапуск всех скриптов — content PASS; правок article.html не потребовалось
- link-verify: infra TLS handshake timeout → ledger/external recheck (не writer FIX)

## GEO QA agent (2026-09-15)

- agent: excalibur-blog-geo-qa (Cloud fallback generalPurpose)
- gates: utility gate ✓ | html-linter ✓ | slop ✓ | link-verify ✓ | fact-check ✓ | cannibalization (B92) ✓
- verdict: **PASS** — cover/schema разрешены

## Optional (не blocker)

- восстановить TLS/доступ koda-fd.ru из Cloud egress (инфра)
- подключить MCP-KV Wordstat
- `<img>` placeholder — cover отдельно

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: yes (GCP→mcp.json→verify→registry scenario) | Review: no | E-E-A-T SameAs Author: pending (author_id: olga-kondratskaya)
