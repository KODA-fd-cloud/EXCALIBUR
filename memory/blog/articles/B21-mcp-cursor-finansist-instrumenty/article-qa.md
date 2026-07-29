# QA: B21 mcp-cursor-finansist-instrumenty

date: 2026-07-22
score_total: 92/100
core_eeat_lite: 19/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 18 | title_seo 56, desc_seo ок; H2 how_to; FAQ 6; primary в лиде; −2 `title`/`h1` 77 > 65 |
| GEO / citability | 25 | 24 | Answer-first lead, таблица стека, схема →, ol×3, pre×2, 6 FAQ; без TOC/TL;DR/Fact Check |
| CORE-EEAT lite | 15 | 14 | 19/20 (см. ниже); −1 Wordstat MCP-KV offline |
| Human voice | 15 | 15 | 0 slop hits, Flesch RU 92.8, режим B Ольга, «Сделайте/Не делайте» |
| Fact safety | 15 | 14 | fact-check PASS; тарифы/Privacy через research-notes + cursor.com/pricing (дата 22.07.2026) |
| Contract HTML | 10 | 7 | linter PASS, объём 9453 ✓, CTA club+TG ≤2 ✓; −3 нет `<img>` (cover отдельно) |

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
| char_count | 9453 (8500–9500) ✓ |
| CTA | club.koda-fd.ru ×1 + t.me/finance_modern ×1 |

## CORE-EEAT lite: 19/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | Title/meta + lead закрывают MCP Cursor для финансиста |
| C02 | ✓ | Первый абзац — direct answer, без «в этой статье» |
| C03 | ✓ | Аудитория: финансист, папка CSV-выгрузок, без дев-сервера day-1 |
| C04 | ✓ | MCP = Model Context Protocol / «розетки» tools (~50 слов) |
| O01 | ✓ | H2: слова → стек → установка → сценарий → риски → дальше + FAQ |
| O02 | ✓ | Outline читается без body |
| O03 | ✓ | FAQ 6 пар из faq_hints research |
| O04 | ✓ | ol (17 li), ul (1), table (1), blockquote (2), pre×2 |
| R01 | ✓ | ≥3 citability-блока (определение MCP, вердикт/схема, DoD пилота) |
| R02 | ✓ | Cursor Tools & MCP / mcp.json + pricing URL с датой в research-notes |
| R03 | ✓ | Нет фейкового Wordstat/процентов; цены с оговоркой даты |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: filesystem MCP + отчёт по data/ (не клон «топ MCP-серверов») |
| E02 | ✓ | «Сделайте / Не делайте» в каждой H2-секции |
| E03 | ✓ | CTA: Telegram finance_modern + клуб KODA (без salebot) |
| Exp01 | ✓ | Режим B, author_id olga-kondratskaya; «в моей практике» без fake кейса |
| Exp02 | ✓ | Тон practice/DoD, мост к B20 без дубля pandas/Streamlit |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | Path/env/gitignore/Privacy Mode/ПДн; не Auto-run day-1 |
| Ept02 | ✓ | Internal: cursor-finansist-skript-dashbord, cursor-ai-agenty, obezlichivanie |
| — | ✗ | R03/Wordstat infra: MCP-KV offline — цифры спроса не выдуманы (−1 lite → 19/20) |

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
- OK: `/blog/cursor-finansist-skript-dashbord/`, `/blog/cursor-ai-agenty-finotchetnost/`, `/blog/obezlichivanie-dannyh-chatgpt-finansist/`, t.me/finance_modern, club.koda-fd.ru
- `--site-base https://koda-fd.ru`
- note: сертификат koda-fd.ru/club — verify failed на default context; HTTP 200 подтверждён с `ssl._create_unverified_context` (`ssl_note` в JSON)

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 4 (таблица+промпт — допустимо)
- Flesch RU: 92.8 (Very Easy)
- verdict PASS

## Fact-check

- verdict: pass (1 extracted; 1 verified in fact-bank — «40 минут»)
- тарифы Hobby/Pro / Privacy Mode не в extracted stats, сверены с research-notes (не blocker)

## Cannibalization

- verdict: pass (0 issues; loaded 15 metas)
- note: primary_query дифференцирован от B03 (`mcp cursor финансист` vs `cursor mcp`); secondary без токенового дубля B03

## Utility gate

- article: PASS (`action_markers=18`, numbered steps=17, faq_h3=6)

## Fix cycle

- cycle 0: HTML без правок; meta primary/secondary уточнены против B03 overlap

## Optional (не blocker)

- обновить SSL-сертификат koda-fd.ru (инфра)
- укоротить meta `title`/`h1` до 50–65 (сейчас 77; SEO-рабочий — `title_seo` 56)
- подключить MCP-KV Wordstat перед следующей семантикой
- `<img>` placeholder UI — по желанию перед Дзен (cover отдельно)
- 7-й FAQ опционален (research hints = 6; utility уже PASS)

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (6) | HowTo: yes (установка MCP → сценарий data/ → риски) | Review: no | E-E-A-T SameAs Author: pending (author_id: olga-kondratskaya)
