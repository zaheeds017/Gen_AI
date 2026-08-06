"""
============================================================
 PROJECT 3 : FILE PROCESSING
 Module 1  : Python for AI & Programming Fundamentals
 AI Powered Engineering Upskilling Program (2026 Edition)
============================================================

WHAT THIS PROGRAM DOES
----------------------
This is a mini "data pipeline" - the everyday job of a Data
Scientist, done by hand so you understand what tools like Pandas
do for you later (Module 3).

Steps:
    1. CREATE a sample data file `marks.csv` (only if it doesn't exist).
    2. READ the data from the CSV file.
    3. ANALYZE it: count, total, average, highest, lowest, pass/fail.
    4. WRITE a nicely formatted `report.txt`, including a simple
       text-based bar chart of each student's marks.
    5. PRINT a quick summary to the screen.

HOW TO RUN
----------
1. Open a terminal in this folder.
2. Type:   python file_processing.py
3. Open the generated `report.txt` to see the full report.

FILES INVOLVED
--------------
- marks.csv   (input)  -> created automatically the first time you run it
- report.txt  (output) -> generated every run

NOTE ON OUTPUT
--------------
All printed and written text is plain ASCII so the program runs the same
on every terminal (including the default Windows console) without any
encoding errors, and the report opens cleanly in any text editor.

PYTHON CONCEPTS USED (from Module 1)
------------------------------------
- file handling (read & write) ... open(), with-statement
- the csv module ................. csv.reader / csv.writer
- functions ...................... read / analyze / write, cleanly split
- lists & tuples ................. records stored as (name, marks) tuples
- dictionaries ................... statistics packed into one dict
- list comprehensions ............ filtering pass/fail
- built-in functions ............. sum(), len(), max(), min(), round()
- try / except ................... handle a missing or malformed file
- integer/floor division ......... marks // 10 for the star bar chart
"""

import csv    # built-in module for reading/writing CSV (spreadsheet) files
import os     # built-in module to check whether a file already exists

# File names kept as constants so they're easy to find and change.
INPUT_FILE = "marks.csv"
OUTPUT_FILE = "report.txt"
PASS_MARK = 40   # the minimum marks needed to pass


# ----------------------------------------------------------------------
# STEP 1 : create some sample data to work with
# ----------------------------------------------------------------------
def create_sample_csv(filename: str) -> None:
    """
    Create a sample marks.csv file - but only if it doesn't already exist,
    so we never overwrite real data the user may have added.
    """
    if os.path.exists(filename):
        print(f"Note: '{filename}' already exists - using the existing file.")
        return

    # A header row followed by (Name, Marks) rows.
    rows = [
        ["Name", "Marks"],
        ["Aarav", 92],
        ["Ayesha", 88],
        ["Rahul", 47],
        ["Sneha", 76],
        ["Arjun", 34],
        ["Priya", 90],
    ]

    # newline="" is the recommended setting when writing CSV files so that
    # blank lines are not inserted between rows on Windows.
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(rows)   # write ALL rows at once
    print(f"Created sample data file '{filename}'.")


# ----------------------------------------------------------------------
# STEP 2 : read the data from the CSV file
# ----------------------------------------------------------------------
def read_marks(filename: str) -> list:
    """
    Read a CSV of (Name, Marks) and return a list of (name, marks) tuples.

    Returns an empty list if the file is missing or a row is malformed.
    """
    records = []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            next(reader)                 # skip the header row ("Name","Marks")
            for row in reader:
                if len(row) < 2:         # skip blank / broken lines
                    continue
                name = row[0].strip()
                marks = int(row[1])      # convert the text "92" -> number 92
                records.append((name, marks))
    except FileNotFoundError:
        print(f"[X] File '{filename}' not found.")
    except ValueError:
        print("[!] A marks value was not a valid number - check the CSV.")
    return records


# ----------------------------------------------------------------------
# STEP 3 : analyze the data
# ----------------------------------------------------------------------
def analyze(records: list) -> dict:
    """Compute summary statistics and return them as a dictionary."""
    # A list comprehension: pull just the marks out of the (name, marks) pairs.
    marks_list = [marks for name, marks in records]

    stats = {
        "count": len(marks_list),
        "total": sum(marks_list),
        "average": round(sum(marks_list) / len(marks_list), 2),
        "highest": max(marks_list),
        "lowest": min(marks_list),
        # Count how many are >= PASS_MARK (passed) and how many are below (failed).
        "passed": len([m for m in marks_list if m >= PASS_MARK]),
        "failed": len([m for m in marks_list if m < PASS_MARK]),
    }
    return stats


# ----------------------------------------------------------------------
# STEP 4 : write a formatted report file
# ----------------------------------------------------------------------
def write_report(records: list, stats: dict, filename: str) -> None:
    """Write a human-readable report, including a text bar chart, to a file."""
    with open(filename, "w", encoding="utf-8") as f:
        f.write("=" * 42 + "\n")
        f.write("           STUDENT MARKS REPORT\n")
        f.write("=" * 42 + "\n\n")

        # --- a simple text bar chart: one '*' for every 10 marks -----------
        f.write("Marks Chart (each * = 10 marks):\n\n")
        for name, marks in records:
            stars = "*" * (marks // 10)   # floor division: 92 // 10 -> 9 stars
            f.write(f"{name:<10}| {stars:<10} {marks}\n")

        # --- summary statistics --------------------------------------------
        f.write("\n" + "-" * 42 + "\n")
        f.write("SUMMARY STATISTICS\n")
        f.write("-" * 42 + "\n")
        for key, value in stats.items():
            # .capitalize() turns "average" into "Average" for a nicer label.
            f.write(f"{key.capitalize():<10}: {value}\n")

    print(f"[OK] Report written to '{filename}'.")


# ----------------------------------------------------------------------
# MAIN : run the whole pipeline in order
# ----------------------------------------------------------------------
def main() -> None:
    print("=" * 42)
    print("          FILE PROCESSING PIPELINE")
    print("=" * 42 + "\n")

    # Step 1 + 2: make sure data exists, then read it.
    create_sample_csv(INPUT_FILE)
    records = read_marks(INPUT_FILE)

    # Guard clause: if there is no data, stop early instead of crashing.
    if not records:
        print("No data to process. Exiting.")
        return

    # Step 3 + 4: analyze and write the report.
    stats = analyze(records)
    write_report(records, stats, OUTPUT_FILE)

    # Step 5: print a quick summary to the screen too.
    print("\n----- QUICK SUMMARY -----")
    print(f"Students processed : {stats['count']}")
    print(f"Average marks      : {stats['average']}")
    print(f"Highest / Lowest   : {stats['highest']} / {stats['lowest']}")
    print(f"Passed / Failed    : {stats['passed']} / {stats['failed']}")
    print(f"\n-> Open '{OUTPUT_FILE}' to see the full report and bar chart.")


if __name__ == "__main__":
    main()
