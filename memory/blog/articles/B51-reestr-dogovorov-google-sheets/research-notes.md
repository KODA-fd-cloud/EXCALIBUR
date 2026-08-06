# Research notes — B51

**topic_id:** B51  
**slug:** reestr-dogovorov-google-sheets  
**h1:** Как вести реестр договоров и сроков оплаты в Google Sheets с напоминаниями  
**research_date:** 2026-08-06  
**publish_target:** сайт koda-fd.ru/blog (+ Дзен по оркестрации)  
**utility_gate:** PASS (`workflow`, mode B)  
**author_id:** olga-kondratskaya  
**related_internal:** /avtomatizaciya-finansov-no-code/, /obezlichivanie-dannyh-chatgpt-finansist/

---

## utility_verdict

**PASS** — тема utility-only workflow. Читатель получает: структуру реестра договоров и графика оплат в Google Sheets, визуальный контроль сроков (условное форматирование), автоматические email-напоминания через Apps Script или условные уведомления Workspace, регламент обновления и проверку без сырых ПДн в облаке. Не «образец Excel», не новость про автоматизацию финотдела.

---

## reader_outcome

После гайда финансист или офис-менеджер сможет собрать в Google Sheets реестр договоров с колонками сроков оплаты и пролонгации, настроить подсветку «просрочено / скоро дедлайн», подключить ежедневные email-напоминания ответственным (Apps Script + time-driven trigger) и описать регламент: кто вносит договор в день подписания и как проверять горизонт 30–45 дней.

---

## action_outline

1. **Проверить, подходит ли Google Sheets** — до ~200–300 договоров при нормированных списках; один владелец реестра; если нужен аудит изменений и жёсткий ACL — рассмотреть 1С/CLM позже.
2. **Создать лист «Реестр»** — обязательные колонки: №, номер/дата договора, контрагент (без лишних ПДн), ИНН, предмет, сумма, дата начала/окончания, пролонгация + срок отказа, ответственный (email), статус, ссылка на скан.
3. **Добавить лист «График оплат»** — строки: договор, дата платежа, сумма, тип (аванс/этап), статус оплаты; связка по внутреннему № договора.
4. **Настроить нормирование** — выпадающие списки статусов, проверка дат, формулы «дней до окончания» (`=DATEDIF(TODAY(), J2, "D")` / `=J2-TODAY()`), защита заголовков и формул.
5. **Включить условное форматирование** — красный: дата окончания < сегодня; жёлтый: ≤30 дней; отдельно — дедлайн уведомления об отказе от пролонгации (дата окончания − N дней).
6. **Выбрать канал напоминаний** — (A) **Условные уведомления** Google Workspace при смене статуса ячейки; (B) **Apps Script + MailApp** для ежедневной проверки дат оплаты/окончания и письма ответственному.
7. **Написать и задеплоить скрипт** — Extensions → Apps Script; цикл по строкам; `today.setHours(0,0,0,0)` для сравнения дат; `MailApp.sendEmail`; триггер Time-driven → Day timer.
8. **Проверить результат** — тестовая строка с датой «завтра»; Executions log; `MailApp.getRemainingDailyQuota()`; чеклист типичных ошибок (текст вместо даты, неверное имя листа, дубли напоминаний).
9. **Закрепить регламент и следующий шаг** — владелец реестра; внесение в день подписания; еженедельный просмотр 30–45 дней; дальше — n8n/Telegram или выгрузка из 1С (без обязательного программиста на MVP).

---

## Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT AUTH WARNING:** сервер MCP `user-mcp-kv` в этой Cloud-сессии **не подключён** (доступен только `cursor-cloud`). Вызов `wordstat_get_top_requests` **не выполнен**. Точные показы/мес **не получены** и **не выдуманы**. Обновите токен / подключите MCP-KV: https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

**Экспертная семантика (без цифр спроса):**

| Кластер | Фразы | Роль |
| --- | --- | --- |
| Primary | реестр договоров google sheets, реестр договоров google таблицы | H1, title |
| Payments | сроки оплаты по договору, график платежей договор, напоминание об оплате | H2 график оплат |
| Reminders | напоминания google sheets, apps script напоминание email, условные уведомления google таблицы | H2 автоматизация |
| Workflow | как вести реестр договоров, контроль сроков договора, автопродление договор | H2 регламент |
| Secondary | автоматизация финотдела, автоматизация google таблиц без программиста | CTA / interlink |
| Security | реестр договоров без персональных данных, обезличивание данных финансы | FAQ, блок безопасности |

**SEO-вывод:** SERP по `реестр договоров google sheets` перекошен в **Excel-шаблоны и скачивание бланков**; мало пошаговых материалов именно про **Google Sheets + напоминания по срокам оплаты и пролонгации**. Угол КОДА: **workflow в облачной таблице + Apps Script без CRM/1С на старте**, с блоком про ПДн и internal link на обезличивание.

