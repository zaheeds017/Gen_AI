# Module 3 — Hands-on Projects 🛠️

**AI Powered Engineering Upskilling Program · Data Analysis & Visualization**

Module 3 is where you start working with **real data** using the professional data-science stack: **NumPy, Pandas, Matplotlib, and Seaborn**. These projects put the AI-lifecycle stages *collect → clean → explore → visualize* into practice.

> 📖 Full theory for each project is in
> [`Course_Notes/Module_03_Data_Analysis_and_Visualization.md`](../../Course_Notes/Module_03_Data_Analysis_and_Visualization.md) (sections 12–14).

---

## ⚙️ One-time setup (required for this module)

Unlike Modules 1–2 (built-in modules only), Module 3 needs external libraries:

```bash
pip install -r requirements.txt
# or:  pip install numpy pandas matplotlib seaborn
```

Check Python first with `python --version` (need **3.10+**).

---

## 📁 Projects

| # | Project | Folder | Libraries | Syllabus link |
|---|---|---|---|---|
| 1 | **Sales Dashboard** 📊 | [`Project 1 - Sales Dashboard/`](Project%201%20-%20Sales%20Dashboard/) | Pandas, Matplotlib | **Sales Dashboard** |
| 2 | **Student Performance Analysis** 🎓 | [`Project 2 - Student Performance Analysis/`](Project%202%20-%20Student%20Performance%20Analysis/) | Pandas, NumPy, Seaborn | **Student Performance Analysis** |
| 3 | **Data Cleaning Workshop** 🧹 | [`Project 3 - Data Cleaning Workshop/`](Project%203%20-%20Data%20Cleaning%20Workshop/) | Pandas, NumPy | *Data Cleaning* (reinforcement) |

Projects 1 & 2 are the **two syllabus activities**. Project 3 is a focused reinforcement of **data cleaning** — "the 80% job".

---

## ▶️ How to run any project

1. Do the one-time `pip install` above.
2. Open a terminal **inside that project's folder**.
3. Run the `.py` file, e.g.:
   ```bash
   python sales_dashboard.py
   ```
4. For Projects 1 & 2, open the generated **`*.png`** dashboard image.

---

## 🔗 How the projects connect

```
Project 3  →  CLEAN     : fix messy raw data (the foundation)
Project 1  →  DASHBOARD : aggregate & visualize business data
Project 2  →  EXPLORE   : full EDA with statistics + correlation
```

**Recommended order: 3 → 1 → 2** — learn to clean data first, then analyze and visualize it. (You can also do 1 → 2 → 3; each project is self-contained.)

---

## ✅ From hand-written code to real tools

In **Module 1's** File Processing project you computed statistics and drew a `*` bar chart **by hand**. These projects show the professional way: `df.describe()` replaces dozens of lines, and Matplotlib/Seaborn draw real charts. Same ideas — vastly more powerful tools.
