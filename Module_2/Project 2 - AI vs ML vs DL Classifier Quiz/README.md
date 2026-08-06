# Project 2 — AI vs ML vs DL Classifier Quiz 🧠

**Module 2 · AI & Data Science Foundations**

An interactive multiple-choice quiz that trains your mental model of the core Module 2 ideas: **AI vs ML vs DL**, the **types of AI**, and the **learning paradigms**. For each real-world scenario you pick the best category — and the program **explains every answer**, so it teaches as it tests.

---

## ▶️ How to run

1. Open a terminal / command prompt **in this folder**.
2. Run:
   ```bash
   python ai_ml_dl_quiz.py
   ```
3. For each question, type the letter of your answer (`a`, `b`, `c`, or `d`).

> Requires **Python 3.x**. No installs — only the built-in `random` module (it shuffles the questions each run).

---

## 🎮 Sample interaction

```
============================================================
Question 1 of 10
============================================================
A model is shown 50,000 emails already labelled 'spam' or 'not spam'
and learns to label new emails on its own.

   a) Rule-based AI
   b) Supervised Machine Learning
   c) Unsupervised Learning
   d) Reinforcement Learning

Your answer (a/b/c/d): b

[CORRECT]
Why: Learning from LABELLED examples (spam / not spam) is SUPERVISED
Machine Learning - specifically classification.
```

At the end you get a score out of 10 and a rating:

```
============================================================
FINAL SCORE: 8 / 10
GREAT job! Your mental model is solid.
============================================================
```

---

## 🧠 What it tests

| Concept from the notes | Example question |
|---|---|
| Rule-based AI vs ML | Hand-written `if/else` rules vs learning from data |
| Supervised / Unsupervised / Reinforcement | Labelled data vs clustering vs reward-based |
| Classic ML vs Deep Learning | Feature engineering vs neural networks |
| Classification vs Regression | Predict a category vs predict a number |
| Types of AI (ANI/AGI/ASI) | What level are today's models? |
| Generative vs Predictive AI | Creating content vs classifying |
| The AI → ML → DL hierarchy | Which field is broadest? |

---

## 🧩 Concepts practised

Lists & dictionaries (the question bank) · functions · loops · conditions · input validation (only `a`–`d`) · the `random` module · f-strings for the report.

---

## 💡 Challenges

1. **Add 5 of your own questions** to the `QUESTIONS` list — one per topic you found tricky.
2. Add a **"category"** field to each question and show a per-topic score at the end (e.g. "Paradigms: 3/3").
3. Add a **timer**: use the `time` module to show how long the quiz took.
