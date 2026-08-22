# Research notes — B90

**topic_id:** B90  
**slug:** cursor-skill-vygruzka-1c-odata  
**h1:** Как оформить Cursor Skill «выгрузка из 1С»: чеклист, OData, типичные ошибки  
**research_date:** 2026-08-22  
**publish_target:** koda-fd.ru/blog  
**utility_gate:** PASS (`checklist`, mode B)  
**related_published:** `/vygruzka-1c-excel-odata/` (B13 — OData в Excel/Sheets), `/mcp-1c-cursor-ostatki-oboroty/` (B80 — MCP + остатки), `/cursor-rules-finotdel/` (B23 — rules), `/mcp-cursor-finansist-instrumenty/` (B21 — filesystem MCP)  
**sibling_queue:** B91 (HTTP-сервис счёта), B81 (Sheets + OData)

---

## utility_verdict

**PASS** — checklist mode B для финотдела: когда оформлять выгрузку 1С как Cursor Skill, а не только MCP/rules; минимальный каркас `.cursor/skills/<name>/SKILL.md`; связка Skill → MCP OData → проверка выборки; чеклист безопасности (read-only, без сырых ПДн в облако); типичные ошибки OData и активации skill. Не новость про Cursor 2.5, не каталог 115 dev-skills Desko77, не курс по BSL.

---

## reader_outcome

После гайда финансист или финаналитик сможет оформить в проекте Cursor Skill «выгрузка из 1С через OData»: прописать `SKILL.md` с триггером и пошаговым workflow для агента, подключить MCP-сервер OData, прогнать smoke-test на ограниченной выборке и сверить результат с отчётом 1С — без повторного объяснения правил в каждом чате.

---

## action_outline

