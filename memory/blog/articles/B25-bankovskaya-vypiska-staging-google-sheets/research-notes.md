# Research notes — B25

**topic_id:** B25  
**slug:** bankovskaya-vypiska-staging-google-sheets  
**h1:** Как разложить банковскую выписку в staging-таблицу без ручного копипаста  
**research_date:** 2026-07-31  
**publish_target:** сайт koda-fd.ru/blog  
**author_id:** olga-kondratskaya  
**article_mode:** B  
**utility_gate (topic):** PASS (`how_to`, mode B) — `utility-gate-topic.json`, research-context.json  
**related_published:** `/ot-excel-k-fin-konturu-30-dney/`, `/python-finansist-sverka-csv/`, `/google-apps-script-finansist-obnovit-dannye/`, `/finansovyj-minimalizm/`

---

## utility_verdict

**PASS** — utility-only how_to / workflow. Читатель получает рабочий маршрут: выгрузить выписку из клиент-банка (CSV/Excel, не PDF как основной путь) → положить сырой файл отдельно → импортировать в Google Sheets с контролем разделителя и «не преобразовывать текст» → разложить в staging-лист с фиксированными колонками (дата, сумма, контрагент, назначение, account_id, row_hash) → дедуп по hash → не править сырой слой руками → отдать staging в ДДС / сверку / дашборд. Не обзор SaaS-конвертеров PDF, не настройка DirectBank в 1С, не «что такое staging».

---

## reader_outcome

После гайда финансист сможет за вечер собрать в Google Sheets контур «сырой файл → staging-лист с едиными колонками и hash-дедупом» для одной банковской выписки (и понять, как масштабировать на несколько счетов) без копипаста строк в отчёт.

---

## action_outline

1. **Зафиксировать DoD** — одна тестовая выписка за период; цель: лист `staging` с нормализованными колонками + контроль суммы/кол-ва строк vs банк.
2. **Выбрать формат источника** — в клиент-банке предпочесть CSV/Excel (или 1CClientBankExchange.txt только если дальше парсер); PDF/скан — запасной путь, не основа пилота.
3. **Правило слоёв** — `raw/` (файл как есть, не трогать) → лист `raw_import` → лист `staging` (формулы/QUERY/скрипт); отчёты читают только staging.
4. **Зафиксировать схему staging** — минимум: `date`, `amount`, `direction` (in/out или знак), `counterparty`, `purpose`, `account_id`, `bank_doc_id` (если есть), `row_hash`, `source_file`, `loaded_at`.
5. **Импорт без копипаста** — Файл → Импорт → Загрузка; явно разделитель (`,` / `;`); снять «Преобразовывать текст в числа, даты и формулы» для ключей/счетов; проверить кодировку (кракозябры → пересохранить UTF-8 / указать Windows-1251 при экспорте из банка).
6. **Нормализация** — единый формат даты, сумма как число (запятая→точка или VALUE), trim контрагента/назначения, `account_id` на каждый счёт.
7. **Дедуп** — `row_hash` = хэш от (date + amount + purpose + account_id + bank_doc_id); при повторной загрузке того же файла не плодить строки; журнал `load_log`.
8. **Контроль качества** — сверка итога оборотов/остатка с PDF-сводкой банка; 5 случайных строк глазами; несколько счетов = отдельные `account_id`, один staging.
9. **Куда дальше** — из staging: категории ДДС / план-факт (B26), сверка CSV (B19), автозагрузка Apps Script (B22), контур 30 дней (legacy).

---

## Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT unavailable:** сервер MCP `user-mcp-kv` в этой Cloud-сессии **не найден** в каталоге MCP (доступны только Cursor Automation Tools и cursor-cloud). Инструмент `wordstat_get_top_requests` **не вызван**. Точные показы/мес **не получены** и **не выдуманы**.

⚠️ **WORDSTAT AUTH WARNING (на будущее):** при 401 обновить токен: https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

**Экспертная семантика (без цифр спроса) — LSI для копирайтера:**

| Кластер | Фразы | Роль |
| --- | --- | --- |
| Primary | банковская выписка в excel автоматически, выписка банка в excel | H1/лид |
| Sheets | загрузка выписки в google sheets, импорт csv google таблицы | H2 импорт |
| Staging | staging таблица финансы, сырой слой выписка, нормализация выписки | H2 схема |
| 1С angle | нормализация выписки 1с, клиент банк выписка txt, 1CClientBankExchange | FAQ / граница темы |
| Качество | дедуп банковских операций, hash транзакции, кодировка cp1251 csv | H2 ловушки |
| Дальше | ддс из выписки, сверка банка и 1с, дашборд денежных потоков | H2 «куда дальше» |

