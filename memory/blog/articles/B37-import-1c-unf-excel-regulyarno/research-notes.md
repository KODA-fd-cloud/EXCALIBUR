# Research notes — B37

**topic_id:** B37  
**slug:** import-1c-unf-excel-regulyarno  
**h1:** Как настроить регулярный импорт из 1С УНФ в Excel без ручных выгрузок  
**research_date:** 2026-08-03  
**publish_target:** сайт koda-fd.ru/blog  
**utility_gate:** PASS (`how_to`, mode B) — `utility-gate-topic.json` + `research-context.json`  
**cannibalization:** published B13 `vygruzka-1c-excel-odata` — **не дублировать** угол «первый раз подключить OData / выгрузить срез». B37 = **регулярный цикл** (расписание / refresh / скрипт / HTTP-сервис + обновление книги). B30 (Power Query без макросов) ещё не published — не уходить в общий туториал PQ; держать источник = УНФ.

---

## utility_verdict

**PASS** — тема utility-only how_to. Читатель получает рабочий маршрут: выбрать схему регулярной поставки УНФ → Excel (Power Query + refresh при открытом файле / скрипт по расписанию / HTTP-сервис с готовым срезом); один раз подготовить узкий канал данных; настроить обновление без ежедневного «Сохранить как»; прогнать чеклист ошибок и безопасности. Не новость, не «вообще про OData», не импорт Excel→1С (обратное направление из SERP-шума).

---

## reader_outcome

После гайда финансист (с разовой помощью админа 1С при необходимости) настроит повторяемый контур «УНФ → Excel», где утренний/ежедневный срез ДДС или справочников появляется в книге по кнопке «Обновить» или по регламенту, без ручной выгрузки отчёта из 1С каждый день.

---

## action_outline

1. **Зафиксировать срез и частоту** — какие сущности УНФ (ДДС, остатки, продажи), горизонт (`$filter` по дате), SLA свежести (раз в день / каждый час), куда писать staging-лист (`raw_*`).
2. **Отделить B37 от разовой выгрузки** — если OData ещё не опубликован, отослать к гайду B13 / админу; в этой статье фокус на **режиме обновления**, не на первом `$metadata`.
3. **Выбрать схему регулярности** — (A) Excel Desktop Power Query: refresh при открытии + «каждые N минут» пока файл открыт; (B) скрипт/планировщик (Python / Task Scheduler / PAD), который дергает OData или HTTP и кладёт CSV/XLSX; (C) кастомный HTTP-сервис УНФ с уже агрегированным JSON под Excel/скрипт.
4. **Сузить канал данных** — отдельный read-only пользователь, минимальный состав OData / метод HTTP; `$select` + `$top` / период; не тащить ПДн в облачный лист.
5. **Собрать Power Query (или скрипт) на живой URL** — OData Feed / из веба / из папки с ночным CSV; сохранить запрос; проверить типы дат и разделители.
6. **Включить регламент обновления** — свойства подключения: обновлять при открытии файла; при необходимости интервал; для «файл закрыт» — честно выбрать скрипт/шлюз/PAD, а не обещать облачный Excel Online refresh OData.
7. **Прогнать smoke-test недели** — сверка контрольных сумм с отчётом УНФ; таймауты; пустой ответ; смена пароля; рост объёма.
8. **Зафиксировать владельца процесса** — кто жмёт Refresh / кто смотрит лог скрипта; что делать при падении (эскалация к 1С-админу).
9. **Что автоматизировать дальше** — staging → дашборд / Sheets; линк на обезличивание перед нейросетями; не раздувать OData до BI на миллионы строк.

---

## Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT unavailable:** сервер MCP `user-mcp-kv` в этой сессии **не найден** (в каталоге MCP нет `wordstat_*`; доступен только `cursor-cloud`). Точные показы/мес **не получены** и **не выдуманы**.  
При появлении MCP-KV / обновлении токена: https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

**Экспертная семантика (без цифр спроса) — LSI для копирайтера:**

