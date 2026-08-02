# Research notes — B36

**topic_id:** B36  
**slug:** dashbord-dds-looker-studio  
**h1:** Как собрать дашборд ДДС в Looker Studio из Google Sheets за час  
**research_date:** 2026-08-02  
**publish_target:** сайт koda-fd.ru/blog  
**utility_gate:** PASS (`how_to`, mode B) — повторно подтверждён `excalibur_blog_utility_gate.py --topic-id B36`  
**related_published:** `/spravochnik-kategorij-dds/` (B29), `/bankovskaya-vypiska-staging-google-sheets/` (B25), `/google-apps-script-finansist-obnovit-dannye/` (B22), `/obezlichivanie-dannyh-chatgpt-finansist/` (B11), `/avtomatizaciya-finansov-no-code/`, `/disnejlend-dlya-dannyh/`  
**internal_links (из карточки + смежные):** `/avtomatizaciya-finansov-no-code/`, `/obezlichivanie-dannyh-chatgpt-finansist/`, `/spravochnik-kategorij-dds/`, `/bankovskaya-vypiska-staging-google-sheets/`, `/google-apps-script-finansist-obnovit-dannye/`

---

## utility_verdict

**PASS** — тема utility-only how-to (mode B). Читатель получает пошаговый маршрут: подготовить «длинный» лист операций ДДС в Google Sheets (без ПДн), подключить нативный коннектор Looker Studio, вывести KPI/графики/таблицу по статьям, проверить свежесть данных и расшарить отчёт собственнику. Не новость про маркетинг-дашборды, не обзор «что такое Looker Studio».

---

## reader_outcome

После гайда CFO или финансист малого финотдела за ~1 час соберёт рабочий дашборд ДДС в Looker Studio (lookerstudio.google.com) из листа Google Sheets: scorecards (притоки / оттоки / чистый поток), динамика по дням/неделям, топ статей расходов, фильтр по дате и счёту — с автообновлением не реже чем раз в 15 минут и без программиста.

---

## action_outline

1. **Решить, когда Looker Studio уместен** — есть уже «длинный» лист операций в Sheets (дата, направление, статья, сумма, счёт); нужен экран для собственника, а не ещё один Excel-свод. Не стартовать, если справочник категорий ещё хаос (сначала B29).
2. **Подготовить лист «Операции_DDS»** — отдельный worksheet только под дашборд: табличный формат, одна строка = одно движение денег; без объединённых ячеек, итоговых строк Totals и картинок; даты как Date (полный день-месяц-год); структура long, не wide (статья в колонке, не отдельные колонки под каждую статью).
3. **Обезличить данные перед облаком** — убрать ФИО сотрудников, полные реквизиты, сырые назначения платежей с ПДн; оставить код/название статьи, сумму, дату, счёт (алиас), опционально тип контрагента. Credentials: для просмотра командой — Owner's Credentials осознанно.
4. **Подключить Google Sheets в Looker Studio** — Create → Data source → коннектор Google Sheets → выбрать файл и лист (один worksheet на источник) → Use first row as headers → CONNECT; проверить типы: Date = Date, Сумма = Number (SUM), Статья/Счёт = Text.
5. **Добавить calculated fields для ДДС** — `Приток` / `Отток` / `Чистый_поток` через CASE по колонке «направление» (приход/расход/перевод); переводы между счетами не считать доходом/расходом.
6. **Собрать холст за час** — Date range control; 3–4 scorecards (приток, отток, чистый поток, остаток если есть входной баланс); time series по чистому потоку; bar chart топ-10 статей расходов; table по статьям × месяц; filter control по счёту и группе статей.
7. **Проверить свежесть и схему** — Data freshness для Sheets: 15 мин (default) / 1 ч / 4 ч / 12 ч; после смены колонок в Sheets — Refresh fields у источника; перед совещанием — ручной Refresh data (cooldown 1 мин).
8. **Проверка сходимости** — сумма по дашборду за период = SUMIF по листу Операции; остаток конец ≈ начало + чистый поток (если ведёте остатки); типичные ошибки: Totals-строка в источнике, mixed types в сумме, wide-таблица статей.
9. **Шаринг и следующий шаг автоматизации** — Share отчёта view-only собственнику; Schedule delivery (PDF по расписанию); дальше — автоподливка из staging-выписки (B25) / кнопка обновления Apps Script (B22), не ручной копипаст.

