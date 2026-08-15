# Research notes — B59

**topic_id:** B59  
**slug:** zayavka-na-rashod-google-forms  
**h1:** Как принимать заявки на расход через Google Forms в реестр Sheets  
**research_date:** 2026-08-15  
**publish_target:** koda-fd.ru/blog  
**utility_gate:** PASS (`workflow`, mode B)  
**author_id:** olga-kondratskaya  
**internal_links (карточка):** `/avtomatizaciya-finansov-no-code/`, `/obezlichivanie-dannyh-chatgpt-finansist/`  
**related_published:** `/reestr-dogovorov-google-sheets/`, `/google-apps-script-finansist-obnovit-dannye/`  
**cover_scene_hint:** abstract holographic finance automation dark #0a0a0f purple #8b5cf6, no text

---

## utility_verdict

**PASS** — тема utility-only workflow. Читатель получает: схему **внутренней** заявки на расход (не бухгалтерская «заявка на кассовый расход» и не «Заявка на расход ДС» в 1С), поля формы, связку Forms → реестр в Google Sheets, колонки согласования, уведомления и чеклист проверки без выгрузки сырых ПДн в общий доступ. Не новость про автоматизацию финотдела, не скачивание бланка Excel.

---

## reader_outcome

После гайда финансист или офис-менеджер сможет за 2–4 часа собрать форму заявки на расход, автоматически складывать ответы в реестр Google Sheets с колонками «статус / сумма к оплате / дата согласования», включить email-оповещения или триггер Apps Script и описать регламент: кто подаёт, кто утверждает и как сверять реестр с фактической оплатой — без программиста на MVP.

---

## action_outline

1. **Проверить, подходит ли связка Forms + Sheets** — 5–80 заявок/мес, нет модуля казначейства в 1С/ERP или нужен быстрый пилот; **не** подменяет «Заявку на расходование ДС» в 1С:ERP и **не** равна бухгалтерской «заявке на кассовый расход» (РКО из кассы).
2. **Спроектировать поля формы** — инициатор (email Workspace), отдел, статья/центр затрат, дата расхода, контрагент/назначение, сумма, валюта, обоснование, проект/договор (выпадающий список), загрузка чека (file upload); **не** собирать: паспорт, полные реквизиты личных карт, сканы с лишними ПДн.
3. **Создать форму и реестр** — `forms.new` или «Инструменты → Создать форму» в Sheets; на вкладке «Ответы» → «Установить связь с Таблицами» → новая или существующая таблица; лист ответов = черновой реестр.
4. **Добавить служебные колонки в реестр** — справа от ответов формы: `request_id`, `status` (новая / на согласовании / одобрено / отклонено / оплачено), `approver`, `approved_amount`, `payment_date`, `review_comment`, `updated_by`; защитить шапку и формулы.
5. **Настроить доступ и безопасность** — форма только для домена `@company` или списка групп; таблица: финотдел — edit, инициаторы — view своих строк (отдельный лист или фильтр); см. internal `/obezlichivanie-dannyh-chatgpt-finansist/`.
6. **Включить оповещения** — (A) в Forms: «Получать уведомления о новых ответах по эл. почте»; (B) Apps Script `onFormSubmit` на таблице — письмо согласующему или запись статуса «новая»; (C) Make/n8n при росте нагрузки.
7. **Провести тестовую заявку** — проверить: строка в листе, вложение чека на Drive, права, уведомление, ручное изменение `status` согласующим; типичные ошибки: текст вместо числа в сумме, дубль email, публичная ссылка формы.
8. **Закрепить регламент сверки** — еженедельно: строки `approved` без `payment_date`; сумма approved vs платёжка/выписка; архив отклонённых; лимит объёма (см. лимиты ответов Forms).
9. **Что автоматизировать дальше** — маршрут согласования в Make/n8n, Telegram-бот (шаблон mayai.ru), выгрузка одобренных строк в 1С; при >100 заявок/мес и жёстком бюджетном контроле — миграция в БИТ.Финанс / 1С:ERP.

---

## Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT AUTH WARNING:** сервер MCP `user-mcp-kv` в этой Cloud-сессии **не подключён** (доступен только `cursor-cloud`). Вызов `wordstat_get_top_requests` для `заявка на расход google forms` **не выполнен**. Точные показы/мес **не получены** и **не выдуманы**.

