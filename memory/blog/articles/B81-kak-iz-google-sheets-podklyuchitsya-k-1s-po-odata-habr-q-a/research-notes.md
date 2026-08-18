# Research notes — B81

**topic_id:** B81  
**slug:** kak-iz-google-sheets-podklyuchitsya-k-1s-po-odata-habr-q-a  
**h1:** Как из google sheets подключиться к 1С по odata? — Хабр Q&A  
**research_date:** 2026-08-18  
**publish_target:** сайт koda-fd.ru/blog (+ Дзен по оркестрации)  
**utility_gate:** PASS (`how_to`, mode B)  
**seed_url:** https://qna.habr.com/q/891699  
**related_published:** `/vygruzka-1c-excel-odata/`, `/google-apps-script-finansist-obnovit-dannye/`  
**practice_source:** паттерн `dds-sheets` (`refreshFrom1C`, Basic Auth, `PropertiesService`) — не дублировать B13/B22 целиком

---

## utility_verdict

**PASS** — utility-only how_to. Читатель получает рабочий маршрут: понять, почему Excel/браузер видят OData, а Google Sheets падает с «Адрес недоступен»; вывести публикацию 1С в интернет по HTTPS; починить Basic Auth в Apps Script; вытащить JSON на лист и повесить кнопку «Обновить»; закрыть безопасность (отдельный пользователь, не тащить ПДн/физлиц). Не новость, не обзор «что такое OData», не повтор гайда Excel↔1С.

---

## reader_outcome

После гайда финансист (или админ с ним) сможет из Google Sheets по кнопке дернуть нужный срез 1С через `…/odata/standard.odata/…?$format=json` и записать строки на staging-лист — либо честно диагностировать, что сервер недоступен из облака Google, и выбрать обходной путь (reverse proxy / push из локального скрипта).

---

## action_outline

1. **Диагностика боли Хабр Q&A** — Excel/Power Query и браузер работают с Basic Auth; `UrlFetchApp` отвечает «Адрес недоступен» → почти всегда нет маршрута из сети Google до публикации 1С (LAN/VPN/закрытый firewall), а не «не тот код».
2. **Проверить публикацию OData** — конфигуратор → Администрирование → Публикация на веб-сервере → галка «Публиковать стандартный интерфейс OData»; состав объектов через `УстановитьСоставСтандартногоИнтерфейсаOData` / БСП «Настройка стандартного интерфейса OData».
3. **Сделать URL достижимым из интернета** — HTTPS-публичный хост (не `192.168.*` / не только офисный DNS); отдельно: whitelist широкого пула IP Google **или** reverse-proxy / промежуточный API — чистый whitelist всех goog.json на практике часто нереалистичен.
4. **Собрать корректный GAS-запрос** — `method: 'get'`, `Authorization: Basic` + `Utilities.base64Encode(login+':'+password)`, `muteHttpExceptions: true`; убрать бессмысленный `credentials: 'include'` (это браузерный Fetch API, не Apps Script).
5. **Проверить `$metadata` и сущность** — сначала GET `…/odata/standard.odata/$metadata` и маленький `$top=5&$format=json` на безопасный Catalog_* (не «ФизическиеЛица» в прод-таблицу).
6. **Разобрать JSON → лист** — `JSON.parse` → `value[]` → `setValues` на `raw_*`; учёт BOM/кодировки ответа 1С.
7. **Кнопка / меню** — `onOpen` + пункт «Обновить из 1С»; логин/пароль только в `PropertiesService`, не в ячейках.
8. **Лимиты и объём** — UrlFetch ~20k/100k в день, runtime 6 мин, timeout вызова ~60 с, ответ до 50 MB; брать срезы `$filter`/`$top`, не весь регистр.
9. **Безопасность и эскалация** — отдельный пользователь только на чтение; не открывать ПДн в облачный Sheet; если прямой GAS→1С невозможен — push из Python/n8n на веб-приложение Sheets (паттерн B22).

---

## Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT AUTH WARNING:** сервер MCP `user-mcp-kv` в этой сессии **не подключён** (в каталоге MCP нет инструментов `wordstat_*`). Точные показы/мес **не получены** и **не выдуманы**. Обновите токен / подключите MCP-KV: https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

**Экспертная семантика (без цифр спроса) — LSI для копирайтера:**

