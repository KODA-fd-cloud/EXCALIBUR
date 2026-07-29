# Research notes — B20

**topic_id:** B20  
**slug:** cursor-finansist-skript-dashbord  
**h1:** Cursor для финансиста: как за вечер собрать скрипт сверки и маленький дашборд  
**research_date:** 2026-07-22  
**publish_target:** сайт koda-fd.ru/blog (+ Дзен по оркестрации)  
**utility_gate:** PASS (`how_to`, mode B)  
**related_published:** `/cursor-ai-agenty-finotchetnost/`, `/vibe-coding-finansist/`, `/claude-code-finotdel/`  
**sibling_queue:** B19 (Python сверка CSV), B21 (MCP в Cursor)

---

## utility_verdict

**PASS** — тема utility-only how_to. Читатель получает рабочий маршрут на один вечер: отличить Cursor от веб-чата ChatGPT для файлов проекта; собрать папку с CSV и `.gitignore` без сырых ПДн; промптом получить скрипт сверки двух выгрузок; из той же папки поднять маленький дашборд (Streamlit или простой HTML); итерировать точечными правками, а не «перепиши всё». Не новость про Cursor 3, не обзор тарифов ради обзора, не «вообще про vibe coding».

---

## reader_outcome

После гайда финансист за один вечер сможет в Cursor открыть папку с двумя CSV, получить рабочий скрипт сверки (ключ + суммы + файл расхождений) и локальный мини-дашборд поверх тех же данных — без заказного разработчика и без выгрузки сырых ПДн в публичный чат.

---

## action_outline

1. **Скачать Cursor только с cursor.com** — установить, открыть пустую папку проекта (не «весь Диск C»), начать с Ask/Chat: «объясни структуру, ничего не меняй».
2. **Подготовить данные** — два CSV сверки (банк vs 1С / две системы); положить в `data/`; в `.gitignore` добавить `data/*.csv`, `.env`, `*.xlsx` с ПДн; в чат не кидать сырые ФИО/ИНН (линк на обезличивание).
3. **Зафиксировать Definition of Done сверки** — ключ (номер+дата / id), поля сумм, допуск округления, выход: `out/mismatches.csv` + краткий summary в терминале.
4. **Сценарий 1: скрипт сверки** — один промпт Agent/Composer: pandas (или csv stdlib), чтение двух файлов, outer join по ключу, отчёт расхождений; принять diff по файлам, прогнать в терминале Cursor.
5. **Проверить краевые случаи** — кодировка CP1251/UTF-8, разделитель `;`/`,`, пробелы в суммах, пустые ключи; править точечно (`Ctrl+K` / короткий follow-up), не «перепиши весь проект».
6. **Сценарий 2: мини-дашборд** — тот же `data/` или `out/`: Streamlit (`streamlit run app.py`) с метриками + таблицей расхождений **или** статический HTML+Chart из одной команды; локально, без деплоя в интернет на первом шаге.
7. **Правила итерации промптов** — одна задача = один чат/ветка; `@файл` вместо «посмотри всё»; Ask перед Agent на незнакомом коде; запрет «сделай красиво как в Notion» без критериев.
8. **Чеклист безопасности перед показом коллегам** — Privacy Mode при необходимости; нет секретов в репо; дашборд только localhost / внутренняя сеть; сырые выгрузки не в Community Cloud.
9. **Куда расти** — повторный запуск по новым CSV; rules/AGENTS.md (B23); MCP вместо ручного копирования (B21); связка с Claude Code / агентами финотчётности без дубля этой статьи.

---

## Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT AUTH WARNING:** сервер MCP `user-mcp-kv` в этой сессии **не подключён** (в каталоге MCP нет инструментов `wordstat_*`). Точные показы/мес **не получены** и **не выдуманы**. Обновите токен / подключите MCP-KV: https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

**Экспертная семантика (без цифр спроса) — LSI для копирайтера:**

| Кластер | Фразы (использовать осмысленно) | Роль |
| --- | --- | --- |
| Primary | cursor ai, курсор ai, cursor ide | H1/лид осторожно: бренд-запрос широкий, угол — финансист + вечерний артефакт |
| Beginner RU | cursor для начинающих, как пользоваться cursor, скачать cursor | H2 установка / отличие от ChatGPT |
| Fin angle | cursor финансист, cursor финотдел, сверка csv cursor | Уникальный угол КОДА; secondary в лиде |
| Vibe + UI | vibe coding cursor, вайб кодинг дашборд, streamlit дашборд csv | H2 сценарий 2 |
| Diff vs chat | cursor vs chatgpt, агент правит файлы, composer cursor | H2 «чем отличается от чата» |
| Adjacent | python сверка csv, pandas две таблицы, .gitignore csv | Перелинк B19 / практика без каннибализации |

