# Research notes — B63

**topic_id:** B63  
**slug:** indeks-cen-postavshchikov-sheets  
**h1:** Как считать индекс изменения цен поставщиков в Excel/Sheets  
**research_date:** 2026-08-15  
**publish_target:** koda-fd.ru/blog  
**utility_gate:** PASS (`how_to`, mode B)  
**author_id:** olga-kondratskaya  
**related_published:** `/avtomatizaciya-finansov-no-code/`, `/obezlichivanie-dannyh-chatgpt-finansist/`  
**internal_links (карточка):** `/avtomatizaciya-finansov-no-code/`, `/obezlichivanie-dannyh-chatgpt-finansist/`  
**cover_scene_hint:** abstract holographic finance automation dark #0a0a0f purple #8b5cf6, no text

---

## utility_verdict

**PASS** — тема utility-only how-to (mode B). Читатель за ~1–2 часа собирает в Excel или Google Sheets таблицу закупок, считает индивидуальные и сводные индексы изменения цен поставщиков (Ласпейрес с весами по объёму закупок), настраивает MoM/YoY и пороги сигналов для переговоров — без программиста и без путаницы с индексами Росстата/44-ФЗ.

---

## reader_outcome

После гайда финансист или руководитель закупок сможет выгрузить историю цен по номенклатуре и поставщикам в Excel/Google Sheets, рассчитать индекс изменения цен (по позиции, по поставщику и по категории), увидеть, кто поднял цены сильнее рынка, и подготовить аргументы для пересмотра условий — с проверкой данных и без выгрузки сырых ПДн в облако.

---

## action_outline

1. **Когда индекс нужен финотделу (и когда нет)** — регулярные закупки 20+ SKU у 3+ поставщиков, нужен аргумент «цены выросли на X%» → да; разовая закупка или уже есть 1С:ERP «Индекс цен поставщиков» → другой маршрут; задача только НМЦК по 44-ФЗ → не этот гайд (дефляторы/ИПЦ — отдельная тема).
2. **Подготовка данных и безопасность** — столбцы: `supplier_code`, `sku`, `base_price`, `current_price`, `base_qty` (объём закупок в базовом периоде), `period`; коды контрагентов вместо ФИО/ИНН в Google Sheets; единая валюта и единица измерения; **не смешивать** разные артикулы одного «похожего» товара.
3. **Индивидуальный индекс по позиции** — формула `(P1/P0)*100` или `(P1/P0)-1` в долях; в Excel: `=ТЕКУЩАЯ_ЦЕНА/БАЗОВАЯ_ЦЕНА*100`; в Sheets: `=CURRENT/BASE*100`; базовый период = 100.
4. **Сводный индекс поставщика (Ласпейрес)** — веса = объёмы базового периода: `=СУММПРОИЗВ(P1:Pn;Q0:Qn)/СУММПРОИЗВ(P0:Pn;Q0:Qn)*100`; Sheets: `=SUMPRODUCT(...)`; это та же модель, что в отчёте 1С:ERP «Индекс цен поставщиков».
5. **Агрегация по категории и динамика MoM/YoY** — сводная таблица / QUERY: индекс по группе SKU; столбцы «изм. к прошлому месяцу» и «к базовому году»; условное форматирование при индексе > порога (например 105) два месяца подряд → триггер пересмотра контракта.
6. **Проверка результата** — контроль: базовый период = 100; нет нулей в `base_price` и `base_qty`; сумма весов согласована с фактическими закупками; 3–5 строк сверить с ERP/накладными; отделить разовые акции от устойчивого роста.
7. **Типичные ошибки** — путать с ИЦП Росстата или индексом-дефлятором Минэкономразвития; менять состав корзины между периодами без фиксации SKU; веса из текущего периода вместо базового (это уже Пааше); сравнивать цены в разных валютах без пересчёта.
8. **Sheets vs Excel** — Excel: `СУММПРОИЗВ`, Power Query для слияния прайсов; Sheets: `SUMPRODUCT`, `QUERY`, опционально Apps Script для ежемесячного импорта CSV; оба — локальная копия или обезличенные коды в облаке (перекрёстно B11).
9. **Что автоматизировать дальше** — ежемесячная выгрузка из 1С (B13), дашборд порогов, n8n-уведомление закупкам при индексе >105 два месяца, сопоставление с внешним ИЦП отрасли для sanity-check.

---

## Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT AUTH WARNING:** сервер MCP `user-mcp-kv` в этой Cloud-сессии **не подключён** (доступен только `cursor-cloud`). Вызов `wordstat_get_top_requests` **не выполнен**. Точные показы/мес **не получены** и **не выдуманы**.

Обновление токена: https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

