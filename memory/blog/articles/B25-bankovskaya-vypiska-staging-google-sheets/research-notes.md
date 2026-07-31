# Research notes — B25

**topic_id:** B25  
**slug:** bankovskaya-vypiska-staging-google-sheets  
**h1:** Как разложить банковскую выписку в staging-таблицу без ручного копипаста  
**research_date:** 2026-07-31  
**publish_target:** сайт koda-fd.ru/blog (+ Дзен по оркестрации)  
**utility_gate:** PASS (`how_to`, mode B)  
**related_published:** `/ot-excel-k-fin-konturu-30-dney/`, `/python-finansist-sverka-csv/`, `/google-apps-script-finansist-obnovit-dannye/`, `/vygruzka-1c-excel-odata/`  
**related_planned:** B26 plan-fakt-dds-google-sheets (следующий шаг после staging)

---

## utility_verdict

**PASS** — тема utility-only how_to. Читатель получает рабочий контур: банк → сырой файл → лист staging с каноном колонок → дедуп/hash → чистый факт для ДДС/сверки. Не обзор PDF-конвертеров, не продажа шаблона за 4000 ₽, не настройка ДиректБанка «вместо» staging, не курс Power Query с нуля.

---

## reader_outcome

После гайда финансист сможет выгрузить выписку (CSV/Excel) из клиент-банка, положить её на отдельный лист `raw`/`staging` в Google Sheets (или Excel), привести колонки к единому формату (дата, сумма, контрагент, назначение, account_id, hash), отсечь дубли и не править исходный файл руками — дальше скормить факт в ДДС/сверку.

---

## action_outline

1. **Зафиксировать боль и DoD** — копипаст из выписки ломает формулы и даёт дубли; цель: один staging-лист + сверка итога с банком за 1 прогон.
2. **Выбрать канал файла** — CSV/Excel из интернет-банка (предпочтительно); PDF только через конвертацию + ручная проверка; не слать выписку в публичные AI-конвертеры с ПДн.
3. **Создать структуру книги** — листы: `raw_import` (грязный импорт), `staging` (канон), `dict_categories` (опционально), позже — Факт/ДДС (ссылка на B26).
4. **Импорт без копипаста** — Google Sheets: Файл → Импорт → на `raw_import` (Replace sheet); Excel: Power Query «Из файла» / «Из папки». Отключить автоконвертацию дат/чисел при первом импорте.
5. **Канон колонок staging** — `date`, `amount`, `direction` (in/out), `counterparty`, `purpose`, `account_id`, `bank`, `source_file`, `row_hash` (дата+сумма+назначение+счёт).
6. **Нормализация** — разделитель `;`/`,`; кодировка UTF-8 / Windows-1251; даты → ISO `YYYY-MM-DD`; суммы → число с `.` как decimal; назначение `TRIM`.
7. **Дедуп и контроль** — уникальность по `row_hash`; не править `raw_import` вручную; сверка Σ приход/расход/остаток с файлом банка; журнал «какой файл когда загружен».
8. **Автоповтор (опционально)** — Drive-папка + Apps Script (офиц. sample Import CSV) или Power Query «Обновить всё»; несколько счетов = `account_id` в каждой строке.
9. **Куда дальше** — staging → план-факт ДДС (B26) / сверка двух CSV (B19) / кнопка «Обновить» (B22); 1С:ДиректБанк — отдельный контур бухучёта, не замена staging для управленки.

---

## Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT AUTH WARNING:** Токен Wordstat устарел / сервер MCP `user-mcp-kv` в этой сессии **не подключён** (в каталоге MCP нет инструментов `wordstat_*`). Точные показы/мес **не получены** и **не выдуманы**. Обновите токен через: https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

**Экспертная семантика (без цифр спроса) — LSI для копирайтера:**

