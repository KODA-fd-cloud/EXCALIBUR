# Research notes — B91

**topic_id:** B91  
**slug:** http-servis-1c-chernovik-scheta-json  
**h1:** Как через HTTP-сервис создать черновик счёта в 1С из JSON своего приложения  
**research_date:** 2026-08-22  
**publish_target:** koda-fd.ru/blog  
**utility_gate:** PASS (`how_to`, mode B) — `utility-gate-topic.json`  
**related_published:** `/schet-1c-unf-telefon-http-servis/` (B18 — УНФ + PWA/Telegram), `/mcp-1c-cursor-ostatki-oboroty/` (B80 — MCP read-only)  
**internal_links (card):** `/avtomatizaciya-finansov-no-code/`, `/obezlichivanie-dannyh-chatgpt-finansist/`

---

## utility_verdict

**PASS** — how_to для финотдела и интегратора: спроектировать JSON-контракт, поднять (или выбрать готовое) HTTP-сервис в 1С, принять POST из backend/CRM, создать **черновик** счёта на оплату, вернуть номер/ID в JSON и проверить документ в 1С. Не новость про Sber API/НДС 2026, не «что такое JSON», не обзор ERP без шагов.

---

## reader_outcome

После гайда финансист с участием 1С-специалista (или no-code-разработчика backend) сможет настроить цепочку «ваше приложение → POST JSON → HTTP-сервис 1С → черновик счёта на оплату с номером в ответе» и прогнать тест через curl/Postman без ручного ввода счёта в интерфейсе 1С.

---

## action_outline

1. **Проверить, подходит ли HTTP-сервис** — нужен узкий сценарий «создать счёт из внешней системы»; если достаточно read-only отчётов — OData/MCP (B80); если уже есть CRM с готовым REST для БП — рассмотреть расширение bit_http_api как альтернативу кастомному коду.
2. **Зафиксировать JSON-контракт** — минимум: идентификаторы продавца/покупателя (ИНН или GUID), массив `items` (наименование, количество, цена), опционально `comment` как ID заказа сайта; договориться о единицах (`price` в копейках vs рубли) до кодирования.
3. **Создать объект HTTP-сервиса в конфигураторе** — «Общие → HTTP-сервисы»: корневой URL, шаблон `/invoices` (или `/create`), метод **POST**, обработчик на встроенном языке.
4. **Написать обработчик POST** — `Запрос.ПолучитьТелоКакСтроку()` → `ЧтениеJSON`/`ПрочитатьJSON` → валидация полей → создание документа «Счёт покупателю» / «СчетНаОплату» **без проведения** (черновик) → `ЗаписьJSON` в `HTTPСервисОтвет(200)` с `number`, `id`, `date`.
5. **Безопасность до публикации** — отдельный пользователь 1С с минимальными правами (создание счетов + чтение контрагентов/номенклатуры), Basic Auth или заголовок токена, HTTPS, лимит размера тела; **не** передавать сырые ПДн в облачный LLM при отладке JSON (см. internal obezlichivanie).
6. **Опубликовать базу на веб-сервере** — IIS/Apache или облачная публикация; галка HTTP-сервисов; URL вида `https://host/{публикация}/hs/{сервис}/{шаблон}`; smoke-test GET health или POST на тестовом JSON.
7. **Проверить из внешнего приложения** — curl/Postman/`fetch` с `Content-Type: application/json`; негативные кейсы: пустое тело → 400, неверный ИНН → 4xx/500 + запись в журнал регистрации 1С.
8. **Сверить результат в 1С и закрыть цикл** — «Продажи → Счета покупателям»: контрагент, сумма, комментарий заказа; при успехе — автоматизировать PDF/ЭДО/проведение отдельным шагом (не смешивать с черновиком на пилоте).

---

## Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT AUTH WARNING:** сервер MCP `user-mcp-kv` в этой сессии **не подключён** (в каталоге MCP доступны только `cursor-cloud`, `cursor-subscriptions`; инструментов `wordstat_*` нет). Точные показы/мес **не получены** и **не выдуманы**. Обновите токен / подключите MCP-KV: https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

**Экспертная семантика (без цифр спроса) — LSI для копирайтера:**

| Кластер | Фразы | Роль |
| --- | --- | --- |
| Primary | http сервис 1с создать счет json, post json 1с счет, api 1с создать счет | H1/лид |
| HTTP setup | публикация http сервиса 1с, hs 1с post запрос, curl 1с json | H2 пошагово |
| Document | счет на оплату 1с api, черновик счета 1с, счет покупателю автоматически | Intent fin |
| Integration | интеграция crm 1с счет, сайт 1с post счет, rest api 1с бухгалтерия | Сценарии |
| JSON | прочитать json 1с, записатьjson http сервис, content-type application/json | Техника |
| Security | basic auth 1с http, пользователь http сервиса 1с, безопасность api 1с | H2 риски |
| Secondary | автоматизация финотдела 2026, http сервис 1с | Контекст CFO |
| Noise | счет-фактура 2026, nds 22, sber api directbank | **Не путать** — только оговорка |

