# QA: B92 mcp-google-sheets-cursor-reestry

date: 2026-09-16
score_total: 90/100
core_eeat_lite: 18/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 18 | primary в лиде; 7 H2 action + FAQ 7; Path A/B/C таблица |
| GEO / citability | 25 | 23 | Answer-first lead; ol setup+сценарий; pre/code mcp.json + промпт; blockquote |
| CORE-EEAT lite | 15 | 14 | 18/20; −1 Wordstat MCP-KV offline; −1 fact-bank gaps на HTTP-коды/квоты (есть в research) |
| Human voice | 15 | 14 | 0 slop; Flesch RU 100; «Сделайте/Не делайте»; 3 over-long (допустимо) |
| Fact safety | 15 | 13 | fact-check PASS; 5 unverified = 403/400/300/100/2ч из research, не fact-bank |
| Contract HTML | 10 | 8 | linter PASS; объём 9460 ✓; CTA club+TG ✓; −1 нет inline `<img>` (cover отдельно); −1 link-fix |

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
| char_count | 9460 (в коридоре 8500–9500) |
| CTA | club.koda-fd.ru ×1 + t.me/finance_modern ×1 |

## CORE-EEAT lite: 18/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | Title/meta + lead: MCP Google Sheets Cursor + реестр без копипаста |
| C02 | ✓ | Первый абзац — direct answer (doc_key, 1–2 ч, MCP Logs) |
| C03 | ✓ | Аудитория: финансист/CFO с реестром в Sheets |
| C04 | ✓ | Path A OAuth vs Path B SA vs Path C; MCP vs B82 скрипт |
| O01 | ✓ | H2: когда → безопасность → setup → Path A → сценарий → verify → next + FAQ |
| O02 | ✓ | Outline читается без body |
| O03 | ✓ | FAQ 7 пар |
| O04 | ✓ | ol, ul, table, blockquote, pre/code |
| R01 | ✓ | Таблица маршрутов, workflow, mcp.json, промпт |
| R02 | ✓ | 03.08.2026, 300/60 квоты, 200–300 договоров, 80–100 заявок — research |
| R03 | ✓ | Нет фейкового Wordstat; OAuth баги — honest |
| R04 | ✓ | FAQ: ответ-действие в первом предложении |
| E01 | ✓ | Угол: финреестры doc_key, не dev-обзор MCP |
| E02 | ✓ | «Сделайте / Не делайте» в H2-секциях |
| E03 | ✓ | CTA: Telegram + клуб (без salebot) |
| Exp01 | ✓ | Режим B, author_id olga-kondratskaya |
| Exp02 | ✓ | Мост B21/B82/no-code/обезличивание |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | ПДн, SA share, approval write-tools, injection |
| Ept02 | ✓ | Internal links на сайте |
| — | ✗ | Wordstat infra: MCP-KV offline (−1) |
| — | ✗ | Цифры квот/порогов не в fact-bank (−1 lite; закрыты research-notes) |

## Script reports

| Скрипт | Verdict | Файл |
|--------|---------|------|
| fact-check | PASS | fact-check-report.json |
| link-verify | PASS (7/7) | link-verify.json |
| html-linter | PASS | html-linter-report.json |
| slop-detector | PASS | slop-detector-report.json |
| cannibalization | PASS для B92 (global WARN B21↔B80) | cannibalization-report.json |
| utility gate (article) | PASS | utility-gate-report.json |

## Link verify

- total: 7, failed: 0
- OK: `/blog/mcp-cursor-finansist-instrumenty/`, `/blog/google-sheets-api-integraciya-finotdel/`, `/blog/avtomatizaciya-finansov-no-code/`, `/blog/obezlichivanie-dannyh-chatgpt-finansist/`, forum.cursor.com (OAuth workaround), t.me/finance_modern, club.koda-fd.ru
- `--site-base https://koda-fd.ru`

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 3
- Flesch RU: 100.0 (Very Easy)
- verdict PASS

## Fact-check

- verdict: pass (1/6 exact in fact-bank; 5 unverified = HTTP/квоты/длительности из research-notes)
- не blocker

## Cannibalization

- global verdict: warning (B21↔B80 overlap 75%, не затрагивает B92)
- B92 verdict: pass — primary «mcp google sheets cursor»; adjacent B21/B82, не duplicate

## Utility gate

- article: PASS (numbered steps 17, faq_h3=7, actionable H2=7, table, workflow)
- report: utility-gate-report.json

## Fix cycle

- cycle 0 (geo-qa 2026-09-16): link-verify FAIL — `https://cursor.com/agents` → HTTP 403 для UA ExcaliburBlogLinkVerify
- fix: убран прямой href на cursor.com/agents; путь Agents оставлен текстом; ссылка на тред форума из research (`google-plugins-broken-auth-2-0`)
- cycle 1: все скрипты PASS; char_count meta → 9460

## GEO QA agent (2026-09-16)

- agent: excalibur-blog-geo-qa
- gates: utility gate ✓ | html-linter ✓ | slop ✓ | link-verify ✓ | fact-check ✓ | cannibalization (B92) ✓
- verdict: **PASS** — cover/schema разрешены

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: yes (GCP→mcp.json→verify→registry scenario) | Review: no | E-E-A-T SameAs Author: pending (author_id: olga-kondratskaya)
