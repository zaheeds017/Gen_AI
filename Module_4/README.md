# Module 4 — Hands-on Projects 🤖

**AI Powered Engineering Upskilling Program · Machine Learning Essentials**

This is where you **build real Machine Learning models** with **scikit-learn**. Three projects cover all three ML paradigms: **regression**, **classification**, and **clustering**.

> 📖 Full theory for each project is in
> [`Course_Notes/Module_04_Machine_Learning_Essentials.md`](../../Course_Notes/Module_04_Machine_Learning_Essentials.md) (sections 12–14).

---

## ⚙️ One-time setup

```bash
pip install -r requirements.txt
# or:  pip install numpy pandas matplotlib seaborn scikit-learn
```

Check Python first with `python --version` (need **3.10+**).

---

## 📁 Projects

| # | Project | Type | Algorithm | Syllabus link |
|---|---|---|---|---|
| 1 | **House Price Prediction** 🏠 | Supervised — **Regression** | LinearRegression | **House Price Prediction** |
| 2 | **Customer Churn Prediction** 📉 | Supervised — **Classification** | LogisticRegression | **Customer Churn Prediction** |
| 3 | **Customer Segmentation** 🎯 | Unsupervised — **Clustering** | K-Means | *Clustering* (reinforcement) |

Projects 1 & 2 are the **two syllabus activities**. Project 3 reinforces **unsupervised clustering** — the third ML paradigm.

---

## 🧠 The one rhythm behind them all

Every supervised model in scikit-learn is the same four steps:

```python
model = SomeModel()             # 1. choose
model.fit(X_train, y_train)     # 2. train
model.predict(X_test)           # 3. predict
evaluate(y_test, predictions)   # 4. score
```

Learn this rhythm once and you can build almost any model. Clustering (Project 3) is similar but has **no `y`** — it finds structure unsupervised.

---

## ▶️ How to run any project

1. Do the one-time `pip install` above.
2. Open a terminal **inside that project's folder**.
3. Run the `.py` file, e.g.:
   ```bash
   python house_price_prediction.py
   ```
4. Open the generated **`*.png`** chart.

---

## 🔗 How the projects fit the AI lifecycle

```
Module 3 gave you CLEAN DATA  ->  Module 4 turns it into MODELS:
   Regression      -> predict a NUMBER   (price)
   Classification  -> predict a CATEGORY (churn: yes/no)
   Clustering      -> find GROUPS         (segments)
```

Together they cover the core of practical Machine Learning — the foundation for Deep Learning (Module 5) and everything after.
