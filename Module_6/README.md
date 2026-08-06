# Module 6 — Hands-on Projects 💬

**AI Powered Engineering Upskilling Program · Natural Language Processing**

This is where you teach computers to **read and understand text**. Three projects cover the NLP essentials: **spam detection**, **sentiment analysis**, and the **text preprocessing** that underpins both.

> 📖 Full theory for each project is in
> [`Course_Notes/Module_06_Natural_Language_Processing.md`](../../Course_Notes/Module_06_Natural_Language_Processing.md) (sections 12–14).

---

## ⚙️ One-time setup

```bash
pip install -r requirements.txt
# or:  pip install numpy matplotlib seaborn scikit-learn
```

Check Python first with `python --version` (need **3.x**). No heavy downloads — everything runs with scikit-learn.

---

## 📁 Projects

| # | Project | Task | Technique | Syllabus link |
|---|---|---|---|---|
| 1 | **Spam Detection** 📧 | Text classification | TF-IDF + Naive Bayes | **Spam Detection** |
| 2 | **Sentiment Analysis** 😀😞 | Positive/negative | TF-IDF + Logistic Regression | *Sentiment Analysis* (reinforcement) |
| 3 | **Text Preprocessing Toolkit** 🧹 | Cleaning & vectorizing text | Tokenize/stopwords/BoW/TF-IDF | *Text Preprocessing* (reinforcement) |

Project 1 is the **syllabus activity**. Projects 2 & 3 reinforce two more listed topics (Sentiment Analysis, Text Preprocessing).

---

## ▶️ How to run any project

1. Do the one-time `pip install` above.
2. Open a terminal **inside that project's folder**.
3. Run the `.py` file, e.g.:
   ```bash
   python spam_detection.py
   ```
4. Open the generated **`*.png`** chart.

---

## 🔗 How the projects connect

```
Project 3  →  PREPROCESS: turn raw text into numbers (tokens → TF-IDF)
Project 1  →  CLASSIFY  : is this message spam or ham?
Project 2  →  ANALYZE   : is this review positive or negative?
```

**Recommended order: 3 → 1 → 2** — understand how text becomes numbers first, then build classifiers on top. (Projects 1 & 2 use the exact TF-IDF vectors that Project 3 explains.)

---

## 🧠 The big idea of this module

> **Machines can't read words — only numbers.** All of NLP is (1) turn text into numbers (TF-IDF, embeddings) and (2) run a model on those numbers. Master that, and spam filters, sentiment engines, and even the Transformers/BERT of the notes all make sense.

---

## ✅ Everything is tested

All three programs were run end-to-end and their outputs verified: 92% spam accuracy with sensible spam words, correct sentiment predictions (with the crucial "keep negation words" lesson), and a full preprocessing → TF-IDF pipeline.
