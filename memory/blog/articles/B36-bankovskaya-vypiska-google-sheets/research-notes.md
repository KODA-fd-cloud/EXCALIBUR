# Research notes — B36

**topic_id:** B36  
**slug:** bankovskaya-vypiska-google-sheets  
**h1:** Как забирать банковскую выписку в Google Sheets без 1С: CSV, API, расписание  
**research_date:** 2026-08-03  
**publish_target:** koda-fd.ru/blog  
**utility_gate:** PASS (`how_to`, mode B)  
**related_published:** `/avtomatizaciya-finansov-no-code/`, `/obezlichivanie-dannyh-chatgpt-finansist/`  
**internal_links (карточка):** `/avtomatizaciya-finansov-no-code/`, `/obezlichivanie-dannyh-chatgpt-finansist/`  
**cover_scene_hint:** abstract holographic finance automation dark #0a0a0f purple #8b5cf6, no text

---

## utility_verdict

**PASS** — тема utility-only how_to. Читатель выбирает маршрут (CSV / e-mail / API), настраивает staging-лист, импортирует выписку в Google Sheets без 1С, ставит расписание Apps Script и проверяет первую неделю вручную. Не обзор «что такое выписка», не ChatGPT-сверка, не PDF-конвертеры.

---

## reader_outcome

После гайда финансист без 1С сможет выбрать способ загрузки (CSV из клиент-банка, вложение с почты или T-API/Sber API), настроить staging-таблицу с дедупом, автоматизировать ежедневный импорт через Apps Script и time-driven trigger, а токены банка хранить в Script Properties — не в ячейках.

---

## action_outline

1. **Когда нужно / когда нет** — мало операций → ручной CSV; несколько счетов или ежедневный ДДС → автоматизация; есть 1С с DirectBank → это другой пайплайн (не эта статья).
2. **Staging-лист** — колонки: `date`, `amount`, `counterparty`, `purpose`, `account`, `hash` (дата+сумма+назначение); отдельный лист `raw_import` «только append».
3. **Маршрут A: CSV** — выгрузка из клиент-банка (CSV/Excel) → папка Google Drive → Apps Script `Utilities.parseCsv()` → append в staging; перенос обработанных файлов в `processed/`.
4. **Маршрут B: e-mail** — фильтр писем банка → `GmailApp.search` + `Utilities.parseCsv(attachment)` → тот же staging; звёздочка/метка «обработано».
5. **Маршрут C: T-API (Т-Бизнес)** — токен в ЛК «Счета и выписки» → `GET /api/v1/statement` через `UrlFetchApp` → маппинг JSON в строки staging; пагинация через `nextCursor`.
6. **Маршрут D: Sber API** — заявка + scope `MCP_STATEMENT`; метод `statement.get_rur_transactions`; лимит ~5 req/s; для Sheets — тот же UrlFetchApp + OAuth access_token (тяжелее старт, описать как «если уже подключены»).
7. **Расписание** — `ScriptApp.newTrigger(...).timeBased().everyDays(1).atHour(7)`; не более 20 triggers/script; consumer: 90 min trigger runtime/день, Workspace: 6 hr.
8. **Проверка недели 1** — сверка 5 первых строк с клиент-банком; журнал ошибок на листе `log`; учёт комиссий и кодировки (`;`, CP1251 → UTF-8).
9. **Безопасность** — токены только `PropertiesService.getScriptProperties()`; не грузить сырые ИНН/счета в ChatGPT; см. `/obezlichivanie-dannyh-chatgpt-finansist/`; отдельный сервисный аккаунт Google.

---

## Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT AUTH WARNING:** сервер MCP `user-mcp-kv` в этой Cloud-сессии **не подключён** (доступен только `cursor-cloud`). Вызов `wordstat_get_top_requests` **не выполнен**. Точные показы/мес **не получены** и **не выдуманы**.

Обновление токена: https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

**Экспертная семантика (LSI для writer, без цифр спроса):**

