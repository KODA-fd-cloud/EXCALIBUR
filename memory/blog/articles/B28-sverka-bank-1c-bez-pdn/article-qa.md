# QA: B28 sverka-bank-1c-bez-pdn

date: 2026-08-01
score_total: 89/100
core_eeat_lite: 17/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 19 | H2 по карточке B28, FAQ 7, primary в лиде/meta; −1 нет `<h1>` в body |
| GEO / citability | 25 | 23 | Answer-first lead, таблица маскирования + сравнение локально/облако, blockquote-схема, ol-шаги, 7 FAQ |
| CORE-EEAT lite | 15 | 13 | 17/20 (см. ниже); −2 Wordstat без MCP-KV |
| Human voice | 15 | 15 | 0 slop hits, Flesch RU 62.6, режим B Ольга, «Сделайте/Не делайте» |
| Fact safety | 15 | 13 | fact-check PASS; ФСБУ 28/2023, 500-2000 строк из research-notes, не blocker |
| Contract HTML | 10 | 6 | linter PASS, объём 8562 ✓, CTA ≤2 ✓; −4 нет `<img>` (cover отдельно) |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate pass — **выполнен**.

## CORE-EEAT lite: 17/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | Title/meta + lead закрывают «сверка банка и 1с» + без ПДн в ChatGPT |
| C02 | ✓ | Первый абзац — direct answer (обороты 51, обезличивание, локальный Python) |
| C03 | ✓ | Аудитория: CFO/финменеджер, self-serve checklist |
| C04 | ✓ | DoD, ОСВ 51, outer merge, DirectBank расшифрованы |
| O01 | ✓ | H2 совпадают с outline B28 (+ «Что сделать сегодня») |
| O02 | ✓ | Outline: что сравниваем → маскирование → локально/облако → чеклист → 1С-ник |
| O03 | ✓ | FAQ 7 пар |
| O04 | ✓ | ol (11 li), ul (7), table (2), blockquote (2) |
| R01 | ✓ | Таблица маскирования + сравнение маршрутов + blockquote-вердикт |
| R02 | ✓ | ФСБУ 28/2023, 402-ФЗ, 152-ФЗ — research-notes + practice |
| R03 | ✗ | Wordstat-цифры не получены (MCP-KV offline) — в тексте нет фейкового спроса |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: сверка + политика ПДн + локальный merge, не DirectBank onboarding |
| E02 | ✓ | «Сделайте / Не делайте» в 5 H2-секциях |
| E03 | ✓ | CTA: Telegram, club.koda-fd.ru (без salebot) |
| Exp01 | ✓ | Режим B, author_id olga-kondratskaya |
| Exp02 | ✓ | Практика закрытия месяца, без generic AI |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | Маскирование, локальный диск, карта замен |
| Ept02 | ✓ | Internal: /obezlichivanie-dannyh-chatgpt-finansist/, /python-finansist-sverka-csv/ |
| — | ✗ | R03 partial: нет свежих Wordstat — −1 к lite (итого 17/20) |

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

- total: 4, failed: 0
- OK: `/blog/obezlichivanie-dannyh-chatgpt-finansist/`, `/blog/python-finansist-sverka-csv/`, club.koda-fd.ru, t.me/finance_modern
- `--site-base https://koda-fd.ru`

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 4 (таблицы/blockquote — допустимо)
- Flesch RU: 62.6 (Easy)
- verdict PASS

## Fact-check

- verdict: pass (4 extracted; 2 verified in fact-bank; 2 unverified — ФСБУ 28/2023, 500-2000 из research-notes, не blocker)

## Cannibalization

- verdict: pass (0 issues)

## Utility gate

- article: PASS (`action_markers=19`, numbered steps=11, faq_h3=7, tables=2)

## Fix cycle

- cycle 0: правки не потребовались — все скрипты PASS с первого прогона

## Forbidden checks

- em dash (—): 0
- salebot: 0
- MCP URLs in production: 0

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: yes (подготовка + маскирование + сверка) | Review: no | E-E-A-T SameAs Author: pending (author_id: olga-kondratskaya)
