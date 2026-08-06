"""
============================================================
 PROJECT 1 : HOUSE PRICE PREDICTION  (Regression)
 Module 4  : Machine Learning Essentials
 AI Powered Engineering Upskilling Program (2026 Edition)
============================================================

WHAT THIS PROGRAM DOES
----------------------
Builds a SUPERVISED REGRESSION model that predicts a house PRICE (a
number) from its features (area, bedrooms, age, location). This is the
classic "hello world" of machine learning.

    1. CREATE a realistic sample `houses.csv` (only if missing).
    2. PREPARE the data: features X, label y, encode the location text,
       and split into train/test sets.
    3. TRAIN a Linear Regression model  (model.fit).
    4. EVALUATE it: MAE, RMSE, and R2 on the unseen test set.
    5. PREDICT the price of a brand-new house.
    6. VISUALIZE: an "actual vs predicted" scatter -> price_prediction.png.

HOW TO RUN
----------
1. Install once:  pip install scikit-learn pandas numpy matplotlib
2. In this folder:  python house_price_prediction.py
3. Open `price_prediction.png` to see how good the model is.

THE 4-LINE ML RHYTHM (learn this!)
----------------------------------
    model = LinearRegression()      # 1. choose a model
    model.fit(X_train, y_train)     # 2. train it
    predictions = model.predict(X_test)   # 3. predict
    score = r2_score(y_test, predictions) # 4. evaluate

CONCEPTS PRACTISED (Module 4)
-----------------------------
- Supervised learning / Regression
- Features (X) vs Label (y)
- One-hot encoding of categorical text (pd.get_dummies)
- train_test_split (never test on data you trained on!)
- LinearRegression, model coefficients
- Regression metrics: MAE, RMSE, R2

NOTE ON OUTPUT
--------------
Console text is plain ASCII; the chart is SAVED as a PNG so it runs on
any machine.
"""

import os

import numpy as np
import pandas as pd

import matplotlib
matplotlib.use("Agg")            # save charts to a file instead of a window
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

DATA_FILE = "houses.csv"
CHART_FILE = "price_prediction.png"

LOCATIONS = ["City-Center", "Suburb", "Rural"]
# A rough price premium (in rupees) added by each location.
LOCATION_PREMIUM = {"City-Center": 3_000_000, "Suburb": 1_200_000, "Rural": 0}


# ----------------------------------------------------------------------
# STEP 1 : create sample housing data
# ----------------------------------------------------------------------
def create_sample_csv(filename: str) -> None:
    """Generate a realistic housing dataset (only if the file is missing)."""
    if os.path.exists(filename):
        print(f"Note: '{filename}' already exists - using it.")
        return

    rng = np.random.default_rng(42)
    n = 500

    area = rng.integers(500, 3500, size=n)          # square feet
    bedrooms = rng.integers(1, 6, size=n)           # 1..5 bedrooms
    age = rng.integers(0, 40, size=n)               # years old
    location = rng.choice(LOCATIONS, size=n)

    # The "true" price rule the model must LEARN (plus random noise so it is
    # realistic and not perfectly predictable).
    base = (area * 3000) + (bedrooms * 500_000) - (age * 25_000)
    premium = np.array([LOCATION_PREMIUM[loc] for loc in location])
    noise = rng.normal(0, 400_000, size=n)
    price = (base + premium + noise).round(-3).astype(int)   # round to 1000s
    price = np.clip(price, 500_000, None)           # no negative prices

    pd.DataFrame({
        "Area": area, "Bedrooms": bedrooms, "Age": age,
        "Location": location, "Price": price,
    }).to_csv(filename, index=False)
    print(f"Created sample data file '{filename}' with {n} houses.")


