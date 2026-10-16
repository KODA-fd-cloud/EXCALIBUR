# QA: B92 mcp-google-sheets-cursor-reestry

date: 2026-08-24
score_total: 96/100
core_eeat_lite: 19/20
link_verify: **pass**
utility_gate: pass
verdict: **PASS**
re_run: after Writer FIX cycle 1

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 18 | primary в лиде; FAQ 7; H2 how-to; таблица Path A/B |
| GEO / citability | 25 | 24 | Answer-first lead 425 симв; blockquote workflow; ol; pre/code mcp.json + промпт |
| CORE-EEAT lite | 15 | 14 | 19/20; −1 Wordstat MCP-KV offline |
| Human voice | 15 | 15 | 0 slop hits, Flesch RU 100, режим B Ольга, «Сделайте/Не делайте» |
| Fact safety | 15 | 15 | цифры 300/60/404/03.08.2026 в research-notes; fact-check PASS; link-verify PASS |
| Contract HTML | 10 | 10 | linter PASS, объём 9264 ✓, CTA club+TG ✓; link-verify 6/6 PASS |

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
| char_count | 9264 (в коридоре 8500–9500) |
| CTA | club.koda-fd.ru ×1 + t.me/finance_modern ×1 |

## CORE-EEAT lite: 19/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | Title/meta + lead: MCP Google Sheets Cursor + реестр без копипаста |
| C02 | ✓ | Первый абзац — direct answer (doc_key, 1–2 ч, MCP Logs) |
| C03 | ✓ | Аудитория: финансист/CFO с реестром в Sheets |
| C04 | ✓ | Path A OAuth vs Path B SA; MCP vs B82; vs копипаст |
| O01 | ✓ | H2: когда → безопасность → setup → Path A → сценарий → ошибки → next + FAQ |
| O02 | ✓ | Outline читается без body |
| O03 | ✓ | FAQ 7 пар |
| O04 | ✓ | ol, ul, table, blockquote, pre/code |
| R01 | ✓ | Citability: таблица маршрутов, workflow, mcp.json, промпт |
| R02 | ✓ | 03.08.2026, 300/60 квоты, 80–100 заявок — research-notes |
| R03 | ✓ | Нет фейкового Wordstat; Marketplace 404 — honest |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: финреестры doc_key |
| E02 | ✓ | «Сделайте / Не делайте» |
| E03 | ✓ | CTA Telegram + клуб (без salebot) |
| Exp01 | ✓ | Режим B, author_id olga-kondratskaya |
| Exp02 | ✓ | Тон practice/DoD, мост B21/B82 |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | ПДн: обезличивание, SA share, approval write |
| Ept02 | ✓ | Internal: avtomatizaciya-finansov-no-code, obezlichivanie-dannyh-chatgpt-finansist |
| — | ✗ | Wordstat infra: MCP-KV offline (−1 → 19/20) |

## Script reports (re-run 2026-08-24)

| Скрипт | Verdict | Файл |
|--------|---------|------|
| fact-check | PASS | fact-check-report.json |
| link-verify | **PASS** (6/6) | link-verify.json |
| html-linter | PASS | html-linter-report.json |
| slop-detector | PASS | slop-detector-report.json |
| cannibalization | WARNING (не B92) | cannibalization-report.json |
| utility gate (article) | PASS | utility-gate-report.json |

## Link verify

- total: 6, failed: 0, verdict: **pass**
- OK: 4 internal `/blog/*`, `t.me/finance_modern`, `club.koda-fd.ru`
- `cursor.com/agents` — plain text (без `<a href>`), не проверяется скриптом — FIX cycle 1 подтверждён
- `--site-base https://koda-fd.ru`

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 3
- Flesch RU: 100.0
- verdict PASS

## Fact-check

- script verdict: pass (extracted 6; 1 in fact-bank; 5 heuristic numbers)
- Ручная сверка с research-notes: 404 Marketplace, 03.08.2026 changelog, квоты 300/60, 80–100 заявок — **OK**
- «403» в тексте = ошибка Share/API, не URL; «1–2 часов» — оценка из research outline

## Cannibalization

- global verdict: warning (B80↔B21 overlap 75%, **не затрагивает B92**)
- B92: primary `mcp google sheets cursor` — duplicate не найден → **pass для темы**

## Utility gate

- article: PASS (numbered steps, actionable markers, table, workflow)
- report: utility-gate-report.json

## Meta soft checks (FIX cycle 1)

- `secondary_queries`: без голого `"2026"` ✓ (`автоматизация финотдела`, `mcp google sheets cursor`)

## Fix cycle

- cycle 0 (writer): article.html готов, meta_ab есть
- cycle 1 (geo-qa): **FAIL** — link `href=https://cursor.com/agents` → 403
- cycle 1 (writer FIX): убран href → plain text; secondary без `"2026"`
- cycle 2 (geo-qa re-run): **PASS** — link-verify 6/6; score 96/100

## GEO QA agent (2026-08-24, re-run)

- agent: excalibur-blog-geo-qa
- gates: utility ✓ | html-linter ✓ | slop ✓ | link-verify ✓ | fact-check ✓ | cannibalization (B92) ✓
- verdict: **PASS** — директор может запускать cover || schema
