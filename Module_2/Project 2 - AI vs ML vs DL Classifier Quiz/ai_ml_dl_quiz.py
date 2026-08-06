"""
============================================================
 PROJECT 2 : AI vs ML vs DL CLASSIFIER QUIZ
 Module 2  : AI & Data Science Foundations
 AI Powered Engineering Upskilling Program (2026 Edition)
============================================================

WHAT THIS PROGRAM DOES
----------------------
An interactive multiple-choice quiz that trains your mental model of
the core Module 2 ideas: Artificial Intelligence vs Machine Learning
vs Deep Learning, the types of AI, and the learning paradigms.

For each real-world SCENARIO you pick the best category. The program
checks your answer, EXPLAINS why it is correct (so it teaches, not
just tests), keeps score, and gives you a rating at the end.

HOW TO RUN
----------
1. Open a terminal in this folder.
2. Type:   python ai_ml_dl_quiz.py
3. For each question type the letter of your answer (a, b, c, or d).

CONCEPTS PRACTISED (Module 1 skills applied to Module 2 ideas)
--------------------------------------------------------------
- lists & dictionaries ....... each question is a dict in a list
- functions .................. ask one question / run the whole quiz
- loops ...................... go through every question
- conditions ................. check right vs wrong
- input validation ........... only accept a, b, c, or d
- the random module .......... shuffle the question order each run
- f-strings .................. build the score report

NOTE ON OUTPUT
--------------
All printed text is plain ASCII so the program runs the same on every
terminal, including the default Windows console.
"""

import random

# ----------------------------------------------------------------------
# THE QUESTION BANK
# Each question is a dictionary:
#   "scenario"  -> the situation to classify
#   "options"   -> the four choices (index 0..3 shown as a..d)
#   "answer"    -> the index (0..3) of the correct option
#   "why"       -> the teaching explanation shown after answering
# ----------------------------------------------------------------------
QUESTIONS = [
    {
        "scenario": "A programmer writes explicit if/else rules: 'IF email "
                    "contains the word lottery THEN mark as spam.' No data is "
                    "used to learn.",
        "options": ["Rule-based AI (not ML)", "Machine Learning",
                    "Deep Learning", "Reinforcement Learning"],
        "answer": 0,
        "why": "Hand-written rules with no learning from data is classic "
               "RULE-BASED AI. It is AI, but it is NOT Machine Learning.",
    },
    {
        "scenario": "A model is shown 50,000 emails already labelled 'spam' or "
                    "'not spam' and learns to label new emails on its own.",
        "options": ["Rule-based AI", "Supervised Machine Learning",
                    "Unsupervised Learning", "Reinforcement Learning"],
        "answer": 1,
        "why": "Learning from LABELLED examples (spam / not spam) is "
               "SUPERVISED Machine Learning - specifically classification.",
    },
    {
        "scenario": "A shop groups its customers into similar segments. Nobody "
                    "told the algorithm what the groups are - it finds them "
                    "in the data by itself.",
        "options": ["Supervised Learning", "Unsupervised Learning",
                    "Reinforcement Learning", "Rule-based AI"],
        "answer": 1,
        "why": "Finding hidden groups in UNLABELLED data is UNSUPERVISED "
               "Learning (clustering).",
    },
    {
        "scenario": "A program learns to play a game by trying moves, getting "
                    "points for winning and penalties for losing, and slowly "
                    "improving its strategy.",
        "options": ["Supervised Learning", "Unsupervised Learning",
                    "Reinforcement Learning", "Deep Learning only"],
        "answer": 2,
        "why": "Learning by trial-and-error using rewards and penalties is "
               "REINFORCEMENT Learning.",
    },
    {
        "scenario": "A system recognizes a cat in a photo using a neural "
                    "network with many layers that learns the important image "
                    "features by itself.",
        "options": ["Rule-based AI", "Classic Machine Learning",
                    "Deep Learning", "Data Analysis"],
        "answer": 2,
        "why": "Multi-layer neural networks that learn features automatically "
               "from images are DEEP LEARNING (a subset of ML).",
    },
    {
        "scenario": "ChatGPT and Claude are extremely capable, but each is "
                    "still specialized and cannot do every human task. What "
                    "capability level are they?",
        "options": ["Artificial Narrow Intelligence (ANI)",
                    "Artificial General Intelligence (AGI)",
                    "Artificial Super Intelligence (ASI)",
                    "Self-aware AI"],
        "answer": 0,
        "why": "ALL AI today, including the best 2026 models, is NARROW AI "
               "(ANI). AGI and ASI do not exist yet.",
    },
    {
        "scenario": "An AI tool creates a brand-new marketing image and writes "
                    "the ad copy to go with it.",
        "options": ["Predictive / Discriminative AI", "Generative AI",
                    "Clustering", "Rule-based AI"],
        "answer": 1,
        "why": "Creating NEW content (images, text, code) is GENERATIVE AI, "
               "the focus of Module 7.",
    },
    {
        "scenario": "Which field is the BROADEST - the umbrella that contains "
                    "the others?",
        "options": ["Deep Learning", "Machine Learning",
                    "Artificial Intelligence", "Neural Networks"],
        "answer": 2,
        "why": "AI is the umbrella. Machine Learning is inside AI, and Deep "
               "Learning is inside Machine Learning.",
    },
    {
        "scenario": "A bank predicts the EXACT loan amount (a number) a "
                    "customer can afford, based on their financial history.",
        "options": ["Classification", "Regression",
                    "Clustering", "Reinforcement Learning"],
        "answer": 1,
        "why": "Predicting a continuous NUMBER is REGRESSION. Predicting a "
               "CATEGORY would be classification.",
    },
    {
        "scenario": "About 80% of a data scientist's time on a project is "
                    "typically spent on which activity?",
        "options": ["Building fancy deep-learning models",
                    "Cleaning and preparing the data",
                    "Writing the final report",
                    "Buying GPUs"],
        "answer": 1,
        "why": "Real AI work is mostly DATA CLEANING and preparation - "
               "'garbage in, garbage out'. Modelling is a smaller slice.",
    },
]

