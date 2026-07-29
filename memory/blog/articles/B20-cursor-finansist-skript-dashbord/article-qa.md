# QA: B20 cursor-finansist-skript-dashbord

date: 2026-07-22
score_total: 92/100
core_eeat_lite: 19/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 18 | title_seo 58, desc 142; H2 по how_to; FAQ 7; primary в лиде; −2 `title`/`h1` meta 77 > 65 |
| GEO / citability | 25 | 24 | Answer-first lead, таблица Cursor vs ChatGPT, схема →, ol-шаги×3, 7 FAQ; без TOC/TL;DR/Fact Check |
| CORE-EEAT lite | 15 | 14 | 19/20 (см. ниже); −1 Wordstat MCP-KV offline |
| Human voice | 15 | 15 | 0 slop hits, Flesch RU 88.4, режим B Ольга, «Сделайте/Не делайте» |
| Fact safety | 15 | 14 | fact-check PASS; тарифы Hobby/Pro $20/Teams $40 из research-notes + cursor.com/pricing |
| Contract HTML | 10 | 7 | linter PASS, объём 9483 ✓, CTA club+TG ≤2 ✓; −3 нет `<img>` (cover отдельно) |

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
| char_count | 9483 (8500–9500) ✓ |
| CTA | club.koda-fd.ru ×1 + t.me/finance_modern ×1 |

## CORE-EEAT lite: 19/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | Title/meta + lead закрывают «cursor ai» / Cursor для финансиста |
| C02 | ✓ | Первый абзац — direct answer, без «в этой статье» |
| C03 | ✓ | Аудитория: финансист, вечерний пилот без заказного dev |
| C04 | ✓ | Cursor = форк VS Code + папка/diff/терминал (chunk ~50 слов) |
| O01 | ✓ | H2: сравнение → папка → сверка → дашборд → итерации → что дальше + FAQ |
| O02 | ✓ | Outline читается без body |
| O03 | ✓ | FAQ 7 пар из faq_hints research |
| O04 | ✓ | ol (21 li), ul (1), table (1), blockquote (3), pre×2 |
| R01 | ✓ | ≥3 citability-блока (определение Cursor, вердикт таблицы, правило Streamlit/HTML) |
| R02 | ✓ | Цены/Privacy Mode + download URL с датой 22.07.2026 в research-notes |
| R03 | ✓ | Нет фейкового Wordstat/процентов; цены с оговоркой даты |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: вечер = mismatches.csv + localhost-дашборд (не клон «установи Cursor») |
| E02 | ✓ | «Сделайте / Не делайте» в каждой H2-секции |
| E03 | ✓ | CTA: Telegram finance_modern + клуб KODA (без salebot) |
| Exp01 | ✓ | Режим B, author_id olga-kondratskaya; «в моей практике» без fake кейса |
| Exp02 | ✓ | Тон practice/DoD, не generic AI conclusion |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | ПДн, Privacy Mode, localhost only, не Community Cloud |
| Ept02 | ✓ | Internal: cursor-ai-agenty, obezlichivanie, vibe-coding, claude-code |
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

- total: 9, failed: 0
- OK: `/blog/cursor-ai-agenty-finotchetnost/`, `/blog/obezlichivanie-dannyh-chatgpt-finansist/`, `/blog/vibe-coding-finansist/`, `/blog/claude-code-finotdel/`, cursor.com/download, cursor.com/pricing, streamlit.io, t.me/finance_modern, club.koda-fd.ru
- `--site-base https://koda-fd.ru`
- note: сертификат koda-fd.ru/club/streamlit — verify failed на default context; HTTP 200 подтверждён с `ssl._create_unverified_context` (`ssl_note` в JSON)

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 3 (таблица+лид — допустимо)
- Flesch RU: 88.4 (Very Easy)
- verdict PASS

## Fact-check

- verdict: pass (1 extracted; 1 verified in fact-bank — year 2026)
- тарифы/Privacy Mode не в extracted stats, но сверены с research-notes (не blocker)

## Cannibalization

- verdict: pass (0 issues; loaded 13 metas)

## Utility gate

- article: PASS (`action_markers=18`, numbered steps=21, faq_h3=7)

## Fix cycle

- cycle 0: правки HTML не потребовались

## Optional (не blocker)

- обновить SSL-сертификат koda-fd.ru (инфра)
- укоротить meta `title`/`h1` до 50–65 (сейчас 77; SEO-рабочий — `title_seo` 58)
- подключить MCP-KV Wordstat перед следующей семантикой
- `<img>` placeholder UI — по желанию перед Дзен (cover отдельно)

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: yes (папка → сверка → дашборд) | Review: no | E-E-A-T SameAs Author: pending (author_id: olga-kondratskaya)
