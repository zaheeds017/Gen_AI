"""
============================================================
 PROJECT 1 : AI USE CASE EXPLORER
 Module 2  : AI & Data Science Foundations
 AI Powered Engineering Upskilling Program (2026 Edition)
============================================================

WHAT THIS PROGRAM DOES
----------------------
This is the hands-on version of the syllabus activity "AI Use Case
Discussion". Instead of only talking about where AI is useful, you
CATALOG real AI use cases and PRIORITIZE them like a professional
AI team does.

For each use case you record:
    - the industry (Healthcare, Finance, Retail, ...)
    - the problem it solves
    - the AI type (Machine Learning, Deep Learning, NLP, ...)
    - an IMPACT score      (1 = tiny, 5 = huge business value)
    - a FEASIBILITY score  (1 = very hard, 5 = easy to build)

The program then ranks the use cases and places each one in the
Impact-vs-Feasibility matrix from the notes:

    Impact HIGH + Feasibility HIGH  -> "Quick Win"    (do first)
    Impact HIGH + Feasibility LOW   -> "Big Bet"      (plan carefully)
    Impact LOW  + Feasibility HIGH  -> "Low Priority"
    Impact LOW  + Feasibility LOW   -> "Avoid"

All data is saved to `ai_use_cases.json` so it survives between runs.

HOW TO RUN
----------
1. Open a terminal in this folder.
2. Type:   python ai_use_case_explorer.py
3. Use the on-screen menu (type 1-5 and press Enter).

CONCEPTS PRACTISED (Module 1 skills applied to Module 2 ideas)
--------------------------------------------------------------
- dictionaries & lists ....... each use case is a dict; all in a list
- functions .................. one job per function (decomposition)
- input validation ........... scores must be whole numbers 1-5
- match / case ............... the menu router
- sorting with a key ......... rank by priority score
- file handling (JSON) ....... save & load the catalog
- f-strings & formatting ..... aligned tables

NOTE ON OUTPUT
--------------
All printed text is plain ASCII so the program runs the same on every
terminal, including the default Windows console.
"""

import json

DATA_FILE = "ai_use_cases.json"

# A few real-world examples so the tool is useful immediately on first run.
SAMPLE_CASES = [
    {"industry": "Healthcare", "problem": "Detect tumors in X-ray/CT scans",
     "ai_type": "Computer Vision", "impact": 5, "feasibility": 3},
    {"industry": "Finance", "problem": "Flag fraudulent card transactions",
     "ai_type": "Machine Learning", "impact": 5, "feasibility": 4},
    {"industry": "Retail", "problem": "Recommend products to shoppers",
     "ai_type": "Machine Learning", "impact": 4, "feasibility": 5},
    {"industry": "Customer Service", "problem": "Answer FAQs with a chatbot",
     "ai_type": "Generative AI (NLP)", "impact": 3, "feasibility": 5},
    {"industry": "Agriculture", "problem": "Predict crop disease from leaf photos",
     "ai_type": "Deep Learning", "impact": 4, "feasibility": 2},
]

# A score of 4 or 5 is treated as "HIGH".
HIGH = 4


# ----------------------------------------------------------------------
# DATA PERSISTENCE
# ----------------------------------------------------------------------
def load_cases() -> list:
    """Load use cases from JSON, or seed with the sample cases on first run."""
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        # list(...) makes a COPY so we never modify the SAMPLE_CASES template.
        return [dict(case) for case in SAMPLE_CASES]
    except json.JSONDecodeError:
        print("[!] Data file unreadable; starting from the sample cases.")
        return [dict(case) for case in SAMPLE_CASES]


