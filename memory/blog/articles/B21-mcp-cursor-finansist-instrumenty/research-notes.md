# Research notes — B21

**topic_id:** B21  
**slug:** mcp-cursor-finansist-instrumenty  
**h1:** MCP в Cursor: как подключить инструменты и перестать копировать CSV руками  
**research_date:** 2026-07-22  
**publish_target:** сайт koda-fd.ru/blog (+ Дзен по оркестрации)  
**utility_gate:** PASS (`how_to`, mode B)  
**related_published:** `/cursor-finansist-skript-dashbord/` (B20), `/cursor-ai-agenty-finotchetnost/`  
**sibling_queue:** B20 (скрипт+дашборд), B23 (Cursor Rules)

---

## utility_verdict

**PASS** — тема utility-only how_to. Читатель получает рабочий маршрут: понять MCP без дев-жаргона; выбрать первый стек под финотдел (файлы / браузер / таблицы, без «магии 1С»); подключить сервер в Cursor (Marketplace или `mcp.json`); проверить зелёный статус и вызов tool из Agent; прогнать сценарий «агент читает папку выгрузок → собирает отчёт»; зафиксировать риски прав, секретов и ПДн. Не новость про MCP Apps, не топ-50 серверов для джуниор-дева, не туториал «напиши свой MCP с нуля».

---

## reader_outcome

После гайда финансист сможет в Cursor подключить минимум один MCP-сервер (файлы/браузер), подтвердить вызов инструмента в Agent и заставить агента собрать отчёт по папке CSV-выгрузок без ручного копипаста содержимого файлов в чат.

---

## action_outline

1. **Зафиксировать боль и DoD** — сейчас: копируешь куски CSV в чат / `@файл` по одному. Цель: агент сам читает папку `data/` (или указанный путь) через MCP-tool и выдаёт summary + расхождения / список файлов.
2. **Выбрать первый сервер под финотдел** — старт: filesystem (чтение локальной папки выгрузок) и/или browser (проверка localhost-дашборда). Не GitHub/Figma/Kubernetes в день 1. Не «подключить 1С напрямую через MCP» — это другой контур (OData / HTTP-сервис).
3. **Подключить через UI** — Settings → Tools & MCP (`Ctrl+Shift+J` / `Cmd+Shift+J`) → Add to Cursor / Marketplace; пройти OAuth/ключ если просят. Альтернатива: проектный `.cursor/mcp.json` или глобальный `~/.cursor/mcp.json` (Windows: `%USERPROFILE%\.cursor\mcp.json`).
4. **Проверить статус** — зелёный индикатор в Tools & MCP; при ошибке — Output → MCP Logs; при ручном JSON — перезапуск Cursor / Reload Window.
5. **Тестовый вызов tool** — в Agent явно: «перечисли файлы в `data/` через MCP» / «прочитай заголовки всех CSV в папке»; подтвердить allow tool (по умолчанию Agent спрашивает).
6. **Рабочий сценарий отчёта** — промпт с DoD: список файлов → схема колонок → свод (кол-во строк, сумма ключевого поля, дубли ключей) → `out/report.md` или краткий ответ в чате. Без «перепиши весь проект».
7. **Секреты и границы** — ключи только в `env` / `${env:VAR}` / UI, не в git; `.env` в `.gitignore`; filesystem MCP — только узкая папка выгрузок, не весь диск C; сырые ПДн не в облачные MCP.
8. **Чеклист безопасности** — что нельзя: боевые пароли 1С в mcp.json, полный дамп базы, токены в коммите, Auto-run всех tools без понимания. Privacy Mode при необходимости (линк B20 / обезличивание).
9. **Куда расти** — rules/AGENTS.md (B23); скрипт+дашборд без MCP уже есть (B20); свой кастомный MCP — только после 2–3 рабочих готовых серверов.

---

## Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT AUTH WARNING:** сервер MCP `user-mcp-kv` в этой сессии **не подключён** (в каталоге MCP нет инструментов `wordstat_*`). Точные показы/мес **не получены** и **не выдуманы**. Обновите токен / подключите MCP-KV: https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

**Экспертная семантика (без цифр спроса) — LSI для копирайтера:**

| Кластер | Фразы (использовать осмысленно) | Роль |
| --- | --- | --- |
| Primary | mcp cursor, cursor mcp, mcp в cursor | H1/лид; бренд+протокол |
| Protocol | model context protocol, модель контекст протокол | H2 «простыми словами»; 1 раз расшифровка |
| Setup RU | подключить mcp cursor, настроить mcp cursor, mcp.json cursor | H2 пошагово |
| Beginner | mcp сервер для начинающих, что такое mcp сервер | FAQ + лид без «создай сервер с нуля» |
| Tools | cursor tools mcp, marketplace mcp, add to cursor | UI-шаги |
| Fin angle | mcp финансист, csv cursor mcp, папка выгрузок агент | Уникальный угол КОДА |
| Adjacent | filesystem mcp, browser mcp, секреты mcp.json | H2 риски / первый стек |

**SEO-вывод:** SERP по `mcp cursor` / «подключить mcp» забит гайдами для разработчиков (топ серверов GitHub/Context7/Playwright, «собери свой MCP»). Угла «финансист + CSV-выгрузки + перестать копировать руками» почти нет. В H1/лиде держать связку «MCP + Cursor + инструменты + CSV без копипаста», не конкурировать лобовым «топ-10 MCP 2026».

---

## SERP (WebSearch Cursor, 22.07.2026)

Приоритет — живой WebSearch; `research-serp.json` (шаг 0) полезен как черновик URL, но сниппеты местами перепутаны между результатами — **перепроверять по живому поиску и официальным docs**.

### Главный запрос: `mcp cursor`

| # | URL | Тип | Пробел для КОДА |
| --- | --- | --- | --- |
| 1 | https://cursor.com/docs/mcp | Официальный reference MCP | Нет сценария финансист/CSV |
| 2 | https://cursor.com/help/customization/mcp | Help: one-click + mcp.json + approvals | Канон шагов; нет финугла |
| 3 | https://developertoolkit.ai/en/cursor-ide/quick-start/mcp-setup/ | EN setup, DB/GitHub примеры | Dev-стек, не выгрузки |
| 4 | https://stackmcp.dev/blog/setup-mcp-servers-cursor | stdio vs URL, пути Windows | Полезно для FAQ путей |
| 5 | https://serenitiesai.com/articles/mcp-server-cursor-setup-2026 | EN 2026: transports stdio/SSE/HTTP | Слишком engineering |
| 6 | https://shtruzel.ru/articles/mcp-v-cursor-podklyuchenie-i-luchshie-servery-2026 | RU: Cursor 3.1, Marketplace, топ-10 | Конкурент по setup; угол — дев-серверы |

### Вторичные

- **`model context protocol cursor`** — cursor.com/docs/mcp, TrueFoundry «best MCP for Cursor», Medium (июль 2026) architecture. Паттерн: USB-C для AI, Host/Client/Server. Нет CFO-языка.
- **`mcp сервер для начинающих`** — mcpdoc.ru quickstart, Habr Raft «MCP для новичков», FastMCP Hello World, «создай сервер с нуля». **Анти-угол для нас:** не учить писать сервер; учить **подключить готовый** под папку выгрузок.
- **`подключить mcp cursor`** — cursor.com/ru/help/customization/mcp (канон), mayai.ru/podklyuchenie-mcp-cursor/, vibecoderz (Cursor+Claude), Habr OTUS (Google Trends MCP). Сильный how-to слой; все про девов/контент-завод, не про сверку CSV.

### Конкурентный зазор (угол КОДА)

