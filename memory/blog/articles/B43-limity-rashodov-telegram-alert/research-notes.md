# Research notes — B43

**topic_id:** B43  
**slug:** limity-rashodov-telegram-alert  
**h1:** Как контролировать лимиты статей расходов и слать алерт в Telegram  
**research_date:** 2026-08-04  
**publish_target:** koda-fd.ru/blog  
**utility_gate:** PASS (`workflow`, mode B) — подтверждено `python3 scripts/excalibur_blog_utility_gate.py --topic-id B43` и `utility-gate-topic.json`  
**related_published:** `/avtomatizaciya-finansov-no-code/`, `/obezlichivanie-dannyh-chatgpt-finansist/`, `/daydzhest-sobstvenniku-n8n-telegram/`, `/platezhnyj-kalendar-google-sheets-n8n/`, `/bankovskaya-vypiska-staging-google-sheets/`, `/spravochnik-kategorij-dds/`  
**internal_links (карточка):** `/avtomatizaciya-finansov-no-code/`, `/obezlichivanie-dannyh-chatgpt-finansist/`  
**cover_scene_hint:** abstract holographic finance automation dark #0a0a0f purple #8b5cf6, no text

---

## utility_verdict

**PASS** — тема utility-only workflow. Читатель собирает реестр лимитов по статьям расходов, считает факт/usage%, вешает порог (обычно 80%), гоняет сценарий n8n/Make по расписанию и получает Telegram-алерт CFO/владельцу статьи с антиспамом. Не новость про лимиты мессенджера Telegram, не personal expense-бот, не ERP-внедрение.

---

## reader_outcome

После гайда финансист без разработчиков сможет завести лист `expense_limits` в Google Sheets (план, факт, порог, owner, last_alert), наполнить факт из выписки/1С без сырых ПДн, собрать в n8n цепочку Schedule → Sheets → IF порога → Telegram Send Message → Update last_alert и проверить, что алерт приходит один раз при пересечении порога, а не на каждую транзакцию.

---

## action_outline

1. **Когда нужно / когда нет** — нужно при 10+ статьях, нескольких инициаторах трат и отсутствии единого дашборда; не нужно при жёстком блоке заявок в 1С/ERP или при 3 стабильных лимитах (хватит условного форматирования раз в неделю).
2. **Реестр лимитов** — лист `expense_limits`: `article_code`, `article_name`, `period` (YYYY-MM), `limit_amount`, `fact_amount`, `usage_pct` (=fact/limit), `threshold_pct` (0.8), `owner`, `last_alert`. Старт с 5–7 «горячих» статей, не со всего P&L на 80 строк.
3. **Факт без ПДн** — лист `raw_expense` только код статьи + сумма + дата (агрегат); источник — банк/категории, выгрузка 1С или заявки. Не класть ФИО, ИНН, номера карт, полные выписки в облако; токены только в credentials n8n. См. `/obezlichivanie-dannyh-chatgpt-finansist/`.
4. **Бот Telegram** — @BotFather → `/newbot` → Access Token в credentials n8n; бот в чат финотдела/личку CFO; `chat_id` через getUpdates или Telegram Trigger.
5. **Сценарий n8n (или Make)** — Schedule (ежедневно 09:00) → Google Sheets Get rows → IF `usage_pct >= threshold_pct` AND (`last_alert` пуст OR прошло N дней) → Telegram Send Message → Sheets Update `last_alert = сегодня`.
6. **Текст алерта** — короткий: статья, период, факт/лимит, %, owner, действие («согласовать доп. бюджет или стоп»). Без контрагентов и реквизитов. Лимит текста Bot API: 1–4096 символов.
7. **Пороги и эскалация** — 80% предупреждение владельцу статьи; 100% «лимит исчерпан»; опционально 110% — второй чат/собственник. Не алертить каждую мелкую проводку.
8. **Проверка недели 1** — вручную поднять `fact_amount` выше порога на тестовой статье → убедиться, что пришло 1 сообщение и `last_alert` записался; повторить на следующий день — спама нет; сверить SUMIFS факта с источником.
9. **Дальше** — второй порог/эскалация; связка с платёжным календарём (B24) и справочником ДДС (B29); weekly digest собственнику (B27) как сводка, не замена порогового алерта.

