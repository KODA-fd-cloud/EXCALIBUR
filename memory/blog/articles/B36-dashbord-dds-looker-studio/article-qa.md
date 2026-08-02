# QA: B36 dashbord-dds-looker-studio

date: 2026-08-02
score_total: 90/100
core_eeat_lite: 18/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 18 | H2 по outline B36, FAQ 6, primary в лиде/meta; −2 нет `<h1>` в body |
| GEO / citability | 25 | 23 | Answer-first lead, table tool-choice, ol-шаги, CASE-блок, 6 FAQ |
| CORE-EEAT lite | 15 | 14 | 18/20 (см. ниже); Wordstat MCP offline — цифры спроса не выдуманы |
| Human voice | 15 | 15 | 0 slop hits, Flesch RU 81.4, mode B, «Сделайте/Не делайте» |
| Fact safety | 15 | 13 | fact-check PASS; 4 500 ₽ / 7 дней / freshness / ПБУ 23 — из research-notes |
| Contract HTML | 10 | 7 | linter PASS, объём 8839 ✓, CTA tg+club ✓; −3 нет `<img>` (cover отдельно) |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate pass — **выполнен**.

## CORE-EEAT lite: 18/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | H1/title/meta закрывают «дашборд ддс looker studio» + Sheets за час |
| C02 | ✓ | Первый абзац — direct answer (scorecards, 15 мин, без программиста) |
| C03 | ✓ | Аудитория: финотдел / экран собственнику к совещанию |
| C04 | ✗ | Часть UI-терминов (Refresh fields, Schedule delivery) даны кратко, без 40–60 слов |
| O01 | ✓ | H2: when → prepare → build → check → next → today → FAQ |
| O02 | ✓ | Логичный how-to outline без TOC-якорного списка |
| O03 | ✓ | FAQ 6 пар (без программиста, срок, Owner's Credentials, Sheets vs Looker, переводы, «не те» цифры) |
| O04 | ✓ | ol (20 li), ul (1), table (1), blockquote (2), pre/code CASE |
| R01 | ✓ | Lead + схема blockquote + freshness/сходимость — standalone answers |
| R02 | ✓ | Freshness 15 мин–12 ч (Google docs), пакет от 4 500 ₽ / ~7 дней (FreeWorker) — research-notes |
| R03 | ✓ | Нет выдуманных %/Wordstat; цена рынка с URL в research-notes |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: DIY ДДС из Sheets за час для финотдела, не маркетинг-Looker |
| E02 | ✓ | «Сделайте / Не делайте» в ключевых H2 |
| E03 | ✓ | CTA: Telegram ×1, club.koda-fd.ru ×1 (без salebot) |
| Exp01 | ✓ | Режим B, author_id olga-kondratskaya; нет fake «я внедрил» |
| Exp02 | ✓ | Практика long-листа / Totals / переводы — не generic AI |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | Риски Owner's Credentials, ПДн, freshness ≥15 мин названы честно |
| Ept02 | ✗ | Internal links >3 из карточки/смежных (6 шт.) — избыток vs «2–3», все 200 OK |

## Script reports

| Скрипт | Verdict | Файл |
|--------|---------|------|
| utility gate (article) | PASS | utility-gate-report.json |
| html-linter | PASS | html-linter-report.json |
| slop-detector | PASS | slop-detector-report.json |
| link-verify | PASS | link-verify.json |
| cannibalization | PASS | cannibalization-report.json |
| fact-check | PASS | fact-check-report.json |

## Link verify

- total: 8, failed: 0
- `--site-base https://koda-fd.ru`
- OK internal: `/blog/disnejlend-dlya-dannyh/`, `/blog/spravochnik-kategorij-dds/`, `/blog/obezlichivanie-dannyh-chatgpt-finansist/`, `/blog/bankovskaya-vypiska-staging-google-sheets/`, `/blog/google-apps-script-finansist-obnovit-dannye/`, `/blog/avtomatizaciya-finansov-no-code/`
- OK external: `t.me/finance_modern`, `club.koda-fd.ru`

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 5 (таблица/лид — допустимо)
- Flesch RU: 81.4 (Very Easy)
- verdict PASS

## Fact-check

- verdict: pass (6 extracted; 2 verified in fact-bank; 4 unverified vs fact-bank)
- Unverified backed by research-notes: ПБУ 23/2011, 7 дней, 12 часов freshness, 4 500 ₽ — не blocker
- WORDSTAT MCP offline — цифры спроса не выдуманы

## Cannibalization

- verdict: pass (0 issues среди 26 статей; slug `dashbord-dds-looker-studio` уникален)
- CLI: `--blog-dir memory/blog/articles -o …/cannibalization-report.json`

## Utility gate

- article: PASS (`action_markers=22`, numbered steps=20, faq_h3=6, tables=1, h2_sections=6)

## Fix cycle

- cycle: 0 (FIX не требуется)

## Forbidden checks

- em dash (—): 0
- ёлочки «»: 0
- salebot: 0
- emoji in body: 0
- MCP URLs in production: 0
- TOC с `href="#..."`: 0

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (6) | HowTo: yes (Sheets → Looker DDS) | Review: no | E-E-A-T SameAs Author: pending (author_id: olga-kondratskaya)
