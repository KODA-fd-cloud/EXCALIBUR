# Research notes — B58

**topic_id:** B58  
**slug:** reestr-upd-google-sheets  
**h1:** Как вести реестр УПД и счетов-фактур в Google Sheets без потери комплекта  
**research_date:** 2026-08-15  
**publish_target:** koda-fd.ru/blog  
**utility_gate:** PASS (`workflow`, mode B)  
**author_id:** olga-kondratskaya  
**internal_links (карточка):** `/avtomatizaciya-finansov-no-code/`, `/obezlichivanie-dannyh-chatgpt-finansist/`  
**related_published:** `/statusy-edo-google-sheets/`, `/reestr-dogovorov-google-sheets/`, `/google-apps-script-finansist-obnovit-dannye/`  
**cover_scene_hint:** abstract holographic finance automation dark #0a0a0f purple #8b5cf6, no text

---

## utility_verdict

**PASS** — тема utility-only workflow. Читатель получает: структуру **внутреннего** реестра УПД и счетов-фактур в Google Sheets с контролем «комплекта» (документ ↔ договор ↔ оплата ↔ статус ЭДО), правила безопасности данных, маршруты наполнения (ручной / CSV / Apps Script / n8n) и чеклист сверки без потери строк. Не новость «УПД 2026 обязателен», не скачивание бланка Excel.

---

## reader_outcome

После гайда бухгалтер или финансист сможет собрать в Google Sheets реестр входящих и исходящих УПД и счетов-фактур с едиными колонками, статусами комплектности («есть УПД / нет оплаты / ждём подписи»), защитой от дублей и регламентом еженедельной сверки — без смешения с официальным журналом посредника и без выгрузки сырых ПДн в облако.

---

## action_outline

1. **Проверить, нужен ли реестр в Sheets** — 20–500 документов/мес, несколько ответственных, нет готового модуля в 1С/ЭДО-дашборде; **не** подменяет обязательный журнал учёта СФ для посредников (ст. 174 НК РФ) и книги покупок/продаж.
2. **Зафиксировать «комплект»** — для каждой сделки: договор/заказ → исходящий или входящий УПД (статус 1 или 2) → при необходимости отдельный счёт-фактура → статус ЭДО → платёж; правило: одна строка реестра = один первичный документ с уникальным `doc_key` (ИНН + номер + дата + тип).
3. **Создать листы «Исходящие» и «Входящие»** — колонки: `doc_key`, тип (УПД/СФ), статус УПД (1/2), № и дата, контрагент, ИНН/КПП, сумма без НДС, НДС, всего, код операции (01/02/…), № договора, ссылка на файл (Drive/ЭДО), `edo_status`, `payment_status`, `kit_status`, ответственный, `updated_at`.
4. **Настроить валидацию и анти-дубли** — выпадающие списки типов и статусов; `=COUNTIF($A:$A,A2)>1` для подсветки дублей; проверка дат; защита шапки; отдельный лист `log` для ошибок импорта.
5. **Блок безопасности** — в таблицу: ИНН, суммы, номера документов; **не** класть: паспортные данные, полные реквизиты счетов контрагентов, сканы с подписью «as is» в общий доступ; см. internal `/obezlichivanie-dannyh-chatgpt-finansist/`.
6. **Выбрать маршрут наполнения** — (A) ручной ввод в день получения/отправки; (B) еженедельный CSV из кабинета ЭДО → Apps Script merge; (C) API оператора + Sheets (см. `/statusy-edo-google-sheets/`); (D) n8n/Make: папка `incoming_docs` → OCR/LLM → строка со статусом `draft` → бухгалтер `approved`.
7. **Формулы контроля комплекта** — `kit_status`: «OK» если `edo_status`=подписан обеими **и** `payment_status`=оплачен; «Дыра» если есть УПД без договора или СФ без связанного УПД (статус 1); условное форматирование красным для «ждём подписи > N дней».
8. **Проверка недели 1** — сверить 10 случайных строк с кабинетом ЭДО/1С; отдельно кейсы: УПД статус 2 (без СФ), аванс со строкой 5б, исправительный/корректировочный документ; чеклист типичных ошибок (текст вместо даты, другой формат номера).
9. **Что автоматизировать дальше** — связка с реестром договоров (B51), авто-статусы ЭДО (B46), approval-очередь через n8n (ezgpt-паттерн); при >1000 строк/мес — миграция метаданных в 1С, Sheets оставить как дашборд.

