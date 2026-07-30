# Research notes — B23

**topic_id:** B23  
**slug:** cursor-rules-finotdel  
**h1:** Как настроить Cursor Rules для финотдела: стиль кода, папки и запрет сырых выгрузок 1С  
**research_date:** 2026-07-30  
**EXCALIBUR_RUN_DATE:** 2026-07-30  
**publish_target:** сайт koda-fd.ru/blog (+ Дзен по оркестрации)  
**utility_gate (shell):** PASS (`how_to`, mode B) — подтверждено `python3 scripts/excalibur_blog_utility_gate.py --topic-id B23`  
**related_published:** `/baza-znaniy-chatgpt-cursor-finotdel/`, `/cursor-finansist-skript-dashbord/`, `/mcp-cursor-finansist-instrumenty/`, `/obezlichivanie-dannyh-chatgpt-finansist/`

---

## utility_verdict

**PASS** — how_to, article_mode B. Практический угол: читатель настраивает минимальный набор Cursor Rules под финотдел (папки `data/`/`out/`, стиль скриптов, запрет сырых выгрузок 1С и ПДн в чат), проверяет Active Rules и коммитит шаблон в git. Не новость про релиз Cursor, не каталог community rules, не deep-dive Skills/Hooks.

---

## reader_outcome

После гайда финдир/финменеджер создаст в репозитории `AGENTS.md` и 2–3 файла `.cursor/rules/*.mdc` (alwaysApply: безопасность + папки; globs: `*.py` / `data/**`), проверит срабатывание в Agent и зафиксирует Definition of Done так, чтобы агент не предлагал коммитить сырые CSV/Excel из 1С и не тащил ПДн в промпт.

---

## action_outline

1. **Зачем rules, а не копипаст в чат** – LLM не помнит прошлые ответы; project rules добавляются в начало контекста Agent каждый раз (официальные docs Cursor).
2. **Выбрать формат 2026** – основной: `.cursor/rules/*.mdc` с YAML frontmatter; простой старт: корневой `AGENTS.md`; legacy `.cursorrules` – мигрировать, не заводить новый.
3. **Зафиксировать каркас папок финотдела** – `data/raw/` (сырые выгрузки, в `.gitignore`), `data/clean/` (обезличенные срезы), `out/` (отчёты/дашборды), `scripts/` – и прописать это в alwaysApply-правиле.
4. **Создать security.mdc (alwaysApply: true)** – запрет: вставлять в чат сырые выгрузки 1С с ФИО/ИНН/телефонами; коммитить `data/raw/`; хардкодить логины OData; ссылка на регламент обезличивания (B11).
5. **Добавить 1–2 scoped rules** – `scripts-python.mdc` (`globs: **/*.py`) стиль и DoD; опционально `data-csv.mdc` (`globs: data/**/*.csv,data/**/*.xlsx`) – только обезличенные колонки, без ПДн.
6. **Прописать короткий AGENTS.md** – стек (Python / Apps Script / Sheets), язык ответов RU, Definition of Done (diff глазами, нет секретов в git, тест на малом CSV).
7. **Проверить срабатывание** – Customize → Rules; новый Agent-чат «какие правила активны?» / Active Rules; тест-промпт «предложи коммит data/raw/выписка.xlsx» – агент должен отказать.
8. **Связать с соседними гайдами** – база знаний (B16), скрипт/дашборд (B20), MCP filesystem с узким path (B21); rules = стиль и запреты, MCP = инструменты.
9. **Внедрить в команду** – закоммитить `.cursor/rules/` + `AGENTS.md`; Team Rules только на Team/Enterprise и только для org-wide compliance; не плодить 40 alwaysApply в день 1.

---

## Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT AUTH WARNING:** сервер MCP `user-mcp-kv` в этой сессии **не подключён** (в каталоге MCP нет `wordstat_*`). Точные показы/мес **не получены через API** и **не выдуманы**. Обновите токен / подключите MCP-KV: https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

**Вторичная оценка спроса (не наша выгрузка API):** конкурент mayai.ru указывает со ссылкой на Яндекс Вордстат от 22.06.2026: «cursor rules» – 248 показов/мес; «как настроить cursor» – 186; «cursor rules 1c» – 34; «cursor ai rules» – 9. Использовать в тексте **только с оговоркой источника** или после свежей выгрузки Wordstat.

**LSI для копирайтера:** как настроить cursor rules; cursor rules; .cursor/rules; .mdc; agents.md cursor; .cursorrules; project rules; правила cursor для команды; alwaysApply; globs; Active Rules; cursor rules 1с; запрет ПДн; сырая выгрузка 1С.

**SEO-вывод:** SERP заполнен дев-гайдами (React/Next/HTML). Дифференциатор КОДА: **финотдел + папки данных + запрет сырых выгрузок 1С/ПДн**, не React conventions.

---

## SERP summary (WebSearch Курсора, 2026-07-30)

Игнорируем утиный `research-serp.json` как вторичный; ниже – живой SERP.