1. **Финансист, не junior-dev** — MCP = «розетки», чтобы агент сам читал папку выгрузок, а не «ещё 12 серверов для GitHub».
2. **Первый стек узкий:** файлы → (опционально) браузер для localhost → таблицы; явно сказать «не 1С по MCP в день 1».
3. **Граница с B20:** B20 = скрипт+дашборд руками/`@файл`; B21 = те же данные, но tool вызывает агент без копипаста CSV в чат.
4. **Безопасность 152-ФЗ** — узкий path filesystem, секреты вне git, подтверждение tool, линк `/obezlichivanie-dannyh-chatgpt-finansist/`.
5. **Не писать свой MCP** — отложить; конкуренты уже закрыли «Hello World FastMCP».

---

## Таблица фактов (только с URL; для writer)

| # | Утверждение | Источник | Дата проверки |
| --- | --- | --- | --- |
| 1 | MCP (Model Context Protocol) подключает Cursor к внешним инструментам и источникам данных (БД, API, сервисы вроде GitHub/Linear/Notion). | https://cursor.com/help/customization/mcp | 2026-07-22 |
| 2 | MCP-сервер экспонирует tools/data Cursor через протокол; Agent может вызывать tools прямо в чате. | https://cursor.com/help/customization/mcp | 2026-07-22 |
| 3 | One-click установка: Settings → Tools & MCP → Add to Cursor (+ auth при необходимости). Hotkeys: `Cmd+Shift+J` (Mac), `Ctrl+Shift+J` (Win/Linux). | https://cursor.com/help/customization/mcp | 2026-07-22 |
| 4 | Ручная установка: файл `mcp.json` — проектный `.cursor/mcp.json` (шарить с командой через git) или глобальный `~/.cursor/mcp.json`. | https://cursor.com/help/customization/mcp | 2026-07-22 |
| 5 | Оба конфига мержатся; при одинаковом имени сервера приоритет у **проектного**. | https://cursor.com/help/customization/mcp | 2026-07-22 |
| 6 | Локальный сервер: блок `command` / `args` / `env` (пример `npx -y mcp-server`). | https://cursor.com/help/customization/mcp | 2026-07-22 |
| 7 | Удалённый сервер: поле `url` (+ опционально `headers` с Bearer-токеном). | https://cursor.com/help/customization/mcp | 2026-07-22 |
| 8 | После ручного сохранения `mcp.json` официальный help указывает **перезапустить Cursor**. | https://cursor.com/help/customization/mcp | 2026-07-22 |
| 9 | Agent подхватывает MCP tools автоматически; tools можно включать/выключать в списке вверху чата. | https://cursor.com/help/customization/mcp | 2026-07-22 |
| 10 | По умолчанию Agent **спрашивает approval** перед вызовом MCP tool. | https://cursor.com/help/customization/mcp | 2026-07-22 |
| 11 | С Cursor **3.6+** режим Auto-review (Settings → Agents → Approvals & Execution): allowlisted tools могут идти сразу, остальное — через safety classifier; есть режим Allowlist. Детали — `permissions.json`. | https://cursor.com/help/customization/mcp | 2026-07-22 |
| 12 | Cursor поддерживает расширение **MCP Apps** (интерактивный UI от tool в чате); без UI tool всё равно работает обычным ответом. | https://cursor.com/help/customization/mcp | 2026-07-22 |
| 13 | Cloud Agents: MCP настраиваются в Cloud Agents dashboard; на Team — shared servers в Dashboard → Integrations & MCP / Team Marketplace. | https://cursor.com/help/customization/mcp | 2026-07-22 |
| 14 | Каталоги: Cursor Marketplace (официальные, one-click); community — cursor.directory. | https://cursor.com/help/customization/mcp | 2026-07-22 |
| 15 | Troubleshooting: Output → MCP Logs; toggle сервера в Tools & MCP; remove+re-add; env из shell profile должны быть видны Cursor (после правки профиля — рестарт). | https://cursor.com/help/customization/mcp | 2026-07-22 |
| 16 | На Windows глобальный путь часто описывают как `%USERPROFILE%\.cursor\mcp.json`. | https://stackmcp.dev/blog/setup-mcp-servers-cursor | 2026-07-22 |
| 17 | Практический RU-гайд: настройка 15–30 мин; два пути — Tools & MCP или mcp.json; Agent по умолчанию подтверждает tool. | https://mayai.ru/podklyuchenie-mcp-cursor/ | 2026-07-22 |
| 18 | Смысл MCP vs «просто прикрепить файл»: агент сам вызывает tool за свежими/множественными данными вместо ручного копипаста контекста в чат (паттерн из Habr OTUS). | https://habr.com/ru/companies/otus/articles/1031434/ | 2026-07-22 |
| 19 | Filesystem MCP видит только то, к чему дан доступ (путь); GitHub MCP — в пределах прав токена (типовая формулировка RU-гайдов; сверять с конкретным сервером). | https://shtruzel.ru/articles/mcp-v-cursor-podklyuchenie-i-luchshie-servery-2026 | 2026-07-22 |
| 20 | Pro на cursor.com/pricing включает MCP/skills/hooks в составе индивидуального тарифа (для FAQ «бесплатно ли» — сверять актуальный pricing; Hobby с лимитами Agent). | https://cursor.com/pricing | 2026-07-22 |

