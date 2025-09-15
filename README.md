# 🍸 VibeCheck

**Find venues that match your vibe.**
Upload (or link) a picture of a restaurant/bar you like, and VibeCheck will analyze the photo, describe its atmosphere, and search for similar venues in your city.

---

## Features

* **Multimodal vibe analysis** — describe an image using a vision-language model (Claude via Anthropic, currently).
* **Local search** — use [Serper.dev](https://serper.dev) (Google Search API) to find matching bars & restaurants in a given city.
* **Agentic workflow** — powered by [CrewAI](https://docs.crewai.com), with specialized agents for vision analysis, search, and recommendations.
* **Interactive UI** — Gradio front-end for easy demos.

---

## Tech Stack

* [Python 3.11](https://www.python.org/)
* [uv](https://github.com/astral-sh/uv) — fast package/dependency manager
* [CrewAI](https://docs.crewai.com/) — multi-agent orchestration
* [Gradio](https://gradio.app/) — web UI
* [Serper.dev](https://serper.dev) — search API for Google queries

---

## Setup

### 1. Clone & install deps

```bash
git clone https://github.com/yourname/vibecheck.git
cd vibecheck
uv sync
```

### 2. Environment variables

Create a `.env` file in the project root:

```
SERPER_API_KEY=your_serper_key
ANTHROPIC_API_KEY=your_anthropic_api_key_here
```

*(see `.env.example` for reference)*

### 3. Run the app

```bash
uv run python src/app.py
```

Gradio will launch at [http://127.0.0.1:7860](http://127.0.0.1:7860).

---

## Repo Structure

```
src/
  ├── app.py                # Gradio UI
  ├── crew.py               # CrewAI setup (agents + tasks)
  ├── config/
  │    ├── agents.yaml      # Agent definitions
  │    └── tasks.yaml       # Task definitions
  └── __init__.py
pyproject.toml              # uv project + deps
uv.lock                     # locked deps
.env.example                # template for secrets
```

---

## Agents

* **Vision Analyst** → analyzes the uploaded photo, outputs vibe description
* **Venue Finder** → turns description into a search query, runs Serper search
* **Recommender** → formats the results into user-friendly cards

---

## Limitations

* Prototype-level — only tested with Anthropic's Claude models
* Requires public image URLs (no file upload yet in production mode)
* Free Serper API tier is rate-limited

---

## License

MIT

---
