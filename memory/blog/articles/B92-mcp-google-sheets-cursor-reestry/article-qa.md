# QA: B92 mcp-google-sheets-cursor-reestry

date: 2026-09-12
score_total: 74/100
core_eeat_lite: 18/20
link_verify: pass
utility_gate: pass
verdict: FAIL

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 18 | primary в лиде; FAQ 7; H2 how-to ×7; таблица Path A/B; meta_ab OK |
| GEO / citability | 25 | 22 | Answer-first lead 425; blockquote workflow; ol×3; pre/code mcp.json + промпт; −3 объём ниже контракта |
| CORE-EEAT lite | 15 | 13 | 18/20; −1 Wordstat MCP-KV offline; −1 объём (Ept/Contract) |
| Human voice | 15 | 15 | 0 slop hits, Flesch RU 100, режим B Ольга, «Сделайте/Не делайте» ×6 |
| Fact safety | 15 | 14 | fact-check PASS; 5 unverified = HTTP-коды/длительности из research, не market-claims |
| Contract HTML | 10 | 2 | linter PASS, CTA club+TG ✓; **объём plain ~7216 вне 8500–9500**; meta.char_count=9313 считает HTML с тегами |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate pass — **не выполнен** (score 74 < 80; объём вне контракта).

## Hard bans (KODA)

| Проверка | Результат |
|----------|-----------|
| TL;DR blockquote | нет |
| Fact Check блок | нет |
| «—» (emdash U+2014) | 0 |
| «мы в KODA» | нет |
| salebot / koda_salebot | нет |
| article_mode | B |
| char_count (plain, без тегов) | **7216 — FAIL** (нужно 8500–9500) |
| char_count в meta | 9313 = `len(html)` — **неверный метод** |
| CTA | club.koda-fd.ru ×1 + t.me/finance_modern ×1 |
| TOC с якорями | нет |

## Блокеры для writer (FIX cycle 1)

1. **Объём:** довести plain text (HTML без тегов, пробелы считаются) до **8500–9500**. Сейчас ~7216 (−1284 до низа банда). Не раздувать тегами/разметкой.
2. **meta.char_count:** пересчитать как plain text и записать реальное значение в банде.
3. **Что дописать (предпочтительно, без полного рерайта):**
   - Path B: 1–2 шага про GCP enable Sheets API / где лежит client_email (коротко).
   - Сценарий: явный пример диапазона/листа после write (diff status/comment).
   - Verify: 1 абзац про ротацию SA-ключа + allowlist write-tools (уже намёки есть — развернуть).
   - FAQ: чуть плотнее ответы (Cloud Agents / 429 / B82), без воды.
4. **Не трогать:** угол Path A vs Path B, research-факты (60/user, 300/project, cursor://), CTA, internal links, режим B.

После правки — снова geo-qa (скрипты + article-qa).

## CORE-EEAT lite: 18/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | Title/meta + lead: MCP Google Sheets Cursor + реестр без копипаста |
| C02 | ✓ | Первый абзац — direct answer (doc_key, 1–2 ч, MCP Logs) |
| C03 | ✓ | Аудитория: финансист/CFO с реестром в Sheets |
| C04 | ✓ | MCP / Path A OAuth / Path B SA / vs B82 — объяснены |
| O01 | ✓ | H2: когда → security → Path B → Path A → сценарий → verify → next + FAQ |
| O02 | ✓ | Outline читается без body |
| O03 | ✓ | FAQ 7 пар |
| O04 | ✓ | ol, ul, table, blockquote×2, pre×2 |
| R01 | ✓ | ≥3 citability (таблица, workflow, mcp.json, промпт) |
| R02 | ✓ | квоты 300/60, Error 400 cursor://, Path B freema — research-notes 2026-09-12 |
| R03 | ✓ | Нет фейкового Wordstat/процентов |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: финреестры doc_key, не dev-обзор MCP |
| E02 | ✓ | «Сделайте / Не делайте» в H2-секциях |
| E03 | ✓ | CTA: TG + клуб KODA (без salebot) |
| Exp01 | ✓ | Режим B, author_id olga-kondratskaya |
| Exp02 | ✓ | Тон practice/DoD |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | ПДн, Share SA, approval write, injection |
| Ept02 | ✓ | Internal ×4: mcp-cursor…, google-sheets-api…, no-code, обезличивание |
| — | ✗ | Wordstat infra offline (−1) |
| — | ✗ | Объём plain вне контракта (−1 → 18/20; gate score <80) |

## Script reports

| Скрипт | Verdict | Файл |
|--------|---------|------|
| fact-check | PASS | fact-check-report.json |
| link-verify | PASS | link-verify.json |
| html-linter | PASS | html-linter-report.json |
| slop-detector | PASS | slop-detector-report.json |
| cannibalization | WARNING (portfolio B21↔B80) | cannibalization-report.json |
| utility gate (article) | PASS | utility-gate-report.json |

## Link verify

- total: 6, failed: 0
- OK: `/blog/mcp-cursor-finansist-instrumenty/`, `/blog/google-sheets-api-integraciya-finotdel/`, `/blog/avtomatizaciya-finansov-no-code/`, `/blog/obezlichivanie-dannyh-chatgpt-finansist/`, t.me/finance_modern, club.koda-fd.ru
- `--site-base https://koda-fd.ru`

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 2 (таблица + MCP-абзац)
- Flesch RU: 100.0 (Very Easy)
- verdict PASS

## Fact-check

- verdict: pass (6 extracted; 1 verified in fact-bank «2026»; 5 unverified = «2 часов», 300/400/403/429 — HTTP/длительности, не выдуманные % спроса)

## Cannibalization

- global verdict: warning (B21↔B80 overlap 75%, не затрагивает B92)
- B92: primary «mcp google sheets cursor» — не duplicate соседних

## Utility gate

- article: PASS (`action_markers=18`, numbered steps=17, faq_h3=7, tables=1, h2=7)
- note: gate смотрит `meta.char_count` и не ловит ошибку измерения HTML vs plain

## Fix cycle

- cycle 0 (writer 2026-09-12): trim HTML `len` → 9313; meta_ab OK
- cycle 1 (geo-qa): **FAIL** — plain ~7216 < 8500; article.html не правился geo-qa (нужен writer FIX)

## GEO QA agent (2026-09-12)

- agent: excalibur-blog-geo-qa
- gates scripts: utility ✓ | linter ✓ | slop ✓ | link-verify ✓ | fact-check ✓ | cannibalization (B92) ✓
- contract volume: **FAIL**
- verdict: **FAIL** — cover/schema **не** запускать; вернуть writer

## Schema ready (handoff для schema-агента)

BlogPosting: blocked until PASS | FAQPage: yes (7) | HowTo: yes | Review: no | author_id: olga-kondratskaya
