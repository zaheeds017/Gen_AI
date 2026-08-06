"""
app.py - Step 2 of deployment: serve the trained model over the web with Flask.

This one file gives you THREE ways to reach the same model:
  GET  /            -> a friendly HTML form in the browser
  POST /predict     -> the form submits here; shows the predicted species
  POST /api/predict -> a JSON API for other programs (returns JSON)
  GET  /health      -> a tiny "is it alive?" check (used by hosting platforms)

Run:  python app.py     then open http://127.0.0.1:5000

If model.joblib does not exist yet, run  python train_model.py  first.
"""

import os
import joblib
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Load the model ONCE when the server starts (not on every request -- that
# would be slow). If it is missing we keep the app alive but flag it.
MODEL_PATH = os.path.join(os.path.dirname(__file__), "model.joblib")
BUNDLE = joblib.load(MODEL_PATH) if os.path.exists(MODEL_PATH) else None


def predict_species(features):
    """features: list of 4 numbers. Returns (label, {species: probability})."""
    if BUNDLE is None:
        raise RuntimeError("Model not found. Run train_model.py first.")
    model = BUNDLE["model"]
    names = BUNDLE["target_names"]
    probs = model.predict_proba([features])[0]
    idx = int(probs.argmax())
    proba_map = {names[i]: round(float(probs[i]), 3) for i in range(len(names))}
    return names[idx], proba_map


@app.route("/")
def home():
    fields = BUNDLE["feature_names"] if BUNDLE else []
    return render_template("index.html", fields=fields, ready=BUNDLE is not None)


@app.route("/predict", methods=["POST"])
def predict_form():
    # Read the 4 numbers the user typed into the HTML form.
    try:
        features = [float(request.form[name]) for name in BUNDLE["feature_names"]]
    except (KeyError, ValueError):
        return render_template("index.html", fields=BUNDLE["feature_names"],
                               ready=True, error="Please enter 4 valid numbers."), 400
    label, proba = predict_species(features)
    return render_template("index.html", fields=BUNDLE["feature_names"], ready=True,
                           result=label, proba=proba, submitted=features)


@app.route("/api/predict", methods=["POST"])
def predict_api():
    """JSON in, JSON out. Example body: {"features": [5.1, 3.5, 1.4, 0.2]}"""
    data = request.get_json(silent=True) or {}
    features = data.get("features")
    if not isinstance(features, list) or len(features) != 4:
        return jsonify({"error": "Send JSON like {\"features\": [5.1,3.5,1.4,0.2]}"}), 400
    try:
        features = [float(x) for x in features]
    except (TypeError, ValueError):
        return jsonify({"error": "All 4 features must be numbers."}), 400
    label, proba = predict_species(features)
    return jsonify({"prediction": label, "probabilities": proba})


@app.route("/health")
def health():
    return jsonify({"status": "ok", "model_loaded": BUNDLE is not None})


if __name__ == "__main__":
    # debug=True auto-reloads on code changes -- great while learning.
    app.run(host="127.0.0.1", port=5000, debug=True)
