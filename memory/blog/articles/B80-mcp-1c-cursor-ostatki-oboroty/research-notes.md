# Research notes — B80

**topic_id:** B80  
**slug:** mcp-1c-cursor-ostatki-oboroty  
**h1:** Как подключить MCP к 1С: читать остатки и обороты прямо из Cursor  
**research_date:** 2026-08-19  
**publish_target:** koda-fd.ru/blog  
**utility_gate:** PASS (`how_to`, mode B)  
**related_published:** `/mcp-cursor-finansist-instrumenty/` (B21 — filesystem MCP без 1С), `/vygruzka-1c-excel-odata/` (B13 — OData вручную)  
**sibling_queue:** B81 (HTTP-сервис), B21 (MCP для CSV-папки)

---

## utility_verdict

**PASS** — how_to для финотдела: выбрать MCP-стек под чтение остатков/оборотов из 1С; подготовить OData или HTTP-сервис и пользователя read-only; прописать сервер в `.cursor/mcp.json`; проверить зелёный статус и tool call; задать промпт «остатки по счёту / обороты за период» и сверить с отчётом 1С. Не новость про MCP Apps, не обзор «50 серверов для джуна», не курс по BSL.

---

## reader_outcome

После гайда финансист или аналитик сможет подключить в Cursor MCP-сервер к своей базе 1С (через OData или HTTP-расширение), запросить в Agent остатки и обороты по счёту или регистру на естественном языке и сверить ответ с типовым отчётом 1С — без выгрузки XLS в чат.

---

## action_outline

1. **Проверить применимость** — есть ли опубликованный OData или готовность поставить расширение с HTTP-сервисом (INFATON MCP35 / feenlace mcp-1c); если нет — маршрут через CSV + filesystem MCP (B21), не обещать «прямую розетку».
2. **Выбрать сервер под задачу «остатки/обороты»** — для бухгалтерских регистров: `get_balance` (INFATON MCP35); для регистров накопления: `get_register_totals`; альтернатива без расширения 1С: `1c-odata-mcp` (`read.analytics.get_debtors`, `get_sales`, `get_cashflow`) при включённом OData.
3. **Подготовить безопасность** — отдельный пользователь 1С только на чтение; пароли в `env` / `${env:…}`, не в git; Privacy Mode / обезличивание перед облачной моделью; не подключать боевую базу с полными правами.
4. **Опубликовать транспорт в 1С** — OData (галочка в публикации) или установить расширение (.cfe) + HTTP-сервис с Basic Auth; для INFATON — публикация «для расширения» + веб-сервер (IIS/Apache).
5. **Установить MCP-обёртку локально** — `npx -y 1c-odata-mcp` или Node `index.mjs` (MCP35), или бинарник `mcp-1c.exe` (feenlace); Node.js LTS при stdio-обёртках.
6. **Прописать `.cursor/mcp.json`** — проектный `.cursor/mcp.json` или глобальный `~/.cursor/mcp.json`; `command`/`args`/`env` с URL базы и учёткой read-only; перезапуск Cursor после правки JSON.
7. **Smoke-test в Cursor** — Settings → Tools & MCP (`Ctrl+Shift+J`): зелёный индикатор; Output → MCP Logs при ошибке; в Agent явный запрос с подтверждением tool.
8. **Рабочий промпт «остатки/обороты»** — пример: «Покажи остатки и обороты по счёту 62 за июль 2026 с разбивкой по контрагентам» → tool `get_balance` или `read.analytics.get_debtors`; сверить 2–3 строки с отчётом «Оборотно-сальдовая ведомость» / «Ведомость по счёту».
9. **Зафиксировать границы** — read-only по умолчанию у `1c-odata-mcp`; запись только с двойным предохранителем; не включать Auto-run всех tools на пилоте; лимит ~40 MCP-tools в Cursor — отключать лишние серверы.

---

## Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT AUTH WARNING:** сервер MCP `user-mcp-kv` в этой сессии **не подключён** (в каталоге MCP доступен только `cursor-cloud`, инструментов `wordstat_*` нет). Точные показы/мес **не получены** и **не выдуманы**. Обновите токен / подключите MCP-KV: https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

**Экспертная семантика (без цифр спроса) — LSI для копирайтера:**

