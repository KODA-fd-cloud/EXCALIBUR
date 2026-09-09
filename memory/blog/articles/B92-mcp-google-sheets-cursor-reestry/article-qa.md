# QA: B92 mcp-google-sheets-cursor-reestry

date: 2026-09-09
score_total: 91/100
core_eeat_lite: 19/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 18 | primary в лиде; FAQ 7; H2 how-to ×5 + FAQ; таблица Path A/B; meta_ab ok |
| GEO / citability | 25 | 24 | Answer-first lead 455 симв; blockquote workflow×2; ol; pre/code mcp.json ×3 |
| CORE-EEAT lite | 15 | 14 | 19/20; −1 Wordstat MCP-KV offline (research) |
| Human voice | 15 | 14 | 0 slop hits, Flesch RU 100, режим B Ольга, «Сделайте/Не делайте»; −1 5 over-long |
| Fact safety | 15 | 15 | fact-check PASS; квоты 300/60 и 80–100 заявок — research-notes URLs |
| Contract HTML | 10 | 6 | linter PASS (после FIX `</code>`), объём 9461 ✓, CTA club×2+TG×1 ≤3 ✓; −4 нет `<img>` (cover отдельно) |

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
| char_count | 9461 (plain без тегов, с whitespace; 8500–9500) ✓ |
| CTA | club.koda-fd.ru ×2 + t.me/finance_modern ×1 (итого 3; лимиты conversion-map: club≤2, TG≤2) |
| TOC с якорями | нет |

## CORE-EEAT lite: 19/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | Title/meta + lead: MCP Google Sheets Cursor + реестр без копипаста |
| C02 | ✓ | Первый абзац — direct answer (doc_key, 1–2 ч, Path A/B) |
| C03 | ✓ | Аудитория: финансист/CFO с реестром в Sheets |
| C04 | ✓ | Path A OAuth vs Path B SA; MCP vs B82 скрипт; vs копипаст |
| O01 | ✓ | H2: when → security → setup → verify → next + FAQ |
| O02 | ✓ | Outline читается без body |
| O03 | ✓ | FAQ 7 пар |
| O04 | ✓ | ol, ul, table×1, blockquote×2, pre/code×3 |
| R01 | ✓ | ≥3 citability-блока (таблица маршрутов, workflow, mcp.json, DoD-промпт) |
| R02 | ✓ | 09.09.2026 / 03.08.2026 changelog, 300/60 req/min, 80–100 заявок — research |
| R03 | ✓ | Нет фейкового Wordstat; Marketplace Sheets — honest note |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: финреестры doc_key, не dev-обзор MCP |
| E02 | ✓ | «Сделайте / Не делайте» в H2-секциях |
| E03 | ✓ | CTA: Telegram finance_modern + клуб KODA ×2 (без salebot) |
| Exp01 | ✓ | Режим B, author_id olga-kondratskaya |
| Exp02 | ✓ | Тон practice/DoD, мост B21/B82 |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | ПДн: обезличивание, SA share, approval write-tools |
| Ept02 | ✓ | Internal: mcp-cursor-finansist-instrumenty, google-sheets-api-integraciya-finotdel, avtomatizaciya-finansov-no-code, obezlichivanie-dannyh-chatgpt-finansist |
| — | ✗ | Wordstat infra: MCP-KV offline (−1 lite → 19/20) |

## Script reports

| Скрипт | Verdict | Файл |
|--------|---------|------|
| fact-check | PASS | fact-check-report.json |
| link-verify | PASS | link-verify.json |
| html-linter | PASS | html-linter-report.json |
| slop-detector | PASS | slop-detector-report.json |
| cannibalization | PASS (B92 не в issues) | cannibalization-report.json |
| utility gate (article) | PASS | utility-gate-report.json |

## Link verify

- total: 9, failed: 0
- OK: `/blog/mcp-cursor-finansist-instrumenty/`, `/blog/google-sheets-api-integraciya-finotdel/`, `/blog/avtomatizaciya-finansov-no-code/`, `/blog/obezlichivanie-dannyh-chatgpt-finansist/`, cursor.com/help/mcp, developers.google.com Sheets MCP, forum.cursor.com Drive MCP, t.me/finance_modern, club.koda-fd.ru
- `--site-base https://koda-fd.ru`

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 5
- Flesch RU: 100.0 (Very Easy)
- verdict PASS

## Fact-check

- verdict: pass (4 extracted; 1 in fact-bank; 3 tech metrics backed by research-notes URLs: 300/60 quotas, 80–100 заявок, 1–2 часа)
- Marketplace Sheets status — honest note из research, не blocker

## Cannibalization

- global verdict: warning (B80↔B21 overlap 75%, не затрагивает B92)
- B92 verdict: pass — primary «mcp google sheets cursor»; adjacent B21/B82, не duplicate

## Utility gate

- article: PASS (numbered steps 17, faq_h3=7, tables=1, blockquotes=2, action_markers=19)
- report: utility-gate-report.json

## Fix cycle

- cycle 0 (writer): article.html + meta char_count 9461; CTA club×2 + TG×1
- cycle 1 (geo-qa): FIX html-linter — закрыть `</code>` в 3× `<pre><code>` блоках mcp.json; re-run всех скриптов → PASS

## GEO QA agent (2026-09-09)

- agent: excalibur-blog-geo-qa
- gates: utility gate ✓ | html-linter ✓ | slop ✓ | link-verify ✓ | fact-check ✓ | cannibalization (B92) ✓
- CTA note: writer дал 3 CTA (club×2 + Telegram×1) — в лимитах conversion-map / contract ≤3; FAIL не требуется
- verdict: **PASS** — cover/schema разрешены

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: yes (GCP→mcp.json→verify→registry scenario) | Review: no | E-E-A-T SameAs Author: pending (author_id: olga-kondratskaya)