| Кластер | Фразы | Роль |
| --- | --- | --- |
| Primary / H1 | как из google sheets подключиться к 1с по odata; google sheets 1с odata | H1, лид, Direct Answer |
| Ошибка | адрес недоступен urlfetchapp; urlfetchapp 1с; apps script odata | H2 диагностика |
| Техника | standard.odata; basic auth apps script; $format=json; muteHttpExceptions | H2/H3 код |
| Публикация | публикация на веб-сервере odata; установить состав стандартного интерфейса odata | H2 подготовка 1С |
| Финансы | выгрузка ддс google sheets; обновить из 1с кнопка | CTA / interlink B13/B22 |
| Альтернативы | power query 1с; n8n 1с google sheets; reverse proxy 1с | FAQ «когда не GAS» |

**SEO-вывод:** seed — Хабр Q&A без ответов (426 просмотров, >3 лет). SERP смешивает OData-туториалы для BI и обратную интеграцию Sheets→в 1С. Угол КОДА: **починить Sheets→OData** (доступность + Basic Auth + кнопка), с честной границей сети Google и interlink на уже опубликованные `/vygruzka-1c-excel-odata/` и `/google-apps-script-finansist-obnovit-dannye/` без каннибализации.

---

## SERP (WebSearch Cursor, 18.08.2026)

Приоритет — живой WebSearch/WebFetch; `research-serp.json` — черновик (много шума: календари 2026, reverse Sheets→1С, вендорские коннекторы).

### Главный запрос / H1 / seed

| # | URL | Тип | Пробел для КОДА |
| --- | --- | --- | --- |
| 1 | https://qna.habr.com/q/891699 | Вопрос без ответов: GAS + OData, ошибка «Адрес недоступен», пример с `credentials: 'include'` | Ответить по сути: сеть Google + правильные params UrlFetchApp + безопасный срез |
| 2 | https://habr.com/ru/companies/modusbi/articles/865798/ | Туториал OData 3.0 → КХД/BI (публикация, состав, риски объёма) | Нет Apps Script / Sheets |
| 3 | https://infostart.ru/1c/articles/1570140/ | Работа с 1С через OData (URL, $filter/$select, состав) | Для 1С-разработчика; нет GAS |
| 4 | https://v8.1c.ru/platforma/rest-interfeys/ | Официально: REST = OData 3.0, публикация, auth как у веб-сервисов | Канон фактов; не how-to Sheets |
| 5 | https://developers.google.com/apps-script/reference/url-fetch/url-fetch-app | UrlFetchApp: запросы с пула IP Google, нужен scope external_request | Объясняет «почему не LAN» |
| 6 | https://developers.google.com/apps-script/guides/services/quotas | Квоты UrlFetch / runtime | Лимиты для честного гайда |
| 7 | https://apimonster.ru/connector/bundle/googleSheets/1c-businessman/ | No-code коннектор Sheets↔1С | Платный обход без обучения; наш угол — свой GAS + границы |
| 8 | https://infostart.ru/1c/tools/2572620/ | Обратное: чтение Google Sheets **в** 1С | Не путать направление; упомянуть в FAQ |

### Вторичные полезные

- **Квоты/ошибки UrlFetch:** https://justin.poehnelt.com/posts/definitive-guide-to-urlfetchapp/ — «Address unavailable», private IP запрещены, timeout ~60 с.
- **Private network:** https://stackoverflow.com/questions/53633449/google-apps-script-fetch-data-from-private-network-vpn — on-prem за VPN недоступен из Apps Script.
- **IP ranges Google:** https://www.gstatic.com/ipranges/goog.json (+ оговорка: нет отдельного стабильного списка «только Apps Script»).
- **Автоматизация финотдела 2026** — общий фон; не раздувать, держать фокус на OData→Sheets.

### Конкурентный зазор (угол КОДА)

1. **Ответ на конкретный Хабр-вопрос** — не «что такое OData», а почему падает GAS и как починить.
2. **Финансист + админ 1С** — чеклист доступности HTTPS, отдельный пользователь, staging-лист.
3. **Не каннибализировать B13/B22** — B13 = Excel/общий OData; B22 = кнопка/меню Apps Script; B81 = **связка Sheets↔OData + сетевой блокер**.
4. **Анти-пример из Q&A** — `Catalog_ФизическиеЛица` в облачную таблицу = красный флаг 152-ФЗ; брать ДДС/статьи/контрагентов обезличенно.
5. **Plan B** — если 1С нельзя открыть наружу: локальный Python/n8n пушит в Sheets webapp (ссылка на B22).

