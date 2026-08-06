"""
============================================================
 PROJECT 2 : STUDENT MANAGEMENT SYSTEM
 Module 1  : Python for AI & Programming Fundamentals
 AI Powered Engineering Upskilling Program (2026 Edition)
============================================================

WHAT THIS PROGRAM DOES
----------------------
A menu-driven console application that lets a teacher manage
student records. You can:
    1. Add a student
    2. View all students (as a neat table)
    3. Search for a student by roll number
    4. Update a student's marks
    5. Delete a student
    6. Save & Exit

All records are saved to a file called `students.json`, so your
data is still there the next time you open the program. This
"load -> change in memory -> save back" pattern is exactly how
real data-driven and AI applications work.

DATA DESIGN
-----------
- Each student is a DICTIONARY:  {"roll": 1, "name": "Aarav", "marks": 92.0}
- All students are stored in a LIST of those dictionaries.

HOW TO RUN
----------
1. Open a terminal in this folder.
2. Type:   python student_management_system.py
3. Use the on-screen menu (type 1-6 and press Enter).

NOTE ON OUTPUT
--------------
All printed text is plain ASCII so the program runs the same on every
terminal (including the default Windows console) without encoding errors.

PYTHON CONCEPTS USED (from Module 1)
------------------------------------
- dictionaries & lists ....... the data model
- functions .................. one function per feature (decomposition)
- loops ...................... searching and displaying records
- if / conditions ............ validation and lookups
- match / case ............... the menu router
- input() + int()/float() .... reading user data
- try / except ............... never crash on bad input or a missing file
- file handling (JSON) ....... json.dump / json.load for saving & loading
- f-strings & formatting ..... aligned table output
"""

import json  # built-in module to read/write JSON files (dict <-> file)

# The file where all student data is stored. Kept as a constant so it is
# easy to change in ONE place if needed.
DATA_FILE = "students.json"


# ----------------------------------------------------------------------
# DATA PERSISTENCE  (load from file / save to file)
# ----------------------------------------------------------------------
def load_students() -> list:
    """
    Load the list of students from the JSON file.

    Returns an empty list on the very first run, when the file does not
    exist yet (FileNotFoundError), or if the file is empty/corrupted.
    """
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)          # JSON in the file -> Python list
    except FileNotFoundError:
        return []                        # first run: no file yet
    except json.JSONDecodeError:
        print("[!] Data file was unreadable; starting with an empty list.")
        return []


def save_students(students: list) -> None:
    """Save the current list of students to the JSON file."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        # indent=4 makes the file human-readable (nicely spaced).
        json.dump(students, f, indent=4)
    print(f"[saved] Data written to '{DATA_FILE}'.")


# ----------------------------------------------------------------------
# SMALL HELPERS
# ----------------------------------------------------------------------
def ask_int(prompt: str):
    """Ask the user for a whole number. Returns None if the input is invalid."""
    try:
        return int(input(prompt))
    except ValueError:
        print("[!] Please enter a valid whole number.")
        return None


def find_by_roll(students: list, roll: int):
    """Return the student dict with this roll number, or None if not found."""
    for student in students:
        if student["roll"] == roll:
            return student
    return None


# ----------------------------------------------------------------------
# FEATURES  (one function per menu option)
# ----------------------------------------------------------------------
def add_student(students: list) -> None:
    """Add a new student record after validating the input."""
    roll = ask_int("Roll number: ")
    if roll is None:
        return

    # Reject duplicate roll numbers so each student is unique.
    if find_by_roll(students, roll) is not None:
        print(f"[!] A student with roll {roll} already exists.")
        return

    name = input("Name: ").strip()
    if name == "":
        print("[!] Name cannot be empty.")
        return

    try:
        marks = float(input("Marks (0-100): "))
    except ValueError:
        print("[!] Marks must be a number.")
        return

    # Store the new student as a dictionary appended to the list.
    students.append({"roll": roll, "name": name, "marks": marks})
    print(f"[OK] Added {name} (roll {roll}).")


def view_students(students: list) -> None:
    """Display all students in a clean, aligned table."""
    if not students:                     # an empty list is "falsy"
        print("(No students yet. Add some first!)")
        return

    # Sort a COPY by roll number so the table is tidy (does not change order
    # of the real list). key=lambda picks the value to sort by.
    ordered = sorted(students, key=lambda s: s["roll"])

    print("\n" + "-" * 40)
    print(f"{'Roll':<6}| {'Name':<20}| {'Marks':>7}")
    print("-" * 40)
    for s in ordered:
        # :<6 left-aligns in 6 chars, :>7 right-aligns in 7 chars.
        print(f"{s['roll']:<6}| {s['name']:<20}| {s['marks']:>7}")
    print("-" * 40)
    print(f"Total students: {len(students)}\n")


def search_student(students: list) -> None:
    """Find and show one student by roll number."""
    roll = ask_int("Enter roll number to search: ")
    if roll is None:
        return

    student = find_by_roll(students, roll)
    if student is not None:
        print(f"Found -> Name: {student['name']}, Marks: {student['marks']}")
    else:
        print(f"[X] No student found with roll {roll}.")


def update_student(students: list) -> None:
    """Update the marks of an existing student."""
    roll = ask_int("Enter roll number to update: ")
    if roll is None:
        return

    student = find_by_roll(students, roll)
    if student is None:
        print(f"[X] No student found with roll {roll}.")
        return

    try:
        student["marks"] = float(input(f"New marks for {student['name']}: "))
        print("[OK] Marks updated.")
    except ValueError:
        print("[!] Marks must be a number. No change made.")


def delete_student(students: list) -> None:
    """Delete a student by roll number."""
    roll = ask_int("Enter roll number to delete: ")
    if roll is None:
        return

    student = find_by_roll(students, roll)
    if student is None:
        print(f"[X] No student found with roll {roll}.")
        return

    students.remove(student)             # remove that dict from the list
    print(f"[OK] Deleted {student['name']} (roll {roll}).")


# ----------------------------------------------------------------------
# MAIN MENU LOOP
# ----------------------------------------------------------------------
MENU = """
========= STUDENT MANAGEMENT SYSTEM =========
1. Add Student
2. View All Students
3. Search Student
4. Update Marks
5. Delete Student
6. Save & Exit
=============================================
"""


def main() -> None:
    # Load any previously saved data when the program starts.
    students = load_students()
    print(f"Loaded {len(students)} student record(s).")

    while True:
        print(MENU)
        choice = input("Choose an option (1-6): ").strip()

        # `match` compares `choice` against each `case`. It is a clean
        # alternative to a long if/elif chain (Python 3.10+).
        match choice:
            case "1":
                add_student(students)
            case "2":
                view_students(students)
            case "3":
                search_student(students)
            case "4":
                update_student(students)
            case "5":
                delete_student(students)
            case "6":
                save_students(students)  # save before leaving
                print("Goodbye!")
                break
            case _:                      # `_` means "anything else" (default)
                print("[!] Invalid choice. Please pick a number from 1 to 6.")


# Standard entry point - only runs main() when this file is executed directly.
if __name__ == "__main__":
    # Wrap main() so that pressing Ctrl+C (KeyboardInterrupt) or the input
    # stream ending (EOFError) exits politely instead of showing a scary
    # error message.
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\n\nExited without saving. Goodbye!")
