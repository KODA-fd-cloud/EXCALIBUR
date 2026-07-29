# Research notes — B23

**topic_id:** B23  
**slug:** cursor-rules-finotdel  
**h1:** Как настроить Cursor Rules для финотдела: стиль кода, папки и запрет сырых выгрузок 1С  
**research_date:** 2026-07-22  
**publish_target:** сайт koda-fd.ru/blog (+ Дзен по оркестрации)  
**utility_gate:** PASS (`how_to`, mode B)  
**related_published:** `/baza-znaniy-chatgpt-cursor-finotdel/`, `/cursor-finansist-skript-dashbord/`, `/obezlichivanie-dannyh-chatgpt-finansist/`

---

## utility_verdict

**PASS** — how_to mode B. Читатель получает: зачем rules вместо «каждый раз писать в чат»; минимальный набор для финотдела (папки, CSV, запрет ПДн); пример `AGENTS.md` / `.cursor/rules/*.mdc`; связь с базой знаний и MCP; внедрение одного шаблона на команду. Не каталог 100 community rules, не hooks/skills deep-dive.

---

## reader_outcome

После гайда финдир/финменеджер сможет создать `AGENTS.md` и 1–3 project rules в `.cursor/rules/`, зафиксировать структуру `data/`/`out/`, запрет сырых выгрузок 1С в чат и Definition of Done – чтобы агент не предлагал коммитить ПДн.

---

## action_outline

1. **Зачем** – чат забывает; rules едут в каждый Agent.
2. **Форматы 2026** – `.cursor/rules/*.mdc` (preferred), `AGENTS.md` (простой), legacy `.cursorrules` deprecate.
3. **Минимум финотдела** – папки, gitignore, запрет ПДн, стек Python/Sheets, DoD.
4. **Пример файлов** – alwaysApply security + globs на `*.py` / `data/**`.
5. **Связь** – база знаний (B16), MCP filesystem (B21), скрипт-пилоты (B20).
6. **Команда** – один шаблон в git; Team rules опционально; без культа сложности.

---

## Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT AUTH WARNING:** сервер MCP `user-mcp-kv` в этой сессии **не подключён**. Точные показы/мес **не получены** и **не выдуманы**. https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

**LSI:** как настроить cursor rules; agents.md cursor; .cursorrules; .cursor/rules mdc; правила cursor для команды; project rules cursor.

**SEO-вывод:** SERP – дев-гайды. Угол КОДА: **запрет сырых 1С + папки финотдела**, не React conventions.

---

## SERP (WebSearch, 22.07.2026)

| # | URL | Заметка |
| --- | --- | --- |
| 1 | https://cursor.com/help/customization/rules | Help: UI + AGENTS.md + legacy |
| 2 | https://cursor.com/docs/rules.md | Docs: mdc frontmatter, nested AGENTS.md |
| 3 | https://taskprio.com/cursor-rules | Обзор 4 типов apply |
| 4 | Community forum rules/AGENTS/hooks | Skills vs rules vs hooks |

### Ключевые факты Cursor Rules (2026)

- Project rules: `.cursor/rules/*.mdc` + frontmatter `description` / `globs` / `alwaysApply`
- Plain `.md` в rules **игнорируется** (нет frontmatter)
- `AGENTS.md` – plain markdown, auto; nested в подпапках; deeper wins
- Legacy `.cursorrules` – migrate to Always Apply mdc
- User rules – локально в Settings; Team rules – dashboard
- CLAUDE.md читается similarly (always)

---

## Таблица фактов

| # | Утверждение | Источник | Дата |
| --- | --- | --- | --- |
| 1 | Rules создаются через Customize → Rules или `/create-rule`. | https://cursor.com/docs/rules.md | 2026-07-22 |
| 2 | Четыре режима: Always / Apply Intelligently / globs / Manual @. | https://cursor.com/help/customization/rules | 2026-07-22 |
| 3 | `AGENTS.md` – простая альтернатива без frontmatter. | https://cursor.com/docs/rules.md | 2026-07-22 |
| 4 | Nested AGENTS.md: более специфичные инструкции приоритетнее. | https://cursor.com/docs/rules.md | 2026-07-22 |
| 5 | `.cursorrules` legacy, мигрировать в `.cursor/rules/`. | https://cursor.com/help/customization/rules | 2026-07-22 |
| 6 | Project rules версионируются с git. | cursor docs | 2026-07-22 |
| 7 | Team rules sync с dashboard, поддерживают globs. | https://cursor.com/help/customization/rules | 2026-07-22 |
| 8 | Rules ≠ Skills ≠ Hooks (hints vs workflows vs deterministic). | forum.cursor.com | 2026-07-22 |
| 9 | База знаний финотдела – соседний гайд B16. | /blog/baza-znaniy-chatgpt-cursor-finotdel/ | 2026-07-22 |
| 10 | Обезличивание – B11; не дублировать длинно. | /blog/obezlichivanie-dannyh-chatgpt-finansist/ | 2026-07-22 |

---

## FAQ hints

1. Free тариф? – Rules – функция продукта; лимиты Agent зависят от плана (сверять pricing).
2. Vs system prompt? – User rules глобальны; project rules в репо и шарятся.
3. Нужны ли одному человеку? – Да: меньше повторов и меньше «агент предложил закоммитить data/».
4. Сколько rules? – 1 AGENTS.md + 2–4 mdc; не 40 файлов в день 1.
5. Работают ли всегда? – Модель может игнорировать; критичное – ещё и `.gitignore`/хуки.
6. Связь с MCP? – В rules: «читай data/ только через filesystem MCP, path узкий».
7. `.cursorrules` удалять? – После миграции да; не держать оба формата.

---

## Cover hint

abstract rule-grid nodes locked paths holographic dark purple, no text
