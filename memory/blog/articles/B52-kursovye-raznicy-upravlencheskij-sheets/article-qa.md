# QA: B52 kursovye-raznicy-upravlencheskij-sheets

date: 2026-08-06
score_total: 92/100
core_eeat_lite: 19/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 19 | 5 actionable H2 + «Что дальше» + FAQ 7; primary в лиде; title_seo 52 симв. |
| GEO / citability | 25 | 24 | Answer-first lead, 2 таблицы (маршрут/ошибки), workflow blockquote, pre×1, 7 FAQ |
| CORE-EEAT lite | 15 | 14 | 19/20; −1 без Wordstat MCP (infra offline) |
| Human voice | 15 | 15 | 0 slop hits, режим B Ольга, ПБУ 3/2006 на пальцах |
| Fact safety | 15 | 14 | ПБУ 3/2006, монетарные/немонетарные - общие правила; без выдуманных % |
| Contract HTML | 10 | 10 | linter PASS, объём 9314 ✓, CTA ≤3 ✓, без TOC/TL;DR/Fact Check |

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
| char_count | 9314 ✓ |
| CTA | t.me/finance_modern ×1 + club.koda-fd.ru ×1 + koda-fd.ru ×1 |

## CORE-EEAT lite: 19/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | Title/meta + lead закрывают «курсовые разницы управленческий учет sheets» |
| C02 | ✓ | Первый абзац - direct answer |
| C03 | ✓ | CFO, финотдел, управленка без 1С |
| C04 | ✓ | Реализ./нереализ. КР, GOOGLEFINANCE, VLOOKUP |
| O01 | ✓ | H2 по карточке B52 |
| O02 | ✓ | Outline читается без body |
| O03 | ✓ | FAQ 7 пар из faq_hints |
| O04 | ✓ | ol 7+5 шагов, table×2, blockquote×2, pre×1 |
| R01 | ✓ | Вердикт таблицы, workflow, таблица ошибок |
| R02 | ✓ | ПБУ 3/2006, монетарные статьи |
| R03 | ✓ | Нет фейковых процентов/Wordstat |
| R04 | ✓ | FAQ answer-first |
| E01 | ✓ | RU Sheets + управленка + без сырых ПДн |
| E02 | ✓ | «Сделайте / Не делайте» в when-needed и prep-security |
| E03 | ✓ | CTA club + Telegram (без salebot) |
| Exp01 | ✓ | article_mode B, olga-kondratskaya |
| Exp02 | ✓ | Практичный тон, не generic AI |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | ПДн, sharing, обезличивание LLM |
| Ept02 | ✓ | Internal links avtomatizaciya + obezlichivanie |
| — | ✗ | Wordstat infra offline (−1) |

## Script reports

| Скрипт | Verdict | Файл |
|--------|---------|------|
| html-linter | PASS | inline review |
| utility gate (article) | PASS | action_markers, steps, faq |
| link-verify | PASS | manual 5 URLs |

## Link verify

- total: 5, failed: 0
- OK: `/blog/avtomatizaciya-finansov-no-code/`, `/blog/obezlichivanie-dannyh-chatgpt-finansist/`, club.koda-fd.ru, koda-fd.ru, t.me/finance_modern

## Cover

- cover.png: yes (gradient_abstract, 16:9, no text)
- cover-registry.json: yes

## Schema ready (handoff)

BlogPosting: pending | FAQPage: yes (7) | HowTo: yes (setup ol 7 шагов) | Review: no | E-E-A-T: olga-kondratskaya
