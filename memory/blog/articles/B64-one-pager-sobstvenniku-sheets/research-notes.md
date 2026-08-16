# Research notes — B64

**topic_id:** B64  
**slug:** one-pager-sobstvenniku-sheets  
**h1:** Как собрать one-pager для собственника из Sheets: 1 экран, 5 цифр  
**research_date:** 2026-08-16  
**publish_target:** koda-fd.ru/blog  
**utility_gate:** PASS (`how_to`, mode B)  
**author_id:** olga-kondratskaya  
**related_published:** `/avtomatizaciya-finansov-no-code/`, `/obezlichivanie-dannyh-chatgpt-finansist/`, B27 (дайджест в Telegram)  
**internal_links (карточка):** `/avtomatizaciya-finansov-no-code/`, `/obezlichivanie-dannyh-chatgpt-finansist/`  
**cover_scene_hint:** abstract holographic finance automation dark #0a0a0f purple #8b5cf6, no text

---

## utility_verdict

**PASS** — тема utility-only how-to (mode B). Читатель за 2–4 часа собирает в Google Sheets отдельный лист «One-pager»: пять управленческих цифр на одном экране (деньги, поток, выручка, риск ДЗ, план-факт или платежи 7 дней), формулы с staging-листов, светофор отклонений и правила без сырых ПДн — без BI, без программиста на первом шаге.

---

## reader_outcome

После гайда финансист или CFO сможет собрать в Google Sheets лист one-pager для собственника: выбрать пять метрик под решения владельца, подтянуть их формулами из staging (банк, ДДС, план-факт), оформить один экран со «светофором» и чеклистом проверки — чтобы собственник за 5 минут понял «в порядке / есть проблема», без бухгалтерской простыни и без выгрузки ПДн в публичные сервисы.

---

## action_outline

1. **Когда one-pager нужен (и когда нет)** — собственник не читает 40 вкладок, но хочет пульс раз в неделю → one-pager в Sheets; уже есть DataLens/Power BI и команда аналитики → не дублировать; нужен push в Telegram → см. B27 (дайджест); one-pager для инвесторов/стартапа → другой intent (SERP-ловушка).
2. **Подготовка данных и безопасность** — staging-листы (`cash`, `dds`, `plan_fact`, `ar`) с кодами контрагентов; в one-pager только агрегаты; без ИНН/ФИО/полных выписок на листе «owner»; доступ «только просмотр» для собственника; линк на обезличивание (B11).
3. **Выбор 5 цифр** — зафиксировать контракт: (1) остаток денег, (2) чистый поток за период, (3) выручка MTD/WTD, (4) просроченная ДЗ или DSO, (5) план-факт одной строкой **или** платежи 7–14 дней; + строка «вопрос недели» опционально, не шестая «цифра».
4. **Структура книги** — листы: `Справочник` → `staging_*` → `one_pager` (единственный экран для собственника); metric_key латиницей (`cash_end`, `net_cf`, `rev_mtd`, `ar_overdue`, `plan_fact_pct`); freeze header, скрыть служебные листы.
5. **Формулы one-pager** — value = SUMIFS/ссылки на staging, не ручной ввод; `plan_fact_pct` = (факт−план)/план; `wow_delta` к прошлой неделе; SPARKLINE или мини-график только если не ломает «один экран»; условное форматирование зел/жёлт/крас по порогам из `Справочник!thresholds`.
6. **Визуал «1 экран»** — верхняя строка: деньги + поток; середина: выручка + маржа/план-факт; справа: риск (ДЗ/платежи); не более 10–12 виджетов на листе (правило ADPASS); тест «3 секунды» — понятен ли статус.
7. **Проверка результата** — сверка остатка с банком; контроль формул (базовый период, единая валюта, НДС/без НДС); 3–5 строк ручной выборки; собственник открывает с телефона — всё читается без зума; нет #REF! после переименования листов.
8. **Типичные ошибки** — путать one-pager с pitch-deck для инвесторов; тащить бухотчёт вместо управленки; менять состав 5 цифр каждую неделю; 25 метрик «на всякий случай»; сырые выписки на том же листе; разные определения «выручки» в CRM и 1С без словаря метрик.
9. **Что автоматизировать дальше** — n8n/Make: банк → staging (статья no-code); еженедельный Telegram-digest с теми же ключами (B27); Apps Script для автообновления; DataLens — когда Sheets перестаёт хватать по объёму.

---

## Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT AUTH WARNING:** сервер MCP `user-mcp-kv` в этой Cloud-сессии **не подключён** (доступен только `cursor-cloud`). Вызов `wordstat_get_top_requests` **не выполнен**. Точные показы/мес **не получены** и **не выдуманы**.

