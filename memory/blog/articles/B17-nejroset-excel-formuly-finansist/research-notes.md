# Research notes — B17

**topic_id:** B17  
**slug:** nejroset-excel-formuly-finansist  
**h1:** Как использовать нейросеть для Excel: ChatGPT пишет формулы, сводные и очистку выгрузок  
**research_date:** 2026-07-22  
**publish_target:** сайт koda-fd.ru/blog (+ Дзен по оркестрации)  
**utility_gate:** PASS (`how_to`, mode B) — см. `utility-gate-topic.json`  
**practice_angle:** финансист + выгрузки 1С/банков → формулы (СУММЕСЛИМН, XLOOKUP/ВПР), сводные, очистка; проверка на галлюцинации; граница «Excel → скрипт/staging»

---

## utility_verdict

**PASS** — тема utility-only how_to. Читатель получает рабочий маршрут: какие задачи Excel отдать нейросети; как выбрать ChatGPT vs Claude для длинных выгрузок; 10 рабочих промптов под RU-Excel; как проверить формулу на контрольной сумме; когда уходить из «просто Excel» в скрипт/staging. Не новость про релиз add-in, не «вообще про ИИ».

---

## reader_outcome

После гайда финансист сможет за один рабочий сеанс описать структуру своей выгрузки нейросети, получить рабочие формулы/шаги сводной на русской раскладке Excel, вставить их в лист и **прогнать чеклист проверки** (контрольная сумма, тестовая строка, версия Excel), не заливая в чат сырую 1С с ПДн.

---

## action_outline

1. **Отделить задачи «нейросети» от задач «Excel сам»** — формулы/очистка/сводная-дизайн vs миллион строк и ежедневный ETL (тогда — скрипт/Power Query/staging).
2. **Подготовить безопасный срез данных** — шапка столбцов + 5–20 обезличенных строк (или только схема); сырую выгрузку 1С не грузить — линк на `/obezlichivanie-dannyh-chatgpt-finansist/`.
3. **Выбрать канал** — чат ChatGPT/Claude (копипаст формулы) vs надстройка ChatGPT for Excel / Copilot in Excel (in-grid); зафиксировать версию Excel (2016/2019 vs 365/2021 — XLOOKUP).
4. **Запросить формулу по шаблону промпта** — структура столбцов + задача + «русская версия Excel, `;`, русские имена функций» + куда вставить.
5. **Собрать пакет из 10 рабочих промптов** — СУММЕСЛИМН, XLOOKUP/ВПР, сводная (поля), дубли, текст по столбцам, даты, trim/пробелы, #Н/Д, исправление ошибки, формула+проверка на примере.
6. **Вставить и прогнать smoke-тест** — контрольная сумма вручную vs формула; 1–2 строки с известным ответом; смена локали/разделителя.
7. **Сводная** — попросить раскладку Rows/Columns/Values/Filters по своим колонкам; собрать руками или через Copilot/VBA только если нужен повтор.
8. **Зафиксировать антигаллюцинационный чеклист** — не принимать формулу без сверки; сложные кейсы — ручная доработка (официально признано OpenAI для beta).
9. **Решить «пора уходить»** — если файл > лимита комфорта, повтор каждый день, нужны join двух выгрузок → Python/Cursor/staging (`raw_*`), не наращивать VBA-зоопарк.

---

## Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT AUTH WARNING / SKIP:** сервер MCP `user-mcp-kv` в этой сессии **не подключён** (в каталоге MCP Cursor доступны только `cursor-ide-browser` и GitLens; инструментов `wordstat_*` нет). Точные показы/мес **не получены** и **не выдуманы**.

Обновите токен / подключите MCP-KV:  
https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

**Экспертная семантика (без цифр спроса) — LSI для копирайтера:**

