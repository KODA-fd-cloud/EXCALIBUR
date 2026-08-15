# QA: B59 zayavka-na-rashod-google-forms

date: 2026-08-15
score_total: 90/100
core_eeat_lite: 19/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 18 | title_seo 56, desc 156; 5 actionable H2 + «Что дальше» + FAQ 6; primary в лиде |
| GEO / citability | 25 | 23 | Answer-first lead, 2 таблицы (маршрут/ошибки), workflow blockquote, Apps Script `<pre>`, 6 FAQ; без TOC/TL;DR/Fact Check |
| CORE-EEAT lite | 15 | 14 | 19/20 (см. ниже); −1 Wordstat MCP-KV offline |
| Human voice | 15 | 14 | 0 slop hits, Flesch RU 66.9, режим B Ольга; −1 slop WARNING (7 over-long, в т.ч. артефакты таблиц) |
| Fact safety | 15 | 14 | fact-check PASS; лимит 100k ответов Forms, Make 15 мин, 5–10 мин CRM — research-notes |
| Contract HTML | 10 | 8 | linter PASS, объём 8765 ✓, CTA club×1+TG×1 ≤3 ✓; −2 нет `<img>` (cover отдельно) |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate pass — **выполнен**.

## Hard bans (KODA)

| Проверка | Результат |
|----------|-----------|
| TL;DR blockquote | нет |
| Fact Check блок | нет |
| «—» (emdash U+2014) | 0 |
| ««» / »» | 0 |
| «мы в KODA» | нет |
| salebot / koda_salebot | нет |
| article_mode | B |
| char_count | 8765 ✓ |
| hook | 498 ✓ (350–500) |
| CTA | club.koda-fd.ru ×1 + t.me/finance_modern ×1 |

## CORE-EEAT lite: 19/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | Title/meta + lead закрывают «заявка на расход google forms» |
| C02 | ✓ | Первый абзац — direct answer, без «в этой статье» |
| C03 | ✓ | Аудитория: финотдел, CFO, офис-менеджер |
| C04 | ✓ | Управленческая заявка vs кассовый расход / 1С — во 2-м абзаце |
| O01 | ✓ | H2: when → security → setup → verify → scale → next + FAQ |
| O02 | ✓ | Outline actionable без body |
| O03 | ✓ | FAQ 6 пар |
| O04 | ✓ | ol (7 setup + 5 next), table (2), blockquote (2), pre×1 |
| R01 | ✓ | Вердикт таблицы маршрутов, workflow blockquote, таблица ошибок |
| R02 | ✓ | 100k лимит Forms, onFormSubmit, Make 15 мин — research-notes |
| R03 | ✓ | Нет фейкового Wordstat/% |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: RU workflow «форма → реестр → согласование → оплата», не бланк Excel |
| E02 | ✓ | «Сделайте / Не делайте» в when-fit и prep-security |
| E03 | ✓ | CTA: Telegram finance_modern + клуб KODA (без salebot) |
| Exp01 | ✓ | Режим B, author_id olga-kondratskaya |
| Exp02 | ✓ | Тон practice/DoD, финансовые аналогии |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | ПДн/sharing Drive, 152-ФЗ, обезличивание перед ChatGPT |
| Ept02 | ✓ | Internal: avtomatizaciya-finansov-no-code, obezlichivanie-dannyh, reestr-dogovorov, apps-script |
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
- OK: `/blog/avtomatizaciya-finansov-no-code/`, `/blog/reestr-dogovorov-google-sheets/`, `/blog/obezlichivanie-dannyh-chatgpt-finansist/`, `/blog/google-apps-script-finansist-obnovit-dannye/`, club.koda-fd.ru, t.me/finance_modern
- `--site-base https://koda-fd.ru`

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 7 (лид + таблицы — допустимо, не blocker)
- Flesch RU: 66.9 (Easy)
- verdict WARNING (0 cliches — не blocker для PASS)

## Fact-check

- verdict: pass (4 extracted; 2 verified in fact-bank; 2 unverified — 100k лимит Forms, порог 80–100 заявок/мес из research, не blocker)

## Cannibalization

- verdict: pass (0 issues)

## Utility gate

- article: PASS (`action_markers=14`, numbered steps=12, faq_h3=6, tables=2)
- topic gate (preflight): PASS

## Fix cycle

- cycle 1: GEO QA — правок article.html не потребовалось

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (6) | HowTo: yes (setup ol 7 шагов) | Review: no | E-E-A-T SameAs Author: pending (author_id: olga-kondratskaya)