| Кластер | Фразы | Роль |
| --- | --- | --- |
| Primary | банковская выписка в excel автоматически, загрузка выписки excel | H1/лид |
| Sheets | загрузка выписки в google sheets, импорт csv google таблицы | H2 импорт |
| Staging | staging таблица финансы, сырой импорт выписки, нормализация выписки | H2 канон |
| 1С angle | нормализация выписки 1с, директбанк выписка, клиент банк txt | FAQ / граница контуров |
| Tech | power query из папки, apps script csv drive, дедуп hash транзакции | H2 автоповтор |
| Pain | копипаст выписки, дубли платежей таблица, кодировка csv 1251 | Лид / ошибки |

**SEO-вывод:** SERP по primary забит **PDF→Excel конвертерами** и платными шаблонами. Угол КОДА: **staging-слой с каноном колонок и дедупом** между банком и отчётом — не «конвертировать PDF» и не «купить шаблон Cash Flow».

---

## SERP (WebSearch Cursor, 31.07.2026)

`research-serp.json` preflight: много нерелевантных PDF-конвертеров / AI-генераторов выписок — **не копировать структуру**. Приоритет: WebSearch ниже.

### Primary — «банковская выписка в excel автоматически»

| # | URL | Тип | Пробел для КОДА |
| --- | --- | --- | --- |
| 1 | https://www.helpexcel.pro/table-bank-statement/ | Платный шаблон 4000 ₽ (Сбер/Альфа/Тинькофф → ДДС) | Продажа, нет DIY staging-канона |
| 2 | https://statementtocsv.com/ru/ и аналоги | PDF→CSV/Excel SaaS | Риск утечки ПДн; нет финконтура |
| 3 | https://www.coderstar.ru/obrabotki/zagruzka-vypiski/ | Excel → документы 1С | Бухучёт 1С, не Sheets staging |
| 4 | https://bankfeeds.1commerce.ru/bank-statements | API/почта/папка → 1С | Enterprise 1С, не управленческий staging |
| 5 | https://learn.microsoft.com/ru-ru/power-query/connectors/folder | Офиц. Power Query «Из папки» | Техдока без фин-сценария выписки |

### Secondary — Google Sheets + staging

| # | URL | Тип | Пробел для КОДА |
| --- | --- | --- | --- |
| 6 | https://rko.by/tri-sposoba-vygruzki-bankovskikh-vypisok-v-google-sheets-i-excel | 3 способа: файл / e-mail / API | РКО BY; мало про hash/дедуп/канон |
| 7 | https://www.expensesorted.com/blog/bank-csv-import-google-sheets-guide-2025 | EN: Raw Import → Cleaned → Categories | Близко к staging; EN + личный бюджет |
| 8 | https://www.rocketstatements.com/blog/bank-statements-to-google-sheets-2026-beginners-guide-to-live-bank-sync-csv-imports-header-mapping-and-fixing-duplicates | EN 2026: staging + dedupe | SaaS-угол; полезны header mapping |
| 9 | https://developers.google.com/apps-script/samples/automations/import-csv-sheets | Офиц. sample: CSV из Drive → Sheets | Нет банковского канона колонок |
| 10 | https://smoothsheet.com/blog/use-cases/import-bank-statements-google-sheets/ | CSV-first для бухгалтеров | Нет RU банков / 1С границы |

### Secondary — 1С / нормализация

| # | URL | Тип | Пробел для КОДА |
| --- | --- | --- | --- |
| 11 | https://buh.ru/news/samoe-novoe-v-1s-bukhgalterii-8-poluchenie-vypiski-banka-po-raspisaniyu.html | ДиректБанк по расписанию с 3.0.125 | Бухучёт; упомянуть как «другой контур» |
| 12 | https://buh.ru/news/samoe-novoe-v-1s-bukhgalterii-8-nastroyki-avtomaticheskogo-polucheniya-bankovskoy-vypiski-cherez-1s-.html | Расписание + автосоздание справочников | Не Sheets |
| 13 | https://infostart.ru/journal/news/mir-1s/avtozagruzka-vypiski-v-1s-kak-ubrat-ruchnuyu-obrabotku-platezhek-i-poisk-schetov_2631010/ | Правила разнесения в 1С | Не управленческий staging |

