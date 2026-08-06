# Project 3 — Prompt Engineering Lab 🧪✍️

**Module 7 · Generative AI & Prompt Engineering**

A hands-on tour of the **five most important prompt-engineering techniques**. For each, the program shows the prompt, the result, and *when* to use it — because the difference between a mediocre and an excellent AI answer is almost always the prompt.

---

## ▶️ How to run

**Mock mode (default — offline, no API key):**
```bash
python prompt_engineering_lab.py
```

**Real mode (run each technique against Claude):**
1. `pip install anthropic`
2. Set `ANTHROPIC_API_KEY` (see Project 1's README).
3. Set `USE_REAL_API = True` and run again — then compare the real answers to the mock ones.

---

## 🎯 The five techniques

| # | Technique | What it means | When to use |
|---|---|---|---|
| 1 | **Zero-shot** | Just ask, no examples | Simple, common tasks |
| 2 | **Few-shot** | Show 1–3 examples first | You want a specific style/format |
| 3 | **Role / persona** | "You are a senior expert…" | You want expert tone and depth |
| 4 | **Chain-of-thought** | "Think step by step" | Reasoning & math problems |
| 5 | **Structured output** | "Reply as JSON with keys…" | Machine-readable results |

---

## 🖼️ Sample output

```
4. CHAIN-OF-THOUGHT PROMPTING
PROMPT:
   A shop sells pens at 12 for $8. How much do 30 pens cost?
   Think step by step, then give the final answer.
RESPONSE:
   Step 1: price per pen = 8 / 12 = $0.667.
   Step 2: 30 pens = 30 x 0.667 = $20.
   Final answer: $20.
WHEN TO USE: For reasoning/math problems; ask it to think step by step.
```

---

## 🧠 The big lesson

> **A clear prompt = a great answer.** Give the AI a **ROLE**, a clear **TASK**, **EXAMPLES** when needed, and the exact **FORMAT** you want back. These four levers cover 90% of real prompt engineering.

---

## 💡 Challenges

1. Add a **6th technique**: *"delimiters"* — wrap the input in triple quotes so the AI can't confuse instructions with data.
2. Write your **own** prompt for each technique and add it to the `TECHNIQUES` list.
3. Enable real mode and see which techniques change the answer most.
4. Take a weak prompt and improve it using all four levers (role/task/examples/format).