**SEO-вывод:** SERP по primary забит **PDF→Excel конвертерами** и шаблонами. Угол КОДА: **staging-слой в Google Sheets** (колонки + hash + не трогать raw), не SaaS-парсер и не «как разнести в 1С».

---

## SERP (WebSearch Cursor, 31.07.2026)

`research-serp.json` preflight есть, но доминируют конвертеры/шаблоны; приоритет — живой WebSearch ниже.

### Primary / «банковская выписка в excel автоматически»

| # | URL | Тип | Пробел для КОДА |
| --- | --- | --- | --- |
| 1 | https://clearvaultapp.com/ru | SaaS: PDF/MT940/CSV↔Excel | Нет staging-схемы для управленки |
| 2 | https://airparser.com/ru/bank-statement-parser/ | ИИ PDF→Excel/Sheets | Облачный парсер; не «свой» контур |
| 3 | https://bankstatementparser.com/ru | Python OSS, 7 форматов | Для разработчика; нет Sheets-ритуала финансиста |
| 4 | https://www.easybankconvert.com/ru/guides/bank-statement-formats-explained | Обзор форматов PDF/CSV/OFX | Справочник, без action outline staging |
| 5 | https://pdf.wondershare.com.ru/excel/bank-statement-pdf-to-excel.html | PDF→Excel утилита | Продуктовый гайд OCR |

### Secondary / Google Sheets + выгрузка

| # | URL | Тип | Пробел для КОДА |
| --- | --- | --- | --- |
| 6 | https://rko.by/tri-sposoba-vygruzki-bankovskikh-vypisok-v-google-sheets-i-excel | 3 способа: файл / email / API | Близко; мало про схему колонок и hash-дедуп |
| 7 | https://www.rocketstatements.com/blog/convert-bank-statements-to-google-sheets-2026-5-methods-compared-free-template | EN 2026: 5 методов → Sheets | Западный SaaS; полезно как карта методов |
| 8 | https://support.google.com/docs/answer/3093335?hl=ru | IMPORTDATA (офиц.) | Только URL-CSV; не файл с диска |
| 9 | https://help.loyverse.com/ru/help/how-open-csv-file-google-sheets | Импорт CSV: снять «преобразовывать текст» | Нет фин-контекста |
| 10 | https://splitforge.app/blog/google-sheets-csv-import-errors-fix | Encoding / `;` / leading zeros | Техсправочник ошибок импорта |

### Secondary / 1С и нормализация

| # | URL | Тип | Пробел для КОДА |
| --- | --- | --- | --- |
| 11 | https://kvant-c.ru/faq/1c-client-bank-exchange/ | Клиент-банк vs DirectBank | 1С-фокус; staging Sheets не тема |
| 12 | https://kvant-c.ru/faq/1c-klient-bank-obmen-sberbank-vtb/ | Дубли контрагентов, кодировки, CSV-парсеры | Факты про боли загрузки — в FAQ |
| 13 | https://saldovka.com/2026-exp/bankovskie-vypiski-v-1s-8-3.html | DirectBank / txt / ручной ввод | Бухучёт 1С, не управленческий staging |
| 14 | https://dipbuh.ru/blog/instruktsiya-po-vygruzke-bankovskoy-vypiski-iz-internet-banka-tinkoff/ | Тинькофф: PDF vs 1С TXT | Конкретный банк — пример форматов |

### Конкурентный зазор (serp_gap)

1. **Staging как слой** (raw → staging → ДДС), а не «конвертни PDF в Excel».
2. **Фиксированная схема колонок + row_hash** — в топе почти нет.
3. **RU-ловушки импорта:** `;`, Windows-1251, «преобразовывать текст в числа/даты», несколько счетов.
4. Граница с 1С: статья **не** про разнесение в Бухгалтерии; staging — для управленки/сверки/дашборда.
5. Мост к published: B19 (сверка CSV), B22 (Apps Script «Обновить»), legacy 30 дней контур.

---

## Сверка с fact-bank.md

В `memory/brief/fact-bank.md` на 2026-07-31 **нет** строк про банковские выписки, staging, Google Sheets импорт или клиент-банк. Цифры из fact-bank (ИИ-заводы, Make/n8n) в B25 **не тащить**. Все утверждения статьи — только из таблицы фактов ниже или без чисел.

