# Research notes — B13

**topic_id:** B13  
**slug:** vygruzka-1c-excel-odata  
**h1:** Как выгрузить данные из 1С в Excel через OData: пошагово без программиста  
**research_date:** 2026-07-22  
**publish_target:** сайт koda-fd.ru/blog (+ Дзен по оркестрации)  
**utility_gate:** PASS (`how_to`, mode B)  
**practice_source:** `D:\projects\1С\dds-sheets` (INSTALL.md, Code.gs `refreshFrom1C`, fetch_cashflow.py)

---

## utility_verdict

**PASS** — тема utility-only how_to. Читатель получает рабочий маршрут: понять, когда OData хватает без программиста; опубликовать `…/odata/standard.odata`; вытащить выборку в Excel (Power Query / CSV) с `$filter`/`$top`; при необходимости связать с Google Sheets кнопкой «Обновить из 1С»; закрыть безопасность отдельным пользователем и минимальным составом объектов. Не новость, не «вообще про интеграции».

---

## reader_outcome

После гайда финансист сможет один раз настроить (или запросить у админа) публикацию OData и дальше сам обновлять нужный срез данных из 1С в Excel или Google Sheets по кнопке / по запросу, без ежедневного «Сохранить как» из отчёта и без заказной обработки на каждую таблицу.

---

## action_outline

1. **Сверить задачу с возможностями OData** — малые/средние срезы (ДДС, справочники, регистры) vs большие BI-выгрузки; если нужны сложные join/СКД на миллионы строк — не мучить OData, звать программиста / экстрактор.
2. **Зафиксировать URL публикации** — база на веб-сервере (IIS/Apache или облако 1С), галка «Публиковать стандартный интерфейс OData», проверка `…/odata/standard.odata` и `$metadata` в браузере.
3. **Ограничить состав объектов** — через «Настройка стандартного интерфейса OData» / `УстановитьСоставСтандартногоИнтерфейсаOData` только нужные Catalog_* и регистры; не открывать всю базу.
4. **Создать отдельного пользователя 1С** — только чтение нужных объектов; пароль не в общий чат; для облака — HTTPS.
5. **Собрать первый запрос** — `Entity?$format=json&$top=N` (+ `$filter` / `$select` по необходимости); проверить ответ JSON.
6. **Подтянуть в Excel** — Данные → из веба / канал OData (Power Query), сохранить запрос, обновить по кнопке; либо сохранить JSON/CSV и открыть.
7. **Опционально: Google Sheets** — Apps Script `UrlFetchApp` + Basic Auth + кнопка «Обновить из 1С» (паттерн `refreshFrom1C` из dds-sheets); учесть, что сервер 1С должен быть доступен с IP Google.
8. **Прогнать чеклист безопасности** — что не тащить в облачные таблицы (ПДн, полные карточки физлиц); сырые выгрузки не слать в ChatGPT без обезличивания.
9. **Зафиксировать регламент обновления** — кто жмёт кнопку, какой `$top`/период, куда писать staging-лист (`raw_*`).

---

## Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT AUTH WARNING:** сервер MCP `user-mcp-kv` в этой сессии **не подключён** (в каталоге MCP нет инструментов `wordstat_*`). Точные показы/мес **не получены** и **не выдуманы**. Обновите токен / подключите MCP-KV: https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

**Экспертная семантика (без цифр спроса) — LSI для копирайтера:**

| Кластер | Фразы (использовать осмысленно) | Роль |
| --- | --- | --- |
| Primary | выгрузка из 1с в excel, выгрузка данных из 1с в excel | H1, лид, Direct Answer |
| OData | odata 1с, standard.odata, rest интерфейс 1с, публикация на веб-сервере odata | H2 про URL и публикацию |
| Excel path | power query 1с, excel из интернета 1с, csv из 1с | H2 про Excel/CSV |
| Sheets path | выгрузка 1с в google sheets, apps script 1с, обновить из 1с | H2 про кнопку в Sheets |
| Fin angle | выгрузка ддс 1с, регистр движений денежных средств odata | Пример сущности из практики |
| Diff | чем odata отличается от сохранить как, выгрузка отчёта 1с excel | FAQ / comparison-врезка |