---

## Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT AUTH WARNING:** сервер MCP `user-mcp-kv` в этой Cloud-сессии **не подключён** (доступен только `cursor-cloud`). Вызов `wordstat_get_top_requests` **не выполнен**. Точные показы/мес **не получены** и **не выдуманы**.

Обновление токена / подключение MCP-KV: https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

**Экспертная семантика (LSI для writer, без цифр спроса):**

| Кластер | Фразы | Роль |
| --- | --- | --- |
| Primary | реестр упд google sheets, реестр счетов фактур google таблицы | H1, title |
| Workflow | как вести реестр упд, контроль комплекта документов, журнал учета счетов фактур excel sheets | H2 структура |
| UPD 2026 | упд 5.03 2026, новая форма упд апрель 2026, строка 5б упд | контекст 1–2 абзаца |
| EDO | статусы эдо реестр, выгрузка упд из диадок, электронный упд реестр | interlink B46 |
| Automation | автоматизация финотдела google sheets, apps script первичка, n8n счета акты | H2 маршруты |
| Security | реестр без персональных данных, обезличивание первички | FAQ |

**SEO-вывод:** SERP по `реестр упд google sheets` **перекошен в бланки УПД 2026 и новости ЭДО**, прямых how-to про Google Sheets почти нет. Конкурентный зазор КОДА: **внутренний реестр комплектности** (УПД + СФ + оплата + ЭДО) в Sheets, с отличением от **официального журнала посредника** и от **скачивания формы 5.03**.

---

## SERP (WebSearch Cursor, 15.08.2026)

### Primary: «реестр упд google sheets 2026»

| # | URL | Тип | Пробел для КОДА |
| --- | --- | --- | --- |
| 1 | https://buh.ru/articles/upd-s-1-yanvarya-2026-goda-kto-obyazan-primenyat-i-kak-bezboleznenno-pereyti.html | explainer УПД 2026 | Нет Sheets; обязательность только для ЭДО |
| 2 | https://spmag.ru/blanks/novaya-forma-upd-s-1-aprelya-2026-goda | бланк УПД | Excel/PDF, не реестр |
| 3 | https://glavkniga.ru/situations/k511708 | образец УПД онлайн | Заполнение одного документа |
| 4 | https://www.moysklad.ru/poleznoe/formy-dokumentov/universalnyj-peredatochnyj-dokument/ | бланк Excel | Не workflow реестра |
| 5 | https://blank-kit.ru/documents/new/upd | онлайн-генератор УПД | XML 5.03, не учётный реестр |
| 6 | https://www.business.ru/article/5830-upd-s-2026-goda | обзор перехода | Нет Google Sheets |

**Вывод:** шаг 0 `research-serp.json` по primary **нерелевантен intent** — игнорируем как SERP; приоритет WebSearch выше.

### Secondary: «автоматизация финотдела google sheets реестр документов 2026»

| # | URL | Тип | Пробел |
| --- | --- | --- | --- |
| 1 | https://ezgpt.ru/articles/kak-sdelat-ii-agenta-dlya-schetov-aktov-i-pervichki | n8n + Sheets queue | УПД в очереди, но не структура реестра комплекта |
| 2 | https://pdf2sheets.app/ru/zachem-perevodit-pdf/kak-sobrat-nakladnye-v-odnu-tablicu/ | PDF → Sheets | Колонки реестра, без УПД/НДС-кодов |
| 3 | https://scand.com/ru/company/blog/best-google-sheets-add-ons/ | add-ons | Общая автоматизация |
| 4 | https://koda-fd.ru/blog/ai-dlya-finansista-2026/ | свой блог | Макро, не реестр УПД |
| 5 | https://developers.google.com/apps-script | API docs | EN; нужен RU-контекст финотдела |

