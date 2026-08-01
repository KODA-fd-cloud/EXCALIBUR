# QA: B30 power-query-finansist-obnovlenie

date: 2026-08-01
score_total: 87/100
core_eeat_lite: 17/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 18 | H2 по карточке B30, FAQ 6, primary в лиде |
| GEO / citability | 25 | 22 | Answer-first lead, table/ol, workflow blockquote |
| CORE-EEAT lite | 15 | 13 | 17/20; Olga voice, fin analogies |
| Human voice | 15 | 15 | mode B, 0 salebot, практические рекомендации |
| Fact safety | 15 | 13 | без выдуманных цифр, осторожные формулировки по Online/Mac |
| Contract HTML | 10 | 9 | объём 8500+, linter-ready, CTA club+tg |

**Порог PASS:** >=80, CORE-EEAT >=16/20, utility gate pass — **выполнен**.

## Script reports

| Скрипт | Verdict |
|--------|---------|
| fact-check | PASS (manual review) |
| link-verify | PASS (internal /blog/ paths) |
| html-linter | PASS (contract tags) |
| slop-detector | PASS |
| cannibalization | PASS (distinct slug B30) |
| utility gate | PASS (how_to, mode B, 5+ steps) |

## Notes

- CTA: club.koda-fd.ru + t.me/finance_modern only; salebot forbidden
- Cover: gradient_abstract via GenerateImage, no text on image
- article_mode: B; no emdash; no publish in this run
