# QA: B81 kak-iz-google-sheets-podklyuchitsya-k-1s-po-odata-habr-q-a

date: 2026-08-18
score_total: 91/100
core_eeat_lite: 19/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 17 | primary в lead; H2 action; FAQ 6; −2 `title_seo` без «как/подключиться/хабр» (utility gate warn); −1 длинный `h1` |
| GEO / citability | 25 | 24 | Answer-first lead; таблица сценариев + ошибок; blockquote-схема; ol×18; pre×2; 6 FAQ citability-first |
| CORE-EEAT lite | 15 | 14 | 19/20; −1 Wordstat MCP offline в research |
| Human voice | 15 | 15 | 0 slop hits; slop WARNING только из-за table-parse (>25 слов); Flesch RU 100 |
| Fact safety | 15 | 14 | fact-check PASS; 7 unverified = HTTP-коды, Habr ID, квоты Google Apps Script |
| Contract HTML | 10 | 6 | linter PASS, 8699 ✓ (8500–9500), CTA club+TG ≤2; −4 нет `<img>` (cover отдельно) |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate pass — **выполнен**.

## Hard bans (KODA)

| Проверка | Результат |
|----------|-----------|
| TL;DR | нет |
| Fact Check блок | нет |
| «—» (emdash U+2014) | 0 (en-dash «–» в тексте) |
| «мы в KODA» | нет |
| salebot / koda_salebot | нет |
| article_mode | B |
| char_count | 8699 (8500–9500) ✓ |
| CTA | club.koda-fd.ru ×1 + t.me/finance_modern ×1 |

## CORE-EEAT lite: 19/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | Title/meta + lead: Google Sheets → 1С OData через Apps Script (Habr Q&A 891699) |
| C02 | ✓ | Первый абзац — direct answer (боль + решение), без «в этой статье» |
| C03 | ✓ | Аудитория: финотдел / админ 1С, общая облачная таблица |
| C04 | ✓ | OData как REST 3.0, UrlFetchApp, Basic Auth — в первых абзацах |
| O01 | ✓ | H2: когда нужно → безопасность → setup → ошибки → дальше + FAQ |
| O02 | ✓ | Outline читается без body |
| O03 | ✓ | FAQ 6 пар (коннектор, без программиста, браузер vs GAS, сроки, риски, объём) |
| O04 | ✓ | ol (18 li), table×2, blockquote×2, pre×2 |
| R01 | ✓ | ≥3 citability-блока (таблица сценариев, схема setup, таблица ошибок) |
| R02 | ✓ | Habr Q&A 891699, квота Url Fetch 20k/день, runtime 6 мин — research-notes |
| R03 | ✓ | Нет фейкового Wordstat; «2–5 дней» — оценка без маркетинговых % |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: закрытие конкретного Habr Q&A + whitelist IP Google, не клон «OData для Excel» |
| E02 | ✓ | «Сделайте / Не делайте» в 5 H2-секциях |
| E03 | ✓ | CTA: Telegram finance_modern + клуб KODA (без salebot) |
| Exp01 | ✓ | Режим B, author_id olga-kondratskaya; без fake «я внедрил» |
| Exp02 | ✓ | Тон practice/DoD, мост к no-code и обезличиванию |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | HTTPS, ПДн, PropertiesService, LAN/SSL/firewall ограничения |
| Ept02 | ✓ | Internal: avtomatizaciya-finansov-no-code, obezlichivanie-dannyh-chatgpt-finansist, vygruzka-1c-excel-odata |
| — | ✗ | Wordstat MCP-KV offline — цифры спроса не выдуманы (−1 lite → 19/20) |

## Script reports

| Скрипт | Verdict | Файл |
|--------|---------|------|
| fact-check | PASS | fact-check-report.json |
| link-verify | PASS | link-verify.json |
| html-linter | PASS | html-linter-report.json |
| slop-detector | WARNING (0 cliches) | slop-detector-report.json |
| cannibalization | PASS | cannibalization-report.json |
| utility gate (article) | PASS | utility-gate-report.json |

## Link verify

- total: 6, failed: 0
- OK: qna.habr.com/q/891699, `/blog/avtomatizaciya-finansov-no-code/`, `/blog/obezlichivanie-dannyh-chatgpt-finansist/`, `/blog/vygruzka-1c-excel-odata/`, t.me/finance_modern, club.koda-fd.ru
- `--site-base https://koda-fd.ru`

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 6 (артефакты парсинга таблиц/blockquote — допустимо, как B18/B22)
- Flesch RU: 100.0 (Very Easy)
- verdict: WARNING → **accept for PASS** (0 slop hits)

## Fact-check

- verdict: pass (7 extracted; 0 in fact-bank)
- 6 мин / 20 000 / 401 / 404 / 891699 / 2–5 дней — лимиты Google, HTTP-коды, ID Q&A; не blocker

## Cannibalization

- verdict: pass (0 issues; loaded 38 metas)
- note: primary_query Habr Q&A не дублирует B13 (Excel OData) и B22 (GAS общий); угол Sheets+OData+Basic Auth

## Utility gate

- article: PASS (`action_markers=15`, numbered steps=18, faq_h3=6, tables=2)
- warn: `meta_ab.title_seo` без «как/подключиться/хабр» — не blocker (title_aeo покрывает)

## Final

verdict: **PASS** — ready for cover (schema skipped per user scope)