**SEO-вывод:** SERP по «выгрузка из 1с в excel» забит ручным «Сохранить как» и списками 5 способов. Угол КОДА — **OData как курьер API** + Excel/Sheets без программиста на стороне финансиста, с честной границей «когда звать 1С-ника» и безопасностью. В H1/лиде держать связку «OData + Excel + без программиста», secondary — Sheets и `standard.odata`.

---

## SERP (WebSearch Cursor, 22.07.2026)

Приоритет — живой WebSearch; `research-serp.json` (шаг 0) — черновик. Много URL из утиного SERP про ручной Excel без OData или чужие ERP (Dynamics/SAP) по запросу `odata standard.odata финансы` — **отфильтрованы**.

### Главный запрос: `выгрузка из 1с в excel` / H1 + OData

| # | URL | Тип | Пробел для КОДА |
| --- | --- | --- | --- |
| 1 | https://lumpics.ru/uploading-data-from-1c-in-excel/ | 5 ручных способов (отчёт, список, документ) | Нет OData / Power Query / Sheets |
| 2 | https://scloud.ru/blog/razbiraemsya_kak_vygruzit_dannye_iz_1s_v_excel_i_naoborot/ | Excel + COM + обработки | Облачный вендор; слабый угол «финансист сам» |
| 3 | https://kvant-c.ru/faq/1c-excel-export/ | FAQ экспорт | Обзор способов, нет пошагового OData→Excel |
| 4 | https://denvic.tech/blog/ekspertnye-stati/vygruzka-dannykh-iz-1s-rasskazyvaem-pro-4-sposoba-i-nakhodim-samyy-optimalnyy/ | Excel / SQL / OData / экстрактор | OData есть, но продают экстрактор; мало «кнопка в Sheets» |
| 5 | https://infostart.ru/1c/articles/2423164/ | BI-методы, лимиты OData (02.07.2025) | Для аналитиков/BI; не CFO-язык и не Apps Script |
| 6 | https://e.fd.ru/1151210 | «Финдиректор» сент. 2025: Excel↔1С через OData | Платный paywall; наш угол — открытый гайд + Sheets из практики |
| 7 | https://arenda1c.ru/articles/analitika-v-1s-dashbordyi-dlya-rukovoditelya-i-eksport-v-power-bi.html | Power BI + OData | Фокус Power BI, не Excel-финансист и не Google Sheets |

### Вторичные

- **`odata 1с`** — сильные источники: https://v8.1c.ru/platforma/rest-interfeys/ (официально OData 3.0), https://infostart.ru/1c/articles/1570140/, https://1c-programmer-blog.ru/programmirovanie/rest-interfejs-odata-v-1c.html. Вебинары API-first июнь 2026 (on-soft) — архитектурные, не how-to для CFO.
- **`выгрузка 1с в google sheets`** — Make/CSV (promaren.ru 19.02.2026), экстракторы и сервисный аккаунт (extractor1c, Infostart). Прямой OData из Apps Script почти не разобран; на Habr Q&A типичная ошибка «Адрес недоступен» (закрытый сервер / блок IP Google).
- **`odata standard.odata`** — ITS приложение 12 (сущности), официальный REST; мусор SERP: Dynamics 365 / SAP — **не цитировать** как про 1С.

### Конкурентный зазор (угол КОДА)

1. **Финансист, не 1С-разработчик** — термины через аналогии (OData = курьер API / реестр выписок), без снобизма.
2. **Граница «хватит OData / нужен программист»** — честно про таймауты и «песочницу» (Infostart/Denvic), чтобы не обещать BI на миллионы строк.
3. **Два потребителя одной публикации:** Excel (Power Query) и Google Sheets (кнопка `refreshFrom1C`) из одного `standard.odata`.
4. **Практика УНФ ДДС** — реальные имена сущностей: `AccumulationRegister_ДвиженияДенежныхСредств_RecordType`, справочники статей/контрагентов/касс (dds-sheets), без выдуманных полей.
5. **Безопасность 152-ФЗ / коммерческая тайна** — отдельный пользователь, узкий состав OData, не тащить ПДн в облачный лист; линк на `/obezlichivanie-dannyh-chatgpt-finansist/`.