# The letters shown for the four options.
LETTERS = ["a", "b", "c", "d"]


def ask_question(q: dict, number: int, total: int) -> bool:
    """Show one question, read the answer, explain it. Return True if correct."""
    print("\n" + "=" * 60)
    print(f"Question {number} of {total}")
    print("=" * 60)
    print(q["scenario"])
    print()
    for i, option in enumerate(q["options"]):
        print(f"   {LETTERS[i]}) {option}")

    # Keep asking until the user types a valid letter (a-d).
    while True:
        choice = input("\nYour answer (a/b/c/d): ").strip().lower()
        if choice in LETTERS:
            break
        print("[!] Please type one of: a, b, c, d.")

    picked = LETTERS.index(choice)          # convert the letter back to 0..3
    correct = q["answer"]

    if picked == correct:
        print("\n[CORRECT]")
        result = True
    else:
        print(f"\n[WRONG] The correct answer was "
              f"'{LETTERS[correct]}) {q['options'][correct]}'.")
        result = False

    print(f"Why: {q['why']}")
    return result


def rating(score: int, total: int) -> str:
    """Turn a score into an encouraging rating message."""
    percent = (score / total) * 100
    if percent == 100:
        return "PERFECT! You have mastered the AI vs ML vs DL foundations."
    if percent >= 70:
        return "GREAT job! Your mental model is solid."
    if percent >= 40:
        return "GOOD start - review Sections 2, 3 and 4 of the notes."
    return "Keep going - re-read the Module 2 notes and try again. You'll get it!"


def main() -> None:
    print("=" * 60)
    print("        AI vs ML vs DL - CONCEPT QUIZ")
    print("=" * 60)
    print("Classify each real-world scenario. The quiz explains every answer.")

    # Shuffle a COPY so every run feels fresh but QUESTIONS stays intact.
    questions = QUESTIONS[:]
    random.shuffle(questions)

    score = 0
    total = len(questions)
    for i, q in enumerate(questions, start=1):
        if ask_question(q, i, total):
            score += 1

    print("\n" + "=" * 60)
    print(f"FINAL SCORE: {score} / {total}")
    print(rating(score, total))
    print("=" * 60)


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\n\nQuiz stopped. Goodbye!")