**SEO-вывод:** SERP по `cursor ai` / «для начинающих» забит общими гайдами для разработчиков (Habr, DTF, Dzen, DEV). Запроса «cursor финансист» почти нет в выдаче — **голубой океан**. В H1/лиде держать связку «Cursor + финансист + скрипт сверки + дашборд за вечер», не конкурировать лобовым «полный гайд Cursor 2026».

---

## SERP (WebSearch Cursor, 22.07.2026)

Приоритет — живой WebSearch; `research-serp.json` (шаг 0) почти пуст по secondary (0 результатов) — **не опираться**. Primary в утке: только cursor.com + англоязычные обзоры.

### Главный запрос: `cursor ai` / Cursor 2026

| # | URL | Тип | Пробел для КОДА |
| --- | --- | --- | --- |
| 1 | https://cursor.com/ | Официальный продукт: coding agent | Нет сценария «финансист / CSV / сверка» |
| 2 | https://cursor.com/blog/cursor-3 | Cursor 3: Agents Window, cloud/local handoff | Новость/продукт; не how-to сверки |
| 3 | https://cursor.com/pricing | Hobby / Pro $20 / Teams $40 | Цены ок для FAQ; не тема статьи |
| 4 | https://habr.com/ru/companies/bothub/articles/1044774/ | RU-гайд лето 2026, Cursor ~3.6, Agent/Ask/Plan | Для девов; нет финотдела и дашборда из CSV |
| 5 | https://dtf.ru/ask/4828335-cursor-ai-polnoe-rukovodstvo-dlya-nachinayushchikh | Новичкам: установка, языки, оплата из РФ | Общий онбординг, не артефакт за вечер |
| 6 | https://dzen.ru/a/ajp8gvOqTyVciATQ | Hobby, скачивать только с cursor.com, Tab/Chat/Agent | Полезно для FAQ «с чего начать»; нет сверки |
| 7 | https://dev.to/asad1/app-development-with-cursor-in-2026-the-definitive-technical-guide-27m6 | Production apps, MCP, .cursorrules | Слишком engineering; B23/B21 заберут rules/MCP |
| 8 | https://vc.ru/services/2731935-cursor-ai-v-2026-obzor-migratsiya-s-vs-code | Обзор/миграция VS Code | Режим A-ish; наш угол — практика за вечер |

### Вторичные

- **`cursor для начинающих`** — Habr Bothub, DTF, Dzen Хорошев, ai.cc: установка, Tab/Chat/Agent, тариф Hobby. Паттерн «скачай → поиграй с чатом». Нет: папка проекта под CSV, `.gitignore`, Definition of Done сверки.
- **`cursor финансист`** — пусто / нерелевант. Ближайшее: англ. vibe-coded finance apps (Medium, Vibe Mart), не RU CFO-язык.
- **`vibe coding cursor дашборд`** — neiropotok (трекер расходов → Vercel), unoapi (критика «сделай дашборд» без MCP), CodeGeeks (personal finance dashboard за субботу + ломка CSV-парсинга). Угол: да, дашборды вайбят; **ломкость CSV и безопасность** — наш якорь честности.

### Конкурентный зазор (угол КОДА)

1. **Финансист, не junior-dev** — Cursor как «папка с рабочими файлами + агент», аналогии из сверки Excel, без культа агентов.
2. **Два артефакта за вечер:** скрипт сверки → мини-дашборд из той же папки (не «сайт на Vercel»).
3. **Граница с уже опубликованным:** agents финотчётности = другой сценарий; vibe-coding = манифест; Claude Code = другой инструмент; B19 = глубже Python/pandas; B20 = Cursor-workflow вокруг обоих артефактов.
4. **Безопасность 152-ФЗ** — `.gitignore`, Privacy Mode, localhost-дашборд, линк `/obezlichivanie-dannyh-chatgpt-finansist/`.
5. **Анти-паттерн промптов** — не «перепиши всё красиво»; итерация по diff + DoD.

---

## Таблица фактов (только с URL; для writer)