Обновление токена / подключение MCP-KV: https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

**Экспертная семантика (LSI для writer, без цифр спроса):**

| Кластер | Фразы | Роль |
| --- | --- | --- |
| Primary | заявка на расход google forms, google forms заявка на оплату | H1, title |
| Registry | реестр заявок google sheets, заявки на расход таблица | H2 реестр |
| Workflow | согласование заявок на расход, статус заявки оплачено | колонки реестра |
| Contrast RU | заявка на кассовый расход бланк, заявка на расход дс 1с | FAQ «чем не является» |
| Automation | автоматизация финотдела google sheets, apps script onFormSubmit | H2 уведомления |
| Security | заявка без персональных данных, google forms доступ домен | H2 безопасность |
| Integrations | make google forms sheets, n8n google forms | H2 «дальше» |

**SEO-вывод:** SERP по `заявка на расход google forms` **перемешивает** официальные страницы Google Forms, **бухгалтерские** подборки «заявка на кассовый расход» (Консультант+, Assistentus) и **бланки Excel**. Прямых RU how-to про **управленческий реестр заявок** в Sheets почти нет. Зазор КОДА: внутренний workflow «форма → реестр → статусы согласования → оплата», с явным отличием от кассовой заявки и 1С.

---

## SERP (WebSearch Cursor, 15.08.2026)

### Primary: «заявка на расход google forms 2026»

| # | URL | Тип | Пробел для КОДА |
| --- | --- | --- | --- |
| 1 | https://docs.google.com/forms/?hl=ru | продукт | Нет workflow реестра |
| 2 | https://www.consultant.ru/law/podborki/poryadok_zapolneniya_zayavki_na_kassovyj_rashod/ | НПА/бухучёт | **Другой документ** — кассовый расход, не Google |
| 3 | https://assistentus.ru/forma/zayavka/ | бланки 2026 | Excel/PDF, не Forms |
| 4 | https://joliform.com/blog/google-forms-expense-reimbursement-template | EN how-to | Поля reimbursement, нет RU финконтекста |
| 5 | https://www.signnow.com/features/google-forms-expense-reimbursement | EN marketing | Общие поля, нет реестра |
| 6 | https://ru.surveymonkey.com/templates/reimbursement-form-template/ | шаблон конкурента | Не Sheets-реестр |

**Вывод:** шаг 0 `research-serp.json` по primary **частично нерелевантен** (Consultant + бланки); приоритет — WebSearch + H1-aligned запросы ниже.

### H1-aligned: «Google Forms заявка расход Google Sheets реестр»

| # | URL | Заметка |
| --- | --- | --- |
| 1 | https://support.google.com/docs/answer/139706?hl=ru | Официально: связь с Таблицами, лимиты ответов |
| 2 | https://support.google.com/docs/answer/6281888?hl=ru | Создание формы, ответы в таблице |
| 3 | https://timeweb.com/ru/community/articles/sozdanie-google-formy-s-vyvodom-v-google-tablicy | RU: форма из Sheets, лист «Ответы на форму» |
| 4 | https://101-help.com/kak-ispolzovat-google-forms-v-kachestve-schetchika-raskhodov-1c3ff195d9/ | Expense tracker pattern, иконка таблицы на вкладке Ответы |
| 5 | https://repetitor.ua/ru/yak-stvoryty-google-formu-povnyj-gajd-2026-dlya-novachkiv-i-profi/ | Гайд 2026: forms.new, granular access |
| 6 | https://developers.google.com/apps-script/guides/triggers/installable | `onFormSubmit` installable trigger |

### Secondary: «автоматизация финотдела 2026 заявки расход»

| # | URL | Тип | Пробел |
| --- | --- | --- | --- |
| 1 | https://integration-software.ru/blog/obzor-funktsionala-kaznacheystvo-v-1s-erp-upravlenie-predpriyatiem | 1С ERP казначейство | Конtrast: когда уходить с Forms |
| 2 | https://firstbit.finance/tpost/ddfpyyug51-zayavka-na-rashod-deneg-kak-sdelat-tak-c | БИТ.Финанс | «Заявка на расход ДС» в 1С — не наш продукт |
| 3 | https://mayai.ru/google-forms-make-zayavki/ | Make + Forms | Уведомления, не фин-реестр |
| 4 | https://www.fl.ru/user/dmshumski/portfolio/8062505/ | кейс n8n | Forms→Sheets→CRM, метрики пилота |
| 5 | https://datalopata.ru/blog/avtomatizatsija-finansov-sistemnyj-podhod-k-uchetu-v-2026-godu/ | обзор 2026 | Макро, без Forms (цифры не брать без верификации) |