### H1-aligned: «реестр УПД счетов-фактур контроль комплект» / «как собрать накладные в одну таблицу»

| # | URL | Заметка |
| --- | --- | --- |
| 1 | https://pdf2sheets.app/ru/zachem-perevodit-pdf/kak-sobrat-nakladnye-v-odnu-tablicu/ | Эталон колонок реестра первички в Sheets |
| 2 | https://www.glavbukh.ru/art/386589-jurnal-ucheta-poluchennyh-i-vystavlennyh-schetov-faktur | Официальный журнал СФ — **не** наш продукт, но поля для маппинга |
| 3 | https://ppt.ru/art/schet-faktura/zhurnal-ucheta-poluchennykh-i-vystavlennykh-schetov-faktur | Коды операций 01/02 для колонки реестра |
| 4 | https://nalog-nalog.ru/nds/zhurnal_schetovfaktur/zhurnal_registracii_schetov-faktur_-_obrazec-nn/ | Хронология, квартальная сдача — только для посредников |
| 5 | https://www.kontur-extern.ru/info/54586-ispolzovanie_upd_i_schet_faktury | УПД vs СФ — FAQ для writer |
| 6 | https://www.diadoc.ru/articles/82777-rekomendacii_fns_po_zapolneniyu_schetov_faktur_i_upd | Рекомендации ФНС по реквизитам |

### Контекст УПД 2026 (1 абзац в статье, не ядро)

| # | URL | Факт для статьи |
| --- | --- | --- |
| 1 | https://bazanpa.ru/vopros/obyazatelnyj-upd-v-2026-godu-kak-oformlyat-otgruzku-tovarov-raboty-i-uslugi/ | ЭДО → только УПД 5.03; бумага и неформализованный ЭДО — без принуждения |
| 2 | https://rarus.ru/publications/20260115-otvety-lk-1c-rarus-obyazatelno-li-primenyat-elektronny-format-upd-s-2026-goda-801724/ | Нет обязанности УПД для всех; отмена форматов ≠ запрет актов |
| 3 | https://blank-kit.ru/blog/novaya-forma-upd-2026-stroka-5b | Строка 5б, ОГРНИП, НДС 22% с 01.04.2026 |

### Конкурентный зазор

1. **Sheets-first реестр комплектности**, а не «скачайте бланк УПД».
2. **Два контура:** исходящие / входящие + связка с оплатой и ЭДО (interlink B46).
3. **Явное отличие** от журнала учёта СФ посредника (кто обязан / кто нет).
4. **Контроль «без потери комплекта»** — формулы `kit_status`, анти-дубли, регламент внесения в день документа.
5. **Безопасность облака** — без сырых ПДн (interlink B11).
6. **Три уровня автоматизации:** ручной → CSV → API/n8n.

**Cannibalization:** B46 (статусы ЭДО), B51 (реестр договоров), B22 (Apps Script) — перелинковка, не копировать H2 1:1.

---

## Таблица фактов

