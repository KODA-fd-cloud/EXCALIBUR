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
| SEO structure | 20 | 18 | title_seo 45; FAQ 7; H2 action; primary в H1/title; −2 `title`/`h1` 86 > 65 |
| GEO / citability | 25 | 24 | таблица инструментов, pre×3 (AGENTS+2.mdc), схемы →, ol шаги, FAQ 7 |
| CORE-EEAT lite | 15 | 14 | 19/20 (см. ниже); −1 Wordstat MCP-KV offline |
| Human voice | 15 | 15 | 0 slop hits, Flesch RU 100, режим B, «Сделайте/Не делайте» |
| Fact safety | 15 | 15 | fact-check PASS; 500 строк / форматы 2026 из docs; «45 мин» из research |
| Contract HTML | 10 | 7 | linter PASS, 9338 ✓, CTA club+TG ≤2 ✓; −3 нет `<img>` (cover отдельно) |

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
| char_count | 9338 (8500–9500) ✓ |
| CTA | club.koda-fd.ru ×1 + t.me/finance_modern ×1 |

## CORE-EEAT lite: 19/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | H1/title закрывают primary «как настроить cursor rules» + финотдел/1С |
| C02 | ✓ | Лид — direct answer (устав в файлах, 30–45 мин), без «в этой статье» |
| C03 | ✓ | Аудитория: финотдел, CSV/1С, папки data/out, не web-dev rules |
| C04 | ✓ | Rules = инструкции в начале контекста агента (~регламент закрытия) |
| O01 | ✓ | H2 ≈ action_outline research (зачем → формат → минимум → файлы → тест → kb/MCP → команда → сегодня) |
| O02 | ✓ | Outline читается без body |
| O03 | ✓ | FAQ 7 пар (тариф, User vs Project, соло, объём, нарушение, .cursorrules, MCP) |
| O04 | ✓ | ol×4, ul×2, table×1, blockquote×3, pre×3 |
| R01 | ✓ | ≥3 citability: определение Rules, вердикт минимум, схема kb→MCP |
| R02 | ✓ | Канон cursor.com/docs/rules.md + help; 500 строк; слои 2026 в research-notes |
| R03 | ✓ | Нет фейкового Wordstat/цен; «45 мин» = reader_outcome research |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: финотдел + запрет сырых 1С/ПДн (не клон Hexlet/mayai) |
| E02 | ✓ | «Сделайте / Не делайте» в каждой H2-секции |
| E03 | ✓ | CTA: Telegram finance_modern + клуб KODA (без salebot) |
| Exp01 | ✓ | Режим B, author_id olga-kondratskaya; без fake кейса |
| Exp02 | ✓ | Тон practice/DoD; мост B16/B20/B11/B21 без дубля |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | Модель может игнорировать rules; дубль .gitignore / confirm tools |
| Ept02 | ✓ | Internal: baza-znaniy, skript-dashbord, obezlichivanie, mcp-cursor |
| — | ✗ | Wordstat infra: MCP-KV offline — показы не выдуманы (−1 lite → 19/20) |

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

- total: 6, failed: 0
- OK: `/blog/baza-znaniy-chatgpt-cursor-finotdel/`, `/blog/cursor-finansist-skript-dashbord/`, `/blog/obezlichivanie-dannyh-chatgpt-finansist/`, `/blog/mcp-cursor-finansist-instrumenty/`, t.me/finance_modern, club.koda-fd.ru
- `--site-base https://koda-fd.ru`

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 1 (мост к B16/B20 — допустимо)
- Flesch RU: 100.0 (Very Easy)
- verdict PASS

## Fact-check

- verdict: pass (4 extracted; 2 verified in fact-bank — «2026», «500»)
- unverified non-blocker: «45 минут» (из research reader_outcome), «0000000000» (маска ИНН-примера, не метрика)

## Cannibalization

- verdict: pass (0 issues; loaded 19 metas)
- note: primary «как настроить cursor rules» уникален среди published metas

## Utility gate

- article: PASS (`action_markers=24`, numbered steps=21, faq_h3=7, h2_sections=8)

## Fix cycle

- cycle 0: HTML без правок writer; scripts + self-check PASS с первого прогона

## Optional (не blocker)

- укоротить meta `title`/`h1` до 50–65 (сейчас 86; SEO-рабочий — `title_seo` 45)
- подключить MCP-KV Wordstat перед следующей семантикой
- `<img>` placeholder UI — по желанию перед Дзен (cover отдельно)

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: yes (формат → минимум → файлы → тест → rollout) | Review: no | E-E-A-T SameAs Author: pending (author_id: olga-kondratskaya)
