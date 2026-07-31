# QA: B24 n8n-finotdel-ustanovka-pervyj-workflow

date: 2026-07-31
score_total: 92/100
core_eeat_lite: 19/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 18 | primary в title_seo/lead; H2 action; FAQ 7; −2 длинный H1/title |
| GEO / citability | 25 | 24 | таблица Cloud vs self-host, ol установка+workflow, pre .env, схема Sheets→Telegram, чек-лист ul |
| CORE-EEAT lite | 15 | 14 | 19/20 (см. ниже); −1 Wordstat MCP-KV offline |
| Human voice | 15 | 15 | 0 slop, режим B Ольга, «Сделайте/Не делайте» |
| Fact safety | 15 | 14 | fact-check PASS; 7 дней / порт 5678 / цены / stable 2.32.6 сверены с research-notes |
| Contract HTML | 10 | 7 | linter PASS, 8788 ✓, CTA club+TG ≤2 ✓; −3 cover отдельно |

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
| char_count | 8788 (8500–9500) ✓ |
| CTA | club.koda-fd.ru ×1 + t.me/finance_modern ×1 |

## CORE-EEAT lite: 19/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | Title/meta + lead закрывают «как установить n8n» для финотдела |
| C02 | ✓ | Первый абзац — direct answer, без «в этой статье» |
| C03 | ✓ | Аудитория: финансист, Sheets/реестр, дайджест в Telegram, 152-ФЗ |
| C04 | ✓ | n8n / self-hosted / Docker объяснены в лиде (~50 слов) |
| O01 | ✓ | H2: зачем → Cloud vs self-host → Docker/HTTPS → workflow → security → дальше + FAQ |
| O02 | ✓ | Outline читается без body |
| O03 | ✓ | FAQ 7 пар из research faq_hints |
| O04 | ✓ | ol×3 (установка + workflow + next), ul чек-лист, table, pre, blockquote×2 |
| R01 | ✓ | ≥3 citability-блока (вердикт Cloud/self-host, .env/WEBHOOK_URL, схема Sheets→Telegram) |
| R02 | ✓ | docs.n8n.io Docker/Compose/OAuth + pricing URL с датой в research-notes |
| R03 | ✓ | Нет фейкового Wordstat; цены Cloud с оговоркой annually; stable 2.32.6 «на дату статьи» |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: финотдел + 152-ФЗ + дайджест Sheets→Telegram (не клон общего VPS-гайда) |
| E02 | ✓ | «Сделайте / Не делайте» в каждой H2-секции |
| E03 | ✓ | CTA: Telegram finance_modern + клуб KODA (без salebot) |
| Exp01 | ✓ | Режим B, author_id olga-kondratskaya; «я ставлю/беру» без fake кейса |
| Exp02 | ✓ | Тон practice/security; мост к B14/B15 без дубля B25 Make |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | HTTPS, encryption key, 5678 localhost, ПДн в Telegram, 152-ФЗ не «автоматом» |
| Ept02 | ✓ | Internal: avtomatizaciya-finansov-no-code, obezlichivanie, debitorka, ollama |
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

- total: 6, failed: 0
- OK: `/blog/avtomatizaciya-finansov-no-code/`, `/blog/obezlichivanie-dannyh-chatgpt-finansist/`, `/blog/upravlenie-debitorkoj-reestr-napominaniya/`, `/blog/ollama-finotdel-lokalnaya-nejroset/`, t.me/finance_modern, club.koda-fd.ru
- `--site-base https://koda-fd.ru`

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 3 (таблица + pre + схема — допустимо)
- Flesch RU: 97.2 (Very Easy)
- verdict PASS

## Fact-check

- verdict: pass (2 extracted; 0 в fact-bank — ожидаемо)
- «7 дней» (Google OAuth Testing) и порт `5678` сверены с research-notes (#1, #12); цены Starter/Pro и stable 2.32.6 — в тексте с оговорками, в fact-bank нет (не blocker)

## Cannibalization

- verdict: pass (0 issues; loaded 20 metas)
- note: primary «как установить n8n» дифференцирован от B02 (AI-агенты в n8n) и legacy no-code hub

## Utility gate

- article: PASS (`action_markers=22`, numbered steps=16, faq_h3=7, tables=1)

## Fix cycle

- cycle 0: HTML без правок; `article.meta.json` `char_count` 8785 → 8788 (writer vs `len(plain)` с пробелами)

## Optional (не blocker)

- укоротить meta `title`/`h1` до 50–65 (сейчас длинный; SEO-рабочий — `title_seo`)
- подключить MCP-KV Wordstat перед следующей семантикой
- `<img>` placeholder UI — по желанию перед Дзен (cover отдельно)
- добавить «7 дней» / порт 5678 в `memory/brief/fact-bank.md` (снизит unverified в fact-check)

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: yes (Docker/HTTPS → OAuth/Bot → Sheets→Telegram) | Review: no | E-E-A-T SameAs Author: pending (author_id: olga-kondratskaya)
