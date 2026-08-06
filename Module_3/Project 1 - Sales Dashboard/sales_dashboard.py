"""
============================================================
 PROJECT 1 : SALES DASHBOARD
 Module 3  : Data Analysis & Visualization
 AI Powered Engineering Upskilling Program (2026 Edition)
============================================================

WHAT THIS PROGRAM DOES
----------------------
A complete mini "business intelligence" pipeline using Pandas and
Matplotlib - the daily work of a Data Analyst:

    1. CREATE a realistic sample `sales.csv` (only if it is missing).
    2. LOAD it into a Pandas DataFrame.
    3. CLEAN it (parse dates, fix types).
    4. ANALYZE it: total revenue, best region, top products, monthly trend.
    5. VISUALIZE it: build a 4-chart dashboard image `sales_dashboard.png`.
    6. SAVE a text KPI report `sales_report.txt`.

HOW TO RUN
----------
1. Install the libraries once:   pip install pandas matplotlib
2. Open a terminal in this folder.
3. Type:   python sales_dashboard.py
4. Open the generated `sales_dashboard.png` to see your dashboard.

FILES INVOLVED
--------------
- sales.csv            (input)  -> auto-created on first run if missing
- sales_dashboard.png  (output) -> the 4-chart dashboard image
- sales_report.txt     (output) -> the text KPI summary

CONCEPTS PRACTISED (Module 3)
-----------------------------
- NumPy ............ generating the sample data with a random generator
- Pandas ........... DataFrame, read_csv, groupby, sort_values, dt accessor
- Data cleaning .... parsing dates, ensuring numeric types
- Aggregation ...... sum(), mean(), groupby totals
- Matplotlib ....... bar, line, barh, and pie charts on a 2x2 grid

NOTE ON OUTPUT
--------------
Console text is plain ASCII so it runs on every terminal. Charts are
SAVED as a PNG file (using Matplotlib's file backend) so the program
works even on machines without a screen; just open the image after.
"""

import os

import numpy as np
import pandas as pd

# Use the "Agg" backend: it draws charts straight to image files instead of
# opening a window. This makes the program run anywhere and simply produces
# a PNG you can open. (Set the backend BEFORE importing pyplot.)
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

DATA_FILE = "sales.csv"
DASHBOARD_FILE = "sales_dashboard.png"
REPORT_FILE = "sales_report.txt"

# Product catalog: each product maps to a category and a unit price.
CATALOG = {
    "Laptop": ("Electronics", 55000),
    "Phone": ("Electronics", 25000),
    "Headphones": ("Accessories", 2000),
    "Keyboard": ("Accessories", 1500),
    "Monitor": ("Electronics", 12000),
    "Chair": ("Furniture", 8000),
    "Desk": ("Furniture", 10000),
}
REGIONS = ["North", "South", "East", "West"]


# ----------------------------------------------------------------------
# STEP 1 : create sample data (NumPy)
# ----------------------------------------------------------------------
def create_sample_csv(filename: str) -> None:
    """Generate a realistic sample sales dataset, only if the file is missing."""
    if os.path.exists(filename):
        print(f"Note: '{filename}' already exists - using it.")
        return

    # A seeded random generator makes the data reproducible for everyone.
    rng = np.random.default_rng(42)
    n = 400  # number of sales transactions

    products = list(CATALOG.keys())
    # Random dates across the first 6 months of 2025.
    start = np.datetime64("2025-01-01")
    dates = start + rng.integers(0, 181, size=n).astype("timedelta64[D]")

    chosen_products = rng.choice(products, size=n)
    rows = []
    for date, product in zip(dates, chosen_products):
        category, price = CATALOG[product]
        units = int(rng.integers(1, 11))          # 1 to 10 units
        revenue = units * price
        rows.append({
            "Date": np.datetime_as_string(date, unit="D"),
            "Region": rng.choice(REGIONS),
            "Product": product,
            "Category": category,
            "Units": units,
            "Revenue": revenue,
        })

    pd.DataFrame(rows).to_csv(filename, index=False)
    print(f"Created sample data file '{filename}' with {n} rows.")


# ----------------------------------------------------------------------
# STEP 2 + 3 : load and clean (Pandas)
# ----------------------------------------------------------------------
def load_data(filename: str) -> pd.DataFrame:
    """Load the CSV into a DataFrame and clean the important columns."""
    df = pd.read_csv(filename)

    # Parse the Date text column into real datetime values so we can group
    # by month later. errors='coerce' turns any bad date into NaT (missing).
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

    # Make sure the numeric columns really are numbers.
    df["Units"] = pd.to_numeric(df["Units"], errors="coerce")
    df["Revenue"] = pd.to_numeric(df["Revenue"], errors="coerce")

    # Drop any rows that failed to parse (basic data cleaning).
    df = df.dropna(subset=["Date", "Units", "Revenue"])

    # A tidy 'Month' label like '2025-01' for grouping and the trend chart.
    df["Month"] = df["Date"].dt.to_period("M").astype(str)
    return df