---

## Таблица фактов (только с URL или practice path; для writer)

| # | Утверждение | Источник | Дата проверки |
| --- | --- | --- | --- |
| 1 | Платформа 1С автоматически формирует REST-интерфейс на базе протокола **OData 3.0**; ответы Atom/XML или JSON. | https://v8.1c.ru/platforma/rest-interfeys/ | 2026-07-22 |
| 2 | Для использования REST/OData базу публикуют на веб-сервере в конфигураторе; после публикации объекты доступны по HTTP. | https://v8.1c.ru/platforma/rest-interfeys/ | 2026-07-22 |
| 3 | URL-паттерн: `…/odata/standard.odata/<ИмяРесурса>`; пример фильтра OData: `$filter=Price le 3.5 or Price gt 200`. | https://v8.1c.ru/platforma/rest-interfeys/ | 2026-07-22 |
| 4 | В REST доступны справочники, документы, регистры (в т.ч. накопления), виртуальные таблицы остатков/оборотов и др.; при операциях выполняются проверки прав. | https://v8.1c.ru/platforma/rest-interfeys/ | 2026-07-22 |
| 5 | Состав стандартного интерфейса OData (с платформы ~8.3.5+) задают явно (`УстановитьСоставСтандартногоИнтерфейсаOData` / обработка настройки); иначе объекты могут быть недоступны. | https://infostart.ru/1c/articles/1570140/ ; https://1c-programmer-blog.ru/programmirovanie/rest-interfejs-odata-v-1c.html | 2026-07-22 |
| 6 | Метаданные интерфейса смотрят по `…/odata/standard.odata/$metadata`; JSON: `?$format=json`. | https://1c-programmer-blog.ru/programmirovanie/rest-interfejs-odata-v-1c.html | 2026-07-22 |
| 7 | Веб-сервер для публикации: IIS или Apache (Apache 2.4 — с платформы 8.3.8+). «Без IIS» = Apache или облачная публикация провайдера, не «без веб-сервера вообще». | https://1c-programmer-blog.ru/programmirovanie/rest-interfejs-odata-v-1c.html ; https://help.albato.ru/ru/article/podklyuchenie-1sunf-k-albato-pue49h/ | 2026-07-22 |
| 8 | OData рекомендован 1С как стандартный REST-доступ, но на практике: медленные запросы, таймауты на больших объёмах, ограничение длины запроса с фильтрами (**~255 символов** — по отраслевым обзорам). Подходит для малых срезов / «песочницы». | https://infostart.ru/1c/articles/2423164/ (02.07.2025) | 2026-07-22 |
| 9 | Ручной Excel с отчёта: без программиста, но полностью ручной цикл и риск ошибок; лист Excel ~1 млн строк — потолок для «просто выгрузить всё». | https://infostart.ru/1c/articles/2423164/ | 2026-07-22 |
| 10 | Описание сущностей стандартного интерфейса OData — официальное приложение 12 в руководстве разработчика (ИТС). | https://its.1c.ru/db/v851doc/bookmark/dev/TI000001392 | 2026-07-22 |
| 11 | УНФ поддерживает OData: в облаке часто уже опубликовано (иначе — в поддержку хостинга); on-prem — галка в «Публикация на веб-сервере» + настройка состава сущностей. | https://help.albato.ru/ru/article/podklyuchenie-1sunf-k-albato-pue49h/ ; практика dds-sheets | 2026-07-22 |
| 12 | Практика КОДА: кнопка обновления тянет OData Basic Auth → лист `raw_dds`; base URL оканчивается на `/odata/standard.odata`; запрос `entity?$format=json&$top=N`. | `D:\projects\1С\dds-sheets\html-dashboard\Code.gs` (`refreshFrom1C`, `odataGet_`); `INSTALL.md` | 2026-07-22 |
| 13 | Практика КОДА (УНФ ДДС): сущности `Catalog_СтатьиДвиженияДенежныхСредств`, `Catalog_Контрагенты`, `Catalog_Организации`, `Catalog_Кассы`, `Catalog_БанковскиеСчета`, `AccumulationRegister_ДвиженияДенежныхСредств_RecordType`; в движениях поля вроде `СуммаПриход` / `СуммаРасход`, ключи `*_Key`. | Code.gs; `fetch_cashflow.py` | 2026-07-22 |
| 14 | В Apps Script учётка кладётся в `PropertiesService` через `saveOnecCredentials`; UI-кнопка «Обновить из 1С»; сертификаты HTTPS валидируются (`validateHttpsCertificates: true`). | INSTALL.md; Code.gs | 2026-07-22 |
| 15 | Типичный блокер Sheets→OData: «Адрес недоступен» у `UrlFetchApp`, если 1С только во внутренней сети или режет IP Google. | https://qna.habr.com/q/891699 | 2026-07-22 |
| 16 | Журнал «Финансовый директор» (№9, сент. 2025) публиковал инструкцию подключения Excel к 1С через OData (paywall) — сигнал спроса у CFO-аудитории. | https://e.fd.ru/1151210 | 2026-07-22 |
| 17 | Аутентификация OData-клиентов совпадает с веб-сервисами 1С (логин/пароль пользователя ИБ). | https://v8.1c.ru/platforma/rest-interfeys/ | 2026-07-22 |

