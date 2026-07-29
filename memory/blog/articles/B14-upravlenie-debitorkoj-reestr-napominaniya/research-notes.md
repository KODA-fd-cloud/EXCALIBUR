# Research notes — B14

**topic_id:** B14  
**slug:** upravlenie-debitorkoj-reestr-napominaniya  
**h1:** Как настроить управление дебиторкой: реестр просрочки + автоматические напоминания контрагентам  
**research_date:** 2026-07-22  
**publish_target:** сайт koda-fd.ru/blog (+ Дзен по оркестрации)  
**utility_gate:** PASS (`workflow`, mode B)  
**practice_source:** n8n/Sheets-паттерны КОДА; при необходимости срез контрагентов из 1С через OData (`D:\projects\1С\dds-sheets`)

---

## utility_verdict

**PASS** — тема utility-only workflow. Читатель получает: минимальный реестр просрочки в таблице, статусы без CRM, цепочку автонапоминаний Sheets/Excel → n8n → Telegram/email, шаблоны писем без давления и без юррисков, контроль эффекта (ответ / оплата / эскалация). Не новость, не «вообще про ДЗ».

---

## reader_outcome

После гайда финансист сможет завести реестр просроченной дебиторки в Google Sheets/Excel, повесить статусы и правила дней просрочки, собрать сценарий напоминаний в n8n и вести учёт касаний без обязательной CRM и без обязательной 1С на каждый шаг.

---

## action_outline

1. **Собрать минимальный реестр** — колонки: контрагент, счёт/основание, сумма, дата отгрузки, плановая оплата, дни просрочки, статус, ответственный, канал, дата последнего касания, результат.
2. **Задать статусы и правила** — `ok` / `due_soon` / `overdue_1` / `overdue_2` / `escalate` / `paid` / `dispute`; пороги дней без «героизма менеджера».
3. **Наполнить из источника** — выгрузка из 1С/банка/CRM или ручной ввод; staging-лист `raw_*`, формулы поверх.
4. **Собрать автонапоминания** — Google Sheets/Excel → n8n (или Make) → email/Telegram; триггер по статусу и дате.
5. **Написать шаблоны** — до срока / день X / +3 / +7; без угроз судом в первом касании; без ЭЦП на мягких напоминаниях.
6. **Логировать эффект** — кто ответил, кто оплатил, кого эскалировать; отдельная колонка «следующий шаг».
7. **Антиспам** — лимит касаний, пауза после ответа, исключение споров по качеству.
8. **Регламент эскалации** — на каком дне передача руководителю/юристу; фиксация переписки.
9. **Еженедельный разбор** — KPI: сумма overdue, % ответов, % оплат после касания.

---

## Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT AUTH WARNING:** сервер MCP `user-mcp-kv` в этой сессии **не подключён** (нет инструментов `wordstat_*`). Точные показы/мес **не получены** и **не выдуманы**. Авторизация: https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

**Экспертная семантика (без цифр спроса):**

| Кластер | Фразы | Роль |
| --- | --- | --- |
| Primary | как управлять дебиторской задолженностью | H1, лид |
| Control | контроль дебиторки, реестр просроченной дебиторки | H2 реестр |
| Reminders | напоминание об оплате контрагенту | H2 шаблоны + n8n |
| Workflow | автонапоминания, n8n дебиторка, google sheets дебиторка | H2 автоматизация |
| Boundary | без CRM, без 1С, эскалация дебиторки | FAQ |

**SEO-вывод:** SERP забит теорией ДЗ, Битрикс24 и страхованием. Угол КОДА – **реестр в таблице + n8n без обязательной CRM**, мягкие шаблоны и контроль эффекта.

---

## SERP (WebSearch Cursor, 22.07.2026)