# ----------------------------------------------------------------------
# STEP 4 : analyze (Pandas aggregation)
# ----------------------------------------------------------------------
def analyze(df: pd.DataFrame) -> dict:
    """Compute the key performance indicators (KPIs) as a dictionary."""
    revenue_by_region = df.groupby("Region")["Revenue"].sum().sort_values(ascending=False)
    revenue_by_product = df.groupby("Product")["Revenue"].sum().sort_values(ascending=False)
    revenue_by_category = df.groupby("Category")["Revenue"].sum().sort_values(ascending=False)
    revenue_by_month = df.groupby("Month")["Revenue"].sum().sort_index()

    return {
        "total_revenue": int(df["Revenue"].sum()),
        "total_units": int(df["Units"].sum()),
        "num_orders": len(df),
        "avg_order_value": round(df["Revenue"].mean(), 2),
        "best_region": revenue_by_region.index[0],
        "best_product": revenue_by_product.index[0],
        "by_region": revenue_by_region,
        "by_product": revenue_by_product,
        "by_category": revenue_by_category,
        "by_month": revenue_by_month,
    }


# ----------------------------------------------------------------------
# STEP 5 : visualize (Matplotlib) -> one dashboard image
# ----------------------------------------------------------------------
def build_dashboard(kpis: dict, filename: str) -> None:
    """Draw four charts on a 2x2 grid and save it as one PNG dashboard."""
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle("Sales Dashboard", fontsize=18, fontweight="bold")

    # (1) Revenue by Region - vertical bar chart
    kpis["by_region"].plot(kind="bar", ax=axes[0, 0], color="#4c72b0")
    axes[0, 0].set_title("Revenue by Region")
    axes[0, 0].set_ylabel("Revenue")
    axes[0, 0].tick_params(axis="x", rotation=0)

    # (2) Monthly Revenue Trend - line chart
    kpis["by_month"].plot(kind="line", marker="o", ax=axes[0, 1], color="#dd8452")
    axes[0, 1].set_title("Monthly Revenue Trend")
    axes[0, 1].set_ylabel("Revenue")
    axes[0, 1].tick_params(axis="x", rotation=45)

    # (3) Top products - horizontal bar chart (top first at the top)
    kpis["by_product"].sort_values().plot(kind="barh", ax=axes[1, 0], color="#55a868")
    axes[1, 0].set_title("Revenue by Product")
    axes[1, 0].set_xlabel("Revenue")

    # (4) Category share - pie chart
    axes[1, 1].pie(kpis["by_category"].values, labels=list(kpis["by_category"].index),
                   autopct="%1.1f%%", startangle=90)
    axes[1, 1].set_title("Revenue Share by Category")

    fig.tight_layout(rect=(0, 0, 1, 0.96))   # leave room for the suptitle
    fig.savefig(filename, dpi=100)
    plt.close(fig)
    print(f"[OK] Dashboard image saved to '{filename}'.")


# ----------------------------------------------------------------------
# STEP 6 : text KPI report
# ----------------------------------------------------------------------
def write_report(kpis: dict, filename: str) -> None:
    """Save a plain-text KPI summary."""
    with open(filename, "w", encoding="utf-8") as f:
        f.write("=" * 45 + "\n")
        f.write("             SALES KPI REPORT\n")
        f.write("=" * 45 + "\n\n")
        f.write(f"Total Revenue     : {kpis['total_revenue']:,}\n")
        f.write(f"Total Units Sold  : {kpis['total_units']:,}\n")
        f.write(f"Number of Orders  : {kpis['num_orders']:,}\n")
        f.write(f"Avg Order Value   : {kpis['avg_order_value']:,}\n")
        f.write(f"Best Region       : {kpis['best_region']}\n")
        f.write(f"Best Product      : {kpis['best_product']}\n\n")
        f.write("Revenue by Region:\n")
        for region, value in kpis["by_region"].items():
            f.write(f"   {region:<8}: {int(value):,}\n")
    print(f"[OK] Text report saved to '{filename}'.")


def main() -> None:
    print("=" * 45)
    print("            SALES DASHBOARD PIPELINE")
    print("=" * 45 + "\n")

    create_sample_csv(DATA_FILE)
    df = load_data(DATA_FILE)
    if df.empty:
        print("No data to analyze. Exiting.")
        return

    kpis = analyze(df)
    build_dashboard(kpis, DASHBOARD_FILE)
    write_report(kpis, REPORT_FILE)

    # Quick on-screen summary (plain ASCII).
    print("\n----- QUICK SUMMARY -----")
    print(f"Total revenue : {kpis['total_revenue']:,}")
    print(f"Orders        : {kpis['num_orders']:,}")
    print(f"Best region   : {kpis['best_region']}")
    print(f"Best product  : {kpis['best_product']}")
    print(f"\n-> Open '{DASHBOARD_FILE}' to view the dashboard.")


if __name__ == "__main__":
    main()
