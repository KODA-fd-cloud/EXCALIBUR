# QA: B37 import-1c-unf-excel-regulyarno

date: 2026-08-03
score_total: 90/100
core_eeat_lite: 19/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 18 | H1/meta = primary; H2 по контуру how-to; FAQ 6; secondary не дублирует H1 |
| GEO / citability | 25 | 23 | Answer-first lead; таблица A/B/C; workflow →; ol 11; FAQ citability-first |
| CORE-EEAT lite | 15 | 14 | 19/20 (см. ниже); −1 к весу за soft-ориентиры времени без Wordstat |
| Human voice | 15 | 15 | mode B Ольга; 0 slop; «Сделайте/Не делайте» в каждой H2 |
| Fact safety | 15 | 13 | fact-check PASS; «100 тысяч»/«5 минут» из research, не fact-bank |
| Contract HTML | 10 | 7 | linter PASS, 8932 ✓, CTA=2 ✓; −3 нет `<img>` (cover отдельно) |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate pass — **выполнен**.

## CORE-EEAT lite: 19/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | Title/H1/meta закрывают «импорт 1с унф excel регулярно» |
| C02 | ✓ | Lead: боль → канал → refresh/регламент; без «в этой статье» |
| C03 | ✓ | Финансист / финотдел, ежедневный срез УНФ |
| C04 | ✓ | OData / Power Query / HTTP-сервис — короткие аналогии в лиде |
| O01 | ✓ | when-needed → security → choose → setup A → errors → next + FAQ |
| O02 | ✓ | Логика: зачем → гигиена → выбор схемы → шаги → сбои → дальше |
| O03 | ✓ | FAQ 6 пар, queries про программиста / Online / отличие от OData |
| O04 | ✓ | ol 11, ul 2, table 1, blockquote 2 |
| R01 | ✓ | Lead, вердикт схем, FAQ-ответы — standalone |
| R02 | ✓ | Desktop-only timer; OData auth=веб-сервисы; 100k ориентир — research-notes |
| R03 | ✓ | Нет фейковых %/цен; soft «полчаса–два часа» как ориентир внедрения |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: регулярный контур vs разовая OData (B13); SERP Excel→1С отвергнут |
| E02 | ✓ | «Сделайте / Не делайте» в каждой H2 |
| E03 | ✓ | CTA: t.me/finance_modern + club.koda-fd.ru (2 ≤ 3); salebot нет |
| Exp01 | ✓ | article_mode B; author_id olga-kondratskaya; без fake «я сделал» |
| Exp02 | ✓ | Практика УНФ/ДДС/staging; не generic AI |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | Online/закрытый файл, OData на миллионах, 401/403, ПДн |
| Ept02 | ✓ | Internal: B13 OData, обезличивание, Power Query, no-code |
| — | ✗ | −1 lite: нет Wordstat-цифр спроса (MCP-KV offline) — в тексте фейка нет |

## Script reports

| Скрипт | Verdict | Файл |
|--------|---------|------|
| fact-check | PASS | fact-check-report.json |
| link-verify | PASS | link-verify.json |
| html-linter | PASS | html-linter-report.json |
| slop-detector | PASS | slop-detector-report.json |
| cannibalization | WARNING (non-fail) | cannibalization-report.json |
| utility gate (article) | PASS | utility-gate-report.json |

## Link verify

- total: 6, failed: 0
- OK: `/blog/vygruzka-1c-excel-odata/`, `/blog/obezlichivanie-dannyh-chatgpt-finansist/`, `/blog/power-query-finansist-obnovlenie/`, `/blog/avtomatizaciya-finansov-no-code/`, t.me/finance_modern, club.koda-fd.ru
- `--site-base https://koda-fd.ru`

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 3 (таблица/схема — допустимо)
- Flesch RU: 79.8 (Easy)
- verdict PASS

## Fact-check

- verdict: pass (3 extracted; 1 verified in fact-bank; 2 unverified — «5 минут», «100» из research-notes, не blocker)

## Cannibalization

- verdict: **warning** (0 fail)
- WARN: primary B13 «выгрузка из 1с в excel» ↔ secondary B37 «выгрузка 1с в excel по расписанию» (sim 75%)
- Не blocker: угол B37 = регулярный refresh/расписание; в тексте явная развилка + internal на B13; CLI `--blog-dir` exit 0

## Utility gate

- article: PASS (`action_markers=19`, numbered steps=11, tables=1, faq_h3=6, water_hits=[])

## Fix cycle

- нет (verdict PASS с первого прогона)

## Optional (не blocker)

- secondary «выгрузка 1с в excel по расписанию» можно сузить ещё сильнее при следующем refill topics
- Wordstat / MCP-KV при следующей семантике
- `<img>` placeholder — cover-агент отдельно

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (6) | HowTo: yes (схема A + чеклист) | Review: no | E-E-A-T SameAs Author: pending (author_id: olga-kondratskaya)