def save_cases(cases: list) -> None:
    """Save the current catalog to the JSON file."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(cases, f, indent=4)
    print(f"[saved] {len(cases)} use case(s) written to '{DATA_FILE}'.")


# ----------------------------------------------------------------------
# HELPERS
# ----------------------------------------------------------------------
def ask_score(prompt: str):
    """Ask for a whole number from 1 to 5. Returns None if the input is bad."""
    try:
        value = int(input(prompt))
    except ValueError:
        print("[!] Please enter a whole number.")
        return None
    if value < 1 or value > 5:
        print("[!] The score must be between 1 and 5.")
        return None
    return value


def priority_label(impact: int, feasibility: int) -> str:
    """Return the Impact-vs-Feasibility quadrant name for a use case."""
    high_impact = impact >= HIGH
    high_feasibility = feasibility >= HIGH
    if high_impact and high_feasibility:
        return "Quick Win"
    if high_impact and not high_feasibility:
        return "Big Bet"
    if not high_impact and high_feasibility:
        return "Low Priority"
    return "Avoid"


def priority_score(case: dict) -> int:
    """A single number used to rank use cases (higher = do sooner)."""
    return case["impact"] * case["feasibility"]


# ----------------------------------------------------------------------
# FEATURES
# ----------------------------------------------------------------------
def add_case(cases: list) -> None:
    """Add a new AI use case after validating every field."""
    industry = input("Industry (e.g. Healthcare): ").strip()
    problem = input("Problem it solves: ").strip()
    ai_type = input("AI type (ML / DL / NLP / Computer Vision / GenAI): ").strip()
    if industry == "" or problem == "":
        print("[!] Industry and problem cannot be empty.")
        return

    impact = ask_score("Impact score (1-5, 5 = huge value): ")
    if impact is None:
        return
    feasibility = ask_score("Feasibility score (1-5, 5 = easy to build): ")
    if feasibility is None:
        return

    cases.append({
        "industry": industry,
        "problem": problem,
        "ai_type": ai_type,
        "impact": impact,
        "feasibility": feasibility,
    })
    print(f"[OK] Added use case in '{industry}'.")


def view_cases(cases: list) -> None:
    """Show every use case in an aligned table."""
    if not cases:
        print("(No use cases yet. Add one from the menu.)")
        return

    print("\n" + "-" * 82)
    print(f"{'#':<3}| {'Industry':<17}| {'AI Type':<20}| {'Imp':<4}| {'Fea':<4}| Problem")
    print("-" * 82)
    for i, c in enumerate(cases, start=1):
        print(f"{i:<3}| {c['industry']:<17}| {c['ai_type']:<20}| "
              f"{c['impact']:<4}| {c['feasibility']:<4}| {c['problem']}")
    print("-" * 82)
    print(f"Total use cases: {len(cases)}\n")


def prioritize(cases: list) -> None:
    """Rank use cases by priority score and show their quadrant."""
    if not cases:
        print("(No use cases to prioritize yet.)")
        return

    # sorted() with a key ranks the list without changing the original order.
    ranked = sorted(cases, key=priority_score, reverse=True)

    print("\n=== AI USE CASES BY PRIORITY (highest first) ===")
    print(f"{'Rank':<5}| {'Score':<6}| {'Quadrant':<13}| Use Case")
    print("-" * 70)
    for rank, c in enumerate(ranked, start=1):
        label = priority_label(c["impact"], c["feasibility"])
        score = priority_score(c)
        print(f"{rank:<5}| {score:<6}| {label:<13}| "
              f"{c['industry']} - {c['problem']}")
    print("-" * 70)
    print("Tip: build the 'Quick Win' items first; plan the 'Big Bet' items.\n")


# ----------------------------------------------------------------------
# MAIN MENU
# ----------------------------------------------------------------------
MENU = """
============ AI USE CASE EXPLORER ============
1. Add a use case
2. View all use cases
3. Prioritize (rank + quadrant)
4. Save & Exit
=============================================
"""


def main() -> None:
    cases = load_cases()
    print(f"Loaded {len(cases)} AI use case(s).")

    while True:
        print(MENU)
        choice = input("Choose an option (1-4): ").strip()
        match choice:
            case "1":
                add_case(cases)
            case "2":
                view_cases(cases)
            case "3":
                prioritize(cases)
            case "4":
                save_cases(cases)
                print("Goodbye!")
                break
            case _:
                print("[!] Invalid choice. Please pick a number from 1 to 4.")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\n\nExited without saving. Goodbye!")
