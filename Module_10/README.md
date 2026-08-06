# Module 10 — Capstone Projects 🏆🎓

**AI Powered Engineering Upskilling Program · Capstone Project**

This is the finish line. Instead of learning a new topic, you **pull everything together** into one complete, end-to-end AI application — planned, built, deployed, and presented. The three projects here are exactly the syllabus's capstone options; **you build one** as your portfolio centerpiece (the other two are working references you can learn from).

> 📖 Full guidance — how to plan, build, deploy, and present a capstone — is in
> [`Course_Notes/Module_10_Capstone_Project.md`](../../Course_Notes/Module_10_Capstone_Project.md).

---

## ⚙️ Setup

All three are **Streamlit** apps whose logic lives in a plain-Python engine you can test on its own.

```bash
pip install -r requirements.txt        # streamlit + pandas
```

The three "engines" (`chatbot_engine.py`, `analyzer.py`, `medical_engine.py`) use **only the Python standard library** — you can run and test them with no installs at all. Streamlit is only needed for the web UI.

> ⏳ First launch of any Streamlit app can take a minute while libraries load; later runs are quick.

---

## 📁 The three capstone options

| Capstone | What it does | Skills it pulls together |
|---|---|---|
| **A — AI Chatbot** 💬 | Answers questions from a knowledge base with a TF-IDF retriever (mock), with an optional real-Claude mode | NLP (M6), Generative AI (M7), deployment (M9) |
| **B — Resume Analyzer** 📄 | Scores a resume against a job description; lists matched/missing skills and gives tips | Text processing, rule-based logic, deployment |
| **C — Medical Assistant** 🏥 | An **educational** symptom-info tool with strong disclaimers and emergency red-flag detection | Safe/responsible AI, rule design, deployment |

Each folder has its own README with run instructions and challenge ideas.

---

## ▶️ How to run each capstone

```bash
# Test the engine with NO installs (pure Python):
cd "Capstone A - AI Chatbot"
python chatbot_engine.py

# Or run the full web app:
streamlit run app.py          # opens http://localhost:8501
```

The same pattern works for B (`analyzer.py`) and C (`medical_engine.py`).

---

## 🧠 What makes this a *capstone*

A capstone is judged less on any single trick and more on the **whole arc**:

```
PLAN     ->  a clear problem + who it helps + what "done" means
BUILD    ->  data + logic + a working app (engine separated from UI)
DEPLOY   ->  a live URL anyone can try (Module 9 skills)
PRESENT  ->  a short demo + honest notes on limits and next steps
```

Every capstone here separates the **engine** (testable logic) from the **app** (UI) — a habit that makes any project easier to build, test, and explain.

---

## 🤖 Optional: real AI mode (Capstone A)

Capstone A runs fully **offline by default**. To try it powered by a live model:

```bash
pip install anthropic
export ANTHROPIC_API_KEY="sk-ant-..."      # from console.anthropic.com
# then set  USE_REAL_API = True  at the top of chatbot_engine.py
```

Capstones B and C are fully rule-based and never need an API key.

---

## ⚠️ Responsible-AI note on Capstone C

The Medical Assistant is an **educational demonstration only**. It cannot and does not diagnose. It always shows a disclaimer, never claims to be a doctor, and checks for emergency warning signs first. It exists to teach the most important lesson of the program: **when AI touches people, honesty about its limits matters more than cleverness.**

---

## 🎓 The end of the journey

> Ten modules ago you wrote your first `print("Hello")`. Now you can take an idea from a blank folder to a deployed AI app you can demo and defend. That arc — **build it, ship it, explain it** — is exactly what an AI engineering role asks for. Congratulations. 🎉

## 📝 A note on sample data

The example identity ("Priya Sharma", `priya.example@email.com`) is **fictional placeholder data**. Replace it with your own before showing your capstone to anyone.