---

## SERP (WebSearch Cursor, 06.08.2026)

### Primary: «реестр договоров google sheets напоминания 2026»

| # | URL | Тип | Пробел для КОДА |
| --- | --- | --- | --- |
| 1 | https://cloudwork.ru/hub/reestr-dogovorov-excel | Excel-гайд 2026, формулы, сроки хранения | Excel, не Sheets; нет email-триггеров |
| 2 | https://pactrum.ru/blog/kak-vesti-reestr-dogovorov | структура, регламент, ошибки | Общий реестр; без Sheets-автоматизации |
| 3 | https://petr-panda.ru/reestr-dogovorov-primery/ | форматы реестра | Упоминает Sheets; без скриптов |
| 4 | https://gistjunction.com/contract-renewal-tracker/ | EN: renewal tracker в Sheets | Другой язык; renewal, не оплаты RU |
| 5 | https://rutube.ru/video/74a0cec1117045cde1f900d1dc9ca39f/ | видео-шаблон Google таблица | Нет текстового workflow |
| 6 | https://support.google.com/docs/answer/14099459?hl=ru | условные уведомления | Только смена ячейки, не календарные даты |

### Secondary: «автоматизация финотдела google sheets»

| # | URL | Тип | Пробел |
| --- | --- | --- | --- |
| 1 | https://blog.albato.ru/google-tabliczy-dlya-biznesa-avtomatizacziya-bez-programmista/ | no-code сценарии Albato | Лиды/CRM, не реестр договоров |
| 2 | https://vc.ru/id705136/2817200-nalogovaya-reforma-2026-avtomatizatsiya-biznesa | макро-тренд 2026 | Нет инструкции |
| 3 | https://developers.google.com/apps-script/reference/mail/mail-app | MailApp API | EN-доки; нужен RU-контекст финотдела |

### H1-aligned: «Как вести реестр договоров и сроков оплаты в Google Sheets с напоминаниями»

| # | URL | Заметка |
| --- | --- | --- |
| 1 | https://frommanual.com/workflows/automatic-invoice-tracker-google-sheets/ | invoice tracker + sendReminders Apps Script |
| 2 | https://dev.to/bulldo_gs/send-email-reminders-based-on-dates-in-google-sheets-58gj | date reminders, setHours, daily trigger |
| 3 | https://neotechnavigators.com/contract-management-tracker-in-google-sheets/ | contract tracker + Apps Script reminders |

### Конкурентный зазор

1. **Sheets-first**, а не «скачайте Excel и импортируйте».
2. **Два контура сроков:** окончание договора / пролонгация **и** график оплат — в одном workflow.
3. **Три уровня автоматизации:** условное форматирование → условные уведомления (Workspace) → Apps Script по расписанию.
4. **Безопасность данных:** ИНН и деловые реквизиты — да; паспортные/лишние ПДн в облако — нет (interlink B11).
5. **Регламент владельца** — не только колонки, но кто обновляет и когда смотрит горизонт 30–45 дней.

---

## Таблица фактов

