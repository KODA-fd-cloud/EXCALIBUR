# Research notes — B56

**topic_id:** B56  
**slug:** abc-analiz-debitorki-excel  
**h1:** Как сделать ABC-анализ дебиторки в Excel/Sheets и решить, кому звонить первым  
**research_date:** 2026-08-08  
**publish_target:** koda-fd.ru/blog  
**utility_gate:** PASS (`how_to`, mode B)  
**author_id:** olga-kondratskaya  
**related_published:** `/avtomatizaciya-finansov-no-code/`, `/obezlichivanie-dannyh-chatgpt-finansist/`  
**internal_links (карточка):** `/avtomatizaciya-finansov-no-code/`, `/obezlichivanie-dannyh-chatgpt-finansist/`  
**cover_scene_hint:** abstract holographic finance automation dark #0a0a0f purple #8b5cf6, no text

---

## utility_verdict

**PASS** — тема utility-only how-to (mode B). Читатель за ~1 час собирает таблицу дебиторки, считает долю и накопительный итог, присваивает классы A/B/C формулами Excel/Google Sheets, добавляет дни просрочки и получает упорядоченный список «кому звонить первым». Не новость про ДЗ-2026, не академический обзор без шагов.

---

## reader_outcome

После гайда финансист или бухгалтер сможет выгрузить открытую дебиторку в Excel или Google Sheets, провести ABC-классификацию по сумме долга, совместить её с возрастом просрочки и составить приоритетный реестр контактов на неделю — без программиста и без обязательной 1С-отчётности.

---

## action_outline

1. **Когда ABC по дебиторке нужен / когда нет** — есть 15+ контрагентов с отсрочкой и не хватает времени на всех → да; одна-две крупные ДЗ → достаточно aging-таблицы; холдинг с 1С:ERP и типовым ABC → другой маршрут (упомянуть, не продавать).
2. **Подготовка данных и безопасность** — выгрузка из 1С/CRM/банка: контрагент (код, не ФИО в облако), сумма долга, дата возникновения, срок оплаты, менеджер; **суммировать все договоры одного контрагента**; маскировать ПДн при работе в Google Sheets / ChatGPT (перекрёстно B11).
3. **Сортировка по убыванию суммы** — каждый контрагент одной строкой; удалить нулевые и оплаченные; проверить, что суммы — числа, не текст.
4. **Доля и накопительный итог** — столбец «Доля» = долг строки / общий долг; «Накоп. %» = нарастающая сумма долей; контроль: последняя строка = 100%.
5. **Классы A / B / C формулой** — пороги по накоп. итогу: A до 80%, B 80–95%, C остальное; `=ЕСЛИ(D2<=0,8;"A";ЕСЛИ(D2<=0,95;"B";"C"))` (Sheets: `=IF(...)`); границы можно сдвинуть под отрасль (70/20/10).
6. **Добавить aging (дни просрочки)** — `=МАКС(0; СЕГОДНЯ()-дата_оплаты)`; внутри группы A сортировать по дням просрочки ↓ — **это и есть очередь звонков**.
7. **Правила действий по группам** — A + просрочка: звонок/письmo в день 1; B: шаблонное напоминание; C: авто-напоминание или списание при экономической нецелесообразности; зафиксировать в колонках «Следующий шаг» / «Дата касания».
8. **Проверка результата** — сумма долгов = исходной выгрузке; 100% накоп. итога; нет дублей контрагентов; 3–5 строк сверить вручную с 1С.
9. **Что автоматизировать дальше** — еженедельное обновление выгрузки (1С OData / CSV), условное форматирование A+просрочка, n8n-напоминания по статусу (B14), опционально ABC+XYZ для нестабильных плательщиков.

---

## Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT AUTH WARNING:** сервер MCP `user-mcp-kv` в этой Cloud-сессии **не подключён** (доступен только `cursor-cloud`). Вызов `wordstat_get_top_requests` **не выполнен**. Точные показы/мес **не получены** и **не выдуманы**.

Обновление токена: https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

**Экспертная семантика (LSI для writer, без цифр спроса):**

