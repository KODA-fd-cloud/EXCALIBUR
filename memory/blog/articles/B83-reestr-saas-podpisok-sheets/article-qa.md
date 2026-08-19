# QA: B83 reestr-saas-podpisok-sheets

date: 2026-08-19
score_total: 90/100
core_eeat_lite: 19/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 18 | title_seo 48, desc_seo 130; 6 actionable H2 + «Что дальше» + FAQ 7; primary в лиде; −2 meta `title`/`h1` 62 > 65 |
| GEO / citability | 25 | 23 | Answer-first lead, 2 таблицы (маршрут/ошибки), workflow blockquote, формулы в ol, 7 FAQ; без TOC/TL;DR/Fact Check |
| CORE-EEAT lite | 15 | 14 | 19/20 (см. ниже); −1 Wordstat MCP-KV offline |
| Human voice | 15 | 13 | 0 slop hits, Flesch RU 60.9, режим B Ольга; −2 slop WARNING (11 over-long, в т.ч. таблицы) |
| Fact safety | 15 | 14 | fact-check PASS; Zylo/Vertice 2026, 60 д — fact-bank; остальные пороги из research-notes |
| Contract HTML | 10 | 8 | linter PASS, объём 9299 ✓, CTA TG×1+club×1+koda×1 ≤3 ✓; −2 нет `<img>` (cover отдельно) |

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
| char_count | 9299 ✓ |
| CTA | t.me/finance_modern ×1 + club.koda-fd.ru ×1 + koda-fd.ru ×1 |

## CORE-EEAT lite: 19/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | Title/meta + lead закрывают «реестр saas подписок компания» |
| C02 | ✓ | Первый абзац — direct answer, без «в этой статье» |
| C03 | ✓ | Аудитория: финотдел, CFO, office manager |
| C04 | ✓ | Реестр + выписка 3 мес + мёртвые seats + CF/алерты (chunk в лиде) |
| O01 | ✓ | H2: when-needed → prep-security → setup → verify → automate → что дальше + FAQ |
| O02 | ✓ | Outline читается без body |
| O03 | ✓ | FAQ 7 пар |
| O04 | ✓ | ol (7 setup + 5 next), table (2), blockquote (2) |
| R01 | ✓ | ≥3 citability-блока (вердикт таблицы маршрутов, workflow blockquote, таблица ошибок) |
| R02 | ✓ | Zylo/Vertice 2026, MailApp 6 мин, 15–20% seats — research-notes |
| R03 | ✓ | Нет фейкового Wordstat/% |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: RU Sheets + выписка + FinOps без SMP на старте |
| E02 | ✓ | «Сделайте / Не делайте» в when-needed и prep-security |
| E03 | ✓ | CTA: Telegram finance_modern + клуб KODA (без salebot) |
| Exp01 | ✓ | Режим B, author_id olga-kondratskaya |
| Exp02 | ✓ | Тон practice/DoD, не generic AI conclusion |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | ПДн/sharing Drive, обезличивание перед ChatGPT, 152-ФЗ |
| Ept02 | ✓ | Internal: avtomatizaciya-finansov-no-code, obezlichivanie-dannyh, reestr-dogovorov |
| — | ✗ | Wordstat infra: MCP-KV offline (−1 lite → 19/20) |

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
- OK: `/blog/avtomatizaciya-finansov-no-code/`, `/blog/obezlichivanie-dannyh-chatgpt-finansist/`, `/blog/reestr-dogovorov-google-sheets/`, club.koda-fd.ru, koda-fd.ru, t.me/finance_modern
- `--site-base https://koda-fd.ru`

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 11 (лид + таблицы — допустимо, не blocker)
- Flesch RU: 60.9 (Easy)
- verdict WARNING (0 cliches — не blocker для PASS)

## Fact-check

- verdict: pass (9 extracted; 2 verified in fact-bank; 7 unverified — пороги CF, сроки, квоты MailApp из research, не blocker)

## Cannibalization

- verdict: pass для B83 (0 issues с участием B83; global scan 41 meta, 1 warning B21↔B80 — unrelated)

## Utility gate

- article: PASS (`action_markers=14`, numbered steps=12, faq_h3=7, tables=2)
- topic gate (preflight): PASS

## Fix cycle

- cycle 1: GEO QA — правок article.html не потребовалось

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: yes (setup ol 7 шагов) | Review: no | E-E-A-T SameAs Author: pending (author_id: olga-kondratskaya)