---

## Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT unavailable:** сервер MCP `user-mcp-kv` в этой сессии **не подключён** (в каталоге MCP доступен только `cursor-cloud`, инструментов `wordstat_*` нет). Точные показы/мес **не получены** и **не выдуманы**. При появлении MCP-KV: вызвать `wordstat_get_top_requests` для `дашборд ддс looker studio`, `looker studio google sheets`, `дашборд ддс google sheets`. Авторизация Wordstat (если 401): https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

**Экспертная семантика (без цифр спроса) — LSI для копирайтера:**

| Кластер | Фразы | Роль |
| --- | --- | --- |
| Primary | дашборд ддс looker studio, дашборд ддс google data studio | H1, title |
| Sheets | looker studio google sheets, подключить google таблицы looker studio | H2 коннектор |
| Методология ДДС | отчет ддс дашборд, cash flow dashboard, статьи ддс визуализация | лид, структура виджетов |
| Автоматизация | автоматизация финотдела, управленческий дашборд looker studio | secondary, CTA внутрь контура |
| Смежные BI | looker studio vs power bi, datalens ддс | FAQ «когда не Looker» |
| Техника | data freshness looker studio, calculated fields looker studio, schedule delivery | H2 проверка / что дальше |

**SEO-вывод:** preflight `research-serp.json` по «дашборд ддс looker studio» уводит в **маркетинговые** гайды Looker Studio (Метрика/Директ/VK Ads) — релевантны по продукту, **не** по ДДС. Прямых how-to «ДДС → Looker Studio из Sheets за час» почти нет (есть фриланс-оффер FreeWorker и шаблоны управленки в Sheets). **serp_gap КОДА:** финансовый how-to для финотдела РФ — лист операций ДДС + коннектор Sheets + виджеты cash flow + ПДн/credentials + связка со справочником категорий и staging-выпиской.

---

## SERP (WebSearch Cursor, 02.08.2026)

> Preflight `research-serp.json` учтён как черновик; приоритет — живой WebSearch. Запрос `secondary_3: 2026 2026` из карточки — мусор (календари/Википедия), игнорирован.

### Primary: `дашборд ддс looker studio` / `дашборд ДДС Looker Studio Google Sheets`

| # | URL | Тип | Пробел для КОДА |
| --- | --- | --- | --- |
| 1 | https://freeworker.su/market/business/gotovyj-biznes/otchet-dds-s-vizualizaciej-dannyx-v-google-data-studio | Услуга: ДДС + Data Studio | Есть состав виджетов; нет пошагового DIY за час |
| 2 | https://docs.cloud.google.com/data-studio/connect-to-google-sheets | Официальный коннектор Sheets | Техника без финконтекста ДДС |
| 3 | https://docs.cloud.google.com/data-studio/tutorial-create-a-google-sheets-data-source | Tutorial: подготовка Sheets | Long vs wide, без Totals — критично для ДДС |
| 4 | https://docs.cloud.google.com/data-studio/manage-data-freshness | Data freshness | Интервалы 15 мин–12 ч для Sheets |
| 5 | https://pravda-ads.ru/blog/dashbord-looker-studio-gajd | Общий гайд Looker 2026 | Маркетинг-фокус |
| 6 | https://dipustovalov.ru/blog/looker-studio-marketing-2026 | Маркетинг-дашборд 2026 | Sheets как слой для Директа/VK; не ДДС |

### Secondary: `автоматизация финотдела` / управленческий дашборд