# ----------------------------------------------------------------------
# STEP 2 : prepare the data for machine learning
# ----------------------------------------------------------------------
def prepare_data(filename: str):
    """Load the data and split it into train/test features (X) and label (y)."""
    df = pd.read_csv(filename)

    # A model needs NUMBERS. 'Location' is text, so we ONE-HOT ENCODE it:
    # one new 0/1 column per location (drop_first avoids redundancy).
    df_encoded = pd.get_dummies(df, columns=["Location"], drop_first=True)

    # X = all the input FEATURES; y = the LABEL we want to predict.
    y = df_encoded["Price"]
    X = df_encoded.drop(columns=["Price"])

    # Split: 80% to TRAIN on, 20% held back to TEST on (data the model
    # has never seen). random_state makes the split reproducible.
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42)
    return X, X_train, X_test, y_train, y_test


# ----------------------------------------------------------------------
# STEP 3 + 4 : train and evaluate
# ----------------------------------------------------------------------
def train_and_evaluate(X_train, X_test, y_train, y_test):
    """Train Linear Regression and report regression metrics."""
    # The 4-line ML rhythm:
    model = LinearRegression()          # 1. choose
    model.fit(X_train, y_train)         # 2. train (learn the price rule)
    y_pred = model.predict(X_test)      # 3. predict on unseen houses

    # 4. evaluate on the TEST set (the honest measure of quality)
    mae = mean_absolute_error(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    r2 = r2_score(y_test, y_pred)

    print("\n----- MODEL PERFORMANCE (on unseen test data) -----")
    print(f"MAE  (avg error)        : {mae:,.0f}")
    print(f"RMSE (penalizes big miss): {rmse:,.0f}")
    print(f"R2   (0..1, higher better): {r2:.3f}  "
          f"-> the model explains {r2*100:.1f}% of price variation")
    return model, y_pred


# ----------------------------------------------------------------------
# STEP 5 : predict a brand-new house
# ----------------------------------------------------------------------
def predict_new_house(model, columns) -> None:
    """Predict the price of one new house described in code."""
    # Build a single-row DataFrame with the SAME columns the model expects.
    new_house = pd.DataFrame([{
        "Area": 2000, "Bedrooms": 3, "Age": 5,
        "Location_Rural": False, "Location_Suburb": True,   # a Suburb house
    }]).reindex(columns=columns, fill_value=False)

    price = model.predict(new_house)[0]
    print("\n----- PREDICTION FOR A NEW HOUSE -----")
    print("House: 2000 sqft, 3 bedrooms, 5 years old, Suburb")
    print(f"Predicted price: {price:,.0f}")


# ----------------------------------------------------------------------
# STEP 6 : visualize actual vs predicted
# ----------------------------------------------------------------------
def plot_results(y_test, y_pred, filename: str) -> None:
    """Scatter of actual vs predicted prices; the closer to the line, the better."""
    plt.figure(figsize=(8, 8))
    plt.scatter(y_test, y_pred, alpha=0.5, color="#4c72b0")
    # A perfect model would put every point on this diagonal line.
    lo, hi = y_test.min(), y_test.max()
    plt.plot([lo, hi], [lo, hi], "r--", linewidth=2, label="Perfect prediction")
    plt.xlabel("Actual Price")
    plt.ylabel("Predicted Price")
    plt.title("House Price: Actual vs Predicted")
    plt.legend()
    plt.tight_layout()
    plt.savefig(filename, dpi=100)
    plt.close()
    print(f"\n[OK] Chart saved to '{filename}'.")


def main() -> None:
    print("=" * 52)
    print("        HOUSE PRICE PREDICTION (Regression)")
    print("=" * 52)

    create_sample_csv(DATA_FILE)
    X, X_train, X_test, y_train, y_test = prepare_data(DATA_FILE)
    model, y_pred = train_and_evaluate(X_train, X_test, y_train, y_test)

    # Show what the model learned: the weight (coefficient) of each feature.
    print("\n----- WHAT THE MODEL LEARNED (coefficients) -----")
    for feature, coef in zip(X.columns, model.coef_):
        print(f"   {feature:<18}: {coef:+,.0f} per unit")

    predict_new_house(model, X.columns)
    plot_results(y_test, y_pred, CHART_FILE)


if __name__ == "__main__":
    main()
