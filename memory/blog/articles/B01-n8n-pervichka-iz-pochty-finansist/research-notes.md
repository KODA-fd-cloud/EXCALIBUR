# Research notes — B01

**topic_id:** B01  
**slug:** n8n-pervichka-iz-pochty-finansist  
**h1:** n8n для финансиста: как собрать первичку из почты в реестр без ручного ввода  
**research_date:** 2026-06-17  
**publish_target:** Дзен `automation_koda` (не WP на первом этапе)  
**utility_gate:** PASS (`how_to`, mode B)

---

## utility_verdict

**PASS** — тема закрывает практический how-to: читатель собирает n8n-сценарий «Яндекс Почта → AI/OCR → Google Таблица-реестр → Telegram», без обзора новостей и без «вообще про n8n».

---

## reader_outcome

После гайда финансист или CFO без dev-команды развернёт n8n (предпочтительно self-hosted), подключит Яндекс Почту по IMAP, настроит извлечение полей счёта/УПД в JSON, заполнит реестр первички в Google Sheets и получит уведомление в Telegram для ручной сверки сумм перед проводкой.

---

## action_outline

1. **Выбрать хостинг n8n** — self-hosted Community (финданные на своём VPS) vs Cloud; зафиксировать бюджет на инфраструктуру и лимиты executions.
2. **Создать «входящий» ящик или папку** — отдельный адрес/папка только для счетов и актов от контрагентов.
3. **Подключить IMAP Trigger к Яндекс Почте** — включить IMAP, пароль приложения, `imap.yandex.ru:993`, SSL.
4. **Отфильтровать мусор** — IF/AI-guardrail: только письма с PDF-вложениями и ключевыми словами в теме («счёт», «акт», «УПД»).
5. **Извлечь текст** — PDF → текст (Extract from File или OCR), затем LLM-нода с жёстким JSON-схемой: ИНН, дата, номер, сумма, НДС, контрагент.
6. **Записать в Google Sheets-реестр** — колонки: дата письма, контрагент, номер документа, сумма, статус `на проверке`, ссылка на файл.
7. **Уведомить в Telegram** — краткая сводка + ссылка на строку реестра; human-in-the-loop обязателен.
8. **Чек-лист ручной сверки** — сравнить сумму с договором/заказом, пометить `одобрено` или `отклонено`; только после этого — экспорт в 1С/ЭДО (второй этап, не обещать «магию»).

---

## Яндекс Wordstat (МCP user-mcp-kv)

⚠️ **WORDSTAT PARTIAL WARNING:** по точной фразе `n8n для финансиста` API вернул пустой ответ `{}` (нулевой или нестабильный спрос в Вордстате). Ниже — проверенные смежные запросы с числами из успешных вызовов `wordstat_get_top_requests`, регион 225 (Россия), 17.06.2026.

| Фраза | Показы в месяц | Роль в статье |
| --- | ---: | --- |
| n8n | 35 475 | Головной спрос на платформу |
| автоматизация n8n | 559 | LSI, блок «зачем финансисту» |
| автоматизация бухгалтерии | 1 142 | Смежный кластер аудитории |
| первичные документы автоматизация | 239 | Боль «первичка» |
| автоматизация первички | 30 | Узкий, но целевой secondary |
| n8n бухгалтерия | 1 | Длинный хвост |
| сбор счетов из почты | 1 | Длинный хвост (формулировка редкая) |

**LSI из топа Вордстата (для копирайтера):** `автоматизация через n8n`, `примеры автоматизации n8n`, `ai автоматизация и n8n`, `автоматизация процессов n8n`, `автоматизация 1с бухгалтерия`, `ввод первичных документов`.

**SEO-вывод:** основной трафик идёт через «n8n» + «автоматизация бухгалтерии/первички»; в H1 и лиде держать связку «n8n + первичка из почты + реестр без ручного ввода», не гнаться за несуществующим высокочастотным «n8n для финансиста».

---

## SERP (WebSearch Cursor, 17.06.2026)

Приоритет — живой поиск агента; `research-serp.json` (шаг 0) использован как черновик, сверка ниже.

### Главный запрос: `n8n для финансиста` / H1

