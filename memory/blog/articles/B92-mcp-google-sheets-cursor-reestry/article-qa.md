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
| SEO structure | 20 | 18 | primary в лиде; FAQ 7; H2 how-to ×7 + FAQ; таблица Path A/B/C |
| GEO / citability | 25 | 24 | Answer-first lead 441 симв; blockquote ×2; ol×4; pre/code mcp.json Path B + Path C + промпт |
| CORE-EEAT lite | 15 | 14 | 19/20; −1 Wordstat MCP-KV offline |
| Human voice | 15 | 15 | 0 slop hits, Flesch RU 100, режим B Ольга, «Сделайте/Не делайте» ×6 |
| Fact safety | 15 | 15 | fact-check PASS; цифры/порты/403 из research-notes; Wordstat не выдуман |
| Contract HTML | 10 | 7 | linter PASS, char_count 8889 ✓ (band 8500–9500), CTA club+TG ✓; −3 нет `<img>` (cover отдельно) |

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
| char_count | 8889 (collapsed); keep_ws 9288 |
| CTA | club.koda-fd.ru ×1 + t.me/finance_modern ×1 |
| TOC в теле | нет (0 `#` hash-href) |

## CORE-EEAT lite: 19/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | Title/meta + lead: MCP Google Sheets Cursor + реестр без копипаста |
| C02 | ✓ | Первый абзац — direct answer (doc_key, 1-2 ч, find-update-re-read) |
| C03 | ✓ | Аудитория: финансист/CFO с реестром в Sheets |
| C04 | ✓ | Path A OAuth / Path B SA / Path C remote preview; MCP vs B82 |
| O01 | ✓ | H2: когда → безопасность → Path B → Path A/C → сценарий → verify → next + FAQ |
| O02 | ✓ | Outline читается без body |
| O03 | ✓ | FAQ 7 пар (без программиста, время, OAuth/SA, риски, B82, Google remote, Cloud) |
| O04 | ✓ | ol (4), ul (1), table (1), blockquote (2), pre/code (3) |
| R01 | ✓ | ≥3 citability-блока (таблица маршрутов, workflow, mcp.json×2, промпт) |
| R02 | ✓ | 03.08.2026 changelog, 14.09.2026 docs Path C, 200-300 договоров, 80-100 заявок — research |
| R03 | ✓ | Нет фейкового Wordstat; Path C = Developer Preview честно |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: финреестры doc_key + Path B production; не dev-обзор MCP |
| E02 | ✓ | «Сделайте / Не делайте» в 6 H2-секциях |
| E03 | ✓ | CTA: Telegram finance_modern + клуб KODA (без salebot) |
| Exp01 | ✓ | Режим B, author_id olga-kondratskaya |
| Exp02 | ✓ | Тон practice/DoD, мост B21/B82 + Path C preview |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | ПДн, SA share, approval write-tools, prompt injection из ячеек |
| Ept02 | ✓ | Internal: mcp-cursor, sheets-api B82, no-code, обезличивание |
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
- method: live HEAD 200 ×6

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 4
- Flesch RU: 100.0 (Very Easy)
- verdict PASS

## Fact-check

- verdict: pass (1/6 exact fact-bank; 5 unverified в bank — порты/HTTP 403/диапазоны из research-notes, не blocker)
- Path C Developer Preview + Marketplace honest note — OK

## Cannibalization

- global verdict: warning (B80↔B21 overlap 75%, не затрагивает B92)
- B92 verdict: pass — primary «mcp google sheets cursor»; adjacent B21/B82, не duplicate

## Utility gate

- article: PASS (numbered steps 17, faq_h3=7, h2=7, table=1, blockquotes=2, action_markers=18)
- report: utility-gate-report.json

## Fix cycle

- cycle 0: все скрипты PASS на char_count 8889; правок article.html не потребовалось
- FIX для writer: нет

## GEO QA agent (2026-09-17)

- agent: excalibur-blog-geo-qa
- gates: utility gate ✓ | html-linter ✓ | slop ✓ | link-verify ✓ | fact-check ✓ | cannibalization (B92) ✓
- verdict: **PASS** — cover/schema разрешены

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: yes (GCP→mcp.json→verify→registry scenario + Path A/C) | Review: no | E-E-A-T SameAs Author: pending (author_id: olga-kondratskaya)