### primary: «как настроить cursor rules» / «cursor rules 2026»

| # | URL | Угол конкурента | Пробел для КОДА |
| --- | --- | --- | --- |
| 1 | https://cursor.com/docs/rules | Официальная docs: типы rules, frontmatter, AGENTS.md, Team Rules | Нет сценария финотдела / 1С / ПДн |
| 2 | https://cursor.com/ru/docs/rules | То же на RU | То же |
| 3 | https://ru.hexlet.io/blog/posts/cursor-rules | Сильный how-to: 4 режима, миграция с .cursorrules, ошибки alwaysApply | Стек React/TS, не финансы |
| 4 | https://mayai.ru/cursor-rules-nastroyka-proekta/ | Пошагово для новичка, Active Rules, Wordstat-цифры | Лендинг/HTML; не data/1С |
| 5 | https://www.morphllm.com/cursor-rules-best-practices | EN best practices MDC 2026 | Нет RU-аудитории CFO |
| 6 | https://vibecoderz.ru/blog/cursor-rules | 20–40 мин setup, миграция legacy | Общий vibe-coding |
| 7 | https://shtruzel.ru/articles/cursor-dlya-1c-nastrojka-mcp-bsl-2026 | Cursor + 1С BSL / MCP | Разработка на BSL, не финотчётность/CSV |

### secondary: agents.md / команда / финансы

| Запрос | Что в выдаче | Вывод |
| --- | --- | --- |
| agents.md cursor | Docs Cursor + сравнения AGENTS.md vs .mdc vs CLAUDE.md | В статье: AGENTS.md = простой always-on; mdc = globs/режимы |
| правила cursor для команды | Team Rules (dashboard), git-commit project rules | Для малого финотдела хватит git; Team – опция |
| .cursorrules финансы / 1С | onerpa, anoda-tech/cursor_rules_1c, shtruzel | Конкуренты про BSL-разработку; наш угол – **данные и запреты**, не синтаксис BSL |

**Угол статьи (utility):** «за 1 вечер собрать 3 файла правил, чтобы агент не слил выписку 1С в чат и не закоммитил raw CSV» – checklist + готовые фрагменты mdc/AGENTS.md.

---

## Таблица фактов (проверено 2026-07-30)

| # | Утверждение | Источник | Дата проверки | В текст |
| --- | --- | --- | --- | --- |
| 1 | Cursor поддерживает 4 типа правил: Project, User, Team, AGENTS.md. | https://cursor.com/docs/rules | 2026-07-30 | да |
| 2 | Project rules хранятся в `.cursor/rules` как `.mdc`, версионируются с репо; область – globs / manual / relevance. | https://cursor.com/docs/rules | 2026-07-30 | да |
| 3 | Обычный `.md` в `.cursor/rules` **игнорируется** системой правил (нет frontmatter). Для plain markdown – `AGENTS.md`. | https://cursor.com/docs/rules | 2026-07-30 | да |
| 4 | Четыре режима project rule: Always Apply; Apply Intelligently (по `description`); Apply to Specific Files (`globs`); Apply Manually (`@rule`). | https://cursor.com/docs/rules | 2026-07-30 | да |
| 5 | Матрица frontmatter: `alwaysApply: true` → всегда; `false` + globs → auto-attach; `false` + description без globs → agent-requested; `false` без description/globs → только `@`. | https://cursor.com/docs/rules | 2026-07-30 | да |
| 6 | Создать правило: `/create-rule` в Agent или Customize → Rules → Add Rule. | https://cursor.com/docs/rules | 2026-07-30 | да |
| 7 | Рекомендация docs: держать правило короче 500 строк; дробить на модульные; избегать копипаста style guide целиком. | https://cursor.com/docs/rules | 2026-07-30 | да |
| 8 | Rules **не** влияют на Cursor Tab и не применяются к Inline Edit (Cmd/Ctrl+K); User Rules – только Agent (Chat). | https://cursor.com/docs/rules (FAQ) | 2026-07-30 | да |
| 9 | `AGENTS.md` – plain markdown без метаданных; поддержка в корне и подпапках; nested комбинируются, более специфичные приоритетнее. | https://cursor.com/docs/rules#agentsmd | 2026-07-30 | да |
| 10 | Team Rules: планы Team/Enterprise; дашборд; приоритет **Team → Project → User**; могут быть enforced. | https://cursor.com/docs/rules | 2026-07-30 | да |
| 11 | Legacy `.cursorrules` в 2025–2026 считается устаревшим; рекомендуют миграцию в `.cursor/rules/*.mdc` (сообщество + Hexlet; docs продвигают mdc). | https://ru.hexlet.io/blog/posts/cursor-rules | 2026-07-30 | да (без абсолюта «удалён из продукта») |
| 12 | Частая ошибка: везде `alwaysApply: true` на длинном файле – раздувает контекст; Always – только для языка/безопасности/папок. | https://ru.hexlet.io/blog/posts/cursor-rules ; https://mayai.ru/cursor-rules-nastroyka-proekta/ | 2026-07-30 | да |
| 13 | Rules ≠ Skills: rules – always-on conventions; skills – подгружаются по задаче (dynamic context). | https://cursor.com/learn/customizing-agents | 2026-07-30 | да (кратко, без deep-dive) |
| 14 | Приказ Роскомнадзора № 140 (19.06.2025) о методах обезличивания ПДн в силе с 01.09.2025 – опираться при формулировке запрета сырых данных в ИИ. | fact-bank соседней B11 / https://companies.rbc.ru/news/lIWDgweSHr/novyie-trebovaniya-k-personalnyim-dannyim-v-2026-chto-teper-obyazatelno/ | 2026-07-30 | да (ссылка + «подробно в B11») |
| 15 | Отправка необезличенной первички/выгрузок 1С во внешние LLM – риск 152-ФЗ; в rules фиксировать запрет + путь `data/clean/`. | внутренняя связка B11 https://koda-fd.ru/blog/obezlichivanie-dannyh-chatgpt-finansist/ | 2026-07-30 | да |
| 16 | Готовые community rules для **разработки BSL** (anoda-tech/cursor_rules_1c) – другой use-case; финотделу копировать BSL-стандарты не нужно. | https://github.com/anoda-tech/cursor_rules_1c | 2026-07-30 | да (анти-угол) |
| 17 | Вторично (mayai + Wordstat 22.06.2026): «cursor rules» ≈ 248; «как настроить cursor» ≈ 186 показов/мес. | https://mayai.ru/cursor-rules-nastroyka-proekta/ | 2026-07-30 | только с атрибуцией / после своего Wordstat |