### Угол КОДА (дифференциация)

**Банк → raw → staging (канон + hash) → ДДС/сверка**, без копипаста и без обещания «проводки в 1С одной кнопкой». Staging — промежуточный слой для управленки в Sheets/Excel; 1С остаётся контуром бухучёта.

---

## Таблица фактов

| # | Утверждение | Источник | Дата проверки |
| --- | --- | --- | --- |
| 1 | Офиц. Apps Script sample импортирует CSV из папки Drive в одну таблицу по time-driven trigger; после успеха файлы переносятся в processed, чтобы не дублировать. | https://developers.google.com/apps-script/samples/automations/import-csv-sheets | 2026-07-31 |
| 2 | По умолчанию sample снимает header-строку каждого CSV перед append в конец листа; шлёт summary e-mail. | тот же | 2026-07-31 |
| 3 | Power Query Desktop: соединитель «Папка» → путь → «Объединить и преобразовать данные» для файлов с одной схемой. | https://learn.microsoft.com/ru-ru/power-query/connectors/folder | 2026-07-31 |
| 4 | Объединение файлов в Power Query полезно для ежемесячных файлов одинаковой структуры; после настройки — обновление при появлении новых файлов в папке. | https://learn.microsoft.com/ru-ru/power-query/combine-files-overview | 2026-07-31 |
| 5 | Практический RU-гайд: форматы выгрузки банка CSV/OFX/MT940; для CSV — Apps Script из Drive или Power Query; на первой неделе сверять суммы. | https://rko.by/tri-sposoba-vygruzki-bankovskikh-vypisok-v-google-sheets-i-excel | 2026-07-31 |
| 6 | Типичные ошибки автоматизации выписок: разные поля у банков, пароли в открытом виде, часовые пояса, полная автоматизация без тестовой выборки, комиссии при сверке. | rko.by (там же) | 2026-07-31 |
| 7 | Рекомендуемая архитектура книги: отдельный лист Raw Import (грязные данные), не лить выписку сразу в master; затем Cleaned/staging формулами. | https://www.expensesorted.com/blog/bank-csv-import-google-sheets-guide-2025 | 2026-07-31 |
| 8 | При импорте CSV в Sheets часто советуют снять «Convert text to numbers, dates, and formulas», чтобы банк не «сломал» даты/длинные числа. | https://www.expensesorted.com/blog/bank-csv-import-google-sheets-guide-2025 ; https://help.loyverse.com/ru/help/how-open-csv-file-google-sheets | 2026-07-31 |
| 9 | RU-банки часто отдают CSV с `;` и кодировкой Windows-1251 / UTF-8 — разделитель и кодировку нужно задавать явно. | практика RU CSV + https://dasle.ru/import-dannyh-iz-csv-v-google-sheets-bystryy-sposob/ | 2026-07-31 |
| 10 | В 1С:Бухгалтерия 8 с версии 3.0.125 — получение выписки по расписанию через 1С:ДиректБанк (по умолчанию раз в час). | https://buh.ru/news/samoe-novoe-v-1s-bukhgalterii-8-poluchenie-vypiski-banka-po-raspisaniyu.html | 2026-07-31 |
| 11 | С версии 3.0.195 — расширенные настройки автозагрузки ДиректБанк: промежуточная/итоговая выписка, автосоздание справочников, проведение документов. | https://buh.ru/news/samoe-novoe-v-1s-bukhgalterii-8-nastroyki-avtomaticheskogo-polucheniya-bankovskoy-vypiski-cherez-1s-.html | 2026-07-31 |
| 12 | Платный конкурент helpexcel.pro: шаблон ~4000 ₽, чтение выписок из папки Drive, статьи ДДС по ИНН/комментарию, архив обработанных файлов. | https://www.helpexcel.pro/table-bank-statement/ | 2026-07-31 |
| 13 | EN-гайд 2026: staging sheet + единый header (Date, Description, Amount, Balance, Account) + dedupe по Date+Description+Amount до pivot. | https://www.rocketstatements.com/blog/bank-statements-to-google-sheets-2026-beginners-guide-to-live-bank-sync-csv-imports-header-mapping-and-fixing-duplicates | 2026-07-31 |
| 14 | `IMPORTDATA` не подходит для банковских порталов (нет публичного URL) — нужен скачанный CSV или API/интегратор. | https://smoothsheet.com/blog/use-cases/import-bank-statements-google-sheets/ | 2026-07-31 |
| 15 | Внутренние мосты: сверка двух CSV — `/python-finansist-sverka-csv/`; кнопка обновления Sheets — `/google-apps-script-finansist-obnovit-dannye/`; OData 1С — `/vygruzka-1c-excel-odata/`. | shared/published-articles.md | 2026-07-31 |

