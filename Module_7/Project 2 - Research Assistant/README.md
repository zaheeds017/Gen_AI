# Project 2 — AI Research Assistant 🔬🤖

**Module 7 · Generative AI & Prompt Engineering**

Turn any topic into a structured **research brief** — overview, key concepts, questions to explore, subtopics, and next steps — using an LLM and a **structured-output prompt**. This is the syllabus's *Research Assistant* activity.

---

## ▶️ How to run

**Mock mode (default — offline, no API key):**
```bash
python research_assistant.py
```

**Real mode (Claude writes a full brief):**
1. `pip install anthropic`
2. Set `ANTHROPIC_API_KEY` (see Project 1's README).
3. Set `USE_REAL_API = True` and run again.

Change the `TOPIC` variable at the top to research anything. The result is saved to **`research_brief.md`**.

---

## 🖼️ Sample output (structure)

```
# Research Brief: How Convolutional Neural Networks (CNNs) work
## 1. Overview
## 2. Key Concepts        (5 bullets)
## 3. Important Questions to Explore   (5 questions)
## 4. Subtopics to Study Next          (5 items)
## 5. How to Learn More
```

---

## 🧠 The prompt-engineering lesson: structured output

The prompt **names the exact sections** it wants back:

> *"Use exactly these Markdown sections: ## 1. Overview … ## 2. Key Concepts …"*

This is **structured-output prompting** — instead of hoping for a useful shape, you *specify* it. It's what makes LLM output predictable enough to build apps on. The prompt also includes a critical safety rule:

> *"Do NOT invent URLs, papers, or author names."*

This guards against **hallucination** (§9 in the notes) — LLMs will happily fabricate fake citations if you let them.

---

## 🧩 Concepts practised

Prompt engineering for **structured output** · system vs user prompts · guarding against hallucination · an optional real Claude API call.

---

## 💡 Challenges

1. Research **3 topics** you're studying and compare the briefs.
2. Add a **"depth"** option (beginner vs advanced) to the prompt.
3. Add a section that lists **key terms with definitions**.
4. Enable real mode — how much richer is the AI's brief than the mock scaffold?
