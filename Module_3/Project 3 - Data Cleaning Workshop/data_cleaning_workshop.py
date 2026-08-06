"""
============================================================
 PROJECT 3 : DATA CLEANING WORKSHOP
 Module 3  : Data Analysis & Visualization
 AI Powered Engineering Upskilling Program (2026 Edition)
============================================================

WHY THIS PROJECT MATTERS
------------------------
Data scientists spend about 80% of their time CLEANING data, not
building models - "garbage in, garbage out" (Module 2). This project
takes a deliberately MESSY dataset and cleans it step by step, so you
learn the real, unglamorous, most-important skill in data work.

WHAT THIS PROGRAM DOES
----------------------
    1. CREATE a messy sample `messy_data.csv` full of common problems:
         - duplicate rows
         - missing values
         - inconsistent text (spacing, upper/lower case)
         - inconsistent categories ("M", "male", "Male")
         - numbers stored as text ("50,000", "unknown")
         - impossible outliers (Age = 250)
    2. CLEAN it in 5 clear steps, printing what changed at each step.
    3. SAVE the result as `cleaned_data.csv`.

HOW TO RUN
----------
1. Install the libraries once:  pip install pandas numpy
2. Open a terminal in this folder.
3. Type:   python data_cleaning_workshop.py

FILES INVOLVED
--------------
- messy_data.csv    (input)  -> auto-created on first run
- cleaned_data.csv  (output) -> the cleaned result

CONCEPTS PRACTISED (Module 3)
-----------------------------
- Pandas ........... read_csv, drop_duplicates, str methods, fillna, median
- NumPy ............ np.nan for marking missing / invalid values
- Data cleaning .... every core technique in one place
- The .str accessor  vectorised text cleaning (strip, lower, title, replace)

NOTE ON OUTPUT
--------------
All console text is plain ASCII, so it runs on every terminal.
"""

import os

import numpy as np
import pandas as pd

MESSY_FILE = "messy_data.csv"
CLEAN_FILE = "cleaned_data.csv"


# ----------------------------------------------------------------------
# STEP 0 : create a deliberately messy dataset
# ----------------------------------------------------------------------
def create_messy_csv(filename: str) -> None:
    """Write a small but realistically messy dataset (only if missing)."""
    if os.path.exists(filename):
        print(f"Note: '{filename}' already exists - using it.")
        return

    # Each row is a customer. The mess is intentional and reproducible.
    rows = [
        {"CustomerID": 1, "Name": "  ravi kumar ", "City": "mumbai",
         "Gender": "M", "Age": "25", "Income": "50,000"},
        {"CustomerID": 2, "Name": "PRIYA SHARMA", "City": "Delhi ",
         "Gender": "female", "Age": "31", "Income": "72,000"},
        {"CustomerID": 3, "Name": "amit  verma", "City": "  chennai",
         "Gender": "male", "Age": "", "Income": "unknown"},
        {"CustomerID": 4, "Name": "Sneha Rao", "City": "MUMBAI",
         "Gender": "F", "Age": "28", "Income": "65,000"},
        {"CustomerID": 5, "Name": "karan mehta", "City": "delhi",
         "Gender": "Male", "Age": "250", "Income": "90,000"},   # outlier age
        {"CustomerID": 6, "Name": "Neha Gupta ", "City": "Chennai",
         "Gender": "f", "Age": "35", "Income": ""},              # missing income
        {"CustomerID": 7, "Name": "arjun singh", "City": "delhi ",
         "Gender": "m", "Age": "40", "Income": "1,10,000"},
        {"CustomerID": 8, "Name": "Divya Nair", "City": " mumbai ",
         "Gender": "Female", "Age": "", "Income": "55,000"},     # missing age
    ]

    # Add DUPLICATE rows (exact copies of rows 1 and 4) - a very common problem.
    rows.append(dict(rows[0]))
    rows.append(dict(rows[3]))

    pd.DataFrame(rows).to_csv(filename, index=False)
    print(f"Created messy sample file '{filename}' with {len(rows)} rows "
          f"(including duplicates).")