| Кластер | Фразы |
| --- | --- |
| Ядро | банковская выписка google sheets, загрузка выписки в google таблицы, выгрузка банка в sheets |
| CSV / файл | импорт csv google sheets, банковская выписка csv, клиент банк выгрузка excel |
| Автоматизация | google apps script банковская выписка, автоматический импорт csv drive, триггер по времени google sheets |
| API RU | тинькофф api выписка, t-api statement, сбер api выписка, directbank без 1с |
| Финконтур | staging таблица финансы, ддс google sheets без 1с, сверка выписки таблица |
| No-code | make n8n банковская выписка (упомянуть как альтернатива, не основной фокус) |

**SEO-вывод:** SERP смешанный — конвертеры PDF (StatementSheet, RocketStatements), ChatGPT-сверка (fin-academy), белорусский гайд rko.by. Угол КОДА: **российский финотдел без 1С**, три рабочих маршрута + расписание + безопасность ПДн. Не конкурировать с PDF-OCR и не дублировать B25 (staging-детали) / B35 (n8n-сверка).

---

## SERP (WebSearch Cursor, 03.08.2026)

| # | URL | Тип | Пробел / угол КОДА |
| --- | --- | --- | --- |
| 1 | https://rko.by/tri-sposoba-vygruzki-bankovskikh-vypisok-v-google-sheets-i-excel | how_to (BY) | Хорошая тройка CSV/e-mail/API, но контекст РБ; нет T-API/Sber, нет квот GAS |
| 2 | https://blog.fin-academy.pro/bankovskaya-sverka-chatgpt-avtomatizatsiya | GPT-сверка | Другой intent — не «забрать выписку» |
| 3 | https://www.rocketstatements.com/blog/convert-bank-statements-to-google-sheets-2026-5-methods-compared-free-template | EN comparison | PDF→Sheets, не RU банки |
| 4 | https://developers.google.com/apps-script/samples/automations/import-csv-sheets | оф. sample | Канон CSV+trigger; нет банковских полей |
| 5 | https://developer.tinkoff.ru/docs/api/get-api-v-1-statement | API docs | T-API statement — взять в гайд |
| 6 | https://developers.sber.ru/docs/ru/sber-api/mcp/mcp-statement | API docs | Sber MCP statement — кратко для ЮЛ |
| 7 | https://saldovka.com/2026-exp/bankovskie-vypiski-v-1s-8-3.html | 1С | DirectBank vs файл — контраст «без 1С» |
| 8 | https://koda-fd.ru/blog/avtomatizaciya-finansov-no-code/ | свой блог | internal CTA / контекст no-code |

**Кannibalization:** B25 (staging), B22 (кнопка Apps Script), B35 (n8n сверка), B28 (сверка без ПДн) — перелинковка, не копировать H2 1:1.

---

## Таблица фактов