| Кластер | Фразы (использовать осмысленно) | Роль |
| --- | --- | --- |
| Primary | импорт 1с унф excel регулярно, выгрузка 1с в excel по расписанию | H1, лид, Direct Answer |
| Direction fix | выгрузка из 1с в excel (не «загрузка excel в 1с») | Отстройка от SERP-шума Excel→1С |
| OData refresh | odata 1с обновление, power query 1с, standard.odata excel | H2 про канал + refresh |
| Schedule | обновлять каждые N минут excel, refresh при открытии, расписание выгрузки 1с | H2 про регулярность |
| UNF | 1с унф odata, управление нашей фирмой excel | Практика конфигурации |
| Alt path | http сервис 1с json excel, скрипт выгрузки 1с csv, n8n 1с | Схема C / FAQ |
| Diff B13 | без ручных выгрузок, регулярный импорт, не разовая настройка odata | Лид + internal link на B13 |
| Noise reject | загрузка номенклатуры из excel в унф | **Не тема статьи** |

**SEO-вывод:** сырой SERP по «импорт 1с унф excel» забит **обратным** направлением (Excel → УНФ: номенклатура, цены). Живой WebSearch по «OData / Power Query / расписание» уводит в **Power BI + gateway**, не в CFO-Excel. Угол КОДА — **УНФ → Excel без ежедневного «Сохранить как»**: выбор схемы refresh + честные границы Desktop vs закрытый файл vs HTTP-сервис. В H1/лиде держать «регулярно / без ручных выгрузок / УНФ → Excel»; secondary — Power Query refresh и OData как уже готовый канал (со ссылкой на B13).

---

## SERP (WebSearch Cursor, 03.08.2026)

Приоритет — живой WebSearch; `research-serp.json` (шаг 0) — черновик с сильным шумом **Excel→1С**.

### Шум (отфильтровать): Excel → УНФ

| # | URL | Почему не конкурент B37 |
| --- | --- | --- |
| 1 | https://topkoder.ru/stati/zagruzka-dannyh-iz-elektronnyh-tablic-excel-v-programmu-1s-upravlenie-nashej-firmoj/ | Загрузка **в** УНФ |
| 2 | https://42clouds.com/ru-ru/manuals/bystryy-vvod-nomenklatury-cherez-fayl-excel-v-1s-upravlenie-nashey-firmoy/ | Номенклатура Excel→УНФ |
| 3 | https://lumpics.ru/upload-from-excel-in-1c/ | Импорт в 1С |
| 4 | https://excel-gid.vercel.app/articles/k/ka/kak-importirovat-eksel-v-1s.html | Обратное направление |
| 5 | https://denvic.tech/blog/ekspertnye-stati/eksport-dannykh-iz-excel-v-1s-s-pomoshchyu-inzhektora-1s-kak-avtomatizirovat-zagruzku-i-izbezhat-osh/ | Excel→1С инжектор |

### Смежные конкуренты: 1С → BI / расписание (не Excel-финансист)

| # | URL | Тип | Пробел для КОДА |
| --- | --- | --- | --- |
| 1 | https://deeone.dev/blog/metody-vygruzki-iz-1c-2026.html | 7 методов 1С→BI 2026; OData лимиты | Power BI/DWH; нет регламента Excel Desktop |
| 2 | https://www.arenda1c.ru/articles/analitika-v-1s-dashbordyi-dlya-rukovoditelya-i-eksport-v-power-bi.html | OData + schedule в Power BI Service + gateway | Не Excel-книга финансиста |
| 3 | https://denvic.tech/blog/ekspertnye-stati/konnektor-dannykh-iz-1s-kak-poluchit-dannye-iz-1s-v-power-bi-ili-drugoy-sisteme-biznes-analitiki/ | Коннекторы, ночной full + инкремент 15–60 мин | Продают экстрактор; не how-to Excel |
| 4 | https://infostart.ru/1c/articles/914689/ | Личный опыт Power BI + OData | BI, не ежедневный Excel-контур |
| 5 | https://bi-team.ru/connector_1s_powerbi | Шлюз + scheduled refresh PBI | Коммерческий коннектор |
| 6 | https://agentsvodka.ru/news/avtomatizatsiya-buhgalterii-ezhednevnye-otchyoty-iz-1s-v-google-sheets | n8n + OData/HTTP → Sheets | Близко по «регулярно», но Sheets/n8n, не Excel PQ |
| 7 | https://www.koderline.ru/expert/instruktsii/article-nastroyka-power-bi-i-1s/ | Рассылка отчётов в папку + PQ к файлу | Полезен как схема B (файл в папку), мало УНФ-языка |

