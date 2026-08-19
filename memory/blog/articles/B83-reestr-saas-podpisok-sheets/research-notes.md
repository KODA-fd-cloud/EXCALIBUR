# Research notes — B83

**topic_id:** B83  
**slug:** reestr-saas-podpisok-sheets  
**h1:** Как вести реестр SaaS-подписок и не платить за мёртвые лицензии  
**research_date:** 2026-08-19  
**publish_target:** koda-fd.ru/blog  
**utility_gate:** PASS (`workflow`, mode B)  
**author_id:** olga-kondratskaya  
**related_internal:** /avtomatizaciya-finansov-no-code/, /obezlichivanie-dannyh-chatgpt-finansist/  
**cover_scene_hint:** abstract holographic finance automation dark #0a0a0f purple #8b5cf6, no text

---

## utility_verdict

**PASS** — тема utility-only workflow. Читатель получает: структуру реестра SaaS-подписок в Google Sheets, сбор данных из банковской выписки (без сырых ПДн), назначение владельцев и категорий, поиск дублей и «мёртвых» seats, подсветку дат продления, регламент квартальной сверки и алерты до автопродления. Не обзор «как оплатить SaaS из России», не рейтинг SMP без инструкции.

---

## reader_outcome

После гайда финансист или CFO сможет за один вечер собрать в Google Sheets реестр всех SaaS-подписок компании из выписки за 3 месяца, проставить владельцев и статусы (активна / на удаление / под замену), найти дубли и неиспользуемые лицензии, настроить условное форматирование и напоминания за 90–120 дней до продления и закрепить квартальную сверку с выпиской — без программиста на MVP.

---

## action_outline

1. **Проверить, подходит ли Google Sheets** — до ~15–30 активных подписок и одного владельца реестра; если сервисов 50+ и нужен SSO-инвентарь — позже SMP/FinOps-инструмент; если жёсткий ACL и аудит — 1С + реестр как зеркало.
2. **Подготовить данные безопасно** — выгрузка CSV/Excel по корпоративным счетам и картам; в таблицу: сервис, сумма, дата, ответственный (email/отдел), без паспортов и лишних ПДн; interlink `/obezlichivanie-dannyh-chatgpt-finansist/`.
3. **Создать лист «Реестр»** — колонки: сервис, категория, стоимость/мес, периодичность, дата следующего списания, кто платит, владелец бюджета, seats (куплено/активно), статус, ссылка на договор/инвойс.
4. **Заполнить из выписки за 3 месяца** — отфильтровать регулярные списания за ПО; добавить подписки с личных карт сотрудников (опрос руководителей); годовые суммы ÷ 12 для единой единицы.
5. **Назначить владельцев и найти дубли** — business owner + техконтакт на каждую строку; категории (CRM, дизайн, облако…) — пересечения = кандидаты на отмену; правило FinOps: без владельца — не автопродлевать.
6. **Пометить мёртвые лицензии** — seats > активных пользователей; «никто не вспомнил кто пользуется»; уволенный сотрудник; статус «на удаление» + дата решения до продления.
7. **Настроить контроль сроков** — формула «дней до продления»; условное форматирование: ≤30 / 31–60 / 61–90 дней; опционально Apps Script (паттерн B51) или календарь за 120 дней для корпоративных годовых.
8. **Проверить результат** — сверка суммы реестра с выпиской; тестовая строка с продлением «завтра»; чеклист: дубли категорий, seats без владельца, личные карты без маршрута возмещения.
9. **Закрепить регламент и следующий шаг** — один владелец реестра; обновление при новой подписке/увольнении; квартальная сверка с выпиской; дальше — n8n/Make, выписка B36, API B82 или автоматический разбор выписки.

---

## Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT AUTH WARNING:** сервер MCP `user-mcp-kv` в этой Cloud-сессии **не подключён** (доступен только `cursor-cloud`). Вызов `wordstat_get_top_requests` **не выполнен**. Точные показы/мес **не получены** и **не выдуманы**.

Обновление токена / подключение MCP: https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

### Таблица спроса (Wordstat)

| Фраза | Показы в месяц |
| --- | --- |
| реестр saas подписок компания | *не получено — MCP недоступен* |
| автоматизация финотдела | *не получено — MCP недоступен* |
| реестр saas подписок компания 2026 | *не получено — MCP недоступен* |
| учёт saas подписок google sheets | *не получено — MCP недоступен* |
| аудит saas подписок | *не получено — MCP недоступен* |

**Экспертная семантика (LSI для writer, без цифр спроса):**