---

## Таблица фактов (только с URL; для writer)

| # | Утверждение | Источник | Дата проверки |
| --- | --- | --- | --- |
| 1 | Платформа 1С автоматически формирует REST на базе **OData 3.0**; ответы Atom/XML или JSON. | https://v8.1c.ru/platforma/rest-interfeys/ | 2026-08-18 |
| 2 | После публикации на веб-сервере сторонние системы обращаются HTTP-запросами; auth OData-клиентов совпадает с веб-сервисами 1С. | https://v8.1c.ru/platforma/rest-interfeys/ | 2026-08-18 |
| 3 | Пример фильтра: `…/odata/standard.odata/Catalog_Goods?$filter=Price le 3.5 or Price gt 200`. | https://v8.1c.ru/platforma/rest-interfeys/ | 2026-08-18 |
| 4 | Для OData нужна платформа **≥ 8.3.5** и веб-сервер (IIS/Apache); публикация: Администрирование → Публикация на веб-сервере → галка «Публиковать стандартный интерфейс OData». | https://habr.com/ru/companies/modusbi/articles/865798/ | 2026-08-18 |
| 5 | Состав объектов задают `УстановитьСоставСтандартногоИнтерфейсаOData()`; в БСП — Администрирование → Синхронизация данных → Настройки стандартного интерфейса OData. В режиме совместимости ≤8.3.4 метод не применяется — доступны все поддерживаемые объекты. | https://habr.com/ru/companies/modusbi/articles/865798/ ; https://infostart.ru/1c/articles/1570140/ | 2026-08-18 |
| 6 | Через OData **недоступны** отчёты, команды, критерии отбора, регламентные задания, внешние источники, пользователи, журнал регистрации. | https://habr.com/ru/companies/modusbi/articles/865798/ | 2026-08-18 |
| 7 | На больших объёмах OData тормозит/таймаутит — дробить порциями; длинные вложенные URL повышают нагрузку. | https://habr.com/ru/companies/modusbi/articles/865798/ | 2026-08-18 |
| 8 | Seed Q&A: автор видит OData в Excel/браузере, в GAS — «Адрес недоступен»; код с `credentials: 'include'` и URL `…/Catalog_ФизическиеЛица`. Вопрос без ответов, ~426 просмотров, >3 лет. | https://qna.habr.com/q/891699 | 2026-08-18 |
| 9 | `UrlFetchApp` ходит через инфраструктуру Google с **пула IP**; для whitelist смотрите публикуемые ranges; нужен scope `https://www.googleapis.com/auth/script.external_request`. | https://developers.google.com/apps-script/reference/url-fetch/url-fetch-app | 2026-08-18 |
| 10 | UrlFetch calls: **20 000/день** consumer, **100 000** Workspace; script runtime **6 мин**/execution; URL Fetch response/POST size **50 MB**; URL length **2 KB**. | https://developers.google.com/apps-script/guides/services/quotas | 2026-08-18 |
| 11 | Timeout одного UrlFetch ~**60 секунд** (не настраивается). | https://justin.poehnelt.com/posts/definitive-guide-to-urlfetchapp/ | 2026-08-18 |
| 12 | Apps Script **не достучится** до on-prem/VPN/private IP (`10.x`, `192.168.x`) — DNS/доступ с облака Google. | https://stackoverflow.com/questions/53633449/google-apps-script-fetch-data-from-private-network-vpn ; UrlFetchApp unofficial docs | 2026-08-18 |
| 13 | «Exception: Address unavailable» часто = IP Google режется firewall целевого хоста или транзиентный routing; retry с backoff может помочь при transient, но не при закрытой LAN. | https://justin.poehnelt.com/posts/definitive-guide-to-urlfetchapp/ | 2026-08-18 |
| 14 | Стабильного узкого списка «только Apps Script IP» нет; goog.json — огромный общий пул Google-сервисов, меняется. | https://brooked.io/guides/apps-script-ip-whitelisting-database ; https://www.gstatic.com/ipranges/goog.json | 2026-08-18 |
| 15 | Параметр `credentials: 'include'` — из браузерного Fetch; в `UrlFetchApp.fetch(url, params)` для Basic Auth достаточно `headers.Authorization` + `method`. | MDN Fetch vs https://developers.google.com/apps-script/reference/url-fetch/url-fetch-app ; разбор seed-кода | 2026-08-18 |
| 16 | Практика КОДА (не выдумывать поля): OData Basic Auth → лист `raw_*`; base URL оканчивается на `/odata/standard.odata`; `$format=json&$top=N`; credentials в Script Properties. | related: `/vygruzka-1c-excel-odata/`, `/google-apps-script-finansist-obnovit-dannye/` | 2026-08-18 |
| 17 | Метаданные: GET `…/odata/standard.odata/$metadata`; JSON: `?$format=json` (в туториалах также встречается `$format=application/json`). | https://habr.com/ru/companies/modusbi/articles/865798/ ; Infostart 1570140 | 2026-08-18 |

