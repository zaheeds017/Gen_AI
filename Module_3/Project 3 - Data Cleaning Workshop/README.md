# Project 3 — Data Cleaning Workshop 🧹

**Module 3 · Data Analysis & Visualization**

Data scientists spend about **80% of their time cleaning data**, not building models. This project takes a deliberately **messy** dataset and cleans it in **5 clear steps** with **Pandas** — the single most important, most-neglected skill in data work.

---

## ▶️ How to run

1. Install the libraries once:
   ```bash
   pip install pandas numpy
   ```
2. Open a terminal **in this folder** and run:
   ```bash
   python data_cleaning_workshop.py
   ```

> Requires **Python 3.x**. The messy `messy_data.csv` is auto-created on first run; the result is saved as `cleaned_data.csv`.

---

## 🐛 The mess (on purpose)

| Problem | Example in the data |
|---|---|
| Duplicate rows | rows 1 & 4 appear twice |
| Missing values | blank Age / Income |
| Messy text | `"  ravi kumar "`, `"MUMBAI"`, `" delhi"` |
| Inconsistent categories | Gender as `M`, `male`, `Female`, `f` |
| Numbers as text | Income `"50,000"`, `"unknown"` |
| Impossible outlier | Age `250` |

## ✨ The 5-step clean

```
Step 1  drop_duplicates()          -> remove exact duplicate rows
Step 2  .str.strip().str.title()   -> tidy Name & City text
Step 3  map to Male/Female         -> standardize categories
Step 4  to_numeric(errors=coerce)  -> turn text into real numbers
Step 5  handle outliers + fillna   -> cap bad ages, fill blanks with median
```

---

## 🎮 Sample output (before → after)

```
BEFORE:  10 rows, Age has 2 missing, Income has 1 missing, Age max = 250
AFTER :   8 rows, 0 missing anywhere, all text tidy, all numbers real
```

```
Cleaned data preview:
 CustomerID         Name    City Gender  Age  Income
          1   Ravi Kumar  Mumbai   Male   25   50000
          2 Priya Sharma   Delhi Female   31   72000
          3   Amit Verma Chennai   Male   31   68500
          ...
```

---

## 🧠 Concepts practised

Pandas `drop_duplicates`, the `.str` accessor (`strip`, `replace`, `title`, `lower`), `map`, `to_numeric(errors="coerce")`, `fillna`, `median` · NumPy `np.nan` for marking bad values · the whole real-world cleaning toolkit in one place.

---

## 💡 Challenges

1. Add a **duplicate-by-CustomerID** check (keep the first occurrence).
2. Standardize a messy **date** column into one format with `pd.to_datetime`.
3. Instead of filling missing Income with the median, **drop** those rows and compare the result.
4. Detect outliers automatically using the **IQR rule** instead of a fixed `Age > 100`.
