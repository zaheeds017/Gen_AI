"""
============================================================
 PROJECT 2 : STUDENT PERFORMANCE ANALYSIS
 Module 3  : Data Analysis & Visualization
 AI Powered Engineering Upskilling Program (2026 Edition)
============================================================

WHAT THIS PROGRAM DOES
----------------------
A full Exploratory Data Analysis (EDA) of student exam performance
using Pandas, NumPy and Seaborn - exactly stages 2-4 of the AI
lifecycle (collect -> clean -> explore) from Module 2.

    1. CREATE a realistic sample `students.csv` (with a few missing
       values on purpose, so we can practise cleaning).
    2. LOAD and CLEAN it (fill missing marks with the column average).
    3. ANALYZE it: describe(), subject averages, pass/fail, and the
       correlation between STUDY HOURS and MARKS.
    4. VISUALIZE it with Seaborn: distribution, subject averages,
       study-hours vs marks scatter, and a correlation heatmap.
    5. SAVE a text report `performance_report.txt`.

HOW TO RUN
----------
1. Install the libraries once:  pip install pandas numpy seaborn matplotlib
2. Open a terminal in this folder.
3. Type:   python student_performance_analysis.py
4. Open `performance_dashboard.png` to see the charts.

FILES INVOLVED
--------------
- students.csv               (input)  -> auto-created on first run
- performance_dashboard.png  (output) -> the Seaborn chart grid
- performance_report.txt     (output) -> the text analysis report

CONCEPTS PRACTISED (Module 3)
-----------------------------
- NumPy ............ generating correlated sample data
- Pandas ........... DataFrame, describe(), mean(), fillna(), corr(), groupby
- Data cleaning .... detecting and filling missing values
- EDA .............. summary statistics and correlation
- Seaborn .......... histplot, barplot, regplot, heatmap
- Matplotlib ....... the 2x2 figure that holds the Seaborn charts

NOTE ON OUTPUT
--------------
Console text is plain ASCII. Charts are saved to a PNG (file backend),
so this runs on any machine; just open the image afterwards.
"""

import os

import numpy as np
import pandas as pd
import seaborn as sns

import matplotlib
matplotlib.use("Agg")           # save charts to a file instead of a window
import matplotlib.pyplot as plt

DATA_FILE = "students.csv"
DASHBOARD_FILE = "performance_dashboard.png"
REPORT_FILE = "performance_report.txt"

SUBJECTS = ["Math", "Science", "English"]
PASS_MARK = 40


# ----------------------------------------------------------------------
# STEP 1 : create sample data (NumPy) - marks depend on study hours
# ----------------------------------------------------------------------
def create_sample_csv(filename: str) -> None:
    """Generate a sample student dataset (only if the file is missing)."""
    if os.path.exists(filename):
        print(f"Note: '{filename}' already exists - using it.")
        return

    rng = np.random.default_rng(7)
    n = 60

    study_hours = rng.integers(1, 15, size=n)          # 1..14 hours/week
    attendance = rng.integers(50, 101, size=n)         # 50..100 percent
    gender = rng.choice(["Male", "Female"], size=n)

    def marks_from(base_skill):
        # Marks rise with study hours + a personal skill + noise, clipped 0-100.
        raw = 25 + 3.5 * study_hours + base_skill + rng.normal(0, 8, size=n)
        return np.clip(raw, 0, 100).round().astype(int)

    df = pd.DataFrame({
        "StudentID": [f"S{i:02d}" for i in range(1, n + 1)],
        "Gender": gender,
        "Math": marks_from(rng.normal(0, 10, size=n)),
        "Science": marks_from(rng.normal(0, 10, size=n)),
        "English": marks_from(rng.normal(0, 10, size=n)),
        "Attendance": attendance,
        "StudyHours": study_hours,
    })

    # Introduce a few MISSING values on purpose (so we can practise cleaning).
    df.loc[3, "Math"] = np.nan
    df.loc[10, "Science"] = np.nan
    df.loc[25, "English"] = np.nan

    df.to_csv(filename, index=False)
    print(f"Created sample data file '{filename}' with {n} students.")


# ----------------------------------------------------------------------
# STEP 2 : load and clean (Pandas)
# ----------------------------------------------------------------------
def load_and_clean(filename: str) -> pd.DataFrame:
    """Load the data and fill missing marks with each subject's average."""
    df = pd.read_csv(filename)

    missing_before = int(df[SUBJECTS].isna().sum().sum())
    for subject in SUBJECTS:
        # Fill any blank marks with the average (mean) of that subject.
        df[subject] = df[subject].fillna(round(df[subject].mean()))
    print(f"Data cleaning: filled {missing_before} missing mark(s) "
          f"with the subject average.")

    # Add helpful derived columns.
    df["Total"] = df[SUBJECTS].sum(axis=1)
    df["Percentage"] = (df["Total"] / (len(SUBJECTS) * 100) * 100).round(1)
    # A student passes only if they clear the pass mark in EVERY subject.
    df["Result"] = np.where((df[SUBJECTS] >= PASS_MARK).all(axis=1),
                            "Pass", "Fail")
    return df


