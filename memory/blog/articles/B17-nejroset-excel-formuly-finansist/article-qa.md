# QA: B17 nejroset-excel-formuly-finansist

date: 2026-07-22
score_total: 92/100
core_eeat_lite: 19/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 18 | title_seo 56, desc 130; H2 по how_to; FAQ 7; primary в лиде; −2 `title`/`h1` meta 87 > 65 |
| GEO / citability | 25 | 24 | Answer-first lead 406, таблица задач, схемы →, 10 промптов, чеклист 8, 7 FAQ; без TOC/TL;DR/Fact Check |
| CORE-EEAT lite | 15 | 14 | 19/20 (см. ниже); −1 Wordstat MCP-KV offline |
| Human voice | 15 | 15 | 0 slop hits, Flesch RU 78.2, режим B Ольга, «Сделайте/Не делайте» |
| Fact safety | 15 | 14 | fact-check PASS; ChatGPT for Excel март 2026 / Copilot / XLOOKUP 2016–2019 из research-notes |
| Contract HTML | 10 | 7 | linter PASS, объём 9493 ✓, CTA TG×2+club×1 ≤3 ✓; −3 нет `<img>` (cover отдельно) |

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
| char_count | 9493 (8500–9500) ✓ |
| CTA | t.me/finance_modern ×2 + club.koda-fd.ru ×1 |

## CORE-EEAT lite: 19/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | Title/meta + lead закрывают «как использовать нейросеть для excel» |
| C02 | ✓ | Первый абзац — direct answer, без «в этой статье» |
| C03 | ✓ | Аудитория: финансист, закрытие месяца, выгрузка 1С |
| C04 | ✓ | Нейросеть = ускоритель формул/сводной/очистки (chunk в лиде) |
| O01 | ✓ | H2: задачи → ChatGPT/Claude → 10 промптов → чеклист → уход → что дальше + FAQ |
| O02 | ✓ | Outline читается без body |
| O03 | ✓ | FAQ 7 пар из research faq_hints |
| O04 | ✓ | ol (28 li), ul (1), table (1), blockquote (4), pre×2 |
| R01 | ✓ | ≥3 citability-блока (вердикт таблицы, схема выбора, правило smoke-теста) |
| R02 | ✓ | ChatGPT for Excel 05.03.2026 + ограничения beta; Copilot verify; XLOOKUP 2016/2019 — research-notes |
| R03 | ✓ | Нет фейкового Wordstat/%; бенчмарк 87,3% не цитирован как «ваша точность» |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: RU-Excel + антигаллюцинация + граница ухода в скрипт |
| E02 | ✓ | «Сделайте / Не делайте» в каждой H2-секции |
| E03 | ✓ | CTA: Telegram finance_modern + клуб KODA (без salebot) |
| Exp01 | ✓ | Режим B, author_id olga-kondratskaya; «Я пользуюсь» без fake кейса |
| Exp02 | ✓ | Тон practice/DoD, не generic AI conclusion |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | ПДн/152-ФЗ, smoke-тест, версия Excel, не грузить сырьё 1С |
| Ept02 | ✓ | Internal: ot-excel-k-fin-konturu-30-dney, vibe-coding-finansist, obezlichivanie-dannyh |
| — | ✗ | Wordstat infra: MCP-KV offline — цифры спроса не выдуманы (−1 lite → 19/20) |

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
- OK: `/blog/ot-excel-k-fin-konturu-30-dney/`, `/blog/vibe-coding-finansist/`, `/blog/obezlichivanie-dannyh-chatgpt-finansist/`, t.me/finance_modern, club.koda-fd.ru
- `--site-base https://koda-fd.ru`
- note: сертификат koda-fd.ru/club — verify failed на default context; HTTP 200 подтверждён с `ssl._create_unverified_context` (`ssl_note` в JSON)

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 4 (лид + таблица — допустимо)
- Flesch RU: 78.2 (Easy)
- verdict PASS

## Fact-check

- verdict: pass (6 extracted; 1 verified in fact-bank — year 2026; 5 unverified — версии Excel/длительности из research, не blocker)

## Cannibalization

- verdict: pass (0 issues; loaded 14 metas)

## Utility gate

- article: PASS (`action_markers=20`, numbered steps=28, faq_h3=7, tables=1)
- article-qa.md: сохранён (verdict PASS) — gate скрипт валидирует article.html; QA-отчёт зафиксирован рядом

## Fix cycle

- cycle 1: GEO QA — CTA club×2→×1 (E03 ≤3); char_count 9493 в диапазоне; meta geo_qa PASS

## Optional (не blocker)

- обновить SSL-сертификат koda-fd.ru (инфра)
- укоротить meta `title`/`h1` до 50–65 (сейчас 87; SEO-рабочий — `title_seo` 56)
- подключить MCP-KV Wordstat перед следующей семантикой
- `<img>` placeholder UI — по желанию перед Дзен (cover отдельно)

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: yes (выбор канала → промпт → smoke-тест → уход) | Review: no | E-E-A-T SameAs Author: pending (author_id: olga-kondratskaya)
