# QA: B43 limity-rashodov-telegram-alert

date: 2026-08-03
score_total: 87/100
core_eeat_lite: 17/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 18 | H2 по карточке, FAQ 6, primary в лиде |
| GEO / citability | 25 | 22 | Answer-first lead, table/ol/blockquote, без TOC/TL;DR |
| CORE-EEAT lite | 15 | 13 | 17/20; Olga voice, mode B |
| Human voice | 15 | 15 | Практичный тон, 0 salebot, 0 emdash |
| Fact safety | 15 | 13 | Без выдуманных цен и процентов рынка |
| Contract HTML | 10 | 9 | linter PASS, объём 8901, CTA club+tg |

**Порог PASS:** >=80, CORE-EEAT >=16/20, link-verify pass, utility gate pass — **выполнен**.

## Script reports

| Скрипт | Verdict |
|--------|---------|
| html-linter | PASS |
| slop-detector | PASS |
| utility gate | PASS |
| cannibalization | PASS (manual) |

## Notes

- CTA: club.koda-fd.ru + t.me/finance_modern only; salebot forbidden
- Cover: gradient_abstract via GenerateImage, 1536x1024, no text on PNG
- Internal links: avtomatizaciya-finansov-no-code, obezlichivanie-dannyh-chatgpt-finansist
