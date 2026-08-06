"""
portfolio.py - the "brain" of the portfolio app, kept SEPARATE from the UI.

Why separate? Streamlit code (app.py) is about buttons and layout. The plain
logic here -- loading JSON, training the demo model, making a prediction -- has
no Streamlit in it, so it can be imported and TESTED on its own. Keeping logic
out of the UI is a habit that pays off in every real project.
"""

import json
import os

from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

HERE = os.path.dirname(__file__)


def load_json(filename):
    """Read a JSON file that sits next to this script."""
    with open(os.path.join(HERE, filename), "r", encoding="utf-8") as f:
        return json.load(f)


def load_profile():
    return load_json("profile.json")


def load_projects():
    return load_json("projects.json")


def build_model():
    """Train a small Iris classifier. Returns (model, feature_names, target_names).

    In the app this is wrapped in @st.cache_resource so it trains only ONCE,
    not on every click.
    """
    data = load_iris()
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(data.data, data.target)
    return model, list(data.feature_names), list(data.target_names)


def predict(model, target_names, features):
    """features: list of 4 numbers -> (label, {species: probability})."""
    probs = model.predict_proba([features])[0]
    idx = int(probs.argmax())
    proba_map = {str(target_names[i]): round(float(probs[i]), 3)
                 for i in range(len(target_names))}
    return str(target_names[idx]), proba_map


if __name__ == "__main__":
    # A quick self-test you can run without Streamlit:  python portfolio.py
    prof = load_profile()
    print("Profile:", prof["name"], "-", prof["headline"])
    print("Projects:", len(load_projects()))
    m, feats, names = build_model()
    label, proba = predict(m, names, [5.1, 3.5, 1.4, 0.2])
    print("Demo prediction for [5.1,3.5,1.4,0.2]:", label, proba)
