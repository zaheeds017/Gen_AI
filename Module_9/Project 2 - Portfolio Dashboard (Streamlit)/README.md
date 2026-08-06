# Project 2 — Portfolio Dashboard (Streamlit) 📊

**This is the module's syllabus activity: your Portfolio Showcase.** Build an interactive personal site — About, Projects, a **live ML demo**, and Contact — from a plain Python script, using **Streamlit**.

---

## What it does

A multi-page app driven by a sidebar:

| Page | Shows |
|---|---|
| **About** | Your intro + a bar chart of your skills |
| **Projects** | Cards built from `projects.json` with tags and links |
| **Live ML Demo** | Sliders that predict an Iris species **in real time** |
| **Contact** | Your email, GitHub, LinkedIn |

The magic of Streamlit: **every slider move re-runs the script and redraws the page.** You write Python; Streamlit handles the web.

---

## Files

```
app.py          # the Streamlit UI (pages, sidebar, widgets)
portfolio.py    # the "brain": load JSON, train the demo model, predict (no Streamlit)
profile.json    # your name, headline, about, skills   <-- EDIT THIS
projects.json   # your list of projects                <-- EDIT THIS
```

Logic lives in `portfolio.py` (which you can test with `python portfolio.py`); the UI lives in `app.py`. Keeping them apart is a good habit.

---

## ▶️ Run it

```bash
pip install streamlit scikit-learn pandas     # once
streamlit run app.py
```

Your browser opens at **http://localhost:8501**. Edit `profile.json` / `projects.json`, save, and the app **live-reloads**.

> ⏳ First launch can take a minute while libraries load; after that it is quick.

---

## 🌐 Deploy it free (Streamlit Community Cloud)

1. Push this folder to a **public GitHub repo** (include a `requirements.txt` listing `streamlit scikit-learn pandas`).
2. Go to **share.streamlit.io**, connect your GitHub, pick the repo and `app.py`.
3. You get a public URL like `https://your-app.streamlit.app` — put it on your resume and LinkedIn.

---

## 🎯 Challenges

1. **Make it yours**: replace every field in `profile.json` and `projects.json` with your real details and projects.
2. **Add a "Resume" page** that shows a download button for your PDF (`st.download_button`).
3. **Add a metric row** on About using `st.metric` (e.g. "Projects built: 6", "Modules completed: 10").
4. **Swap the demo**: load *your own* saved model (from Project 1) instead of the Iris model.

> 💡 A live portfolio URL is worth more than a line on a resume — it lets people *use* your work in 10 seconds.