| Кластер | Фразы |
| --- | --- |
| Ядро | abc анализ дебиторской задолженности, abc анализ дебиторки excel |
| Метод | abc xyz анализ дебиторской задолженности, анализ дебиторской задолженности по срокам, aging дебиторка |
| Excel/Sheets | abc анализ в excel формула, abc анализ google sheets, накопительный итог excel |
| Действие | кому звонить по дебиторке, приоритет взыскания дебиторки, реестр просроченной дебиторки |
| Автоматизация | автоматизация финотдела, выгрузка дебиторки 1с excel, n8n напоминание оплата |
| Ловушка SERP | дипломная работа дебиторская задолженность 2026, выписка егрюл — **не целевой intent** |

**SEO-вывод:** `primary_query` в preflight-SERP **загрязнён** подборками Consultant, «дипломными» сайтами и общими гайдами по ДЗ без ABC в Excel. По H1 конкурируют **универсальные** ABC-гайды для товаров (Bitrix24, Lumpics, Brightboard). Прямого пошагового «ABC дебиторки → очередь звонков в Sheets» почти нет. Угол КОДА: **Excel/Sheets за час + aging + безопасность данных + мост к автоматизации (B14/B13)**.

---

## SERP (WebSearch Cursor, 08.08.2026)

`research-serp.json` по `primary_query` **слабо релевантен** (нормативные подборки, академические «гайды 2026» без формул) — дополнен живым WebSearch.

### Primary: abc анализ дебиторской задолженности

| # | URL | Тип | Пробел для КОДА |
| --- | --- | --- | --- |
| 1 | https://alexeydemidov.ru/blog/avs-analiz-debitorskoy-zadolzhennosti-primer-rascheta/ | пример ABC + юриспруденция | Близкий intent, но акцент на суд/претензии; мало формул Excel/Sheets |
| 2 | https://www.consultant.ru/law/podborki/analiz_debitorskoj_zadolzhennosti/ | НПА-подборка | Не how-to; не конкурировать |
| 3 | https://www.1ab.ru/blog/detail/upravlenie-debitorskoy-zadolzhennostyu-polnoe-rukovodstvo-dlya-biznesa-v-2026-godu/ | обзор ДЗ 2026 | Макро/теория, нет таблицы ABC |
| 4 | https://cyberleninka.ru/article/n/razvitie-biznesa-na-osnove-vektornoy-raboty-s-pokupatelyami | научная статья ABC+XYZ | Академично; взять идею матрицы, не структуру |
| 5 | https://www.coderstar.ru/otchety/abc-analiz | ABC в 1С | Пороги 70/20/10; продажа отчёта, не Excel |

### H1 / Excel: ABC в таблицах (перенос методики на дебиторку)

| # | URL | Тип | Пробел для КОДА |
| --- | --- | --- | --- |
| 6 | https://www.bitrix24.ru/journal/abc-analiz-excel/ | пошаговый Excel | Товары/клиенты по выручке; формулы применимы, объект другой |
| 7 | https://brightboard.ru/blog/abc-analiz-v-excel-poshagovyy-raschyot-cherez-svodnye-tablitsy | сводные таблицы | Склад/ассортимент; нет дебиторки и звонков |
| 8 | https://exceltable.com/en/analyses-reports/abc-xyz-analysis-in-excel | EN гайд ABC+XYZ | Явно: debtors анализируют **по сумме задолженности** |
| 9 | https://mpmgr.ru/blog/analytics/chto-takoye-abc-analiz-na-wildberries-i-kak-ego-sdelat | формула IF | Пороги 80/95, формула класса — шаблон для writer |
| 10 | https://ppc.world/articles/abc-analiz-sut-metoda-poshagovye-instrukcii-s-formulami-v-excel-keysy-ot-ekspertov/ | ABC Excel | Общий метод, без ДЗ |
| 11 | https://businessolog.ru/abc-xyz-excel/ | ABC+XYZ Excel | Запасы; XYZ-пороги для блока «что дальше» |

### Secondary: автоматизация финотдела / контекст ДЗ

