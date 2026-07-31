# QA: B25 bankovskaya-vypiska-staging-google-sheets

date: 2026-07-31
score_total: 92/100
core_eeat_lite: 19/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 18 | title_seo ~58; desc_seo ок; H2 how_to×8; FAQ 7; primary в лиде; −2 `title`/`h1` 68 > 65 |
| GEO / citability | 25 | 24 | Answer-first lead, таблица источников, схема →, ol×3 (18 li), ul×2, pre×1, 7 FAQ; без TOC/TL;DR/Fact Check |
| CORE-EEAT lite | 15 | 14 | 19/20 (см. ниже); −1 Wordstat MCP-KV offline |
| Human voice | 15 | 15 | 0 slop hits, Flesch RU 75.9, режим B Ольга, «Сделайте/Не делайте» в каждой H2 |
| Fact safety | 15 | 14 | fact-check PASS; unverified = примеры (15000/40702) + Windows-1251 + «30 дней» из якоря; нет выдуманных %/Wordstat |
| Contract HTML | 10 | 7 | linter PASS, объём 9271 ✓, CTA club+TG ≤2 ✓; −3 нет `<img>` (cover отдельно) |

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
| char_count | 9271 (8500–9500) ✓ |
| CTA | club.koda-fd.ru ×1 + t.me/finance_modern ×1 |

## CORE-EEAT lite: 19/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | Title/meta + H1 закрывают primary «банковская выписка в excel автоматически» |
| C02 | ✓ | Первый абзац — direct answer (staging-слой), без «в этой статье» |
| C03 | ✓ | Аудитория: финансист, клиент-банк → ДДС, копипаст ломает формулы |
| C04 | ✓ | Staging = промежуточный журнал перед главной книгой (~40 слов) |
| O01 | ✓ | H2: зачем → файл → листы → импорт → канон → дедуп → автоповтор → дальше + FAQ |
| O02 | ✓ | Outline читается без body |
| O03 | ✓ | FAQ 7 пар из faq_hints research |
| O04 | ✓ | ol (18 li), ul (2), table (1), blockquote (2), pre×1 |
| R01 | ✓ | ≥3 citability-блока (определение staging, вердикт CSV vs PDF, канон+hash) |
| R02 | ✓ | Apps Script Import CSV + Power Query Folder в теле; источники в research-notes |
| R03 | ✓ | Нет фейкового Wordstat/%; примеры сумм в pre не выданы за статистику |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: staging-канон + row_hash (не PDF-SaaS и не ДиректБанк «вместо») |
| E02 | ✓ | «Сделайте / Не делайте» в каждой H2-секции |
| E03 | ✓ | CTA: клуб KODA + Telegram finance_modern (без salebot) |
| Exp01 | ✓ | Режим B, author_id olga-kondratskaya; без fake кейса |
| Exp02 | ✓ | Тон practice/DoD, мост к B19/B22 без дубля |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | PDF SaaS/ПДн, пароли не в ячейке, граница 1С:ДиректБанк |
| Ept02 | ✓ | Internal: ot-excel-k-fin-konturu-30-dney, google-apps-script-finansist-obnovit-dannye, python-finansist-sverka-csv |
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
- OK: `/blog/ot-excel-k-fin-konturu-30-dney/`, `/blog/google-apps-script-finansist-obnovit-dannye/`, `/blog/python-finansist-sverka-csv/`, club.koda-fd.ru, t.me/finance_modern
- `--site-base https://koda-fd.ru`

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 2 (таблица + список канона — допустимо)
- Flesch RU: 75.9 (Easy)
- verdict PASS

## Fact-check

- verdict: pass (5 extracted; 1 verified in fact-bank — «2026»; 4 unverified: «30 дней» якорь, Windows-1251, пример 15000/40702)
- нет blocker-цифр спроса; качественные формулировки без %

## Cannibalization

- verdict: pass (0 issues; loaded 21 metas)
- CLI: `--blog-dir memory/blog/articles -o <article_dir>/cannibalization-report.json`
- note: primary_query дифференцирован от соседних Excel/Sheets/1С тем

## Utility gate

- article: PASS (`action_markers=24`, numbered steps=18, faq_h3=7, tables=1)

## Fix cycle

- cycle 0: HTML без правок writer; все скрипты PASS с первого прогона

## Optional (не blocker)

- укоротить meta `title`/`h1` до 50–65 (сейчас 68; SEO-рабочий — `title_seo` ~58)
- подключить MCP-KV Wordstat перед следующей семантикой
- `<img>` placeholder UI — по желанию перед Дзен (cover отдельно)

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: yes (листы → импорт → канон → дедуп → автоповтор) | Review: no | E-E-A-T SameAs Author: pending (author_id: olga-kondratskaya)