Обновление токена: https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

**Экспертная семантика (LSI для writer, без цифр спроса):**

| Кластер | Фразы |
| --- | --- |
| Ядро | one pager для собственника, дашборд собственника, one pager финансы |
| Sheets | google sheets дашборд собственника, one pager google sheets, управленческий дашборд таблица |
| Метрики | 5 ключевых показателей собственник, план факт собственник, cash flow дашборд |
| Автоматизация | автоматизация финотдела, staging google sheets, дайджест собственнику |
| Ловушка SERP | one pager стартап инвесторам, one pager generator, pitch deck one page — **другой intent** |

**SEO-вывод:** `primary_query` в preflight-SERP **загрязнён** стартап-pitch (Happycapy, PitchBob, FeoFinance, Visme). Живой WebSearch даёт кластер «дашборд собственника / 1 экран / KPI». Прямого «one-pager **из Google Sheets** → 5 цифр → пошагово» почти нет — конкуренты продают BI, шаблоны или Telegram. Угол КОДА: **Sheets one-pager + staging + 5 метрик + безопасность + мост B27/no-code**.

---

## SERP (WebSearch Cursor, 16.08.2026)

`research-serp.json` (шаг 0) по `primary_query` **нерелевантен** (генераторы pitch-deck) — дополнен живым WebSearch.

### Primary: one pager для собственника финансы

| # | URL | Тип | Пробел для КОДА |
| --- | --- | --- | --- |
| 1 | https://genad.ru/dashboard-sobstvennika-161/ | дашборд собственника | Блоки метрик есть; нет Sheets, нет «5 цифр», продаёт услугу |
| 2 | https://adpass.ru/dashbordy-dlya-sobstvennika-i-ropa-kak-perestat-gadat-i-nachat-upravlyat-za-5-minut-v-den/ | BI/дашборды 2026 | Принципы 5 мин/нед, ≤10–12 метрик, светофор; Power BI, не Sheets |
| 3 | https://gse.kz/blog/dashbord-sobstvennika-kpi-istochniki-dannykh | KPI + источники | «1 экран», словарь метрик, DSO; enterprise-проект, не DIY Sheets |
| 4 | https://noboring-finance.ru/gazeta/glossariy-otchety-dlya-sobstvennikov/page2/7/ | отчёты собственника | Концепция «личный дашборд»; без инструкции в таблице |
| 5 | https://dzen.ru/a/anBLF2tbQE6qYile | DataLens | 5–10 денежных показателей; Yandex DataLens, не Sheets |
| 6 | https://happycapy.ai/ru/tools/one-pager-generator | AI generator | **Ловушка:** pitch для продукта, не CFO |
| 7 | https://feofinance.com/blog/tpost/ef7zjnl811-primeri-one-pager | примеры one pager | Стартап/продукт, не управленка |

### H1 / Sheets / one-pager

| # | URL | Тип | Пробел для КОДА |
| --- | --- | --- | --- |
| 8 | https://tableprof.ru/ | шаблон Finance | P&L, dashboard собственника за 3–7 дней — **платный** шаблон |
| 9 | https://excel.birdyx.ru/blog/show/uchet-biznesa-google-sheets | учёт в Sheets | Дашборд KPI на одном экране; нет «5 цифр для собственника» |
| 10 | https://xn--80acea1apc7cg1b5c.xn--p1ai/upruchetsdashbordom | УУ + дашборд | Блоки ОПУ/ОДДС; продажа шаблона, не one-pager workflow |
| 11 | https://peroksa.ru/guides/business-financials | шаблон P&L | Google Sheets/Excel; нет роли «собственник за 5 минут» |
| 12 | https://dzen.ru/a/am1bDGtbQE6qWNrS | дайджест Sheets→TG | Близкий контент KODA (B27); B64 = **экран в Sheets**, не push |
| 13 | https://koda-fd.ru/blog/avtomatizaciya-finansov-no-code/ | свой блог | staging, bank→dashboard; перелинковка |
| 14 | https://getfiledrop.com/how-to-build-a-financial-dashboard-in-google-sheets/ | EN how-to | Общий financial dashboard; KPI-список, без owner one-pager RU |

### Secondary: автоматизация финотдела 2026

