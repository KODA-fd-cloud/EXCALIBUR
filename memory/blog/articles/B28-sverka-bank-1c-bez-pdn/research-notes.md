# Research notes — B28

**topic_id:** B28  
**slug:** sverka-bank-1c-bez-pdn  
**h1:** Как сверить банк и 1С без отправки ПДн в ChatGPT  
**research_date:** 2026-08-01  
**publish_target:** сайт koda-fd.ru/blog  
**utility_gate:** PASS (`checklist`, mode B)  
**related_published:** `/obezlichivanie-dannyh-chatgpt-finansist/` (B11), `/python-finansist-sverka-csv/` (B19)  
**internal_links:** `/obezlichivanie-dannyh-chatgpt-finansist/`, `/python-finansist-sverka-csv/`

---

## utility_verdict

**PASS** — тема utility-only checklist (mode B). Читатель получает рабочий маршрут: сверить обороты и остатки банк ↔ 1С, обезличить выписку до любой облачной LLM, выбрать локальный vs облачный маршрут (Python/Claude Code vs ChatGPT), пройти чеклист расхождений (дата, сумма, назначение, дубли, комиссии) и понять, когда хватает таблицы, а когда нужен 1С-ник. Не новость про DirectBank, не «что такое сверка» без шагов.

---

## reader_outcome

После гайда финансист или CFO сможет за один закрывающий цикл сверить банковскую выписку с 1С (обороты и остаток по счёту 51), подготовить обезличенную выгрузку для ИИ или прогнать сверку локально через Python/Cursor без передачи ИНН, счетов и ФИО в ChatGPT, и закрыть типовые «висяки» по чеклисту расхождений.

---

## action_outline

1. **Зафиксировать DoD сверки** — период, счёт, совпадение входящего остатка, дебет/кредит оборотов и конечного сальдо с банком; отдельно список «висяков» (есть в банке, нет в 1С, и наоборот).
2. **Подготовить данные в 1С** — загрузить выписку (DirectBank или файл `1CClientBankExchange`), провести документы «Поступление/Списание», сверить ОСВ по счёту 51 и карточку счёта с интернет-банком на контрольную дату.
3. **Выгрузить две «половинки» для сверки** — из 1С и из банка в CSV/Excel с колонками: дата, сумма, тип (приход/расход), ключ операции (хэш или surrogate-id), без сырых реквизитов в общий чат.
4. **Обезличить до любой нейросети** — заменить ИНН, р/с, названия контрагентов, ФИО в назначении платежа на маркеры `[Контрагент_1]`, `[Счёт_A]`; проверить колонтитулы и комментарии; см. B11.
5. **Выбрать маршрут анализа** — облако (только обезличенный срез + промпт «найди расхождения по дате/сумме») vs локально (pandas merge / Claude Code / Ollama на CSV в папке проекта без upload).
6. **Пройти чеклист расхождений** — дубль загрузки, неверная дата документа, неучтённая комиссия, неверный контрагент/договор, пропущенная строка выписки, расхождение входящего остатка.
7. **Исправить и пересверить** — точечно править документы за проблемный день, не «перепроводить всё»; повторить сравнение оборотов до нуля расхождения.
8. **Зафиксировать правило команды** — сырые выписки и выгрузки 1С не в публичный ChatGPT; повторяемый скрипт сверки в `data/` (мост к B19/B20).

---

## Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT AUTH WARNING:** сервер MCP `user-mcp-kv` в этой сессии **не подключён** (в каталоге MCP нет инструментов `wordstat_*`). Точные показы/мес **не получены** и **не выдуманы**. Обновите токен / подключите MCP-KV: https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

**Экспертная семантика (без цифр спроса) — LSI для копирайтера:**

| Кластер | Фразы | Роль |
| --- | --- | --- |
| Primary | сверка банка и 1с, сверка банка с 1с | H1, лид |
| Выписка | сверка выписки 1с, загрузка банковской выписки 1с, расхождения выписки банк | H2 подготовка |
| Обороты | сверка оборотов банк учет, остаток по счету 51, оборотно-сальдовая ведомость 51 | H2 DoD |
| ИИ / ПДн | обезличить выписку для ии, chatgpt бухгалтерия без персональных данных, маскирование инн excel | H2 обезличивание |
| Автоматизация | directbank 1с, клиент банк 1с, 1cclientbankexchange | FAQ / контекст |
| Локально | python сверка csv, pandas merge банк 1с, claude code финотдел | CTA → B19 |

