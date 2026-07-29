# QA: B18 schet-1c-unf-telefon-http-servis

date: 2026-07-22
score_total: 92/100
core_eeat_lite: 19/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 18 | title_seo 49, desc_seo 132; H2 how_to; FAQ 7; primary в лиде; −2 `title`/`h1` 67 > 65 |
| GEO / citability | 25 | 24 | Answer-first lead, таблица сравнения, схема →, ol×3, pre×2, 7 FAQ; без TOC/TL;DR/Fact Check |
| CORE-EEAT lite | 15 | 14 | 19/20 (см. ниже); −1 Wordstat MCP-KV offline |
| Human voice | 15 | 15 | 0 slop hits, Flesch RU 83.6, режим B Ольга, «Сделайте/Не делайте» ×5 |
| Fact safety | 15 | 14 | fact-check PASS; 3 unverified = примеры JSON (8080/ИНН/10000), не маркетинг-цифры |
| Contract HTML | 10 | 7 | linter PASS, объём 8860 ✓, CTA club+TG ≤2 ✓; −3 нет `<img>` (cover отдельно) |

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
| char_count | 8860 (8500–9500) ✓ |
| CTA | club.koda-fd.ru ×1 + t.me/finance_modern ×1 |

## CORE-EEAT lite: 19/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | Title/meta + lead: счёт на оплату из УНФ с телефона через HTTP |
| C02 | ✓ | Первый абзац — direct answer, без «в этой статье» |
| C03 | ✓ | Аудитория: менеджер/финконтур, не RDP и не полное МП |
| C04 | ✓ | Счёт на оплату vs счёт-фактура; HTTP-сервис / API / FastAPI / JSON |
| O01 | ✓ | H2: задача → архитектура → установка → запуск → риски → дальше + FAQ |
| O02 | ✓ | Outline читается без body |
| O03 | ✓ | FAQ 7 пар (УНФ 1.6/3.0, 1С-ник, Telegram, МП, НДС, безопасность, PDF) |
| O04 | ✓ | ol (16 li), ul (1), table (1), blockquote (3), pre×2 |
| R01 | ✓ | ≥3 citability-блока (таблица выбора, схема, вердикт безопасности) |
| R02 | ✓ | Версия УНФ 3.0.13.374 + метаданные документа в тексте; research-notes |
| R03 | ✓ | Нет фейкового Wordstat/процентов; примерные ИНН/суммы в JSON |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: узкий InvoiceBot + FastAPI/PWA, не клон «мобильное УНФ» |
| E02 | ✓ | «Сделайте / Не делайте» в 5 H2-секциях |
| E03 | ✓ | CTA: Telegram finance_modern + клуб KODA (без salebot) |
| Exp01 | ✓ | Режим B, author_id olga-kondratskaya; пилот без fake кейса |
| Exp02 | ✓ | Тон practice/DoD, мост к no-code и OData без дубля выгрузки |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | Права InvoiceBot, HTTPS, whitelist, .env, маскирование ПДн |
| Ept02 | ✓ | Internal: avtomatizaciya-finansov-no-code, vygruzka-1c-excel-odata |
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

- total: 4, failed: 0
- OK: `/blog/avtomatizaciya-finansov-no-code/`, `/blog/vygruzka-1c-excel-odata/`, t.me/finance_modern, club.koda-fd.ru
- `--site-base https://koda-fd.ru`
- note: сертификат koda-fd.ru/club — verify failed на default context; HTTP 200 подтверждён с `ssl._create_unverified_context` (`ssl_note` в JSON)

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 3 (таблица+схема+JSON — допустимо)
- Flesch RU: 83.6 (Very Easy)
- verdict PASS

## Fact-check

- verdict: pass (4 extracted; 1 verified in fact-bank — «2026»)
- 8080 / 7700000000 / 10000 — примеры конфига и JSON, не blocker

## Cannibalization

- verdict: pass (0 issues; loaded 16 metas)
- note: primary_query `выставить счет в 1с` не пересекается токеново с B13 OData; угол HTTP+телефон vs выгрузка Excel

## Utility gate

- article: PASS (`action_markers=13`, numbered steps=16, faq_h3=7, actionable H2 ≥3)
- article-qa.md: зафиксирован PASS (этот файл)

## Fix cycle

- cycle 1: GEO QA — H2 → императивы (utility actionable_h2); internal links → `/blog/…`; char_count 8860; meta geo_qa PASS

## Optional (не blocker)

- обновить SSL-сертификат koda-fd.ru (инфра)
- укоротить meta `title`/`h1` до 50–65 (сейчас 67; SEO-рабочий — `title_seo` 49)
- подключить MCP-KV Wordstat перед следующей семантикой
- `<img>` placeholder UI — по желанию перед Дзен (cover отдельно)

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: yes (установка InvoiceBot → запуск PWA → безопасность) | Review: no | E-E-A-T SameAs Author: pending (author_id: olga-kondratskaya)