**Экспертная семантика (LSI для writer, без цифр спроса):**

| Кластер | Фразы |
| --- | --- |
| Ядро | индекс цен поставщиков excel, индекс изменения цен поставщиков, расчёт индекса цен в excel |
| Метод | индекс ласпейреса excel, суммпродукт индекс цен, взвешенный индекс цен закупки |
| Sheets | индекс цен google sheets, sumproduct price index, анализ цен поставщиков таблица |
| Закупки | мониторинг цен поставщиков, динамика закупочных цен, контроль стоимости закупок |
| Автоматизация | автоматизация финотдела, выгрузка цен из 1с excel, power query прайс поставщиков |
| Ловушка SERP | индекс цен производителей росстат, индекс дефлятор 44-фз, нмцк коэффициент вариации — **другой intent** |

**SEO-вывод:** `primary_query` в preflight-SERP **загрязнён** нормативными подборками (дефляторы Минэкономразвития, ИЦП Росстата, 44-ФЗ). По H1 конкурируют общие гайды «индексы в Excel» и ERP-обзоры 1С без пошаговых формул в Sheets. Прямого «индекс цен **ваших** поставщиков → Excel/Sheets за час» почти нет. Угол КОДА: **управленческий индекс закупок + Ласпейрес + безопасность данных + мост к B13/B11**.

---

## SERP (WebSearch Cursor, 15.08.2026)

`research-serp.json` по `primary_query` **слабо релевантен** (Consultant/Росстат/дефляторы) — дополнен живым WebSearch.

### Primary: индекс цен поставщиков excel

| # | URL | Тип | Пробел для КОДА |
| --- | --- | --- | --- |
| 1 | https://1ccl.ru/company/blog/analiz-usloviy-zakupok-i-tsen-postavshchikov-v-1s-erp/ | 1С:ERP отчёты | Есть «Индекс цен поставщиков» и Ласпейрес, но только ERP — нет Excel/Sheets |
| 2 | https://ppt.ru/art/zakupki/koeffitsienty-i-indeksy-kogda-ispolzovat-i-kak-schitat | 44-ФЗ индексы | Дефлятор/ИПЦ/КВ — не внутренний индекс закупок |
| 3 | https://www.consultant.ru/document/cons_doc_LAW_504677/ | прогноз ИЦП | Норматив, не how-to |
| 4 | https://calculatorlib.com/ru/laspeyres-paasche-fisher-price-index-calculator | калькулятор L/P/F | Формулы есть, нет закупок/поставщиков |
| 5 | https://corporatefinanceinstitute.com/resources/economics/laspeyres-price-index/ | EN теория L | База 100, формула — шаблон для writer |
| 6 | https://datafinder.ru/solutions/ekspert-bi-zakupki/bi-dwh/kontrol-stoimosti-zakupok-analiz-dinamiki-zakupochnyh-cen-po-tovaram-dlya-vyyavleniya-rosta-stoimosti-i-ocenki-effektivnosti-peregovorov-s-postavshchikami | методология закупок | MoM/YoY, пороги сигналов — контекст H2 |
| 7 | https://intmag24.ru/tablitsy-excel/analiz-postavshhikov-i-tsen-dlya-marketplejsov/ | Power Query | Сравнение мин. цены, не индекс динамики |

### H1: Как считать индекс изменения цен поставщиков в Excel/Sheets

| # | URL | Тип | Пробел для КОДА |
| --- | --- | --- | --- |
| 8 | https://excel-gid.vercel.app/articles/k/ka/kak-poschitat-indeksy-v-eksel.html | общий Excel | ИПЦ/статистика, не поставщики |
| 9 | https://toolfox.ru/tools/price-index-calculator | онлайн-кальк | Без таблицы закупок |
| 10 | https://dashboardsexcel.com/blogs/blog/excel-tutorial-calculate-cpi | CPI Excel EN | SUMPRODUCT для CPI — переносимо |
| 11 | https://mksegment.ru/b/kak-najti-indeks-izmeneniya-cen-formula-raschet-i-primery | формулы | Общая теория, мало закупок |

### Secondary: автоматизация финотдела / мониторинг цен

| # | URL | Тип | Пробел для КОДА |
| --- | --- | --- | --- |
| 12 | https://koda-fd.ru/blog/ai-dlya-finansista-2026/ | свой блог | Перелинковка «что автоматизировать» |
| 13 | https://datalopata.ru/blog/avtomatizatsija-finansov-sistemnyj-podhod-k-uchetu-v-2026-godu/ | автоматизация 2026 | Фон для финального H2 |
| 14 | https://nfp2b.ru/2026/06/04/robotizatsiya-monitoringa-tsen-v-zakupkah-kak-svyazka-rpa-i-bi-pomogaet-uskorit-raschet-nmtsk-i-snizit-ruchnuyu-nagruzku/ | RPA мониторинг | Enterprise-конtrast; Excel — старт без RPA |
| 15 | https://uglekislygaz.ru/news/kak-avtomatizirovat-proverku-aktualnosti-tsen-i-ostatkov-pered-otpravkoj-zakaza/ | пороги цен | Пример порога 5% — для блока сигналов |

