# QA: B81 kak-iz-google-sheets-podklyuchitsya-k-1s-po-odata-habr-q-a

date: 2026-08-18
score_total: 92/100
core_eeat_lite: 18/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 18 | Title/H1 закрывают Sheets↔OData; FAQ 7; −2 WARN: title_seo без «хабр» из primary_query |
| GEO / citability | 25 | 24 | Answer-first lead, таблица сценариев, схема →, ol 16 li, pre-шаблон, 7 FAQ |
| CORE-EEAT lite | 15 | 13 | 18/20 (см. ниже); −2 Wordstat MCP offline |
| Human voice | 15 | 15 | 0 slop hits, Flesch RU 100, «Сделайте/Не делайте» в H2, режим B Ольга |
| Fact safety | 15 | 14 | fact-check PASS; квоты 20k/100k/60с/50MB из research-notes (Google quotas), не fact-bank |
| Contract HTML | 10 | 8 | linter PASS, char_count 8945 ✓, CTA ≤3 ✓; −2 нет `<img>` (cover отдельно) |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate pass — **выполнен**.

## CORE-EEAT lite: 18/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | Title/meta + H1 закрывают primary (Sheets → 1С OData); «хабр» только в H1 meta |
| C02 | ✓ | Первый абзац — direct answer (сеть UrlFetch), без «в этой статье» |
| C03 | ✓ | Аудитория: финотдел, кнопка обновления среза |
| C04 | ✓ | OData 3.0 / UrlFetchApp / Basic Auth объяснены при первом появлении |
| O01 | ✓ | H2 совпадают с research action_outline + «Что дальше» + FAQ |
| O02 | ✓ | Outline: когда нужно → публикация → ПДн → GAS шаги → ошибки → дальше |
| O03 | ✓ | FAQ 7 пар, ответы-действия |
| O04 | ✓ | ol (16 li), ul (2), table (1), blockquote (2), pre (1) |
| R01 | ✓ | Lead + вердикт + диагностика ошибок — standalone блоки |
| R02 | ✓ | Квоты UrlFetch + платформа ≥8.3.5 — research-notes / Google docs |
| R03 | ✓ | Нет выдуманных цен/% спроса; Wordstat не фейкован |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол Хабр Q&A: Sheets↔UrlFetch + сеть, без дубля B13/B22 |
| E02 | ✓ | «Сделайте / Не делайте» в каждой H2-секции |
| E03 | ✓ | CTA: Telegram + club.koda-fd.ru (2 ≤ 3); salebot нет |
| Exp01 | ✓ | Режим B, author_id olga-kondratskaya; нет fake «я сделал» |
| Exp02 | ✓ | Практика УНФ/ДДС + seed Хабр; не generic AI |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | LAN/private IP, 152-ФЗ/физлица, Plan B push названы |
| Ept02 | ✓ | Internal: vygruzka-1c-excel-odata, google-apps-script…, obezlichivanie…, avtomatizaciya-finansov-no-code |
| — | ✗ | Wordstat MCP-KV offline (−2 к lite → 18/20); цифры спроса не выдуманы |

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
- OK: `/blog/vygruzka-1c-excel-odata/`, `/blog/google-apps-script-finansist-obnovit-dannye/`, `/blog/obezlichivanie-dannyh-chatgpt-finansist/`, `/blog/avtomatizaciya-finansov-no-code/`, t.me/finance_modern, club.koda-fd.ru
- `--site-base https://koda-fd.ru`

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 2 (H2+абзац / таблица → допустимо)
- Flesch RU: 100.0 (Very Easy)
- verdict PASS

## Fact-check

- verdict: pass (3 extracted; 0 in fact-bank; 3 unverified — квоты/runtime из research-notes / Google Apps Script quotas, не blocker)

## Cannibalization

- verdict: pass (0 issues; угол Sheets+UrlFetch ≠ B13 Excel OData / B22 Apps Script меню)

## Utility gate

- article: PASS (`action_markers=18`, numbered_list_items=16, faq_h3=7, tables=1)
- WARN (не blocker): `meta_ab.title_seo` не содержит «хабр» из primary_query

## Fix cycle

- cycle: 0 (FIX writer не требуется)

## Optional (не blocker)

- добавить «Хабр» в `meta_ab.title_seo` / description при желании SEO-полноты primary_query
- подключить MCP-KV Wordstat перед следующей семантикой
- `<img>` — cover-агент после PASS

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: yes (публикация OData + Apps Script → raw_*) | Review: no | E-E-A-T SameAs Author: pending (author_id: olga-kondratskaya)

## Blockers

- нет
