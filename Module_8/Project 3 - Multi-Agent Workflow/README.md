# Project 3 — Multi-Agent Workflow 👥🔗

**Module 8 · AI Agents & Automation**

Shows the **multi-agent** pattern: instead of one agent doing everything, several **specialist agents** each do one job and pass their work down a pipeline — like a small team. Here, three agents turn a topic into a short article.

```
RESEARCHER  →  WRITER  →  EDITOR  →  finished article
```

---

## ▶️ How to run

**Mock mode (default — offline, no API key):**
```bash
python multi_agent_workflow.py
```

**Real AI mode (Claude plays each agent):**
1. `pip install anthropic`
2. Set `ANTHROPIC_API_KEY`, set `USE_REAL_API = True`, run again.

Change the `TOPIC` variable to generate an article on anything. The result is saved to **`article.md`**.

---

## 👥 The three agents

| Agent | Role (its own "system prompt") | Output |
|---|---|---|
| **Researcher** | Gathers the key points to cover | a list of points |
| **Writer** | Turns points into a draft | a draft article |
| **Editor** | Polishes, adds title + TL;DR | the finished article |

Each agent's **output becomes the next agent's input** — that hand-off is the heart of multi-agent systems.

---

## 🖼️ Sample output

```
[Agent 1: RESEARCHER] gathering key points...
    - A plain-language definition of the topic
    ...
   ...handing the points to the Writer...
[Agent 2: WRITER] drafting the article...
   ...handing the draft to the Editor...
[Agent 3: EDITOR] polishing and formatting...

# How AI agents work
*TL;DR: A beginner-friendly overview...*
...
```

---

## 🧠 Why multi-agent?

- **Specialization** — each agent is good at one thing (research, writing, editing), so quality improves.
- **Separation of concerns** — easier to build, test, and improve one step at a time.
- **This is how real frameworks work** — **CrewAI**, **AutoGen**, and **LangGraph** orchestrate teams of agents exactly like this.

> Single agent (Project 2) = one worker with tools. Multi-agent (this project) = a *team* of specialists with hand-offs.

---

## 🧩 Concepts practised

Multi-agent orchestration · specialized role prompting · agent hand-off (output → input) · workflow pipelines.

---

## 💡 Challenges

1. Add a **4th agent** (e.g., a "Fact-Checker" between Writer and Editor).
2. Give the Researcher agent the **calculator/knowledge tools** from Project 2.
3. Add a **Critic loop**: the Editor sends the draft back if it's too short.
4. Enable real AI mode and watch three Claude agents collaborate.
