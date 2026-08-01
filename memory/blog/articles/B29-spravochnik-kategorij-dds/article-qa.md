# QA: B29 spravochnik-kategorij-dds

date: 2026-08-01
score_total: 92/100
core_eeat_lite: 19/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 18 | primary в title_seo/лиде; H2 how_to; FAQ 6; −2 длинный H1/title в meta |
| GEO / citability | 25 | 24 | Answer-first lead, таблица 4 групп, blockquote-схема, ol 17 li, 6 FAQ |
| CORE-EEAT lite | 15 | 14 | 19/20 (см. ниже); −1 Wordstat MCP-KV offline |
| Human voice | 15 | 15 | 0 slop hits, Flesch RU 47.5 (Standard), режим B Ольга, «Сделайте/Не делайте» |
| Fact safety | 15 | 14 | fact-check PASS; ПБУ 23/2011 и «200» из research-notes, не blocker |
| Contract HTML | 10 | 7 | linter PASS, объём 8966 ✓, CTA ≤2 ✓; −3 нет `<img>` (cover отдельно) |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate pass — **выполнен**.

## Hard bans (KODA)

| Проверка | Результат |
|----------|-----------|
| TL;DR | нет |
| Fact Check блок | нет |
| «—» (emdash U+2014) | 0 (только en-dash «–») |
| «мы в KODA» | нет |
| salebot / koda_salebot | нет |
| article_mode | B |
| char_count | 8966 (8500–9500) ✓ |
| CTA | club.koda-fd.ru ×1 + t.me/finance_modern ×1 |
| TOC с якорями `#` | нет |

## CORE-EEAT lite: 19/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | Title/meta + lead закрывают «категории ддс справочник» + anti-разъезд отчётов |
| C02 | ✓ | Первый абзац — direct answer (единый справочник, validation, один код) |
| C03 | ✓ | Аудитория: CFO/финменеджер, self-serve checklist за вечер |
| C04 | ✓ | Управленческий справочник vs план счетов; validation; DDS_Categories |
| O01 | ✓ | H2 совпадают с outline B29 (+ «Что сделать сегодня») |
| O02 | ✓ | Outline: объём → справочник → Прочее/переводы → команда → план-факт |
| O03 | ✓ | FAQ 6 пар |
| O04 | ✓ | ol (17 li), ul (1), table (1), blockquote (2) |
| R01 | ✓ | Lead + таблица групп + blockquote-схема staging→категория→отчёт |
| R02 | ✓ | ПБУ 23/2011, ориентир 20–25 статей — research-notes (Fintablo) |
| R03 | ✓ | Нет фейкового Wordstat/процентов/цен |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: единый справочник + validation + регламент команды, не «что такое ДДС» |
| E02 | ✓ | «Сделайте / Не делайте» в H2-секциях |
| E03 | ✓ | CTA: Telegram + club.koda-fd.ru (без salebot) |
| Exp01 | ✓ | Режим B, author_id olga-kondratskaya; без fake «я сделал» |
| Exp02 | ✓ | Практика Google Sheets validation / именованный диапазон |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | 152-ФЗ/доступ; «Прочее»; риск раздува выручки переводами |
| Ept02 | ✓ | Internal: disnejlend, ot-excel-k-fin-konturu, bankovskaya-vypiska (все 200) |
| — | ✗ | Wordstat infra: MCP-KV offline — цифры спроса не выдуманы (−1 lite → 19/20) |

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
- OK: `/blog/disnejlend-dlya-dannyh/`, `/blog/ot-excel-k-fin-konturu-30-dney/`, `/blog/bankovskaya-vypiska-staging-google-sheets/`, club.koda-fd.ru, t.me/finance_modern
- `--site-base https://koda-fd.ru`

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 3 (таблица/blockquote — допустимо)
- Flesch RU: 47.5 (Standard)
- verdict PASS

## Fact-check

- verdict: pass (2 extracted; 0 verified in fact-bank; 2 unverified — «2011»/ПБУ 23/2011, «200» строк — оба в research-notes, не blocker)

## Cannibalization

- verdict: pass (0 issues среди 24 статей)

## Utility gate

- article: PASS (`action_markers=12`, numbered steps=17, faq_h3=6, tables=1, blockquotes=2)

## Fix cycle

- cycle 0: HTML без правок GEO QA; все скрипты PASS с первого прогона

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (6) | HowTo: yes (справочник + validation + команда) | Review: no | E-E-A-T SameAs Author: pending (author_id: olga-kondratskaya)
