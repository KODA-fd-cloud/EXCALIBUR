# QA: B29 spravochnik-kategorij-dds

date: 2026-08-01
score_total: 90/100
core_eeat_lite: 19/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 19 | H2 по карточке B29, FAQ 6, primary в лиде/meta; −1 нет `<h1>` в body |
| GEO / citability | 25 | 23 | Answer-first lead, таблица 4 групп, blockquote-схема, ol-шаги (17 li), 6 FAQ |
| CORE-EEAT lite | 15 | 14 | 19/20 (см. ниже); −1 Wordstat без MCP-KV |
| Human voice | 15 | 15 | 0 slop hits, Flesch RU 48.2 (Standard), режим B Ольга, «Сделайте/Не делайте» |
| Fact safety | 15 | 13 | fact-check PASS; ПБУ 23/2011, «200 строк», «30 дней» из research/slug — не blocker |
| Contract HTML | 10 | 6 | linter PASS, объём 9316 ✓, CTA ≤2 ✓; −4 нет `<img>` (cover отдельно) |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate pass — **выполнен**.

## CORE-EEAT lite: 19/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | Title/meta + lead закрывают «категории ддс справочник» + anti-разъезд отчётов |
| C02 | ✓ | Первый абзац — direct answer (единый справочник, validation, один код) |
| C03 | ✓ | Аудитория: CFO/финменеджер, self-serve checklist за один вечер |
| C04 | ✓ | DoD: 4 группы, DDS_Categories, SUMIFS/QUERY, validation «отклонять ввод» |
| O01 | ✓ | H2 совпадают с outline B29 (+ «Что сделать сегодня» + FAQ) |
| O02 | ✓ | Outline: объём → справочник → Прочее/переводы → команда → план-факт |
| O03 | ✓ | FAQ 6 пар |
| O04 | ✓ | ol (17 numbered), ul (1), table (1), blockquote (2) |
| R01 | ✓ | Таблица групп + blockquote-схема staging→категория→отчёт + вердикт |
| R02 | ✓ | ПБУ 23/2011 (п. 7), 152-ФЗ, правило «Прочее» — research-notes |
| R03 | ✗ | Wordstat-цифры не получены (MCP-KV offline) — в тексте нет фейкового спроса; 5% из research |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: единый справочник + validation + регламент, не «что такое ДДС» |
| E02 | ✓ | «Сделайте / Не делайте» в 5 H2-секциях |
| E03 | ✓ | CTA: Telegram, club.koda-fd.ru (без salebot) |
| Exp01 | ✓ | Режим B, author_id olga-kondratskaya |
| Exp02 | ✓ | Практика Google Sheets validation, без generic AI |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | Риски: Прочее как чёрная дыра, 152-ФЗ, не копировать план счетов 1С |
| Ept02 | ✓ | Internal ×3: disnejlend-dlya-dannyh, bankovskaya-vypiska-staging, ot-excel-k-fin-konturu-30-dney |

## Script reports

| Скрипт | Verdict | Файл |
|--------|---------|------|
| fact-check | PASS | fact-check-report.json |
| link-verify | PASS | link-verify.json |
| html-linter | PASS | html-linter-report.json |
| slop-detector | PASS | slop-detector-report.json |
| cannibalization | PASS | cannibalization-report.json |
| utility gate (article) | PASS | utility-gate-report.json |

## Link verify

- total: 5, failed: 0
- OK: `/blog/disnejlend-dlya-dannyh/`, `/blog/bankovskaya-vypiska-staging-google-sheets/`, `/blog/ot-excel-k-fin-konturu-30-dney/`, club.koda-fd.ru, t.me/finance_modern
- `--site-base https://koda-fd.ru`
- B26 plan-fakt — без href (не опубликован), как в Writer

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 5 (таблица/blockquote — допустимо)
- Flesch RU: 48.2 (Standard)
- verdict PASS

## Fact-check

- verdict: pass (4 extracted; 1 verified in fact-bank; 3 unverified — ПБУ 23/2011, «200», «30 дней» из research-notes / slug — не blocker)

## Cannibalization

- verdict: pass (0 issues среди 24 статей)

## Utility gate

- article: PASS (`action_markers=12`, numbered steps=17, faq_h3=6, tables=1, h2=6)

## Fix cycle

- cycle 0: правки не потребовались — все скрипты PASS; FIX list пуст

## Forbidden checks

- em dash (—): 0
- salebot: 0
- MCP URLs in production: 0

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (6) | HowTo: yes (справочник + validation + команда) | Review: no | E-E-A-T SameAs Author: pending (author_id: olga-kondratskaya)
