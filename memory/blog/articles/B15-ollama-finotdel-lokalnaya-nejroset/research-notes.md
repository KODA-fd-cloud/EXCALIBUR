# Research notes — B15

**topic_id:** B15  
**slug:** ollama-finotdel-lokalnaya-nejroset  
**h1:** Как поставить Ollama для финотдела: локальная нейросеть под выгрузки 1С без облака  
**research_date:** 2026-07-22  
**utility_gate:** PASS (`how_to`, mode B)  
**practice_angle:** локальный контур рядом с CSV/выгрузками; сырое 1С не в ChatGPT

---

## utility_verdict

**PASS** — how_to: установить Ollama, выбрать модель под железо, прогнать сценарии сверки/категоризации/пояснений, зафиксировать лимиты галлюцинаций и политику «сырое 1С не в облако».

---

## reader_outcome

Финансист ставит Ollama на свой ПК/сервер, запускает локальную LLM, прогоняет обезличенный CSV и понимает, где модель помогает, а где цифры надо проверять руками.

---

## action_outline

1. Решить, зачем локальная модель (152-ФЗ / коммерческая тайна / нет облака).
2. Установить Ollama с ollama.com (Win/Mac/Linux).
3. Проверить `ollama --version` и `http://localhost:11434`.
4. Выбрать модель под RAM/VRAM (Qwen/Llama small → medium).
5. `ollama run …` на тестовом промпте.
6. Сценарии: сверка CSV, категории ДДС, черновик пояснений.
7. Правила проверки цифр (human-in-the-loop).
8. Связка с Cursor / скриптами; API `:11434`.
9. Политика: сырое 1С не в облако; локально тоже не индексировать ПДн без нужды.

---

## Яндекс Wordstat

⚠️ **WORDSTAT AUTH WARNING:** MCP `user-mcp-kv` недоступен. Цифры спроса не выдуманы. OAuth: https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

LSI: как установить ollama, локальная нейросеть, ollama для бизнеса, локальная llm финансы, localhost 11434, qwen llama.

---

## SERP (WebSearch, 22.07.2026)

| URL | Зазор |
| --- | --- |
| https://arte.itlibra.com/ru/articles/ollama-complete-guide | общий гайд; мало CFO |
| https://pasqualepillitteri.it/ru/news/3708/… | установка Win/Mac/Linux 2026 |
| https://knowcorp.ru/ai/ollama/ | связка с 1С-базой знаний; порт 11434 |
| https://toolarium.ru/ollama-zapusk-llm-lokalno/ | localhost, OLLAMA_NO_CLOUD |
| https://vc.ru/future/2681631-… | Ollama+n8n, GPU мифы |

Угол КОДА: финотдел + выгрузки 1С + запрет облака для сырых данных + честные лимиты галлюцинаций.

---

## Факты

| # | Факт | Источник |
| --- | --- | --- |
| 1 | Ollama – локальный рантайм LLM; установка с ollama.com (exe/dmg/curl). | ollama.com; arte.itlibra; pasqualepillitteri |
| 2 | API по умолчанию `localhost:11434`; в браузере «Ollama is running». | knowcorp.ru |
| 3 | Модели: `ollama run qwen3` / llama и др.; первая загрузка тянет веса. | arte.itlibra |
| 4 | Для полного локального режима без облака Ollama – `OLLAMA_NO_CLOUD=1` / disable cloud в server.json (по докам 2026). | toolarium.ru |
| 5 | Docker→хост: `http://host.docker.internal:11434`. | vc.ru |
| 6 | GPU ускоряет, CPU возможен медленнее; размер модели должен влезать в память. | vc.ru; knowcorp |
| 7 | Лицензия движка ≠ лицензия весов модели – проверять перед коммерцией. | arte.itlibra |

---

## FAQ

какая видеокарта; можно ли на CPU; бесплатно ли; чем хуже ChatGPT; безопасно ли для 1С; как связать с Cursor

## CTA / links

club + t.me/finance_modern; internal: /obezlichivanie-dannyh-chatgpt-finansist/, /claude-code-finotdel/; **no salebot**