| # | Утверждение | Источник | Дата проверки |
| --- | --- | --- | --- |
| 1 | УПД объединяет счёт-фактуру и первичный документ; статус «1» — с СФ, статус «2» — без СФ. | https://buh.ru/articles/upd-s-1-yanvarya-2026-goda-kto-obyazan-primenyat-i-kak-bezboleznenno-pereyti.html | 2026-08-15 |
| 2 | УПД нельзя использовать, когда нужен **только** счёт-фактура без первички (письмо ФНС № АС-4-15/16298@). | https://buh.ru/articles/upd-s-1-yanvarya-2026-goda-kto-obyazan-primenyat-i-kak-bezboleznenno-pereyti.html | 2026-08-15 |
| 3 | С 01.01.2026 утратили силу форматы электронных ТОРГ-12 и актов (приказ ФНС № ЕД-7-26/28@); для ЭДО — УПД формата 5.03. | https://buh.ru/articles/upd-s-1-yanvarya-2026-goda-kto-obyazan-primenyat-i-kak-bezboleznenno-pereyti.html | 2026-08-15 |
| 4 | Переход на обязательный электронный УПД касается компаний, которые **уже** обмениваются отгрузочными документами через ЭДО; бумажные ТОРГ-12 и акты сохраняются. | https://buh.ru/articles/upd-s-1-yanvarya-2026-goda-kto-obyazan-primenyat-i-kak-bezboleznenno-pereyti.html ; https://bazanpa.ru/vopros/obyazatelnyj-upd-v-2026-godu-kak-oformlyat-otgruzku-tovarov-raboty-i-uslugi/ | 2026-08-15 |
| 5 | ФНС рекомендует перейти на УПД до 01.01.2026, чтобы избежать ошибок при внедрении. | https://buh.ru/articles/upd-s-1-yanvarya-2026-goda-kto-obyazan-primenyat-i-kak-bezboleznenno-pereyti.html | 2026-08-15 |
| 6 | Новая печатная форма счёта-фактуры/УПД — с 01.04.2026 (ПП РФ № 26 от 23.01.2026); в форме строка **5б** для авансовых СФ. | https://spmag.ru/blanks/novaya-forma-upd-s-1-aprelya-2026-goda ; https://blank-kit.ru/blog/novaya-forma-upd-2026-stroka-5b | 2026-08-15 |
| 7 | Для ИП вместо свидетельства о регистрации указывают **ОГРНИП и дату присвоения** (изменения с 2026). | https://spmag.ru/blanks/novaya-forma-upd-s-1-aprelya-2026-goda | 2026-08-15 |
| 8 | Электронный XML-формат УПД 5.03 утверждён приказом ФНС № ЕД-7-26/970@; операторы ЭДО принимают 5.03 для структурированного обмена. | https://blank-kit.ru/documents/new/upd ; https://docboss.ru/blog/obyazatelnyj-perekhod-na-upd-2026 | 2026-08-15 |
| 9 | С 01.04.2026 обновлена форма **журнала** учёта полученных и выставленных счетов-фактур (ПП № 26); структура: 2 части (выставленные / полученные). | https://nalog-nalog.ru/nds/zhurnal_schetovfaktur/zhurnal_registracii_schetov-faktur_-_obrazec-nn/ | 2026-08-15 |
| 10 | Журнал учёта СФ обязателен для **посредников** (комиссия и др.); сдаётся в ИФНС ежеквартально в электронном виде по ТКС (п. 5.2 ст. 174 НК РФ). | https://www.glavbukh.ru/art/386589-jurnal-ucheta-poluchennyh-i-vystavlennyh-schetov-faktur | 2026-08-15 |
| 11 | В журнале/реестре СФ используют **коды операций** (01 — продажа, 02 — аванс и др.), те же что в книгах покупок/продаж. | https://ppt.ru/art/schet-faktura/zhurnal-ucheta-poluchennykh-i-vystavlennykh-schetov-faktur | 2026-08-15 |
| 12 | Записи в журнале СФ — в **хронологическом** порядке по дате выставления/получения. | https://nalog-nalog.ru/nds/zhurnal_schetovfaktur/zhurnal_registracii_schetov-faktur_-_obrazec-nn/ | 2026-08-15 |
| 13 | Для внутреннего реестра в таблице типовые поля: № документа, дата, контрагент, сумма, НДС/ставка, итог, ссылка на PDF. | https://pdf2sheets.app/ru/zachem-perevodit-pdf/kak-sobrat-nakladnye-v-odnu-tablicu/ | 2026-08-15 |
| 14 | Паттерн автоматизации первички: очередь в Sheets со статусами `draft` / `approved` / `needs_fix` / `rejected` после OCR+LLM. | https://ezgpt.ru/articles/kak-sdelat-ii-agenta-dlya-schetov-aktov-i-pervichki | 2026-08-15 |
| 15 | Google Sheets API **не атомарен** — после записи агент/скрипт должен перечитывать строку для верификации. | https://ezgpt.ru/articles/kak-sdelat-ii-agenta-dlya-schetov-aktov-i-pervichki | 2026-08-15 |
| 16 | Runtime Apps Script — до **6 минут** на запуск; UrlFetch — 20 000 вызовов/день (consumer). | https://developers.google.com/apps-script/guides/services/quotas | 2026-08-15 |
| 17 | При изменениях в форме счёта-фактуры те же реквизиты нужно вносить в используемую форму УПД (письмо ФНС № ЗГ-3-3/4368@). | https://buh.ru/articles/upd-s-1-yanvarya-2026-goda-kto-obyazan-primenyat-i-kak-bezboleznenno-pereyti.html | 2026-08-15 |
| 18 | Нет законодательной обязанности оформлять **внутренний** реестр УПД именно в Google Sheets — это управленческий инструмент контроля комплекта. | https://pdf2sheets.app/ru/zachem-perevodit-pdf/kak-sobrat-nakladnye-v-odnu-tablicu/ ; https://rarus.ru/publications/20260115-otvety-lk-1c-rarus-obyazatelno-li-primenyat-elektronny-format-upd-s-2026-goda-801724/ | 2026-08-15 |
| 19 | Ставка НДС **22%** и новые графы книг покупок/продаж — контекст для колонок реестра с апреля 2026. | https://www.rnk.ru/article/217794-upd-blank-obrazets | 2026-08-15 |
| 20 | Официального шаблона «реестра УПД в Google Sheets» от ФНС **не существует** — таблицу проектирует финотдел под свой комплект. | https://www.moysklad.ru/poleznoe/formy-dokumentov/universalnyj-peredatochnyj-dokument/ ; WebSearch synthesis 2026-08-15 | 2026-08-15 |