| # | URL | Тип | Пробел для КОДА |
| --- | --- | --- | --- |
| 12 | https://datalopata.ru/blog/avtomatizatsija-finansov-sistemnyj-podhod-k-uchetu-v-2026-godu/ | автоматизация 2026 | Фон для H2 «что автоматизировать» |
| 13 | https://schollufsin.ru/en/legislation/kak-sdelat-otchet-po-debitorskoi-zadolzhennosti-analiz-debitorskoi-zadolzhennosti-v-excel-kak-vychlen/ | aging в Excel | Расчёт дней просрочки — паттерн для шага 6 |
| 14 | https://infostart.ru/1c/reports/1827054/ | 1С отчёт просрочки | Альтернатива 1С; не обязательный минимум |

**serp_gap КОДА:** пошаговый workflow «выгрузка дебиторки → ABC по сумме → aging → очередь звонков» в **Excel и Google Sheets** с таблицей формул, проверкой ошибок, правилами без выгрузки ПДн в облако и мостом к n8n/1С. Прямого H1-конкурента нет.

**Cannibalization:** B14 (реестр + напоминания), B13 (выгрузка 1С), B11 (обезличивание) — перелинковка; B56 = **приоритизация**, B14 = **исполнение касаний**.

---

## Таблица фактов

| # | Утверждение | Источник | Дата проверки |
| --- | --- | --- | --- |
| 1 | ABC-анализ опирается на принцип Парето: ~20% объектов дают ~80% результата. | https://www.bitrix24.ru/journal/abc-analiz-excel/ | 2026-08-08 |
| 2 | Для ABC в Excel типичные границы по **накопительному итогу**: группа A — до **80%**, B — **80–95%**, C — остальное. | https://www.bitrix24.ru/journal/abc-analiz-excel/ | 2026-08-08 |
| 3 | Формула класса в Excel: `=ЕСЛИ(D2<=0,8;"A";ЕСЛИ(D2<=0,95;"B";"C"))`, где D — накопительная доля. | https://www.bitrix24.ru/journal/abc-analiz-excel/ | 2026-08-08 |
| 4 | Доля позиции: `=B2/СУММ($B$2:$B$N)` с абсолютной ссылкой на итог; накоп. итог: `=СУММ($C$2:C3)`. | https://www.bitrix24.ru/journal/abc-analiz-excel/ | 2026-08-08 |
| 5 | Ручной ABC-анализ в Excel занимает порядка **20–30 минут** при небольшом наборе данных. | https://www.bitrix24.ru/journal/abc-analiz-excel/ | 2026-08-08 |
| 6 | Метод ABC применим к **дебиторам** — ранжирование по **сумме задолженности** (наряду с клиентами, поставщиками, ассортиментом). | https://exceltable.com/en/analyses-reports/abc-xyz-analysis-in-excel | 2026-08-08 |
| 7 | Алгоритм ABC: сортировка ↓ → доля каждого → накопительная доля → граница A при ~**80%**, B при ~**95%**. | https://exceltable.com/en/analyses-reports/abc-xyz-analysis-in-excel | 2026-08-08 |
| 8 | В 1С-отчётах ABC часто используют пороги **70% / 20% / 10%** (A/B/C) — допустимо сдвигать под бизнес. | https://www.coderstar.ru/otchety/abc-analiz | 2026-08-08 |
| 9 | ABC по дебиторке: группа A ≈ **70–80%** суммы ДЗ, B ≈ **15–20%**, C ≈ **5–10%** (ориентиры, не догма). | https://alexeydemidov.ru/blog/avs-analiz-debitorskoy-zadolzhennosti-primer-rascheta/ | 2026-08-08 |
| 10 | Все долги **одного контрагента суммируют** в одну строку перед ABC. | https://alexeydemidov.ru/blog/avs-analiz-debitorskoy-zadolzhennosti-primer-rascheta/ | 2026-08-08 |
| 11 | ABC по одной только сумме **недостаточен** — рекомендуется совмещать с **aging** (анализ по срокам просрочки). | https://alexeydemidov.ru/blog/avs-analiz-debitorskoy-zadolzhennosti-primer-rascheta/ | 2026-08-08 |
| 12 | Минимальная частота пересчёта ABC по дебиторке — **раз в квартал**; при высокой динамике — чаще. | https://alexeydemidov.ru/blog/avs-analiz-debitorskoy-zadolzhennosti-primer-rascheta/ | 2026-08-08 |
| 13 | Общий срок исковой давности по денежным требованиям — **3 года** (ст. 196 ГК РФ). | https://alexeydemidov.ru/blog/avs-analiz-debitorskoy-zadolzhennosti-primer-rascheta/ | 2026-08-08 |
| 14 | ABC+XYZ даёт **9 групп** (AX…CZ) для дифференцированного управления дебиторкой. | https://cyberleninka.ru/article/n/razvitie-biznesa-na-osnove-vektornoy-raboty-s-pokupatelyami | 2026-08-08 |
| 15 | XYZ: коэффициент вариации **0–10%** → X (стабильный спрос), **10–25%** → Y, **>25%** → Z. | https://exceltable.com/en/analyses-reports/abc-xyz-analysis-in-excel | 2026-08-08 |
| 16 | Для aging в Excel: дни просрочки = текущая дата минус плановая дата оплаты (отгрузка + отсрочка). | https://schollufsin.ru/en/legislation/kak-sdelat-otchet-po-debitorskoi-zadolzhennosti-analiz-debitorskoi-zadolzhennosti-v-excel-kak-vychlen/ | 2026-08-08 |
| 17 | Классические границы A/B/C в retail-гайдах: A до **80%**, B до **95%**, C — остальное; формула `=ЕСЛИ(Кумулятивно<=0,8;"A";...)`. | https://mpmgr.ru/blog/analytics/chto-takoye-abc-analiz-na-wildberries-i-kak-ego-sdelat | 2026-08-08 |
| 18 | Для ABC желателен период данных **3–6 месяцев** (сглаживает сезонность); для дебиторки — срез **на дату**. | https://brightboard.ru/blog/abc-analiz-v-excel-poshagovyy-raschyot-cherez-svodnye-tablitsy | 2026-08-08 |
| 19 | Контроль корректности: последняя строка накопительного итога = **100%**; сумма долей = **100%**. | https://brightboard.ru/blog/abc-analiz-v-excel-poshagovyy-raschyot-cherez-svodnye-tablitsy | 2026-08-08 |
| 20 | Infostart ABC в 1С строится на **накопительном итоге доли** и условном оформлении границ — тот же принцип, что в Excel. | https://infostart.ru/1c/articles/2336616/ | 2026-08-08 |