| # | URL | Тип | Пробел для КОДА |
| --- | --- | --- | --- |
| 15 | https://koda-fd.ru/blog/ai-dlya-finansista-2026/ | свой блог | Что автоматизировать; H2 «дальше» |
| 16 | https://datalopata.ru/blog/avtomatizatsija-finansov-sistemnyj-podhod-k-uchetu-v-2026-godu/ | автоматизация 2026 | Классификация, cash flow; без one-pager |
| 17 | https://developers.google.com/workspace/sheets/api/guides/batch | Google Sheets API | batchUpdate, атомарность — для блока Apps Script «дальше» |
| 18 | https://habr.com/ru/articles/1017260/ | Sheets API + агенты | Верификация после batch-записи; не one-pager UI |

**serp_gap КОДА:** пошаговый workflow «staging в Sheets → выбор 5 метрик → лист one_pager → формулы SUMIFS → светофор → проверка → без ПДн» на **русском** для финансиста без BI-команды.

**Cannibalization:** B27 = Telegram digest; B64 = **визуальный one-pager в Sheets**; `/avtomatizaciya-finansov-no-code/` = архитектура staging; не дублировать n8n-расписание из B27 в центре статьи.

---

## Таблица фacts (только с URL; для writer)

| # | Утверждение | Источник | Дата проверки |
| --- | --- | --- | --- |
| 1 | Дашборд собственника должен показывать выручку (день/неделя/месяц), прибыль, расходы, cash flow, план/фact; **собственнику не нужен бухгалтерский отчёт** — нужна понятная управленческая картина. | https://genad.ru/dashboard-sobstvennika-161/ | 2026-08-16 |
| 2 | Цель дашборда собственника — за **~5 минут** понять состояние бизнеса и принять решение. | https://genad.ru/dashboard-sobstvennika-161/ | 2026-08-16 |
| 3 | Задача дашборда собственника — однозначный ответ: «всё в порядке» или «есть проблема»; метрики можно оценить за **5 минут раз в неделю**. | https://adpass.ru/dashbordy-dlya-sobstvennika-i-ropa-kak-perestat-gadat-i-nachat-upravlyat-za-5-minut-v-den/ | 2026-08-16 |
| 4 | Правило ADPASS: если на экране **больше 10–12 ключевых метрик**, дашборд перестаёт работать; один дашборд = один вопрос. | https://adpass.ru/dashbordy-dlya-sobstvennika-i-ropa-kak-perestat-gadat-i-nachat-upravlyat-za-5-minut-v-den/ | 2026-08-16 |
| 5 | Для индикации отклонений — принцип «светофор»: зелёный норма, жёлтый внимание, красный — вмешательство. | https://adpass.ru/dashbordy-dlya-sobstvennika-i-ropa-kak-perestat-gadat-i-nachat-upravlyat-za-5-minut-v-den/ | 2026-08-16 |
| 6 | Финансовый блок собственника: выручка, валовая и чистая прибыль, денежный поток с отклонениями от плана. | https://adpass.ru/dashbordy-dlya-sobstvennika-i-ropa-kak-perestat-gadat-i-nachat-upravlyat-za-5-minut-v-den/ | 2026-08-16 |
| 7 | Формат «1 экран» — короткий набор цифр для просмотра **раз в день или раз в неделю**, по которым понятно, что делать дальше. | https://gse.kz/blog/dashbord-sobstvennika-kpi-istochniki-dannykh | 2026-08-16 |
| 8 | На one-pager по деньгам достаточно двух уровней прибыли: **валовая маржа** (после себестоимости) и **операционная прибыль** (после основных расходов) — больше видов → споры на планерке. | https://gse.kz/blog/dashbord-sobstvennika-kpi-istochniki-dannykh | 2026-08-16 |
| 9 | Ранние сигналы кассового разрыва: остаток падает **2–3 периода подряд**; просрочка ДЗ растёт; платежи на **7–14 дней** «съедают» большую долю остатка. | https://gse.kz/blog/dashbord-sobstvennika-kpi-istochniki-dannykh | 2026-08-16 |
| 10 | Источники финдашборда: **1С/ERP**, **CRM**, **банк**, склад, HR; нужен **владелец** каждого источника (бизнес-роль). | https://gse.kz/blog/dashbord-sobstvennika-kpi-istochniki-dannykh | 2026-08-16 |
| 11 | Отчёты собственника — «личный дашборд» без лишних строк: сколько заработал бизнес, сколько денег доступно, какие направления тянут вниз. | https://noboring-finance.ru/gazeta/glossariy-otchety-dlya-sobstvennikov/page2/7/ | 2026-08-16 |
| 12 | Рабочий принцип панели: **5–10 денежных показателей** в цепочке расход → лид → сделка → оплата → маржа; метрика без решения о бюджете на экране не нужна. | https://dzen.ru/a/anBLF2tbQE6qYile | 2026-08-16 |
| 13 | Staging (промежуточная таблица) — обязательный слой: без него workflow множатся и CEO не доверяет цифрам (архитектура bank → staging → dashboard). | https://koda-fd.ru/blog/avtomatizaciya-finansov-no-code/ | 2026-08-16 |
| 14 | Кейс KODA: сбор ДДС сократился с **20 часов до 15 минут** в месяц после staging + n8n (контекст «зачем формулы, а не копипаст»). | https://koda-fd.ru/blog/avtomatizaciya-finansov-no-code/ | 2026-08-16 |
| 15 | До **63%** сотрудников тайно копируют финданные в публичные чаты ИИ; штрафы по **152-ФЗ** — до **6 млн ₽** (контекст безопасности Sheets). | https://koda-fd.ru/blog/obezlichivanie-dannyh-chatgpt-finansist/ | 2026-08-16 |
| 16 | Google Sheets API: subrequests в batchUpdate применяются **атомарно** — если один невалиден, **весь** batch не применяется. | https://developers.google.com/workspace/sheets/api/guides/batch | 2026-08-16 |
| 17 | Google рекомендует **батчить** несколько запросов в один вызов API для снижения round-trips. | https://developers.google.com/workspace/sheets/api/guides/batch | 2026-08-16 |
| 18 | Habr-кейс: после batch-записи в Sheets нужно **перечитать и сверить** — API может «терять» строки (пример: записали 100, в таблице 97). | https://habr.com/ru/articles/1017260/ | 2026-08-16 |
| 19 | TableProf Finance: шаблон P&L + Cashflow + dashboard собственника; заявленный срок внедрения шаблона **3–7 дней** (конtrast DIY one-pager за день). | https://tableprof.ru/ | 2026-08-16 |
| 20 | Birdyx-шаблон: дашборд в Google Sheets с выручкой, прибылью, заказами, средним чеком — «вся суть на одном экране». | https://excel.birdyx.ru/blog/show/uchet-biznesa-google-sheets | 2026-08-16 |

