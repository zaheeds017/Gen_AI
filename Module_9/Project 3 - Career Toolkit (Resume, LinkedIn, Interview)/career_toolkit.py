"""
career_toolkit.py - turn one profile.json into three career-ready documents:

  1) resume.md  + resume.html   (a clean, one-page-style resume)
  2) linkedin.md                (headline ideas + an "About" section)
  3) interview_prep.md          (a personalised question bank with model answers)

Everything here uses ONLY the Python standard library, so it runs anywhere with
no installs. Edit profile.json with your own details, then run:

    python career_toolkit.py

The generated files appear in the  output/  folder.
"""

import json
import os
from datetime import date

HERE = os.path.dirname(__file__)
OUT = os.path.join(HERE, "output")


# --------------------------------------------------------------------------
# Load
# --------------------------------------------------------------------------
def load_profile(path=None):
    path = path or os.path.join(HERE, "profile.json")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


# --------------------------------------------------------------------------
# 1) RESUME
# --------------------------------------------------------------------------
def build_resume_markdown(p):
    lines = []
    lines.append("# %s" % p["name"])
    lines.append("**%s**  |  %s" % (p["title"], p["location"]))
    contact = " | ".join([p["email"], p["phone"], p["github"], p["linkedin"]])
    lines.append(contact)
    lines.append("")
    lines.append("## Summary")
    lines.append(p["summary"])
    lines.append("")

    lines.append("## Skills")
    lines.append(", ".join(p["skills"]))
    lines.append("")

    if p.get("experience"):
        lines.append("## Experience")
        for job in p["experience"]:
            lines.append("**%s** - %s  *(%s)*" % (job["role"], job["org"], job["period"]))
            for b in job["bullets"]:
                lines.append("- %s" % b)
            lines.append("")

    if p.get("projects"):
        lines.append("## Projects")
        for proj in p["projects"]:
            lines.append("**%s**" % proj["name"])
            for b in proj["bullets"]:
                lines.append("- %s" % b)
            lines.append("")

    if p.get("education"):
        lines.append("## Education")
        for ed in p["education"]:
            lines.append("**%s** - %s  *(%s)*" % (ed["degree"], ed["school"], ed["period"]))
            if ed.get("detail"):
                lines.append("- %s" % ed["detail"])
            lines.append("")

    if p.get("certifications"):
        lines.append("## Certifications")
        for c in p["certifications"]:
            lines.append("- %s" % c)
        lines.append("")

    return "\n".join(lines).strip() + "\n"


def build_resume_html(p):
    """Build a printable HTML resume (open it in a browser, then Print to PDF)."""
    def esc(s):
        return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))

    parts = []
    parts.append("<h1>%s</h1>" % esc(p["name"]))
    parts.append("<p class='title'>%s &nbsp;|&nbsp; %s</p>" % (esc(p["title"]), esc(p["location"])))
    parts.append("<p class='contact'>%s</p>" % esc(" | ".join(
        [p["email"], p["phone"], p["github"], p["linkedin"]])))

    parts.append("<h2>Summary</h2><p>%s</p>" % esc(p["summary"]))
    parts.append("<h2>Skills</h2><p>%s</p>" % esc(", ".join(p["skills"])))

    if p.get("experience"):
        parts.append("<h2>Experience</h2>")
        for job in p["experience"]:
            parts.append("<h3>%s - %s <span class='when'>(%s)</span></h3>" % (
                esc(job["role"]), esc(job["org"]), esc(job["period"])))
            parts.append("<ul>" + "".join("<li>%s</li>" % esc(b) for b in job["bullets"]) + "</ul>")

    if p.get("projects"):
        parts.append("<h2>Projects</h2>")
        for proj in p["projects"]:
            parts.append("<h3>%s</h3>" % esc(proj["name"]))
            parts.append("<ul>" + "".join("<li>%s</li>" % esc(b) for b in proj["bullets"]) + "</ul>")

    if p.get("education"):
        parts.append("<h2>Education</h2>")
        for ed in p["education"]:
            parts.append("<h3>%s - %s <span class='when'>(%s)</span></h3>" % (
                esc(ed["degree"]), esc(ed["school"]), esc(ed["period"])))
            if ed.get("detail"):
                parts.append("<p>%s</p>" % esc(ed["detail"]))

    if p.get("certifications"):
        parts.append("<h2>Certifications</h2>")
        parts.append("<ul>" + "".join("<li>%s</li>" % esc(c) for c in p["certifications"]) + "</ul>")

    style = (
        "body{font-family:Georgia,'Times New Roman',serif;max-width:800px;"
        "margin:32px auto;color:#222;line-height:1.45;padding:0 20px;}"
        "h1{margin-bottom:2px;} .title{font-weight:bold;margin:2px 0;}"
        ".contact{color:#555;font-size:13px;margin-top:0;}"
        "h2{border-bottom:2px solid #333;padding-bottom:3px;margin-top:22px;"
        "text-transform:uppercase;font-size:15px;letter-spacing:1px;}"
        "h3{margin:12px 0 2px;font-size:14px;} .when{color:#777;font-weight:normal;}"
        "ul{margin:4px 0 8px 20px;} li{margin:2px 0;}"
    )
    return ("<!DOCTYPE html><html><head><meta charset='UTF-8'>"
            "<title>%s - Resume</title><style>%s</style></head><body>%s"
            "</body></html>") % (esc(p["name"]), style, "".join(parts))


