"""
============================================================
 PROJECT 1 : AI RESUME GENERATOR
 Module 7  : Generative AI & Prompt Engineering
 AI Powered Engineering Upskilling Program (2026 Edition)
============================================================

WHAT THIS PROGRAM DOES
----------------------
Turns a few facts about a person into a polished, professional resume
summary using a Large Language Model (LLM). This teaches the core skill
of the module: PROMPT ENGINEERING - writing a clear, structured prompt
that gets a great result from an AI.

    1. Read a PROFILE (name, role, skills, experience, education).
    2. BUILD a well-engineered prompt (role + task + format + rules).
    3. SEND the prompt to an LLM and get the generated resume back.
    4. SAVE the result to `resume.md`.

TWO MODES
---------
- MOCK mode (default): runs fully OFFLINE with no API key. It prints the
  prompt that WOULD be sent, and assembles a clean resume from the
  profile so you can see the whole app working immediately.
- REAL mode: set USE_REAL_API = True and provide an Anthropic API key to
  have Claude actually generate the resume. See the README for setup.

HOW TO RUN
----------
1. (Mock mode) just run:   python ai_resume_generator.py
2. (Real mode) pip install anthropic, set ANTHROPIC_API_KEY, and set
   USE_REAL_API = True below.

CONCEPTS PRACTISED (Module 7)
-----------------------------
- Prompt engineering: role prompting, clear instructions, output format
- System vs user prompts
- Calling an LLM API (Anthropic Claude) - shown, optional to run
- Separating the prompt-building logic from the model call

NOTE ON OUTPUT
--------------
All console text is plain ASCII so it runs on every terminal.
"""

# Set to True to call the real Claude API (needs: pip install anthropic
# and the ANTHROPIC_API_KEY environment variable). Default False = offline mock.
USE_REAL_API = False

# The model to use in REAL mode. claude-opus-5 is the most capable; you can
# switch to "claude-sonnet-5" (cheaper/faster) or "claude-haiku-4-5" (fastest).
MODEL = "claude-opus-5"

OUTPUT_FILE = "resume.md"

# A sample profile (edit this with your own details, or wire up input()).
PROFILE = {
    "name": "Alex Rivera",
    "target_role": "Junior AI/Machine Learning Engineer",
    "summary_facts": "Final-year engineering student; loves building AI apps; "
                     "completed a 72-hour AI upskilling program.",
    "skills": ["Python", "Pandas", "scikit-learn", "TensorFlow (basics)",
               "OpenCV", "Prompt Engineering", "Git"],
    "experience": [
        "Built a customer-churn prediction model (87% accuracy) with scikit-learn",
        "Created a YOLO object-detection demo and an OpenCV image pipeline",
        "Developed a spam detector and a sentiment analyzer using NLP",
    ],
    "education": "B.E. in Computer Science, Expected 2026",
}


# ----------------------------------------------------------------------
# STEP 1: PROMPT ENGINEERING - build a strong, structured prompt
# ----------------------------------------------------------------------
def build_system_prompt() -> str:
    """The SYSTEM prompt sets the AI's role and overall behavior."""
    return (
        "You are an expert technical resume writer and career coach. "
        "You write concise, achievement-focused resumes that pass recruiter "
        "screening. You never invent facts; you only use what you are given."
    )


def build_user_prompt(profile: dict) -> str:
    """The USER prompt gives the task, the data, the format, and the rules.
    Notice the four parts: ROLE context, DATA, FORMAT, and RULES - this
    structure is what makes a prompt reliable."""
    skills = ", ".join(profile["skills"])
    experience = "\n".join(f"- {item}" for item in profile["experience"])
    return f"""Write a professional resume for the person below, targeting the role of
"{profile['target_role']}".

CANDIDATE DETAILS
Name: {profile['name']}
Background: {profile['summary_facts']}
Skills: {skills}
Experience / Projects:
{experience}
Education: {profile['education']}

FORMAT (use these exact section headings, in Markdown):
# {profile['name']}
## Professional Summary
## Key Skills
## Experience & Projects
## Education

RULES
- Keep the professional summary to 2-3 punchy sentences.
- Turn each experience item into a strong bullet starting with an action verb.
- Do not invent employers, dates, or facts that were not provided.
- Keep the whole resume under 250 words."""


# ----------------------------------------------------------------------
# STEP 2: the LLM call (mock by default, real if you enable it)
# ----------------------------------------------------------------------
def call_llm(system_prompt: str, user_prompt: str) -> str:
    """Send the prompt to an LLM and return its text response.
    Uses a real API call if USE_REAL_API is True, else a local mock."""
    if USE_REAL_API:
        return call_claude(system_prompt, user_prompt)
    return mock_response(PROFILE)


def call_claude(system_prompt: str, user_prompt: str) -> str:
    """Call Anthropic's Claude API. Requires: pip install anthropic and the
    ANTHROPIC_API_KEY environment variable set to your key."""
    import anthropic
    client = anthropic.Anthropic()          # reads ANTHROPIC_API_KEY from env
    response = client.messages.create(
        model=MODEL,
        max_tokens=1024,
        system=system_prompt,
        messages=[{"role": "user", "content": user_prompt}],
    )
    # response.content is a list of blocks; collect the text blocks.
    return "".join(block.text for block in response.content if block.type == "text")


def mock_response(profile: dict) -> str:
    """A deterministic, offline stand-in for the LLM so the app runs with no
    API key. It assembles a clean resume from the profile data."""
    skills = " | ".join(profile["skills"])
    bullets = "\n".join(f"- {item}." for item in profile["experience"])
    return f"""# {profile['name']}

## Professional Summary
Aspiring {profile['target_role']} with hands-on experience building
end-to-end AI applications. {profile['summary_facts'].capitalize()}
Eager to apply machine learning and prompt-engineering skills to
real-world problems.

## Key Skills
{skills}

## Experience & Projects
{bullets}

## Education
{profile['education']}
"""


# ----------------------------------------------------------------------
# MAIN
# ----------------------------------------------------------------------
def main() -> None:
    print("=" * 56)
    print("            AI RESUME GENERATOR")
    print("=" * 56)
    mode = "REAL API (Claude)" if USE_REAL_API else "MOCK (offline)"
    print(f"Mode: {mode}\n")

    system_prompt = build_system_prompt()
    user_prompt = build_user_prompt(PROFILE)

    # Show the engineered prompt so students SEE the prompt engineering.
    print("----- THE PROMPT SENT TO THE AI -----")
    print("[SYSTEM]")
    print(system_prompt)
    print("\n[USER]")
    print(user_prompt)
    print("-" * 56)

    resume = call_llm(system_prompt, user_prompt)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(resume)

    print("\n----- GENERATED RESUME -----")
    print(resume)
    print(f"[OK] Resume saved to '{OUTPUT_FILE}'.")
    if not USE_REAL_API:
        print("\n(Tip: set USE_REAL_API = True + an API key to have Claude "
              "write it for real. Same prompt, smarter output!)")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\n[ERROR] {type(e).__name__}: {e}")
        print("If using REAL mode: run 'pip install anthropic' and set "
              "ANTHROPIC_API_KEY. Otherwise keep USE_REAL_API = False.")
