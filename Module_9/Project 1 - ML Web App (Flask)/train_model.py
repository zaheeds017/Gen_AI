"""
train_model.py - Step 1 of deploying a model.

We train a small classifier on the classic Iris flower dataset and SAVE it to
disk (model.joblib). The web app (app.py) will later LOAD this file and use it
to make predictions -- it never re-trains. This "train once, load many times"
split is exactly how real ML deployment works.

Run:  python train_model.py
"""

import joblib
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


def train_and_save(model_path="model.joblib"):
    # 1) Load data: 150 flowers, 4 measurements each, 3 species.
    data = load_iris()
    X, y = data.data, data.target
    feature_names = list(data.feature_names)   # e.g. 'sepal length (cm)'
    target_names = list(data.target_names)     # ['setosa','versicolor','virginica']

    # 2) Split so we can honestly measure accuracy on unseen flowers.
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # 3) Train.
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # 4) Report honest accuracy.
    acc = accuracy_score(y_test, model.predict(X_test))
    print("Test accuracy: {:.1%}".format(acc))

    # 5) Save EVERYTHING the app needs in one bundle: the model + the label
    #    names + the feature names. Now the app is self-contained.
    bundle = {
        "model": model,
        "feature_names": feature_names,
        "target_names": target_names,
    }
    joblib.dump(bundle, model_path)
    print("Saved model bundle to:", model_path)
    return acc


if __name__ == "__main__":
    train_and_save()