**Не использовать как факт без оговорки:** точные цены «автовыгрузки за 30 000 ₽» из коммерческих лендингов; любые показы Wordstat до подключения MCP-KV.

---

## Структура H2/H3 для будущей статьи (спека для writer)

Следовать карточке B13; ниже — наполнение.

### H2: Когда хватает OData, а когда нужен программист 1С
- Ручной «Сохранить как» vs OData vs заказная обработка / экстрактор / SQL.
- Правило: OData = регулярный срез и обновление; программист = сложная СКД, огромные объёмы, недоступные объекты, закрытый контур без публикации.

### H2: Публикация базы и URL `…/odata/standard.odata`
- Веб-сервер / облако; галка стандартного OData; `$metadata` как проверка.
- Имена ресурсов: `Catalog_…`, `Document_…`, `AccumulationRegister_…_RecordType`.
- JSON: `$format=json`, пагинация через `$top` (и осторожно с фильтрами).

### H2: Выгрузка в Excel / CSV: запрос, фильтр, лимиты
- Power Query / «из интернета»: URL + учётка.
- `$filter` / `$select` / `$top`; лимиты скорости и длины фильтра.
- CSV/JSON как запасной путь.

### H2: Связка с Google Sheets: кнопка «Обновить из 1С»
- Схема: OData → Apps Script → лист `raw_*` → дашборд/сводные.
- Паттерн `saveOnecCredentials` + `refreshFrom1C` (без копирования секретов в статью).
- Требование: база доступна из интернета (HTTPS); иначе Python/локальный sync, не GAS.

### H2: Безопасность: отдельный пользователь, права, что не тащить в облако
- Отдельный read-only пользователь; минимальный состав OData.
- Не выгружать лишние ПДн; облачный Sheets = чужой контур.
- Связка с обезличиванием перед нейросетями.

### Блок «Что дальше» + FAQ
- Internal: `/ot-excel-k-fin-konturu-30-dney/`, `/obezlichivanie-dannyh-chatgpt-finansist/`.
- CTA: Telegram + клуб по conversion-map (≤3 упоминания оффера).

---

## Практика dds-sheets (для writer — не выдумывать)

