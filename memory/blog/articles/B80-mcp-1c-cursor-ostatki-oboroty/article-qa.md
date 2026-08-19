# QA: B80 mcp-1c-cursor-ostatki-oboroty

date: 2026-08-19
score_total: 93/100
core_eeat_lite: 19/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 19 | title_seo 49, desc 138; H2 how_to; FAQ 6; primary в лиде; −1 title/h1 65 (верхняя граница) |
| GEO / citability | 25 | 24 | Answer-first lead, таблица OData vs HTTP, workflow blockquote, ol×23, pre×2, 6 FAQ; без TOC/TL;DR/Fact Check |
| CORE-EEAT lite | 15 | 14 | 19/20 (см. ниже); −1 Wordstat MCP-KV offline в research |
| Human voice | 15 | 15 | 0 slop hits, Flesch RU 82.9, режим B Ольга, «Сделайте/Не делайте» |
| Fact safety | 15 | 14 | fact-check PASS; INFATON/1c-odata факты через research-notes URLs |
| Contract HTML | 10 | 7 | linter PASS, объём 9181 ✓, CTA club+TG ≤2 ✓; −3 нет `<img>` (cover отдельно) |

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
| char_count | 9181 (8500–9500) ✓; meta 9175 |
| CTA | club.koda-fd.ru ×1 + t.me/finance_modern ×1 |

## CORE-EEAT lite: 19/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | Title/meta + lead закрывают MCP 1С Cursor остатки/обороты |
| C02 | ✓ | Первый абзац — direct answer, без «в этой статье» |
| C03 | ✓ | Аудитория: финотдел/CFO, повторяющиеся запросы к остаткам без XLS |
| C04 | ✓ | MCP = Model Context Protocol / «розетка» tools (~50 слов) |
| O01 | ✓ | H2: when → security → setup (2 трека) → verify → next + FAQ |
| O02 | ✓ | Outline читается без body |
| O03 | ✓ | FAQ 6 пар из faq_hints research |
| O04 | ✓ | ol (23 li), ul (1), table (1), blockquote (2), pre×2 |
| R01 | ✓ | ≥3 citability-блока (определение MCP, вердикт/схема, DoD сверки) |
| R02 | ✓ | get_balance, 1c-odata-mcp, Cursor mcp.json — URLs в research-notes |
| R03 | ✓ | Нет фейкового Wordstat/процентов; Wordstat offline задокументирован |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: живая 1С vs B21 CSV; OData vs HTTP get_balance (не dev BSL) |
| E02 | ✓ | «Сделайте / Не делайте» в каждой H2-секции |
| E03 | ✓ | CTA: Telegram finance_modern + клуб KODA (без salebot) |
| Exp01 | ✓ | Режим B, author_id olga-kondratskaya; «публикую» без fake кейса |
| Exp02 | ✓ | Тон practice/DoD, мосты B21/B13 без дубля filesystem |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | 152-ФЗ, read-only, env, Privacy Mode; не Auto-run day-1 |
| Ept02 | ✓ | Internal: mcp-cursor-finansist-instrumenty, vygruzka-1c-excel-odata, obezlichivanie, avtomatizaciya-no-code |
| — | ✗ | R03/Wordstat infra: MCP-KV offline — цифры спроса не выдуманы (−1 lite → 19/20) |

## Script reports

| Скрипт | Verdict | Файл |
|--------|---------|------|
| fact-check | PASS | fact-check-report.json |
| link-verify | PASS | link-verify.json |
| html-linter | PASS | html-linter-report.json |
| slop-detector | PASS | slop-detector-report.json |
| cannibalization | PASS (warning) | cannibalization-report.json |
| utility gate (article) | PASS | utility-gate-report.json |

## Link verify

- total: 6, failed: 0
- OK: `/blog/mcp-cursor-finansist-instrumenty/`, `/blog/vygruzka-1c-excel-odata/`, `/blog/obezlichivanie-dannyh-chatgpt-finansist/`, `/blog/avtomatizaciya-finansov-no-code/`, t.me/finance_modern, club.koda-fd.ru
- `--site-base https://koda-fd.ru`

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 4 (таблица/схема — допустимо)
- Flesch RU: 82.9 (Very Easy)
- verdict PASS

## Fact-check

- verdict: pass (1 extracted; 1 verified in fact-bank — «2026»)
- INFATON/OData/feenlace claims опираются на research-notes fact table (не blocker)

## Cannibalization

- verdict: warning (0 fail; 1 warn)
- note: 75% primary overlap с B21 (`mcp cursor финансист` vs `mcp 1с cursor финансы`); дифференциация по углу «остатки/обороты + 1С live base» — не blocker

## Utility gate

- article: PASS (`action_markers=20`, numbered steps=23, faq_h3=8 incl. setup H3)

## Fix cycle

- cycle 0: HTML без правок; все hard gates PASS с первого прогона

## Optional (не blocker)

- подключить MCP-KV Wordstat перед следующей семантикой
- синхронизировать meta char_count 9175 → 9181
- `<img>` placeholder UI — cover отдельно

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (6) | HowTo: yes (OData/HTTP setup → verify) | Review: no | E-E-A-T SameAs Author: pending (author_id: olga-kondratskaya)
