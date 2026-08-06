"""
============================================================
 PROJECT 2 : CUSTOMER CHURN PREDICTION  (Classification)
 Module 4  : Machine Learning Essentials
 AI Powered Engineering Upskilling Program (2026 Edition)
============================================================

WHAT THIS PROGRAM DOES
----------------------
Builds a SUPERVISED CLASSIFICATION model that predicts whether a
customer will CHURN (leave) - a Yes/No answer. This is one of the most
valuable models in business: keeping a customer is far cheaper than
finding a new one.

    1. CREATE a realistic sample `customers.csv` (only if missing).
    2. PREPARE: features X, label y (churn 0/1), encode the contract
       text, and split into train/test.
    3. TRAIN a Logistic Regression model (with feature scaling).
    4. EVALUATE it properly: accuracy, precision, recall, F1, and a
       CONFUSION MATRIX - because accuracy alone can lie.
    5. PREDICT churn (with a probability) for a new customer.
    6. VISUALIZE the confusion matrix -> churn_confusion_matrix.png.

HOW TO RUN
----------
1. Install once:  pip install scikit-learn pandas numpy matplotlib seaborn
2. In this folder:  python customer_churn_prediction.py
3. Open `churn_confusion_matrix.png`.

CONCEPTS PRACTISED (Module 4)
-----------------------------
- Supervised learning / Classification
- One-hot encoding + feature scaling (StandardScaler)
- train_test_split with stratify (keep class balance)
- LogisticRegression inside a Pipeline
- Classification metrics: accuracy, precision, recall, F1
- The confusion matrix (True/False Positives & Negatives)
- predict_proba (a probability, not just a label)

NOTE ON OUTPUT
--------------
Console text is plain ASCII; the chart is SAVED as a PNG.
"""

import os

import numpy as np
import pandas as pd

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.metrics import (accuracy_score, precision_score, recall_score,
                             f1_score, confusion_matrix, classification_report)

DATA_FILE = "customers.csv"
CHART_FILE = "churn_confusion_matrix.png"

CONTRACTS = ["Month-to-month", "One-year", "Two-year"]
# Month-to-month customers churn far more than long-contract ones.
CONTRACT_EFFECT = {"Month-to-month": 1.2, "One-year": 0.2, "Two-year": -0.5}


def sigmoid(x):
    """Turn any number into a probability between 0 and 1."""
    return 1 / (1 + np.exp(-x))


# ----------------------------------------------------------------------
# STEP 1 : create sample customer data
# ----------------------------------------------------------------------
def create_sample_csv(filename: str) -> None:
    """Generate a customer dataset where churn depends on real factors."""
    if os.path.exists(filename):
        print(f"Note: '{filename}' already exists - using it.")
        return

    rng = np.random.default_rng(42)
    n = 800

    tenure = rng.integers(1, 73, size=n)              # months as a customer
    monthly_charges = rng.uniform(20, 120, size=n).round(2)
    complaints = rng.integers(0, 7, size=n)           # support complaints
    contract = rng.choice(CONTRACTS, size=n)

    # The hidden rule the model must LEARN: churn is more likely with low
    # tenure, high charges, more complaints, and a month-to-month contract.
    logit = (-3.0
             + complaints * 0.9
             + (monthly_charges - 70) * 0.02
             - tenure * 0.04
             + np.array([CONTRACT_EFFECT[c] for c in contract]))
    prob = sigmoid(logit)
    churn = (rng.random(n) < prob).astype(int)        # 1 = left, 0 = stayed

    pd.DataFrame({
        "Tenure": tenure, "MonthlyCharges": monthly_charges,
        "Complaints": complaints, "Contract": contract, "Churn": churn,
    }).to_csv(filename, index=False)
    print(f"Created sample data file '{filename}' with {n} customers "
          f"({churn.mean()*100:.0f}% churned).")


# ----------------------------------------------------------------------
# STEP 2 : prepare the data
# ----------------------------------------------------------------------
def prepare_data(filename: str):
    """Load, one-hot encode the contract, split into train/test."""
    df = pd.read_csv(filename)
    df_encoded = pd.get_dummies(df, columns=["Contract"], drop_first=True)

    y = df_encoded["Churn"]
    X = df_encoded.drop(columns=["Churn"])

    # stratify=y keeps the same churn ratio in both train and test sets.
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y)
    return X, X_train, X_test, y_train, y_test


# ----------------------------------------------------------------------
# STEP 3 + 4 : train and evaluate
# ----------------------------------------------------------------------
def train_and_evaluate(X_train, X_test, y_train, y_test):
    """Train Logistic Regression (scaled) and report classification metrics."""
    # A Pipeline scales the features THEN fits the model - in one object.
    # Scaling matters because features have very different ranges.
    model = make_pipeline(StandardScaler(),
                          LogisticRegression(max_iter=1000, random_state=42))
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    print("\n----- MODEL PERFORMANCE (on unseen test data) -----")
    print(f"Accuracy : {accuracy_score(y_test, y_pred):.3f}  "
          f"(share of all predictions that were correct)")
    print(f"Precision: {precision_score(y_test, y_pred):.3f}  "
          f"(of those we flagged as churn, how many really churned)")
    print(f"Recall   : {recall_score(y_test, y_pred):.3f}  "
          f"(of all real churners, how many we caught)")
    print(f"F1-score : {f1_score(y_test, y_pred):.3f}  "
          f"(balance of precision and recall)")

    print("\nFull classification report:")
    print(classification_report(y_test, y_pred,
                                target_names=["Stayed", "Churned"]))
    return model, y_pred


# ----------------------------------------------------------------------
# STEP 5 : predict a new customer
# ----------------------------------------------------------------------
def predict_new_customer(model, columns) -> None:
    """Predict churn (and its probability) for one new customer."""
    new_customer = pd.DataFrame([{
        "Tenure": 3, "MonthlyCharges": 95.0, "Complaints": 4,
        "Contract_One-year": False, "Contract_Two-year": False,  # month-to-month
    }]).reindex(columns=columns, fill_value=False)

    label = model.predict(new_customer)[0]
    prob = model.predict_proba(new_customer)[0][1]   # probability of churn
    print("----- PREDICTION FOR A NEW CUSTOMER -----")
    print("Customer: 3 months tenure, $95/mo, 4 complaints, month-to-month")
    print(f"Prediction: {'WILL CHURN' if label == 1 else 'will stay'} "
          f"(churn probability {prob*100:.0f}%)")


# ----------------------------------------------------------------------
# STEP 6 : confusion matrix chart
# ----------------------------------------------------------------------
def plot_confusion(y_test, y_pred, filename: str) -> None:
    """Draw the confusion matrix as a labelled heatmap."""
    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(7, 6))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues",
                xticklabels=["Stayed", "Churned"],
                yticklabels=["Stayed", "Churned"])
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.title("Churn Prediction - Confusion Matrix")
    plt.tight_layout()
    plt.savefig(filename, dpi=100)
    plt.close()
    print(f"\n[OK] Confusion matrix saved to '{filename}'.")


def main() -> None:
    print("=" * 54)
    print("      CUSTOMER CHURN PREDICTION (Classification)")
    print("=" * 54)

    create_sample_csv(DATA_FILE)
    X, X_train, X_test, y_train, y_test = prepare_data(DATA_FILE)
    model, y_pred = train_and_evaluate(X_train, X_test, y_train, y_test)
    predict_new_customer(model, X.columns)
    plot_confusion(y_test, y_pred, CHART_FILE)


if __name__ == "__main__":
    main()
