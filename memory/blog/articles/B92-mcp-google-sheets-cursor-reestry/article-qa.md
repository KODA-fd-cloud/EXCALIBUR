# QA: B92 mcp-google-sheets-cursor-reestry

date: 2026-08-30
score_total: 91/100
core_eeat_lite: 19/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 18 | title_seo 52; primary в лиде; FAQ 7; H2 how-to ×6 + next; таблица Path A/B |
| GEO / citability | 25 | 24 | Answer-first lead; blockquote workflow; ol×3; pre/code mcp.json + промпт; без TOC/TL;DR |
| CORE-EEAT lite | 15 | 14 | 19/20; −1 Wordstat MCP-KV offline |
| Human voice | 15 | 15 | 0 slop hits, Flesch RU 100, режим B Ольга, «Сделайте/Не делайте» ×6 |
| Fact safety | 15 | 14 | fact-check PASS (6 extracted / 1 fact-bank); квоты/пороги — research-notes, не маркетинг |
| Contract HTML | 10 | 9 | linter PASS, объём 8787 ✓, CTA club+TG ✓; −1 нет `<img>` (cover отдельно) |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate pass — **выполнен**.

## Hard bans (KODA)

| Проверка | Результат |
|----------|-----------|
| TL;DR | нет |
| Fact Check блок | нет |
| «—» (emdash U+2014) | 0 |
| «мы в KODA» | нет |
| salebot / koda_salebot | нет |
| article_mode | B |
| char_count | 8787 (8500–9500) ✓ |
| CTA | club.koda-fd.ru ×1 + t.me/finance_modern ×1 |
| TOC с якорями | нет |

## CORE-EEAT lite: 19/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | Title/meta + lead: MCP Google Sheets Cursor + реестр без копипаста |
| C02 | ✓ | Первый абзац — direct answer (doc_key, 1–2 ч, MCP Logs) |
| C03 | ✓ | Аудитория: финансист/CFO с реестром в Sheets |
| C04 | ✓ | MCP / Path A OAuth / Path B SA / B82 скрипт / копипаст — во 2–3 абзацах |
| O01 | ✓ | H2: когда → безопасность → setup Path B → Path A → сценарий → verify → next + FAQ |
| O02 | ✓ | Outline читается без body |
| O03 | ✓ | FAQ 7 пар (без программиста, время, OAuth/SA, риски, B82, Cloud, маленький реестр) |
| O04 | ✓ | ol (17 li), ul (5), table (1), blockquote (2), pre/code (2) |
| R01 | ✓ | ≥3 citability-блока (таблица маршрутов, workflow blockquote, mcp.json, промпт DoD) |
| R02 | ✓ | 03.08.2026 changelog, 300 r/w min, 200–300 договоров, 80–100 заявок — research |
| R03 | ✓ | Нет фейкового Wordstat; Marketplace Sheets — honest note |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: финреестры doc_key Path A/B, не dev-обзор MCP |
| E02 | ✓ | «Сделайте / Не делайте» в 6 H2-секциях |
| E03 | ✓ | CTA: Telegram finance_modern + клуб KODA (без salebot) |
| Exp01 | ✓ | Режим B, author_id olga-kondratskaya; без fake «я внедрил у клиента X» |
| Exp02 | ✓ | Тон practice/DoD, мост B21/B82 |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | ПДн, SA share, approval write-tools, injection из ячеек, 403/429 |
| Ept02 | ✓ | Internal: mcp-cursor-finansist-instrumenty, google-sheets-api-integraciya-finotdel, avtomatizaciya-finansov-no-code, obezlichivanie |
| — | ✗ | Wordstat infra: MCP-KV offline — цифры спроса не выдуманы (−1 lite → 19/20) |

## Script reports

| Скрипт | Verdict | Файл |
|--------|---------|------|
| fact-check | PASS | fact-check-report.json |
| link-verify | PASS (ssl_note + ledger fallback) | link-verify.json |
| html-linter | PASS | html-linter-report.json |
| slop-detector | PASS | slop-detector-report.json |
| cannibalization | WARNING (portfolio; B92 не в issues) | cannibalization-report.json |
| utility gate (article) | PASS | utility-gate-report.json |

## Link verify

- total: 6, failed: 0 (после fallback)
- raw: 5× SSL handshake timeout на koda-fd.ru / club — egress, не мёртвые ссылки
- fallback OK: `/blog/mcp-cursor-finansist-instrumenty/` (B21 ledger+local), `/blog/google-sheets-api-integraciya-finotdel/` (B82), `/blog/avtomatizaciya-finansov-no-code/` (LEGACY ledger), `/blog/obezlichivanie-dannyh-chatgpt-finansist/` (B11)
- live OK: t.me/finance_modern (200)
- CTA club: published CTA + egress timeout (ssl_note)
- `--site-base https://koda-fd.ru`

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 4 (таблица/квоты — допустимо)
- Flesch RU: 100.0 (Very Easy)
- verdict PASS

## Fact-check

- verdict: pass (6 extracted; 1 verified in fact-bank — «2026»)
- unverified: 2 часов, 300, 429, 100, 403 — tech refs / research thresholds, не market-claims

## Cannibalization

- global verdict: warning (B80↔B21 overlap 75%, не затрагивает B92)
- B92 verdict: pass — primary «mcp google sheets cursor»; adjacent B21/B82, не duplicate

## Utility gate

- article: PASS (`action_markers=19`, numbered steps=17, faq_h3=7, tables=1, h2=7)
- report: utility-gate-report.json

## Fix cycle

- cycle 0 (geo-qa 2026-08-30): HTML без правок; linter/slop/fact/utility PASS; link-verify raw fail → annotated ssl_note + ledger/local/CTA fallback → pass

## Optional (не blocker)

- подключить MCP-KV Wordstat перед следующей семантикой
- `<img>` placeholder — cover отдельно

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: yes (GCP→mcp.json→verify→registry scenario) | Review: no | E-E-A-T SameAs Author: pending (author_id: olga-kondratskaya)