**Схема:** Выписка/1С → `raw_expense` → формулы fact + usage_pct → n8n Schedule → фильтр порога → Telegram → запись `last_alert` → разбор перерасходов

---

## Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT AUTH WARNING:** сервер MCP `user-mcp-kv` в этой Cloud-сессии **не подключён** (доступны только `Cursor Automation Tools`, `cursor-cloud`). Вызов `wordstat_get_top_requests` **не выполнен**. Точные показы/мес **не получены** и **не выдуманы**.

Обновление токена: https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

**Экспертная семантика (LSI для writer, без цифр спроса):**

| Кластер | Фразы |
| --- | --- |
| Ядро | лимиты расходов telegram алерт, контроль лимитов статей расходов, уведомление о перерасходе бюджета telegram |
| Workflow | google sheets лимиты бюджета, n8n telegram алерт расходы, make.com бюджет уведомление |
| Финконтур | план факт расходы статьи, порог 80% бюджета, реестр лимитов финотдел |
| Автоматизация | автоматизация финотдела, контроль бюджета без erp, алерт cfo telegram |
| Безопасность | обезличивание выписки, без пдн в n8n, токен бота credentials |
| Смежное (не каннибалить) | дайджест собственнику telegram, платёжный календарь n8n, справочник категорий ддс |

**SEO-вывод:** сырой `research-serp.json` (DuckDuckGo) **засорён** запросами про лимиты мессенджера Telegram (рассылки, инвайты, Ads). Игнорировать. Реальный конкурентный SERP (WebSearch Cursor) — personal expense-боты, n8n invoice+budget templates (EN), AI-CFO обзоры, рекламные алерты Google Ads→Telegram. **Угол КОДА:** управленческий контроль статей расходов МСБ/финотдела на Google Sheets + n8n/Make + антиспам `last_alert`, без ERP и без personal finance UX.

---

## SERP (WebSearch Cursor, 04.08.2026)

| # | URL | Тип | Пробел / угол КОДА |
| --- | --- | --- | --- |
| 1 | https://n8n.io/workflows/13115-track-invoice-spending-vs-budget-from-google-drive-with-gpt-4o-and-telegram-alerts | n8n template EN | Порог 80%, Telegram budget status — взять паттерн; убрать OCR/OpenRouter/Drive как обязательный стек; фокус на реестре статей РФ-финотдела |
| 2 | https://axdigital.ru/blog/ai-finansovyj-direktor-unit-ekonomika-byudzhet/ | AI-CFO обзор | Алерт перерасхода + n8n+Sheets — широкий «AI-CFO»; мы даём узкий workflow за 1 день без Claude в контуре |
| 3 | https://flow-masters.ru/blog/financial-bot-expenses/ | продукт-бот | Учёт расходов + кассовый прогноз в боте; не how-to собрать самому на Sheets |
| 4 | https://linero.store/ai-expense-management-automation/ | n8n+AI expenses | Согласование крупных трат; слабый акцент на месячных лимитах статей |
| 5 | https://ezgpt.ru/articles/kak-sdelat-ii-agenta-dlya-zakupok-i-snabzheniya | procurement agent | `budget_limits` + approval — смежный паттерн; не дублировать закупки |
| 6 | https://netpeak.net/ru/blog/kak-ot-slezhivat-ostatok-byudzheta-v-google-ads-skript-dlya-opoveshcheniy-v-telegram/ | Ads→Telegram | Только рекламный кабинет; наш кейс — любые статьи ДДС/P&L |
| 7 | https://docs.n8n.io/integrations/builtin/credentials/telegram/ | оф. docs | BotFather `/newbot`, Access Token в credentials — канон шага 4 |
| 8 | https://core.telegram.org/bots/api#sendmessage | оф. API | sendMessage, chat_id, text 1–4096 — факты для алерта |
| 9 | https://developers.google.com/workspace/sheets/api/limits | оф. quotas | 300 read/write per project/min, 60 per user/min — не опрашивать Sheets каждую минуту |
| 10 | https://koda-fd.ru/blog/avtomatizaciya-finansov-no-code/ | свой блог | internal CTA / контекст no-code |
| 11 | https://koda-fd.ru/blog/daydzhest-sobstvenniku-n8n-telegram/ | свой блог | дайджест ≠ пороговый алерт — различать в тексте |
| 12 | https://n8n.io/workflows/13667-track-telegram-expenses-with-gpt-4-and-google-sheets-self-learning-categories/ | personal tracker | Ввод расходов из чата — **не** наш intent; упомянуть как антипаттерн для финотдела |