**SEO-вывод:** SERP по «сверка банка и 1с» занят гайдами 1С-интеграторов (DirectBank, клиент-банк, типовые ошибки). Прямого ответа на H1 («без ПДн в ChatGPT») в топ-10 нет. Угол КОДА: **чеклист сверки + политика данных + локальный маршрут**, не настройка банк-клиента с нуля.

---

## SERP (WebSearch Cursor, 01.08.2026)

`research-serp.json` (preflight) использован как черновик; приоритет — живой WebSearch ниже. Запрос «обезличить выписку для ии» в duck-поиске уехал в новости про ИНН/ЕГРН — игнорируем; релевантность взята из WebSearch по маскированию + финансы.

### Primary: `сверка банка и 1с`

| # | URL | Тип | Пробел для КОДА |
| --- | --- | --- | --- |
| 1 | https://saldovka.com/2026-exp/bankovskie-vypiski-v-1s-8-3.html | How-to: DirectBank, клиент-банк, сверка 51 | Нет обезличивания и ИИ; чистая 1С-настройка |
| 2 | https://integration-software.ru/blog/bank-statement-discrepancies | Чеклист расхождений банк↔1С | Нет AI/152-ФЗ; сильный блок типовых ошибок — взять алгоритм, не копировать структуру |
| 3 | https://assistant1c.com/blog/1c-buhgalteriya/bank/bankovskie-vypiski-v-1s/ | Загрузка и разнесение выписок | Облако LLM не упоминается |
| 4 | https://1c.itat.ru/articles/rabota-s-klient-bankom-v-1s-bukhgalteriya-polnoe-rukovodstvo-2025-2026/ | Клиент-банк полный гайд | Длинный onboarding; не checklist для CFO с ИИ |
| 5 | https://itsreda.ru/articles/1c-buh-8/kak-nastroit-obmen-s-bankom-v-1s-bukhgalterii-3-0-i-izbezhat-raskhozhdeniy-po-vypiskam/ | Обмен с банком + контроль | Нет staging/маскирования |
| 6 | https://life1c.ru/post/3462 | Сверка данных с банками | Классический 1С-контент |

### Secondary: `сверка выписки 1с`

| # | URL | Тип | Пробел для КОДА |
| --- | --- | --- | --- |
| 7 | https://www.1cbit.kz/services/line_consult/faq/kak_proverit_pravilnost_razneseniya_bankovskikh_vypisok_v_1s_erp_i_1s_ka/ | ERP: отчёт «Сверка банковских выписок» | ERP/КА, не Бух 3.0 + не AI |
| 8 | https://dorabotka-1c.my1.ru/blog/pochemu_pri_zagruzke_bankovskoj_vypiski_v_1s_ne_skhodjatsja_vkhodjashhij_i_iskhodjashhij_ostatki/2025-07-23-2723 | Troubleshooting входящего остатка | Узкий кейс, без чеклиста ИИ |
| 9 | https://dzen.ru/a/agVowf-C5kd-2Oog | Дубли, остаток 51 | Практика без compliance |

### Secondary: обезличивание / ChatGPT + финансы

| # | URL | Тип | Пробел для КОДА |
| --- | --- | --- | --- |
| 10 | https://zinin-shturbin.com/blog/transgranichnaya-peredacha-dannyh-cherez-chatgpt/ | 152-ФЗ, трансграничная передача | Нет связки со сверкой банк↔1С |
| 11 | https://workwithai.ru/read/how-to-anonymize-data-before-ai | Шаблон обезличивания для ИИ | Общий, не банковская выписка |
| 12 | https://filehostseller.com/ru/cheklist-bezopasnosti-dlia-chatgpt-gemini-i-claude-chtoby-ne-peredavat-personalnye-dannye-v-ai/ | Чеклист безопасности LLM | Нет пошаговой сверки |
| 13 | https://sdvg.vc/blog/1s-i-chatgpt-kak-integrirovat-model-dlia-avtomatizatsii-bukhgalterii/ | 1С + ChatGPT интеграция | Риск утечки ПДн; противоречит углу КОДА |

