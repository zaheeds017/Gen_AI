# Project 2 — Student Management System 🎓

**Module 1 · Python for AI & Programming Fundamentals**

A menu-driven console app to **add, view, search, update, and delete** student records. All data is saved to a `students.json` file, so it persists between runs. This is a classic **CRUD** application (Create, Read, Update, Delete) — the backbone of every data-driven and AI system.

---

## ▶️ How to run

1. Open a terminal / command prompt **in this folder**.
2. Run:
   ```bash
   python student_management_system.py
   ```
3. Use the menu: type a number `1`–`6` and press Enter.

> Requires **Python 3.10 or newer** (uses the `match` statement). Nothing to install — it only uses the built-in `json` module.

---

## 🗂️ How data is stored

- Each student is a **dictionary**: `{"roll": 1, "name": "Aarav", "marks": 92.0}`
- All students live in a **list** of those dictionaries.
- On **Save & Exit**, the list is written to `students.json`. Example file:

```json
[
    {
        "roll": 1,
        "name": "Aarav",
        "marks": 92.0
    },
    {
        "roll": 2,
        "name": "Ayesha",
        "marks": 88.0
    }
]
```

> The file `students.json` is created automatically the first time you save. You can delete it to start fresh.

---

## 🎮 Sample run

```
Loaded 0 student record(s).

========= STUDENT MANAGEMENT SYSTEM =========
1. Add Student ... 6. Save & Exit
=============================================
Choose an option (1-6): 1
Roll number: 1
Name: Aarav
Marks (0-100): 92
[OK] Added Aarav (roll 1).

Choose an option (1-6): 2
----------------------------------------
Roll  | Name                |   Marks
----------------------------------------
1     | Aarav               |    92.0
----------------------------------------
Total students: 1

Choose an option (1-6): 6
[saved] Data written to 'students.json'.
Goodbye!
```

> The program prints plain ASCII (no emoji) so it runs identically on
> every terminal, including the default Windows console.

---

## 🧠 Concepts practised

| Concept | Where it's used |
|---|---|
| Dictionaries & lists | the whole data model |
| Functions (decomposition) | one function per feature |
| `match / case` | the menu router in `main()` |
| Loops | `find_by_roll()`, `view_students()` |
| `try / except` | validating numbers & handling a missing file |
| File handling (JSON) | `load_students()`, `save_students()` |
| String formatting | aligned table with `:<6`, `:>7` |
| `if __name__ == "__main__"` | program entry point |

---

## 💡 Try these challenges

1. **Sort options:** add a menu item to view students sorted by **marks** (highest first).
2. **Class stats:** show the class **average, topper, and lowest** scorer.
3. **Grades:** display a letter grade (A+/A/B/…) next to each student's marks.
4. **Auto-save:** save after every change instead of only on exit.

> **AI connection:** loading records → changing them in memory → saving back is the exact workflow you'll use for **datasets** in Data Science (Module 3) and for storing **model results** later in the program.
