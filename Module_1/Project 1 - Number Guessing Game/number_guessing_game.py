"""
============================================================
 PROJECT 1 : NUMBER GUESSING GAME
 Module 1  : Python for AI & Programming Fundamentals
 AI Powered Engineering Upskilling Program (2026 Edition)
============================================================

WHAT THIS PROGRAM DOES
----------------------
The computer secretly picks a random number between 1 and 100.
You keep guessing. After each guess the game tells you whether
your guess was too high or too low, and counts your attempts.
When you finally guess correctly, it shows how many tries it took.
You can then choose to play again.

HOW TO RUN
----------
1. Open a terminal in this folder.
2. Type:   python number_guessing_game.py
3. Follow the on-screen prompts.

NOTE ON OUTPUT
--------------
We keep all printed text as plain ASCII (letters, digits, and simple
symbols). This guarantees the program runs the same way on every
terminal - including the default Windows console - without any
"UnicodeEncodeError". This is a good, professional habit.

PYTHON CONCEPTS USED (from Module 1)
------------------------------------
- import / modules ............ the built-in `random` module
- variables & counters ........ secret_number, attempts
- while loops ................. keep asking until correct / quit
- if / elif / else ........... compare the guess and give hints
- input() + int() ............ read text and convert it to a number
- try / except (ValueError) .. never crash on bad input like "abc"
- break / continue ........... control the loop flow
- f-strings .................. build readable messages
- functions .................. play_game() groups one round of logic
- if __name__ == "__main__" .. standard program entry point
"""

# `random` is a BUILT-IN module (library) for generating random numbers.
# We must import it once at the top before we can use it.
import random


# The number range the game uses. Written in UPPER_CASE because these are
# CONSTANTS - values that never change while the program runs.
LOWER_BOUND = 1
UPPER_BOUND = 100


def play_game() -> int:
    """
    Play ONE full round of the guessing game.

    Returns:
        The number of attempts the player took to guess correctly.
    """
    # random.randint(a, b) returns a random whole number from a to b,
    # where BOTH ends are included. So this picks a secret 1..100.
    secret_number = random.randint(LOWER_BOUND, UPPER_BOUND)

    # A counter that starts at 0 and increases by 1 for each valid guess.
    attempts = 0

    print("\nWelcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between {LOWER_BOUND} and {UPPER_BOUND}.\n")

    # `while True` loops forever. We stay in the loop until we hit `break`,
    # which happens only when the player guesses correctly.
    while True:
        # --- Step 1: read the guess safely ---------------------------------
        # input() ALWAYS returns text (a string), so we wrap the int()
        # conversion in try/except. If the user types "hello", int() raises
        # a ValueError; we catch it and ask again instead of crashing.
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("[!] That's not a whole number. Please try again.\n")
            continue  # skip the rest of the loop and ask again

        # --- Step 2: reject out-of-range guesses ---------------------------
        if guess < LOWER_BOUND or guess > UPPER_BOUND:
            print(f"[!] Out of range! Pick a number "
                  f"between {LOWER_BOUND} and {UPPER_BOUND}.\n")
            continue  # not counted as a real attempt

        # This was a valid guess, so count it.
        attempts += 1

        # --- Step 3: compare the guess to the secret -----------------------
        if guess < secret_number:
            print("Too low!  Try a HIGHER number.\n")
        elif guess > secret_number:
            print("Too high! Try a LOWER number.\n")
        else:
            # guess == secret_number  ->  the player won!
            print(f"\nCorrect! The number was {secret_number}.")
            print(f"You guessed it in {attempts} attempt(s).")
            break  # leave the while loop - this round is over

    return attempts


def main() -> None:
    """Run the game and let the player play as many rounds as they like."""
    best_score = None  # will hold the lowest number of attempts across rounds

    print("=" * 50)
    print("             NUMBER GUESSING GAME")
    print("=" * 50)

    while True:
        attempts = play_game()

        # Track the best (lowest) score seen so far.
        # `best_score is None` is True only on the very first round.
        if best_score is None or attempts < best_score:
            best_score = attempts
        print(f"Best score so far: {best_score} attempt(s).")

        # .strip() removes stray spaces, .lower() makes the check
        # case-insensitive so "Yes", "YES" and "yes" all work.
        again = input("\nPlay again? (yes/no): ").strip().lower()
        if again not in ("yes", "y"):
            print("\nThanks for playing!")
            break


# This standard guard means: only run main() when THIS file is executed
# directly (python number_guessing_game.py). If another file imports this
# one, main() will NOT run automatically. You will see this in almost every
# professional Python program.
if __name__ == "__main__":
    # Wrap main() so that pressing Ctrl+C (KeyboardInterrupt) or the input
    # stream ending (EOFError) exits politely instead of showing a scary
    # error message. This is a small, professional touch.
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\n\nGame stopped. Goodbye!")