| Кластер | Фразы (использовать осмысленно) | Роль |
| --- | --- | --- |
| Primary | как использовать нейросеть для excel, нейросеть excel формулы | H1, лид, Direct Answer |
| Formulas | chatgpt формулы excel, суммеслимн chatgpt, xlookup chatgpt, впр нейросеть | H2 про промпты |
| Pivot | chatgpt сводные таблицы, сводная таблица промпт, pivot excel ai | H2 про сводные |
| Finance | ai для excel финансист, chatgpt выгрузка 1с excel, очистка данных excel chatgpt | Угол КОДА + FAQ |
| Compare | excel copilot vs chatgpt, claude excel формулы, chatgpt for excel | H2 сравнение + FAQ |
| Safety | обезличивание данных chatgpt excel, можно ли загружать выгрузку 1с | FAQ + internal link B11 |
| Locale | русская версия excel формулы точка с запятой, английские функции excel chatgpt | Критичный блок в промптах |

**SEO-вывод:** SERP забит списками «N промптов» и обзорами add-in/Copilot. Угол КОДА — **финансист + RU-Excel + проверка формул + граница ухода в скрипт**, а не каталог инструментов. В H1/лиде держать связку «нейросеть → формулы/сводные/очистка выгрузок», secondary — ChatGPT формулы и сводные.

---

## SERP (WebSearch Cursor, 22.07.2026)

Приоритет — живой WebSearch. `research-serp.json` из шага 0 был **пустым** (result_count: 0 по всем запросам) — перезаписан результатами Cursor WebSearch (см. обновлённый файл).

### Главный запрос: `как использовать нейросеть для excel` / H1

| # | URL | Тип | Пробел для КОДА |
| --- | --- | --- | --- |
| 1 | https://openai.com/ru-RU/index/chatgpt-for-excel/ | Официальный анонс ChatGPT for Excel (05.03.2026) + апдейт Sheets 22.04.2026 | Product news; нет RU-промптов и чеклиста проверки для финансиста |
| 2 | https://mashagpt.ru/blog/kak-zagruzit-dannye-iz-excel-v-chatgpt | Обзор загрузки Excel + add-in GPT-5.4 | Широкий обзор; слабый угол «выгрузка 1С → проверка суммы» |
| 3 | https://ya.zerocoder.ru/chatgpt-v-excel-chto-umeet-i-kak-ispolzovat/ | Что умеет add-in | Маркетинг возможностей, мало actionable шагов |
| 4 | https://dzen.ru/a/ai2l3OAECSudCPHW | Шаблон промпта под RU-Excel | Есть locale-хак; нет пакета финанс-задач и границы «уходи в скрипт» |
| 5 | https://habr.com/ru/companies/sberbank/articles/918676/ | Плагин/API/UDF для Excel↔ChatGPT | Технический путь с API-ключом; не CFO-howto без VBA |

### Вторичные

- **`chatgpt формулы excel`** — сильные практические: https://dzen.ru/a/ags2OJne4hbdTbbG (7 промптов + `;`), https://petr-panda.ru/nejroset-chatgpt-excel/ (23 примера, антипаттерны), https://vc.ru/aihub/2843144-neyroset-dlya-excel-luchshie-instrumenty-i-sovety (инструменты 2026 + XLOOKUP-промпт). Мусор: SEO-каталоги промптов без проверки.
- **`chatgpt сводные таблицы`** — EN-гайды доминируют: layout Rows/Values (gptprompts.ai, findskill.ai, ai-toolbox.co); VBA-макрос на blank pivot (thebricks.com). RU-SERP слабый — **наш зазор**: сводная по выгрузке ДДС/продаж с именами колонок финансиста.
- **`ai для excel финансист`** — Infostart «Умный Excel» (обработка внутри 1С), excelmaster.ai (агент in-Excel), fin-ctrl.ru (уход из Excel). Мало статей «ChatGPT пишет формулу → ты проверяешь контрольной суммой».
- **Copilot vs ChatGPT (FAQ):** https://support.microsoft.com/en-us/excel/copilot/frequently-asked-questions-about-copilot-in-excel ; сравнение оператор/аналитик — datastudios.org, excelmojo.com. Официально: Copilot умеет PivotTables и формулы in-grid, но требует лицензию/формат таблицы/AutoSave.

