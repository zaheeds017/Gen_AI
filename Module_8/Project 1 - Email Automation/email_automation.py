"""
============================================================
 PROJECT 1 : EMAIL AUTOMATION  (Workflow Automation)
 Module 8  : AI Agents & Automation
 AI Powered Engineering Upskilling Program (2026 Edition)
============================================================

WHAT THIS PROGRAM DOES
----------------------
An automated WORKFLOW that generates a PERSONALIZED email for every person
in a list and "sends" it - the syllabus "Email Automation" activity. This
is exactly the kind of task you would build visually in n8n (see the notes),
done here in Python so you understand what happens under the hood.

THE WORKFLOW (trigger -> process each item -> generate -> deliver):
    1. TRIGGER: read a list of recipients (name, email, context).
    2. For EACH recipient:
         a. BUILD a prompt from their details.
         b. GENERATE the email (subject + body).
         c. "SEND" it (here: save to the `outbox/` folder + log it).
    3. REPORT how many emails were processed.

TWO MODES
---------
- MOCK mode (default): OFFLINE. Emails are generated from a template and
  "sent" by saving to `outbox/`. No API key, no SMTP, no internet.
- REAL AI mode: set USE_REAL_API = True + an Anthropic key to have Claude
  write each email. (Real SMTP SENDING is shown in the README, kept off by
  default so nobody accidentally emails anyone.)

HOW TO RUN
----------
1. (Mock)  python email_automation.py
2. (Real AI)  pip install anthropic, set ANTHROPIC_API_KEY, USE_REAL_API=True.

CONCEPTS PRACTISED (Module 8)
-----------------------------
- Workflow automation: trigger -> steps -> action, looped over data
- Templating / prompt-building per item
- Generating content with an LLM (optional)
- "Delivering" the result (save/send)

NOTE ON OUTPUT
--------------
All console text is plain ASCII so it runs on every terminal.
"""

import os

USE_REAL_API = False
MODEL = "claude-opus-5"      # or "claude-sonnet-5" / "claude-haiku-4-5"
OUTBOX = "outbox"            # folder where "sent" emails are saved

# The recipient list (a real workflow would load this from a CSV, database,
# or a signup form). Each has a name, an email, and a one-line context.
RECIPIENTS = [
    {"name": "Aarav Sharma", "email": "aarav@example.com",
     "context": "completed the AI Upskilling Program with distinction"},
    {"name": "Diya Menon", "email": "diya@example.com",
     "context": "registered for the upcoming Machine Learning workshop"},
    {"name": "Kabir Rao", "email": "kabir@example.com",
     "context": "has a mentoring session scheduled for next Tuesday"},
]

# The overall purpose of this email campaign (drives the prompt/template).
CAMPAIGN = "a warm, professional update email from the program team"


# ----------------------------------------------------------------------
# STEP A: build the prompt for one recipient (prompt engineering, Module 7)
# ----------------------------------------------------------------------
def build_prompt(recipient: dict) -> str:
    return (
        f"Write {CAMPAIGN} to {recipient['name']}, who "
        f"{recipient['context']}. Keep it under 90 words, friendly and clear. "
        f"Return the SUBJECT on the first line (prefixed 'Subject: ') and the "
        f"body after a blank line. Do not invent facts."
    )


# ----------------------------------------------------------------------
# STEP B: generate the email (mock template, or real Claude)
# ----------------------------------------------------------------------
def generate_email(recipient: dict) -> str:
    if USE_REAL_API:
        return call_claude(build_prompt(recipient))
    return mock_email(recipient)


def call_claude(prompt: str) -> str:
    """Real AI generation via Claude. Needs: pip install anthropic + ANTHROPIC_API_KEY."""
    import anthropic
    client = anthropic.Anthropic()
    response = client.messages.create(
        model=MODEL,
        max_tokens=400,
        system="You are a helpful assistant that writes concise, warm emails.",
        messages=[{"role": "user", "content": prompt}],
    )
    return "".join(b.text for b in response.content if b.type == "text")


def mock_email(recipient: dict) -> str:
    """Offline template so the workflow runs with no API key."""
    name = recipient["name"].split()[0]     # first name for a friendly greeting
    return (
        f"Subject: A quick update from the AI Program team\n\n"
        f"Hi {name},\n\n"
        f"We're reaching out because you {recipient['context']}. "
        f"Thank you for being part of the program - we're excited about your "
        f"progress and here to support your next steps.\n\n"
        f"Warm regards,\n"
        f"The Program Team"
    )


# ----------------------------------------------------------------------
# STEP C: "send" the email (here: save to the outbox folder)
# ----------------------------------------------------------------------
def send_email(recipient: dict, content: str) -> str:
    """Mock 'send' by saving to outbox/. In REAL sending you would use smtplib
    (see the README) - kept OFF by default so no real mail is sent."""
    os.makedirs(OUTBOX, exist_ok=True)
    safe = recipient["name"].replace(" ", "_").lower()
    path = os.path.join(OUTBOX, f"{safe}.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(f"To: {recipient['email']}\n")
        f.write(content + "\n")
    return path


# ----------------------------------------------------------------------
# THE WORKFLOW
# ----------------------------------------------------------------------
def main() -> None:
    print("=" * 56)
    print("            EMAIL AUTOMATION WORKFLOW")
    print("=" * 56)
    print(f"Mode: {'REAL AI (Claude)' if USE_REAL_API else 'MOCK (offline)'}")
    print(f"Recipients: {len(RECIPIENTS)} | Delivery: save to '{OUTBOX}/' "
          f"(mock send)\n")

    sent = 0
    for i, recipient in enumerate(RECIPIENTS, start=1):
        print(f"[{i}/{len(RECIPIENTS)}] Processing {recipient['name']} "
              f"<{recipient['email']}>")
        content = generate_email(recipient)          # generate
        path = send_email(recipient, content)        # deliver
        subject = content.split("\n", 1)[0].replace("Subject: ", "")
        print(f"        Subject: {subject}")
        print(f"        [SENT -> saved to {path}]")
        sent += 1

    print("\n----- WORKFLOW COMPLETE -----")
    print(f"Emails generated and 'sent': {sent}")
    print(f"Open the '{OUTBOX}/' folder to read them.")
    if not USE_REAL_API:
        print("\n(Set USE_REAL_API = True + an API key for Claude-written "
              "emails. See the README to enable REAL SMTP sending.)")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\n[ERROR] {type(e).__name__}: {e}")
        print("REAL AI mode needs: pip install anthropic and ANTHROPIC_API_KEY.")
