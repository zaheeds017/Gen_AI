"""
============================================================
 PROJECT 3 : PROMPT ENGINEERING LAB
 Module 7  : Generative AI & Prompt Engineering
 AI Powered Engineering Upskilling Program (2026 Edition)
============================================================

WHAT THIS PROGRAM DOES
----------------------
A hands-on tour of the most important PROMPT ENGINEERING techniques. For
each technique it shows (a) the prompt you would send and (b) the kind of
response it produces, with a short note on WHEN to use it. This is the core
skill of Module 7 - the difference between a mediocre and an excellent AI
result is almost always the prompt.

TECHNIQUES DEMONSTRATED
    1. Zero-shot prompting        (just ask)
    2. Few-shot prompting         (show examples)
    3. Role / persona prompting   (assign an expert role)
    4. Chain-of-thought           (ask it to think step by step)
    5. Structured-output prompting(force a specific format)

TWO MODES
---------
- MOCK mode (default): OFFLINE, no API key. Prints each prompt plus a
  representative response so you learn the pattern.
- REAL mode: set USE_REAL_API = True + an Anthropic API key to see each
  technique run against Claude for real. See the README.

HOW TO RUN
----------
1. (Mock)  python prompt_engineering_lab.py
2. (Real)  pip install anthropic, set ANTHROPIC_API_KEY, USE_REAL_API = True.

NOTE ON OUTPUT
--------------
Console text is plain ASCII so it runs on every terminal.
"""

USE_REAL_API = False
MODEL = "claude-opus-5"     # or "claude-sonnet-5" / "claude-haiku-4-5"

# Each technique: a title, the prompt to send, a mock response, and a "when".
TECHNIQUES = [
    {
        "title": "1. ZERO-SHOT PROMPTING",
        "when": "The task is simple and common; just ask directly.",
        "prompt": "Classify the sentiment of this review as Positive or "
                  "Negative:\n\"The battery dies within an hour. Very "
                  "disappointing.\"",
        "mock": "Negative",
    },
    {
        "title": "2. FEW-SHOT PROMPTING",
        "when": "You want a specific style/format; show 1-3 examples first.",
        "prompt": ("Classify sentiment. Examples:\n"
                   "Review: \"I love it!\" -> Positive\n"
                   "Review: \"Total waste of money.\" -> Negative\n"
                   "Review: \"Fast delivery and great quality.\" ->"),
        "mock": "Positive",
    },
    {
        "title": "3. ROLE / PERSONA PROMPTING",
        "when": "You want expert-level tone and depth; assign a role.",
        "prompt": ("You are a senior cybersecurity expert. In 2 sentences, "
                   "explain to a beginner why using the same password "
                   "everywhere is risky."),
        "mock": ("Reusing one password means a single breach exposes every "
                 "account you own - attackers try leaked passwords everywhere. "
                 "Use a password manager to create a unique, strong password "
                 "per site."),
    },
    {
        "title": "4. CHAIN-OF-THOUGHT PROMPTING",
        "when": "For reasoning/math problems; ask it to think step by step.",
        "prompt": ("A shop sells pens at 12 for $8. How much do 30 pens cost? "
                   "Think step by step, then give the final answer."),
        "mock": ("Step 1: price per pen = 8 / 12 = $0.667.\n"
                 "Step 2: 30 pens = 30 x 0.667 = $20.\n"
                 "Final answer: $20."),
    },
    {
        "title": "5. STRUCTURED-OUTPUT PROMPTING",
        "when": "You need machine-readable output; specify the exact format.",
        "prompt": ("Extract the name, role, and city from this text and reply "
                   "as JSON with keys name, role, city:\n"
                   "\"Priya is a data scientist based in Pune.\""),
        "mock": '{"name": "Priya", "role": "data scientist", "city": "Pune"}',
    },
]


def run_technique(system_prompt: str, user_prompt: str, mock: str) -> str:
    """Return a real Claude response (REAL mode) or the mock (offline)."""
    if USE_REAL_API:
        return call_claude(system_prompt, user_prompt)
    return mock


def call_claude(system_prompt: str, user_prompt: str) -> str:
    """Call Anthropic's Claude. Requires: pip install anthropic + ANTHROPIC_API_KEY."""
    import anthropic
    client = anthropic.Anthropic()
    response = client.messages.create(
        model=MODEL,
        max_tokens=512,
        system=system_prompt or "You are a helpful assistant.",
        messages=[{"role": "user", "content": user_prompt}],
    )
    return "".join(block.text for block in response.content if block.type == "text")


def main() -> None:
    print("=" * 60)
    print("              PROMPT ENGINEERING LAB")
    print("=" * 60)
    print(f"Mode: {'REAL API (Claude)' if USE_REAL_API else 'MOCK (offline)'}")
    print("Five techniques, each with the prompt, the result, and when to use it.")

    for tech in TECHNIQUES:
        print("\n" + "=" * 60)
        print(tech["title"])
        print("=" * 60)
        print("PROMPT:")
        for line in tech["prompt"].split("\n"):
            print(f"   {line}")
        # Role prompting puts the persona in the system prompt; others don't.
        system_prompt = tech["prompt"] if "You are a" in tech["prompt"] else ""
        response = run_technique(system_prompt, tech["prompt"], tech["mock"])
        print("\nRESPONSE:")
        for line in response.split("\n"):
            print(f"   {line}")
        print(f"\nWHEN TO USE: {tech['when']}")

    print("\n" + "=" * 60)
    print("KEY LESSON")
    print("=" * 60)
    print("A clear prompt = a great answer. Give the AI a ROLE, a clear TASK,")
    print("EXAMPLES when needed, and the exact FORMAT you want back.")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\n[ERROR] {type(e).__name__}: {e}")
        print("REAL mode needs: pip install anthropic and ANTHROPIC_API_KEY.")
