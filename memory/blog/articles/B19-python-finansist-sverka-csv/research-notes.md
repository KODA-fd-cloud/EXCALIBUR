# Research notes — B19

**topic_id:** B19  
**slug:** python-finansist-sverka-csv  
**h1:** Как начать с Python для финансиста: сверка двух CSV без зависания Excel  
**research_date:** 2026-07-22  
**publish_target:** сайт koda-fd.ru/blog (+ Дзен по оркестрации)  
**utility_gate:** PASS (`how_to`, mode B)  
**related_published:** `/claude-code-finotdel/`, `/vibe-coding-finansist/`, `/cursor-finansist-skript-dashbord/` (B20)

---

## utility_verdict

**PASS** — тема utility-only how_to. Читатель получает рабочий маршрут: понять, когда Excel уже не тянет две выгрузки; поставить Python и запустить первый скрипт в Cursor; сверстать сверку двух CSV (ключ, суммы, отчёт расхождений); закрыть типичные ошибки кодировки/разделителя/типов; зафиксировать папку проекта для повторных прогонов. Не курс «Python с нуля 40 часов», не датасаенс, не «топ библиотек 2026».

---

## reader_outcome

После гайда финансист сможет установить Python, открыть папку пилота в Cursor, прогнать pandas-скрипт сверки двух CSV и получить файл расхождений (`left_only` / `right_only` / разница сумм) без зависания Excel на больших выгрузках.

---

## action_outline

1. **Зафиксировать боль и DoD** — две выгрузки (банк vs 1С / маркетплейс vs внутренняя) висят в Excel; цель: скрипт + `out/diffs.csv` за минуты.
2. **Поставить Python + pandas** — python.org / winget; `pip install pandas`; проверить `python -c "import pandas; print(pandas.__version__)"`.
3. **Собрать папку пилота** — `data/` (обезличенные CSV), `scripts/`, `out/`, `.gitignore`; открыть в Cursor.
4. **Написать сверку** — `read_csv` → нормализация ключа → `merge(how="outer", indicator=True)` → фильтр расхождений → сравнение сумм → `to_csv("out/diffs.csv")`.
5. **Прогнать и проверить глазами** — 3–5 строк из `both` и все `left_only`/`right_only`; сверка итога сумм.
6. **Закрыть типичные ошибки** — `encoding=cp1251` / `utf-8-sig`, `sep=";"`, `decimal=","`, ключ как строка (`dtype=str`), пробелы `strip()`.
7. **Повторяемый запуск** — тот же скрипт на свежие файлы; без ПДн в чат; мост к B20 (дашборд) и Claude Code.

---

## Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT SKIP WARNING:** сервер MCP `user-mcp-kv` в этой сессии **не подключён** (в каталоге MCP нет инструментов `wordstat_*`). Точные показы/мес **не получены** и **не выдуманы**. Обновите токен / подключите MCP-KV: https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

**Экспертная семантика (без цифр спроса) — LSI для копирайтера:**

| Кластер | Фразы | Роль |
| --- | --- | --- |
| Primary | как начать python для финансиста, python для финансиста | H1/лид |
| Reconcile | сверка csv python, сверка двух таблиц pandas, сравнить два csv | H2 сверка |
| Stack | pandas сверка таблиц, merge outer indicator, _merge left_only | H2 код |
| Excel angle | python excel финансы, excel зависает большая таблица | Лид/боль |
| Setup | установить python windows, pip install pandas | H2 установка |
| Errors | csv кодировка cp1251, разделитель точка с запятой, decimal запятая | H2 ошибки |

**SEO-вывод:** SERP по «python для финансиста» уходит в курсы/моделирование/«стать продуктивнее». Угол КОДА: **первая рабочая сверка двух CSV** (ключ + суммы + отчёт), не учебник синтаксиса и не DCF-модель.

---

## SERP (WebSearch Cursor, 22.07.2026)

`research-serp.json` preflight: **0 результатов** по всем запросам — игнорируем. Приоритет: WebSearch ниже.

