# QA: B29 spravochnik-kategorij-dds

date: 2026-08-01
score_total: 89/100
core_eeat_lite: 17/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 19 | H2 по карточке B29, FAQ 6, primary в лиде/meta; −1 нет `<h1>` в body |
| GEO / citability | 25 | 23 | Answer-first lead, таблица 4 групп, blockquote-схема, ol-шаги (17 li), 6 FAQ |
| CORE-EEAT lite | 15 | 13 | 17/20 (см. ниже); −2 Wordstat без MCP-KV |
| Human voice | 15 | 15 | 0 slop hits, Flesch RU 45.8 (Standard), режим B Ольга, «Сделайте/Не делайте» |
| Fact safety | 15 | 13 | fact-check PASS; ПБУ 23/2011, «200 строк» из research-notes, не blocker |
| Contract HTML | 10 | 6 | linter PASS, объём 9293 ✓, CTA ≤2 ✓; −4 нет `<img>` (cover отдельно) |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate pass — **выполнен**.

## CORE-EEAT lite: 17/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | Title/meta + lead закрывают «категории ддс справочник» + anti-разъезд отчётов |
| C02 | ✓ | Первый абзац — direct answer (единый справочник, validation, один код) |
| C03 | ✓ | Аудитория: CFO/финменеджер, self-serve checklist |
| C04 | ✓ | DoD: 4 группы, DDS_Categories, SUMIFS/QUERY, validation «отклонять ввод» |
| O01 | ✓ | H2 совпадают с outline B29 (+ «Что сделать сегодня») |
| O02 | ✓ | Outline: объём → справочник → Прочее/переводы → команда → план-факт |
| O03 | ✓ | FAQ 6 пар |
| O04 | ✓ | ol (17 li), ul (3), table (1), blockquote (2) |
| R01 | ✓ | Таблица групп + blockquote-схема staging→категория→отчёт |
| R02 | ✓ | ПБУ 23/2011 (4 группы потоков), 152-ФЗ — research-notes + practice |
| R03 | ✗ | Wordstat-цифры не получены (MCP-KV offline) — в тексте нет фейкового спроса |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: единый справочник + validation + регламент, не «что такое ДДС» |
| E02 | ✓ | «Сделайте / Не делайте» в 5 H2-секциях |
| E03 | ✓ | CTA: Telegram, club.koda-fd.ru (без salebot) |
| Exp01 | ✓ | Режим B, author_id olga-kondratskaya |
| Exp02 | ✓ | Практика Google Sheets validation, без generic AI |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | Код категории латиницей, именованный диапазон, контрольная формула |
| Ept02 | ✗ | B26 `/plan-fakt-dds-google-sheets/` — 404 (очередь); plain text до publish B26 |
| — | ✗ | R03 partial: нет свежих Wordstat — −1 к lite (итого 17/20) |

## Script reports

| Скрипт | Verdict | Файл |
|--------|---------|------|
| utility gate (article) | PASS | utility-gate-report.json |
| html-linter | PASS | html-linter-report.json |
| slop-detector | PASS (WARNING) | slop-detector-report.json |
| link-verify | PASS | link-verify.json |
| cannibalization | PASS | cannibalization-report.json |
| fact-check | PASS | fact-check-report.json |

## Link verify

- total: 4, failed: 0
- OK: `/blog/disnejlend-dlya-dannyh/`, `/blog/bankovskaya-vypiska-staging-google-sheets/`, club.koda-fd.ru, t.me/finance_modern
- `--site-base https://koda-fd.ru`
- B26 `/blog/plan-fakt-dds-google-sheets/` — 404 (не опубликован); заменён на plain text

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 7 (таблицы/blockquote — допустимо)
- Flesch RU: 45.8 (Standard)
- verdict PASS (WARNING по длинным предложениям, не blocker)

## Fact-check

- verdict: pass (3 extracted; 1 verified in fact-bank; 2 unverified — ПБУ 23/2011, «200 строк» из research-notes, не blocker)

## Cannibalization

- verdict: pass (0 issues среди 24 статей)

## Utility gate

- article: PASS (`action_markers=11`, numbered steps=17, faq_h3=6, tables=1)

## Fix cycle

- cycle 1: GEO QA — `<a href="/blog/plan-fakt-dds-google-sheets/">` → plain text «план-факт ДДС в Google Sheets (B26, href после публикации)» (HTTP 404 — B26 в очереди)

## Forbidden checks

- em dash (—): 0
- salebot: 0
- MCP URLs in production: 0

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (6) | HowTo: yes (справочник + validation + команда) | Review: no | E-E-A-T SameAs Author: pending (author_id: olga-kondratskaya)
