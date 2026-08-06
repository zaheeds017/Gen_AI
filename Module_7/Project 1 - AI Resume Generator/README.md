# Project 1 — AI Resume Generator 📄🤖

**Module 7 · Generative AI & Prompt Engineering**

Turn a few facts about a person into a polished, professional resume using a **Large Language Model** and a well-engineered **prompt**. This is the syllabus's *AI Resume Generator* activity.

---

## ▶️ How to run

**Mock mode (default — no setup, no API key, fully offline):**
```bash
python ai_resume_generator.py
```
It prints the exact prompt it would send, then assembles a clean resume so you see the whole app working immediately.

**Real mode (Claude actually writes the resume):**
1. `pip install anthropic`
2. Get a key at [console.anthropic.com](https://console.anthropic.com) and set it:
   ```bash
   export ANTHROPIC_API_KEY="sk-ant-..."     # Windows: setx ANTHROPIC_API_KEY "sk-ant-..."
   ```
3. In the file, set `USE_REAL_API = True`, then run it again.

---

## 🖼️ Sample output (mock mode)

```
# Alex Rivera
## Professional Summary
Aspiring Junior AI/Machine Learning Engineer with hands-on experience building
end-to-end AI applications...
## Key Skills
Python | Pandas | scikit-learn | TensorFlow (basics) | OpenCV | Prompt Engineering | Git
## Experience & Projects
- Built a customer-churn prediction model (87% accuracy) with scikit-learn.
...
```

The result is saved to **`resume.md`**.

---

## 🧠 The prompt engineering (the real lesson)

The program builds the prompt in **two parts**, and that structure is *why* the output is reliable:

| Part | Purpose |
|---|---|
| **System prompt** | Sets the AI's **role** ("expert technical resume writer") and rules ("never invent facts") |
| **User prompt** | Gives the **task**, the **data**, the exact **format** (section headings), and the **rules** (word limit, action verbs) |

> **Key idea:** the *same model* gives a mediocre or an excellent resume depending entirely on the prompt. Role + task + format + rules = a great prompt.

---

## 🔌 The real API call (accurate for 2026)

```python
import anthropic
client = anthropic.Anthropic()          # reads ANTHROPIC_API_KEY
response = client.messages.create(
    model="claude-opus-5",              # or claude-sonnet-5 / claude-haiku-4-5
    max_tokens=1024,
    system=system_prompt,
    messages=[{"role": "user", "content": user_prompt}],
)
text = "".join(b.text for b in response.content if b.type == "text")
```

---

## 💡 Challenges

1. Replace the `PROFILE` with **your own** details and generate your resume.
2. Add an **input()** flow so the user types their details interactively.
3. Add a **"tone"** option (formal vs friendly) and inject it into the prompt.
4. Enable real mode and compare the AI output to the mock — what did the LLM add?
