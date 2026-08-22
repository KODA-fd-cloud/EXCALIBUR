# QA: B90 cursor-skill-vygruzka-1c-odata

date: 2026-08-22
score_total: 92/100
core_eeat_lite: 19/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 19 | title_seo 52, desc 158; H2 checklist; FAQ 6; primary в лиде; −1 длинный h1 в meta |
| GEO / citability | 25 | 24 | Answer-first lead 387 симв, таблица Rules/MCP/Skill + errors, workflow blockquote, ol×22, pre×1, 6 FAQ |
| CORE-EEAT lite | 15 | 14 | 19/20; −1 Wordstat MCP-KV offline в research |
| Human voice | 15 | 15 | 0 slop hits, Flesch RU 97.3, режим B Ольга, «Сделайте/Не делайте» |
| Fact safety | 15 | 14 | fact-check PASS (8 stats, 2 verified in fact-bank; 6 tech refs из research-notes) |
| Contract HTML | 10 | 5 | linter PASS, объём 8949 ✓, CTA club×1 + TG×1 ✓; −5 нет `<img>` (cover отдельно) |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate pass — **выполнен**.

## Hard bans (KODA)

| Проверка | Результат |
|----------|-----------|
| TL;DR | нет |
| Fact Check блок | нет |
| «—» (emdash U+2014) | 0 |
| ««» / «»» (guillemets в body) | 0 |
| «мы в KODA» | нет |
| salebot / koda_salebot | нет |
| article_mode | B |
| char_count | 8949 (8500–9500) ✓ |
| CTA | club.koda-fd.ru ×1 + t.me/finance_modern ×1; koda-fd.ru упоминание в тексте ×1 |

## CORE-EEAT lite: 19/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | Title/meta + lead закрывают cursor skill 1С OData |
| C02 | ✓ | Первый абзац – direct answer |
| C03 | ✓ | Аудитория: финотдел, повторяемые выгрузки ДДС/дебиторка |
| C04 | ✓ | Skill/MCP/OData объяснены через аналогии rules/транспорт |
| O01 | ✓ | H2: when → security → setup → verify/errors → next + FAQ |
| O02 | ✓ | Outline из карточки B90 |
| O03 | ✓ | FAQ 6 пар из faq_hints research |
| O04 | ✓ | ol (22 li), table (2), blockquote (2), pre×1 |
| R01 | ✓ | ≥3 citability-блока (таблица слоёв, схема workflow, DoD сверки) |
| R02 | ✓ | cursor.com/docs/skills, 1c-odata-mcp, v8.1c.ru – URLs в research-notes |
| R03 | ✓ | Нет фейкового Wordstat; offline задокументирован |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: fin-export checklist vs Desko77 dev-skills; граница B13/B80/B23 |
| E02 | ✓ | «Сделайте / Не делайте» в каждой H2-секции |
| E03 | ✓ | CTA: Telegram finance_modern + клуб KODA (без salebot) |
| Exp01 | ✓ | Режим B, author_id olga-kondratskaya |
| Exp02 | ✓ | Тон practice/DoD, без fake кейса |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | 152-ФЗ, read-only, env, exports/, обезличивание |
| Ept02 | ✓ | Internal: avtomatizaciya-finansov-no-code, obezlichivanie, vygruzka-1c-excel-odata, mcp-1c-cursor-ostatki-oboroty, cursor-rules-finotdel |
| — | ✗ | Wordstat infra offline (−1 lite → 19/20) |

## Script reports

| Скрипт | Verdict | Файл |
|--------|---------|------|
| html-linter | PASS | html-linter-report.json |
| slop-detector | PASS | slop-detector-report.json |
| utility gate (article) | PASS | utility-gate-report.json |
| link-verify | PASS (7/7) | link-verify.json |
| fact-check | PASS | fact-check-report.json |
| cannibalization | PASS (B90 не в issues) | cannibalization-report.json |

## Link verify

- total: 7, failed: 0
- OK: `/blog/avtomatizaciya-finansov-no-code/`, `/blog/obezlichivanie-dannyh-chatgpt-finansist/`, `/blog/vygruzka-1c-excel-odata/`, `/blog/mcp-1c-cursor-ostatki-oboroty/`, `/blog/cursor-rules-finotdel/`, t.me/finance_modern, club.koda-fd.ru
- `--site-base https://koda-fd.ru`

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 2
- Flesch RU: 97.3 (Very Easy)
- verdict PASS

## Fact-check

- verdict: PASS
- extracted: 8 stats; verified in fact-bank: 2 (2026, 500); unverified: 6 (115, 1000, 100000, 401, 404, 200000 — tech refs из research-notes, не маркетинг)
- Опора на research-notes fact table (20 утверждений с URL)
- Без «115 skills обязательны для CFO», без write без human-in-the-loop

## Cannibalization

- global report: WARNING (B80↔B21 overlap 75%, не B90)
- B90 primary `cursor skill 1с odata` — дифференциация от B13 (Excel), B80 (MCP остатки), B23 (rules)
- verdict: PASS

## Utility gate

- article: PASS (`checklist`, numbered steps 22, faq_h3=6, h2=5, tables=2)

## Fix cycle

- cycle 0: HTML без правок; все gates PASS

## Optional (не blocker)

- подключить MCP-KV Wordstat перед следующей семантикой
- `<img>` placeholder UI – cover отдельно

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (6) | HowTo: yes (setup → verify) | Review: no | E-E-A-T SameAs Author: pending (author_id: olga-kondratskaya)
