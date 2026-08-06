# Project 1 — Number Guessing Game 🎯

**Module 1 · Python for AI & Programming Fundamentals**

A beginner-friendly console game where the computer picks a secret number (1–100) and you try to guess it, getting "too high / too low" hints along the way.

---

## ▶️ How to run

1. Open a terminal / command prompt **in this folder**.
2. Run:
   ```bash
   python number_guessing_game.py
   ```
3. Follow the prompts and start guessing!

> Requires **Python 3.10 or newer** (any recent Python works). Nothing to install — it only uses the built-in `random` module.

---

## 🎮 Sample run

```
==================================================
             NUMBER GUESSING GAME
==================================================

Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.

Enter your guess: 50
Too low!  Try a HIGHER number.

Enter your guess: 75
Too high! Try a LOWER number.

Enter your guess: 62

Correct! The number was 62.
You guessed it in 3 attempt(s).
Best score so far: 3 attempt(s).

Play again? (yes/no): no

Thanks for playing!
```

> The on-screen text is kept as plain ASCII (no emoji) so the game runs
> identically on **every** terminal — including the default Windows
> console — without a `UnicodeEncodeError`. The emoji in this README are
> just for documentation and are never printed by the program.

---

## 🧠 Concepts practised

| Concept | Where it's used |
|---|---|
| `import` a module | `import random` |
| Constants | `LOWER_BOUND`, `UPPER_BOUND` |
| `while` loop | main game loop (`while True`) |
| `if / elif / else` | comparing the guess |
| `input()` + `int()` | reading and converting the guess |
| `try / except ValueError` | handling non-numeric input safely |
| `break` / `continue` | controlling loop flow |
| f-strings | building the messages |
| Functions | `play_game()`, `main()` |
| `if __name__ == "__main__"` | program entry point |

---

## 💡 Try these challenges

1. **Limited tries:** give the player only 7 guesses. If they run out, reveal the number.
2. **Difficulty levels:** ask Easy (1–50) or Hard (1–500) at the start using a `match` statement.
3. **Smart-guess hint:** after the game, tell the player that a "always guess the middle" (binary search) strategy can always win in **≤ 7 guesses** for 1–100 — and explain why (each guess halves the range).

> **AI connection:** the halving/binary-search idea behind the optimal strategy is the same "divide and decide" logic used by **decision trees** in Machine Learning (Module 4).
