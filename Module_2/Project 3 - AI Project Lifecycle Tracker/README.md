# Project 3 — AI Project Lifecycle Tracker 📋

**Module 2 · AI & Data Science Foundations**

Turns the **7-stage AI Project Lifecycle** from the notes into a tool you can actually **plan and track**. Pick a project idea, then move it through every stage — setting a status and notes for each — and watch a live **progress bar** and completion percentage.

---

## ▶️ How to run

1. Open a terminal / command prompt **in this folder**.
2. Run:
   ```bash
   python ai_lifecycle_tracker.py
   ```
3. Use the menu (type `1`–`4` and press Enter).

> Requires **Python 3.10+** (uses `match`). No installs — only the built-in `json` module. Your project is saved to `ai_project.json` between runs.

---

## 🔄 The 7 stages tracked

```
1. Problem Definition
2. Data Collection
3. Data Preparation & Cleaning
4. EDA & Feature Engineering
5. Model Building & Training
6. Model Evaluation
7. Deployment & Monitoring
```

Each stage has a **status** — `Not Started` (0%), `In Progress` (50%), or `Done` (100%) — and free-text **notes**. Overall progress is the average across all seven stages.

---

## 🎮 Sample output

```
======================================================================
PROJECT: Churn Predictor
======================================================================
#  | Stage                       | Status      | Notes
----------------------------------------------------------------------
1  | Problem Definition          | Done        | Defined goal: predict churn
2  | Data Collection             | In Progress | Pulling 2yr data
3  | Data Preparation & Cleaning | Not Started | -
4  | EDA & Feature Engineering   | Not Started | -
5  | Model Building & Training   | Not Started | -
6  | Model Evaluation            | Not Started | -
7  | Deployment & Monitoring     | Not Started | -
----------------------------------------------------------------------
Overall progress: [####----------------] 21%
```

> `Done` counts as 100% and `In Progress` as 50%, so 1 done + 1 in-progress out of 7 = **21%**. Output is plain ASCII — runs cleanly on any terminal.

---

## 🧠 Concepts practised

Dictionaries & lists (project + stages) · functions · loops & `enumerate` · `match/case` menu · input validation (valid stage numbers) · JSON save/load · integer math for the progress bar.

---

## 📝 Activity

Take the **top use case** you chose in **Project 1 (AI Use Case Explorer)** and plan it here:
1. Rename the project to your use case.
2. For each of the 7 stages, write **one note** describing what you would actually do.
3. Mark the stages you *could* realistically start as `In Progress`.

This connects all three projects: **discuss (P1) → understand (P2) → plan (P3)**.

## 💡 Challenges

1. Add a **"blocked"** status (weight 0%) with its own label.
2. Add a menu option to **reset** all stages to `Not Started`.
3. Warn the user if they mark a later stage `Done` while an earlier stage is still `Not Started` (stages usually happen in order).
