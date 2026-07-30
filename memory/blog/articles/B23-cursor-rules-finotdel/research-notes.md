# Research notes — B23

**topic_id:** B23  
**slug:** cursor-rules-finotdel  
**h1:** Как настроить Cursor Rules для финотдела: стиль кода, папки и запрет сырых выгрузок 1С  
**research_date:** 2026-07-30  
**EXCALIBUR_RUN_DATE:** 2026-07-30  
**publish_target:** сайт koda-fd.ru/blog (+ Дзен по оркестрации)  
**utility_gate:** PASS (`how_to`, mode B) — подтверждено `excalibur_blog_utility_gate.py --topic-id B23`  
**related_published:** `/baza-znaniy-chatgpt-cursor-finotdel/` (B16), `/cursor-finansist-skript-dashbord/` (B20), `/mcp-cursor-finansist-instrumenty/` (B21), `/obezlichivanie-dannyh-chatgpt-finansist/` (B11)  
**freshness_window:** предпочитать источники после 2026-05-01; версии Cursor — актуальные на 2026-07-30

---

## utility_verdict

**PASS** — how_to, article_mode B.  
Читатель после статьи **создаёт** рабочий минимум: `AGENTS.md` + 1–3 `.mdc` в `.cursor/rules/`, фиксирует папки `data/`/`out/`, запрет сырых выгрузок 1С/ПДн в чат и Definition of Done.  
Не новость про Cursor 3.x, не каталог 100 community rules, не deep-dive hooks/skills.

---

## reader_outcome

Финдир/финменеджер за 30–45 минут закоммитит в git шаблон правил финотдела: агент знает стек (Python/Sheets), структуру папок, не предлагает коммитить сырые CSV из 1С и не тащит ПДн в промпт.

---

## action_outline

1. **Зачем rules, а не «каждый раз в чат»** — LLM не помнит прошлые сессии; rules = постоянный контекст в начале запроса (офиц. docs).
2. **Выбрать формат 2026** — минимум `AGENTS.md` в корне; для скоупа по файлам — `.cursor/rules/*.mdc` с frontmatter; legacy `.cursorrules` мигрировать и удалить.
3. **Создать правило** — Command Palette → «New Cursor Rule» **или** `/create-rule` в Agent **или** Customize → Rules → Add Rule.
4. **Минимум финотдела (alwaysApply)** — язык ответов, стек, папки `data/` / `out/` / `scripts/`, запрет: сырые выгрузки 1С в чат, коммит `data/**` с ПДн, секреты в коде.
5. **Scoped rules (globs)** — отдельно на `*.py` / `data/**` / `**/*.csv`: стиль кода, только обезличенные срезы, путь через MCP filesystem узкий.
6. **AGENTS.md + DoD** — стек, команды запуска, Definition of Done (gitignore, без ПДн, тест на малом файле).
7. **Проверка** — новый Agent-чат: «какие правила активны?»; тест-промпт «закоммить выгрузку из 1С» → отказ по правилам.
8. **Связь с базой знаний и MCP** — в rules сослаться на knowledge/ (B16) и узкий filesystem MCP (B21); обезличивание — B11.
9. **Команда** — один шаблон в git; Team Rules (Team/Enterprise) опционально для орг-запрета ПДн; без культа сложности (1 AGENTS + 2–4 mdc).

---

## Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT AUTH WARNING:** сервер MCP `user-mcp-kv` в этой сессии **не подключён** (Available servers: Cursor Automation Tools, cursor-cloud). Вызов `wordstat_get_top_requests` невозможен. Точные показы/мес **не получены** и **не выдуманы**.

Обновите доступ / токен Wordstat: https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

**Запросы для повторного сбора (когда MCP доступен):**

| Фраза | Показы в месяц |
| --- | --- |
| как настроить cursor rules | ⚠️ нет данных |
| agents.md cursor | ⚠️ нет данных |
| .cursorrules финансы | ⚠️ нет данных |
| правила cursor для команды | ⚠️ нет данных |
| .cursor/rules mdc | ⚠️ нет данных |

**LSI (экспертно, без объёмов — для копирайтера):** project rules cursor; alwaysApply; globs; AGENTS.md; User Rules; Team Rules; New Cursor Rule; `/create-rule`; миграция .cursorrules; запрет ПДн; выгрузка 1С.

**SEO-вывод:** RU-SERP занят общими дев-гайдами (Hexlet, mayai, neurinix, vibecoderz) и EN-сравнениями AGENTS.md vs CLAUDE.md. Угол КОДА: **финотдел + папки + запрет сырых 1С/ПДн** — в SERP по H1 конкурентов нет (result_count: 0 на 2026-07-30).

---

## SERP (WebSearch Курсора + research-serp.json, 30.07.2026)

### Primary: «как настроить cursor rules» / «… 2026»