**serp_gap КОДА:** пошаговый workflow «выгрузка цен поставщиков → индивидуальный индекс → сводный Ласпейрес по поставщику/категории → MoM/YoY → пороги для переговоров» в **Excel и Google Sheets** с таблицей формул, проверкой ошибок, отличением от Росстата/44-ФЗ и правилами без ПДн в облаке.

**Cannibalization:** B13 (выгрузка 1С), B11 (обезличивание), `/avtomatizaciya-finansov-no-code/` — перелинковка; B63 = **расчёт индекса и решение «к кому идти на переговоры»**, не автоматизация целиком.

---

## Таблица фактов

| # | Утверждение | Источник | Дата проверки |
| --- | --- | --- | --- |
| 1 | Отчёт 1С:ERP «Индекс цен поставщиков» рассчитывает индексы по номенклатуре **в разрезе поставщиков** с моделью **индексов цен Ласпейреса**. | https://1ccl.ru/company/blog/analiz-usloviy-zakupok-i-tsen-postavshchikov-v-1s-erp/ | 2026-08-15 |
| 2 | Отчёт «Индекс цен номенклатуры» в 1С:ERP также использует **модель Ласпейреса**: сравнение базового периода с последующими. | https://1ccl.ru/company/blog/analiz-usloviy-zakupok-i-tsen-postavshchikov-v-1s-erp/ | 2026-08-15 |
| 3 | Индекс Ласпейреса: **L = Σ(p_t × q_0) / Σ(p_0 × q_0) × 100**, где веса — **количества базового периода** q_0. | https://calculatorlib.com/ru/laspeyres-paasche-fisher-price-index-calculator | 2026-08-15 |
| 4 | **Базисный период** в индексах цен по общепринятому правилу принимается за **100**. | https://calculatorlib.com/ru/laspeyres-paasche-fisher-price-index-calculator | 2026-08-15 |
| 5 | Индекс **Пааше** использует веса **отчётного** периода; обычно **ниже** Ласпейреса из‑за эффекта замещения. | https://calculatorlib.com/ru/laspeyres-paasche-fisher-price-index-calculator | 2026-08-15 |
| 6 | Индекс **Фишера** = √(L × P) — среднее геометрическое Ласпейреса и Пааше. | https://calculatorlib.com/ru/laspeyres-paasche-fisher-price-index-calculator | 2026-08-15 |
| 7 | Laspeyres Price Index: числитель — расходы наблюдаемого периода при **базовых количествах**; знаменатель — расходы базового периода; базовый год часто = **100**. | https://corporatefinanceinstitute.com/resources/economics/laspeyres-price-index/ | 2026-08-15 |
| 8 | Пример CFI: при фиксированных количествах Year 0 = **100**, Year 1 = **128,23**, Year 2 = **123,53** — меняются только цены. | https://corporatefinanceinstitute.com/resources/economics/laspeyres-price-index/ | 2026-08-15 |
| 9 | **Индивидуальный** индекс цены: (цена текущего периода / цена базового периода) × **100**. | https://mksegment.ru/b/kak-najti-indeks-izmeneniya-cen-formula-raschet-i-primery | 2026-08-15 |
| 10 | Для закупок: ценовой индекс = отношение **текущей средней цены к базовому периоду**; можно взвешивать по **объёму закупок**. | https://datafinder.ru/solutions/ekspert-bi-zakupki/bi-dwh/kontrol-stoimosti-zakupok-analiz-dinamiki-zakupochnyh-cen-po-tovaram-dlya-vyyavleniya-rosta-stoimosti-i-ocenki-effektivnosti-peregovorov-s-postavshchikami | 2026-08-15 |
| 11 | Рекомендуемый анализ динамики закупок: **MoM и YoY** для сезонности и трендов. | https://datafinder.ru/solutions/ekspert-bi-zakupki/bi-dwh/kontrol-stoimosti-zakupok-analiz-dinamiki-zakupochnyh-cen-po-tovaram-dlya-vyyavleniya-rosta-stoimosti-i-ocenki-effektivnosti-peregovorov-s-postavshchikami | 2026-08-15 |
| 12 | Сигнальное правило (пример): если индекс **выше порога два последовательных месяца** — запрос на перепроверку поставщиков и переоценку контрактов. | https://datafinder.ru/solutions/ekspert-bi-zakupki/bi-dwh/kontrol-stoimosti-zakupok-analiz-dinamiki-zakupochnyh-cen-po-tovaram-dlya-vyyavleniya-rosta-stoimosti-i-ocenki-effektivnosti-peregovorov-s-postavshchikami | 2026-08-15 |
| 13 | В 44-ФЗ для НМЦК **коэффициент вариации** по методрекомендациям не должен превышать **33%** — это **другой** инструмент, не индекс цен поставщиков в Excel. | https://ppt.ru/art/zakupki/koeffitsienty-i-indeksy-kogda-ispolzovat-i-kak-schitat | 2026-08-15 |
| 14 | ИПЦ для пересчёта цен в закупках по 44-ФЗ берётся с **сайта Росстата** — не подменяет внутренний индекс ваших контрагентов. | https://ppt.ru/art/zakupki/koeffitsienty-i-indeksy-kogda-ispolzovat-i-kak-schitat | 2026-08-15 |
| 15 | Ручной анализ сотен/тысяч позиций цен поставщиков занимает **часы**; Power Query в Excel 2016+ сокращает до **минут** при повторяющихся прайсах. | https://intmag24.ru/tablitsy-excel/analiz-postavshhikov-i-tsen-dlya-marketplejsov/ | 2026-08-15 |
| 16 | Excel CPI/SUMPRODUCT: взвешенный индекс = `SUMPRODUCT(PriceRelative, Weight) / SUM(Weight) * 100` при базе 100. | https://dashboardsexcel.com/blogs/blog/excel-tutorial-calculate-cpi | 2026-08-15 |
| 17 | Пример автоматизации мониторинга: сокращение ручного труда на мониторинг с **4–6 ч/день** до ~**30 мин** на проверку (RPA+BI, enterprise). | https://nfp2b.ru/2026/06/04/robotizatsiya-monitoringa-tsen-v-zakupkah-kak-svyazka-rpa-i-bi-pomogaet-uskorit-raschet-nmtsk-i-snizit-ruchnuyu-nagruzku/ | 2026-08-15 |
| 18 | Пример бизнес-правила: если цена изменилась **более чем на 5%** с момента подтверждения — ручной пересчёт (аналог порога в таблице индексов). | https://uglekislygaz.ru/news/kak-avtomatizirovat-proverku-aktualnosti-tsen-i-ostatkov-pered-otpravkoj-zakaza/ | 2026-08-15 |
| 19 | Индекс цен — **относительный показатель** изменения цен во времени (в коэффициентах или процентах); для статистики закупок материалов важен отбор **стабильных поставщиков**. | https://normativ.kontur.ru/document?documentId=463835&moduleId=1 | 2026-08-15 |
| 20 | CalculatorLib пример: L=**150**, P=**125**, F≈**136,93** при двух товарах с разными q_t — иллюстрация разницы L и P. | https://calculatorlib.com/ru/laspeyres-paasche-fisher-price-index-calculator | 2026-08-15 |