# --------------------------------------------------------------------------
# 2) LINKEDIN
# --------------------------------------------------------------------------
def build_linkedin(p):
    top_skills = ", ".join(p["skills"][:4])
    headlines = [
        "%s | %s" % (p["title"], top_skills),
        "%s turning data into working AI apps | %s" % (p["title"], top_skills),
        "%s | Building and deploying ML projects end-to-end" % p["title"],
    ]
    about = (
        "%s\n\n"
        "What I can do:\n"
        "- Take a project from raw data to a deployed web app\n"
        "- Train and evaluate machine-learning models honestly (no leakage, real test sets)\n"
        "- Communicate results clearly to both technical and non-technical people\n\n"
        "Core tools: %s.\n\n"
        "I am currently open to AI/ML internships and entry-level roles. "
        "Feel free to connect or message me."
    ) % (p["summary"], ", ".join(p["skills"]))

    lines = ["# LinkedIn Content", "", "## Headline options (pick one, max ~220 chars)"]
    for h in headlines:
        lines.append("- %s" % h)
    lines.append("")
    lines.append("## About section")
    lines.append(about)
    lines.append("")
    lines.append("## Featured / tips")
    lines.append("- Pin your 2-3 best GitHub projects under 'Featured'.")
    lines.append("- Add the skills above to the 'Skills' section so recruiters can find you.")
    lines.append("- Use a clear, friendly headshot and a banner image related to tech.")
    return "\n".join(lines) + "\n"


# --------------------------------------------------------------------------
# 3) INTERVIEW PREP
# --------------------------------------------------------------------------
# A small, honest question bank. Keys are topics; we include a topic only if the
# person lists a matching skill, so the prep is tailored to THEIR resume.
QUESTION_BANK = {
    "Python": [
        ("What is the difference between a list and a tuple?",
         "A list is mutable (you can change it) and uses []; a tuple is immutable and uses (). "
         "Use a tuple for fixed data you do not want changed, e.g. coordinates."),
        ("What does a list comprehension do? Give an example.",
         "It builds a list in one line: squares = [x*x for x in range(5)] gives [0,1,4,9,16]. "
         "It is shorter and often faster than a for-loop that appends."),
    ],
    "Machine Learning": [
        ("Explain the train/test split and why we need it.",
         "We hold back part of the data (the test set) and never train on it, so we can measure "
         "how the model does on data it has never seen. Testing on training data gives a "
         "dishonestly high score."),
        ("What is overfitting and how do you reduce it?",
         "Overfitting is when a model memorises the training data and fails on new data. Reduce it "
         "with more data, a simpler model, regularisation, or cross-validation."),
        ("When is accuracy a misleading metric?",
         "On imbalanced data. If 99 percent of emails are 'not spam', a model that always says "
         "'not spam' is 99 percent accurate but useless. Use precision, recall, or F1 instead."),
    ],
    "Data Visualization": [
        ("How do you choose the right chart?",
         "Match the chart to the question: bar for comparing categories, line for trends over time, "
         "histogram for one variable's distribution, scatter for the relationship between two."),
    ],
    "NLP": [
        ("What is TF-IDF in one line?",
         "It scores a word high when it is frequent in one document but rare across all documents, "
         "so common words like 'the' get low weight and distinctive words get high weight."),
    ],
    "Flask": [
        ("How do you serve a trained model with Flask?",
         "Load the saved model once when the server starts, add a route (e.g. /predict) that reads "
         "the input, calls model.predict, and returns the result as JSON or a rendered page."),
    ],
    "Streamlit": [
        ("Why might you pick Streamlit over Flask for a demo?",
         "Streamlit builds an interactive UI from a plain Python script with almost no web code, so "
         "it is faster for data demos. Flask gives more control and is better for real APIs."),
    ],
    "Git/GitHub": [
        ("What is the difference between git commit and git push?",
         "commit saves a snapshot to your LOCAL history; push uploads your commits to the REMOTE "
         "repository (e.g. GitHub) so others can see them."),
    ],
}