| # | URL | Тип | Заметка для угла |
| --- | --- | --- | --- |
| 1 | https://cursor.com/docs/rules.md | official | Канон: 4 типа rules, mdc, AGENTS.md, Team, precedence |
| 2 | https://cursor.com/help/customization/rules | official help | UI создания, миграция .cursorrules, CLAUDE.md |
| 3 | https://cursor.com/ru/docs/rules | official RU | То же на русском |
| 4 | https://ru.hexlet.io/blog/posts/cursor-rules | competitor RU | Хороший how-to; стек web/React — не финансы |
| 5 | https://mayai.ru/cursor-rules-nastroyka-proekta/ | competitor RU | Новичок 20–40 мин; Active Rules чеклист |
| 6 | https://neurinix.com/2026/06/20/nastrojka-cursor-rules/ | competitor RU | 4 режима, чеклист 15 пунктов перед Git |
| 7 | https://vibecoderz.ru/blog/cursor-rules | competitor RU | alwaysApply/globs, ошибки новичка |
| 8 | https://insidepc.tech/ai/ai-guides/cursorrules-pravila-proekta-nastraivaem-cursor-svoy-stek | competitor RU | Сравнение форматов; грабли monorepo |
| 9 | https://www.morphllm.com/cursor-rules-best-practices | competitor EN | Best practices mdc 2026 |
| 10 | https://shtruzel.ru/articles/cursor-dlya-1c-nastrojka-mcp-bsl-2026 | adjacent | Cursor+1С BSL — рядом, но не финотдел/CSV |

### Secondary: agents.md cursor

| # | URL | Заметка |
| --- | --- | --- |
| 1 | https://cursor.com/docs/rules.md#agentsmd | Офиц.: plain markdown, nested, deeper wins |
| 2 | https://thepromptshelf.dev/blog/cursor-agents-md-complete-guide-2026/ | Setup guide |
| 3 | https://vibecoding.app/blog/agents-md-guide | AGENTS.md + .cursor/rules вместе |
| 4 | https://codersera.com/blog/agents-md-vs-claude-md-vs-cursor-rules-comparison-2026/ | Comparison 2026 |
| 5 | https://blog.buildbetter.ai/agents-md-vs-cursorrules-vs-claude-skills-2026-comparison/ | Migration framing |

### Secondary: правила cursor для команды

| # | URL | Заметка |
| --- | --- | --- |
| 1 | https://cursor.com/docs/rules.md (Team Rules) | Dashboard, Enforce, precedence Team→Project→User |
| 2 | https://cursor.com/dashboard/team-content | UI управления Team Rules |
| 3 | https://khar-ag.ru/docs/cursor-rules-guide/ | RU: User/Project/.mdc |
| 4 | https://habr.com/ru/amp/publications/1044774/ | Обзор Cursor 2026 (широкий) |

### Gap

Полный H1 «…для финотдела… запрет сырых выгрузок 1С» — **0 результатов** в research-serp (2026-07-30). Практический угол свободен.

### Gaps конкурентов (наш дифференциатор)

- Нет шаблона папок `data/` / `out/` под выгрузки 1С → Excel/Sheets  
- Нет явного запрета сырых выгрузок и ПДн в Agent  
- Нет связки rules ↔ база знаний (B16) ↔ MCP (B21) ↔ обезличивание (B11)  
- Team Rules упоминают редко; для SMB финотдела достаточно git-шаблона

---

## Таблица фактов (проверено 2026-07-30)

