# Project 2 — AI Agent with Tools 🤖🛠️

**Module 8 · AI Agents & Automation**

Builds a simple **AI agent** — a program that, given a goal, **decides which tool to use, uses it, observes the result, and answers**. This is the core **agent loop** and the leap from Module 7's chatbots (which only *talk*) to Module 8's agents (which *act*).

```
THINK  →  ACT (use a tool)  →  OBSERVE  →  ANSWER
```

---

## ▶️ How to run

```bash
python ai_agent.py
```

> **No installs, no API key, no internet** — uses only Python's standard library.

---

## 🛠️ The agent's tools

| Tool | Does | Example goal |
|---|---|---|
| **calculator** | Evaluates a maths expression | "What is 15 * 23 + 100?" |
| **clock** | Current date & time | "What time is it?" |
| **word_counter** | Counts words in text | "How many words in '…'?" |
| **knowledge** | Looks up a built-in fact | "What is the capital of France?" |

---

## 🖼️ Sample output

```
GOAL: What is 15 * 23 + 100?
  THINK  : This needs the 'calculator' tool.
  ACT    : calculator('15 * 23 + 100')
  OBSERVE: 445
  ANSWER : The answer is: 445
```

The visible **THINK → ACT → OBSERVE → ANSWER** trace lets you watch the agent "reason."

---

## 🧠 How the "brain" works (and how a real agent differs)

- **Here:** a small set of **rules** (a router) picks the tool — so the project runs **offline and is fully testable**.
- **In a real agent:** an **LLM** reads the goal and *chooses* the tool (often replying in a structured format the code then executes). **The loop is identical** — only the decision-maker changes. The Module 8 notes (§4) show the LLM-driven version.

> **The formula:** `Agent = an LLM (the brain) + Tools + a Loop.` Swap the rule-based brain for an LLM and you have a real AI agent.

---

## 🧩 Concepts practised

The agent loop · tools as callable functions · routing a goal to a tool · safe evaluation · a transparent reasoning trace.

---

## 💡 Challenges

1. Add a **new tool** (e.g., a temperature converter, or a dictionary of definitions).
2. Add a tool that can **fail**, and have the agent report the error gracefully.
3. Make it **interactive**: read the user's goal with `input()` in a loop.
4. Let the agent **chain two tools** (e.g., look up a number, then calculate with it).
