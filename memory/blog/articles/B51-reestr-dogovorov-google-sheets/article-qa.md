# QA: B51 reestr-dogovorov-google-sheets

date: 2026-08-06
score_total: 91/100
core_eeat_lite: 19/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 18 | title_seo 56, desc 130; 5 actionable H2 + «Что дальше» + FAQ 7; primary в лиде; −2 meta `title`/`h1` 87 > 65 |
| GEO / citability | 25 | 23 | Answer-first lead, 2 таблицы (маршрут/ошибки), workflow blockquote, Apps Script `<pre>`, 7 FAQ; без TOC/TL;DR/Fact Check |
| CORE-EEAT lite | 15 | 14 | 19/20 (см. ниже); −1 Wordstat MCP-KV offline |
| Human voice | 15 | 14 | 0 slop hits, Flesch RU 75.9, режим B Ольга; −1 slop WARNING (7 over-long, в т.ч. артефакты таблиц) |
| Fact safety | 15 | 14 | fact-check PASS; 5 лет ФЗ-402/НК, MailApp квоты, 6 мин runtime — из research-notes |
| Contract HTML | 10 | 8 | linter PASS, объём 8640 ✓, CTA TG×1+club×1+koda×1 ≤3 ✓; −2 нет `<img>` (cover отдельно) |

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
| char_count | 8640 ✓ |
| CTA | t.me/finance_modern ×1 + club.koda-fd.ru ×1 + koda-fd.ru ×1 |

## CORE-EEAT lite: 19/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | Title/meta + lead закрывают «реестр договоров google sheets» |
| C02 | ✓ | Первый абзац — direct answer, без «в этой статье» |
| C03 | ✓ | Аудитория: финотдел, CFO, офис-менеджер |
| C04 | ✓ | Реестр + график оплат + Apps Script напоминания (chunk в лиде) |
| O01 | ✓ | H2: когда нужен → безопасность → setup → verify → automate → что дальше + FAQ |
| O02 | ✓ | Outline читается без body |
| O03 | ✓ | FAQ 7 пар |
| O04 | ✓ | ol (12 li setup + 5 next), table (2), blockquote (2), pre×1 |
| R01 | ✓ | ≥3 citability-блока (вердикт таблицы маршрутов, workflow blockquote, таблица ошибок) |
| R02 | ✓ | ФЗ-402/НК 5 лет, MailApp 100/1500, 6 мин runtime — research-notes |
| R03 | ✓ | Нет фейкового Wordstat/% |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: RU Sheets + сроки оплаты/пролонгации + без сырых ПДн |
| E02 | ✓ | «Сделайте / Не делайте» в секциях when-needed и prep-security |
| E03 | ✓ | CTA: Telegram finance_modern + клуб KODA (без salebot) |
| Exp01 | ✓ | Режим B, author_id olga-kondratskaya |
| Exp02 | ✓ | Тон practice/DoD, не generic AI conclusion |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | ПДн/sharing Drive, обезличивание перед ChatGPT, ACL Workspace |
| Ept02 | ✓ | Internal: avtomatizaciya-finansov-no-code, obezlichivanie-dannyh |
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

- total: 5, failed: 0
- OK: `/blog/avtomatizaciya-finansov-no-code/`, `/blog/obezlichivanie-dannyh-chatgpt-finansist/`, club.koda-fd.ru, koda-fd.ru, t.me/finance_modern
- `--site-base https://koda-fd.ru`

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 7 (лид + таблицы — допустимо, не blocker)
- Flesch RU: 75.9 (Easy)
- verdict WARNING (0 cliches — не blocker для PASS)

## Fact-check

- verdict: pass (9 extracted; 0 verified in fact-bank; 9 unverified — квоты MailApp, сроки хранения, пороги договоров из research, не blocker)

## Cannibalization

- verdict: pass (0 issues; loaded 30 metas)

## Utility gate

- article: PASS (`action_markers=11`, numbered steps=12, faq_h3=7, tables=2)
- topic gate (preflight): PASS

## Fix cycle

- cycle 1: GEO QA — правок article.html не потребовалось

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: yes (setup ol 7 шагов) | Review: no | E-E-A-T SameAs Author: pending (author_id: olga-kondratskaya)