### Secondary: `сверка оборотов банк учет`

| # | URL | Тип | Пробел для КОДА |
| --- | --- | --- | --- |
| 14 | https://centerbooker.ru/base/accounting/sverka-s-bankom/ | Базовая сверка с банком | Без 1С и без ИИ |
| 15 | https://beancount.io/ru/blog/2026/04/08/bank-reconciliation-what-it-is-how-to-do-it-and-why-every-small-business-needs-it | МSB bank reconciliation | Не российский 1С-контекст |
| 16 | https://www.lockobank.ru/articles/RKO/inventarizaciya-raschetnogo-scheta | ФСБУ 28/2023 инвентаризация р/с | Нормативный контекст, не how-to ИИ |

### H1: «Как сверить банк и 1С без отправки ПДн в ChatGPT»

Прямых конкурентов с таким H1 **нет**. Выдача смешивает банк-клиент и статьи про ChatGPT+1С без политики ПДн. **serp_gap КОДА:** единый checklist = сверка 1С + маскирование выписки + локальный Python/Cursor + ссылка на B11/B19.

---

## Таблица фактов (только с URL; для writer)

| # | Утверждение | Источник | Дата проверки |
| --- | --- | --- | --- |
| 1 | В 1С:Бухгалтерия 3.0 выписки загружают тремя способами: DirectBank (прямой обмен), клиент-банк (файл), ручной ввод. | https://saldovka.com/2026-exp/bankovskie-vypiski-v-1s-8-3.html | 2026-08-01 |
| 2 | Формат файлового обмена с банком — `1CClientBankExchange` (txt). | https://saldovka.com/2026-exp/bankovskie-vypiski-v-1s-8-3.html | 2026-08-01 |
| 3 | DirectBank — обмен между 1С и банком без промежуточных файлов; платёжки и выписки идут из программы. | https://saldovka.com/2026-exp/bankovskie-vypiski-v-1s-8-3.html | 2026-08-01 |
| 4 | Срок хранения банковских выписок — 5 лет (ст. 29 Закона № 402-ФЗ «О бухгалтерском учёте»). | https://saldovka.com/2026-exp/bankovskie-vypiski-v-1s-8-3.html | 2026-08-01 |
| 5 | После загрузки 1С создаёт «Поступление на расчётный счёт» и «Списание с расчётного счёта», подбирает контрагентов по ИНН; виды операций для комиссий нужно проверять вручную. | https://saldovka.com/2026-exp/bankovskie-vypiski-v-1s-8-3.html | 2026-08-01 |
| 6 | Контроль сверки: остаток в 1С vs банк, карточка счёта 51, отсутствие дублей по дате и сумме. | https://1c.itat.ru/articles/rabota-s-klient-bankom-v-1s-bukhgalteriya-polnoe-rukovodstvo-2025-2026/ | 2026-08-01 |
| 7 | Три частые причины расхождений: двойная загрузка файла, неверная дата документа (1С подставляет текущую), неучтённая банковская комиссия. | https://integration-software.ru/blog/bank-statement-discrepancies | 2026-08-01 |
| 8 | Алгоритм сверки начинается с сравнения **итоговых оборотов**, не построчного хаоса; отчёт «Оборотно-сальдовая ведомость по счёту 51» vs суммы из выписки банка. | https://integration-software.ru/blog/bank-statement-discrepancies | 2026-08-01 |
| 9 | Для поиска проблемного дня используют «Карточку счёта 51» с группировкой по дням и сравнивают дневные обороты с выпиской. | https://integration-software.ru/blog/bank-statement-discrepancies | 2026-08-01 |
| 10 | В 1С:ERP / КА есть отчёт «Сверка банковских выписок» (Казначейство → Отчёты по казначейству → Банк); расхождения по суммам подсвечиваются. | https://www.1cbit.kz/services/line_consult/faq/kak_proverit_pravilnost_razneseniya_bankovskikh_vypisok_v_1s_erp_i_1s_ka/ | 2026-08-01 |
| 11 | Несовпадение входящего и исходящего остатка при загрузке часто связано с неверным входящим остатком на начало периода — проверять последнюю выписку предыдущего периода. | https://dorabotka-1c.my1.ru/blog/pochemu_pri_zagruzke_bankovskoj_vypiski_v_1s_ne_skhodjatsja_vkhodjashhij_i_iskhodjashhij_ostatki/2025-07-23-2723 | 2026-08-01 |
| 12 | Повторная загрузка той же выписки создаёт дубли документов; контроль — сортировка выписок по дате и сумме. | https://integration-software.ru/blog/bank-statement-discrepancies | 2026-08-01 |
| 13 | 1С:ДиректБанк использует защищённый канал и стандарт ISO 20022; после подключения система запрашивает выписку и создаёт документы с реквизитами. | https://integration-software.ru/blog/avtomaticheskaya-vygruzka-bankovskoi-vypiski-1s-directbank | 2026-08-01 |
| 14 | С 1 апреля 2025 действуют правила инвентаризации по ФСБУ 28/2023; инвентаризация р/с — сверка остатков учёта с банковскими выписками. | https://www.lockobank.ru/articles/RKO/inventarizaciya-raschetnogo-scheta | 2026-08-01 |
| 15 | Перед отправкой в зарубежную LLM (ChatGPT) персональные и идентифицирующие данные нужно обезличивать: имена, телефоны, реквизиты заменять метками; иначе — трансграничная передача по 152-ФЗ. | https://zinin-shturbin.com/blog/transgranichnaya-peredacha-dannyh-cherez-chatgpt/ | 2026-08-01 |
| 16 | В банковской выписке нельзя отправлять в ИИ без обработки: ИНН, р/с, названия контрагентов, номера договоров — заменять на `[Компания_A]`, `[ID_1]`, `[реквизиты_X]`. | https://workwithai.ru/read/how-to-anonymize-data-before-ai | 2026-08-01 |
| 17 | Чеклист безопасности LLM: не передавать банковские выписки, пароли, кадровые файлы; маскировать ФИО и точные суммы при необходимости диапазонами. | https://filehostseller.com/ru/cheklist-bezopasnosti-dlia-chatgpt-gemini-i-claude-chtoby-ne-peredavat-personalnye-dannye-v-ai/ | 2026-08-01 |
| 18 | Сверка с банком — сопоставление учётных записей с выпиской для выявления неучтённых платежей, ошибок проводок и комиссий до сдачи отчётности. | https://centerbooker.ru/base/accounting/sverka-s-bankom/ | 2026-08-01 |