| Кластер | Фразы | Роль |
| --- | --- | --- |
| Primary | mcp 1с cursor финансы, mcp 1с cursor, cursor mcp 1с | H1/лид |
| Balances | остатки обороты 1с cursor, get_balance, оборотно-сальдовая | Уникальный угол B80 |
| Setup | mcp.json cursor 1с, подключить mcp к 1с, настройка mcp cursor | H2 пошагово |
| Transport | odata 1с mcp, http сервис 1с mcp, infaton mcp | Выбор стека |
| Fin angle | дебиторка cursor 1с, обороты счёт 62, управленческая отчётность без xls | Сценарии |
| Adjacent | автоматизация финотдела 2026, ai для финансиста 1с | Secondary intent |
| Safety | read-only mcp 1с, обезличивание, пользователь только чтение | H2 риски |

**SEO-вывод:** SERP смешивает dev-гайды (BSL, metadata, mcp-1c для кода) и бухгалтерские longread'ы (Claude Desktop, без Cursor). Пробел — **узкий how-to для Cursor + остатки/обороты + выбор между OData и HTTP-расширением**, с чеклистом сверки и безопасности. Не конкурировать с B21 (CSV-папка без 1С).

---

## SERP (WebSearch Cursor, 19.08.2026)

Приоритет — живой WebSearch; `research-serp.json` (шаг 0) использован как черновик URL, дополнен результатами ниже.

### Главный запрос: `mcp 1с cursor финансы 2026`

| # | URL | Тип | Пробел для КОДА |
| --- | --- | --- | --- |
| 1 | https://koda-fd.ru/blog/mcp-cursor-finansist-instrumenty/ | RU how-to (B21) | Filesystem MCP, не прямой 1С — наш B80 = следующий уровень |
| 2 | https://blog.fin-academy.pro/mcp-servery-dlya-buhgalterii-1c | RU longread CFO | Claude Desktop, мало Cursor; много «что такое MCP» |
| 3 | https://infostart.ru/1c/articles/2712602/ | RU tech (INFATON) | Dev/админ аудитория; нет пошагового Cursor для финансиста |
| 4 | https://github.com/evilbruce666/1c-odata-mcp | OSS OData MCP | README сильный; нужен мост «финансист + Cursor + сверка» |
| 5 | https://github.com/infaton/MCP35 | OSS HTTP MCP | `get_balance` / `get_register_totals` — ядро B80 |
| 6 | https://shtruzel.ru/articles/cursor-dlya-1c-nastrojka-mcp-bsl-2026 | RU dev stack | BSL + metadata; не остатки для CFO |
| 7 | https://github.com/feenlace/mcp-1c | OSS Go MCP | 10 tools, execute_query SELECT — dev + данные |
| 8 | https://infostart.ru/1c/articles/2635907/ | RU (mcp-1c Go) | Разработка; упоминает execute_query к данным |
| 9 | https://aitools1c.dev/guides/mcp-server-dlya-1c/ | Каталог/обзор | Сравнение серверов, без сценария «остатки из Cursor» |
| 10 | https://glama.ai/mcp/servers/infaton/MCP35 | Каталог MCP | Спека tools, без fin workflow |

### Вторичный: `автоматизация финотдела MCP 1С Cursor 2026`

- Общие статьи про автоматизацию финансов (Oracle/SAP/Make) — **не наш intent**.
- https://koda-fd.ru/blog/ai-dlya-finansista-2026/ — AI-контур без MCP к 1С; линк как adjacent.
- https://mayai.ru/mcp-server-chto-eto-i-kak-nastroit-ego-rabotu-v-cursor-dlya-1s/ — setup MCP для 1С, dev-угол.

### H1: «Как подключить MCP к 1С: читать остатки и обороты прямо из Cursor»

Прямых статей с таким H1 нет. Ближайшие: fin-academy (бухгалтерия + MCP), INFATON Infostart (`get_balance`), 1c-odata-mcp (дебиторка/продажи). **Угол КОДА:** один вечер → Cursor → конкретные tools → сверка с ОСВ.

### Конкурентный зазор

1. **Финансист vs 1С-разработчик** — не BSL Pack и не YaXUnit; запрос «остатки по 41/62 за период» из чата Cursor.
2. **Два маршрута в одной статье** — OData (`1c-odata-mcp`) vs HTTP-расширение (`get_balance` / `get_register_totals`).
3. **Сверка как DoD** — не «подключили и верим», а 2–3 строки против отчёта 1С.
4. **Граница с B21/B13** — B21 = CSV; B13 = OData руками; B80 = MCP + natural language.
5. **152-ФЗ** — read-only user, env-секреты, обезличивание, без Auto-run записи.

---

## Таблица фактов (только с URL; для writer)