**Заметка про research-serp.json:** результаты primary/H1 уводят в «лимиты Telegram 2026» (gopulsar, gramgpt, sostav). Writer **не** опирается на эти URL. Использовать SERP-таблицу выше.

**Cannibalization:**  
- B27 дайджест собственнику — периодическая сводка, не порог по статье.  
- B24 платёжный календарь — платежи/календарь, не лимиты статей.  
- B25 staging выписки — источник факта, не алерт.  
- B29 справочник ДДС — коды статей для реестра.  
- B36/B28 — выписка/сверка.  
Перелинковка, H2 не копировать 1:1.

---

## Таблица фактов

| # | Утверждение | Источник | Дата проверки |
| --- | --- | --- | --- |
| 1 | Создание бота: чат с @BotFather → команда `/newbot` → имя и username (username 5–32 символа, латиница/цифры/`_`, оканчивается на `bot`) → BotFather выдаёт Access Token. | https://docs.n8n.io/integrations/builtin/credentials/telegram/ · https://core.telegram.org/bots/features#creating-a-new-bot | 2026-08-04 |
| 2 | n8n Telegram credentials принимают API bot access token; токен вставляется в поле Access Token credential, не в ячейки Sheets. | https://docs.n8n.io/integrations/builtin/credentials/telegram/ | 2026-08-04 |
| 3 | Метод Bot API `sendMessage`: обязательны `chat_id` и `text`; `text` — 1–4096 символов после разбора entities. | https://core.telegram.org/bots/api#sendmessage | 2026-08-04 |
| 4 | Базовый URL запросов Bot API: `https://api.telegram.org/bot<token>/METHOD_NAME` (HTTPS). | https://core.telegram.org/bots/api/ | 2026-08-04 |
| 5 | n8n Telegram node operation Send Message использует Bot API sendMessage; Chat ID — числовой id или `@channelusername`; текст max 4096. | https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.telegram/message-operations/ | 2026-08-04 |
| 6 | Google Sheets API: read requests 300/min per project и 60/min per user per project; write — те же лимиты; при превышении HTTP 429; дневного лимита запросов нет при соблюдении per-minute. | https://developers.google.com/workspace/sheets/api/limits | 2026-08-04 |
| 7 | Рекомендуемый max payload Sheets API ~2 MB; при 429 — exponential backoff. | https://developers.google.com/workspace/sheets/api/limits | 2026-08-04 |
| 8 | Шаблон n8n «Invoice Budget Tracker»: алерт при spending ≥ 80% бюджета категории; управление бюджетом через Telegram; дедуп SHA256; weekly/monthly reports. | https://n8n.io/workflows/13115-track-invoice-spending-vs-budget-from-google-drive-with-gpt-4o-and-telegram-alerts | 2026-08-04 |
| 9 | В том же шаблоне `alert_threshold` по умолчанию `0.8`; алерт только если бюджет категории задан. | https://n8n.io/workflows/13115-track-invoice-spending-vs-budget-from-google-drive-with-gpt-4o-and-telegram-alerts | 2026-08-04 |
| 10 | Паттерн AI-CFO: n8n + Google Sheets (выписки) + алерт в Telegram/Slack при близком перерасходе; вариант «n8n + Claude + Telegram» оценивают как настройку за 1–2 часа (маркетинговая оценка автора, не гарантия). | https://axdigital.ru/blog/ai-finansovyj-direktor-unit-ekonomika-byudzhet/ | 2026-08-04 |
| 11 | В закупках/снабжении лимиты хранят в таблице `budget_limits`; заявка сравнивается с `available_amount` и `budget_overrun_pct` перед approval. | https://ezgpt.ru/articles/kak-sdelat-ii-agenta-dlya-zakupok-i-snabzheniya | 2026-08-04 |
| 12 | Для MVP контроля оплат/лимитов достаточно Google Sheets + n8n Cloud или self-hosted; запись в учётные системы — после стабилизации процесса. | https://ezgpt.ru/articles/kak-sdelat-ii-agenta-dlya-kontrolya-oplat-i-debitorki | 2026-08-04 |
| 13 | Практический антипаттерн внедрения ботов: перфекционизм; старт с минимальной конфигурацией за 1 день, доработка по ходу (месяц 2 — прогноз/бюджетирование). | https://flow-masters.ru/blog/financial-bot-expenses/ | 2026-08-04 |
| 14 | Google Ads→Telegram скрипты показывают паттерн TOKEN + CHAT_ID + расписание (daily/weekly/monthly) для остатка бюджета — переносимо на Sheets-реестр статей. | https://netpeak.net/ru/blog/kak-ot-slezhivat-ostatok-byudzheta-v-google-ads-skript-dlya-opoveshcheniy-v-telegram/ | 2026-08-04 |
| 15 | Updates через getUpdates хранятся не дольше 24 часов; webhook и getUpdates взаимоисключающи. | https://core.telegram.org/bots/api/ | 2026-08-04 |
| 16 | По умолчанию боты могут broadcast до 30 сообщений/сек (для нашего сценария 1–N алертов/день лимит несущественен). | https://core.telegram.org/bots/api/ | 2026-08-04 |

