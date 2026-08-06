"""
============================================================
 PROJECT 3 : CUSTOMER SEGMENTATION  (Clustering)
 Module 4  : Machine Learning Essentials
 AI Powered Engineering Upskilling Program (2026 Edition)
============================================================

WHAT THIS PROGRAM DOES
----------------------
Builds an UNSUPERVISED CLUSTERING model that groups customers into
segments based on their income and spending - WITHOUT any labels. The
algorithm discovers the groups by itself. Marketing teams use exactly
this to target each segment differently.

    1. CREATE a sample `mall_customers.csv` (only if missing).
    2. SCALE the features (clustering needs comparable scales).
    3. Use the ELBOW METHOD to sanity-check the number of clusters.
    4. TRAIN a K-Means model to find the segments.
    5. DESCRIBE each segment (average income, spending, size, a name).
    6. VISUALIZE: an elbow plot + a colored segment scatter -> segments.png.

HOW TO RUN
----------
1. Install once:  pip install scikit-learn pandas numpy matplotlib
2. In this folder:  python customer_segmentation.py
3. Open `segments.png`.

CONCEPTS PRACTISED (Module 4)
-----------------------------
- Unsupervised learning / Clustering (no labels!)
- Feature scaling with StandardScaler
- K-Means: fit, cluster labels, centroids, inertia
- The Elbow Method for choosing k
- Interpreting and NAMING clusters (turning math into business value)

NOTE ON OUTPUT
--------------
Console text is plain ASCII; charts are SAVED as a PNG.
"""

import os

import numpy as np
import pandas as pd

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

DATA_FILE = "mall_customers.csv"
CHART_FILE = "segments.png"
N_CLUSTERS = 5


# ----------------------------------------------------------------------
# STEP 1 : create sample data (5 natural groups + noise)
# ----------------------------------------------------------------------
def create_sample_csv(filename: str) -> None:
    """Generate mall-customer data with a few natural groups baked in."""
    if os.path.exists(filename):
        print(f"Note: '{filename}' already exists - using it.")
        return

    rng = np.random.default_rng(42)
    # Each tuple is a hidden segment: (income_center, spend_center, count).
    groups = [
        (30, 30, 40),   # low income, low spending
        (80, 20, 40),   # high income, low spending (savers)
        (30, 80, 40),   # low income, high spending (spenders)
        (85, 82, 40),   # high income, high spending (premium)
        (55, 50, 40),   # middle of the road
    ]
    incomes, scores = [], []
    for inc_c, spend_c, count in groups:
        incomes.append(rng.normal(inc_c, 7, count))
        scores.append(rng.normal(spend_c, 7, count))

    income = np.clip(np.concatenate(incomes), 10, 140).round(1)
    spending = np.clip(np.concatenate(scores), 1, 100).round(1)

    pd.DataFrame({
        "CustomerID": range(1, len(income) + 1),
        "AnnualIncome_k": income,
        "SpendingScore": spending,
    }).to_csv(filename, index=False)
    print(f"Created sample data file '{filename}' with {len(income)} customers.")


# ----------------------------------------------------------------------
# STEP 2 : the Elbow Method (helps choose the number of clusters)
# ----------------------------------------------------------------------
def compute_elbow(X_scaled, max_k=10):
    """Return the inertia (within-cluster spread) for k = 1..max_k."""
    inertias = []
    for k in range(1, max_k + 1):
        km = KMeans(n_clusters=k, random_state=42, n_init=10)
        km.fit(X_scaled)
        inertias.append(km.inertia_)     # lower = tighter clusters
    return inertias


# ----------------------------------------------------------------------
# STEP 3 : give each cluster a human-friendly name
# ----------------------------------------------------------------------
def name_segment(income: float, spending: float) -> str:
    """Turn a cluster's average income & spending into a business label."""
    # Sort each value into a band: low / mid / high (with a middle gap).
    def band(value, low_edge, high_edge):
        if value < low_edge:
            return "low"
        if value > high_edge:
            return "high"
        return "mid"

    inc = band(income, 45, 65)        # <45 low, 45-65 mid, >65 high
    spend = band(spending, 40, 60)    # <40 low, 40-60 mid, >60 high

    if inc == "mid" and spend == "mid":
        return "Average"
    if inc == "high" and spend == "high":
        return "Premium (VIP - target!)"
    if inc == "high" and spend == "low":
        return "Savers (win them over)"
    if inc == "low" and spend == "high":
        return "Young Spenders"
    if inc == "low" and spend == "low":
        return "Budget"
    return "Average"


def main() -> None:
    print("=" * 52)
    print("        CUSTOMER SEGMENTATION (Clustering)")
    print("=" * 52)

    create_sample_csv(DATA_FILE)
    df = pd.read_csv(DATA_FILE)

    # Features to cluster on (no label exists - this is unsupervised!).
    X = df[["AnnualIncome_k", "SpendingScore"]]

    # Scaling matters: income (10-140) and spending (1-100) have different
    # ranges; without scaling, income would dominate the distance maths.
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # STEP: elbow, then fit the final K-Means with k = N_CLUSTERS.
    inertias = compute_elbow(X_scaled)
    kmeans = KMeans(n_clusters=N_CLUSTERS, random_state=42, n_init=10)
    df["Segment"] = kmeans.fit_predict(X_scaled)   # each customer's cluster

    # Describe every segment (averages + size + a name).
    print("\n----- CUSTOMER SEGMENTS FOUND -----")
    summary = df.groupby("Segment")[["AnnualIncome_k", "SpendingScore"]].mean().round(1)
    sizes = df["Segment"].value_counts().sort_index()
    for seg in summary.index:
        inc = summary.loc[seg, "AnnualIncome_k"]
        spend = summary.loc[seg, "SpendingScore"]
        print(f"   Segment {seg}: {sizes[seg]:>3} customers | "
              f"avg income {inc:>5}k | avg spend {spend:>5} | "
              f"{name_segment(inc, spend)}")

    # --- VISUALIZE: elbow (left) + segment scatter (right) ---
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))

    axes[0].plot(range(1, 11), inertias, marker="o")
    axes[0].axvline(N_CLUSTERS, color="red", linestyle="--",
                    label=f"chosen k = {N_CLUSTERS}")
    axes[0].set_title("Elbow Method (pick k at the 'elbow')")
    axes[0].set_xlabel("Number of clusters (k)")
    axes[0].set_ylabel("Inertia (lower = tighter)")
    axes[0].legend()

    scatter = axes[1].scatter(df["AnnualIncome_k"], df["SpendingScore"],
                              c=df["Segment"], cmap="viridis", s=40)
    # Plot the cluster centers (convert them back to the original scale).
    centers = scaler.inverse_transform(kmeans.cluster_centers_)
    axes[1].scatter(centers[:, 0], centers[:, 1], c="red", marker="X",
                    s=250, edgecolors="black", label="Centroids")
    axes[1].set_title("Customer Segments")
    axes[1].set_xlabel("Annual Income (k)")
    axes[1].set_ylabel("Spending Score (1-100)")
    axes[1].legend()

    fig.tight_layout()
    fig.savefig(CHART_FILE, dpi=100)
    plt.close(fig)
    print(f"\n[OK] Charts saved to '{CHART_FILE}'.")
    print("Insight: target the 'Premium' segment; win back the 'Savers'.")


if __name__ == "__main__":
    main()