| # | Утверждение | Источник | Дата проверки |
| --- | --- | --- | --- |
| 1 | Cursor поддерживает 4 типа rules: Project, User, Team, AGENTS.md | https://cursor.com/docs/rules.md | 2026-07-30 |
| 2 | Project rules — файлы `.mdc` в `.cursor/rules/`, версионируются в git | https://cursor.com/docs/rules.md | 2026-07-30 |
| 3 | Обычный `.md` в `.cursor/rules` **игнорируется** (нет frontmatter) | https://cursor.com/docs/rules.md | 2026-07-30 |
| 4 | Четыре режима: Always / Apply Intelligently / globs / Manual `@` | https://cursor.com/docs/rules.md | 2026-07-30 |
| 5 | Frontmatter: `alwaysApply`, `description`, `globs` задают поведение | https://cursor.com/docs/rules.md | 2026-07-30 |
| 6 | Создание: `/create-rule` в Agent или Customize → Rules → Add Rule; также Command Palette «New Cursor Rule» | https://cursor.com/docs/rules.md · https://cursor.com/help/customization/rules | 2026-07-30 |
| 7 | Рекомендация: правила < 500 строк; дробить на модульные | https://cursor.com/docs/rules.md | 2026-07-30 |
| 8 | `AGENTS.md` — plain markdown без frontmatter; альтернатива `.cursor/rules` | https://cursor.com/docs/rules.md | 2026-07-30 |
| 9 | Nested `AGENTS.md` в подпапках; более специфичные инструкции приоритетнее | https://cursor.com/docs/rules.md | 2026-07-30 |
| 10 | `.cursorrules` в корне — legacy, будет deprecated; мигрировать в Always Apply mdc и удалить | https://cursor.com/help/customization/rules | 2026-07-30 |
| 11 | User Rules — локально в Customize; только Agent (Chat), не Tab и не Inline Edit (Cmd/Ctrl+K) | https://cursor.com/docs/rules.md · help | 2026-07-30 |
| 12 | Team Rules — планы Team/Enterprise; dashboard; Enforce; precedence: Team → Project → User | https://cursor.com/docs/rules.md | 2026-07-30 |
| 13 | Team Rules: free-form text; поддерживают glob; AI guidance ≠ единственный security control | https://cursor.com/docs/rules.md | 2026-07-30 |
| 14 | Cursor читает `CLAUDE.md` как `AGENTS.md`; CLAUDE.md всегда в каждом разговоре | https://cursor.com/help/customization/rules | 2026-07-30 |
| 15 | Rules не влияют на Cursor Tab и другие AI-фичи кроме Agent | https://cursor.com/docs/rules.md FAQ | 2026-07-30 |
| 16 | Содержимое rules добавляется в начало контекста модели | https://cursor.com/docs/rules.md | 2026-07-30 |
| 17 | База знаний финотдела — соседний гайд B16 | https://koda-fd.ru/blog/baza-znaniy-chatgpt-cursor-finotdel/ | 2026-07-30 |
| 18 | MCP-инструменты для финансиста — B21 | https://koda-fd.ru/blog/mcp-cursor-finansist-instrumenty/ | 2026-07-30 |
| 19 | Обезличивание данных — B11; не дублировать длинно | https://koda-fd.ru/blog/obezlichivanie-dannyh-chatgpt-finansist/ | 2026-07-30 |
| 20 | Скрипт/дашборд пилот — B20 | https://koda-fd.ru/blog/cursor-finansist-skript-dashbord/ | 2026-07-30 |

**fact-bank.md:** прямых строк про Cursor Rules нет — опираться на официальные URL выше; цифры Wordstat не использовать.

---

## Рекомендуемый каркас статьи (для writer)

**H1:** Как настроить Cursor Rules для финотдела: стиль кода, папки и запрет сырых выгрузок 1С

**H2 (из карточки + action_outline):**
1. Зачем rules, если «и так понятно из чата»
2. Форматы 2026: `.mdc` / `AGENTS.md` / legacy `.cursorrules`
3. Минимальный набор правил финотдела: папки, CSV, запрет ПДн и сырых 1С
4. Пример `AGENTS.md` + 2–3 `.mdc` (alwaysApply security + globs)
5. Проверка: Active Rules и тест-промпт
6. Связь с базой знаний и MCP
7. Внедрение в команду: один шаблон в git (Team Rules — опционально)

**CTA ≤ 3:** база знаний; MCP; обезличивание — без подмены пользы.

---

## FAQ hints

1. **Free тариф?** — Project rules / AGENTS.md — функция продукта; лимиты Agent зависят от плана (сверять pricing.cursor.com, не выдумывать цифры).
2. **Vs system prompt / User Rules?** — User Rules глобальны на машине; Project Rules в репо и шарятся через git.
3. **Нужны ли одному человеку?** — Да: меньше повторов и меньше «агент предложил закоммитить data/».
4. **Сколько rules?** — 1 AGENTS.md + 2–4 mdc; не 40 файлов в день 1.
5. **Работают ли всегда?** — Модель может игнорировать; критичное дублировать `.gitignore` / права доступа / хуки.
6. **Связь с MCP?** — В rules: «читай data/ только через filesystem MCP, path узкий» (B21).
7. **`.cursorrules` удалять?** — После миграции в Always Apply mdc — да; не держать оба формата.
8. **Team Rules обязательны?** — Нет для старта; достаточно git. Team — если нужен Enforce орг-запрета ПДн.

---

## Cover hint

abstract rule-grid nodes locked paths holographic dark purple, no text

---

## Writer constraints

- Язык: русский; тон — практика для финотдела, не senior-dev jargon без расшифровки  
- Цифры спроса Wordstat — **не писать** (нет API)  
- Не копировать структуру Hexlet/mayai 1:1  
- Обязательные примеры файлов: фрагменты `AGENTS.md`, `security.mdc` (alwaysApply), `python-data.mdc` (globs)  
- workflow-схема: `чат-хаос → AGENTS.md + .mdc → git → проверка Agent → команда`  
- Дата/год в тексте: 2026; не «2024/2025 как актуальный год»
