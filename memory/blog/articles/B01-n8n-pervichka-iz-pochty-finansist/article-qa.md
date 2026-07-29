# QA: B01 n8n-pervichka-iz-pochty-finansist

date: 2026-06-17
score_total: 92/100
core_eeat_lite: 19/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 19 | H2/H3, FAQ 7, primary query, якорные id — OK; −1 нет `<h1>` в body (title в meta) |
| GEO / citability | 25 | 24 | Lead answer-first, TL;DR, таблица hosting, 8+5 шагов, 7 FAQ |
| CORE-EEAT lite | 15 | 14 | 19/20 (см. ниже); −1 Wordstat-цифры не в fact-bank |
| Human voice | 15 | 15 | 0 AI-slop hits, Flesch RU 84.9, режим B Ольга |
| Fact safety | 15 | 13 | fact-check PASS; 7/11 чисел unverified (Вордстат, тарифы — из research-notes) |
| Contract HTML | 10 | 7 | linter PASS, объём 8679 ✓, CTA ≤3 ✓; −3 нет `<img>` с alt (cover отдельно) |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate pass — **выполнен**.

## CORE-EEAT lite: 19/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | Title/meta + lead закрывают «n8n для финансиста» |
| C02 | ✓ | Первый абзац — direct answer, без «в этой статье» |
| C03 | ✓ | Аудитория: финансист/CFO без программиста |
| C04 | ✓ | IMAP, API, LLM, JSON — «на пальцах» |
| O01 | ✓ | H2 совпадают с карточкой B01 (+ секция «Что дальше») |
| O02 | ✓ | Outline: зачем → хостинг → workflow → промпты → чек-лист |
| O03 | ✓ | FAQ 7 пар, реальные queries из faq_hints |
| O04 | ✓ | ol (8+5), ul (9), table |
| R01 | ✓ | TL;DR + blockquote-схемы, standalone блоки |
| R02 | ✓ | Тарифы n8n, IMAP Яндекс, шаблон #9439 — research-notes |
| R03 | ✓ | Цены с оговоркой «июнь 2026»; 60–70% — «по оценкам из открытых материалов» |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: RU Яндекс IMAP + staging Sheets + HITL |
| E02 | ✓ | «Делайте / Не делайте» в каждой H2 |
| E03 | ✓ | CTA клуб KODA, Telegram finance_modern, @koda_salebot |
| Exp01 | ✓ | Режим B, автор olga-kondratskaya, без fake case |
| Exp02 | ✓ | Тон brief/research, не generic AI |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | 152-ФЗ, зарубежные LLM, HITL, галлюцинации сумм |
| Ept02 | ✓ | Internal links: /avtomatizaciya-finansov-no-code/, /ot-excel-k-fin-konturu-30-dney/ |

## Script reports

| Скрипт | Verdict | Файл |
|--------|---------|------|
| fact-check | PASS | fact-check-report.json |
| link-verify | PASS | link-verify.json |
| html-linter | PASS | html-linter-report.json |
| slop-detector | WARNING | slop-detector-report.json |
| cannibalization | PASS | cannibalization-report.json |
| utility gate (article) | PASS | utility-gate-report.json |

## Link verify

- total: 6, failed: 0
- OK: koda-fd.ru/avtomatizaciya-finansov-no-code/, koda-fd.ru/ot-excel-k-fin-konturu-30-dney/, koda-fd.ru/club, koda-fd.ru/, t.me/finance_modern, t.me/koda_salebot
- `--site-base https://koda-fd.ru`

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 7 (таблица/чеклист/термины — допустимо)
- Flesch RU: 84.9 (Very Easy)
- verdict WARNING — не blocker (Exp03: 0 hits)
- see `slop-detector-report.json`

## Fact-check

- verdict: pass (11 extracted, 4 verified in fact-bank, 7 unverified — Вордстат/тарифы/порт 993 из research, не blocker)
- see `fact-check-report.json`

## Cannibalization

- verdict: pass (0 issues, 6 articles in blog-dir)
- see `cannibalization-report.json`

## Utility gate

- article: PASS (`excalibur_blog_utility_gate.py --article-dir`)
- topic: PASS (utility-gate-topic.json)

## Fix cycle

- cycle 0: первичный GEO QA — без правок writer

## Optional (не blocker)

- добавить `<img>` с alt перед publish в WP (для Дзен — cover отдельно)
- занести Wordstat-цифры и тарифы n8n Cloud в fact-bank
- сократить 1–2 длинных предложения в lead и секции чек-листа

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: yes (8 шагов) | Review: no | E-E-A-T SameAs Author: pending (author_id: olga-kondratskaya)
