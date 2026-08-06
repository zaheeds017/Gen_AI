# Project 3 — File Processing 📄

**Module 1 · Python for AI & Programming Fundamentals**

A mini **data pipeline**: read a CSV of student marks, compute statistics, and write a clean report (with a text bar chart) to a file. This is exactly what a Data Scientist does every day — done here by hand so you understand what libraries like **Pandas** and **Matplotlib** (Module 3) do for you later.

---

## ▶️ How to run

1. Open a terminal / command prompt **in this folder**.
2. Run:
   ```bash
   python file_processing.py
   ```
3. Open the generated **`report.txt`** to see the full report and bar chart.

> Requires **Python 3.10 or newer**. Nothing to install — it uses only the built-in `csv` and `os` modules.

---

## 🔄 What it does (the pipeline)

```
create_sample_csv  →  read_marks  →  analyze  →  write_report  →  print summary
   (marks.csv)         (records)     (stats)     (report.txt)
```

| File | Role | Created |
|---|---|---|
| `marks.csv` | **input** data | Automatically, on first run (if missing) |
| `report.txt` | **output** report | Every run |

> The sample `marks.csv` is only created if it doesn't already exist, so you can safely edit it and re-run without losing your changes.

---

## 🎮 Sample output

**On screen:**
```
==========================================
          FILE PROCESSING PIPELINE
==========================================

Created sample data file 'marks.csv'.
[OK] Report written to 'report.txt'.

----- QUICK SUMMARY -----
Students processed : 6
Average marks      : 71.17
Highest / Lowest   : 92 / 34
Passed / Failed    : 5 / 1

-> Open 'report.txt' to see the full report and bar chart.
```

**Inside `report.txt`:**
```
==========================================
           STUDENT MARKS REPORT
==========================================

Marks Chart (each * = 10 marks):

Aarav     | *********  92
Ayesha    | ********   88
Rahul     | ****       47
Sneha     | *******    76
Arjun     | ***        34
Priya     | *********  90

------------------------------------------
SUMMARY STATISTICS
------------------------------------------
Count     : 6
Total     : 427
Average   : 71.17
Highest   : 92
Lowest    : 34
Passed    : 5
Failed    : 1
```

> Both the screen output and the report use plain ASCII (the bar chart uses
> `*`, not a special star character) so everything runs and opens cleanly on
> any system, including the default Windows console.

---

## 🧠 Concepts practised

| Concept | Where it's used |
|---|---|
| File reading & writing | `with open(...)` in every step |
| The `csv` module | `csv.reader`, `csv.writer` |
| Functions (pipeline stages) | read / analyze / write |
| Lists & tuples | records as `(name, marks)` |
| Dictionaries | the `stats` result |
| List comprehensions | pass/fail counting |
| Built-in functions | `sum`, `len`, `max`, `min`, `round` |
| Floor division `//` | building the `*` bar chart |
| `try / except` | missing / malformed file handling |

---

## 💡 Try these challenges

1. **Grades column:** add a letter grade to each row in the report (A+/A/B/…).
2. **Sort the chart:** show students from highest to lowest marks.
3. **Median:** add the median mark to the statistics.
4. **Bigger data:** add more rows to `marks.csv` and confirm the stats update.

> **AI connection:** In Module 3 you'll replace this hand-written code with **Pandas** (`df.describe()` gives all these statistics in one line) and **Matplotlib** (real bar charts instead of `*`). Building it by hand first means you'll deeply understand what those powerful tools are doing.
