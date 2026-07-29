# QA: B13 vygruzka-1c-excel-odata

date: 2026-07-22
score_total: 90/100
core_eeat_lite: 18/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 19 | H2 по карточке B13, FAQ 6, primary в лиде/H1 meta; −1 нет `<h1>` в body |
| GEO / citability | 25 | 23 | Answer-first lead 431, таблица сравнения, схема →, ol-шаги, 6 FAQ; без TOC/TL;DR (KODA) |
| CORE-EEAT lite | 15 | 13 | 18/20 (см. ниже); −2 Wordstat без MCP-KV |
| Human voice | 15 | 15 | 0 slop hits, Flesch RU 81.4, режим B Ольга, «Сделайте/Не делайте» |
| Fact safety | 15 | 13 | fact-check PASS; числа 255/$top/2000 из research-notes, не fact-bank |
| Contract HTML | 10 | 7 | linter PASS, объём 8760 ✓, CTA ≤3 ✓; −3 нет `<img>` (cover отдельно) |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate pass — **выполнен**.

## CORE-EEAT lite: 18/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | Title/meta + lead закрывают «выгрузка из 1с в excel» + OData |
| C02 | ✓ | Первый абзац — direct answer, без «в этой статье» |
| C03 | ✓ | Аудитория: финансист, self-serve после разовой публикации |
| C04 | ✓ | OData = курьер/акт сверки; JSON расшифрован |
| O01 | ✓ | H2 совпадают с карточкой B13 (+ «Что дальше») |
| O02 | ✓ | Outline: когда OData → публикация → Excel → Sheets → security |
| O03 | ✓ | FAQ 6 пар из faq_hints |
| O04 | ✓ | ol (16 li), ul (2), table (1), blockquote (2) |
| R01 | ✓ | Сравнительная таблица + вердикт + схема цепочки |
| R02 | ✓ | URL/сущности УНФ, лимиты — research-notes + practice dds-sheets |
| R03 | ✗ | Wordstat-цифры не получены (MCP-KV offline) — в тексте нет фейкового спроса |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: OData → Excel + кнопка Sheets + граница «звать 1С-ника» |
| E02 | ✓ | «Сделайте / Не делайте» в каждой H2-секции |
| E03 | ✓ | CTA: Telegram, клуб KODA, @koda_salebot |
| Exp01 | ✓ | Режим B, author_id olga-kondratskaya |
| Exp02 | ✓ | Практика УНФ ДДС, без generic AI |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | Read-only user, узкий состав OData, обезличивание перед ChatGPT |
| Ept02 | ✓ | Internal: /ot-excel-k-fin-konturu-30-dney/, /obezlichivanie-dannyh-chatgpt-finansist/ |
| — | ✗ | R03 partial: нет свежих Wordstat — −1 к lite (итого 18/20) |

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
- OK: `/blog/ot-excel-k-fin-konturu-30-dney/`, `/blog/obezlichivanie-dannyh-chatgpt-finansist/`, koda-fd.ru/club, t.me/finance_modern, t.me/koda_salebot
- `--site-base https://koda-fd.ru`
- note: сертификат koda-fd.ru expired на дату прогона; HTTP 200 подтверждён с unverified SSL context (`ssl_note` в JSON)

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 1 (таблица → допустимо)
- Flesch RU: 81.4 (Very Easy)
- verdict PASS

## Fact-check

- verdict: pass (5 extracted; 1 verified in fact-bank; 4 unverified — из research-notes/practice, не blocker)

## Cannibalization

- verdict: pass (0 issues)

## Utility gate

- article: PASS (`action_markers=17`, numbered steps=16)
- FIX cycle 1: «Делать/Не делать» → «Сделайте/Не делайте» + «Избегайте…» (было 6 < 8 маркеров)

## Fix cycle

- cycle 1: GEO QA — utility gate BLOCK → точечные правки article.html (императивные маркеры); char_count → 8760; meta geo_qa

## Optional (не blocker)

- обновить SSL-сертификат koda-fd.ru (инфра)
- подключить MCP-KV Wordstat перед следующей итерацией семантики
- `<img>` placeholder UI — по желанию перед Дзен (cover отдельно)

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (6) | HowTo: yes (публикация + Excel + Sheets) | Review: no | E-E-A-T SameAs Author: pending (author_id: olga-kondratskaya)
