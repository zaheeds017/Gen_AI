"""
medical_engine.py - the logic for an EDUCATIONAL health-information assistant.

VERY IMPORTANT - READ THIS:
This tool does NOT diagnose and is NOT a doctor. It only matches everyday
symptom words to general, educational self-care information and clear
"see a doctor if..." guidance. It also watches for a list of emergency
"red-flag" phrases and, if it sees one, tells the user to seek urgent help
instead of showing self-care tips.

Building it teaches an important engineering lesson: when software touches
people's health, SAFETY and honest limits matter more than clever features.

Pure Python, no external libraries.
"""

import json
import os
import re

HERE = os.path.dirname(__file__)


def load_info(path=None):
    path = path or os.path.join(HERE, "health_info.json")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def _contains(text, phrase):
    """Whole-phrase, case-insensitive match."""
    return re.search(r"(?<![a-z])" + re.escape(phrase.lower()) + r"(?![a-z])",
                     text.lower()) is not None


def check_emergency(text, info):
    """Return the list of emergency red-flag phrases found in the text."""
    return [flag for flag in info["emergency_flags"] if _contains(text, flag)]


def match_conditions(text, info):
    """Return educational entries whose keywords appear in the text."""
    matches = []
    for cond in info["conditions"]:
        if any(_contains(text, kw) for kw in cond["keywords"]):
            matches.append(cond)
    return matches


def assess(symptom_text, info=None):
    """Main entry point. Returns a structured, SAFE educational response."""
    info = info or load_info()
    result = {"disclaimer": info["disclaimer"], "emergency": False,
              "emergency_flags": [], "conditions": [], "message": ""}

    flags = check_emergency(symptom_text, info)
    if flags:
        # Safety first: if any red flag appears, do NOT give self-care tips.
        result["emergency"] = True
        result["emergency_flags"] = flags
        result["message"] = (
            "Your description includes something that can be serious. "
            "Please seek emergency care now - call your local emergency number "
            "or go to the nearest emergency department. Do not wait."
        )
        return result

    conds = match_conditions(symptom_text, info)
    result["conditions"] = conds
    if not conds:
        result["message"] = (
            "I couldn't match your description to the general topics I know about. "
            "That does not mean it is nothing - if you are worried, please talk to "
            "a pharmacist or doctor."
        )
    else:
        names = ", ".join(c["name"] for c in conds)
        result["message"] = ("Here is general, educational information related to: %s. "
                             "This is not a diagnosis." % names)
    return result


if __name__ == "__main__":
    # Offline self-test:  python medical_engine.py
    info = load_info()
    print("--- Emergency example ---")
    r = assess("I have sudden chest pain and difficulty breathing", info)
    print("emergency:", r["emergency"], "| flags:", r["emergency_flags"])
    print(r["message"], "\n")

    print("--- Everyday example ---")
    r = assess("runny nose, sore throat and a mild cough", info)
    print("emergency:", r["emergency"])
    print(r["message"])
    for c in r["conditions"]:
        print("  *", c["name"], "->", c["info"])
    print("\nDisclaimer:", info["disclaimer"])
