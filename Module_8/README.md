# Module 8 — Hands-on Projects 🤖⚙️

**AI Powered Engineering Upskilling Program · AI Agents & Automation**

This module is about making AI **act**, not just answer: **automated workflows**, **AI agents** that use tools, and **multi-agent** teams. These three projects build all three ideas in Python — so you understand what tools like **n8n**, **CrewAI**, and **LangGraph** do under the hood.

> 📖 Full theory for each project is in
> [`Course_Notes/Module_08_AI_Agents_and_Automation.md`](../../Course_Notes/Module_08_AI_Agents_and_Automation.md) (sections 12–14).

---

## ⚙️ Setup — nothing required to start

**Every project runs OFFLINE in MOCK mode with no installs and no API key.** Just run the `.py` file.

To switch a project to **REAL AI mode** (Claude powers the agents/emails):
```bash
pip install anthropic
export ANTHROPIC_API_KEY="sk-ant-..."     # get a key at console.anthropic.com
# then set  USE_REAL_API = True  at the top of the project file
```
*(Project 2 uses only the standard library — no installs at all, ever.)*

---

## 📁 Projects

| # | Project | Concept | Syllabus link |
|---|---|---|---|
| 1 | **Email Automation** 📧 | Workflow automation | **Email Automation** |
| 2 | **AI Agent with Tools** 🤖 | The agent loop (single agent) | *AI Agents* (reinforcement) |
| 3 | **Multi-Agent Workflow** 👥 | Agents collaborating | *Multi-Agent Concepts* (reinforcement) |

Project 1 is the **syllabus activity**; Projects 2 & 3 drill the **agent** and **multi-agent** concepts the module is built on.

---

## ▶️ How to run any project

1. Open a terminal **inside that project's folder**.
2. Run the `.py` file, e.g.:
   ```bash
   python email_automation.py
   ```

---

## 🔗 How the projects build up

```
Project 1  →  AUTOMATE  : a workflow that loops over data and delivers results
Project 2  →  AGENT     : one worker that uses TOOLS in a think→act→observe loop
Project 3  →  TEAM      : several specialist agents hand work down a pipeline
```

Together they trace the arc of the module: **automation → single agent → multi-agent teams.**

---

## 🧠 The big idea of this module

> **A chatbot talks; an agent acts.** An agent is an **LLM (the brain) + tools + a loop**. Chain agents into a **workflow**, or a **team of specialists**, and you can automate real multi-step work — which is exactly what the Module 10 Capstone will do.