### Primary / «python для финансиста»

| # | URL | Тип | Пробел для КОДА |
| --- | --- | --- | --- |
| 1 | https://habr.com/ru/articles/1005114/ | Habr: pandas CSV→аналитика | Есть RU sep `;` / 1С, нет DoD сверки банк/1С |
| 2 | https://sf.education/blog/python-v-finansovom-modelirovanii | Курсы: финмоделирование | Jupyter + EBITDA, не reconcile CSV |
| 3 | https://kurshub.ru/journal/blog/python-dlya-finansov-prostoj-sposob-stat-produktivnee/ | Обзор «Python в финансах» | Вода + курс, нет шагов сверки |
| 4 | https://qna.habr.com/q/1249184 | Q&A: сравнить 2 больших CSV | `equals`/построчно, не outer+indicator+отчёт сумм |

### Secondary / сверка + merge

| # | URL | Тип | Пробел для КОДА |
| --- | --- | --- | --- |
| 5 | https://pandas.pydata.org/docs/reference/api/pandas.merge.html | Офиц. docs 3.0.4 | Нет фин-сценария |
| 6 | https://kariernik.ru/blog/merge-pandas-shpargalka | RU шпаргалка merge + сверка | Есть `indicator`, нет установки Python/Cursor |
| 7 | https://habr.com/ru/companies/otus/articles/913736/ | OTUS: грабли merge | Дубли/типы — полезно в H2 ошибок |
| 8 | https://note.nkmk.me/en/python-pandas-merge-join/ | EN merge/join | Технический reference |

### Encoding / RU CSV

| # | URL | Тип | Пробел для КОДА |
| --- | --- | --- | --- |
| 9 | https://runebook.dev/ru/docs/pandas/reference/api/pandas.read_csv | RU: encoding/sep/dtype | Нет связки со сверкой |
| 10 | https://pythonlib.ru/post58 | CSV/Excel запись | Общий гайд |

### Конкурентный зазор (serp_gap)

1. **Финансист + две выгрузки + отчёт расхождений** — не «урок 1: переменные», не DCF.
2. Явные **RU-грабли**: `;`, cp1251, запятая в числах, ключ-строка (ведущие нули).
3. Граница с **B20**: здесь — первый Python + сверка; B20 — Cursor-вечер со скриптом+дашбордом.
4. Безопасность: обезличенные CSV, без сырых ИНН/ФИО в чат (→ B11).
5. DoD: `out/diffs.csv` с `left_only` / `right_only` / дельтой сумм — этого нет у курсов «Python для финансов».

---

## Таблица фактов (только с URL; для writer)

| # | Утверждение | Источник | Дата проверки |
| --- | --- | --- | --- |
| 1 | `pandas.merge` / `DataFrame.merge`: `how` включает left/right/outer/inner/cross; в docs 3.0.4 также left_anti/right_anti. | https://pandas.pydata.org/docs/reference/api/pandas.merge.html | 2026-07-22 |
| 2 | `indicator=True` добавляет колонку `_merge` со значениями `left_only`, `right_only`, `both`. | https://pandas.pydata.org/docs/reference/api/pandas.merge.html | 2026-07-22 |
| 3 | Актуальная версия документации pandas на момент проверки — **3.0.4**. | https://pandas.pydata.org/docs/reference/api/pandas.merge.html | 2026-07-22 |
| 4 | Паттерн сверки: `how='outer', indicator=True`, затем `merged[merged['_merge'] != 'both']`. | https://kariernik.ru/blog/merge-pandas-shpargalka | 2026-07-22 |
| 5 | Тот же паттерн + `.query("_merge != 'both'")` как тест на orphan-строки. | https://habr.com/ru/companies/otus/articles/913736/ | 2026-07-22 |
| 6 | В РФ CSV часто `sep=';'` (запятая занята десятичным разделителем) и `encoding='cp1251'`. | https://runebook.dev/ru/docs/pandas/reference/api/pandas.read_csv | 2026-07-22 |
| 7 | Habr: выгрузки из 1С / русской Excel часто с `;` — без `sep` pandas свалит всё в одну колонку. | https://habr.com/ru/articles/1005114/ | 2026-07-22 |
| 8 | `dtype` для ключей-ID как строк предотвращает потерю ведущих нулей. | https://runebook.dev/ru/docs/pandas/reference/api/pandas.read_csv | 2026-07-22 |
| 9 | Несовпадение типов ключа (object vs int) ломает outer merge — ключи не схлопываются. | https://stackoverflow.com/questions/34161870/merging-two-pandas-data-frames-in-python-using-outer-merge-not-identifying-ident | 2026-07-22 |
| 10 | Дубли ключей на одной стороне дают fan-out (декартово размножение) — чистить/validate до merge. | https://habr.com/ru/companies/otus/articles/913736/ | 2026-07-22 |
| 11 | Cursor удобен как среда запуска/правки скрипта (связь с B20). | internal / published B20 | 2026-07-22 |
| 12 | Обезличивание перед облачным ИИ — отдельный гайд B11. | /blog/obezlichivanie-dannyh-chatgpt-finansist/ | 2026-07-22 |