**SEO-вывод:** SERP по primary смешивает общие гайды «HTTP-сервис + JSON» (Infostart, itcodik, v8.1c.ru) и готовый REST bit_http_api для **Бухгалтерии**. Пробел КОДА — **финансовый how-to: черновик счёта из своего приложения**, контракт JSON для fin, безопасность ПДн, сравнение «свой сервис vs готовое расширение», проверка в UI 1С. Отличать от B18 (УНФ + телефон + PWA) и B80 (MCP read-only).

---

## SERP (WebSearch Cursor, 22.08.2026)

Приоритет — живой WebSearch; `research-serp.json` (шаг 0) дополнен и уточнён. Noise по «2026 2026» (календари) отфильтрован.

### Главный запрос: `http сервис 1с создать счет json` / POST invoice

| # | URL | Тип | Пробел для КОДА |
| --- | --- | --- | --- |
| 1 | https://bit22.ru/blog/rest-api-1c-sozdat-schet-post-swagger | POST `/invoices`, Basic Auth, копейки, OpenAPI | Готовое расширение **БП 3.0**, не кастом + не акцент «черновик» |
| 2 | https://www.bit22.ru/rest-api-1c | Лендинг REST API: счета, акты, PDF | Коммерческий продукт; нет fin-безопасности ПДн |
| 3 | https://www.bit22.ru/blog/rest-api-1c-prostoj-obmen-bez-odata | REST vs OData, сценарий магазин→счёт | Dev/внедренец; мало «сделай сам в конфигураторе» |
| 4 | https://itcodik.com/article/http-servis-1s-svoimi-rukami | HTTP-сервис с нуля, curl, коды 200/400/404 (авг. 2026) | Учебный GET/status; нет документа «Счёт» |
| 5 | https://infostart.ru/1c/articles/1293341/ | Пошаговое создание HTTP-сервиса, публикация | Базовый учебник 2020; не счёт |
| 6 | https://infostart.ru/1c/articles/2354374/ | POST + JSON → создание объекта, номер в ответе | Альфа-Авто кейс; паттерн ответа полезен |
| 7 | https://www.1cget.ru/product/obmen-s-saytom-post-zapros-i-sozdanie-scheta-s-vozvratom-ego-nomera-v-otvete/ | POST счёт, возврат номера | Платная обработка; мало security |
| 8 | https://v8.1c.ru/platforma/http-servisy/ | Официально: объект HTTP-сервис, 404, HTTPСервисЗапрос | Нет прикладного счёта |
| 9 | https://v8.1c.ru/platforma/json/ | JSON-слои: ЧтениеJSON, ЗаписьJSON, XDTO | Справочник платформы |
| 10 | https://1c-dn.com/blog/work-with-http-services-in-1c-part-2-post-method/ | POST method EN tutorial | Не RU fin audience |

### Secondary: `автоматизация финотдела` / API 2026

| # | URL | Тип | Пробел для КОДА |
| --- | --- | --- | --- |
| 1 | https://koda-fd.ru/blog/ai-dlya-finansista-2026/ | KODA: AI для fin | Связка через internal, не HTTP invoice |
| 2 | https://1c.ru/news/info.jsp?id=34401 | Sber API / DirectBank 2026 | **Noise** для темы HTTP-счёта |
| 3 | https://integration-software.ru/blog/avtomatizacia-kaznacheistva | Казначейство, DirectBank, УПД 5.03 | Широкий обзор, не POST счёт |
| 4 | https://1c.itat.ru/articles/nastroyka-avtomaticheskogo-obmena-s-bankom-v-1s-bukhgalteriya-polnoe-rukovodstvo-2025-2026/ | Банк↔1С API | Смежная автоматизация, другой intent |

### Конкурентный зазор (угол КОДА)

1. **Свой HTTP-сервис под один документ** vs покупка bit_http_api vs OData «на всё» — таблица выбора для fin.
2. **Черновик без проведения** — явный статус документа, чтобы бухгалтер успел проверить.
3. **JSON-контракт «для финансиста»** — ИНN, суммы, comment=order_id, без BSL в основном тексте (BSL в сниппетах/приложении).
4. **Безопасность** — отдельный пользователь, HTTPS, обезличивание логов; internal link на obezlichivanie.
5. **Проверка curl → документ в 1С → типичные 500** (контрагент не найден) — troubleshooting чеклист.