**Не выдумывать:** точные показы Wordstat; «one-pager снижает кассовые разрывы на X%»; цены TableProf/шаблонов без актуальной проверки на дату публикации; что one-pager заменяет управленческий учёт в 1С.

**fact-bank.md:** прямых фактов по one-pager/дашборду собственника нет — цифры только из таблицы выше + перекрёстно B11/KODA (факты 15).

---

## Структура H2 для writer (из карточки B64)

1. Когда это нужно финотделу (и когда нет)  
2. Подготовка данных и безопасность (без сырых ПДн в облако)  
3. Пошаговая настройка листа one_pager / формулы / макет  
4. Проверка результата и типичные ошибки  
5. Что автоматизировать дальше  
+ FAQ + CTA

## FAQ-кандидаты (из карточки + SERP)

- Можно ли без программиста? (да — формулы; Apps Script опционально)  
- Сколько займёт первое внедрение? (ориентир **2–4 ч** на staging + one-pager при готовых данных)  
- Какие риски для данных в Google Sheets? (ПДн, доступы, 152-ФЗ → B11)  
- Чем one-pager отличается от дашборда в DataLens/Power BI?  
- Чем отличается от еженедельного дайджеста в Telegram? (B27)  
- Какие именно 5 цифр выбрать для производства / услуг / e-com?  
- Нужен ли один лист или можно PDF/print area?

## CTA / interlink

- CTA: club.koda-fd.ru (`?utm_source=blog&utm_medium=article&utm_campaign=one-pager-sobstvenniku-sheets`), t.me/finance_modern (≤2)  
- Internal: `/avtomatizaciya-finansov-no-code/`, `/obezlichivanie-dannyh-chatgpt-finansist/`  
- Перекрёстно: B27 (digest), B36 (выписка), B29 (справочник ДДС)

---

=== EXCALIBUR BLOG RESEARCH ===
topic_id: B64
article_dir: memory/blog/articles/B64-one-pager-sobstvenniku-sheets
status: ✅ PASS
utility_verdict: PASS
reader_outcome: One-pager в Google Sheets: 5 управленческих цифр на одном экране, формулы со staging, светофор, проверка, без ПДн — собственник за 5 минут видит «норма / проблема».
summary: SERP primary загрязнён startup one-pager; живой WebSearch — дашборды собственника (ADPASS, GSE, genad). Прямого RU how-to «Sheets → 5 цифр» нет. Wordstat недоступен (MCP user-mcp-kv). 20 фактов с URL, 9 шагов action_outline, 7 FAQ. Internal: avtomatizaciya-finansov-no-code, obezlichivanie-dannyh-chatgpt-finansist. Готов к writer.
===
