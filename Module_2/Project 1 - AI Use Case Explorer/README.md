# Project 1 — AI Use Case Explorer 🧭

**Module 2 · AI & Data Science Foundations**

The hands-on version of the syllabus activity **"AI Use Case Discussion."** Instead of only *talking* about where AI is useful, you **catalog** real AI use cases and **prioritize** them the way a professional AI team does — using the **Impact vs Feasibility** framework from the notes.

---

## ▶️ How to run

1. Open a terminal / command prompt **in this folder**.
2. Run:
   ```bash
   python ai_use_case_explorer.py
   ```
3. Use the menu (type `1`–`4` and press Enter).

> Requires **Python 3.10+** (uses `match`). No installs — only the built-in `json` module. The tool comes pre-loaded with 5 example use cases so it's useful immediately.

---

## 🧩 What you record for each use case

| Field | Meaning |
|---|---|
| Industry | Healthcare, Finance, Retail, … |
| Problem | The task AI would solve |
| AI type | ML / DL / NLP / Computer Vision / GenAI |
| **Impact** (1–5) | How much business value (5 = huge) |
| **Feasibility** (1–5) | How easy to build (5 = easy) |

The tool then ranks use cases by **priority score = impact × feasibility** and labels each with its quadrant:

| Quadrant | Meaning | Action |
|---|---|---|
| **Quick Win** | High impact + high feasibility | Build first |
| **Big Bet** | High impact + low feasibility | Plan carefully |
| **Low Priority** | Low impact + high feasibility | Later |
| **Avoid** | Low impact + low feasibility | Skip |

---

## 🎮 Sample output (prioritize view)

```
=== AI USE CASES BY PRIORITY (highest first) ===
Rank | Score | Quadrant     | Use Case
----------------------------------------------------------------------
1    | 20    | Quick Win    | Finance - Flag fraudulent card transactions
2    | 20    | Quick Win    | Retail - Recommend products to shoppers
3    | 15    | Big Bet      | Healthcare - Detect tumors in X-ray/CT scans
4    | 15    | Low Priority | Customer Service - Answer FAQs with a chatbot
5    | 8     | Big Bet      | Agriculture - Predict crop disease from leaf photos
----------------------------------------------------------------------
Tip: build the 'Quick Win' items first; plan the 'Big Bet' items.
```

> Output is plain ASCII, so it runs identically on every terminal including the default Windows console.

---

## 🧠 Concepts practised

Dictionaries & lists · functions · input validation (scores 1–5) · `match/case` menu · sorting with a `key` · JSON save/load · aligned tables. *(All Module 1 skills, applied to Module 2 ideas.)*

---

## 📝 Discussion worksheet (do this with your team)

1. Brainstorm **5 AI use cases** for an industry you care about. Add each to the tool.
2. Score every one for **Impact** and **Feasibility** — and *defend* your scores.
3. Run **Prioritize**. Which are "Quick Wins"? Do you agree with the ranking?
4. Pick the **top use case** and sketch which of the 7 lifecycle stages (see Project 3) it would need.

## 💡 Challenges

1. Add a **"data needed"** field to each use case and show it in the table.
2. Add a menu option to **delete** a use case by its number.
3. Change the priority score to **impact × 2 + feasibility** (weight impact more) and see how the ranking changes.