| # | URL | Тип | Пробел для КОДА |
| --- | --- | --- | --- |
| 7 | https://datalopata.ru/blog/avtomatizatsija-finansov-sistemnyj-podhod-k-uchetu-v-2026-godu/ | Автоматизация финансов 2026 | cash flow в приоритете; нет Looker-шагов |
| 8 | https://www.get-started-int.com/post/about-looker-studio | Управленческий дашборд Looker | Общий обзор; Sheets как ручные данные |
| 9 | https://media.klyasyuk.ru/google-looker-studio-marketing-dashboard-guide/ | Маркетинг за 1 день | Паттерн «Sheets → Looker за минуты» |
| 10 | https://osipenkov.ru/connectors-looker-studio/ | Коннекторы RU | Пошаговое добавление листа Sheets в отчёт |
| 11 | https://blog.coupler.io/how-to-connect-google-sheets-to-looker-studio/ | Sheets ↔ Looker | Freshness ≥15 мин; рекомендации по интервалу |

### Secondary: техника Looker Studio

| # | URL | Тип | Пробел для КОДА |
| --- | --- | --- | --- |
| 12 | https://cloud.google.com/looker/docs/studio/refresh-data-source-fields | Refresh fields | Смена схемы Sheets не подхватывается сама |
| 13 | https://docs.cloud.google.com/data-studio/schedule-automatic-report-delivery | Schedule delivery | PDF/CSV по расписанию собственнику |
| 14 | https://netpeak.net/ru/blog/kak-ob-yedinit-istochniki-dannykh-v-google-looker-studio/ | Data blending | На потом: план + факт на разных листах |
| 15 | https://discuss.google.dev/t/real-time-data-sync-between-google-sheets-and-looker-studio/192167/1 | Q&A 2025 | Нет realtime; минимум 15 мин + ручной refresh |

### H1: «Как собрать дашборд ДДС в Looker Studio из Google Sheets за час»

Прямых статей с таким H1 **нет**. Ближайшие: маркетинг «за 1 час/день» + фриланс-пакет ДДС+Data Studio. **serp_gap КОДА:** DIY за час для финотдела — от чистого листа операций до scorecards ДДС, с ПДн и связкой на справочник категорий / staging.

---

## Таблица фактов (только с URL; для writer)

