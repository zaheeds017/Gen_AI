# Module 7 — Hands-on Projects 🪄

**AI Powered Engineering Upskilling Program · Generative AI & Prompt Engineering**

This module is about **using LLMs productively** — ChatGPT, Claude, Gemini, Copilot — and the skill that unlocks them: **prompt engineering**. These three projects build real GenAI apps and teach the prompt patterns behind them.

> 📖 Full theory for each project is in
> [`Course_Notes/Module_07_Generative_AI_and_Prompt_Engineering.md`](../../Course_Notes/Module_07_Generative_AI_and_Prompt_Engineering.md) (sections 12–14).

---

## ⚙️ Setup — nothing required to start

**Every project runs OFFLINE in MOCK mode with no installs and no API key.** Just run the `.py` file and it works, printing the engineered prompt and a representative result.

To switch a project to **REAL mode** (have Claude actually respond):
```bash
pip install anthropic
export ANTHROPIC_API_KEY="sk-ant-..."     # get a key at console.anthropic.com
# then set  USE_REAL_API = True  at the top of the project file
```

> **Why mock-by-default?** So you can learn the app structure and prompt patterns *immediately* — no account, no key, no cost, no internet. The real API is one flag away when you're ready.

---

## 📁 Projects

| # | Project | Teaches | Syllabus link |
|---|---|---|---|
| 1 | **AI Resume Generator** 📄 | Role + task + format + rules prompting | **AI Resume Generator** |
| 2 | **AI Research Assistant** 🔬 | Structured-output prompting; anti-hallucination | **Research Assistant** |
| 3 | **Prompt Engineering Lab** 🧪 | The 5 core prompt techniques | *Prompt Engineering* (reinforcement) |

Projects 1 & 2 are the **two syllabus activities**; Project 3 drills the **prompt-engineering** techniques both rely on.

---

## ▶️ How to run any project

1. Open a terminal **inside that project's folder**.
2. Run the `.py` file, e.g.:
   ```bash
   python ai_resume_generator.py
   ```
3. (Optional) switch to REAL mode as described above.

---

## 🔌 The real API code is accurate for 2026

The `call_claude()` function in each project uses the current Anthropic SDK correctly:

```python
import anthropic
client = anthropic.Anthropic()          # reads ANTHROPIC_API_KEY
resp = client.messages.create(
    model="claude-opus-5",              # or claude-sonnet-5 / claude-haiku-4-5
    max_tokens=1024,
    system=system_prompt,
    messages=[{"role": "user", "content": user_prompt}],
)
```

Swap `claude-opus-5` for OpenAI's or Google's SDK and the *prompt* stays the same — that's the point: **prompt engineering is provider-independent.**

---

## 🧠 The one idea of this module

> **The model is powerful; the prompt is the steering wheel.** A great prompt gives a role, a clear task, examples when needed, and the exact output format. Master that and you can build almost any GenAI app — which is exactly what Module 8 (AI Agents) and Module 10 (Capstone) do next.