1. **Проверить, что Skill — нужный слой** — повторяющиеся сценарии «выгрузи регистр / дебиторку / ДДС за период»; если OData ещё не опубликован — сначала B13/B80 с админом, Skill не заменяет публикацию.
2. **Подготовить транспорт OData + MCP** — опубликовать `…/odata/standard.odata`, узкий состав сущностей, пользователь read-only; в `.cursor/mcp.json` подключить `1c-odata-mcp` (`npx -y 1c-odata-mcp`) или MCP из `gybson63/1c-oData-skill`; секреты только в `env`.
3. **Создать папку skill** — `.cursor/skills/1c-odata-export/SKILL.md` (имя папки = `name` во frontmatter, lowercase + дефисы).
4. **Заполнить YAML frontmatter** — обязательные `name`, `description` (когда агент включает skill: «выгрузка», «OData», «1С», «дебиторка», «реестр»); опционально `paths` на `data/**`, `exports/**`; для ручного вызова — `disable-model-invocation: true`.
5. **Описать workflow в теле SKILL.md** — блоки «When to Use», « Preconditions », «Steps»: (a) уточнить сущность и период, (b) вызвать MCP tool / GET с `$top`/`$filter`, (c) сохранить в `exports/` или staging-лист, (d) **не** слать сырой JSON в облачный чат без обезличивания.
6. **Добавить references/** — шаблон URL, список разрешённых `Catalog_*` / `AccumulationRegister_*`, лимиты `$top`, примеры ошибок 401/404; при необходимости `scripts/validate_export.py` для локальной сверки строк.
7. **Smoke-test в Agent** — Customize → Skills: skill виден; промпт «Выгрузи движения ДДС за август 2026, top 100» → подтверждение MCP tool → сверка 2–3 сумм с отчётом 1С.
8. **Прогнать чеклист безопасности** — read-only MCP; запрет write/confirm без человека; минимальный состав OData; линк на обезличивание; не коммитить пароли и полные выгрузки в git.
9. **Зафиксировать типичные ошибки в skill** — пустой `value` (объект не в составе OData), 401 (роль OData / логин), таймаут на больших `$top`, галлюцинации имён сущностей без `$metadata` / conf-doc search.

---

## Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT AUTH WARNING:** сервер MCP `user-mcp-kv` в этой сession **не подключён** (в каталоге MCP доступны только `cursor-cloud` и `cursor-subscriptions`, инструментов `wordstat_*` нет). Точные показы/мес **не получены** и **не выдуманы**. Обновите токен / подключите MCP-KV: https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

**Экспертная семантика (без цифр спроса) — LSI для копирайтера:**

| Кластер | Фразы | Роль |
| --- | --- | --- |
| Primary | cursor skill 1с odata, cursor skill выгрузка 1с | H1, лид |
| Skills format | skill.md cursor, agent skills cursor, .cursor/skills | H2 про оформление |
| OData | odata 1с standard.odata, публикация odata, выгрузка данных 1с | H2 транспорт |
| MCP bridge | 1c-odata-mcp, mcp cursor 1с, odata mcp | H2 связка Skill→MCP |
| Fin angle | автоматизация финотдела 2026, выгрузка для финансиста, дебиторка odata | Secondary intent |
| Safety | read-only odata, обезличивание 1с, пользователь только чтение | H2 риски |
| Errors | odata 401, объект не в составе odata, типичные ошибки odata | H2 troubleshooting |

**SEO-вывод:** SERP по «cursor skill 1с odata» — dev-контент (Desko77, Rutube, MCP+BSL). По «автоматизация финотдела 2026» — ERP/SAP/Make без Cursor Skills. **Пробел КОДА:** checklist **оформления Skill** под финансовую выгрузку через OData + MCP, с DoD-сверкой и безопасностью; не дублировать B13 (ручной Excel) и B80 (подключение MCP без SKILL.md).

---

## SERP (WebSearch Cursor, 22.08.2026)

Приоритет — живой WebSearch; `research-serp.json` (шаг 0) использован как черновик URL, дополнен результатами ниже.

### Главный запрос: `cursor skill 1с odata 2026`

| # | URL | Тип | Пробел для КОДА |
| --- | --- | --- | --- |
| 1 | https://cursor.com/docs/skills | Официальная доку Cursor Skills | Формат SKILL.md, каталоги — нет 1С/OData |
| 2 | https://github.com/Desko77/cursor-1c-skills | OSS: 115 skills для разработки 1С | BSL/метаданные/EDT; не fin-export checklist |
| 3 | https://github.com/gybson63/1c-oData-skill | OSS: skills/odata + MCP + бот | Близкий референс SKILL.md; аудитория — разработчик бота |
| 4 | https://github.com/evilbruce666/1c-odata-mcp | OSS MCP OData | README сильный; нужен мост «Skill + финотдел + чеклист» |
| 5 | https://shtruzel.ru/articles/cursor-dlya-1c-nastrojka-mcp-bsl-2026 | RU dev stack 2026 | MCP-1C + rules; не Skill для выгрузки CFO |
| 6 | https://rutube.ru/video/063997c7e3aae6107e4be2bfd06df119/ | Видео Rules+Skills 1С (май 2026) | Установка community skills; нет OData export workflow |
| 7 | https://vibecoderz.ru/notes/cursor-ai-ecosystem-2026-rules-mcp-skills | Конспект экосистемы Cursor | Rules vs Skills vs MCP; без финконтура |
| 8 | https://aitools1c.dev/tools/1c-odata-mcp/ | Каталог 1C AI tools | Спека tools/limitations; не how-to Skill |

### Вторичный: `автоматизация финотдела 2026`

| # | URL | Тип | Пробел |
| --- | --- | --- | --- |
| 1 | https://vsl-bi.ru/avtomatizaciya_biznesa_2026 | RU trends CFO | Классификация платежей, сверки — без Cursor |
| 2 | https://koda-fd.ru/blog/ai-dlya-finansista-2026/ | Adjacent KODA | AI-контур; линк, не конкурент |
| 3 | https://bsg-it.ru/blog/odata-i-ii-agenty-v-1c | OData + ИИ-агенты | Безопасное чтение — усилить H2 security |
| 4 | https://infostart.ru/1c/articles/2714438/ | OData → Telegram (БП 3.0) | Практические грабли OData — в FAQ/errors |
| 5 | https://superintellect.ru/guides/kak-podklyuchit-1c-k-ii-agentu | Коннектор OData (SaaS) | Роль OData, логин латиницей — факты, не CTA конкурента |

### H1: «Как оформить Cursor Skill «выгрузка из 1С»: чеклист, OData, типичные ошибки»

Прямых статей с таким H1 **нет**. Ближайшие: `gybson63/1c-oData-skill` (структура skills), `cursor.com/docs/skills` (формат), B13/B80 на koda-fd (OData/MCP без Skill). **Угол КОДА:** один вечер → готовый SKILL.md + MCP → сверка с отчётом 1С.

### Конкурентный зазор

1. **Финансист vs 1С-разработчик** — не 115 dev-skills; один focused skill под повторяемую выгрузку.
2. **Skill как упаковка workflow** — rules = конституция; MCP = транспорт; Skill = пошаговый сценарий «что делать агенту» при запросе выгрузки.
3. **DoD = сверка** — 2–3 строки против отчёта 1С, не «агент что-то вернул».
4. **Граница с B13/B80/B23** — B13 Excel/Sheets; B80 MCP остатки; B23 rules/ПДн; B90 = SKILL.md + OData export.
5. **152-ФЗ / коммерческая тайна** — read-only, узкий OData, обезличивание перед облачной моделью.

---

## Таблица фacts (только с URL; для writer)

| # | Утверждение | Источник | Дата проверки |
| --- | --- | --- | --- |
| 1 | Agent Skills — открытый стандарт; skill = папка с `SKILL.md`; Cursor подхватывает skills при старте и предлагает агенту по релевантности. | https://cursor.com/docs/skills | 2026-08-22 |
| 2 | Обязательные поля frontmatter: `name` (lowercase, дефисы, совпадает с именем папки) и `description` (агент решает, когда применять). | https://cursor.com/docs/skills | 2026-08-22 |
| 3 | Каталоги skills: `.cursor/skills/`, `.agents/skills/`, глобально `~/.cursor/skills/`, `~/.agents/skills/`; вложенные `.cursor/skills/` в monorepo scope'ятся к подпапке. | https://cursor.com/docs/skills | 2026-08-22 |
| 4 | Опционально: `paths` (glob) — skill только при работе с matching files; `disable-model-invocation: true` — только явный `/skill-name`. | https://cursor.com/docs/skills | 2026-08-22 |
| 5 | Skill может включать `scripts/`, `references/`, `assets/`; детали выносить из SKILL.md для progressive loading. | https://cursor.com/docs/skills | 2026-08-22 |
| 6 | В Cursor есть built-in `/create-skill` для генерации структуры SKILL.md. | https://cursor.com/docs/skills | 2026-08-22 |
| 7 | Платформа 1С формирует REST/OData **3.0**; публикация на веб-сервере; URL вида `…/odata/standard.odata`. | https://v8.1c.ru/platforma/rest-interfeys/ | 2026-08-22 |
| 8 | Состав стандартного OData задаётся явно; без включения объекта в публикацию запросы дают пустой результат / 404. | https://infostart.ru/1c/articles/1570140/ | 2026-08-22 |
| 9 | **1c-odata-mcp**: запуск `npx -y 1c-odata-mcp`; **read-only по умолчанию**; запись — двойной флаг + preview/confirm; без расширения/COM/SQL на стороне 1С. | https://github.com/evilbruce666/1c-odata-mcp | 2026-08-22 |
| 10 | 1c-odata-mcp: Node.js **20+**; нужен опубликованный OData; analytics tools: debtors, inventory, sales, cashflow (ориентация на БП 3.0). | https://aitools1c.dev/tools/1c-odata-mcp/ | 2026-08-22 |
| 11 | 1c-odata-mcp регистрирует **55 tools** (21 read/analytics + 34 write); write-tools видны в list даже в read-only — блокировка на уровне env/HTTP. | https://aitools1c.dev/tools/1c-odata-mcp/ | 2026-08-22 |
| 12 | Лимиты чтения: `ODATA_MAX_ROWS` до 100000 (default 1000); аналитика до 1M строк (default 200000) — риск тяжёлых выборок для финотдела. | https://aitools1c.dev/tools/1c-odata-mcp/ | 2026-08-22 |
| 13 | **gybson63/1c-oData-skill**: отдельный skill `skills/odata/SKILL.md` + workflow `conf_doc_search` → OData fetch; docs/mcp-setup.md для Cursor. | https://github.com/gybson63/1c-oData-skill | 2026-08-22 |
| 14 | **Desko77/cursor-1c-skills**: **115 skills** и **35 rules** — разработка конфигураций; skill `1c-mcp-toolkit` для HTTP API к базе, не fin-export checklist. | https://github.com/Desko77/cursor-1c-skills | 2026-08-22 |
| 15 | OData для ИИ в 1С — аккуратный слой **чтения**; опасно: массовое чтение всего, запись без человека, изменение справочников без аудита. | https://bsg-it.ru/blog/odata-i-ii-agenty-v-1c | 2026-08-22 |
| 16 | Infostart (2714438): рабочая OData-выгрузка показателей в мессенджер собирается за **вечер**, если заранее знать грабли (состав OData, файловая база, регламентные операции). | https://infostart.ru/1c/articles/2714438/ | 2026-08-22 |
| 17 | Для OData-интеграций рекомендуют отдельного пользователя ИБ с минимальными правами и ролью удалённого доступа OData; логин **латиницей** (кириллица может не приниматься коннекторами). | https://superintellect.ru/guides/kak-podklyuchit-1c-k-ii-agentu | 2026-08-22 |
| 18 | Noltis 2026: OData — «получить/записать» без бизнес-логики; на больших выборках (**200+** записей в их примере) уже тормозит; сложная аналитика — HTTP-сервисы. | https://noltis.ru/blog/ii-poverh-1s-automation/ | 2026-08-22 |
| 19 | Agent Skills spec: `name` max **64** символа; `description` max **1024**; SKILL.md рекомендуется держать **<500 строк**. | https://github.com/agentskills/agentskills/blob/main/docs/specification.mdx | 2026-08-22 |
| 20 | Cursor MCP config: проектный `.cursor/mcp.json`; после правки — перезапуск; Agent запрашивает подтверждение tool call (см. B80/B21). | https://cursor.com/ru/help/customization/mcp | 2026-08-22 |

**Не использовать как факт без оговорки:** «экономия 40% времени финотдела» из generic SEO; «800+ бухгалтеров»; точные показы Wordstat; «115 skills» Desko77 как обязательная установка для CFO; обещание «без программиста на 100%» если OData не опубликован; write-сценарии 1c-odata-mcp в fin-skill без human-in-the-loop.

**Fact-bank:** прямых фактов про Cursor Skill + 1С OData в `fact-bank.md` **нет** — опираться на таблицу выше. Контент-заводные цифры fact-bank к B90 **не тянуть**.

---

## Структура H2/H3 для writer (из карточки B90)

### H2: Когда это нужно финотделу (и когда нет)
- Нужно: повторяемые выгрузки (ДДС, дебиторка, реестр документов), ad-hoc срезы через Agent.
- Не нужно: разовая ручная выгрузка → B13; нет OData → сначала админ; нужны только остатки без skill-packaging → B80.
- Таблица: Rules vs MCP vs Skill (когда что).

### H2: Подготовка данных и безопасность (без сырых ПДн в облако)
- Read-only пользователь; узкий состав OData; env-секреты; Privacy Mode.
- В SKILL.md явный запрет: не paste полный JSON с ФИО/ИНН в чат; staging `exports/` + `.gitignore`.
- Internal: `/obezlichivanie-dannyh-chatgpt-finansist/`.

### H2: Пошаговое оформление Skill + MCP
- Шаг 1: папка `.cursor/skills/1c-odata-export/`.
- Шаг 2: frontmatter + skeleton SKILL.md (When to Use / Preconditions / Steps / Errors).
- Шаг 3: `.cursor/mcp.json` для `1c-odata-mcp` (плейсхолдеры URL/user).
- Шаг 4: `references/entities.md` — whitelist сущностей fin-отдела.
- Мини-пример SKILL.md (без реальных паролей).

### H2: Проверка результата и типичные ошибки
- DoD: 2–3 строки vs отчёт 1С; skill сработал (badge / `/1c-odata-export`).
- Ошибки: 401, пустой value, timeout на `$top`, agent без tool call (галлюцинация), write без confirm.
- MCP Logs; `$metadata` для имён сущностей.

### H2: Что автоматизировать дальше
- Второй skill: сверка CSV vs 1С (B28); scheduled export; связка с Sheets (B81).
- Internal: `/avtomatizaciya-finansov-no-code/`, `/vygruzka-1c-excel-odata/`, `/mcp-1c-cursor-ostatki-oboroty/`.

---

## FAQ hints (ответы-действия)

| Вопрос | Направление ответа |
| --- | --- |
| Можно ли без программиста? | Skill оформить — да. OData опубликовать и состав сущностей — часто админ **один раз**; дальше финансист повторяет сценарий через Agent. |
| Сколько займёт внедрение? | OData готов: **1–2 часа** на SKILL.md + smoke-test. С нуля публикация + MCP: **вечер** с админом (ориентир Infostart 2714438 — «за вечер» при известных граблях). |
| Чем Skill отличается от Rules? | Rules — постоянные ограничения (ПДн, папки). Skill — **процедура** выгрузки при релевантном запросе. |
| Нужен ли отдельный MCP? | Да, Skill инструктирует агента **как** вызывать tools; транспорт — MCP (`1c-odata-mcp` или аналог). |
| Какие риски для данных? | Утечка через облачную модель + избыточный `$top`; mitigations: read-only, whitelist, обезличивание, локальная модель. |
| Можно ли писать в базу через skill? | Для fin-старта — **нет**; только read; write только отдельный проект с preview/confirm и отдельным skill. |

---

## Internal links

- `/avtomatizaciya-finansov-no-code/` (из карточки)
- `/obezlichivanie-dannyh-chatgpt-finansist/` (из карточки)
- `/vygruzka-1c-excel-odata/` (B13)
- `/mcp-1c-cursor-ostatki-oboroty/` (B80)
- `/cursor-rules-finotdel/` (B23)

---

## CTA (conversion-map)

| CTA | URL | Лимит |
| --- | --- | --- |
| Клуб KODA | https://club.koda-fd.ru/?utm_source=blog&utm_medium=article&utm_campaign=cursor-skill-vygruzka-1c-odata | ≤2 |
| Telegram | https://t.me/finance_modern?utm_source=blog&utm_medium=article | ≤2 |

**Запрещено:** `t.me/koda_salebot`, `@koda_salebot`.

---

## Cover hint

abstract holographic finance automation dark #0a0a0f purple #8b5cf6, no text (из карточки)

---

## Источники исследования

- https://cursor.com/docs/skills
- https://github.com/agentskills/agentskills/blob/main/docs/specification.mdx
- https://github.com/evilbruce666/1c-odata-mcp
- https://aitools1c.dev/tools/1c-odata-mcp/
- https://github.com/gybson63/1c-oData-skill
- https://github.com/Desko77/cursor-1c-skills
- https://v8.1c.ru/platforma/rest-interfeys/
- https://bsg-it.ru/blog/odata-i-ii-agenty-v-1c
- https://infostart.ru/1c/articles/2714438/
- https://superintellect.ru/guides/kak-podklyuchit-1c-k-ii-agentu
- https://noltis.ru/blog/ii-poverh-1s-automation/
- https://shtruzel.ru/articles/cursor-dlya-1c-nastrojka-mcp-bsl-2026
- WebSearch Cursor 2026-08-22; `research-serp.json` как черновик шага 0