**Не выдумывать:** точные показы Wordstat; макро-ИЦП Росстата за август 2026 (fetch timeout); «индекс снижает закупки на X%»; что Excel-таблица заменяет отчёт 1С без выгрузки.

**fact-bank.md:** прямых фактов по индексу цен поставщиков нет — все цифры только из таблицы выше.

---

## Структура H2 для writer (из карточки B63)

1. Когда это нужно финотделу (и когда нет)  
2. Подготовка данных и безопасность (без сырых ПДн в облако)  
3. Пошаговая настройка таблицы и формул (Excel + Sheets, Ласпейрес)  
4. Проверка результата и типичные ошибки (путаница с Росстатом/44-ФЗ, веса, валюта)  
5. Что автоматизировать дальше (1С, n8n, Power Query)  
+ FAQ + CTA

## FAQ-кандидаты (из карточки)

- Можно ли без программиста?  
- Сколько займёт первый расчёт (ориентир ~1–2 ч на 50–100 SKU)?  
- Какие риски для данных в Google Sheets?  
- Чем отличается от индекса цен производителей Росстата?  
- Ласпейреса или Пааше — что выбрать для закупок?  
- Какой базовый период брать — месяц, квартал, год?  
- Нужна ли 1С, если есть Excel?

## CTA / interlink

- CTA: club.koda-fd.ru (utm_campaign=indeks-cen-postavshchikov-sheets), t.me/finance_modern  
- Internal: `/avtomatizaciya-finansov-no-code/`, `/obezlichivanie-dannyh-chatgpt-finansist/`  
- Перекрёстно: B13 (выгрузка 1С), B11 (обезличивание)