| Кластер | Фразы | Роль |
| --- | --- | --- |
| Primary | реестр saas подписок компания, реестр подписок компании | H1, title |
| Sheets | реестр подписок google sheets, учёт saas google таблицы | H2 настройка |
| Finance | мёртвые лицензии saas, неиспользуемые seats, finops saas | H2 аудит |
| Source | учёт saas по выписке, найти все подписки компании | H2 сбор данных |
| Workflow | автоматизация финотдела, контроль автопродления подписок | CTA / interlink |
| Security | реестр подписок без персональных данных, 152-фз saas | FAQ |

**SEO-вывод:** SERP по `реестр saas подписок компания` **перекошен в оплату зарубежного SaaS из России** (RBC, vc.ru) и **промо SMP** (Subsly). Мало материалов именно про **Google Sheets + выписка + владельцы + квартальный регламент** от лица финотдела. Угол КОДА: **workflow в Sheets без dev-команды**, с блоком ПДн и связкой с автоматизацией финконтура (n8n/Make).

---

## SERP (WebSearch Cursor, 19.08.2026)

### Primary: «реестр saas подписок компания 2026»

| # | URL | Тип | Пробел для КОДА |
| --- | --- | --- | --- |
| 1 | https://companies.rbc.ru/news/3k19caudNM/oplata-podpiski-na-saas-servisyi-iz-rossii-kakie-sposobyi-est-v-2026-godu/ | Оплата SaaS из РФ | Не реестр, не Sheets |
| 2 | https://subsly.org/blog/reestr-podpisok-kompanii-shablon/ | Excel-шаблон, колонки, выписка | Excel-centric; автоматизация = их продукт |
| 3 | https://hightime.media/raiting-saas-kompaniy/ | Рейтинг SaaS РФ | Маркетинг, не учёт |
| 4 | https://saasheriff.ru/blog/invoice-vypiska-nayti-vse-podpiski/ | Выписка + почта | Лендинг сервиса, нет Sheets |
| 5 | https://onreport.ru/articles/finops-dlya-saas-i-oblakov-kak-kontrolirovat-podpiski-limity-i-rashody-na-cifrovye-servisy/ | FinOps, владельцы, лимиты | Общий FinOps; мало пошагового Sheets |
| 6 | https://allcontract.ru/documents/contracts/dogovor-saas-podpiski | Образец договора | Юрдок, не реестр |

### Secondary: «автоматизация финотдела 2026»

| # | URL | Тип | Пробел |
| --- | --- | --- | --- |
| 1 | https://znaj.org/ru/6-luchshikh-reshenii-2026-goda-avtomatizacii-upravleniya-finansami/ | ERP/SAP обзор | Нет реестра подписок в Sheets |
| 2 | https://koda-fd.ru/blog/ai-dlya-finansista-2026/ | AI для финансиста | Смежный кластер, не SaaS-реестр |
| 3 | https://remont-netbook.ru/tendenczii-avtomatizaczii-finansovyh-operaczij-i-buhgalterii-v-2026-godu/ | Тренды 2026 | Классификация платежей — да; SaaS-реестр — нет |
| 4 | https://datalopata.ru/blog/avtomatizatsija-finansov-sistemnyj-podhod-k-uchetu-v-2026-godu/ | Системный учёт | Без Sheets-workflow |

### H1-aligned: «Как вести реестр SaaS-подписок и не платить за мёртвые лицензии 2026»

| # | URL | Заметка |
| --- | --- | --- |
| 1 | https://subsly.org/blog/audit-saas-podpisok-za-30-minut/ | Аудит за 30 мин, выписка 3 мес, дубли |
| 2 | https://www.kt-team.ru/blog/audit-saas-podpisok-kompanii | Реестр для CFO: 9 полей, решения до продления |
| 3 | https://beancount.io/ru/blog/2026/03/11/saas-subscription-management-small-business-guide | EN/RU: управление подписками SMB |
| 4 | https://termedora.com/blog/saas-renewal-tracking-spreadsheet-template | Google Sheets renewal tracker, CF 30/60/90 |
| 5 | https://duubesoft.com/articles/kak-proverit-skrytye-komissii/ | Сбор реестра: AP, SSO, expense, владельцы |
| 6 | https://github.com/KiTaUc/ledger-renewals | Open-source реестр продлений |

### Конкурентный зазор

1. **Sheets-first для финотдела** — не «скачайте Excel у вендора SMP» и не «как оплатить Notion».
2. **Единица учёта = аккаунт/рабочая область**, не только строка выписки (kt-team).
3. **Три слоя экономии:** мёртвые seats → дубли категорий → даунгрейд тарифа — с чеклистом статусов в таблице.
4. **FinOps-правила в регламенте:** владелец, лимит, алерт 90–120 дней, запрет автопродления без owner (onreport).
5. **Безопасность данных** — суммы и сервисы в облако; ПДн сотрудников минимум; 152-ФЗ в FAQ (saasheriff).
6. **Fork на автоматизацию** — Apps Script / n8n (B51, B36) vs SMP при >20 сервисах.