GENERIC_QUESTIONS = [
    ("Tell me about yourself.",
     "Give a 60-second story: who you are, what you have built, and what you want next. "
     "End on why this role fits."),
    ("Why do you want to work in AI/ML?",
     "Tie it to something concrete you built and enjoyed, plus the impact you want to have."),
]


def build_behavioral(p):
    """Turn the person's real projects into STAR practice answers."""
    star = []
    star.append("## Behavioral questions (use the STAR method)")
    star.append("STAR = Situation, Task, Action, Result. Keep answers to ~60-90 seconds.\n")
    projects = p.get("projects", [])
    if projects:
        proj = projects[0]
        star.append("**Q: Tell me about a project you are proud of.**")
        star.append("- Situation: I built '%s' during my AI program." % proj["name"])
        star.append("- Task: I had to make it work end-to-end, not just in a notebook.")
        star.append("- Action: %s" % (proj["bullets"][0] if proj["bullets"] else "I designed, built, and tested it."))
        star.append("- Result: It runs reliably and is on my GitHub as a portfolio piece.\n")
    star.append("**Q: Tell me about a time you faced a bug or setback.**")
    star.append("- Situation/Task: describe the problem and what was at stake.")
    star.append("- Action: what you tried, step by step (this is the important part).")
    star.append("- Result: what fixed it and what you learned.\n")
    return "\n".join(star)


def build_interview_prep(p):
    lines = ["# Interview Prep - %s" % p["name"], ""]
    lines.append("Generated %s. Practice out loud; do not memorise word for word.\n" % date.today().isoformat())

    lines.append("## Technical questions (tailored to your skills)")
    skills_lower = {s.lower() for s in p["skills"]}
    matched = 0
    for topic, qas in QUESTION_BANK.items():
        if topic.lower() in skills_lower:
            matched += 1
            lines.append("\n### %s" % topic)
            for q, a in qas:
                lines.append("**Q: %s**" % q)
                lines.append("A: %s\n" % a)
    if matched == 0:
        lines.append("(No topic-specific questions matched your skills list.)")

    lines.append("\n## General questions")
    for q, a in GENERIC_QUESTIONS:
        lines.append("**Q: %s**" % q)
        lines.append("A: %s\n" % a)

    lines.append(build_behavioral(p))
    return "\n".join(lines) + "\n"


# --------------------------------------------------------------------------
# Save everything
# --------------------------------------------------------------------------
def write_file(name, content):
    os.makedirs(OUT, exist_ok=True)
    path = os.path.join(OUT, name)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    return path


def generate_all(profile=None):
    p = profile or load_profile()
    outputs = {
        "resume.md": build_resume_markdown(p),
        "resume.html": build_resume_html(p),
        "linkedin.md": build_linkedin(p),
        "interview_prep.md": build_interview_prep(p),
    }
    paths = [write_file(name, content) for name, content in outputs.items()]
    return paths


if __name__ == "__main__":
    for path in generate_all():
        print("Wrote:", os.path.relpath(path, HERE))
    print("\nDone. Open output/resume.html in a browser and Print -> Save as PDF.")