| # | Утверждение | Источник | Дата проверки |
| --- | --- | --- | --- |
| 1 | Model Context Protocol (MCP) — открытый протокол Anthropic для подключения AI к внешним инструментам и данным; анонс 25 ноября 2024. | https://www.anthropic.com/news/model-context-protocol | 2026-08-19 |
| 2 | INFATON MCP Server v2.1 — open-source MCP для 1С: **51 инструмент**; рост с 35 до 51 за ~месяц (апр–май 2026). | https://infostart.ru/1c/articles/2712602/ | 2026-08-19 |
| 3 | Tool `get_balance` — остатки и обороты **регистра бухгалтерии** (любой план счетов). | https://infostart.ru/1c/articles/2712602/ , https://github.com/infaton/MCP35 | 2026-08-19 |
| 4 | Tool `get_register_totals` — итоги **регистров накопления** (остатки/обороты). | https://infostart.ru/1c/articles/2712602/ | 2026-08-19 |
| 5 | INFATON MCP: платформа 1С **8.3.20+**; конфигурации ERP 2.5, Бухгалтерия 3.0, УТ 11, КА 2; транспорт HTTP (Basic Auth) + stdio Node.js proxy. | https://infostart.ru/1c/articles/2712602/ | 2026-08-19 |
| 6 | Пример вызова `get_balance` через HTTP JSON-RPC: параметры `account_code`, `period_from`, `period_to`. | https://glama.ai/mcp/servers/infaton/MCP35 | 2026-08-19 |
| 7 | **1c-odata-mcp** — MCP-сервер к 1С через **OData**; запуск `npx -y 1c-odata-mcp`; **только чтение по умолчанию**; запись — с предпросмотром и флагом. | https://github.com/evilbruce666/1c-odata-mcp | 2026-08-19 |
| 8 | 1c-odata-mcp: analytics tools — `read.analytics.get_debtors` (счёт 62), `get_inventory`, `get_sales`, `get_cashflow`; на стороне 1С нужен только опубликованный OData. | https://github.com/evilbruce666/1c-odata-mcp | 2026-08-19 |
| 9 | **feenlace/mcp-1c** — один Go-бинарник, **10 MCP-tools**, нулевые внешние зависимости; данные через HTTP-сервис расширения; `execute_query` — только SELECT. | https://github.com/feenlace/mcp-1c/blob/main/docs/getting-started.md | 2026-08-19 |
| 10 | Cursor: конфиг MCP — проектный `.cursor/mcp.json` или глобальный `~/.cursor/mcp.json`; после ручной правки — **перезапуск Cursor**. | https://cursor.com/ru/help/customization/mcp | 2026-08-19 |
| 11 | Cursor: Settings → Tools & MCP; hotkey `Ctrl+Shift+J` (Win/Linux), `Cmd+Shift+J` (Mac); Agent **запрашивает подтверждение** перед вызовом MCP-tool. | https://cursor.com/ru/help/customization/mcp | 2026-08-19 |
| 12 | feenlace рекомендует держать **~≤40 MCP-tools** суммарно по всем серверам в Cursor; mcp-1c — 10 tools. | https://github.com/feenlace/mcp-1c/blob/main/docs/getting-started.md | 2026-08-19 |
| 13 | HTTP-сервисы 1С штатно на платформе **8.3.10+**; ниже — HTTP-сервисы не поддерживаются (fin-academy, типовые гайды). | https://blog.fin-academy.pro/mcp-servery-dlya-buhgalterii-1c | 2026-08-19 |
| 14 | MCP INFATON построен на **JSON-RPC 2.0**; цепочка: Cursor → stdio proxy → HTTP POST `/hs/mcp/` → расширение .cfe. | https://infostart.ru/1c/articles/2712602/ | 2026-08-19 |
| 15 | Для публикации HTTP-сервиса расширения INFATON нужна публикация **«для расширения»** и установленный веб-сервер (комментарий Infostart Q&A). | https://infostart.ru/1c/articles/2712602/ | 2026-08-19 |
| 16 | 1c-odata-mcp: без OData на стороне 1С коннектор **не работает** (не использует COM/SQL напрямую). | https://github.com/evilbruce666/1c-odata-mcp | 2026-08-19 |
| 17 | mcp-1c (Go, infostart 2635907): один бинарник, работает с Claude Desktop, **Cursor**, Windsurf; нужен только HTTP-сервис 1С. | https://infostart.ru/1c/articles/2635907/ | 2026-08-19 |
| 18 | BSL Language Server поддерживает режим **Run in MCP mode** (отдельно от fin-data MCP). | https://1c-syntax.github.io/bsl-language-server/en/ | 2026-08-19 |