---

## Таблица фактов

| # | Утверждение | Источник | Дата |
| --- | --- | --- | --- |
| 1 | Реестр подписок — таблица всех платных сервисов: что, сколько, кто пользуется, когда продление; без него — дубли, автопродления, лицензии уволенных. | https://subsly.org/blog/reestr-podpisok-kompanii-shablon/ | 2026-08-19 |
| 2 | Норма для компании ~30 человек — **20–30** SaaS-подписок; пока сервисов 3–5, держат «в голове». | https://subsly.org/blog/reestr-podpisok-kompanii-shablon/ | 2026-08-19 |
| 3 | Базовые колонки реестра: сервис, категория, стоимость/мес (годовые ÷12), периодичность, дата списания, кто платит, ответственный, seats, статус. | https://subsly.org/blog/reestr-podpisok-kompanii-shablon/ | 2026-08-19 |
| 4 | Сбор данных: выписка **за 3 месяца** по всем счетам/картам → отбор регулярных списаний за ПО → дополнение подписок с личных карт. | https://subsly.org/blog/reestr-podpisok-kompanii-shablon/ ; https://subsly.org/blog/audit-saas-podpisok-za-30-minut/ | 2026-08-19 |
| 5 | На этапе первичного заполнения обычно находят **2–4** подписки на удаление и **1–2** дубля. | https://subsly.org/blog/reestr-podpisok-kompanii-shablon/ | 2026-08-19 |
| 6 | Реестр в Excel/Sheets устаревает за **1–2 месяца** без владельца и регламента; нужна **квартальная** сверка с выпиской. | https://subsly.org/blog/reestr-podpisok-kompanii-shablon/ | 2026-08-19 |
| 7 | Порог перехода от ручной таблицы: **15–20+** сервисов с частыми изменениями — смотреть автоматизацию разбора выписки. | https://subsly.org/blog/reestr-podpisok-kompanii-shablon/ | 2026-08-19 |
| 8 | Аудит SaaS за **30 минут** по выписке; для компаний до **100** человек; типовая экономия аудита **50–150 тыс. ₽/мес** (кейс вендора — использовать осторожно, как ориентир). | https://subsly.org/blog/audit-saas-podpisok-za-30-minut/ | 2026-08-19 |
| 9 | На команду 30–50 человек после фильтрации выписки — **20–40** уникальных подписок, суммарно **100–300 тыс. ₽/мес** (кейс Subsly). | https://subsly.org/blog/audit-saas-podpisok-za-30-minut/ | 2026-08-19 |
| 10 | **15–20%** подписок в среднем «на отмену» (неиспользуемые); экономия на дублях категорий **15–40 тыс. ₽/мес** (кейс Subsly). | https://subsly.org/blog/audit-saas-podpisok-za-30-minut/ | 2026-08-19 |
| 11 | Одна строка реестра = **отдельный аккаунт/рабочая область**; поля: владелец бюджета, seats, полная стоимость в ₽, решение и дедлайн **до** продления. | https://www.kt-team.ru/blog/audit-saas-podpisok-kompanii | 2026-08-19 |
| 12 | Бухгалтерская выгрузка отвечает «сколько заплатили»; для продления нужны аккаунт, пользователи, активность, документы (3 слоя). | https://www.kt-team.ru/blog/audit-saas-podpisok-kompanii | 2026-08-19 |
| 13 | Пять рисков портфеля: автопродление без решения, неиспользуемые места после увольнения, неподходящий тариф, личный платёж, непредсказуемая стоимость (валюта, usage). | https://www.kt-team.ru/blog/audit-saas-podpisok-kompanii | 2026-08-19 |
| 14 | FinOps для SaaS: у каждого сервиса — **владелец**, **лимит**, **алерт**, **маршрут согласования**; без владельца — не автопродлевать. | https://onreport.ru/articles/finops-dlya-saas-i-oblakov-kak-kontrolirovat-podpiski-limity-i-rashody-na-cifrovye-servisy/ | 2026-08-19 |
| 15 | Документы FinOps-контура: реестр сервисов, матрица владельцев, правила согласования, бюджет по ЦЗ, журнал продлений. | https://onreport.ru/articles/finops-dlya-saas-i-oblakov-kak-kontrolirovat-podpiski-limity-i-rashody-na-cifrovye-servisy/ | 2026-08-19 |
| 16 | Формула экономии для CFO: отключённые seats + разница тарифов + предотвращённый перерасход лимитов. | https://onreport.ru/articles/finops-dlya-saas-i-oblakov-kak-kontrolirovat-podpiski-limity-i-rashody-na-cifrovye-servisy/ | 2026-08-19 |
| 17 | Источники инвентаризации: банковская выписка (MCC, периодичность), корпоративная почта (Stripe/Paddle renewal), AP, SSO (duubesoft). | https://duubesoft.com/articles/kak-proverit-skrytye-komissii/ ; https://saasheriff.ru/blog/invoice-vypiska-nayti-vse-podpiski/ | 2026-08-19 |
| 18 | У каждой подписки — **business owner** и **техконтакт**; переговоры о тарифе за неделю до автопродления — слабая позиция; лучше **90–120 дней** (ormobil, duubesoft). | https://duubesoft.com/articles/kak-proverit-skrytye-komissii/ ; https://ormobil.com/articles/kak-nastroit-avtoprodlenie-podpiski/ | 2026-08-19 |
| 19 | Шаблон renewal tracker в Google Sheets: колонки vendor, annual cost, renewal date, days until renewal (auto), owner; CF: жёлтый 31–60 д, зелёный 61–90 д (Termedora). | https://termedora.com/blog/saas-renewal-tracking-spreadsheet-template | 2026-08-19 |
| 20 | Spreadsheet renewal tracker **не шлёт email сам** — нужен Zapier/Apps Script или ручной обзор (Termedora). | https://termedora.com/blog/saas-renewal-tracking-spreadsheet-template | 2026-08-19 |
| 21 | Zylo 2026 SMI: средняя организация использует **54%** лицензий; **46%** не используются; лучшие — **≥90%** utilization (междун. бенчмарк для мотивации аудита). | https://zylo.com/blog/how-much-wasted-on-saas-spend | 2026-08-19 |
| 22 | Vertice Q2 2026: **65%** лицензий unused или underutilized (<50% seats); «shelfware» **14%** (междун. бенчмарк). | https://www.vertice.one/insights/unused-saas-applications | 2026-08-19 |
| 23 | Обработка данных выписки/почты — с учётом **152-ФЗ**; доступы согласуются с ИБ (saasheriff). | https://saasheriff.ru/blog/invoice-vypiska-nayti-vse-podpiski/ | 2026-08-19 |
| 24 | В 2026 финотдел в приоритете автоматизирует **классификацию платежей**, сверки, управленческую отчётность, cash flow — реестр SaaS ложится в контур классификации (remont-netbook / znaj). | https://remont-netbook.ru/tendenczii-avtomatizaczii-finansovyh-operaczij-i-buhgalterii-v-2026-godu/ | 2026-08-19 |