### Конкурентный зазор (угол КОДА) — serp_gap

1. **RU-locale first** — почти все EN-промпты ломают русскую Excel (`,` vs `;`, SUMIFS vs СУММЕСЛИМН).
2. **Финансист + выгрузка** — не «sales by region», а ДДС/дебиторка/номенклатура из 1С, очистка мусора столбцов.
3. **Антигаллюцинация** — контрольная сумма, тестовая строка, версия Excel (XLOOKUP недоступен в 2016/2019) — у конкурентов часто «просто скопируй».
4. **ChatGPT vs Claude vs Copilot** — коротко и по делу: чат-формулы / длинный контекст / in-grid; без вендорской воды.
5. **Граница ухода** — когда пора в Python/Cursor/staging (линки `/vibe-coding-finansist/`, `/ot-excel-k-fin-konturu-30-dney/`), а не ещё один макрос.
6. **Безопасность** — можно ли грузить 1С: нет сырьём → B11.

---

## Таблица фактов (только с URL; для writer)

| # | Утверждение | Источник | Дата проверки |
| --- | --- | --- | --- |
| 1 | OpenAI представила **ChatGPT для Excel** в бета-версии **5 марта 2026** — надстройка, встраивающая ChatGPT в рабочую книгу для создания/обновления/анализа моделей на формулах. | https://openai.com/ru-RU/index/chatgpt-for-excel/ | 2026-07-22 |
| 2 | Add-in работает на базе **GPT‑5.4**; позиционируется для аналитиков, стратегов, исследователей и бухгалтеров. | https://openai.com/ru-RU/index/chatgpt-for-excel/ | 2026-07-22 |
| 3 | Перед изменением книги ChatGPT **запрашивает разрешение**; расчёты выполняются в Excel, ответы можно связать с ячейками. | https://openai.com/ru-RU/index/chatgpt-for-excel/ | 2026-07-22 |
| 4 | Известные ограничения beta: ответы могут требовать **ручной очистки/корректировки**; сложные/нестандартные формулы — **ручная доработка**. | https://openai.com/ru-RU/index/chatgpt-for-excel/ | 2026-07-22 |
| 5 | Доступность beta (по анонсу): ChatGPT Business, Enterprise, Edu, Teachers (K-12), а также Pro и Plus **за пределами ЕС**; в Enterprise/Edu доступ по умолчанию выключен (включает админ). | https://openai.com/ru-RU/index/chatgpt-for-excel/ | 2026-07-22 |
| 6 | **22 апреля 2026** — обновление: ChatGPT для **Google Sheets** в бета; интеграции/скиллы для Excel и Sheets. | https://openai.com/ru-RU/index/chatgpt-for-excel/ | 2026-07-22 |
| 7 | Внутренний бенчмарк OpenAI (investment banking workflows): эффективность с **43,7%** (GPT‑5) до **87,3%** (GPT‑5.4 Thinking) — пример построения модели трёх отчётов. *Цитировать как заявление OpenAI, не как независимый аудит.* | https://openai.com/ru-RU/index/chatgpt-for-excel/ | 2026-07-22 |
| 8 | Copilot in Excel: insights, формулы, charts, **PivotTables**, форматирование; умеет вносить изменения в книгу по описанию. | https://support.microsoft.com/en-us/excel/copilot/frequently-asked-questions-about-copilot-in-excel | 2026-07-22 |
| 9 | Для Copilot данные лучше как **Excel Table** или supported range (одна строка заголовков, без пустых/merged headers и т.д.); работает на файлах с **AutoSave**. | https://support.microsoft.com/en-au/topic/format-data-for-copilot-in-excel-1604c8eb-57f1-4db1-8363-d53336228c65 | 2026-07-22 |
| 10 | Создание PivotTable через Copilot: кнопка Copilot → описать нужную сводку естественным языком (примеры промптов на Support). | https://support.microsoft.com/en-us/topic/create-pivottables-with-copilot-in-excel-93f14f4e-1cb4-4d24-9509-d36a8677d652 | 2026-07-22 |
| 11 | Microsoft прямо предупреждает: контент Copilot **может быть неточным** — review/verify до опоры на результат. | https://support.microsoft.com/en-us/excel/copilot/frequently-asked-questions-about-copilot-in-excel | 2026-07-22 |
| 12 | Copilot требует подходящую подписку Microsoft 365 / Copilot (Personal/Family/Premium/commercial Copilot и др. — см. FAQ); кнопка может отсутствовать из‑за лицензии/канала/privacy. | https://support.microsoft.com/en-us/excel/copilot/frequently-asked-questions-about-copilot-in-excel | 2026-07-22 |
| 13 | **XLOOKUP недоступен в Excel 2016 и Excel 2019**; в книге с XLOOKUP на старых версиях — ошибка имени/#NAME?. Для совместимости — ВПР / ИНДЕКС+ПОИСКПОЗ. | https://support.microsoft.com/en-us/office/xlookup-function-b7fd680e-6d10-43e6-84f9-88eae8bf5929 | 2026-07-22 |
| 14 | Практический паттерн промпта для RU-Excel: указать структуру столбцов + задачу + фразу «русская версия Excel, русские названия функций, разделитель `;`». | https://dzen.ru/a/ai2l3OAECSudCPHW ; https://dzen.ru/a/ags2OJne4hbdTbbG | 2026-07-22 |
| 15 | Пример рабочей формулы из гайдов по промптам: `=СУММЕСЛИМН(C2:C1000;B2:B1000;"Иванов";A2:A1000;">="&ДАТА(2026;1;1);…)` — шаблон «сумма по нескольким условиям». | https://dzen.ru/a/ags2OJne4hbdTbbG | 2026-07-22 |
| 16 | Антипаттерн промпта: «посчитай сумму продаж по менеджеру» без листа/столбцов/ячейки результата → нейросеть гадает; нужен СУММЕСЛИМН с явными ссылками. | https://petr-panda.ru/nejroset-chatgpt-excel/ | 2026-07-22 |
| 17 | ChatGPT для сводных: лучше просить **раскладку полей** (Rows/Columns/Values/Filters) по списку колонок; альтернатива — VBA на создание pivot или формулы SUMIFS вместо pivot cache. | https://gptprompts.ai/chatgpt-prompts-excel ; https://www.ai-toolbox.co/chatgpt-management-and-productivity/chatgpt-excel-data-analysis-guide-2026 | 2026-07-22 |
| 18 | Практическое разделение (обзоры 2026): **Copilot** сильнее как Excel-оператор in-grid; **ChatGPT** — как гибкий аналитик/отладчик формул и скриптов (часто copy-paste). | https://www.datastudios.org/post/chatgpt-5-4-vs-microsoft-copilot-for-spreadsheet-analysis-which-ai-is-better-for-excel-heavy-work-a ; https://www.excelmojo.com/excel-copilot-vs-chatgpt-spreadsheets-2026/ | 2026-07-22 |
| 19 | Независимые тесты формул (Talkory, 30 задач): Claude часто лидирует на сложных массивах/LAMBDA; ChatGPT силён на lookup; Copilot — на интеграции. *Один бенчмарк — не абсолют; для статьи: «проверяй на своих данных».* | https://www.talkory.ai/blog/best-ai-for-excel-formulas-2026 | 2026-07-22 |
| 20 | Плагин/UDF-пути (API-ключ в Excel) существуют, но это отдельный IT-контур; для большинства финансистов старт — чат + copy-paste формулы или официальный add-in/Copilot. | https://habr.com/ru/companies/sberbank/articles/918676/ | 2026-07-22 |

