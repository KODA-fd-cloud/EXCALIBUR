# QA: B56 abc-analiz-debitorki-excel

date: 2026-08-08
score_total: 90/100
core_eeat_lite: 19/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 18 | title/h1 67 > 65; primary в лиде; FAQ 7; H2 how-to |
| GEO / citability | 25 | 24 | Answer-first lead, таблица колонок, blockquote workflow, ol×2, формулы Excel/Sheets |
| CORE-EEAT lite | 15 | 14 | 19/20 (см. ниже); −1 Wordstat MCP-KV offline |
| Human voice | 15 | 15 | 0 slop hits, Flesch RU 68.6, режим B Ольга, «Сделайте/Не делайте» ×5 |
| Fact safety | 15 | 14 | fact-check PASS; 5 unverified = примеры (485000, K-0142, ст. 196), не маркетинг |
| Contract HTML | 10 | 7 | linter PASS, объём 8945 ✓, CTA club+TG ✓; −3 нет `<img>` (cover отдельно) |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate pass — **выполнен**.

## Hard bans (KODA)

| Проверка | Результат |
|----------|-----------|
| TL;DR | нет |
| Fact Check блок | нет |
| «—» (emdash U+2014) | 0 |
| «мы в KODA» | нет |
| salebot / koda_salebot | нет |
| article_mode | B |
| char_count | 8945 |
| CTA | club.koda-fd.ru ×2 + t.me/finance_modern ×2 + koda-fd.ru ×1 |

## CORE-EEAT lite: 19/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | Title/meta + lead: ABC дебиторки в Excel/Sheets + очередь звонков |
| C02 | ✓ | Первый абзац — direct answer (40 должников, ABC за час, aging) |
| C03 | ✓ | Аудитория: финотдел/бухгалтер без программиста |
| C04 | ✓ | ABC vs aging; Excel/Sheets vs 1С:ERP; 80/95 vs 70/20/10 |
| O01 | ✓ | H2: когда → данные → формулы → проверка → автоматизация + FAQ |
| O02 | ✓ | Outline читается без body |
| O03 | ✓ | FAQ 7 пар (без программиста, время, Sheets риски, пороги, суммирование, очередь, aging-only) |
| O04 | ✓ | ol (10 li), ul (3), table (1), blockquote (1) |
| R01 | ✓ | ≥3 citability-блока (таблица колонок, workflow blockquote, формулы IF/SUM/MAX) |
| R02 | ✓ | Пороги 80/95, ст. 196 ГК РФ, 20–30 мин — research-notes таблица фактов |
| R03 | ✓ | Нет фейкового Wordstat; примеры K-0142/485000 — иллюстрация |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: ABC дебиторки + aging + очередь звонков (не общий ABC товаров) |
| E02 | ✓ | «Сделайте / Не делайте» в 5 H2-секциях |
| E03 | ✓ | CTA: Telegram finance_modern + клуб KODA (без salebot) |
| Exp01 | ✓ | Режим B, author_id olga-kondratskaya |
| Exp02 | ✓ | Тон practice/DoD, мост к B13/B14/B11 без дубля |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | ПДн: коды вместо ФИО, обезличивание перед ChatGPT |
| Ept02 | ✓ | Internal: avtomatizaciya-finansov-no-code, obezlichivanie-dannyh-chatgpt-finansist |
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
- OK: `/obezlichivanie-dannyh-chatgpt-finansist/`, `/avtomatizaciya-finansov-no-code/`, t.me/finance_modern, club.koda-fd.ru, koda-fd.ru
- `--site-base https://koda-fd.ru`

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 4 (таблица + workflow — допустимо)
- Flesch RU: 68.6 (Easy)
- verdict PASS

## Fact-check

- verdict: pass (7 extracted; 2 verified in fact-bank — «2026», «60 дней»)
- 30 мин / 485000 / K-0142 / ст. 196 — примеры и норма, не blocker

## Cannibalization

- verdict: pass (0 issues; loaded 33 metas)
- note: B56 = приоритизация ABC+aging; B14 = реестр+напоминания; перекрёстные secondary без overlap ≥70%

## Utility gate

- article: PASS (`action_markers=20`, numbered steps=10, faq_h3=7, actionable H2=5)
- article-qa.md: PASS (этот файл)

## Fix cycle

- cycle 0: правки article.html не потребовались; все скрипты PASS с первого прогона

## Optional (не blocker)

- укоротить meta `title`/`h1` до 50–65 (сейчас 67; SEO-рабочий — `title_seo` 58)
- internal links можно нормализовать на `/blog/…` (сейчас 200 без префикса)
- подключить MCP-KV Wordstat перед следующей семантикой

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: yes (ABC таблица → формулы → очередь) | Review: no | E-E-A-T SameAs Author: pending (author_id: olga-kondratskaya)