**Не использовать из fact-bank.md:** прямых строк про сверку банк/1С или ChatGPT там нет; цифры из mayai.ru/kontent-zavod не относятся к теме.

---

## Структура H2 для writer (из карточки B28)

1. **Что сравниваем: обороты, остатки, «висяки»** — DoD, счёт 51, outer-merge логика.
2. **Маскирование ИНН/счетов до любой нейросети** — таблица замен, тест «узнаёт ли коллега контрагента»; ссылка B11.
3. **Локальный маршрут: Python/Claude Code vs облако** — когда достаточно обезличенного промпта, когда только `data/` локально (B19).
4. **Чеклист расхождений: дата, сумма, назначение** — дубли, комиссии, входящий остаток, контрагент.
5. **Когда звать 1С-ника, а когда хватает таблицы** — границы типовой Бух 3.0 vs доработки ERP.

**FAQ hints (карточка):** можно ли полностью в Excel; нужен ли OData.

**CTA:** Telegram + клуб; не подменять чеклист продажей.

---

## Риски и запреты writer

- Не обещать «ChatGPT сверит банк за вас» на сырых данных.
- Не давать юридических гарантий по 152-ФЗ; формулировка «снижаем риск при обезличивании».
- Не дублировать B11 (3 уровня защиты) и B19 (установка Python) — только мосты.
- Эмодзи и длинное тире «—» запрещены (`site-brief.md`).
- B35 (`sverka-banka-n8n-google-sheets`) — другой slug; не смешивать с B28.

---

## Handoff marker

См. `.cursor/excalibur-blog-handoff.md` → `=== EXCALIBUR BLOG RESEARCH ===`
