# QA: B82 google-sheets-api-integraciya-finotdel

date: 2026-08-19
score_total: 91/100
core_eeat_lite: 19/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 17 | primary в lead; H2 action; FAQ 6; −2 `title_seo` без «финансы» (utility gate warn); −1 длинный `h1` |
| GEO / citability | 25 | 24 | Answer-first lead; таблица маршрутов + ошибок; blockquote workflow; ol×11; pre×1; 6 FAQ citability-first |
| CORE-EEAT lite | 15 | 14 | 19/20; −1 Wordstat MCP offline в research |
| Human voice | 15 | 15 | 0 slop hits; slop WARNING только из-за table-parse (>25 слов); Flesch RU 91.7 |
| Fact safety | 15 | 14 | fact-check PASS; 6 unverified = HTTP-коды 403/429/200, квота 300 write/min, примеры сумм в коде |
| Contract HTML | 10 | 6 | linter PASS, 9188 ✓ (8500–9500), CTA club+TG ≤2; −4 нет `<img>` (cover отдельно) |

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
| char_count | 9188 (8500–9500) ✓ |
| CTA | club.koda-fd.ru ×1 + t.me/finance_modern ×1 |

## CORE-EEAT lite: 19/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | Title/meta + lead: Google Sheets API + service account для финотдела |
| C02 | ✓ | Первый абзац — direct answer (боль + решение), без «в этой статье» |
| C03 | ✓ | Аудитория: финотдел / аналитик, выгрузка из 1С/банка в таблицы |
| C04 | ✓ | API, service account, scopes, IAM — объяснены во 2-м абзаце |
| O01 | ✓ | H2: когда нужно → безопасность → setup → ошибки → дальше + FAQ |
| O02 | ✓ | Outline читается без body |
| O03 | ✓ | FAQ 6 пар (без программиста, сроки, риски, OAuth vs SA, Drive API, vs Apps Script) |
| O04 | ✓ | ol (11 li), table×2, blockquote×2, pre×1 |
| R01 | ✓ | ≥3 citability-блока (таблица маршрутов, workflow-схема, таблица ошибок) |
| R02 | ✓ | 300 write/min, scopes Sensitive/Recommended, 403/429 — research-notes + Google docs |
| R03 | ✓ | Нет фейкового Wordstat; «1–2 часа» / «2–4 часа» — оценка без маркетинговых % |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: staging + service account + Python для финотдела, не клон «Sheets API tutorial» |
| E02 | ✓ | «Сделайте / Не делайте» в 5 H2-секциях |
| E03 | ✓ | CTA: Telegram finance_modern + клуб KODA (без salebot) |
| Exp01 | ✓ | Режим B, author_id olga-kondratskaya; без fake «я внедрил» |
| Exp02 | ✓ | Тон practice/DoD, мост к no-code и обезличиванию |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | ПДн, JSON-ключ, scopes Sensitive, 403/429/locale — честно |
| Ept02 | ✓ | Internal: avtomatizaciya-finansov-no-code, obezlichivanie-dannyh-chatgpt-finansist |
| — | ✗ | Wordstat MCP-KV offline — цифры спроса не выдуманы (−1 lite → 19/20) |

## Script reports

| Скрипт | Verdict | Файл |
|--------|---------|------|
| fact-check | PASS | fact-check-report.json |
| link-verify | PASS | link-verify.json |
| html-linter | PASS | html-linter-report.json |
| slop-detector | WARNING (0 cliches) | slop-detector-report.json |
| cannibalization | PASS (0 issues для B82) | cannibalization-report.json |
| utility gate (article) | PASS | utility-gate-report.json |

## Link verify

- total: 5, failed: 0
- OK: `/blog/avtomatizaciya-finansov-no-code/`, `/blog/obezlichivanie-dannyh-chatgpt-finansist/`, developers.google.com/workspace/sheets/api/limits, t.me/finance_modern, club.koda-fd.ru
- `--site-base https://koda-fd.ru`

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 7 (артефакты парсинга таблиц/blockquote — допустимо)
- Flesch RU: 91.7 (Very Easy)
- verdict: WARNING → **accept for PASS** (0 slop hits)

## Fact-check

- verdict: pass (7 extracted; 1 in fact-bank)
- 403 / 429 / 200 / 300 / 150000 / 320000 — HTTP-коды, квота Google, примеры в коде; не blocker

## Cannibalization

- verdict: pass для B82 (0 issues с участием B82; loaded 40 metas)
- note: глобальный WARNING B21↔B80 (MCP) — не относится к B82; primary_query «google sheets api сервисный аккаунт финансы» не дублирует B51/B36/B25 (другой угол: SA + Python transport)

## Utility gate

- article: PASS (`action_markers=13`, numbered steps=11, faq_h3=6, tables=2)
- warn: `meta_ab.title_seo` без «финансы» — не blocker (title_aeo покрывает)

## Final

verdict: **PASS** — ready for cover || schema