### Конкурентный зазор

1. **Sheets-first реестр заявок на расход** с колонками согласования — не бланк «заявка на кассовый расход».
2. **Явное разведение:** управленческая заявка (Forms) vs «Заявка на расход ДС» (1С) vs кассовый расход (РКО).
3. **Безопасность облака** — минимизация ПДн, доменный доступ (interlink B11-паттерн).
4. **Три уровня автоматизации:** встроенные email → Apps Script → Make/n8n.
5. **RU контекст финотдела** — статьи расходов, центры затрат, привязка к договору (interlink B51).

**Cannibalization:** B51 (реестр договоров), B22 (Apps Script), `/avtomatizaciya-finansov-no-code/` — перелинковка, не копировать H2 1:1.

---

## Таблица фактов

| # | Утверждение | Источник | Дата проверки |
| --- | --- | --- | --- |
| 1 | Google Forms создаётся на `forms.google.com` или через «Пустая форма»; быстрый URL — `forms.new`. | https://support.google.com/docs/answer/6281888?hl=ru ; https://repetitor.ua/ru/yak-stvoryty-google-formu-povnyj-gajd-2026-dlya-novachkiv-i-profi/ | 2026-08-15 |
| 2 | Ответы формы можно сохранять в Google Таблицы; данные добавляются **в режиме реального времени**. | https://support.google.com/a/users/answer/13046755?hl=ru | 2026-08-15 |
| 3 | Связь формы с таблицей: вкладка «Ответы» → «Установить связь с Таблицами» (или значок таблицы). | https://support.google.com/docs/answer/139706?hl=ru ; https://support.google.com/docs/answer/2917686?hl=en | 2026-08-15 |
| 4 | Можно создать форму из Google Sheets: «Инструменты» → «Создать форму» — ответы попадают на новый лист той же таблицы. | https://support.google.com/docs/answer/6281888?hl=ru ; https://timeweb.com/ru/community/articles/sozdanie-google-formy-s-vyvodom-v-google-tablicy | 2026-08-15 |
| 5 | При **>100 000** ответов синхронизация с Таблицами **может прекратиться**; при **>50 000** — сводка ответов может не отображаться. | https://support.google.com/docs/answer/139706?hl=ru | 2026-08-15 |
| 6 | При **>10 000** ответов возможны сбои сортировки в CSV и отображения отдельных вопросов. | https://support.google.com/docs/answer/139706?hl=ru | 2026-08-15 |
| 7 | В Forms можно включить «Получать уведомления о новых ответах по эл. почте» на вкладке «Ответы». | https://support.google.com/docs/answer/139706?hl=ru | 2026-08-15 |
| 8 | Installable-триггер **`onFormSubmit`** на таблице срабатывает при отправке формы, связанной с этой таблицей; простой `onEdit` при добавлении строки формой **не** срабатывает. | https://developers.google.com/apps-script/guides/triggers/installable ; https://stackoverflow.com/questions/70213466/how-to-trigger-a-conditional-email-when-a-new-google-sheet-row-is-added-via-google-forms | 2026-08-15 |
| 9 | Программная установка триггера: `ScriptApp.newTrigger('fn').forSpreadsheet(sheet).onFormSubmit().create()`. | https://developers.google.com/apps-script/reference/script/spreadsheet-trigger-builder | 2026-08-15 |
| 10 | Google Workspace: файлы Forms и загрузки на Drive **шифруются при передаче и хранении**. | https://workspace.google.com/intl/ru/products/forms/ | 2026-08-15 |
| 11 | Типовые поля формы возмещения/расхода: ФИО, отдел, дата, категория, сумма, описание, загрузка чека, подтверждение политики. | https://joliform.com/blog/google-forms-expense-reimbursement-template ; https://ru.surveymonkey.com/templates/reimbursement-form-template/ | 2026-08-15 |
| 12 | В связанной таблице финкоманда добавляет **вручную** служебные колонки: approved amount, review date, payment status, комментарий реviewer. | https://joliform.com/blog/google-forms-expense-reimbursement-template ; https://www.signnow.com/features/google-forms-expense-reimbursement | 2026-08-15 |
| 13 | «Заявка на **кассовый расход**» в подборках Consultant+/Assistentus — документ для **наличных из кассы** / РКО, **не** автоматизация Google Forms. | https://www.consultant.ru/law/podborki/poryadok_zapolneniya_zayavki_na_kassovyj_rashod/ ; https://assistentus.ru/forma/zayavka/ | 2026-08-15 |
| 14 | В 1С:ERP «Заявка на расходование ДС» проходит проверку лимитов, маршрут согласования и превращается в платёжное поручение — **другой класс системы**, чем Forms+Sheets. | https://integration-software.ru/blog/obzor-funktsionala-kaznacheystvo-v-1s-erp-upravlenie-predpriyatiem | 2026-08-15 |
| 15 | БИТ.Финанс: документ «Заявка на расходование денежных средств» — центральный узел бюджетного контроля и согласований в 1С-контуре. | https://firstbit.finance/tpost/ddfpyyug51-zayavka-na-rashod-deneg-kak-sdelat-tak-c | 2026-08-15 |
| 16 | Make: модуль Google Forms «Watch Responses» на Free проверяет форму **раз в 15 минут**; альтернатива — webhook через Apps Script. | https://mayai.ru/google-forms-make-zayavki/ | 2026-08-15 |
| 17 | Кейс автоматизации: ручной перенос заявки Forms→CRM занимал **5–10 минут**; цепочка Forms→Sheets→n8n→CRM сняла ручной ввод (портфолио FL.ru). | https://www.fl.ru/user/dmshumski/portfolio/8062505/ | 2026-08-15 |
| 18 | Паттерн expense tracker: каждая отправка формы = строка в Sheets; далее `SUMIF`/сводные по категориям и периодам. | https://101-help.com/kak-ispolzovat-google-forms-v-kachestve-schetchika-raskhodov-1c3ff195d9/ | 2026-08-15 |
| 19 | Связь формы с таблицей можно **разорвать** («Unlink form»); уже собранные данные в таблице сохраняются. | https://support.google.com/docs/answer/2917686?hl=en | 2026-08-15 |
| 20 | Официального шаблона Google «реестр заявок на расход в Sheets» **не существует** — структуру проектирует финотдел (SERP + синтез WebSearch 2026-08-15). | https://workspace.google.com/intl/ru/products/forms/ ; анализ SERP | 2026-08-15 |