**Fact-bank:** релевантных строк по выпискам/staging нет — цифры спроса и «экономия N часов» без источника **не утверждать**. Допустима качественная формулировка «убрать копипаст» без выдуманных %.

---

## Рекомендации writer (mode B)

### Lead
Боль: выписка из клиента-банка каждый день копируется в «мастер» → плывут даты, двоятся платежи, формулы ДДС красные. Ответ: staging-слой с каноном колонок и hash. Результат: один прогон импорта + сверка итога с банком.

### H2-скелет (не копировать конкурентов)
1. Зачем staging между банком и отчётом (не править сырой файл)
2. Какой файл брать: CSV/Excel vs PDF vs ДиректБанк (граница контуров)
3. Листы книги: `raw_import` → `staging` → (позже Факт)
4. Канон колонок + пример `row_hash`
5. Импорт в Google Sheets / альтернатива Power Query без копипаста
6. Ловушки: `;` / 1251 / автодаты / комиссии / несколько счетов
7. Дедуп, журнал файлов, сверка Σ
8. Автоповтор: Drive + Apps Script или «Обновить» в Excel
9. Куда дальше: ДДС / сверка / кнопка обновить

### Workflow-схема (обязательна в статье)
`Клиент-банк (CSV/Excel) → raw_import → нормализация → staging (+ hash) → Факт ДДС / сверка`  
Параллельно (не смешивать): `Банк ↔ 1С:ДиректБанк` = бухучёт.

### FAQ hints
1. Подойдёт ли выписка из клиента-банка? — Да, если есть CSV/Excel; PDF — хуже, нужна конвертация + проверка.
2. Несколько счетов? — Колонка `account_id` / `bank` в каждой строке; отдельные raw или один staging с фильтром.
3. Это замена 1С? — Нет. Staging для управленки/ДДС; ДиректБанк — контур проводок.
4. Можно ли Excel вместо Sheets? — Да: Power Query из файла/папки; канон колонок тот же.
5. Как не задвоить платежи? — `row_hash` + не трогать raw; processed-папка для скрипта.
6. Безопасно ли онлайн-конвертер PDF? — Для юрлиц с ПДн/реквизитами — не рекомендуем; локально или банк CSV.
7. Куда дальше после staging? — План-факт ДДС; сверка с 1С/реестром (B19); кнопка «Обновить» (B22).

### CTA / interlink
- `/ot-excel-k-fin-konturu-30-dney/` — рамка контура  
- `/python-finansist-sverka-csv/` — сверка staging vs другая выгрузка  
- `/google-apps-script-finansist-obnovit-dannye/` — автообновление  
- Не более 3 CTA; польза > продажа

### Cover hint
abstract bank data stream into table grid dark holographic, no text

### Cannibalization
Не дублировать B19 (pandas сверка двух CSV) и B22 (кнопка Apps Script) — здесь фокус на **раскладке одной выписки в staging**. B26 (план-факт) — «следующий шаг», не раскрывать формулами SUMIFS.

---

## wordstat_status

**warning** — MCP `user-mcp-kv` недоступен; цифры показов отсутствуют.