**Не выдумывать:** показы Wordstat; точную «экономию X часов» без замера; что SMP обязателен для всех; суммы $19.8M как норму для SMB РФ (только enterprise Zylo); цены конкретных SaaS без актуального прайса.

---

## Структура H2 для writer (из карточки B83)

1. Когда это нужно финотделу (и когда нет)  
2. Подготовка данных и безопасность (без сырых ПДн в облако)  
3. Пошаговая настройка таблицы, формул и напоминаний о продлении  
4. Проверка результата и типичные ошибки  
5. Что автоматизировать дальше  

**Workflow-схема для статьи:**  
`Выписка 3 мес → фильтр SaaS → строки в Sheets → владелец + категория → дубли/seats → статус → подсветка продления → алерт за 120 д → квартальная сверка → n8n/SMP`

---

## FAQ-кандидаты (из карточки)

- Можно ли без программиста? — Да: таблица + CF; Apps Script — опционально по паттерну B51.
- Сколько займёт внедрение? — 2–4 ч первичный реестр; 1 ч регламент; квартальная сверка ~30 мин.
- Какие риски для данных в Google Sheets? — Минимизировать ПДн; доступ по ролям; JSON/ключи не в таблице.
- Чем реестр отличается от SMP (Subsly, Torii)? — Sheets = нулевой порог входа; SMP — при росте shadow IT.
- Как отличить «мёртвую» лицензию от сезонной? — Запросить у владельца; правило 30 дней неактивности как триггер проверки.
- Нужна ли выписка, если есть договоры? — Да: ловит shadow SaaS на картах и личных возмещениях.

---

## CTA / interlink

- Internal: `/avtomatizaciya-finansov-no-code/` (n8n/Make для выписки), `/obezlichivanie-dannyh-chatgpt-finansist/` (ПДн)
- Соседние темы: B36 (выписка в Sheets), B51 (реестр договоров + Apps Script), B82 (API для staging)
- CTA: club.koda-fd.ru (utm_campaign=reestr-saas-podpisok-sheets), t.me/finance_modern
- **Запрет:** salebot; не превращать статью в рейтинг посредников оплаты SaaS из РФ

---

## Handoff marker

`=== EXCALIBUR BLOG RESEARCH ===` — см. `.cursor/excalibur-blog-handoff.md`