---

## Таблица фактов (только с URL; для writer)

| # | Утверждение | Источник | Дата проверки |
| --- | --- | --- | --- |
| 1 | Классический обмен 1С↔банк идёт через формат `1CClientBankExchange`; файл `.txt`, типичная кодировка Windows-1251. | https://kvant-c.ru/faq/1c-client-bank-exchange/ | 2026-07-31 |
| 2 | Имена файлов обмена в типовой настройке: выгрузка `1c_to_kl.txt`, загрузка `kl_to_1c.txt`; кодировка Windows (1251). | https://kvant-c.ru/faq/1c-client-bank-exchange/ | 2026-07-31 |
| 3 | DirectBank — прямой обмен 1С↔банк без файлов; среди банков: Сбербанк, ВТБ, Альфа-Банк, Тинькофф и др.; нужен ИТС ПРОФ. | https://kvant-c.ru/faq/1c-client-bank-exchange/ | 2026-07-31 |
| 4 | Частая причина сбоя загрузки: UTF-8 вместо Windows-1251 / неверный формат; нужен именно `1CClientBankExchange`. | https://kvant-c.ru/faq/1c-client-bank-exchange/ | 2026-07-31 |
| 5 | Выгрузка из банка может быть в Windows-1251, UTF-8 или DOS; неверная кодировка в обработке даёт «кракозябры» в назначениях. | https://kvant-c.ru/faq/1c-klient-bank-obmen-sberbank-vtb/ | 2026-07-31 |
| 6 | Ряд банков/эквайринг/маркетплейсы отдают CSV/Excel, а не стандарт 1CClientBankExchange — нужны отдельные парсеры/маппинг колонок. | https://kvant-c.ru/faq/1c-klient-bank-obmen-sberbank-vtb/ | 2026-07-31 |
| 7 | В Тинькофф-бизнесе выписку можно создать как PDF или как формат 1С (TXT). | https://dipbuh.ru/blog/instruktsiya-po-vygruzke-bankovskoy-vypiski-iz-internet-banka-tinkoff/ | 2026-07-31 |
| 8 | Три рабочих канала данных в таблицы: файл CSV/OFX/MT940 + импорт; email-вложения; API/интеграторы (Make/Zapier и т.п.). | https://rko.by/tri-sposoba-vygruzki-bankovskikh-vypisok-v-google-sheets-i-excel | 2026-07-31 |
| 9 | Практичный старт недели: проверить форматы банка → один тестовый файл в Sheets → ежедневная проверка первых 5 строк + журнал ошибок. | https://rko.by/tri-sposoba-vygruzki-bankovskikh-vypisok-v-google-sheets-i-excel | 2026-07-31 |
| 10 | Типичные ошибки автоматизации: разные поля у разных банков, пароли в скриптах, часовые пояса, автомат без тестовой выборки, комиссии при сверке. | https://rko.by/tri-sposoba-vygruzki-bankovskikh-vypisok-v-google-sheets-i-excel | 2026-07-31 |
| 11 | `IMPORTDATA` в Google Sheets импортирует CSV/TSV **по URL** (нужен протокол http/https), не локальный файл с диска. | https://support.google.com/docs/answer/3093335?hl=ru | 2026-07-31 |
| 12 | При импорте CSV через Файл → Импорт рекомендуется снять флажок «Преобразовывать текст в числа, даты и формулы». | https://help.loyverse.com/ru/help/how-open-csv-file-google-sheets | 2026-07-31 |
| 13 | Европейские/RU CSV часто с разделителем `;`; при неверном разделителе все данные падают в одну колонку — задать Custom separator. | https://splitforge.app/blog/google-sheets-csv-import-errors-fix | 2026-07-31 |
| 14 | ANSI/Windows-1252 vs UTF-8 даёт кракозябры; перед импортом перекодировать в UTF-8 или выбрать нужный charset в диалоге. | https://splitforge.app/blog/google-sheets-csv-import-errors-fix | 2026-07-31 |
| 15 | Автоконвертация текста в числа срезает ведущие нули у счетов/ID — импорт как текст, затем точечно NUMBER для сумм. | https://splitforge.app/blog/google-sheets-csv-import-errors-fix | 2026-07-31 |
| 16 | Bank Statement Parser (OSS): 7 форматов (CAMT.053, PAIN.001, CSV, OFX, QFX, MT940, PDF) → pandas; локальная обработка. | https://bankstatementparser.com/ru | 2026-07-31 |
| 17 | ClearVault заявляет конвертацию PDF/CSV/Excel/MT940/OFX и поддержку выгрузок российских банков (Сбер, ВТБ, Альфа, Тинькофф и др.) в CSV/Excel. | https://clearvaultapp.com/ru | 2026-07-31 |
| 18 | Airparser: экспорт выписки в Excel/CSV/JSON и опционально в Google Sheets / Zapier/Make. | https://airparser.com/ru/bank-statement-parser/ | 2026-07-31 |
| 19 | В 1С 8.3 три пути: DirectBank, клиент-банк (txt), ручной ввод документов. | https://saldovka.com/2026-exp/bankovskie-vypiski-v-1s-8-3.html | 2026-07-31 |
| 20 | Сбербанк Бизнес Онлайн: экспорт выписок в т.ч. Excel, txt, dbf, 1C, SWIFT MT940 (по материалам справочников СБОЛ). | https://sberbank-info.com/eksport-v-1s-v-biznes-onlajn.html | 2026-07-31 |