**Не использовать как факт без оговорки:** любые показы Wordstat до подключения MCP-KV; цены сторонних «Excel AI агентов»; заявления блогов про «GPT-5.5 / GA May 2026» без сверки с OpenAI; бенчмарк 87,3% как «ваша точность формул».

---

## Структура H2/H3 для будущей статьи (спека для writer)

Следовать карточке B17; ниже — наполнение.

### H2: Какие задачи Excel реально отдать нейросети

- **Делать:** формулы с условиями, lookup, очистка текста/дат/дублей, дизайн сводной, объяснение чужой формулы, черновик VBA/Power Query шагов.
- **Не делать:** «проверь всю книгу на 200k строк», юридически значимый расчёт без сверки, загрузка сырой 1С с ФИО/ИНН.
- Таблица: задача → канал (чат / Copilot / add-in) → что проверить руками.

### H2: ChatGPT vs Claude для длинных выгрузок и формул

- ChatGPT: быстрые формулы, add-in Excel/Sheets (официально), удобный итеративный дебаг.
- Claude: часто сильнее на длинном контексте и сложных вложенных формулах (по независимым обзорам) — *формулировать осторожно*.
- Copilot: если уже в M365 с лицензией — in-grid Pivot/формулы.
- Рекомендация: один основной чат + обязательная сверка; для критичных формул — второй прогон другой моделью.

