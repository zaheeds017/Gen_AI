# Capstone B — Resume Analyzer 📄

Paste a **resume** and a **job description**; get a **match score**, the skills you already have vs. the skills you're missing, a resume-health check, and concrete tips. A practical tool you'd actually use — and a clean capstone to demo.

---

## What it does

- Finds known skills in both the resume and the job description.
- **Match score** = (job-required skills you have) / (job-required skills total).
- Health checks: word count, action verbs, contact email, quantified results.
- Prioritised suggestions ("Add these missing skills", "Quantify your results", …).

---

## Files

```
analyzer.py        # the engine: skill matching + scoring + tips (pure Python)
skills_db.json     # the list of known skills + action verbs   <-- EXTEND THIS
app.py             # the Streamlit UI (two text boxes + results)
```

Test the engine directly (no Streamlit needed):
```bash
python analyzer.py
```

---

## ▶️ Run it

```bash
pip install streamlit pandas       # once
streamlit run app.py               # opens http://localhost:8501
```

The app opens with sample text pre-filled — click **Analyze** to see it work, then replace it with your own resume and a real job posting.

---

## How the score works

```
resume skills  = known skills found in the resume
job skills     = known skills found in the job description
match score    = how many job skills the resume covers  (e.g. 3 of 6 = 50%)
```

It's a transparent, rule-based approach: you can always see *why* a score came out the way it did — which is exactly what you want when giving people feedback.

---

## 🎯 Challenges

1. **Grow the skill list:** add skills from your field to `skills_db.json` (the matching updates automatically).
2. **Weight the score:** count "required" skills more than "nice to have" ones.
3. **Upload files:** accept a `.txt` resume via `st.file_uploader` instead of pasting.
4. **LLM feedback (optional):** send the resume to Claude for a human-style rewrite of one weak bullet (see Module 7).

> 💡 Recruiters skim in seconds and many use software to pre-filter. A tool that shows the *gap* between a resume and a job — with fixes — is genuinely useful.