**Не выдумывать:** точные показы Wordstat; «экономия X часов/день» без замера; что Forms заменяет 1С/БИТ.Финанс; что управленческая заявка = «заявка на кассовый расход» по НПА.

**fact-bank.md:** прямых строк про Google Forms / заявки на расход нет — цифры и лимиты только из таблицы выше (п. 5–6, 16–17).

---

## Структура H2 для writer (из карточки B59)

1. Когда это нужно финотделу (и когда нет)  
2. Подготовка данных и безопасность (без сырых ПДн в облако)  
3. Пошаговая настройка формы, реестра и уведомлений  
4. Проверка результата и типичные ошибки  
5. Что автоматизировать дальше  

**Workflow-схема для статьи:**  
`Инициатор заполняет Form → строка в реестре Sheets → email/скрипт согласующему → status approved → оплата → payment_date → еженедельная сверка с выпиской`

---

## FAQ-кандидаты (из карточки)

- Можно ли без программиста? (да: форма + связь + служебные колонки + email; скрипт — опционально по B22)
- Сколько займёт внедрение? (2–4 ч MVP; +0.5–1 день при Make/n8n)
- Какие риски для данных в Google Sheets?
- Чем это отличается от «заявки на кассовый расход» и от 1С?
- Нужно ли собирать чеки в форме?
- Когда пора уходить в ERP/казначейство?

---

## CTA / interlink

- Internal: `/avtomatizaciya-finansov-no-code/`, `/obezlichivanie-dannyh-chatgpt-finansist/`, `/reestr-dogovorov-google-sheets/`, `/google-apps-script-finansist-obnovit-dannye/`
- CTA: club.koda-fd.ru (utm_campaign=zayavka-na-rashod-google-forms), t.me/finance_modern
- **Запрет:** salebot

---

## Handoff marker

`=== EXCALIBUR BLOG RESEARCH ===` — см. `.cursor/excalibur-blog-handoff.md`