| # | URL | Тип | Пробел для КОДА |
| --- | --- | --- | --- |
| 1 | https://1cfresh.info/blog/debitorka-2026-kak-vystroit-sistemu-kontrolya-s-uchetom-novykh-trebovaniy-minfina-i-minimizirovat-ri/ | контроль ДЗ 2026, реестр 1–2 числа, кураторы | Нет Sheets→n8n; акцент на приказ/Минфин |
| 2 | https://www.gersains.ru/blog/kak-upravlyat-debitorskoy-zadolzhennostyu-5-shagov-k-bezopasnym-sdelkam/ | 5 шагов, тайминг 3–5 / 1–7 / 7–30 | Страхование; мало no-code |
| 3 | https://b24.org.ru/debitorskaya-zadolzhennost-v-bitriks24-v-2025/ | Битрикс24 автоматизация | Продажа CRM; не «без CRM» |
| 4 | https://salemagazine.ru/upravlenie-assortimentom/rabota-s-debitorkoj-kak-myagko-i-effektivno-vozvrashhat-oplaty/ | мягкие касания, шаблоны | Близко по тону; нет n8n+Sheets |
| 5 | https://academy-of-capital.ru/blog/upravleniye-debitorskoy-zadolzhennostyu/ | теория процесса | Вода, мало workflow |
| 6 | https://secrets.tbank.ru/blogi-kompanij/rabota-s-debitorskoj-zadolzhennostyu-2026/ | МСБ 2026, 7 шагов | Макроцифры ДЗ – не копировать без осторожности |

### Конкурентный зазор

1. Реестр как staging-таблица финансиста, не модуль CRM.
2. Автоматизация через n8n/Make + Telegram/email.
3. Шаблоны без давления и без юррисков на ранних касаниях.
4. Честно: можно без 1С на старте; 1С/OData – источник наполнения, не обязательный движок.

---

## Таблица фактов

| # | Утверждение | Источник | Дата |
| --- | --- | --- | --- |
| 1 | Практика: реестр ДЗ формируют регулярно (часто 1–2 числа месяца) с полями контрагент, сумма, дата/основание, статус, ответственный. | https://1cfresh.info/blog/debitorka-2026-kak-vystroit-sistemu-kontrolya-s-uchetom-novykh-trebovaniy-minfina-i-minimizirovat-ri/ | 2026-07-22 |
| 2 | Типичный цикл касаний: напоминание за 3–5 дней до срока; 1–7 дней просрочки – переговоры; 7–30 – претензия; далее суд/эскалация. | https://www.gersains.ru/blog/kak-upravlyat-debitorskoy-zadolzhennostyu-5-shagov-k-bezopasnym-sdelkam/ | 2026-07-22 |
| 3 | Мягкий цикл: −2…−3 дня до срока + счёт; день просрочки письмо+звонок; +2 повтор; +7 график платежей. | https://salemagazine.ru/upravlenie-assortimentom/rabota-s-debitorkoj-kak-myagko-i-effektivno-vozvrashhat-oplaty/ | 2026-07-22 |
| 4 | CRM (Битрикс24 и др.) умеет триггеры email/задачи по просрочке – альтернатива, не обязательный минимум. | https://b24.org.ru/debitorskaya-zadolzhennost-v-bitriks24-v-2025/ | 2026-07-22 |
| 5 | Фиксация переписки нужна для претензионной работы и списания. | https://1cfresh.info/… ; https://salemagazine.ru/… | 2026-07-22 |
| 6 | n8n/Make = сценарий «супер-Excel»: ячейка/строка → письмо/Telegram без ручного копирования. | практика КОДА; /avtomatizaciya-finansov-no-code/ | 2026-07-22 |
| 7 | Наполнение реестра из 1С возможно через выгрузку/OData (см. B13), не обязательно для MVP. | `D:\projects\1С\dds-sheets`; B13 | 2026-07-22 |

**Не выдумывать:** точные % снижения ДЗ «после внедрения»; показы Wordstat; юридические гарантии взыскания.

---

## Структура H2 для writer

1. Минимальный реестр дебиторки: какие колонки обязательны  
2. Статусы и правила просрочки без CRM  
3. Автонапоминания: Google Sheets / Excel → n8n → Telegram/email  
4. Что писать контрагенту: шаблоны без давления и без юррисков  
5. Контроль эффекта: кто ответил, кто оплатил, что эскалировать  
+ Что дальше + FAQ

## FAQ-кандидаты

- Можно ли без 1С?
- Как не спамить клиентов?
- Сколько раз напоминать?
- Нужна ли ЭЦП на напоминаниях?
- Чем Sheets+n8n отличается от CRM?
- Когда звать юриста?

## CTA / interlink

- CTA: club.koda-fd.ru (utm_campaign=upravlenie-debitorkoj-reestr-napominaniya), t.me/finance_modern  
- **Запрет:** salebot  
- Internal: /avtomatizaciya-finansov-no-code/, /ot-excel-k-fin-konturu-30-dney/