| # | Утверждение | Источник | Дата проверки |
| --- | --- | --- | --- |
| 1 | Коннектор Google Sheets в Looker Studio (Data Studio) подключается к **одному worksheet** в таблице. | https://docs.cloud.google.com/data-studio/connect-to-google-sheets | 2026-08-02 |
| 2 | Данные должны быть в **табличном формате**; заголовок — **одна строка**; все ячейки в колонке — **одного типа**. | https://docs.cloud.google.com/data-studio/connect-to-google-sheets | 2026-08-02 |
| 3 | Рекомендуется **отдельный worksheet** под данные для Looker Studio (не смешивать с «красивыми» сводами). | https://docs.cloud.google.com/data-studio/tutorial-create-a-google-sheets-data-source | 2026-08-02 |
| 4 | **Merged cells**, графики и изображения в диапазоне ломают/искажают импорт. | https://docs.cloud.google.com/data-studio/tutorial-create-a-google-sheets-data-source | 2026-08-02 |
| 5 | Формат данных: **long лучше wide** (категория в колонке «Статья», а не отдельная колонка на каждую статью) — иначе фильтры и графики по статьям невозможны. | https://docs.cloud.google.com/data-studio/tutorial-create-a-google-sheets-data-source | 2026-08-02 |
| 6 | Строку **Totals** в источнике не включать: Looker просуммирует её вместе с деталями и **раздует** KPI. | https://docs.cloud.google.com/data-studio/tutorial-create-a-google-sheets-data-source | 2026-08-02 |
| 7 | Даты в Sheets должны содержать **полный день, месяц и год** и быть отформатированы как Date (`Format → Number → Date`). | https://docs.cloud.google.com/data-studio/tutorial-create-a-google-sheets-data-source | 2026-08-02 |
| 8 | Data freshness для Google Sheets: **каждые 15 минут (default)**, 1 час, 4 часа или 12 часов. | https://docs.cloud.google.com/data-studio/manage-data-freshness | 2026-08-02 |
| 9 | Редактор отчёта может **вручную** обновить данные; cooldown между ручными refresh — **1 минута**. | https://docs.cloud.google.com/data-studio/manage-data-freshness | 2026-08-02 |
| 10 | При смене структуры колонок в Sheets Looker **не детектит схему сам** — нужен **Refresh fields** у data source. | https://cloud.google.com/looker/docs/studio/refresh-data-source-fields | 2026-08-02 |
| 11 | Credentials: **Owner's** — зрители видят данные без своего доступа к Sheets; **Viewer's** — каждому нужен свой доступ к таблице. | https://docs.cloud.google.com/data-studio/connect-to-google-sheets | 2026-08-02 |
| 12 | Можно подключаться к таблице по **URL**, если есть доступ; либо к файлам, которыми владеете / которые вам расшарили. | https://docs.cloud.google.com/data-studio/connect-to-google-sheets | 2026-08-02 |
| 13 | Для дашборда ДДС в Data Studio/Looker типичный набор вводных: **счета**, **статьи доходов/расходов**, **контрагенты**, доступ к Google-аккаунту. | https://freeworker.su/market/business/gotovyj-biznes/otchet-dds-s-vizualizaciej-dannyx-v-google-data-studio | 2026-08-02 |
| 14 | Типовая визуализация ДДС: блоки **выручка / переменные / постоянные расходы** за месяц, анализ статей расходов, соотношение расходов и выручки, таблица по месяцам. | https://freeworker.su/market/business/gotovyj-biznes/otchet-dds-s-vizualizaciej-dannyx-v-google-data-studio | 2026-08-02 |
| 15 | Услуга «таблица ДДС + визуализация в Google Data Studio» на маркетплейсе оценивается от **4 500 ₽** / срок около **7 дней** (ориентир рынка DIY vs подряд). | https://freeworker.su/market/business/gotovyj-biznes/otchet-dds-s-vizualizaciej-dannyx-v-google-data-studio | 2026-08-02 |
| 16 | Google Sheets — **универсальный промежуточный слой**, если нет нативного коннектора; подключение Sheets в Looker — порядка **десятков секунд** после подготовки данных (оценка практиков). | https://media.klyasyuk.ru/google-looker-studio-marketing-dashboard-guide/ | 2026-08-02 |
| 17 | Минимальный интервал автообновления Sheets→Looker — **15 минут**; чаще (realtime каждую минуту) **недоступно**. | https://discuss.google.dev/t/real-time-data-sync-between-google-sheets-and-looker-studio/192167/1 | 2026-08-02 |
| 18 | Рекомендация практиков: если не нужен near-real-time, ставить freshness **1 час** — реже дёргать источник и меньше тормозов. | https://blog.coupler.io/how-to-connect-google-sheets-to-looker-studio/ | 2026-08-02 |
| 19 | Schedule delivery: регулярная рассылка отчёта **PDF** (снимок страниц) или **CSV** (данные чартов) + превью первой страницы и ссылка на отчёт. | https://docs.cloud.google.com/data-studio/schedule-automatic-report-delivery | 2026-08-02 |
| 20 | Денежные потоки в ОДДС (ПБУ 23/2011) делятся на **текущие, инвестиционные и финансовые** — удобная группировка верхнего уровня на дашборде (из fact-связки B29). | https://vse-ob-1c.ru/oplata/pbu-denezhnye-sredstva-2.html | 2026-08-02 |
| 21 | Для старта ДДС достаточно **5–7 статей поступлений** и **10–15 статей платежей** (не раздувать справочник перед дашбордом). | https://monuchet.ru/spravochnik/dds-dlya-sobstvennika-na-1-liste/ | 2026-08-02 |
| 22 | Принцип учёта: **одна строка = одно движение денег**; поля минимум: дата, тип (доход/расход/перевод), категория, сумма, счёт. | https://store.birdyx.ru/article/tablica-dds-google-sheets-uchet-deneg | 2026-08-02 |
| 23 | Контроль: **остаток конец = остаток начало + чистый денежный поток**; расхождение → искать пропуск/дубль в операциях. | https://monuchet.ru/spravochnik/dds-dlya-sobstvennika-na-1-liste/ | 2026-08-02 |
| 24 | В 2026 в приоритете автоматизации финотдела — классификация платежей, сверки, управленческая отчётность, **прогноз cash flow**. | https://datalopata.ru/blog/avtomatizatsija-finansov-sistemnyj-podhod-k-uchetu-v-2026-godu/ | 2026-08-02 |

