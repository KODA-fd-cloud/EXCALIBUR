# QA: B23 cursor-rules-finotdel

date: 2026-07-30
score_total: 93/100
core_eeat_lite: 19/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 18 | primary в title_seo (53); H2 action; FAQ 7; −2 `title`/`h1` 86 > 65 |
| GEO / citability | 25 | 24 | таблица tools, workflow →, pre×3 (AGENTS + 2 mdc), чеклист «сегодня», FAQ action-first |
| CORE-EEAT lite | 15 | 14 | 19/20; −1 Wordstat MCP-KV offline |
| Human voice | 15 | 15 | 0 slop, режим B, «Сделайте/Не делайте» |
| Fact safety | 15 | 15 | fact-check PASS; cursor.com/docs/rules; без выдуманных %/цен |
| Contract HTML | 10 | 7 | linter PASS, char 8909 ✓, CTA 2; −3 cover/`<img>` отдельно |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate pass — **выполнен**.

## Hard bans (KODA)

| Проверка | Результат |
|----------|-----------|
| TL;DR | нет |
| Fact Check блок | нет |
| «—» (emdash U+2014) | 0 (только en-dash «–») |
| «мы в KODA» | нет |
| salebot / koda_salebot | нет |
| article_mode | B |
| char_count | 8909 (8500–9500) ✓ |
| CTA | club.koda-fd.ru ×1 + t.me/finance_modern ×1 |
| TOC якорный | нет (linter PASS) |

## CORE-EEAT lite: 19/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | H1/title + title_seo закрывают «как настроить cursor rules» |
| C02 | ✓ | Lead: боль (чат/raw) + ответ (rules) + результат вечера; без «в этой статье» |
| C03 | ✓ | Аудитория: финотдел, CSV/1С, не React/BSL |
| C04 | ✓ | Rules = устав в файлах; MCP = «курьер с ключом» |
| O01 | ✓ | H2: why → format → folders → create → kb/MCP → team → today + FAQ |
| O02 | ✓ | Outline читается без body |
| O03 | ✓ | FAQ 7 пар из research faq_hints |
| O04 | ✓ | ol×3 (24 li), ul×2, table×1, blockquote×3, pre×3 |
| R01 | ✓ | ≥3 citability: вердикт таблицы, workflow папок, шаблоны mdc |
| R02 | ✓ | docs Cursor (режимы/500 строк) + Hexlet/миграция в research |
| R03 | ✓ | Нет фейкового Wordstat/процентов/цен в HTML |
| R04 | ✓ | FAQ: ответ-действие в первом предложении |
| E01 | ✓ | Угол: финотдел + data/raw + запрет 1С/ПДн (не клон Hexlet/React) |
| E02 | ✓ | «Сделайте / Не делайте» в каждой H2-секции |
| E03 | ✓ | CTA ≤2: Telegram + клуб KODA |
| Exp01 | ✓ | Режим B, author_id olga-kondratskaya; без fake «я сделал» |
| Exp02 | ✓ | Тон практики/DoD; мост B16/B20/B21/B11 без дубля |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | Rules могут игнорироваться → .gitignore + ревью diff |
| Ept02 | ✓ | Internal: baza-znaniy, cursor-skript, mcp, obezlichivanie |
| — | ✗ | Wordstat infra: MCP-KV offline — цифры спроса не выдуманы (−1 → 19/20) |

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

- total: 7, failed: 0
- OK: cursor.com/docs/rules; `/blog/baza-znaniy-chatgpt-cursor-finotdel/`; `/blog/cursor-finansist-skript-dashbord/`; `/blog/obezlichivanie-dannyh-chatgpt-finansist/`; `/blog/mcp-cursor-finansist-instrumenty/`; t.me/finance_modern; club.koda-fd.ru
- `--site-base https://koda-fd.ru`

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 2 (допустимо: interlink + таблица)
- Flesch RU: 100.0 (Very Easy)
- verdict PASS

## Fact-check

- verdict: pass (2 extracted; 2 verified — «2026», «500»)
- утверждения про режимы rules / AGENTS.md / Tab+Inline сверены с research-notes + cursor.com/docs/rules

## Cannibalization

- verdict: pass (0 issues; loaded 19 metas)
- primary_query `как настроить cursor rules` не дублирует соседние B16/B20/B21

## Utility gate

- article: PASS (`action_markers=23`, numbered steps=24, faq_h3=7, tables=1, blockquotes=3)

## Fix cycle

- cycle 0: HTML без правок QA; все скрипты PASS с первой прогонки 2026-07-30

## Optional (не blocker)

- укоротить meta `title`/`h1` до 50–65 (сейчас 86; SEO-рабочий — `title_seo` 53)
- подключить MCP-KV Wordstat перед следующей семантикой
- `<img>` placeholder — cover отдельно после PASS

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: yes (папки → AGENTS/mdc → Active Rules → тест raw) | Review: no | E-E-A-T SameAs Author: pending (author_id: olga-kondratskaya)
