# QA: B33 akty-sverki-reestr-kontrol

date: 2026-08-02
score_total: 88/100
core_eeat_lite: 18/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 18 | H2 по outline B33, FAQ 7, primary «реестр актов сверки» в лиде/meta |
| GEO / citability | 25 | 22 | Answer-first lead, table колонок, 2× blockquote-схемы, ol-шаги, FAQ citability-first |
| CORE-EEAT lite | 15 | 13 | 18/20 (см. ниже); −2 Wordstat unavailable |
| Human voice | 15 | 14 | mode B Ольга, 0 slop, «Сделайте/Не делайте»; Flesch RU 70.2 |
| Fact safety | 15 | 13 | fact-check PASS; 0510477 / ст.203 из research-notes; примеры сумм в таблице = иллюстрация |
| Contract HTML | 10 | 8 | linter PASS, объём ~9.2k ✓, CTA club+tg ≤2 ✓; −2 нет `<img>` (cover отдельно) |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate pass — **выполнен**.

## CORE-EEAT lite: 18/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | Title/H1/lead закрывают «реестр актов сверки» + контроль ответов без CRM |
| C02 | ✓ | Первый абзац — direct answer (реестр + статусы + Sheets→n8n→email) |
| C03 | ✓ | Аудитория: финансист малого финотдела |
| C04 | ✓ | Акт ≠ первичка 402-ФЗ; 0510477 = госсектор; статусы draft→closed |
| O01 | ✓ | H2: колонки → статусы → n8n → граница 1С → ДЗ/месяц → запуск |
| O02 | ✓ | Логичный workflow outline |
| O03 | ✓ | FAQ 7 пар |
| O04 | ✓ | ol 16 li, ul 2, table 1, blockquote 2 |
| R01 | ✓ | Lead + статусы + n8n-схема — standalone answer blocks |
| R02 | ✓ | Закон не обязывает; ст.203 ГК / Пленум ВС; 0510477 с 01.01.2026 — research-notes |
| R03 | ✗ | Wordstat недоступен (MCP-KV offline) — цифр спроса в тексте нет (не выдуманы) |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол Sheets/Excel + n8n без CRM, не клон 0510477/Entera/1С |
| E02 | ✓ | «Сделайте / Не делайте» в рабочих H2 |
| E03 | ✓ | CTA: t.me/finance_modern + club.koda-fd.ru (без salebot) |
| Exp01 | ✓ | Режим B, author_id olga-kondratskaya |
| Exp02 | ✓ | Практика staging/реестр/n8n, без generic AI |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | ПДн/реквизиты не в облако; credentials vault; полномочия подписанта |
| Ept02 | ✓ | 2 internal published: debitorka + sverka-bank-1c (оба HTTP 200) |
| — | ✗ | R03 Wordstat unavailable → −2 к lite (итого 18/20) |

## Script reports

| Скрипт | Verdict | Файл |
|--------|---------|------|
| fact-check | PASS | fact-check-report.json |
| link-verify | PASS | link-verify.json |
| html-linter | PASS | html-linter-report.json |
| slop-detector | PASS | slop-detector-report.json |
| cannibalization | PASS | cannibalization-report.json |
| utility gate | PASS | utility-gate-report.json |

## Link verify

- total: 4, failed: 0, verdict: pass
- OK internal: `/blog/upravlenie-debitorkoj-reestr-napominaniya/` (200), `/blog/sverka-bank-1c-bez-pdn/` (200)
- OK external: `t.me/finance_modern`, `club.koda-fd.ru`
- `--site-base https://koda-fd.ru`

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 0
- Flesch RU: 70.2 (Easy)
- verdict: PASS

## Fact-check

- verdict: pass (8 extracted; 3 verified in fact-bank; 5 unverified — примеры K-0142/185400/12300, форма 0510477, ст.203; ключевые из research-notes, не blocker)

## Cannibalization

- verdict: pass (0 issues среди 26 статей)

## Utility gate

- article: PASS (`action_markers=15`, numbered_list_items=16, faq_h3=7, tables=1, blockquotes=2, water_hits=[])

## Fix cycle

- none (HTML/meta правки не требуются)

## Forbidden checks

- em dash (—): 0
- ёлочки («»): 0
- salebot: 0
- MCP URLs in production: 0

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: yes (реестр + статусы + n8n) | Review: no | E-E-A-T SameAs Author: pending (author_id: olga-kondratskaya)
