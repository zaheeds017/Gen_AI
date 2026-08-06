"""
============================================================
 PROJECT 2 : AI AGENT WITH TOOLS
 Module 8  : AI Agents & Automation
 AI Powered Engineering Upskilling Program (2026 Edition)
============================================================

WHAT THIS PROGRAM DOES
----------------------
Builds a simple AI AGENT - a program that, given a goal, decides which TOOL
to use, uses it, observes the result, and produces an answer. This is the
core "agent loop":

        THINK  ->  ACT (use a tool)  ->  OBSERVE  ->  ANSWER

A plain chatbot only talks. An AGENT can ACT: do maths, check the time,
look things up. That is the leap from Module 7 (chat) to Module 8 (agents).

    Tools this agent has:
      - calculator   : evaluate a maths expression
      - clock        : the current date and time
      - word_counter : count the words in some text
      - knowledge    : look up a fact from a small built-in knowledge base

HOW THE "BRAIN" WORKS
---------------------
In a production agent, an LLM reads the goal and picks the tool. To keep
this project OFFLINE and fully testable, the brain here is a small set of
rules (a "router"). The notes show the LLM-driven version - the LOOP is
identical; only the decision-maker changes.

HOW TO RUN
----------
    python ai_agent.py

CONCEPTS PRACTISED (Module 8)
-----------------------------
- The agent loop: think -> act -> observe -> answer
- Tools (functions the agent can call)
- Routing a goal to the right tool
- A transparent trace so you can see the agent "reasoning"

NOTE ON OUTPUT
--------------
All console text is plain ASCII so it runs on every terminal.
"""

import re
from datetime import datetime


# ----------------------------------------------------------------------
# THE TOOLS - each is a small function the agent can call
# ----------------------------------------------------------------------
def tool_calculator(expression: str) -> str:
    """Safely evaluate a basic maths expression (digits and + - * / ( ) only)."""
    if not re.fullmatch(r"[0-9+\-*/(). ]+", expression):
        return "Error: only numbers and + - * / ( ) are allowed."
    try:
        # Locked-down eval: no builtins, no variables -> only arithmetic runs.
        result = eval(expression, {"__builtins__": {}}, {})
        return str(result)
    except Exception:
        return "Error: could not evaluate that expression."


def tool_clock(_: str) -> str:
    """Return the current date and time."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def tool_word_counter(text: str) -> str:
    """Count the words in a piece of text."""
    return f"{len(text.split())} words"


KNOWLEDGE_BASE = {
    "capital of france": "Paris",
    "capital of japan": "Tokyo",
    "capital of india": "New Delhi",
    "largest planet": "Jupiter",
    "speed of light": "about 300,000 km/s",
    "who created python": "Guido van Rossum",
}


def tool_knowledge(query: str) -> str:
    """Look up a fact in the small built-in knowledge base."""
    key = query.lower().strip("?. ")
    for fact_key, answer in KNOWLEDGE_BASE.items():
        if fact_key in key:
            return answer
    return "I don't have that fact in my knowledge base."


# ----------------------------------------------------------------------
# THE BRAIN - decide which tool a goal needs (rule-based router)
# ----------------------------------------------------------------------
def choose_tool(goal: str):
    """Return (tool_name, tool_function, tool_input) for a goal.
    In a real agent, an LLM makes this choice; here we use simple rules."""
    text = goal.lower()

    # 1) A maths expression? Look for digits joined by an operator.
    math_match = re.search(r"[0-9][0-9+\-*/(). ]*[+\-*/][0-9+\-*/(). ]*[0-9]", goal)
    if math_match:
        return "calculator", tool_calculator, math_match.group().strip()

    # 2) Time / date?
    if "time" in text or "date" in text or "day" in text:
        return "clock", tool_clock, ""

    # 3) Word counting?
    if "how many words" in text or "count the words" in text or "word count" in text:
        # Pull the quoted text if present, else everything after the colon.
        quoted = re.search(r"[\"'](.+?)[\"']", goal)
        payload = quoted.group(1) if quoted else goal.split(":", 1)[-1]
        return "word_counter", tool_word_counter, payload

    # 4) Otherwise, treat it as a knowledge question.
    return "knowledge", tool_knowledge, goal


# ----------------------------------------------------------------------
# THE AGENT LOOP - think, act, observe, answer (with a visible trace)
# ----------------------------------------------------------------------
def run_agent(goal: str) -> str:
    print(f"\nGOAL: {goal}")
    # THINK: choose a tool
    tool_name, tool_fn, tool_input = choose_tool(goal)
    print(f"  THINK  : This needs the '{tool_name}' tool.")
    # ACT: call the tool
    print(f"  ACT    : {tool_name}({tool_input!r})")
    observation = tool_fn(tool_input)
    # OBSERVE: read the result
    print(f"  OBSERVE: {observation}")
    # ANSWER: present it
    answer = f"The answer is: {observation}"
    print(f"  ANSWER : {answer}")
    return answer


def main() -> None:
    print("=" * 56)
    print("               AI AGENT WITH TOOLS")
    print("=" * 56)
    print("Watch the agent THINK -> ACT -> OBSERVE -> ANSWER for each goal.")
    print(f"Available tools: calculator, clock, word_counter, knowledge")

    goals = [
        "What is 15 * 23 + 100?",
        "What time is it right now?",
        "What is the capital of France?",
        "How many words are in this sentence: 'AI agents can use tools'?",
        "What is the largest planet?",
    ]
    for goal in goals:
        run_agent(goal)

    print("\n" + "=" * 56)
    print("KEY IDEA: an agent = an LLM (the brain) + TOOLS + a LOOP.")
    print("Swap the rule-based brain for an LLM and you have a real AI agent.")


if __name__ == "__main__":
    main()
