"""
============================================================
 PROJECT 3 : AI PROJECT LIFECYCLE TRACKER
 Module 2  : AI & Data Science Foundations
 AI Powered Engineering Upskilling Program (2026 Edition)
============================================================

WHAT THIS PROGRAM DOES
----------------------
This tool turns the 7-stage AI Project Lifecycle from the notes into
something you can actually PLAN and TRACK. Pick a project idea, then
walk it through every stage:

    1. Problem Definition
    2. Data Collection
    3. Data Preparation & Cleaning
    4. Exploratory Data Analysis (EDA) & Feature Engineering
    5. Model Building & Training
    6. Model Evaluation
    7. Deployment & Monitoring

For each stage you set a status (Not Started / In Progress / Done) and
write short notes. The tracker shows a progress bar and a completion
percentage, and saves everything to `ai_project.json`.

HOW TO RUN
----------
1. Open a terminal in this folder.
2. Type:   python ai_lifecycle_tracker.py
3. Use the on-screen menu (type 1-4 and press Enter).

CONCEPTS PRACTISED (Module 1 skills applied to Module 2 ideas)
--------------------------------------------------------------
- dictionaries & lists ....... the project and its 7 stages
- functions .................. one job per function
- loops & enumerate .......... number and display the stages
- conditions / match-case .... the menu and status choices
- input validation ........... only accept valid stage numbers
- file handling (JSON) ....... save & load the project
- integer math ............... build the text progress bar

NOTE ON OUTPUT
--------------
All printed text is plain ASCII so the program runs the same on every
terminal, including the default Windows console.
"""

import json

DATA_FILE = "ai_project.json"

# The seven lifecycle stages, in order (from the Module 2 notes).
STAGES = [
    "Problem Definition",
    "Data Collection",
    "Data Preparation & Cleaning",
    "EDA & Feature Engineering",
    "Model Building & Training",
    "Model Evaluation",
    "Deployment & Monitoring",
]

# Each status maps to how "complete" it is (used for the progress %).
STATUS_WEIGHT = {"Not Started": 0.0, "In Progress": 0.5, "Done": 1.0}
STATUS_CHOICES = list(STATUS_WEIGHT.keys())


# ----------------------------------------------------------------------
# DATA PERSISTENCE
# ----------------------------------------------------------------------
def new_project(name: str) -> dict:
    """Create a fresh project with every stage 'Not Started' and empty notes."""
    return {
        "name": name,
        "stages": [
            {"stage": stage, "status": "Not Started", "notes": ""}
            for stage in STAGES
        ],
    }


def load_project() -> dict:
    """Load the saved project, or create a new empty one on first run."""
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return new_project("My First AI Project")
    except json.JSONDecodeError:
        print("[!] Data file unreadable; starting a new project.")
        return new_project("My First AI Project")


def save_project(project: dict) -> None:
    """Save the project to the JSON file."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(project, f, indent=4)
    print(f"[saved] Project written to '{DATA_FILE}'.")


# ----------------------------------------------------------------------
# HELPERS
# ----------------------------------------------------------------------
def completion_percent(project: dict) -> int:
    """Return overall completion as a whole-number percentage (0-100)."""
    weights = [STATUS_WEIGHT[s["status"]] for s in project["stages"]]
    return round(sum(weights) / len(weights) * 100)


def progress_bar(percent: int, width: int = 20) -> str:
    """Build a text progress bar like [#########-----------] for a percentage."""
    filled = round(percent / 100 * width)      # how many '#' blocks to show
    return "[" + "#" * filled + "-" * (width - filled) + "]"


def ask_stage_number() -> int:
    """Ask which stage (1-7) to update. Returns a 0-based index, or -1 if bad."""
    try:
        number = int(input(f"Which stage number to update (1-{len(STAGES)})? "))
    except ValueError:
        print("[!] Please enter a whole number.")
        return -1
    if number < 1 or number > len(STAGES):
        print(f"[!] Pick a number from 1 to {len(STAGES)}.")
        return -1
    return number - 1                            # convert 1-based to 0-based


# ----------------------------------------------------------------------
# FEATURES
# ----------------------------------------------------------------------
def rename_project(project: dict) -> None:
    """Change the project's name."""
    name = input("New project name: ").strip()
    if name == "":
        print("[!] Name cannot be empty.")
        return
    project["name"] = name
    print(f"[OK] Project renamed to '{name}'.")


def update_stage(project: dict) -> None:
    """Set the status and notes for one stage."""
    view_progress(project)                       # show the list first
    index = ask_stage_number()
    if index == -1:
        return

    stage = project["stages"][index]
    print(f"\nUpdating: {stage['stage']}")
    print("Status options:")
    for i, status in enumerate(STATUS_CHOICES, start=1):
        print(f"   {i}. {status}")

    try:
        pick = int(input("Choose a status (1-3): "))
    except ValueError:
        print("[!] Please enter 1, 2, or 3.")
        return
    if pick < 1 or pick > len(STATUS_CHOICES):
        print("[!] Please choose 1, 2, or 3.")
        return

    stage["status"] = STATUS_CHOICES[pick - 1]
    notes = input("Add a note (press Enter to skip): ").strip()
    if notes != "":
        stage["notes"] = notes
    print(f"[OK] '{stage['stage']}' -> {stage['status']}.")


def view_progress(project: dict) -> None:
    """Show every stage, its status, notes, and the overall progress bar."""
    print("\n" + "=" * 70)
    print(f"PROJECT: {project['name']}")
    print("=" * 70)
    print(f"{'#':<3}| {'Stage':<28}| {'Status':<12}| Notes")
    print("-" * 70)
    for i, s in enumerate(project["stages"], start=1):
        note = s["notes"] if s["notes"] else "-"
        print(f"{i:<3}| {s['stage']:<28}| {s['status']:<12}| {note}")
    print("-" * 70)

    percent = completion_percent(project)
    print(f"Overall progress: {progress_bar(percent)} {percent}%\n")


# ----------------------------------------------------------------------
# MAIN MENU
# ----------------------------------------------------------------------
MENU = """
========= AI PROJECT LIFECYCLE TRACKER =========
1. Rename the project
2. Update a stage (status + notes)
3. View progress
4. Save & Exit
================================================
"""


def main() -> None:
    project = load_project()
    print(f"Loaded project: '{project['name']}' "
          f"({completion_percent(project)}% complete).")

    while True:
        print(MENU)
        choice = input("Choose an option (1-4): ").strip()
        match choice:
            case "1":
                rename_project(project)
            case "2":
                update_stage(project)
            case "3":
                view_progress(project)
            case "4":
                save_project(project)
                print("Goodbye!")
                break
            case _:
                print("[!] Invalid choice. Please pick a number from 1 to 4.")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\n\nExited without saving. Goodbye!")