---

## Таблица фактов (≥15; только с URL; для writer)

| # | Утверждение | Источник | Дата проверки |
| --- | --- | --- | --- |
| 1 | HTTP-сервисы 1С — произвольные REST-подобные endpoint'ы поверх встроенного языка; платформа сопоставляет URL с шаблоном и HTTP-методом. | https://v8.1c.ru/platforma/http-servisy/ | 2026-08-22 |
| 2 | Если URL/метод не совпали с шаблоном HTTP-сервиса, платформа возвращает **404 Not Found**. | https://v8.1c.ru/platforma/http-servisy/ ; https://itcodik.com/article/http-servis-1s-svoimi-rukami | 2026-08-22 |
| 3 | Обработчик получает `HTTPСервисЗапрос` (URL, заголовки, тело) и возвращает `HTTPСервисОтвет` с кодом, заголовками и телом. | https://v8.1c.ru/platforma/http-servisy/ | 2026-08-22 |
| 4 | JSON в 1С читают через `ЧтениеJSON`/`ПрочитатьJSON`, пишут через `ЗаписьJSON`/`ЗаписатьJSON`; формат активно используется в HTTP-интерфейсах. | https://v8.1c.ru/platforma/json/ | 2026-08-22 |
| 5 | Типичный POST-обработчик: `ТелоЗапроса = Запрос.ПолучитьТелоКакСтроку()` → разбор JSON → запись объекта → JSON-ответ с `Content-Type: application/json; charset=utf-8`. | https://infostart.ru/1c/articles/2354374/ ; https://www.1cget.ru/product/obmen-s-saytom-post-zapros-i-sozdanie-scheta-s-vozvratom-ego-nomera-v-otvete/ | 2026-08-22 |
| 6 | После публикации HTTP-сервис доступен по шаблону `http(s)://{хост}/{публикация}/hs/{имя_сервиса}/{шаблон}`. | https://infostart.ru/1c/articles/1293341/ ; https://itcodik.com/article/http-servis-1s-svoimi-rukami | 2026-08-22 |
| 7 | Для публикации HTTP-сервисов нужен веб-сервер (IIS или Apache) и включение сервиса на закладке «HTTP-сервисы» мастера публикации. | https://infostart.ru/1c/articles/1293341/ | 2026-08-22 |
| 8 | GET в HTTP-сервисе — чтение; POST — создание ресурса или запуск обработки (разные обработчики на одном шаблоне). | https://itcodik.com/article/http-servis-1s-svoimi-rukami | 2026-08-22 |
| 9 | На неверный ввод рекомендуют **400**, на отсутствие ресурса **404**, на ошибку auth **401/403** — не прятать ошибки в HTTP 200. | https://itcodik.com/article/http-servis-1s-svoimi-rukami | 2026-08-22 |
| 10 | Токены/секреты не следует передавать в URL query — только заголовки + HTTPS + отдельный пользователь с минимальными правами. | https://itcodik.com/article/http-servis-1s-svoimi-rukami | 2026-08-22 |
| 11 | Расширение bit_http_api: `POST /hs/bit_http_api/invoices` с Basic Auth создаёт счёт в **1С:Бухгалтерия 3.0**; тело — `seller_inn`, `payer_inn`, `items[]`, опционально `comment`. | https://bit22.ru/blog/rest-api-1c-sozdat-schet-post-swagger ; https://www.bit22.ru/rest-api-1c | 2026-08-22 |
| 12 | В bit_http_api поле `price` передаётся **в копейках** (1 000 000 = 10 000,00 ₽). | https://bit22.ru/blog/rest-api-1c-sozdat-schet-post-swagger | 2026-08-22 |
| 13 | Успешный ответ bit_http_api включает `id`, `number`, `date`, `total_amount`, `comment` — их можно использовать для сверки в UI 1С. | https://bit22.ru/blog/rest-api-1c-sozdat-schet-post-swagger | 2026-08-22 |
| 14 | Типичная ошибка 500 при POST счёта в bit_http_api — не найден контрагент по ИНН или неверный JSON; диагностика через журнал регистрации 1С. | https://bit22.ru/blog/rest-api-1c-sozdat-schet-post-swagger | 2026-08-22 |
| 15 | bit_http_api требует конфигурацию **БП 3.0.190.22+**, роль `bitHttpApi_ОсновнаяРоль`, публикацию `/{публикация}/hs/bit_http_api/`. | https://bit22.ru/blog/rest-api-1c-sozdat-schet-post-swagger ; https://www.bit22.ru/blog/rest-api-1c-prostoj-obmen-bez-odata | 2026-08-22 |
| 16 | REST через HTTP-сервис позиционируется как альтернатива OData для узкого обмена «сайт/CRM → счёт» без открытия всего REST/OData интерфейса. | https://www.bit22.ru/blog/rest-api-1c-prostoj-obmen-bez-odata | 2026-08-22 |
| 17 | Паттерн «сайт шлёт POST → 1С создаёт документ → возвращает номер/ID в JSON» описан для обмена с сайтом (сквозная нумерация). | https://infostart.ru/1c/articles/2354374/ | 2026-08-22 |
| 18 | Счёт на оплату в типовых конфигурациях создаётся в разделе «Продажи → Счета покупателям» (ручная сверка после API). | https://bit22.ru/blog/rest-api-1c-sozdat-schet-post-swagger ; https://integration-software.ru/blog/kak-vystavit-schet-klientu-v-1s-8-3 | 2026-08-22 |