**Не использовать без источника:** конкретные «Excel падает после N строк», цены курсов, «% финансистов учат Python».

---

## Угол статьи (mode B)

Сцена: две выгрузки по 50–200 тыс. строк, Excel крутит вентилятор, VLOOKUP на полчаса. Ответ: 30–40 строк pandas + `out/diffs.csv` (ключ → суммы → отчёт). Голос «я», шаги, код в `<pre><code>`, без TL;DR. CTA: Telegram + клуб по conversion-map (≤2 каждый).

**Мини-скелет кода для writer (не копировать 1:1 у конкурентов):**

```
read_csv(A) + read_csv(B)
→ strip/astype(str) на ключе
→ merge(how="outer", on=key, indicator=True, suffixes=("_a","_b"))
→ amount_diff = amount_a - amount_b (где both)
→ diffs = filter left_only | right_only | abs(diff) > tol
→ to_csv("out/diffs.csv")
```

---

## FAQ hints → ответы-действия

1. Нужно ли знать программирование? — Нет курса; копируете скрипт, меняете имена колонок и пути к файлам.
2. Pandas обязателен? — Для сверки таблиц — да, стандарт; чистый csv+циклы дольше и хрупче.
3. Безопасно ли для 1С-файлов? — Только выгрузки/обезличенные срезы; не пароль к базе в скрипт/чат.
4. Excel всё же справится? — На малых объёмах иногда да; при зависании/повторах каждую неделю — скрипт.
5. Куда дальше? — B20 дашборд; Claude Code; повторный запуск на свежие CSV.
6. Windows vs Mac? — Один скрипт; на Windows чаще `py` launcher.
7. Ключи называются по-разному? — `left_on`/`right_on` или переименовать колонки до merge.

---

## Internal links

- `/claude-code-finotdel/`
- `/vibe-coding-finansist/`
- (мягко) `/cursor-finansist-skript-dashbord/` как next step
- `/obezlichivanie-dannyh-chatgpt-finansist/` в блоке безопасности

---

## Cover hint

abstract dual data streams merging nodes dark purple cyan, no text

---

## CTA (conversion-map)

| CTA | URL | Max |
| --- | --- | --- |
| Клуб KODA | https://club.koda-fd.ru/?utm_source=blog&utm_medium=article&utm_campaign=python-finansist-sverka-csv | 2 |
| Telegram | https://t.me/finance_modern?utm_source=blog&utm_medium=article | 2 |
| Сайт | https://koda-fd.ru/ | 1 |

Запрещено: `t.me/koda_salebot`.

---

## next_step

→ Writer (`excalibur-blog-writer`): `article.html` по контракту mode B, H2 из карточки B19, факты только из таблицы выше.