**Не использовать без оговорки:** точные показы Wordstat; обещание «whitelist трёх IP и заработает»; выгрузка полных физлиц/ПДн в Google Sheets как нормальный сценарий.

---

## Структура H2/H3 для writer (спека)

Следовать карточке B81; наполнение:

### H2: Когда это нужно финотделу (и когда нет)
- Нужно: регулярный срез справочников/ДДС в Sheets без «Сохранить как».
- Не нужно / опасно: весь регистр, ПДн, запись обратно в 1С без регламента.
- Рекомендация: если Excel уже тянет OData, а Sheets нет — проблема сети, не «Sheets хуже».

### H2: Подготовка 1С и доступность из Google
- Публикация + состав OData + отдельный пользователь readonly.
- Чеклист: браузер с телефона вне офиса открывает `$metadata`?
- Рекомендация: без публичного HTTPS не начинать писать GAS.

### H2: Пошагово: Apps Script → OData → лист
- Правильный `UrlFetchApp` (Basic Auth, muteHttpExceptions).
- Парсинг `value` → `raw_*`.
- Меню «Обновить из 1С» + PropertiesService.
- Рекомендация: первый запрос `$top=5` на безопасную сущность.

### H2: Типичные ошибки (разбор Хабр Q&A)
- «Адрес недоступен» / DNS / private IP.
- 401/403 — логин/права/HTTPS-сертификат.
- Таймаут 60 с / квоты — резать `$filter`/`$top`.
- Рекомендация: не копировать `credentials: 'include'` из браузерных сниппетов.

### H2: Что автоматизировать дальше
- Interlink B22 (кнопка/триггер), B13 (Excel path), обезличивание.
- Plan B: push из локального контура.
- Рекомендация: регламент «кто жмёт / какой период / куда staging».

---

## FAQ hints (ответы-действия)

1. **Можно ли без программиста?** — Скрипт GAS — по шаблону; публикацию OData и firewall один раз делает админ/1С-ник.
2. **Сколько займёт?** — Если OData уже снаружи по HTTPS: вечер на скрипт+кнопку; если база только в LAN: сначала инфраструктура (дни), иначе Plan B.
3. **Какие риски для данных?** — Пароль в Properties, не на листе; не тащить физлиц/полные карточки; отдельный readonly-пользователь.
4. **Почему в Excel ок, а в Sheets нет?** — Excel ходит с вашего ПК/VPN; UrlFetchApp — с IP Google.
5. **Нужен ли IIS?** — Нужен веб-сервер (IIS или Apache) или облачная публикация провайдера — не «магия без HTTP».
6. **Можно ли писать в 1С из Sheets?** — Технически POST/PATCH есть; для финотдела по умолчанию только чтение.
7. **Альтернатива без открытия 1С наружу?** — Локальный скрипт/n8n → веб-приложение Google Sheets (см. гайд про кнопку обновления).

---

## Cover hint

abstract holographic data bridge sheets-to-erp dark #0a0a0f purple #8b5cf6 blue #93c5fd, no text on image

---

## Cannibalization note

- **B13** `/vygruzka-1c-excel-odata/` — общий OData→Excel(+Sheets вскользь). B81 углубляет **только Sheets/GAS + ошибку доступа**.
- **B22** `/google-apps-script-finansist-obnovit-dannye/` — кнопка/меню/квоты. B81 — источник OData и сетевой precondition.
- Writer: interlink оба, не пересказывать их целиком.
