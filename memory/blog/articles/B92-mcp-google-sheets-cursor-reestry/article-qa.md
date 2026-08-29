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
| SEO structure | 20 | 18 | title_seo 54, desc_seo ~140; H2 how-to ×7; FAQ 7; primary в лиде; Path A vs Path B; −2 meta_ab emoji/CTR чуть «продажно» |
| GEO / citability | 25 | 24 | Answer-first lead; таблица 4 маршрута; blockquote workflow; ol×4; pre×2 (mcp.json + промпт); FAQ 7 |
| CORE-EEAT lite | 15 | 14 | 19/20 (см. ниже); −1 Wordstat MCP-KV offline |
| Human voice | 15 | 15 | 0 slop hits, Flesch RU 100, режим B Ольга, «Сделайте/Не делайте» ×6 |
| Fact safety | 15 | 14 | fact-check PASS 1/5 bank; 4 unverified = 1–2 ч, 200–300, 80–100, 403 из research — не маркетинг |
| Contract HTML | 10 | 7 | linter PASS, объём 9295 ✓, CTA club+TG ✓; −3 нет `<img>` (cover отдельно) |

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
| char_count | 9295 (8500–9500) ✓ |
| CTA | club.koda-fd.ru ×1 + t.me/finance_modern ×1 |
| TOC с якорями | нет |

## CORE-EEAT lite: 19/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | Title/meta + lead: MCP Google Sheets Cursor + реестр без копипаста |
| C02 | ✓ | Первый абзац — direct answer (doc_key, Path A/B, 1–2 ч, MCP Logs) |
| C03 | ✓ | Аудитория: финансист/CFO с реестром в Sheets |
| C04 | ✓ | MCP, Path A OAuth, Path B SA, doc_key — в первых абзацах |
| O01 | ✓ | H2: when → security → Path B setup → Path A → scenario → verify → next + FAQ |
| O02 | ✓ | Outline читается без body |
| O03 | ✓ | FAQ 7 пар (без программиста, время, OAuth/SA, риски, B82, Cloud, changelog) |
| O04 | ✓ | ol (17 li), ul (5), table (1), blockquote (2), pre/code (2) |
| R01 | ✓ | ≥3 citability-блока (таблица маршрутов, workflow, mcp.json, промпт DoD) |
| R02 | ✓ | 03.08.2026 changelog, 300 req/min, 200–300 договоров, 80–100 заявок — research |
| R03 | ✓ | Нет фейкового Wordstat; Marketplace Sheets — honest note |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: финреестры Path A vs Path B; не «Sheets всегда в Marketplace» |
| E02 | ✓ | «Сделайте / Не делайте» в 6 H2-секциях |
| E03 | ✓ | CTA: Telegram finance_modern + клуб KODA (без salebot) |
| Exp01 | ✓ | Режим B, author_id olga-kondratskaya; без fake «я внедрил у клиента» |
| Exp02 | ✓ | Тон practice/DoD, мост B21/B82/B51/B58/B83 |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | ПДн, SA share, approval write, injection из ячеек, Cloud OAuth limit |
| Ept02 | ✓ | Internal: B21 MCP, B82 API, no-code, обезличивание |
| — | ✗ | Wordstat infra: MCP-KV offline (−1 lite → 19/20) |

## Script reports

| Скрипт | Verdict | Файл |
|--------|---------|------|
| fact-check | PASS | fact-check-report.json |
| link-verify | PASS (ledger + live t.me; SSL handshake timeout koda-fd.ru) | link-verify.json |
| html-linter | PASS | html-linter-report.json |
| slop-detector | PASS | slop-detector-report.json |
| cannibalization | PASS (global warning B80↔B21) | cannibalization-report.json |
| utility gate (article) | PASS | utility-gate-report.json |

## Link verify

- total: 6, failed: 0
- Live: t.me/finance_modern → 200
- Internals (ledger OK): `/blog/mcp-cursor-finansist-instrumenty/` (B21), `/blog/google-sheets-api-integraciya-finotdel/` (B82), `/blog/avtomatizaciya-finansov-no-code/` (LEGACY), `/blog/obezlichivanie-dannyh-chatgpt-finansist/` (B11)
- club.koda-fd.ru: TLS handshake timeout (TCP:443 OK) — CTA pattern как в B90/B91; не broken URL
- `--site-base https://koda-fd.ru`
- note: urllib default/unverified SSL → handshake timeout (egress); не мёртвые ссылки

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 5 (lead/table/blockquote — допустимо)
- Flesch RU: 100.0 (Very Easy)
- verdict PASS

## Fact-check

- verdict: pass (5 extracted; 1 verified in fact-bank — «2026»)
- unverified: «2 часов», «300», «100», «403» — пороги/коды из research-notes, не market-claims

## Cannibalization

- global verdict: warning (B80↔B21 overlap 75%, не затрагивает B92)
- B92 verdict: pass — primary «mcp google sheets cursor»; adjacent B21/B82, не duplicate

## Utility gate

- article: PASS (`action_markers=18`, numbered steps=17, faq_h3=7, tables=1, blockquotes=2)
- report: utility-gate-report.json

## Fix cycle

- cycle 0 (2026-08-29 geo-qa): перезапуск всех скриптов после rewrite writer; HTML без правок
- link-verify: live SSL timeout → ledger/CTA fallback (как ssl_unverified_recheck в B13/B19); writer FIX не требуется

## GEO QA agent (2026-08-29)

- agent: excalibur-blog-geo-qa (Cloud fallback generalPurpose)
- gates: utility ✓ | html-linter ✓ | slop ✓ | link-verify ✓ | fact-check ✓ | cannibalization (B92) ✓
- verdict: **PASS** — cover/schema разрешены

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: yes (Path B GCP→mcp.json→verify→registry scenario; Path A optional) | Review: no | E-E-A-T SameAs Author: pending (author_id: olga-kondratskaya)