**Fact-bank:** в `memory/brief/fact-bank.md` нет строк именно про лимиты расходов/Telegram-алерты (записи про контент-заводы/Make). В статью B43 цифры только из таблицы выше + здравый смысл без выдуманной статистики «% компаний». Маркетинговые цифры axdigital (73% стартапов, зарплаты CFO) — **не использовать** без отдельной верификации первички АКАР.

---

## FAQ hints (кандидаты)

1. **Можно ли без программиста?** — Да: Google Sheets + n8n/Make по шагам; код не обязателен. Apps Script — альтернатива без n8n, если всё уже в одном Google-аккаунте.
2. **Сколько займёт внедрение?** — Реестр + бот + один сценарий: один рабочий день на 5–7 статей; подключение факта из банка/1С — ещё 1–3 дня в зависимости от источника.
3. **Какие риски для данных?** — Токен бота и OAuth Google только в credentials; в облако — агрегаты без ПДн; self-hosted n8n если политика запрещает SaaS. См. `/obezlichivanie-dannyh-chatgpt-finansist/`.
4. **Порог 80% или 100%?** — 80% для раннего стопа/перераспределения; 100% — «стоп»; два порога лучше одного «поздно».
5. **Почему не алерт на каждую транзакцию?** — Шум убивает реакцию; алерт по агрегату статьи за период + `last_alert`.
6. **Чем отличается от дайджеста собственнику?** — Дайджест (B27) — регулярная сводка; эта статья — событие при пересечении порога по статье.
7. **Нужен ли ERP?** — Нет для MVP; ERP имеет смысл, если уже есть жёсткий блок заявок — тогда алерт можно повесить там, а не в Sheets.
8. **Make вместо n8n?** — Да, та же логика Schedule → Sheets → Filter → Telegram → Update; выбирать по уже используемому стеку (`/avtomatizaciya-finansov-no-code/`).

---

## Writer notes

- **author_id:** olga-kondratskaya  
- **article_mode:** B — workflow: 5–9 нумерованных шагов + таблица колонок реестра + схема `→`.  
- **Не путать intent:** заголовок «лимиты… Telegram» в выдаче = лимиты мессенджера; в лиде явно: *статьи расходов / бюджет*, не API Telegram.  
- **CTA (conversion-map):** клуб KODA ≤2, Telegram ≤2, koda-fd.ru ≤1; UTM `?utm_source=blog&utm_medium=article&utm_campaign=limity-rashodov-telegram-alert`  
- **Не обещать:** блок оплаты в банке, 100% защиту от перерасхода, автосогласование в 1С, цены клуба.  
- **H2 из карточки** заменить на блоки action_outline (when / data / setup / verify / next).  
- **Запрет редактуры:** эмодзи в тексте статьи; длинное тире «—» → «–» или «-».  
- **В папке уже есть** `article.html` / `article.meta.json` от прошлого прогона (2026-08-03, GEO QA PASS в meta) — writer/QA решают переписать или обновить; research зафиксирован на 2026-08-04. Research **не** правит article.html.

---

## Блокеры

Нет. `utility_verdict: PASS`. Wordstat недоступен — зафиксирован warning, цифры спроса не выдуманы.