**Не выдумывать:** точные показы Wordstat; «экономия X часов» без замера; обязательность Google Sheets для всех; что внутренний реестр заменяет журнал посредника или книги покупок/продаж.

**fact-bank.md:** прямых строк про УПД/Sheets нет — все цифры и даты только из таблицы выше.

---

## Структура H2 для writer (из карточки B58)

1. Когда это нужно финотделу (и когда нет)  
2. Подготовка данных и безопасность (без сырых ПДн в облако)  
3. Пошаговая настройка таблицы, формул и сценария наполнения  
4. Проверка результата и типичные ошибки  
5. Что автоматизировать дальше  

**Workflow-схема для статьи:**  
`Документ в ЭДО/почте → строка в реестре → статус подписи → привязка к договору/оплате → kit_status OK → еженедельная сверка с 1С`

---

## FAQ-кандидаты (из карточки)

- Можно ли без программиста? (да: структура + CF + ручной/CSV; API — по шаблону B46)
- Сколько займёт внедрение? (2–4 ч MVP таблицы; +1–2 дня при API)
- Какие риски для данных в Google Sheets?
- Чем реестр в Sheets отличается от журнала учёта СФ?
- Нужен ли реестр, если уже есть 1С и ЭДО?
- Как учитывать УПД статус 2 и отдельные счета-фактуры?

---

## CTA / interlink

- Internal: `/avtomatizaciya-finansov-no-code/`, `/obezlichivanie-dannyh-chatgpt-finansist/`, `/statusy-edo-google-sheets/`, `/reestr-dogovorov-google-sheets/`
- CTA: club.koda-fd.ru (utm_campaign=reestr-upd-google-sheets), t.me/finance_modern
- **Запрет:** salebot

---

## Handoff marker

`=== EXCALIBUR BLOG RESEARCH ===` — см. `.cursor/excalibur-blog-handoff.md`
