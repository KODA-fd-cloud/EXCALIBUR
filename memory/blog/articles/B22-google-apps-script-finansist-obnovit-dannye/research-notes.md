# Research notes — B22

**topic_id:** B22  
**slug:** google-apps-script-finansist-obnovit-dannye  
**h1:** Как сделать кнопку «обновить данные» в Google Sheets через Apps Script  
**research_date:** 2026-07-22  
**publish_target:** сайт koda-fd.ru/blog (+ Дзен по оркестрации)  
**utility_gate:** PASS (`how_to`, mode B)  
**practice_source:** `D:\projects\1С\dds-sheets\html-dashboard` (`Code.gs`, `refreshFrom1C`, `doGet`/`doPost`, `INSTALL.md`)  
**related_published:** `/vygruzka-1c-excel-odata/`, `/avtomatizaciya-finansov-no-code/`

---

## utility_verdict

**PASS** — тема utility-only how_to. Читатель получает: зачем кнопка/меню вместо ручного CSV; первый скрипт `onOpen` + пункт меню; источники данных (Drive CSV / webhook / OData 1С); HTML-дашборд через `HtmlService` без отдельного сайта; права, триггеры, квоты и типичные поломки развёртывания. Не курс JS, не Marketplace add-on с нуля.

---

## reader_outcome

После гайда финансист сможет привязать Apps Script к таблице, сделать меню «Обновить», сохранить учётку 1С в Script Properties, вызвать обновление (OData или POST из Python) и при желании открыть HTML-сводку через веб-приложение.

---

## action_outline

1. **Боль** – каждый раз скачать CSV → Импорт → сломать формулы.
2. **Меню onOpen** – Extensions → Apps Script → `createMenu` → «Обновить данные».
3. **Функция refresh** – toast + запись на лист / вызов OData / приём POST.
4. **Практика dds-sheets** – `saveOnecCredentials` → `refreshFrom1C()` → лист `raw_dds` + `meta`.
5. **HTML-дашборд** – `doGet` + `Index.html`; кнопка UI вызывает `google.script.run.refreshFrom1C()`.
6. **Альтернатива** – Python `push_via_webapp.py` → `doPost` на тот же URL.
7. **Квоты/безопасность** – UrlFetch 20k/100k, runtime 6 мин; пароль только в Properties; не «выполнять от имени всех» без понимания.

---

## Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT AUTH WARNING:** сервер MCP `user-mcp-kv` в этой сессии **не подключён**. Точные показы/мес **не получены** и **не выдуманы**. https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

**LSI:** google apps script кнопка; google таблицы скрипт меню; apps script onOpen; обновить данные google sheets; UrlFetchApp 1с; HtmlService дашборд.

**SEO-вывод:** SERP забит общими «custom menu». Угол КОДА: кнопка **обновить финданные** + OData/веб-приложение сводки кассы.

---

## SERP (WebSearch, 22.07.2026)

| # | URL | Заметка |
| --- | --- | --- |
| 1 | https://developers.google.com/apps-script/guides/menus | Канон custom menu + onOpen |
| 2 | https://developers.google.com/apps-script/guides/triggers | Simple vs installable triggers |
| 3 | https://developers.google.com/apps-script/guides/services/quotas | UrlFetch 20k/100k, runtime 6 min |
| 4 | https://developers.google.com/apps-script/guides/html/ | HtmlService |
| 5 | practice INSTALL.md | Развёртывание веб-приложения |

### Практика (dds-sheets) – факты для writer

- Листы: `raw_dds`, `meta`, `dashboard`
- `refreshFrom1C()` тянет AccumulationRegister ДДС + справочники через OData Basic Auth
- Credentials: `PropertiesService.getScriptProperties()` via `saveOnecCredentials`
- UI: кнопка «Обновить из 1С» → `google.script.run.refreshFrom1C()`
- Параллельный канал: Python POST → `doPost` пишет те же листы
- BOM в ответе 1С обрабатывается в `odataGet_`

---

## Таблица фактов

| # | Утверждение | Источник | Дата |
| --- | --- | --- | --- |
| 1 | Custom menu только у bound-скрипта; код меню в `onOpen`. | https://developers.google.com/apps-script/guides/menus | 2026-07-22 |
| 2 | Можно назначить функцию на рисунок/изображение (Assign script). | https://developers.google.com/apps-script/guides/menus | 2026-07-22 |
| 3 | `onOpen` – simple trigger при открытии файла с правом edit. | https://developers.google.com/apps-script/guides/triggers | 2026-07-22 |
| 4 | UrlFetch: 20 000/день consumer, 100 000 Workspace. | https://developers.google.com/apps-script/guides/services/quotas | 2026-07-22 |
| 5 | Макс. runtime скрипта 6 минут за запуск. | https://developers.google.com/apps-script/guides/services/quotas | 2026-07-22 |
| 6 | Triggers total runtime: 90 min/day consumer, 6 hr Workspace. | quotas docs | 2026-07-22 |
| 7 | UrlFetch response/POST size до 50 MB; timeout вызова ~60 сек. | community + quotas | 2026-07-22 |
| 8 | HtmlService.createTemplateFromFile + doGet = веб-UI без отдельного хостинга. | practice Code.gs + Google HtmlService | 2026-07-22 |
| 9 | OData 1С как источник – см. гайд выгрузки. | /blog/vygruzka-1c-excel-odata/ | 2026-07-22 |
| 10 | Пароль 1С не хранить в ячейках листа – только Script Properties. | practice + security practice | 2026-07-22 |

---

## FAQ hints

1. Можно ли без JS? – Да для старта: копируете шаблон, меняете URL/имена листов.
2. Безопасно ли хранить пароль 1С? – Только Script Properties / не в git и не на листе.
3. Лимиты Google? – 6 мин/запуск, UrlFetch квоты; крупные выгрузки – Python push.
4. Меню не появилось? – Сохранить, переоткрыть вкладку, Run onOpen вручную.
5. Нужен ли программист 1С? – Для публикации OData/прав учётки – да один раз.
6. Только Telegram/кнопка на листе? – Меню, drawing Assign script, или HTML-кнопка.
7. Чем отличается от Make/n8n? – Логика живёт в таблице; внешние сценарии – другая статья.

---

## Cover hint

abstract sheet grid with refresh pulse nodes dark purple, no text