| # | URL | Тип | Пробел для КОДА |
| --- | --- | --- | --- |
| 1 | https://n8n.io/pricing/ | Официальные тарифы | Нет финансового кейса |
| 2 | https://utilo.io/ru/home/blog/n8n-review-2026-workflow-automation | Обзор платформы | Не про первичку |
| 3 | https://tenchat.ru/media/5295215-oplata-n8n-iz-rossii-2026-godu-obzor-dostupnykh-sposobov-kupit-podpisku-n8n | Оплата из РФ | Не про workflow |
| 4 | https://bot-craft.ru/blog/n8n-automation-2026/ | Общая автоматизация | Без пошаговой первички |
| 5 | https://subger.com/ru/service/n8n-cloud | Агрегатор + сниппет про 5 автоматизаций финансиста | Нет разбора нод и Яндекс Почты |
| 6 | https://pressaff.com/articles/n8n-in-practice-company-cases-installation-and-the-first-workflow/ | Практика, установка | Кейс почты есть, но не реестр первички |
| 7 | https://nikolaymatrosov.ru/2025-11-28-Yandex-Mail-in-N8n/ | **IMAP + Яндекс** | Только триггер, без AI и реестра |
| 8 | https://n8n.io/workflows/9439-automated-invoice-processing-and-filing-with-imap-ai-google-drive-and-datev/ | **Шаблон invoice IMAP→AI→Sheets** | Западный стек (DateV), нет РФ-контекста |
| 9 | https://ezgpt.ru/articles/kak-sdelat-ii-agenta-dlya-schetov-aktov-i-pervichki | ИИ-агент для первички | Широкий стек, не фокус «финансист сам в n8n» |
| 10 | https://linero.store/n8n-invoice-automation-accounting/ | Архитектура LLM + n8n | Маркетинговый тон, мало конкретики по Яндексу |
| 11 | https://chimitdorzhi.tech/blog/ai-pomoshchnik-buhgaltera-2026/ | AI для бухгалтера 2026 | Python/1С, не no-code гайд n8n |

### Вторичные запросы

- **`автоматизация первички n8n`** — в топе контент-заводы и AI-маркетинг (mayai.ru, neiroscop.ru), **не** финансовый реестр.
- **`n8n бухгалтерия`** — journal.tarasovkn.ru (генератор workflow), chimitdorzhi.tech; нет связки «почта → таблица за 1 вечер».
- **`сбор счетов из почты автоматически`** — SaaS (GetInvoice, Receiptor AI, Bitrix24), не self-hosted n8n.

### Конкурентный зазор (угол КОДА)

1. **Финансист-автоматизатор** (Ольга / КОДА): staging-реестр в Sheets как прослойка до 1С — не обещать прямую проводку.
2. **Яндекс Почта + IMAP** — редко в связке с пошаговыми скринами нод (есть только Matrosov).
3. **Human-in-the-loop + 152-ФЗ** — предупреждение про ПД в облачных LLM; self-hosted n8n на РФ-VPS.
4. **Чек-лист сверки сумм** — отличие от «полной автоматизации бухгалтерии» конкурентов.
5. **Дзен-формат:** один рабочий сценарий, цифры времени/денег, CTA в Telegram/клуб KODA.

---

## Таблица фактов (только с URL; для writer)