**Не использовать как факт без оговорки:** «с февраля 2026 Marketplace без рестарта» из сторонних блогов (UI плавает); CVE/баги конкретных npm-пакетов без первоисточника; «MCP = прямой доступ к 1С»; любые показы Wordstat; цены клуба KODA; обещание «подключи 50 серверов за 5 минут».

**Fact-bank:** прямых фактов про MCP/Cursor в `fact-bank.md` нет — опираться на таблицу выше + официальные URL. Контент-заводные цифры fact-bank к B21 **не тянуть**.

---

## Структура H2/H3 для будущей статьи (спека для writer)

Следовать карточке B21; ниже — наполнение.

### H2: MCP простыми словами: зачем это финансисту, а не только разработчику
- Аналогия: «розетка» / USB-C для инструментов агента.
- Без MCP: копипаст CSV / много `@файл`. С MCP: tool читает папку / ходит во внешний сервис.
- Рекомендация: сначала готовый сервер под файлы, не писать свой.

### H2: Что подключать первым: файлы, браузер, таблицы — без «магии 1С»
- Таблица выбора: задача → тип MCP → чего ждать.
- Явно: 1С ≠ MCP day-1; OData/HTTP — другие статьи.
- Рекомендация: 1–2 сервера максимум на пилоте.

### H2: Пошагово: установить MCP в Cursor и проверить вызов инструмента
- UI: Tools & MCP → Add to Cursor.
- JSON: пример минимального `mcpServers` без секретов в открытую.
- Проверка: зелёный статус + тестовый промпт + approve tool.
- Troubleshooting: MCP Logs.

### H2: Рабочий сценарий: агент читает папку выгрузок и собирает отчёт
- Промпт-шаблон с DoD (файлы, колонки, свод, out/).
- Связка с артефактами B20 (та же `data/`), без дубля «как написать pandas».
- Рекомендация: один сценарий отчёта, не «агент сам решит архитектуру».

### H2: Риски: права доступа, секреты в `.env`, что нельзя отдавать серверу
- Чеклист: path scope, env, gitignore, confirmation tools, ПДн.
- Auto-review / allowlist — осторожно включать.
- Линк обезличивание + Privacy Mode.

### Блок «Что дальше» + FAQ
- Internal: `/cursor-finansist-skript-dashbord/`, `/cursor-ai-agenty-finotchetnost/` (+ B23 rules когда live).
- CTA: club.koda-fd.ru + t.me/finance_modern (≤2 каждый; **без** salebot).

---

## Риски и оговорки для writer