# ----------------------------------------------------------------------
# STEP 3 : analyze (Pandas / EDA)
# ----------------------------------------------------------------------
def analyze(df: pd.DataFrame) -> dict:
    """Compute the key exploratory statistics."""
    numeric_cols = SUBJECTS + ["Attendance", "StudyHours", "Percentage"]
    return {
        "subject_avg": df[SUBJECTS].mean().round(1),
        "overall_avg": round(df["Percentage"].mean(), 1),
        "topper": df.loc[df["Percentage"].idxmax(), "StudentID"],
        "top_percentage": df["Percentage"].max(),
        "pass_count": int((df["Result"] == "Pass").sum()),
        "fail_count": int((df["Result"] == "Fail").sum()),
        "gender_avg": df.groupby("Gender")["Percentage"].mean().round(1),
        # How strongly study hours relate to final percentage (-1..+1).
        "study_corr": round(df["StudyHours"].corr(df["Percentage"]), 2),
        "corr_matrix": df[numeric_cols].corr(),
    }


# ----------------------------------------------------------------------
# STEP 4 : visualize (Seaborn)
# ----------------------------------------------------------------------
def build_dashboard(df: pd.DataFrame, stats: dict, filename: str) -> None:
    """Draw four Seaborn charts on a 2x2 grid and save as one PNG."""
    sns.set_theme(style="whitegrid")            # nice Seaborn styling
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle("Student Performance Analysis", fontsize=18, fontweight="bold")

    # (1) Distribution of final percentages
    sns.histplot(df["Percentage"], bins=10, kde=True, ax=axes[0, 0], color="#4c72b0")
    axes[0, 0].set_title("Distribution of Percentage")

    # (2) Average marks per subject
    subject_avg = stats["subject_avg"]
    sns.barplot(x=subject_avg.index, y=subject_avg.values, ax=axes[0, 1],
                hue=subject_avg.index, palette="viridis", legend=False)
    axes[0, 1].set_title("Average Marks by Subject")
    axes[0, 1].set_ylabel("Average Mark")
    axes[0, 1].set_xlabel("Subject")

    # (3) Study hours vs percentage, with a regression line
    sns.regplot(data=df, x="StudyHours", y="Percentage", ax=axes[1, 0],
                scatter_kws={"color": "#55a868"}, line_kws={"color": "#c44e52"})
    axes[1, 0].set_title(f"Study Hours vs Percentage (corr = {stats['study_corr']})")

    # (4) Correlation heatmap of the numeric columns
    sns.heatmap(stats["corr_matrix"], annot=True, cmap="coolwarm", fmt=".2f",
                ax=axes[1, 1], cbar=False)
    axes[1, 1].set_title("Correlation Heatmap")

    fig.tight_layout(rect=(0, 0, 1, 0.96))
    fig.savefig(filename, dpi=100)
    plt.close(fig)
    print(f"[OK] Dashboard image saved to '{filename}'.")


# ----------------------------------------------------------------------
# STEP 5 : text report
# ----------------------------------------------------------------------
def write_report(df: pd.DataFrame, stats: dict, filename: str) -> None:
    """Save a plain-text analysis report."""
    with open(filename, "w", encoding="utf-8") as f:
        f.write("=" * 50 + "\n")
        f.write("        STUDENT PERFORMANCE REPORT\n")
        f.write("=" * 50 + "\n\n")
        f.write(f"Students analyzed : {len(df)}\n")
        f.write(f"Overall average % : {stats['overall_avg']}\n")
        f.write(f"Topper            : {stats['topper']} "
                f"({stats['top_percentage']}%)\n")
        f.write(f"Passed / Failed   : {stats['pass_count']} / "
                f"{stats['fail_count']}\n")
        f.write(f"Study-vs-marks correlation : {stats['study_corr']} "
                f"(closer to 1 = studying helps more)\n\n")

        f.write("Average marks by subject:\n")
        for subject, value in stats["subject_avg"].items():
            f.write(f"   {subject:<10}: {value}\n")

        f.write("\nAverage percentage by gender:\n")
        for gender, value in stats["gender_avg"].items():
            f.write(f"   {gender:<10}: {value}\n")

        f.write("\nStatistical summary (describe):\n")
        f.write(df[SUBJECTS + ["Percentage"]].describe().round(1).to_string())
        f.write("\n")
    print(f"[OK] Text report saved to '{filename}'.")


def main() -> None:
    print("=" * 50)
    print("       STUDENT PERFORMANCE ANALYSIS")
    print("=" * 50 + "\n")

    create_sample_csv(DATA_FILE)
    df = load_and_clean(DATA_FILE)
    stats = analyze(df)
    build_dashboard(df, stats, DASHBOARD_FILE)
    write_report(df, stats, REPORT_FILE)

    print("\n----- QUICK SUMMARY -----")
    print(f"Students        : {len(df)}")
    print(f"Overall average : {stats['overall_avg']}%")
    print(f"Topper          : {stats['topper']} ({stats['top_percentage']}%)")
    print(f"Passed / Failed : {stats['pass_count']} / {stats['fail_count']}")
    print(f"Study vs marks  : correlation {stats['study_corr']}")
    print(f"\n-> Open '{DASHBOARD_FILE}' to view the charts.")


if __name__ == "__main__":
    main()