### Excel refresh (важно для честных границ)

| # | URL | Факт для угла |
| --- | --- | --- |
| 1 | https://www.howtogeek.com/microsoft-excel-auto-refresh-power-query/ | Таймер PQ refresh только в **Desktop** и пока книга **открыта** |
| 2 | https://support.microsoft.com/en-gb/office/refresh-an-external-data-connection-in-excel-1524175f-777a-48fc-8fc7-c8514b984440 | Официально: Refresh / Refresh All; свойства подключения; периодическое обновление |
| 3 | https://github.com/OfficeDev/office-scripts-docs/blob/main/docs/testing/power-automate-troubleshooting.md | В Power Automate облаке `refreshAllDataConnections` **не** обновляет обычный Power Query (кроме Power BI source) |
| 4 | https://techcommunity.microsoft.com/discussions/excelgeneral/power-query-background-refresh-while-file-is-closed/2773106 | Background refresh при закрытом файле — нет |

### Официальные / УНФ OData (переиспользовать, не пересказывать B13)

| # | URL | Роль |
| --- | --- | --- |
| 1 | https://v8.1c.ru/platforma/rest-interfeys/ | OData 3.0, публикация, `$filter`, auth = веб-сервисы |
| 2 | https://1cfresh.com/articles/data_odata | Fresh/облако: URL `…/odata/standard.odata`, состав через `УстановитьСостав…` |
| 3 | https://help.albato.ru/ru/article/podklyuchenie-1sunf-k-albato-pue49h/ | УНФ: галка публикации OData + настройка сущностей |
| 4 | https://42clouds.com/ru-ru/manuals/interfeys-odata-vozmozhnosti-i-nastroyka/ | UI: состав OData, отдельный пользователь REST |
| 5 | https://infostart.ru/1c/articles/1570140/ | Практическая публикация + URL-паттерн |
| 6 | https://koda-fd.ru/blog/vygruzka-1c-excel-odata/ | Internal: разовая настройка канала (B13) |

### Конкурентный зазор (угол КОДА)

1. **Направление данных** — явно «из УНФ в Excel», в лиде снять путаницу с загрузкой номенклатуры.
2. **Регулярность, не первый конект** — B13 = опубликовать и один раз вытащить; B37 = **кто/когда/чем обновляет** и что делать, когда файл закрыт.
3. **Три схемы на выбор** — Desktop PQ timer / скрипт+CSV / HTTP-сервис с готовым срезом; таблица «когда какую».
4. **Честные границы Excel** — нет магии «облачный Excel сам по расписанию тянет закрытую УНФ»; для закрытого файла — скрипт, PAD, или Power BI (упомянуть кратко, не уходить в BI-гайд).
5. **Финансистский срез УНФ** — ДДС/справочники с `$filter` по периоду; не «весь регистр в миллион строк».
6. **Безопасность** — отдельный пользователь, узкий состав, без сырых ПДн; линк `/obezlichivanie-dannyh-chatgpt-finansist/`.

---

## Таблица фактов (только с URL; для writer)