**fact-bank.md:** прямых строк про Cursor Rules нет – опираемся на официальные docs Cursor + связанные статьи блога КОДА (B11/B16/B20/B21).

---

## Черновик содержимого правил (для writer, не копировать 1:1 в статью без адаптации)

**`AGENTS.md` (фрагмент):** стек Python/Sheets; ответы по-русски; рабочие папки `scripts/`, `data/clean/`, `out/`; запрет трогать `data/raw/` без явного запроса; DoD: нет секретов, нет ПДн в diff, тест на 10–20 строках CSV.

**`.cursor/rules/finotdel-security.mdc`:** `alwaysApply: true` – не вставлять в чат ФИО/ИНН/телефоны/полные выписки; не коммитить `data/raw/**`, `*.env`, пароли OData; перед анализом – только `data/clean/` или обезличенный срез (ссылка на B11).

**`.cursor/rules/scripts-python.mdc`:** `globs: **/*.py`, `alwaysApply: false` – pathlib, явные имена колонок, без `eval`, вывод в `out/`, не перезаписывать raw.

---

## FAQ hints (ответы-действия)

1. **Rules на Free?** – Project rules и AGENTS.md – часть продукта; лимиты Agent зависят от плана (сверять cursor.com/pricing перед утверждением).
2. **Чем не system prompt?** – User Rules глобальны в Settings; Project Rules лежат в git и шарятся с командой.
3. **Нужны ли одному человеку?** – Да: меньше повторов и меньше риска «агент предложил закоммитить выписку».
4. **Сколько файлов в день 1?** – 1× AGENTS.md + 2× mdc (security always + scripts globs); не 40.
5. **Гарантируют ли 100%?** – Нет; критичное дублировать `.gitignore` и процесс ревью diff.
6. **Связь с MCP?** – В rules: «читай только разрешённые пути»; настройка MCP – отдельный гайд B21.
7. **Удалять `.cursorrules`?** – После проверки Active Rules на mdc – да, не держать дубль.
8. **Team Rules обязательны?** – Нет для соло/малого отдела; достаточно git.

---

## Cannibalization / interlink

| Статья | Роль | Не дублировать |
| --- | --- | --- |
| B16 `/baza-znaniy-chatgpt-cursor-finotdel/` | куда класть знания / @файлы | длинный setup базы знаний |
| B20 `/cursor-finansist-skript-dashbord/` | пилот скрипта после rules | пошаговый код дашборда |
| B21 `/mcp-cursor-finansist-instrumenty/` | инструменты MCP | установка MCP серверов |
| B11 `/obezlichivanie-dannyh-chatgpt-finansist/` | юридика/методы обезличивания | полный разбор 152-ФЗ |

CTA: Telegram https://t.me/finance_modern ; клуб https://club.koda-fd.ru/ (без выдуманных цен).

---

## Cover hint

abstract rule-grid nodes locked paths holographic dark purple `#0a0a0f` / `#8b5cf6`, no text on image

---

## Handoff checklist (research)

- [x] utility_gate PASS (shell + notes)
- [x] Wordstat: попытка MCP – сервер отсутствует; warning записан
- [x] SERP через WebSearch 2026-07-30
- [x] ≥10 фактов с URL
- [x] reader_outcome + action_outline 9 шагов
- [x] utility_verdict: PASS