### H2: 10 рабочих промптов

Минимум 10 нумерованных шаблонов (копипаст):

1. СУММЕСЛИМН (менеджер + период)  
2. XLOOKUP / fallback ВПР (с оговоркой версии)  
3. Сводная: раскладка полей  
4. Удаление дублей (логика / Power Query шаги)  
5. Текст по столбцам / разделитель  
6. Нормализация дат из выгрузки 1С  
7. TRIM/очистка пробелов и неразрывных  
8. Обработка #Н/Д / ЕСЛИОШИБКА  
9. «Вот ошибка Excel — исправь»  
10. «Формула + проверка на примере строк 2 и 5»  

В каждый — блок про RU-Excel.

### H2: Как проверять формулы, чтобы не поймать галлюцинацию в сумме

Чеклист 6–8 пунктов: контрольная сумма блока; 2 тестовые строки; смена фильтра; сверка с ручным подсчётом; не принимать EN-формулу в RU-книге; не доверять «красивому» объяснению без цифр.

### H2: Когда пора уходить из «просто Excel» в скрипт или staging

Триггеры: ежедневный повтор, две выгрузки на join, файл тормозит, нужна воспроизводимость → Python/Cursor, лист `raw_*`, ссылки на B19/B20/B01-контур.

### FAQ (из карточки)

- Можно ли загружать выгрузку 1С? — только обезличенный срез / схема; иначе B11.  
- Хватит ли бесплатного тарифа? — для copy-paste формул часто да; add-in/Copilot — по подписке (факты OpenAI/Microsoft выше).  
- Excel Copilot vs ChatGPT? — оператор in-grid vs гибкий чат-аналитик; hybrid ок.

### Internal links

- `/ot-excel-k-fin-konturu-30-dney/`  
- `/vibe-coding-finansist/`  
- дополнительно уместно: `/obezlichivanie-dannyh-chatgpt-finansist/`

### CTA (conversion-map)

- Telegram `finance_modern` ≤2  
- Клуб `club.koda-fd.ru` ≤2 с UTM `utm_campaign=nejroset-excel-formuly-finansist`  
- Сайт koda-fd.ru ≤1  
- Не использовать koda_salebot

---

## Handoff

Готово к **excalibur-blog-writer**.  
Артефакты: `research-context.json`, `research-serp.json` (обновлён WebSearch), `research-notes.md`, `utility-gate-topic.json`.
