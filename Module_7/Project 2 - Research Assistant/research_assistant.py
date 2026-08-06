"""
============================================================
 PROJECT 2 : AI RESEARCH ASSISTANT
 Module 7  : Generative AI & Prompt Engineering
 AI Powered Engineering Upskilling Program (2026 Edition)
============================================================

WHAT THIS PROGRAM DOES
----------------------
Turns a topic into a structured RESEARCH BRIEF using an LLM - an overview,
key concepts, important questions, subtopics to explore, and next steps.
This is a real productivity tool and a great showcase of prompt engineering
for a *structured* output.

    1. Take a TOPIC.
    2. BUILD a prompt that asks for a specific, sectioned brief.
    3. SEND it to an LLM and get the brief back.
    4. SAVE it to `research_brief.md`.

TWO MODES
---------
- MOCK mode (default): runs OFFLINE with no API key; builds a useful brief
  scaffold from the topic so the app works immediately.
- REAL mode: set USE_REAL_API = True + an Anthropic API key for Claude to
  write a full, intelligent brief. See the README.

HOW TO RUN
----------
1. (Mock)  python research_assistant.py
2. (Real)  pip install anthropic, set ANTHROPIC_API_KEY, USE_REAL_API = True.

CONCEPTS PRACTISED (Module 7)
-----------------------------
- Prompt engineering for STRUCTURED output (fixed sections)
- System vs user prompts
- Optional real LLM call (Anthropic Claude)

NOTE ON OUTPUT
--------------
Console text is plain ASCII so it runs on every terminal.
"""

USE_REAL_API = False
MODEL = "claude-opus-5"          # or "claude-sonnet-5" / "claude-haiku-4-5"
OUTPUT_FILE = "research_brief.md"

# The topic to research (edit this, or wire up input()).
TOPIC = "How Convolutional Neural Networks (CNNs) work in computer vision"


# ----------------------------------------------------------------------
# PROMPT ENGINEERING
# ----------------------------------------------------------------------
def build_system_prompt() -> str:
    return (
        "You are a meticulous research assistant. You produce clear, "
        "well-structured research briefs for students. You are accurate, "
        "you flag uncertainty, and you never fabricate sources or facts."
    )


def build_user_prompt(topic: str) -> str:
    """Ask for a STRUCTURED brief with named sections - the key to a
    predictable, useful answer."""
    return f"""Create a beginner-friendly research brief on the topic:
"{topic}".

Use exactly these Markdown sections:
# Research Brief: {topic}
## 1. Overview (3-4 sentences)
## 2. Key Concepts (5 bullet points, each with a one-line explanation)
## 3. Important Questions to Explore (5 questions)
## 4. Subtopics to Study Next (5 items)
## 5. How to Learn More (general study steps - no fake links)

RULES
- Keep it concise and beginner-friendly.
- Do NOT invent URLs, papers, or author names.
- Prefer plain language over jargon; define any term you must use."""


# ----------------------------------------------------------------------
# THE LLM CALL (mock by default)
# ----------------------------------------------------------------------
def call_llm(system_prompt: str, user_prompt: str) -> str:
    if USE_REAL_API:
        return call_claude(system_prompt, user_prompt)
    return mock_response(TOPIC)


def call_claude(system_prompt: str, user_prompt: str) -> str:
    """Call Anthropic's Claude. Requires: pip install anthropic + ANTHROPIC_API_KEY."""
    import anthropic
    client = anthropic.Anthropic()
    response = client.messages.create(
        model=MODEL,
        max_tokens=1500,
        system=system_prompt,
        messages=[{"role": "user", "content": user_prompt}],
    )
    return "".join(block.text for block in response.content if block.type == "text")


def mock_response(topic: str) -> str:
    """Offline scaffold so the app works with no API key. It builds a real,
    if generic, brief structure around the topic."""
    return f"""# Research Brief: {topic}

## 1. Overview
This brief introduces "{topic}" for a beginner. It outlines the core ideas,
the questions worth exploring, and where to go next. (In REAL mode, an AI
model fills this section with a rich, topic-specific explanation.)

## 2. Key Concepts
- Core idea: the central principle behind the topic.
- Building blocks: the smaller parts it is made of.
- How it works: the step-by-step process or mechanism.
- Why it matters: the real-world value or application.
- Common pitfalls: what beginners often misunderstand.

## 3. Important Questions to Explore
- What problem does this topic solve, and for whom?
- What are the essential terms I must understand first?
- How does it compare to the alternative approaches?
- Where is it used in the real world today?
- What are its current limitations or open challenges?

## 4. Subtopics to Study Next
- The foundational math or concepts it relies on
- A closely related, more advanced topic
- A practical tool or library used with it
- A famous example or case study
- Ethical or practical considerations

## 5. How to Learn More
- Start with a beginner tutorial, then build a tiny hands-on project.
- Explain the idea out loud in one sentence to test your understanding.
- Read one reputable overview, then one deeper resource.
- Practise by teaching it to a peer.
"""


def main() -> None:
    print("=" * 56)
    print("            AI RESEARCH ASSISTANT")
    print("=" * 56)
    print(f"Mode : {'REAL API (Claude)' if USE_REAL_API else 'MOCK (offline)'}")
    print(f"Topic: {TOPIC}\n")

    system_prompt = build_system_prompt()
    user_prompt = build_user_prompt(TOPIC)

    print("----- THE PROMPT SENT TO THE AI -----")
    print("[SYSTEM]", system_prompt)
    print("\n[USER]")
    print(user_prompt)
    print("-" * 56)

    brief = call_llm(system_prompt, user_prompt)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(brief)

    print("\n----- RESEARCH BRIEF -----")
    print(brief)
    print(f"[OK] Brief saved to '{OUTPUT_FILE}'.")
    if not USE_REAL_API:
        print("\n(Set USE_REAL_API = True + an API key for a full AI-written "
              "brief on any topic.)")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\n[ERROR] {type(e).__name__}: {e}")
        print("REAL mode needs: pip install anthropic and ANTHROPIC_API_KEY.")