| # | Утверждение | Источник | Дата проверки |
| --- | --- | --- | --- |
| 1 | Google sample «Import CSV data» создаёт time-driven trigger, парсит CSV из папки Drive, append в лист, переносит файлы в processed и шлёт summary e-mail. | https://developers.google.com/apps-script/samples/automations/import-csv-sheets | 2026-08-03 |
| 2 | `Utilities.parseCsv()` + `sheet.getRange(...).setValues(data)` — базовый паттерн импорта CSV в Sheets. | https://spreadsheet.dev/how-to-import-csv-files-into-google-sheets-using-apps-script | 2026-08-03 |
| 3 | UrlFetchApp: 20 000 вызовов/день (consumer), 100 000/день (Google Workspace). | https://developers.google.com/apps-script/guides/services/quotas | 2026-08-03 |
| 4 | Trigger total runtime: 90 min/день (consumer), 6 hr/день (Workspace). | https://developers.google.com/apps-script/guides/services/quotas | 2026-08-03 |
| 5 | Макс. runtime одного запуска скрипта: 6 минут (consumer и Workspace). | https://developers.google.com/apps-script/guides/services/quotas | 2026-08-03 |
| 6 | Лимит installable triggers: 20 на пользователя на скрипт. | https://developers.google.com/apps-script/guides/services/quotas | 2026-08-03 |
| 7 | T-API `GET /api/v1/statement`: данные с июня 2023; limit 1–5000 (default 1000); пагинация `nextCursor`; RPS ≤ 20. | https://developer.tinkoff.ru/docs/api/get-api-v-1-statement | 2026-08-03 |
| 8 | T-API token выпускается в ЛК Т-Бизнес → Интеграции; действует 90 дней без использования, при регулярном использовании — бессрочно. | https://developer.tinkoff.ru/docs/intro/manuals/self-service-auth | 2026-08-03 |
| 9 | T-API: для statement нужен scope «Счета и выписки → Информация об операциях компании». | https://developer.tinkoff.ru/docs/products/account-info | 2026-08-03 |
| 10 | Sber API statement: scope `MCP_STATEMENT`; лимит ~5 запросов/сек; выписка по рублёвому счёту за 5 лет + текущий год. | https://developers.sber.ru/docs/ru/sber-api/mcp/mcp-statement | 2026-08-03 |
| 11 | Клиент-банк РФ часто выдаёт 1CClientBankExchange (.txt), не CSV — для Sheets нужен CSV/Excel или парсер txt (упомянуть как ловушку). | https://saldovka.com/2026-exp/bankovskie-vypiski-v-1s-8-3.html | 2026-08-03 |
| 12 | DirectBank (Сбер, ВТБ, Т-Банк и др.) — прямой обмен с 1С; для «без 1С» остаются файл/API/e-mail. | https://saldovka.com/2026-exp/bankovskie-vypiski-v-1s-8-3.html | 2026-08-03 |
| 13 | Типичные ошибки автоматизации: разный формат колонок, часовые пояса, комиссии банка, пароли в открытом коде. | https://rko.by/tri-sposoba-vygruzki-bankovskikh-vypisok-v-google-sheets-i-excel | 2026-08-03 |
| 14 | E-mail-сценарий: фильтр писем банка → парсинг CSV-вложений → отдельный ящик для обработки + ручная верификация неделю 1. | https://rko.by/tri-sposoba-vygruzki-bankovskikh-vypisok-v-google-sheets-i-excel | 2026-08-03 |
| 15 | ISO 8601 для дат в T-API запросах/ответах (UTC). | https://developer.tinkoff.ru/docs/api/get-api-v-1-statement | 2026-08-03 |

---

## FAQ hints (кандидаты)

1. **Можно ли без программиста?** — CSV + готовый sample Google: да; API банка — базовый Apps Script по шаблону; Sber API — обычно нужна помощь с OAuth.
2. **Сколько займёт внедрение?** — CSV+trigger: один вечер; T-API: 1–2 дня с тестами; Sber API: от заявки в банке.
3. **Какие риски для данных?** — облако Google, токены в Properties, не отправлять сырые выписки в LLM; см. internal `/obezlichivanie-dannyh-chatgpt-finansist/`.
4. **Банк отдаёт только .txt для 1С?** — экспортируйте CSV/Excel если есть; иначе промежуточный парсер или другой банк-канал (API).
5. **Нужен ли 1С?** — нет, статья про Sheets как финконтур; 1С — опционально позже.
6. **Make/n8n вместо Apps Script?** — да для оркестрации; Apps Script — нулевая инфра внутри таблицы (ссылка на `/avtomatizaciya-finansov-no-code/`).
7. **Как не задвоить операции?** — колонка `hash` + проверка перед append; processed-папка для CSV.
8. **Лимиты Google сломают импорт?** — при >20k UrlFetch/день или длинных выгрузках — chunk + Properties cursor (T-API `nextCursor`).

---

## Writer notes

- **author_id:** olga-kondratskaya  
- **article_mode:** B — минимум 5 нумерованных шагов + таблица сравнения маршрутов (CSV / e-mail / T-API / Sber API).  
- **CTA (conversion-map):** клуб KODA ≤2, Telegram ≤2, koda-fd.ru ≤1; UTM `?utm_source=blog&utm_medium=article&utm_campaign=bankovskaya-vypiska-google-sheets`  
- **Не обещать:** автопроводки в бухучёт, «100% без ошибок парсинга», работу всех банков из коробки.  
- **H2 из карточки** заменить на практические блоки из action_outline (карточка scout — шаблонные заголовки).  
- **Код:** псевдо/фрагменты Apps Script (importCsvFromDrive, fetchTinkoffStatement, installDailyTrigger) — без полных токенов.  
- **Связка с B25:** после staging → нормализация/ДДС (одна фраза + будущая перелинковка).

---

## Cover hint

abstract holographic finance automation dark #0a0a0f purple #8b5cf6, no text