| # | Утверждение | Источник | Дата проверки |
| --- | --- | --- | --- |
| 1 | n8n Cloud Starter: **20 €/мес** при годовой оплате, **2 500** workflow executions/мес | https://n8n.io/pricing/ | 2026-06-17 |
| 2 | n8n Cloud Pro: **50 €/мес** годовая, **10 000** executions/мес | https://n8n.io/pricing/ | 2026-06-17 |
| 3 | n8n Business self-hosted: **667 €/мес** годовая, **40 000** executions/мес, SSO/SAML | https://n8n.io/pricing/ | 2026-06-17 |
| 4 | Community Edition self-hosted: **€0** за лицензию, unlimited workflows/users на своей инфраструктуре | https://n8n.io/pricing/ | 2026-06-17 |
| 5 | Один **execution** = один полный прогон workflow, шаги внутри не тарифицируются отдельно | https://n8n.io/pricing/ | 2026-06-17 |
| 6 | Яндекс IMAP для n8n: хост **imap.yandex.ru**, порт **993**, SSL, пароль приложения | https://nikolaymatrosov.ru/2025-11-28-Yandex-Mail-in-N8n/ | 2026-06-17 |
| 7 | Шаблон n8n #9439: IMAP → AI извлечение полей счёта → Google Drive → **Google Sheets** → архив письма | https://n8n.io/workflows/9439-automated-invoice-processing-and-filing-with-imap-ai-google-drive-and-datev/ | 2026-06-17 |
| 8 | В шаблоне #9439 AI выделяет: компания, номер счёта, дата, сумма, НДС | https://n8n.io/workflows/9439-automated-invoice-processing-and-filing-with-imap-ai-google-drive-and-datev/ | 2026-06-17 |
| 9 | Self-hosted n8n: VPS **€5–10/мес** на малых нагрузках; **$20–40/мес** при ~20k executions (оценка инфраструктуры) | https://arahi.ai/blog/n8n-pricing-explained-2026 | 2026-06-17 |
| 10 | pressaff: self-host **€5–10** VPS vs **€20–120** облако; актуально для ПД (GDPR, **152-ФЗ**) | https://pressaff.com/articles/n8n-in-practice-company-cases-installation-and-the-first-workflow/ | 2026-06-17 |
| 11 | AI в бухгалтерии снимает **60–70%** рутины (OCR, сверки, категоризация) — оценка автора | https://chimitdorzhi.tech/blog/ai-pomoshchnik-buhgaltera-2026/ | 2026-06-17 |
| 12 | Human-in-the-loop: AI готовит черновик, финальную ответственность несёт бухгалтер | https://chimitdorzhi.tech/blog/ai-pomoshchnik-buhgaltera-2026/ | 2026-06-17 |
| 13 | ПД в первичке (ИНН, ФИО): прямая отправка в зарубежные LLM из РФ-юрлица — риск **152-ФЗ** | https://chimitdorzhi.tech/blog/ai-pomoshchnik-buhgaltera-2026/ | 2026-06-17 |
| 14 | Типовой торговый поток: **200–1500** первичных документов/день (контекст масштаба боли) | https://chimitdorzhi.tech/blog/ai-pomoshchnik-buhgaltera-2026/ | 2026-06-17 |
| 15 | OCR Yandex Vision: порядка **50 коп./страница**, лимит **1 МБ** на запрос (альтернатива LLM на PDF) | https://chimitdorzhi.tech/blog/ai-pomoshchnik-buhgaltera-2026/ | 2026-06-17 |
| 16 | ezgpt: стек агента первички — n8n, Google Sheets журнал, OCR, LLM JSON, опционально 1С/Диадок | https://ezgpt.ru/articles/kak-sdelat-ii-agenta-dlya-schetov-aktov-i-pervichki | 2026-06-17 |
| 17 | Спрос «n8n» в Wordstat РФ: **35 475** показов/мес | MCP wordstat_get_top_requests | 2026-06-17 |
| 18 | «автоматизация бухгалтерии»: **1 142** показов/мес | MCP wordstat_get_top_requests | 2026-06-17 |

**Не использовать из fact-bank.md** — записи про контент-заводы/Make; к B01 не относятся.

---

## Риски и оговорки для writer

- Не обещать автоматическую проводку в 1С без доработки API и типовой конфигурации.
- Не давать юридических гарантий по НДС/налогам.
- Цены клуба KODA — только с лендинга/бота.
- Длинное тире «—» в тексте статьи запрещено (site-brief).
- Эмодзи в теле статьи запрещены.

---

## Internal links (из карточки)

- `/avtomatizaciya-finansov-no-code/`
- `/ot-excel-k-fin-konturu-30-dney/`

---

## FAQ hints (ответы-действия)

| Вопрос | Направление ответа |
| --- | --- |
| Нужно ли программировать для n8n? | Нет для базового сценария; Code node опционален |
| Безопасно ли гонять первичку через нейросеть? | Self-hosted + обезличивание/российские LLM; всегда ручная сверка |
| Сколько времени экономит сценарий? | Оценка: минус 30–60 мин/день на ручной ввод при 10–30 счетах/нед (экспертная оценка, пометить в тексте) |

---

## Источники исследования

- WebSearch Cursor (17.06.2026): primary + secondary queries
- MCP Wordstat: `n8n`, `автоматизация бухгалтерии`, `автоматизация n8n`, `первичные документы автоматизация`, `сбор счетов из почты`
- WebFetch: n8n.io/pricing, nikolaymatrosov.ru, n8n workflow 9439, chimitdorzhi.tech, ezgpt.ru
- `memory/brief/site-brief.md`, `memory/topics/blog-topics.md` (карточка B01)