**Не использовать как факт без оговорки:** цены лицензии bit_http_api (137 250 ₽) — только если writer явно сравнивает buy vs build; показы Wordstat; цифры «экономия 40% времени fin» с маркетинговых лендингов автоматизации 2026.

---

## Структура H2/H3 (спека для writer)

1. **Когда это нужно финотделу (и когда нет)** — CRM/интернет-магазин/собственный портал; vs ручной счёт; vs готовое мобильное 1С (B18); vs только чтение остатков (B80).
2. **Подготовка данных и безопасность** — JSON-схема; ИНН vs GUID; comment как order_id; без ПДн в облаке LLM; пользователь API read/write scope.
3. **Пошаговая настройка** — ветка A: свой HTTP-сервис (конфигуратор → POST → черновик); ветка B: bit_http_api для БП (curl-пример); таблица сравнения.
4. **Проверка результата и типичные ошибки** — curl/Postman; сверка в «Счета покупателям»; 404/400/500; журнал регистрации.
5. **Что автоматизировать дальше** — проведение, PDF, ЭДО, webhook статуса оплаты; internal avtomatizaciya-finansov-no-code.

**FAQ hints (card):** можно ли без программиста; сколько займёт внедрение; какие риски для данных.

---

## CTA (conversion-map)

| CTA | URL | Лимит |
| --- | --- | --- |
| Клуб KODA | https://club.koda-fd.ru/?utm_source=blog&utm_medium=article&utm_campaign=http-servis-1c-chernovik-scheta-json | ≤2 |
| Telegram «Финансист, который кодит» | https://t.me/finance_modern?utm_source=blog&utm_medium=article | ≤2 |
| Сайт КОДА | https://koda-fd.ru/ | ≤1 |

**Запрещено:** `t.me/koda_salebot`, `@koda_salebot`.

---

## Источники исследования

- Официально: https://v8.1c.ru/platforma/http-servisy/ ; https://v8.1c.ru/platforma/json/
- HTTP how-to: https://itcodik.com/article/http-servis-1s-svoimi-rukami ; https://infostart.ru/1c/articles/1293341/
- POST + ответ номером: https://infostart.ru/1c/articles/2354374/ ; https://www.1cget.ru/product/obmen-s-saytom-post-zapros-i-sozdanie-scheta-s-vozvratom-ego-nomera-v-otvete/
- REST счета БП: https://bit22.ru/blog/rest-api-1c-sozdat-schet-post-swagger ; https://www.bit22.ru/rest-api-1c ; https://www.bit22.ru/blog/rest-api-1c-prostoj-obmen-bez-odata
- Fin context 2026: https://koda-fd.ru/blog/ai-dlya-finansista-2026/
- `memory/brief/fact-bank.md` — прямых фактов по HTTP-счёту нет; цифры только из таблицы выше
- WebSearch Cursor 2026-08-22; `research-serp.json` обновлён

---

=== EXCALIBUR BLOG RESEARCH ===
topic_id: B91
article_dir: memory/blog/articles/B91-http-servis-1c-chernovik-scheta-json
status: ✅ PASS
utility_verdict: PASS
reader_outcome: Настроить POST JSON → HTTP-сервис 1С → черновик счёта на оплату с номером в ответе и проверить через curl/Postman + UI 1С.
summary: WebSearch: bit22 POST/invoices (БП), itcodik/infostart (HTTP+JSON), v8.1c.ru (platform). Wordstat недоступен (MCP user-mcp-kv). 18 фактов с URL, 8 шагов action_outline. Internal: avtomatizaciya-finansov-no-code, obezlichivanie-dannyh-chatgpt-finansist. Отличие от B18/B80. Готов к writer.
===