**Не использовать как факт без оговорки:** «экономия 40% времени финотдела» из generic SEO-статей; «800+ бухгалтеров» fin-academy; точные цены Claude Pro/API без сверки на день публикации; «Cursor 3.1» из сторонних блогов без официального источника; любые показы Wordstat; обещание «без программиста» если OData/HTTP не опубликованы.

**Fact-bank:** прямых фактов про MCP+1С+Cursor в `fact-bank.md` нет — опираться на таблицу выше. Контент-заводные цифры fact-bank к B80 **не тянуть**.

---

## Структура H2/H3 для writer (из карточки B80)

### H2: Когда это нужно финотделу (и когда нет)
- Нужно: повторяющиеся запросы к остаткам/оборотам, ad-hoc аналитика без XLS.
- Не нужно: нет OData/HTTP и нет админа; достаточно разовой выгрузки → B13/B21.
- Рекомендация: сначала проверить OData в браузере.

### H2: Подготовка данных и безопасность
- Read-only пользователь; env-секреты; Privacy Mode; линк `/obezlichivanie-dannyh-chatgpt-finansist/`.
- Таблица: OData path vs HTTP extension path.

### H2: Пошаговая настройка (два трека)
- **Трек A — OData:** включить OData → `npx -y 1c-odata-mcp` → `.cursor/mcp.json` → промпт дебиторка/продажи.
- **Трек B — HTTP (INFATON):** установить .cfe → опубликовать `/hs/mcp/` → `index.mjs` + env → промпт `get_balance`.
- Минимальные JSON-примеры без паролей в открытую.

### H2: Проверка результата и типичные ошибки
- DoD: сверка 2–3 строк с ОСВ; MCP Logs; красный индикатор (Node, URL, auth); 401/403; «галлюцинации» без tool call.

### H2: Что автоматизировать дальше
- `get_register_totals`, cashflow, связка с B21 (CSV fallback); B81 HTTP для своих приложений.
- Internal: `/avtomatizaciya-finansov-no-code/`, `/mcp-cursor-finansist-instrumenty/`.

---

## FAQ hints (ответы-действия)

| Вопрос | Направление ответа |
| --- | --- |
| Можно ли без программиста? | Если OData уже опубликован — да, через `1c-odata-mcp` + mcp.json. Если нужно ставить расширение и IIS — минимум админ базы. |
| Сколько займёт? | OData готов: 1–2 часа smoke-test. С нуля HTTP+расширение: вечер с админом (ориентир fin-academy «1–2 вечера» — оговорить зависимость от инфраструктуры). |
| Какие риски для данных? | Утечка через облачную модель (текст запроса + ответ tool); mitigations: read-only, обезличивание, локальная модель + OData MCP локально. |
| MCP = прямой SQL к 1С? | Нет. Только OData или HTTP-сервис; права пользователя 1С сохраняются. |
| Чем отличается от B21? | B21 читает CSV-папку; B80 — живая база 1С через MCP-tools. |

---

## Internal links

- `/mcp-cursor-finansist-instrumenty/` (B21)
- `/vygruzka-1c-excel-odata/` (B13)
- `/obezlichivanie-dannyh-chatgpt-finansist/`
- `/avtomatizaciya-finansov-no-code/` (из карточки)

---

## CTA (conversion-map)

| CTA | URL | Лимит |
| --- | --- | --- |
| Клуб KODA | https://club.koda-fd.ru/?utm_source=blog&utm_medium=article&utm_campaign=mcp-1c-cursor-ostatki-oboroty | ≤2 |
| Telegram | https://t.me/finance_modern?utm_source=blog&utm_medium=article | ≤2 |

**Запрещено:** `t.me/koda_salebot`, `@koda_salebot`.

---

## Источники исследования

- https://cursor.com/ru/help/customization/mcp
- https://infostart.ru/1c/articles/2712602/
- https://github.com/infaton/MCP35
- https://glama.ai/mcp/servers/infaton/MCP35
- https://github.com/evilbruce666/1c-odata-mcp
- https://github.com/feenlace/mcp-1c/blob/main/docs/getting-started.md
- https://infostart.ru/1c/articles/2635907/
- https://blog.fin-academy.pro/mcp-servery-dlya-buhgalterii-1c
- https://koda-fd.ru/blog/mcp-cursor-finansist-instrumenty/
- https://aitools1c.dev/guides/mcp-server-dlya-1c/
- https://www.anthropic.com/news/model-context-protocol
- WebSearch Cursor 2026-08-19; `research-serp.json` дополнен блоком `agent_websearch`
