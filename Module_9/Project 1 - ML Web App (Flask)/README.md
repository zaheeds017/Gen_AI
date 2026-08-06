# Project 1 — ML Web App (Flask) 🧠🌐

Deploy a trained machine-learning model as a **real web app**: an HTML form for humans **and** a JSON API for other programs. This is the single most common way ML reaches users in industry.

---

## What it does

You train a Random Forest on the classic **Iris** flower dataset, save it to disk, then serve it with **Flask**:

| Route | Method | Purpose |
|---|---|---|
| `/` | GET | A friendly HTML form (4 measurement fields) |
| `/predict` | POST | The form submits here; shows the predicted species + a probability bar chart |
| `/api/predict` | POST | JSON in, JSON out — for other apps/scripts |
| `/health` | GET | A tiny "is it alive?" check hosting platforms use |

---

## Files

```
train_model.py      # Step 1: train the model, save model.joblib
app.py              # Step 2: load the model, serve it with Flask
templates/index.html# The web page (Flask fills in the {{ ... }} parts)
model.joblib        # Created by train_model.py (a saved model bundle)
```

---

## ▶️ Run it

```bash
pip install flask scikit-learn joblib      # once
python train_model.py                      # trains + saves model.joblib
python app.py                              # starts the server
```

Then open **http://127.0.0.1:5000** in your browser.

Try the **JSON API** from a second terminal:
```bash
curl -X POST http://127.0.0.1:5000/api/predict \
     -H "Content-Type: application/json" \
     -d "{\"features\":[5.1,3.5,1.4,0.2]}"
# -> {"prediction":"setosa","probabilities":{"setosa":1.0,...}}
```

---

## How it works (the deployment idea)

```
TRAIN ONCE                         SERVE MANY TIMES
train_model.py  --->  model.joblib  --->  app.py loads it at startup
                                          every request just calls model.predict
```

Training is slow and happens **once**; prediction is fast and happens on **every request**. Separating them is the heart of real ML deployment.

---

## 🎯 Challenges (try these)

1. **Swap the model** in `train_model.py` (e.g. `LogisticRegression`) and compare accuracy — no change needed in `app.py`.
2. **Add a `/api/info` route** that returns the feature names and species list as JSON.
3. **Show the confidence** ("87% sure") as text above the bar chart in `index.html`.
4. **Deploy it free**: push to GitHub, then host on Render or Railway (see notes §13). Add a `Procfile` with `web: gunicorn app:app`.

> 💡 A model in a notebook helps no one; a model behind a URL helps everyone.