---

## Угол КОДА (дифференциация)

| Конкурент | Что делает | Чего не даёт |
| --- | --- | --- |
| Маркетинг-гайды Looker 2026 | Метрика/Директ/Ads → дашборд | ДДС, статьи, переводы между счетами |
| FreeWorker / подрядчики | Готовый пакет ДДС+Data Studio за деньги | Пошаговый DIY + ПДн + связка со справочником |
| Шаблоны управленки в Sheets | ОДДС внутри таблицы | Looker как экран для собственника, freshness, sharing |
| Официальные docs Google | Коннектор и freshness | Финансовая методология и чеклист ошибок ДДС |

**Позиционирование статьи:** «Sheets = data foundation (Disneyland), Looker = витрина для решений». Час хватает **если** справочник категорий уже есть (B29) и операции в long-формате; иначе сначала 30–60 мин на лист. Без программиста; дальше — staging выписки и Apps Script, не Power BI на старте.

---

## FAQ hints (ответы-действия)

| Вопрос | Направление ответа |
| --- | --- |
| Можно ли без программиста? | Да: нативный коннектор Sheets → Create report; формулы CASE в calculated fields; Apps Script только для автоподливки данных |
| Сколько займёт внедрение? | При готовом листе операций — **≈1 час** на первый дашборд; если нет справочника/long-таблицы — сначала 0,5–1 день data foundation |
| Какие риски для данных? | Owner's Credentials открывают данные всем с ссылкой на отчёт; не класть ПДн/полные назначения; отдельная копия листа «для BI» |
| Looker или просто Sheets-дашборд? | Sheets — для ввода и контроля; Looker — фильтры, шаринг view-only, schedule PDF собственнику |
| Что с переводами между счетами? | Отдельное направление «перевод»; не суммировать в приток/отток, иначе раздуется оборот |
| Почему цифры «не те»? | Totals в листе, текст в сумме, wide-колонки статей, не обновлены fields после смены схемы, кэш freshness |

---

## Writer constraints

- **article_mode:** B only; CTA клуб/Telegram ≤ 3
- **Цифры:** только из таблицы фактов выше; Wordstat-цифр **нет** — не выдумывать частотность
- **H2 из карточки:** (1) когда нужно финотделу (2) подготовка данных и ПДн (3) пошаговая сборка дашборда (4) проверка и типичные ошибки (5) что автоматизировать дальше
- **Тон:** Ольга Кондрацкая, практик; кириллица; без эмодзи; без длинного тире «—» в тексте статьи (по контракту писателя)
- **Не копировать** структуру маркетинговых гайдов 1:1; фокус на ДДС-метриках и финансовом контуре КОДА
- **Запрет:** обещать realtime чаще 15 мин; обещать «без Google-аккаунта»

---

## Источники preflight

`research-serp.json` — частично релевантен (Looker how-to 2026, автоматизация финотдела); **слаб по ДДС**. Использован как карта URL; факты перепроверены WebSearch/WebFetch 2026-08-02. Запрос `2026 2026` из secondary — отброшен.