| # | Утверждение | Источник | Дата проверки |
| --- | --- | --- | --- |
| 1 | Платформа 1С формирует REST на базе **OData 3.0**; ответы Atom/XML или JSON; публикация на веб-сервере. | https://v8.1c.ru/platforma/rest-interfeys/ | 2026-08-03 |
| 2 | Пример фильтра: `…/odata/standard.odata/Catalog_Goods?$filter=Price le 3.5 or Price gt 200`. | https://v8.1c.ru/platforma/rest-interfeys/ | 2026-08-03 |
| 3 | Аутентификация OData-клиентов совпадает с веб-сервисами 1С. | https://v8.1c.ru/platforma/rest-interfeys/ | 2026-08-03 |
| 4 | С платформы **8.3.5+** доступен стандартный интерфейс OData; состав объектов задают (`УстановитьСоставСтандартногоИнтерфейсаOData`). | https://1cfresh.com/articles/data_odata | 2026-08-03 |
| 5 | В 1С:Фреш базовый URL OData: `адрес-приложения/odata/standard.odata`. | https://1cfresh.com/articles/data_odata | 2026-08-03 |
| 6 | Для УНФ on-prem: Конфигуратор → Администрирование → «Публикация на веб-сервере» → галка «Публиковать стандартный интерфейс OData». | https://help.albato.ru/ru/article/podklyuchenie-1sunf-k-albato-pue49h/ | 2026-08-03 |
| 7 | Рекомендуется отдельный пользователь для REST/OData и явный состав сущностей на вкладке «Состав». | https://42clouds.com/ru-ru/manuals/interfeys-odata-vozmozhnosti-i-nastroyka/ | 2026-08-03 |
| 8 | OData удобен для небольших срезов; на крупных регистрах (миллионы строк) медленный и нагружает продуктив — для BI ищут SQL/экстракторы. | https://deeone.dev/blog/metody-vygruzki-iz-1c-2026.html | 2026-08-03 |
| 9 | Ориентир применения OData (обзор 2026): справочники до ~100k строк с полной перезаливкой раз в сутки; регистры с миллионами — потолок OData. | https://deeone.dev/blog/metody-vygruzki-iz-1c-2026.html | 2026-08-03 |
| 10 | Альтернатива «тонкий канал»: кастомный **HTTP-сервис** 1С отдаёт уже нужный JSON-срез (агрегаты) — меньше парсинга на стороне Excel/n8n. | https://deeone.dev/blog/metody-vygruzki-iz-1c-2026.html ; https://agentsvodka.ru/news/avtomatizatsiya-buhgalterii-ezhednevnye-otchyoty-iz-1s-v-google-sheets | 2026-08-03 |
| 11 | В Excel Desktop у подключения Power Query можно задать **Refresh every N minutes** и **Refresh data when opening the file**; таймер работает, пока книга открыта в Desktop. | https://www.howtogeek.com/microsoft-excel-auto-refresh-power-query/ ; https://support.microsoft.com/en-gb/office/refresh-an-external-data-connection-in-excel-1524175f-777a-48fc-8fc7-c8514b984440 | 2026-08-03 |
| 12 | Автотаймер PQ **не** работает как фоновый процесс при закрытом файле. | https://techcommunity.microsoft.com/discussions/excelgeneral/power-query-background-refresh-while-file-is-closed/2773106 | 2026-08-03 |
| 13 | Office Scripts в облачном Power Automate: большинство refresh-методов (в т.ч. обычный Power Query) **не** обновляют данные; `Workbook.refreshAllDataConnections` по сути для Power BI source. | https://github.com/OfficeDev/office-scripts-docs/blob/main/docs/testing/power-automate-troubleshooting.md | 2026-08-03 |
| 14 | Для расписания в Power BI Service при локальной 1С нужен On-premises data gateway + credentials источника. | https://www.arenda1c.ru/articles/analitika-v-1s-dashbordyi-dlya-rukovoditelya-i-eksport-v-power-bi.html ; https://learn.microsoft.com/en-us/power-bi/connect-data/refresh-scheduled-refresh | 2026-08-03 |
| 15 | Практичный обход без live-OData в Excel: регламентная **рассылка отчётов** 1С в папку/FTP → Power Query читает файл из папки. | https://www.koderline.ru/expert/instruktsii/article-nastroyka-power-bi-i-1s/ | 2026-08-03 |
| 16 | Типичный BI-регламент (обзоры): ночной full + дневные инкременты каждые 15–60 мин — ориентир частоты, не обещание для Desktop Excel. | https://denvic.tech/blog/ekspertnye-stati/konnektor-dannykh-iz-1s-kak-poluchit-dannye-iz-1s-v-power-bi-ili-drugoy-sisteme-biznes-analitiki/ | 2026-08-03 |
| 17 | Published КОДА B13 уже закрывает «как выгрузить через OData в Excel/Sheets» — в B37 давать internal link, не повторять пошаговую публикацию 1:1. | https://koda-fd.ru/blog/vygruzka-1c-excel-odata/ | 2026-08-03 |

