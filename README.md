# Hands-on Projects 🛠️

**AI Powered Engineering Upskilling Program**

This folder holds **all the hands-on projects** for the 10-module program — **30 projects in total** (3 per module). Each module's projects turn that module's theory into something you actually build, run, and can show off. The final module is your **capstone**.

> 📖 Every project pairs with the matching module notes in
> [`../Course_Notes/`](../Course_Notes/). Read the notes for the theory; build the projects for the practice.

---

## 🗂️ How this folder is organized

```
Hands-on Projects/
├── Module 1 Hands-on Projects/   ... Module 10 Hands-on Projects/
│   ├── README.md                 <- overview of that module's 3 projects
│   ├── requirements.txt          <- (where installs are needed)
│   ├── Project 1 - .../          <- each project in its own subfolder
│   ├── Project 2 - .../             with its own README + code
│   └── Project 3 - .../
```

Open any module folder's **README first** — it explains the three projects, how they build on each other, and how to run them.

---

## 📚 The 30 projects at a glance

| Module | Theme | Project 1 | Project 2 | Project 3 |
|---|---|---|---|---|
| **1** | Python Fundamentals | Number Guessing Game | Student Management System | File Processing |
| **2** | AI & DS Foundations | AI Use Case Explorer | AI vs ML vs DL Quiz | AI Project Lifecycle Tracker |
| **3** | Data Analysis & Viz | Sales Dashboard | Student Performance Analysis | Data Cleaning Workshop |
| **4** | Machine Learning | House Price Prediction | Customer Churn Prediction | Customer Segmentation |
| **5** | Deep Learning & CV | Digit Recognition | Object Detection | OpenCV Image Processing |
| **6** | NLP | Spam Detection | Sentiment Analysis | Text Preprocessing Toolkit |
| **7** | Generative AI | AI Resume Generator | Research Assistant | Prompt Engineering Lab |
| **8** | AI Agents & Automation | Email Automation | AI Agent with Tools | Multi-Agent Workflow |
| **9** | Deployment & Careers | ML Web App (Flask) | Portfolio Dashboard (Streamlit) | Career Toolkit |
| **10** | **Capstone** | AI Chatbot | Resume Analyzer | Medical Assistant |

The program builds up: pure Python → data → models → deep learning/vision → language → generative AI → agents → **shipping** → a full **capstone**.

---

## ⚙️ Setup & requirements

Most early projects (Modules 1–2) and the "engine" files throughout use **only the Python standard library** — no installs needed.

Later modules use popular libraries. Each module folder that needs them ships a **`requirements.txt`**; install per module:

```bash
cd "Module 4 Hands-on Projects"
pip install -r requirements.txt
```

**Libraries used across the program:** `numpy`, `pandas`, `matplotlib`, `seaborn`, `scikit-learn`, `opencv-python`, `torch` / `ultralytics` (Module 5), `flask`, `streamlit` (Modules 9–10), and optionally `anthropic` for the real-AI modes in Modules 7, 8, and 10.

> ⏳ The **first run** after a fresh install can be slow (a minute or two) while your machine/antivirus scans the newly installed libraries. This is a one-time cost — later runs start quickly.

---

## ▶️ How to run a project

1. Open a terminal **inside that project's folder**.
2. Read its `README.md` for the exact command.
3. Typically one of:
   ```bash
   python main.py            # a script or CLI project
   streamlit run app.py      # a Streamlit web app (Modules 9–10)
   python app.py             # a Flask web app (Module 9)
   ```

Every project's own README lists its run command, sample output, and **challenge ideas** to extend it.

---

## 🤖 A note on "real AI" modes (Modules 7, 8, 10)

Projects that can use a live large language model are **mock-by-default**: they run fully **offline, free, and with no API key** using rule-based or template logic. To switch on the real model:

```bash
pip install anthropic
export ANTHROPIC_API_KEY="sk-ant-..."     # from console.anthropic.com
# then set  USE_REAL_API = True  at the top of the project file
```

This "build the mock first" habit lets you develop and demo everything without cost, then flip one switch for the real thing.

---

## 🔒 A note on data & privacy

All sample names and contact details in these projects (e.g. "Priya Sharma", `priya.example@email.com`) are **fictional placeholders**. Replace them with your own details before showing a project (especially the portfolio and resume tools) to anyone. No real personal data is stored or committed.

> ⚠️ **Module 10's Medical Assistant is an educational demonstration only** — it does not diagnose and is not medical advice. See its README for the full disclaimer.

---

## 🎯 What to do with these projects

- **Build them** alongside the notes as you learn.
- **Complete the challenges** in each project README to make them your own.
- **Deploy your best ones** (Module 9) and put the live links on your GitHub, resume, and LinkedIn.
- **Pick a capstone** (Module 10) as your portfolio centerpiece.

> **Build it, ship it, explain it.** These 30 projects are how you practice that arc — the exact thing an AI engineering role asks for. 🚀
