# QA: B92 mcp-google-sheets-cursor-reestry

date: 2026-08-27
score_total: 78/100
core_eeat_lite: 19/20
link_verify: fail
utility_gate: pass
verdict: FAIL

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 18 | primary в лиде; FAQ 7; H2 how-to ×8; таблица Path A/B; meta_ab ✓ |
| GEO / citability | 25 | 23 | Answer-first lead; blockquote workflow; ol×3; pre/code mcp.json; −2 за dead external href |
| CORE-EEAT lite | 15 | 14 | 19/20; −1 Wordstat MCP-KV offline |
| Human voice | 15 | 15 | 0 slop hits, Flesch RU 100, режим B Ольга, «Сделайте/Не делайте» |
| Fact safety | 15 | 14 | fact-check PASS (6 extracted / 1 bank); цифры 1–2 ч / 200–300 / Error 400 из research |
| Contract HTML | 10 | −6→4 | linter PASS, объём 8884 ✓, CTA club+TG ✓; **link-verify FAIL** (−6 hard gate) |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate pass — **НЕ выполнен** (link-verify fail).

## Hard bans (KODA)

| Проверка | Результат |
|----------|-----------|
| TL;DR blockquote | нет |
| Fact Check блок | нет |
| «—» (emdash U+2014) | 0 |
| «мы в KODA» | нет |
| salebot / koda_salebot | нет |
| article_mode | B |
| char_count | 8884 (8500–9500) ✓ |
| CTA | club.koda-fd.ru ×1 + t.me/finance_modern ×1 |
| TOC с якорями | нет |

## CORE-EEAT lite: 19/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | Title/meta + lead: MCP Google Sheets Cursor + реестр без копипаста |
| C02 | ✓ | Первый абзац — direct answer (doc_key, 1–2 ч, MCP Logs) |
| C03 | ✓ | Аудитория: финансист/CFO с реестром в Sheets |
| C04 | ✓ | Path A OAuth vs Path B SA; MCP vs B82 скрипт; vs копипаст |
| O01 | ✓ | H2: когда → безопасность → Path B → Path A → сценарий → verify → next + FAQ |
| O02 | ✓ | Outline читается без body |
| O03 | ✓ | FAQ 7 пар |
| O04 | ✓ | ol, ul, table, blockquote, pre/code |
| R01 | ✓ | ≥3 citability-блока (таблица маршрутов, workflow, mcp.json, промпт) |
| R02 | ✓ | 03.08.2026 changelog, 200–300 договоров, 80–100 заявок — research |
| R03 | ✓ | Нет фейкового Wordstat; Marketplace/OAuth — honest note |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: финреестры doc_key, не dev-обзор MCP |
| E02 | ✓ | «Сделайте / Не делайте» в H2-секциях |
| E03 | ✓ | CTA: Telegram finance_modern + клуб KODA (без salebot) |
| Exp01 | ✓ | Режим B, author_id olga-kondratskaya |
| Exp02 | ✓ | Тон practice/DoD, мост B21/B82 |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | ПДн: обезличивание, SA share, approval write-tools |
| Ept02 | ✓ | Internal: avtomatizaciya-finansov-no-code, obezlichivanie-dannyh-chatgpt-finansist |
| — | ✗ | Wordstat infra: MCP-KV offline (−1 lite → 19/20) |

## Script reports

| Скрипт | Verdict | Файл |
|--------|---------|------|
| fact-check | PASS | fact-check-report.json |
| link-verify | **FAIL** | link-verify.json |
| html-linter | PASS | html-linter-report.json |
| slop-detector | PASS | slop-detector-report.json |
| cannibalization | PASS (portfolio WARNING B21↔B80) | cannibalization-report.json |
| utility gate (article) | PASS | utility-gate-report.json |

## Link verify

- total: 7, failed: 1 → **verdict fail**
- OK: `/blog/mcp-cursor-finansist-instrumenty/`, `/blog/google-sheets-api-integraciya-finotdel/`, `/blog/avtomatizaciya-finansov-no-code/`, `/blog/obezlichivanie-dannyh-chatgpt-finansist/`, t.me/finance_modern, club.koda-fd.ru
- **FAIL:** `https://cursor.com/agents` → HTTP 403 (HEAD+GET; bot/WAF; UA не помогает)
- `--site-base https://koda-fd.ru`
- Примечание: `https://forum.cursor.com/t/167413` отвечает 200 (источник research)

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 3
- Flesch RU: 100.0 (Very Easy)
- verdict PASS

## Fact-check

- verdict: pass (6 extracted; 1 verified in fact-bank — «2026»)
- прочие метрики (1–2 ч, 200–300, Error 400, 80–100) — из research-notes, не market-claims

## Cannibalization

- global verdict: warning (B80↔B21 overlap 75%, не затрагивает B92)
- B92: pass — primary «mcp google sheets cursor»; adjacent B21/B82, не duplicate

## Utility gate

- article: PASS (`action_markers=19`, numbered steps=17, faq_h3=7, tables=1)
- report: utility-gate-report.json

## FIX для writer (cycle 1) — НЕ править geo-qa

**Блокер:** одна внешняя ссылка ломает hard gate `link-verify`.

1. В `article.html` найти `<a href="https://cursor.com/agents" …>cursor.com/agents</a>`.
2. Выбрать один вариант (предпочтительно A):
   - **A (рекомендуется):** заменить href на `https://forum.cursor.com/t/167413` (research: OAuth Error 400 / workaround; link-verify 200). Текст якоря можно оставить «forum Cursor (OAuth Error 400)» или «тред Cursor про Error 400».
   - **B:** убрать тег `<a>`, оставить plain/`<b>cursor.com/agents</b>` (как уже в списке ошибок) — link-verify не проверяет голый текст.
3. Не менять longread/структуру/char_count сверх необходимого для ссылки (±50 символов ок).
4. После правки: перезапуск `excalibur_blog_link_verify.py` → ожидается pass → geo-qa cycle 2.

**Запрещено geo-qa:** править article.html самостоятельно; cover/schema/publish.

## Fix cycle

- cycle 0 (writer 2026-08-27): article.html 8884; Path A OAuth Error 400 + agents workaround
- cycle 1 (geo-qa 2026-08-27): все скрипты кроме link-verify PASS → **FAIL**, FIX выше

## Schema ready (после PASS — handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: yes (GCP→mcp.json→verify→registry) | Review: no | E-E-A-T SameAs Author: pending (author_id: olga-kondratskaya)

**cover/schema НЕ запускать** до geo-qa PASS.
