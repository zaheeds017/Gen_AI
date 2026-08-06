"""
============================================================
 PROJECT 3 : MULTI-AGENT WORKFLOW
 Module 8  : AI Agents & Automation
 AI Powered Engineering Upskilling Program (2026 Edition)
============================================================

WHAT THIS PROGRAM DOES
----------------------
Shows the MULTI-AGENT pattern: instead of one agent doing everything,
several SPECIALIST agents each do one job and pass their work down a
pipeline - like a small team. Here, three agents turn a topic into a
short article:

    RESEARCHER  ->  WRITER  ->  EDITOR  ->  finished article

    - Researcher: gathers the key points to cover.
    - Writer:     turns those points into a draft.
    - Editor:     polishes it, adds a title and a TL;DR.

Each agent has its own ROLE (its own "system prompt"), and the OUTPUT of
one agent becomes the INPUT of the next - that hand-off is the heart of
multi-agent workflows and tools like CrewAI, AutoGen, and LangGraph.

TWO MODES
---------
- MOCK mode (default): OFFLINE. Each agent does real, template-based work
  so the pipeline runs with no API key.
- REAL AI mode: set USE_REAL_API = True + an Anthropic key to have Claude
  play each agent, using that agent's role prompt.

HOW TO RUN
----------
1. (Mock)  python multi_agent_workflow.py
2. (Real)  pip install anthropic, set ANTHROPIC_API_KEY, USE_REAL_API=True.

CONCEPTS PRACTISED (Module 8)
-----------------------------
- Multi-agent concepts: specialized roles + orchestration
- Agent hand-off (output of one -> input of the next)
- Workflow pipelines
- Role prompting per agent (Module 7)

NOTE ON OUTPUT
--------------
All console text is plain ASCII so it runs on every terminal.
"""

USE_REAL_API = False
MODEL = "claude-opus-5"     # or "claude-sonnet-5" / "claude-haiku-4-5"
OUTPUT_FILE = "article.md"

TOPIC = "How AI agents work"


def call_claude(system_prompt: str, user_prompt: str) -> str:
    """Real AI. Needs: pip install anthropic + ANTHROPIC_API_KEY."""
    import anthropic
    client = anthropic.Anthropic()
    response = client.messages.create(
        model=MODEL,
        max_tokens=800,
        system=system_prompt,
        messages=[{"role": "user", "content": user_prompt}],
    )
    return "".join(b.text for b in response.content if b.type == "text")


# ----------------------------------------------------------------------
# AGENT 1: RESEARCHER - gathers key points
# ----------------------------------------------------------------------
def researcher_agent(topic: str) -> list:
    role = ("You are a research agent. You list the key points a short "
            "article should cover. You are concise and factual.")
    if USE_REAL_API:
        text = call_claude(role, f"List 5 key points to cover about: {topic}. "
                                  f"One short point per line, no numbering.")
        return [line.strip("-* ") for line in text.splitlines() if line.strip()]
    # Mock: a generic-but-sensible set of aspects to cover.
    return [
        "A plain-language definition of the topic",
        "The main components or steps involved",
        "A simple real-world example",
        "Why it is useful in practice",
        "One key limitation or challenge",
    ]


# ----------------------------------------------------------------------
# AGENT 2: WRITER - drafts the article from the points
# ----------------------------------------------------------------------
def writer_agent(topic: str, points: list) -> str:
    role = ("You are a writing agent. You turn a list of key points into a "
            "clear, friendly draft for beginners.")
    if USE_REAL_API:
        joined = "\n".join(f"- {p}" for p in points)
        return call_claude(role, f"Write a short beginner article on '{topic}' "
                                  f"covering these points:\n{joined}")
    # Mock: turn the points into a simple, readable draft.
    lines = [f"This article introduces {topic.lower()}. It covers:", ""]
    for point in points:
        lines.append(f"- {point}.")
    return "\n".join(lines)


# ----------------------------------------------------------------------
# AGENT 3: EDITOR - polishes and formats
# ----------------------------------------------------------------------
def editor_agent(topic: str, draft: str) -> str:
    role = ("You are an editor agent. You polish a draft: add a title and a "
            "one-line TL;DR, fix flow, and format it neatly in Markdown.")
    if USE_REAL_API:
        return call_claude(role, f"Polish and format this draft as Markdown "
                                  f"with a title and a TL;DR:\n\n{draft}")
    # Mock: add a title, a TL;DR, and a closing line around the draft.
    # Capitalize just the first letter so acronyms like "AI" stay intact.
    clean = topic.strip().rstrip("?.")
    title = clean[0].upper() + clean[1:] if clean else "Article"
    return (
        f"# {title}\n\n"
        f"*TL;DR: A beginner-friendly overview of {topic.lower()}.*\n\n"
        f"{draft}\n\n"
        f"In summary, {topic.lower()} is best understood by learning its "
        f"parts and trying a small example yourself."
    )


# ----------------------------------------------------------------------
# THE ORCHESTRATOR - runs the agents in sequence, passing work along
# ----------------------------------------------------------------------
def main() -> None:
    print("=" * 56)
    print("              MULTI-AGENT WORKFLOW")
    print("=" * 56)
    print(f"Mode : {'REAL AI (Claude)' if USE_REAL_API else 'MOCK (offline)'}")
    print(f"Topic: {TOPIC}\n")

    # --- Agent 1 ---
    print("[Agent 1: RESEARCHER] gathering key points...")
    points = researcher_agent(TOPIC)
    for p in points:
        print(f"    - {p}")

    # --- hand-off ---
    print("\n   ...handing the points to the Writer...\n")

    # --- Agent 2 ---
    print("[Agent 2: WRITER] drafting the article...")
    draft = writer_agent(TOPIC, points)
    print("    (draft created)")

    # --- hand-off ---
    print("\n   ...handing the draft to the Editor...\n")

    # --- Agent 3 ---
    print("[Agent 3: EDITOR] polishing and formatting...")
    final = editor_agent(TOPIC, draft)
    print("    (final article ready)")

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(final)

    print("\n" + "=" * 56)
    print("FINAL ARTICLE")
    print("=" * 56)
    print(final)
    print(f"\n[OK] Saved to '{OUTPUT_FILE}'.")
    print("\nKEY IDEA: specialist agents + hand-offs = a multi-agent workflow.")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\n[ERROR] {type(e).__name__}: {e}")
        print("REAL AI mode needs: pip install anthropic and ANTHROPIC_API_KEY.")