| # | Утверждение | Источник | Дата проверки |
| --- | --- | --- | --- |
| 1 | Cursor позиционируется как AI coding agent / среда для сборки ПО с агентами; сайт продукта — cursor.com. | https://cursor.com/ | 2026-07-22 |
| 2 | Cursor изначально — форк VS Code (чтобы менять поверхность IDE, а не только расширение). | https://cursor.com/blog/cursor-3 | 2026-07-22 |
| 3 | Cursor 3 — workspace вокруг агентов: multi-repo, параллельные local/cloud agents, handoff cloud↔local, diffs/PR. | https://cursor.com/blog/cursor-3 | 2026-07-22 |
| 4 | В Cursor 3 есть встроенный browser для открытия/навигации локальных сайтов и промптов по ним (удобно для проверки Streamlit/HTML localhost). | https://cursor.com/blog/cursor-3 | 2026-07-22 |
| 5 | Тариф **Hobby**: бесплатно, без карты; limited Agent requests и Tab completions. | https://cursor.com/pricing | 2026-07-22 |
| 6 | Индивидуальный старт **Pro**: **$20/мес** (на yearly UI также показывают ~$16/мес при годовой оплате); Extended Agent, frontier models, MCP/skills/hooks, cloud agents. | https://cursor.com/pricing | 2026-07-22 |
| 7 | **Teams**: от **$40/user/мес**; Privacy Mode на уровне команды, SSO, админка. | https://cursor.com/pricing | 2026-07-22 |
| 8 | Privacy Mode: при включении код **не используется для обучения** Cursor и провайдерами моделей (формулировка официального FAQ на pricing). | https://cursor.com/pricing | 2026-07-22 |
| 9 | Подписки Cursor продаются **только** через cursor.com; покупки у реселлеров/третьих лиц — unauthorized, риск блокировки. | https://cursor.com/pricing | 2026-07-22 |
| 10 | RU-обзор (лето 2026): Cursor ~**3.6**; агент читает/правит файлы, терминал, MCP; режимы Agent / Ask / Plan / Debug / Multitask; правки через diff accept/reject. | https://habr.com/ru/companies/bothub/articles/1044774/ | 2026-07-22 |
| 11 | Горячие клавиши из RU-гайда: агентное окно `Ctrl/Cmd+I`; точечное `Ctrl/Cmd+K`; контекст через `@`. (В UI 2026 названия режимов могут чуть плавать — сверять с установленной версией.) | https://habr.com/ru/companies/bothub/articles/1044774/ | 2026-07-22 |
| 12 | Практический совет новичкам: качать установщик **только** с cursor.com/download; после триала остаётся Hobby с лимитами. | https://dzen.ru/a/ajp8gvOqTyVciATQ | 2026-07-22 |
| 13 | Streamlit — open-source фреймворк: data scripts → web apps на чистом Python, без фронтенд-опыта; старт: `pip install streamlit`, `streamlit hello`. | https://streamlit.io/ | 2026-07-22 |
| 14 | Типовой паттерн дашборда: `pd.read_csv` + `st.dataframe` / `st.line_chart`; скрипт перезапускается при изменении файла. | https://streamlit.io/ ; https://www.deeplearningnerds.com/build-an-interactive-dashboard-for-your-pandas-dataframe-with-streamlit/ | 2026-07-22 |
| 15 | Для внутренних CSV-дашбордов Streamlit часто выбирают за скорость прототипа; production auth/RBAC — отдельный слой (не обещать «корпоративный BI за вечер»). | https://reflex.dev/blog/streamlit-vs-dash-python-dashboards/ | 2026-07-22 |
| 16 | Vibe-coded finance dashboard за день/субботу реалистичен, но CSV с разными заголовками ломает импорт «молча» — нужны явные ошибки и схема колонок. | https://www.codegeeks.solutions/blog/vibe-coding-examples-10-real-projects-lessons-learned | 2026-07-22 |
| 17 | Критика вайб-кодинга: промпт «сделай дашборд» даёт гору UI без надёжных данных/инструментов; проверка и границы задачи важнее «магии». | https://unoapi.ru/blog/vibe-coding-reality-check | 2026-07-22 |

**Не использовать как факт без оговорки:** «1M users / 360k paying» из сторонних туториалов (tech-insider и др.) — маркетинг третьих лиц; любые показы Wordstat; цены клуба KODA; обещание «бесплатно навсегда хватит Hobby для ежедневной работы».

**Fact-bank:** прямых фактов про Cursor/Streamlit в `fact-bank.md` нет — опираться на таблицу выше + официальные URL. Контент-заводные цифры fact-bank к B20 **не тянуть**.

---

## Структура H2/H3 для будущей статьи (спека для writer)

Следовать карточке B20; ниже — наполнение.

### H2: Чем Cursor отличается от чата ChatGPT для рабочих файлов
- Чат = копипаст фрагментов; Cursor = папка проекта, diff, терминал, несколько файлов.
- Ask vs Agent: сначала «объясни, не трогай», потом правки.
- Рекомендация: для сверки CSV не работать в веб-чате с сырыми выгрузками.

### H2: Подготовка папки проекта: CSV, `.gitignore`, запрет сырых ПДн
- Структура: `data/`, `src/` или корень, `out/`, `.gitignore`.
- Что не коммитить и не прикреплять в облачный чат.
- Privacy Mode — когда включать (FAQ).

### H2: Сценарий 1: скрипт сверки двух выгрузок
- Промпт-шаблон с DoD (ключ, суммы, mismatches.csv).
- Прогон в терминале; разбор ошибок кодировки/разделителя.
- Рекомендация: один скрипт, один отчёт, без «фреймворка».

