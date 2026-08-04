# QA: B43 limity-rashodov-telegram-alert

date: 2026-08-04
score_total: 91/100
core_eeat_lite: 17/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 19 | H2 по карточке B43, FAQ 7, primary в лиде/meta; −1 нет `<h1>` в body |
| GEO / citability | 25 | 23 | Answer-first lead, таблица реестра, blockquote-схема, ol-шаги, 7 FAQ |
| CORE-EEAT lite | 15 | 13 | 17/20 (см. ниже); −2 Wordstat без MCP-KV |
| Human voice | 15 | 15 | 0 slop hits, Flesch RU 77.4 (Easy), режим B Ольга, «Сделайте/Не делайте» |
| Fact safety | 15 | 13 | fact-check PASS; 7 unverified (примеры сумм, Bot API/Sheets quotas из research-notes) — не blocker |
| Contract HTML | 10 | 8 | linter PASS, объём meta 8963 ✓, CTA ≤3 ✓; −2 нет `<img>` (cover отдельно) |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate pass — **выполнен**.

## CORE-EEAT lite: 17/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | Title/meta + lead закрывают «лимиты расходов telegram алерт» + anti-разъезд лимитов мессенджера |
| C02 | ✓ | Первый абзац — direct answer (реестр Sheets + n8n/Make + алерт) |
| C03 | ✓ | Аудитория: CFO/финконтролёр МСБ, self-serve workflow |
| C04 | ✓ | n8n/Make как «супер-Excel», API как курьер, last_alert = антиспам |
| O01 | ✓ | H2 совпадают с action_outline research (when → registry → pdn → setup → verify → next) |
| O02 | ✓ | Outline: когда нужен → реестр → ПДн → цепочка → проверка → дальше |
| O03 | ✓ | FAQ 7 пар |
| O04 | ✓ | ol (16 li utility), ul, table (1), blockquote (1) |
| R01 | ✓ | Standalone: when-needed, registry columns, verify mistakes, FAQ answers |
| R02 | ✓ | Sheets ~300 rpm, Bot API 1–4096, getUpdates ≤24h, порог 0.8 — research-notes |
| R03 | ✗ | Wordstat-цифры не получены (MCP-KV offline) — в тексте нет фейкового спроса |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: лимиты статей расходов + last_alert, не лимиты Telegram-мессенджера |
| E02 | ✓ | «Сделайте / Не делайте» во всех content-H2 |
| E03 | ✓ | CTA: t.me/finance_modern, club.koda-fd.ru, koda-fd.ru (без salebot) |
| Exp01 | ✓ | Режим B, author_id olga-kondratskaya |
| Exp02 | ✓ | Практика Sheets/n8n/антиспам, без generic AI |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | ПДн, token leak, ложные срабатывания, timezone — названы |
| Ept02 | ✓ | Internal: obezlichivanie…, avtomatizaciya-finansov-no-code (published, 200) |
| — | ✗ | R03: нет свежих Wordstat — −1 к lite (итого 17/20); ещё −2 в score block |

## Script reports

| Скрипт | Verdict | Файл |
|--------|---------|------|
| utility gate (article) | PASS | utility-gate-report.json |
| html-linter | PASS | html-linter-report.json |
| slop-detector | PASS | slop-detector-report.json |
| link-verify | PASS | link-verify.json |
| cannibalization | PASS | cannibalization-report.json |
| fact-check | PASS | fact-check-report.json |

## Link verify

- total: 5, failed: 0
- OK: `/blog/obezlichivanie-dannyh-chatgpt-finansist/`, `/blog/avtomatizaciya-finansov-no-code/`, club.koda-fd.ru, t.me/finance_modern, koda-fd.ru/
- `--site-base https://koda-fd.ru`

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 2 (lead + schema/pre — допустимо)
- Flesch RU: 77.4 (Easy)
- verdict PASS

## Fact-check

- verdict: pass (8 extracted; 1 verified in fact-bank; 7 unverified — примеры 450k/382k, 24h getUpdates, Sheets 300 rpm, 4096 Bot API, «200 строк», «3 дней» гистерезис из research-notes / практики — не blocker)

## Cannibalization

- verdict: pass (0 issues среди 27 статей)
- дайджест / платёжный календарь — plain text, без клона H2 B27/B24

## Utility gate

- article: PASS (`action_markers=17`, numbered_list_items=16, faq_h3=7, tables=1, blockquotes=1)

## Fix cycle

- cycle: не требуется (все скрипты PASS с первого прогона 2026-08-04)

## Forbidden checks

- em dash (—): 0
- salebot: 0
- MCP URLs in production: 0

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: yes (реестр + n8n + Telegram) | Review: no | E-E-A-T SameAs Author: pending (author_id: olga-kondratskaya)
