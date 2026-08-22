# QA: B91 http-servis-1c-chernovik-scheta-json

date: 2026-08-22
score_total: 92/100
core_eeat_lite: 19/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 19 | title_seo 52, desc 138; H2 how_to; FAQ 7; primary в лиде; −1 h1/title 65 символов (верхняя граница) |
| GEO / citability | 25 | 24 | Answer-first lead, таблица HTTP vs OData/MCP, workflow blockquote, ol×13, pre×2, FAQ 7; без TOC/TL;DR/Fact Check |
| CORE-EEAT lite | 15 | 14 | 19/20 (см. ниже); −1 Wordstat MCP-KV offline в research |
| Human voice | 15 | 14 | 0 slop hits, Flesch RU 66.8, режим B Ольга, «Сделайте/Не делайте»; −1 slop WARNING (6 over-long в таблицах/JSON) |
| Fact safety | 15 | 14 | fact-check PASS; примеры JSON/копейки — маскированные иллюстрации, не market-claims |
| Contract HTML | 10 | 7 | linter PASS, объём 8868 ✓, CTA club+TG+koda ✓; −3 нет `<img>` (cover отдельно) |

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
| char_count | 8868 (8500–9500) ✓ |
| CTA | club.koda-fd.ru ×1 + t.me/finance_modern ×1 + koda-fd.ru ×1 |
| TOC с якорями | нет |

## CORE-EEAT lite: 19/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | Title/meta + lead закрывают «http сервис 1с создать счет json» |
| C02 | ✓ | Первый абзац — direct answer, без «в этой статье» |
| C03 | ✓ | Аудитория: finotdel + backend/1С-интегратор, счёт из CRM/сайта |
| C04 | ✓ | Счёт на оплату, HTTP-сервис, JSON, API — ~50 слов во 2-м абзаце |
| O01 | ✓ | H2: when → JSON/security → setup (2 ветки) → verify → next + FAQ |
| O02 | ✓ | Outline читается без body |
| O03 | ✓ | FAQ 7 пар из faq_hints research |
| O04 | ✓ | ol (13 li), table (2), blockquote (2), pre×2 |
| R01 | ✓ | ≥3 citability-блока (схема POST, JSON-контракт, DoD curl→номер→список) |
| R02 | ✓ | bit22 REST, v8.1c.ru HTTP/JSON, itcodik — URLs в research-notes |
| R03 | ✓ | Нет фейкового Wordstat/процентов; Wordstat offline задокументирован |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: fin how-to черновик vs dev-учебники; diff B18 (УНФ+телефон), B80 (MCP read-only) |
| E02 | ✓ | «Сделайте / Не делайте» в каждой H2-секции |
| E03 | ✓ | CTA: Telegram + клуб KODA + koda-fd.ru (без salebot) |
| Exp01 | ✓ | Режим B, author_id olga-kondratskaya; без fake «я внедрил у клиента X» |
| Exp02 | ✓ | Тон practice/DoD, fin-контекст, мосты B18/B80 |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | 152-ФЗ, auth, HTTPS, черновик без проведения, 400/404/401 |
| Ept02 | ✓ | Internal: avtomatizaciya-finansov-no-code, obezlichivanie-dannyh-chatgpt-finansist |
| — | ✗ | Wordstat infra: MCP-KV offline — цифры спроса не выдуманы (−1 lite → 19/20) |

## Script reports

| Скрипт | Verdict | Файл |
|--------|---------|------|
| fact-check | PASS | fact-check-report.json |
| link-verify | PASS | link-verify.json |
| html-linter | PASS | html-linter-report.json |
| slop-detector | WARNING | slop-detector-report.json |
| cannibalization | PASS (warning portfolio) | cannibalization-report.json |
| utility gate (article) | PASS | utility-gate-report.json |

## Link verify

- total: 5, failed: 0
- OK: `/blog/obezlichivanie-dannyh-chatgpt-finansist/`, `/blog/avtomatizaciya-finansov-no-code/`, t.me/finance_modern, club.koda-fd.ru, koda-fd.ru
- `--site-base https://koda-fd.ru`

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 6 (таблица/JSON/curl — допустимо)
- Flesch RU: 66.8 (Easy)
- verdict WARNING (не blocker: 0 cliches)

## Fact-check

- verdict: pass (10 extracted; 2 verified in fact-bank — «2026», «500»)
- JSON-примеры (7700000000, копейки) — иллюстрации контракта, не fact-bank claims

## Cannibalization

- verdict: warning (portfolio; 0 issues для B91)
- note: глобальный warn B80↔B21 (MCP); B91 primary «http сервис 1с создать счет json» не пересекается с B18/B80 по углу

## Utility gate

- article: PASS (`action_markers=15`, numbered steps=13, faq_h3=7, tables=2)

## Fix cycle

- cycle 0: HTML без правок; все hard gates PASS с первого прогона

## Optional (не blocker)

- подключить MCP-KV Wordstat перед следующей семантикой
- `<img>` placeholder — cover отдельно

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: yes (JSON → hs → curl → verify) | Review: no | E-E-A-T SameAs Author: pending (author_id: olga-kondratskaya)
