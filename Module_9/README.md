# Module 9 — Hands-on Projects 🚀🎯

**AI Powered Engineering Upskilling Program · Deployment & Career Readiness**

Modules 1–8 taught you to *build* AI. This module is about the last mile: **shipping** your work so anyone can use it, and **presenting yourself** so recruiters take notice. You will deploy a model as a web app, build an interactive portfolio, and generate your own resume, LinkedIn content, and interview prep.

> 📖 Full theory for each project is in
> [`Course_Notes/Module_09_Deployment_and_Career_Readiness.md`](../../Course_Notes/Module_09_Deployment_and_Career_Readiness.md) (sections 11–13).

---

## ⚙️ Setup

Project 3 needs **no installs** (standard library only). Projects 1 and 2 use small, popular web frameworks:

```bash
pip install -r requirements.txt
```

That installs **Flask** (Project 1), **Streamlit** (Project 2), **scikit-learn**, **joblib**, and **pandas**.

> ⏳ **First run may be slow (a minute or two)** while your machine/antivirus scans the freshly installed scientific libraries. This is a one-time cost — later runs start quickly.

---

## 📁 Projects

| # | Project | You learn | Syllabus link |
|---|---|---|---|
| 1 | **ML Web App (Flask)** 🧠🌐 | Serve a trained model as a web page **and** a JSON API | **Flask**, deployment |
| 2 | **Portfolio Dashboard (Streamlit)** 📊 | Turn a Python script into an interactive showcase | **Streamlit**, **Portfolio Showcase** |
| 3 | **Career Toolkit** 📄💼 | Auto-generate a resume, LinkedIn About, and interview prep | **Resume**, **LinkedIn**, **Interview Preparation** |

Project 2 is the **syllabus activity (Portfolio Showcase)**; Projects 1 & 3 cover the module's other pillars — **deployment** and **career readiness**.

---

## ▶️ How to run each project

```bash
# Project 1 — train once, then start the web server
cd "Project 1 - ML Web App (Flask)"
python train_model.py
python app.py                 # open http://127.0.0.1:5000

# Project 2 — launch the portfolio
cd "Project 2 - Portfolio Dashboard (Streamlit)"
streamlit run app.py          # opens http://localhost:8501

# Project 3 — generate your career documents (no installs)
cd "Project 3 - Career Toolkit (Resume, LinkedIn, Interview)"
python career_toolkit.py      # writes into output/
```

---

## 🔗 How the projects fit together

```
Project 1  →  DEPLOY   : a model becomes a live web app + API others can call
Project 2  →  SHOWCASE : your projects become an interactive portfolio site
Project 3  →  PRESENT  : your story becomes a resume, LinkedIn, and interview prep
```

Together they answer the recruiter's real question: **"Can you build it, ship it, and explain it?"**

---

## 🧠 The big idea of this module

> **A model in a notebook helps no one; a model on the web helps everyone.** Deployment (Flask/Streamlit) + a public portfolio (GitHub) + a sharp resume and interview story are what turn "I studied AI" into "I can do the job." Next up: the **Module 10 Capstone**, where you deploy one complete end-to-end project.

---

## 📝 A note on the sample identity

The example profile ("Priya Sharma", `your-username`, `priya.example@email.com`) is **fictional placeholder data**. Replace it in `profile.json` (Projects 2 & 3) with your own details before showing your portfolio to anyone.