# ----------------------------------------------------------------------
# Small helper to print a labelled snapshot of the data
# ----------------------------------------------------------------------
def show(df: pd.DataFrame, title: str) -> None:
    print(f"\n----- {title} -----")
    print(f"Shape: {df.shape[0]} rows x {df.shape[1]} columns")
    print(f"Missing values per column:\n{df.isna().sum().to_string()}")


# ----------------------------------------------------------------------
# THE CLEANING PIPELINE (5 steps)
# ----------------------------------------------------------------------
def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean the messy DataFrame in five clearly-labelled steps."""

    # --- STEP 1: remove duplicate rows ---------------------------------
    before = len(df)
    df = df.drop_duplicates()
    print(f"\n[Step 1] Removed {before - len(df)} duplicate row(s). "
          f"{len(df)} rows remain.")

    # --- STEP 2: clean text columns (whitespace + consistent case) -----
    # .str.replace(r"\s+", " ") collapses any run of spaces into a single one,
    # so "amit  verma" (double space) becomes "amit verma".
    df["Name"] = (df["Name"].str.strip()
                  .str.replace(r"\s+", " ", regex=True)
                  .str.title())                          # "  ravi  kumar " -> "Ravi Kumar"
    df["City"] = df["City"].str.strip().str.title()      # " mumbai " / "MUMBAI" -> "Mumbai"
    print("[Step 2] Trimmed spaces and fixed the case of Name and City.")

    # --- STEP 3: standardize the Gender categories ---------------------
    gender_map = {"m": "Male", "male": "Male", "f": "Female", "female": "Female"}
    df["Gender"] = df["Gender"].str.strip().str.lower().map(gender_map)
    print("[Step 3] Standardized Gender to just 'Male' / 'Female'.")

    # --- STEP 4: fix numeric columns stored as text --------------------
    # Income has commas and the word 'unknown'; remove commas, coerce to number.
    df["Income"] = (
        df["Income"].astype(str)
        .str.replace(",", "", regex=False)
        .replace({"unknown": np.nan, "": np.nan})
    )
    df["Income"] = pd.to_numeric(df["Income"], errors="coerce")
    df["Age"] = pd.to_numeric(df["Age"], errors="coerce")
    print("[Step 4] Converted Age and Income from text to real numbers.")

    # --- STEP 5: handle outliers, then fill missing values -------------
    # An Age above 100 is almost certainly an error -> mark it missing.
    outliers = int((df["Age"] > 100).sum())
    df.loc[df["Age"] > 100, "Age"] = np.nan

    # Fill missing Age and Income with the MEDIAN (robust to outliers).
    age_median = df["Age"].median()
    income_median = df["Income"].median()
    df["Age"] = df["Age"].fillna(age_median).round().astype(int)
    df["Income"] = df["Income"].fillna(income_median).astype(int)
    print(f"[Step 5] Replaced {outliers} impossible age(s), then filled "
          f"missing Age with median {age_median:.0f} and missing "
          f"Income with median {income_median:.0f}.")

    return df


def main() -> None:
    print("=" * 52)
    print("            DATA CLEANING WORKSHOP")
    print("=" * 52)

    create_messy_csv(MESSY_FILE)
    df = pd.read_csv(MESSY_FILE)

    show(df, "BEFORE CLEANING (raw messy data)")
    print("\nRaw data preview:")
    print(df.to_string(index=False))

    df = clean_data(df)

    show(df, "AFTER CLEANING")
    print("\nCleaned data preview:")
    print(df.to_string(index=False))

    df.to_csv(CLEAN_FILE, index=False)
    print(f"\n[OK] Cleaned data saved to '{CLEAN_FILE}'.")
    print("Lesson: real data is messy - cleaning is ~80% of a data job!")


if __name__ == "__main__":
    main()