**Не использовать без оговорки:** цены коммерческих экстракторов; обещание «Excel Online сам по cron обновляет OData УНФ»; выдуманные показы Wordstat; цифры «500–2000 строк/сек» из обзоров — только как ориентир с атрибуцией deeone, не как гарантия УНФ клиента.

**Fact-bank:** релевантных строк по 1С/Excel в `memory/brief/fact-bank.md` нет — опираться на таблицу выше + практику B13 (сущности УНФ ДДС), без новых выдуманных имён полей.

---

## Структура H2/H3 для writer (спека)

Следовать карточке B37; наполнение под регулярность.

### H2: Когда это нужно финотделу (и когда нет)
- Боль: ежедневное «Сохранить как» из отчёта УНФ → копипаст в книгу.
- Нужно: один и тот же срез каждое утро / каждый час в Excel.
- Не нужно: разовая миграция номенклатуры Excel→1С; BI на миллионы строк (звать экстрактор/SQL).
- Рекомендация: если канала OData ещё нет — сначала B13 / админ, потом эта статья.

### H2: Подготовка данных и безопасность
- Список полей и период; staging `raw_*`.
- Отдельный пользователь, узкий состав OData / метод HTTP.
- Не тащить ПДн; линк на обезличивание.
- Рекомендация: `$filter` по дате + `$top` на дымовом тесте.

### H2: Три схемы регулярного импорта (выбрать одну)
Таблица comparison:
| Схема | Когда | Ограничение |
| --- | --- | --- |
| A. Power Query + свойства refresh | Книга открыта у финансиста днём | Нет обновления при закрытом файле |
| B. Скрипт / планировщик → CSV/XLSX → PQ из папки | Нужен cron «в 7:00», ПК/сервер доступен | Нужен хост для скрипта |
| C. HTTP-сервис УНФ (готовый JSON) + PQ/скрипт | Сложный срез/агрегат, OData неудобен | Нужен 1С-ник на сервис |

Кратко шаги для A (основной путь статьи) и чеклист для B/C.

### H2: Пошаговая настройка схемы A (Excel Desktop)
1. URL сущности (или файл из папки после B).
2. Данные → OData / из веба / из папки.
3. Преобразования: типы, даты, удаление служебных колонок.
4. Свойства: обновлять при открытии; опционально каждые N минут.
5. «Обновить всё» → контрольная сумма vs УНФ.

### H2: Проверка результата и типичные ошибки
- 401/403 после смены пароля.
- Таймаут / пустой `$top` слишком маленький.
- Excel Online / облачный Power Automate «успех без обновления».
- Раздувание запроса без `$filter`.
- Рекомендация: лог даты последнего успешного refresh на отдельном листе.

### H2: Что автоматизировать дальше
- Staging → дашборд / Google Sheets (паттерн B13).
- n8n только как опция, не ядро статьи.
- CTA: Telegram + клуб (по conversion-map, ≤3).

### FAQ (действие, не пересказ)
- Можно ли без программиста? — Схема A после публикации OData (админ один раз); схема C — нет.
- Сколько займёт? — Канал 0,5–2 ч если OData уже есть; регламент скрипта — полдня с тестами.
- Риски для данных? — Широкий состав OData + учётка в файле Excel; лечится узким составом и отдельным пользователем.
- Чем не дублирует B13? — B13 = подключить канал; B37 = сделать его **ежедневным** без ручных выгрузок.
- Excel Online сам обновит? — Нет надёжного авто-refresh обычного PQ к УНФ; Desktop или скрипт.

---

## Internal links / CTA hints

- `/blog/vygruzka-1c-excel-odata/` (B13) — обязательно в лиде/H2 «когда канала ещё нет»
- `/obezlichivanie-dannyh-chatgpt-finansist/`
- `/avtomatizaciya-finansov-no-code/`
- Не каннибализировать будущий B30: общие азы PQ — в 1–2 предложениях, без отдельного туториала «что такое Power Query»

---

## Blockers

- Wordstat: **unavailable** (нет MCP `user-mcp-kv`) — не блокер публикации статьи, но цифры спроса в текст не ставить.
- Research sources: **достаточны** для how-to (официальный OData + Excel refresh + обзоры 2026 + отстройка от B13).
- `❌ RESEARCH BLOCKER` — нет.
