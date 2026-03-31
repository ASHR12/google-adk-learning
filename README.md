# 🌍 Google ADK Multi-Agent Playground

Welcome to your modular multi-agent learning environment. This project uses the **Google Agent Development Kit (ADK)** to explore everything from real-time tool usage to complex agent orchestration.

## 🚀 How to Run
Everything runs directly in your browser using the ADK Web UI:

```powershell
cd d:\Code\google-adk-learning\agents
uv run python -m google.adk.cli web lessons
```
*   Browse the UI at **http://localhost:8000**
*   Create **+ New Session** for each trial.

---

## 🏗️ Lessons Included

### 1. 🌤️ Lesson: Basic (The Global Assistant)
**Location:** `/lessons/basic`
*   **Goal:** Learn how to bridge an AI to the real world using third-party APIs.
*   **Tools:**
    *   `get_real_weather`: Fetches live status via `wttr.in`.
    *   `get_real_time`: Fetches current local time for any global city via `geopy` and `timezonefinder`.
*   **Why it's cool:** It geolocates your request and provides data in real-time.

### 2. 🔍 Lesson: Sequential (Researcher & Summarizer)
**Location:** `/lessons/sequential`
*   **Goal:** Multi-agent collaboration with data passing.
*   **Workflow:**
    1.  **Researcher Agent:** Uses the built-in `google_search` tool to fetch live results.
    2.  **Summarizer Agent:** Receives the raw search data and produces a structured brief.
*   **Why it's cool:** It demonstrates how to pass state (`output_key="research_raw"`) between agents.

---

## 🛠️ Adding New Lessons
To create a new lesson (e.g., `parallel`), follow this structure:

1.  Create `lessons/my_new_lesson/`
2.  Add an empty `__init__.py`.
3.  Add an `agent.py` defining:
    ```python
    from google.adk.agents.agent import Agent
    from google.adk.apps.app import App

    root_agent = Agent(name="my_agent", ...)
    app = App(name="my_new_lesson", root_agent=root_agent)
    ```
4.  Restart the server and it will appear in the UI dropdown.

---

## ⚠️ Important Rules
*   **Naming:** Folder names must be valid Python identifiers (e.g., `03_parallel` is invalid, use `parallel_agent`).
*   **Environment:** Ensure your `GOOGLE_API_KEY` is set in the `agents/.env` file.
*   **Clean Cache:** If the UI acts weird, delete any `.adk` folders inside your lesson directories.