**Не использовать без источника:** «экономия N часов в день», «% ошибок копипаста», цены SaaS-конвертеров, гарантии OCR 100%, обещания DirectBank «везде».

---

## Угол статьи (mode B)

**Сцена:** CFO/финменеджер каждое утро копирует строки из выгрузки банка в «главный» Excel/Sheets для ДДС — колонки плывут, дубли после повторной загрузки, второй счёт ломает свод.

**Ответ:** staging-таблица в Google Sheets: сырой файл не трогаем → импорт с контролем `;`/кодировки → единые колонки + `row_hash` → отчёты только из staging.

**Голос:** «я» Ольги; шаги; схема `raw → staging → ДДС`; таблица колонок; чеклист ловушек; FAQ про клиент-банк и несколько счетов. Без TL;DR-простыни. CTA ≤2: Telegram + клуб.

**Мини-схема для writer:**

```text
Клиент-банк (CSV/XLSX)
  → Drive/папка raw (файл как есть)
  → Google Sheets: raw_import
  → staging (нормализация + row_hash + account_id)
  → ДДС / сверка / дашборд
```

**Рекомендуемые колонки staging (черновик):**

| Колонка | Зачем |
| --- | --- |
| date | единый YYYY-MM-DD или ДД.ММ.ГГГГ |
| amount | число; знак или отдельный direction |
| counterparty | trim; без ручного «улучшения» в raw |
| purpose | назначение платежа |
| account_id | какой р/с |
| bank_doc_id | номер п/п если есть |
| row_hash | дедуп повторных загрузок |
| source_file | имя файла выгрузки |
| loaded_at | когда положили в staging |

---

## FAQ-заготовки (ответы-действия)

1. **Подойдёт ли выписка из клиент-банка?** — Да, если есть CSV/Excel; для txt `1CClientBankExchange` нужен разбор полей или конвертация в таблицу до staging; PDF — только после конвертации + ручная сверка сумм.
2. **Несколько счетов?** — Один лист staging, колонка `account_id`; сырые файлы хранить отдельно на счёт; hash включает account_id.
3. **Зачем не править raw?** — Повторная загрузка и аудит: staging можно пересобрать из файла; правки только в правилах нормализации.
4. **Это замена 1С?** — Нет. Staging — управленческий слой; в 1С — учётные документы (DirectBank/клиент-банк — отдельный контур).
5. **Как автоматизировать дальше?** — Папка на Drive + Apps Script (см. B22) или n8n; сначала ручной пилот одной выписки.

---

## Риски для writer / QA

- Не обещать «полный автомат без проверки» — контроль 5 строк обязателен.
- Не рекомендовать заливать ПДн/полные реквизиты в публичные онлайн-конвертеры PDF без дисклеймера.
- Не путать статью с B19 (сверка двух CSV) и B22 (кнопка Apps Script) — здесь ядро = **схема staging**.
- В тексте: без длинного тире «—», без ёлочек «», без эмодзи (site-brief).

---

## Handoff checklist

- [x] utility_gate topic PASS  
- [x] Wordstat: unavailable (MCP отсутствует) — цифры не выдуманы  
- [x] WebSearch Cursor по primary + secondary  
- [x] fact-bank сверен (релевантных строк нет)  
- [x] action_outline 9 шагов, reader_outcome, utility_verdict PASS  
- [ ] article.html — зона writer  