### H2: Сценарий 2: маленький дашборд (Streamlit / простой HTML) из той же папки
- Streamlit: метрики (кол-во расхождений, сумма delta) + таблица.
- Альтернатива: один HTML, если Streamlit пугает.
- Только localhost на первом шаге; browser в Cursor — для проверки UI.

### H2: Как итерировать промптами и не утонуть в «перепиши всё»
- Чеклист анти-паттернов; `@файл`; короткие follow-up.
- Когда остановиться: DoD выполнен.
- Мост на B21 (MCP) и B23 (rules) без раскрытия их целиком.

### Блок «Что дальше» + FAQ
- Internal: `/cursor-ai-agenty-finotchetnost/`, `/vibe-coding-finansist/`, `/claude-code-finotdel/` (+ при публикации B19 — сверка CSV).
- CTA: club.koda-fd.ru + t.me/finance_modern (≤2 каждый; **без** salebot).

---

## Риски и оговорки для writer

- Не писать «полный гайд Cursor 2026» — каннибализация и режим A.
- Не дублировать B19 (глубокий pandas) и `/cursor-ai-agenty-finotchetnost/` (агенты отчётности).
- Не обещать деплой в интернет / BI для совета директоров за вечер.
- Не вставлять Wordstat-цифры.
- Длинное тире «—» запрещено в article.html; кавычки прямые `"`.
- Эмодзи в тексте статьи — нет.
- Цены клуба не выдумывать; CTA только conversion-map.
- Автор: `olga-kondratskaya`; голос КОДА.
- Версии UI Cursor плавают (3.x) — описывать действия («открой Agent», «прими diff»), не привязываться к пикселям скриншотов третьих лиц.

---

## Internal links

- `/cursor-ai-agenty-finotchetnost/`
- `/vibe-coding-finansist/`
- `/claude-code-finotdel/`
- (опционально) `/obezlichivanie-dannyh-chatgpt-finansist/` — блок безопасности
- (когда B19 live) `/python-finansist-sverka-csv/`

---

## FAQ hints (ответы-действия)

| Вопрос | Направление ответа |
| --- | --- |
| Платный ли Cursor? | Старт с Hobby (free). Для регулярной агентной работы смотреть Pro $20/мес на cursor.com/pricing; сверить лимиты в Settings → Billing. Не покупать у «серых» перекупов. |
| Нужен ли git? | Для вечернего пилота — нет. `.gitignore` всё равно завести (привычка). Git понадобится, когда делишься с коллегой или откатываешь сломанный промпт. |
| Чем отличается от статьи про AI-агентов финотчётности? | Та — про агентный контур отчётности. Эта — один вечер: скрипт сверки + мини-дашборд в папке Cursor. Разные DoD. |
| Нужен ли Python заранее? | Желательно поставить Python и объяснить агенту путь; сам код можно сгенерировать. Если Python нет — сначала мини-установка, иначе терминал не запустит скрипт/Streamlit. |
| Streamlit или HTML? | Streamlit быстрее для таблицы+метрик на Python. HTML — если нельзя ставить пакеты. На первом шаге оба только localhost. |
| Безопасно ли кидать выгрузки 1С в Cursor? | Не кидать сырые ПДн. Обезличить / урезать колонки; Privacy Mode; не пушить `data/` в публичный GitHub; дашборд не в Community Cloud с боевыми данными. |

---

## CTA (conversion-map)

| CTA | URL | Лимит |
| --- | --- | --- |
| Клуб KODA | https://club.koda-fd.ru/?utm_source=blog&utm_medium=article&utm_campaign=cursor-finansist-skript-dashbord | ≤2 |
| Telegram | https://t.me/finance_modern?utm_source=blog&utm_medium=article | ≤2 |

**Запрещено:** `t.me/koda_salebot`, `@koda_salebot`.

---

## Источники исследования

- https://cursor.com/ , https://cursor.com/pricing , https://cursor.com/blog/cursor-3 , https://cursor.com/download
- https://habr.com/ru/companies/bothub/articles/1044774/
- https://dzen.ru/a/ajp8gvOqTyVciATQ , https://dtf.ru/ask/4828335-cursor-ai-polnoe-rukovodstvo-dlya-nachinayushchikh
- https://streamlit.io/ , https://www.deeplearningnerds.com/build-an-interactive-dashboard-for-your-pandas-dataframe-with-streamlit/
- https://www.codegeeks.solutions/blog/vibe-coding-examples-10-real-projects-lessons-learned
- https://unoapi.ru/blog/vibe-coding-reality-check
- `memory/brief/fact-bank.md`, `conversion-map.md`, карточка B20 в `blog-topics.md`
- WebSearch Cursor 2026-07-22; `research-serp.json` как неполный черновик шага 0