- **Стек:** УНФ OData → (A) Python `fetch_cashflow.py` / (B) Apps Script `refreshFrom1C` → Google Sheet → HTML-дашборд «Сводка кассы».
- **Кнопка UI:** «Обновить из 1С» (INSTALL.md).
- **Лимиты в коде:** движения `$top=2000`, справочники `$top=500` (можно менять; писать как пример, не как закон 1С).
- **Секреты:** в статье только плейсхолдеры `ONEC_BASE_URL` / пользователь; **не** копировать реальные URL/пароли из `.env`.
- **Аналогия для текста:** OData — «защищённый курьер», который по URL отдаёт структурированный акт (JSON), а не «магия без публикации базы».

---

## Риски и оговорки для writer

- Не обещать «без программиста на 100%»: публикация веб-сервера и состав OData часто делает админ **один раз**; дальше финансист самообслуживается.
- Не путать OData 1С с Dynamics/SAP OData из мусорного SERP.
- Не упоминать VPN / обход блокировок.
- Длинное тире «—» запрещено; кавычки прямые `"`.
- Эмодзи в тексте статьи — нет.
- Цены клуба KODA не выдумывать.
- Wordstat-цифры в статье **не ставить**, пока MCP-KV не отдаст факты.
- Режим A / новости — запрещены; каждый H2 — действие.
- Автор: `olga-kondratskaya`, голос от первого лица / редакции КОДА по site-brief.

---

## Internal links

- `/ot-excel-k-fin-konturu-30-dney/`
- `/obezlichivanie-dannyh-chatgpt-finansist/`

---

## FAQ hints (ответы-действия)

| Вопрос | Направление ответа |
| --- | --- |
| Работает ли OData на УНФ? | Да, это механизм платформы. Нужна публикация + состав объектов. В облаке часто уже есть URL; иначе — тикет в хостинг или админ on-prem. |
| Нужен ли HTTPS? | Для доступа из Excel/Sheets снаружи — да, разумный минимум. Практика dds-sheets ходит по HTTPS с проверкой сертификата. Внутри LAN иногда HTTP, но пароль 1С тогда в открытом периметре. |
| Чем отличается от обычной выгрузки Excel? | «Сохранить как» — разовый снимок глазами. OData — повторяемый HTTP-запрос к живой базе с фильтром и автообновлением в Power Query / скрипте. |
| Можно ли без IIS? | Да: Apache или облачная публикация. Без любого веб-сервера/публикации OData снаружи не заработает. |
| Можно ли сразу лить в Google Sheets? | Да, если URL 1С доступен из интернета. Иначе UrlFetchApp получит «Адрес недоступен» — тогда выгрузка локально (Python/CSV) и уже файл на Диск. |
| Нужен ли программист на каждый отчёт? | На чтение уже опубликованных сущностей — нет. На новый сложный отчёт СКД, недоступный объект или миллионы строк — да. |

---

## CTA (conversion-map)

| CTA | URL | Лимит |
| --- | --- | --- |
| Клуб KODA | https://koda-fd.ru/club?utm_source=blog&utm_medium=article&utm_campaign=vygruzka-1c-excel-odata | ≤2 |
| Telegram | https://t.me/finance_modern?utm_source=blog&utm_medium=article | ≤2 |
| Оплата бот | https://t.me/koda_salebot | ≤1 в «что дальше» |

---

## Источники исследования

- Официальный REST/OData 1С: https://v8.1c.ru/platforma/rest-interfeys/
- ИТС: описание сущностей OData (прил. 12)
- Infostart: OData how-to; методы выгрузки для BI (лимиты)
- Albato help: УНФ + OData (облако / публикация)
- Habr Q&A: Apps Script ↔ OData connectivity
- Практика: `D:\projects\1С\dds-sheets` (INSTALL.md, Code.gs, fetch_cashflow.py, POST-joint.md)
- `memory/brief/site-brief.md`, `conversion-map.md`, карточка B13 в `blog-topics.md`
- WebSearch Cursor 2026-07-22; `research-serp.json` как черновик шага 0
