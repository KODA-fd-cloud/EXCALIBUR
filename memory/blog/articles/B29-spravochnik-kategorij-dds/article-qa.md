# QA: B29 spravochnik-kategorij-dds

date: 2026-08-01
score_total: 95/100
core_eeat_lite: 18/20
link_verify: pass
utility_gate: pass
verdict: PASS
re_run: after writer FIX (B26 href removed) — all scripts re-run 2026-08-01

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 19 | H2 по карточке B29, FAQ 6, primary в лиде/meta; −1 нет `<h1>` в body |
| GEO / citability | 25 | 23 | Answer-first lead, таблица 4 групп, blockquote-схема, ol-шаги (17 li), 6 FAQ |
| CORE-EEAT lite | 15 | 14 | 18/20 (см. ниже); −1 Wordstat без MCP-KV (R03) |
| Human voice | 15 | 15 | 0 slop hits, Flesch RU 47.8 (Standard), режим B Ольга, «Сделайте/Не делайте» |
| Fact safety | 15 | 14 | fact-check PASS; 1 verified / 3 unverified (ПБУ 23/2011, «200», «30 дней») — не blocker |
| Contract HTML | 10 | 10 | linter PASS, CTA ≤2 ✓, img placeholder ✓, link-verify pass (5/5) |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate pass — **выполнен**.

## CORE-EEAT lite: 18/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | Title/meta + lead закрывают «категории ддс справочник» + anti-разъезд отчётов |
| C02 | ✓ | Первый абзац — direct answer (единый справочник, validation, один код) |
| C03 | ✓ | Аудитория: CFO/финменеджер, self-serve checklist |
| C04 | ✓ | DoD: 4 группы, DDS_Categories, SUMIFS/QUERY, validation «отклонять ввод» |
| O01 | ✓ | H2 совпадают с outline B29 (+ «Что сделать сегодня») |
| O02 | ✓ | Outline: объём → справочник → Прочее/переводы → команда → план-факт |
| O03 | ✓ | FAQ 6 пар |
| O04 | ✓ | ol (17 li utility), ul (1), table (1), blockquotes (2) |
| R01 | ✓ | Таблица групп + blockquote-схема staging→категория→отчёт |
| R02 | ✓ | ПБУ 23/2011 (4 группы потоков), 152-ФЗ — research-notes + practice |
| R03 | ✗ | Wordstat-цифры не получены (MCP-KV offline) — в тексте нет фейкового спроса |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: единый справочник + validation + регламент, не «что такое ДДС» |
| E02 | ✓ | «Сделайте / Не делайте» в H2-секциях |
| E03 | ✓ | CTA: Telegram, club.koda-fd.ru (без salebot) |
| Exp01 | ✓ | Режим B, author_id olga-kondratskaya |
| Exp02 | ✓ | Практика Google Sheets validation, без generic AI |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | Код категории латиницей, именованный диапазон, контрольная формула |
| Ept02 | ✓ | B26 без dead href: plain text «план-факт ДДС в Google Sheets (B26, ссылка после публикации)» |

## Script reports (re-run)

| Скрипт | Verdict | Файл |
|--------|---------|------|
| fact-check | PASS | fact-check-report.json |
| link-verify | **PASS** (5/5) | link-verify.json |
| html-linter | PASS | html-linter-report.json |
| slop-detector | PASS | slop-detector-report.json |
| cannibalization | PASS | cannibalization-report.json |
| utility gate (article) | PASS | utility-gate-report.json |

## Link verify

- total: 5, failed: 0, verdict: **pass**
- OK: `/blog/disnejlend-dlya-dannyh/`, `/blog/bankovskaya-vypiska-staging-google-sheets/`, `/blog/ot-excel-k-fin-konturu-30-dney/`, club.koda-fd.ru, t.me/finance_modern
- B26 `/blog/plan-fakt-dds-google-sheets/` — **нет в HTML** (writer FIX cycle 1)

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 4 (таблица/blockquote — допустимо)
- Flesch RU: 47.8 (Standard)
- verdict PASS

## Fact-check

- verdict: pass (4 extracted; 1 verified in fact-bank; 3 unverified — ПБУ 23/2011, «200», «30 дней» из research/anchors, не blocker)

## Cannibalization

- verdict: pass (0 issues среди 24 статей)

## Utility gate

- article: PASS (`action_markers=12`, numbered steps=17, faq_h3=6, tables=1)

## FIX history

1. Cycle 1 (done): убран href B26 → plain text; re-run link-verify → pass.
2. Дальнейших FIX не требуется.

## Forbidden checks

- em dash (—): 0
- salebot: 0
- MCP URLs in production: 0

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (6) | HowTo: yes (справочник + validation + команда) | Review: no | E-E-A-T SameAs Author: pending (author_id: olga-kondratskaya)  
**cover||schema можно запускать** (article-qa PASS).