- Не писать «полный каталог MCP 2026» / топ-10 дев-серверов — каннибализация и режим A-ish.
- Не учить создавать MCP-сервер с нуля (это secondary «для начинающих» у конкурентов; наш beginner = подключить).
- Не обещать прямой MCP к боевой 1С.
- Не вставлять Wordstat-цифры.
- Длинное тире «—» запрещено в article.html; кавычки прямые `"`.
- Эмодзи в тексте статьи — нет.
- Цены клуба не выдумывать; CTA только conversion-map.
- Автор: `olga-kondratskaya`; голос КОДА.
- UI Cursor 3.x плавает — описывать действия («открой Tools & MCP», «подтверди tool»), не пиксели сторонних скринов.
- Не дублировать B20 (скрипт сверки/Streamlit) — только мост «те же CSV, другой способ доступа».

---

## Internal links

- `/cursor-finansist-skript-dashbord/`
- `/cursor-ai-agenty-finotchetnost/`
- (опционально) `/obezlichivanie-dannyh-chatgpt-finansist/` — блок безопасности
- (когда B23 live) `/cursor-rules-finotdel/`

---

## FAQ hints (ответы-действия)

| Вопрос | Направление ответа |
| --- | --- |
| MCP это доступ к 1С напрямую? | Нет. MCP даёт tools агенту (файлы, API, браузер). К 1С — отдельно: OData / HTTP-сервис / выгрузка CSV в папку, которую читает filesystem MCP. |
| Бесплатно ли? | Протокол открытый; клиент — Cursor. Старт с тарифа Hobby с лимитами Agent; стабильная агентная работа + MCP обычно на Pro — сверить https://cursor.com/pricing. Сами community-серверы часто free, но могут просить API keys сторонних сервисов. |
| Чем лучше просто прикрепить файл? | Один файл — хватит `@`. Много файлов / повторные прогоны / свежие данные с диска или API — MCP, чтобы не копипастить. Для разовой сверки двух CSV см. B20. |
| Куда писать конфиг на Windows? | Проект: `.cursor/mcp.json` в корне папки. Глобально: `%USERPROFILE%\.cursor\mcp.json`. Секреты — в env, не в git. |
| Почему сервер красный/серый? | Output → MCP Logs; проверить Node/`npx`/путь; env видны ли Cursor; remove+re-add; рестарт после правки JSON. |
| Нужно ли разрешать Auto-run всех tools? | На пилоте — нет. Оставлять confirmation; allowlist только понятным read-only tools. |

---

## CTA (conversion-map)

| CTA | URL | Лимит |
| --- | --- | --- |
| Клуб KODA | https://club.koda-fd.ru/?utm_source=blog&utm_medium=article&utm_campaign=mcp-cursor-finansist-instrumenty | ≤2 |
| Telegram | https://t.me/finance_modern?utm_source=blog&utm_medium=article | ≤2 |

**Запрещено:** `t.me/koda_salebot`, `@koda_salebot`.

---

## Источники исследования

- https://cursor.com/docs/mcp , https://cursor.com/help/customization/mcp , https://cursor.com/ru/help/customization/mcp , https://cursor.com/pricing
- https://mayai.ru/podklyuchenie-mcp-cursor/
- https://vibecoderz.ru/blog/kak-podklyuchit-mcp-server-k-cursor-i-claude
- https://shtruzel.ru/articles/mcp-v-cursor-podklyuchenie-i-luchshie-servery-2026
- https://habr.com/ru/companies/otus/articles/1031434/
- https://stackmcp.dev/blog/setup-mcp-servers-cursor
- https://serenitiesai.com/articles/mcp-server-cursor-setup-2026
- https://mcpdoc.ru/reference/quickstart/ (конкурент «свой сервер» — знать, но не копировать угол)
- `memory/brief/fact-bank.md`, `conversion-map.md`, карточка B21 в `blog-topics.md`
- WebSearch Cursor 2026-07-22; `research-serp.json` как черновик шага 0 (сниппеты сверять)
