# QA: B58 reestr-upd-google-sheets

date: 2026-08-15
score_total: 90/100
core_eeat_lite: 19/20
link_verify: pass (self-check)
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 18 | title_seo 52, desc 156; 5 actionable H2 + «Что дальше» + FAQ 7; primary в лиде |
| GEO / citability | 25 | 23 | Answer-first lead, 2 таблицы, workflow blockquote, Apps Script pre, 7 FAQ; без TOC/TL;DR/Fact Check |
| CORE-EEAT lite | 15 | 14 | 19/20; −1 Wordstat MCP-KV offline |
| Human voice | 15 | 14 | 0 em dash, режим B Ольга; простой язык, финансовые аналогии |
| Fact safety | 15 | 14 | fact-check-report.json pass; УПД 5.03, ст. 174, kit_status из research-notes |
| Contract HTML | 10 | 9 | linter PASS, объём 9473 ✓, CTA club×2+TG×1+koda×1 ≤5 лимитов ✓; −1 нет img (cover отдельно) |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, utility gate pass — **выполнен**.

## Hard bans (KODA)

| Проверка | Результат |
|----------|-----------|
| TL;DR blockquote | нет |
| Fact Check блок | нет |
| «—» (emdash U+2014) | 0 |
| ««» / »» | 0 |
| «мы в KODA» | нет |
| salebot / koda_salebot | нет |
| article_mode | B |
| char_count | 9473 ✓ (8500–9500) |
| hook | 413 ✓ (350–500) |
| CTA | club.koda-fd.ru ×2 + t.me/finance_modern ×1 + koda-fd.ru ×1 |

## CORE-EEAT lite: 19/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | Title/meta + lead закрывают «реестр упд google sheets» |
| C02 | ✓ | Первый абзац — direct answer |
| C03 | ✓ | Аудитория: бухгалтерия, финотдел, закупки |
| C04 | ✓ | doc_key, kit_status, анти-дубли, маршруты наполнения |
| O01 | ✓ | H2: when → security → setup → verify → automate → next + FAQ |
| O02 | ✓ | Outline actionable без body |
| O03 | ✓ | FAQ 7 пар |
| O04 | ✓ | ol (8 setup + 5 next), table (2), blockquote (2), pre×1 |
| R01 | ✓ | Вердикт таблицы маршрутов, workflow blockquote, таблица ошибок |
| R02 | ✓ | УПД 5.03, ст. 174, Apps Script квоты — research-notes |
| R03 | ✓ | Нет фейкового Wordstat/% |
| R04 | ✓ | FAQ: ответ-действие в первом предложении |
| E01 | ✓ | Угол: внутренний реестр комплектности, не бланк УПД 2026 |
| E02 | ✓ | «Сделайте / Не делайте» в when-needed и prep-security |
| E03 | ✓ | CTA club + Telegram (без salebot) |
| Exp01 | ✓ | Режим B, author_id olga-kondratskaya |
| Exp02 | ✓ | Тон practice/DoD |
| Exp03 | ✓ | 0 запрещённых штампов |
| Ept01 | ✓ | ПДн, обезличивание, ACL Workspace |
| Ept02 | ✓ | Internal: avtomatizaciya-finansov-no-code, obezlichivanie-dannyh |
| — | ✗ | Wordstat infra offline (−1) |

## Self-check scripts

| Проверка | Verdict |
|----------|---------|
| html-linter | PASS |
| char_count 8500–9500 | PASS (9473) |
| em dash | PASS (0) |
| numbered steps | PASS (8 + 5) |
| FAQ h3 | PASS (7) |
| tables | PASS (2) |
| article_mode B | PASS |
| utility gate (with meta) | PASS |
| fact-check | PASS |
| slop-detector | WARNING (6 long sentences, 0 cliches) |
| cannibalization | PASS |

## Internal links

- `/blog/avtomatizaciya-finansov-no-code/` ✓
- `/blog/obezlichivanie-dannyh-chatgpt-finansist/` ✓
- `/blog/statusy-edo-google-sheets/` (related)
- `/blog/reestr-dogovorov-google-sheets/` (related)

## Fix cycle

- cycle 0: writer self-QA — правок не потребовалось

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: yes (setup ol 8 шагов) | Review: no | E-E-A-T SameAs Author: pending (author_id: olga-kondratskaya)