| # | Утверждение | Источник | Дата |
| --- | --- | --- | --- |
| 1 | Реестр договоров — одна строка на контракт: контрагент, предмет, сумма, сроки, ответственный, статус. | https://cloudwork.ru/hub/reestr-dogovorov-excel | 2026-08-06 |
| 2 | Минимальный «костяк» полей: внутренний №, тип, дата, контрагент, ИНН, сумма, даты начала/окончания, статус, ответственный, ссылка на скан, признак автопродления. | https://cloudwork.ru/hub/reestr-dogovorov-excel | 2026-08-06 |
| 3 | Условное форматирование «просрочено»: дата окончания < `TODAY()`; «≤30 дней»: между `TODAY()` и `TODAY()+30`. | https://cloudwork.ru/hub/reestr-dogovorov-excel | 2026-08-06 |
| 4 | Формула «дней до окончания»: `=DATEDIF(TODAY(), J2, "D")` или разность дат. | https://cloudwork.ru/hub/reestr-dogovorov-excel | 2026-08-06 |
| 5 | Договоры с контрагентами хранят **5 лет** после прекращения (ст. 29 ФЗ-402, ст. 23 НК РФ). | https://cloudwork.ru/hub/reestr-dogovorov-excel ; https://42clouds.com/ru-ru/faq/kakoj-srok-hraneniya-dogovorov-s-kontragentami/ | 2026-08-06 |
| 6 | Для обычных коммерческих договоров **обязательный** реестр по закону не требуется (в отличие от 44-ФЗ). | https://pactrum.ru/blog/kak-vesti-reestr-dogovorov | 2026-08-06 |
| 7 | Критичная колонка — **пролонгация и срок уведомления об отказе**; типовой горизонт контроля — **30–45 дней**. | https://pactrum.ru/blog/kak-vesti-reestr-dogovorov | 2026-08-06 |
| 8 | Правило: договор вносится **в день подписания**; допсоглашение обновляет сумму/срок **в тот же день**. | https://pactrum.ru/blog/kak-vesti-reestr-dogovorov | 2026-08-06 |
| 9 | Статусы — закрытый список («Действует», «Завершён», «Расторгнут», «На согласовании»); произвольный текст ломает фильтры. | https://pactrum.ru/blog/kak-vesti-reestr-dogovorov | 2026-08-06 |
| 10 | Реестр можно вести в Excel, Google Sheets или CLM; таблица требует ручного контроля сроков без скриптов/триггеров. | https://pactrum.ru/blog/kak-vesti-reestr-dogovorov ; https://petr-panda.ru/reestr-dogovorov-primery/ | 2026-08-06 |
| 11 | **Условные уведомления**: Инструменты → Условные уведомления; письмо при изменении ячейки; доступны не во всех аккаунтах. | https://support.google.com/docs/answer/14099459?hl=ru | 2026-08-06 |
| 12 | Условные уведомления **не срабатывают** на пересчёт `TODAY()` при закрытом файле — не заменяют календарные напоминания. | https://support.google.com/docs/answer/14099459?hl=ru | 2026-08-06 |
| 13 | `MailApp.sendEmail()` отправляет письма из Apps Script; квота считается **по числу получателей**, не сообщений. | https://developers.google.com/apps-script/reference/mail/mail-app | 2026-08-06 |
| 14 | Квота MailApp: **100** получателей/день (consumer Gmail), **1500** (Google Workspace); проверка — `MailApp.getRemainingDailyQuota()`. | https://developers.google.com/apps-script/guides/services/quotas | 2026-08-06 |
| 15 | Макс. runtime скрипта — **6 минут** на запуск; time-driven triggers: **90 мин/день** (consumer) / **6 ч/день** (Workspace). | https://developers.google.com/apps-script/guides/services/quotas | 2026-08-06 |
| 16 | Для сравнения дат в напоминаниях нужно `setHours(0,0,0,0)` на `today` и `dueDate`, иначе срабатывание «день в день» ломается. | https://dev.to/bulldo_gs/send-email-reminders-based-on-dates-in-google-sheets-58gj | 2026-08-06 |
| 17 | Паттерн invoice tracker: ежедневный trigger на `sendReminders()`, параметр «за N дней до срока» (`reminderDays = 3`). | https://frommanual.com/workflows/automatic-invoice-tracker-google-sheets/ | 2026-08-06 |
| 18 | No-code (Albato и др.): триггер «новая строка / изменение» → запись в Sheets; для реестра договоров — альтернатива скрипту. | https://blog.albato.ru/google-tabliczy-dlya-biznesa-avtomatizacziya-bez-programmista/ | 2026-08-06 |

**Не выдумывать:** точные показы Wordstat; «экономия X часов» без замера; обязательность реестра для всех юрлиц; лимиты Gmail UI = лимитам MailApp (см. примечание Google Workspace Help про Apps Script).

---

## Структура H2 для writer (из карточки B51)

1. Когда это нужно финотделу (и когда нет)  
2. Подготовка данных и безопасность (без сырых ПДн в облако)  
3. Пошаговая настройка таблицы, формул и Apps Script / сценария напоминаний  
4. Проверка результата и типичные ошибки  
5. Что автоматизировать дальше  

**Workflow-схема для статьи:**  
`Договор подписан → строка в реестре → график оплат → подсветка сроков → ежедневный скрипт → email ответственному → еженедельный обзор 30–45 дней`

---

## FAQ-кандидаты (из карточки)

- Можно ли без программиста? (да: CF + условные уведомления; скрипт — копипаст + Gemini)
- Сколько займёт внедрение? (2–4 ч на MVP таблицы + 1–2 ч на скрипт)
- Какие риски для данных в Google Sheets?
- Чем отличается дедлайн пролонгации от даты оплаты?
- Нужен ли Google Workspace для email-напоминаний?
- Когда пора уходить с Sheets на 1С/CLM?

---

## CTA / interlink

- Internal: `/avtomatizaciya-finansov-no-code/` (следующий уровень: n8n/Make), `/obezlichivanie-dannyh-chatgpt-finansist/` (ПДn в облаке)
- CTA: club.koda-fd.ru (utm_campaign=reestr-dogovorov-google-sheets), t.me/finance_modern
- **Запрет:** salebot

---

## Handoff marker

`=== EXCALIBUR BLOG RESEARCH ===` — см. `.cursor/excalibur-blog-handoff.md`