**Не выдумывать:** точные показы Wordstat; статистику Росстата/РБК из alexeydemidov без первичного источника; «ABC снижает ДЗ на X%»; гарантии взыскания.

**fact-bank.md:** прямых фактов по ABC-дебиторке нет — все цифры только из таблицы выше.

---

## Структура H2 для writer (из карточки B56)

1. Когда это нужно финотделу (и когда нет)  
2. Подготовка данных и безопасность (без сырых ПДн в облако)  
3. Пошаговая настройка таблицы ABC в Excel/Sheets (формулы, пример)  
4. Проверка результата и типичные ошибки (дубли, пороги, только сумма без aging)  
5. Что автоматизировать дальше (обновление, n8n, 1С)  
+ FAQ + CTA

## FAQ-кандидаты (из карточки)

- Можно ли без программиста?  
- Сколько займёт внедрение (ориентир ~1 ч на первую таблицу)?  
- Какие риски для данных в Google Sheets?  
- Чем 80/95 отличается от 70/20/10?  
- Нужно ли суммировать договоры одного клиента?  
- Как совместить ABC и дни просрочки для очереди звонков?  
- Когда достаточно aging без ABC?

## CTA / interlink

- CTA: club.koda-fd.ru (utm_campaign=abc-analiz-debitorki-excel), t.me/finance_modern  
- Internal: `/avtomatizaciya-finansov-no-code/`, `/obezlichivanie-dannyh-chatgpt-finansist/`  
- Перекрёстно: B14 (напоминания), B13 (выгрузка 1С)
