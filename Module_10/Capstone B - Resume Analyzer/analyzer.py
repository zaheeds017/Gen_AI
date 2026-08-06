"""
analyzer.py - the resume-analysis engine (pure Python, no external libraries).

Given a RESUME and a JOB DESCRIPTION, it reports:
  * which required skills the resume already has, and which are missing
  * a match score (how well the resume fits the job)
  * quick resume-health checks (length, contact info, action verbs, numbers)
  * concrete, prioritised suggestions

This is a rule-based analyzer -- transparent and free. In the notes we discuss
how an LLM (Module 7) could make the feedback even richer.
"""

import json
import os
import re

HERE = os.path.dirname(__file__)


def load_db(path=None):
    path = path or os.path.join(HERE, "skills_db.json")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def find_skills(text, skills):
    """Return the set of known skills that appear in text (whole-word match)."""
    text_low = text.lower()
    found = set()
    for skill in skills:
        # \b word boundaries so 'r' doesn't match inside 'random', etc.
        pattern = r"(?<![a-z0-9])" + re.escape(skill.lower()) + r"(?![a-z0-9])"
        if re.search(pattern, text_low):
            found.add(skill)
    return found


def count_action_verbs(text, verbs):
    words = set(re.findall(r"[a-z]+", text.lower()))
    return sorted(v for v in verbs if v in words)


def has_contact(text):
    email = re.search(r"[\w.\-]+@[\w.\-]+\.\w+", text)
    phone = re.search(r"(\+?\d[\d\-\s()]{7,}\d)", text)
    return {"email": bool(email), "phone": bool(phone)}


def has_numbers(text):
    """Quantified achievements ('cut cost 60%') are stronger -- do any appear?"""
    return bool(re.search(r"\d+\s*%|\b\d{2,}\b", text))


def analyze(resume_text, job_description, db=None):
    db = db or load_db()
    skills, verbs = db["skills"], db["action_verbs"]

    resume_skills = find_skills(resume_text, skills)
    jd_skills = find_skills(job_description, skills)

    # Match score: of the skills the JOB asks for, how many are in the resume?
    if jd_skills:
        matched = resume_skills & jd_skills
        missing = jd_skills - resume_skills
        score = round(100 * len(matched) / len(jd_skills))
    else:
        # No known skills in the JD -> fall back to word overlap.
        matched, missing = resume_skills, set()
        score = min(100, len(resume_skills) * 10)

    words = re.findall(r"[a-zA-Z0-9']+", resume_text)
    report = {
        "match_score": score,
        "matched_skills": sorted(matched),
        "missing_skills": sorted(missing),
        "resume_skills": sorted(resume_skills),
        "word_count": len(words),
        "action_verbs": count_action_verbs(resume_text, verbs),
        "contact": has_contact(resume_text),
        "has_numbers": has_numbers(resume_text),
    }
    report["suggestions"] = build_suggestions(report)
    return report


def build_suggestions(r):
    tips = []
    if r["missing_skills"]:
        tips.append("Add these job-required skills if you have them: %s."
                    % ", ".join(r["missing_skills"]))
    if r["word_count"] < 200:
        tips.append("Your resume looks short (%d words) - add more detail on projects and impact."
                    % r["word_count"])
    elif r["word_count"] > 900:
        tips.append("Your resume is long (%d words) - trim to one page for entry-level roles."
                    % r["word_count"])
    if len(r["action_verbs"]) < 3:
        tips.append("Start bullet points with strong action verbs (Built, Designed, Deployed, Reduced).")
    if not r["has_numbers"]:
        tips.append("Quantify results with numbers (e.g. 'cut runtime by 40%', '0.82 ROC-AUC').")
    if not r["contact"]["email"]:
        tips.append("Add a professional email address near the top.")
    if not tips:
        tips.append("Strong match! Tailor the summary line to mention the top job skills first.")
    return tips


if __name__ == "__main__":
    # Offline self-test:  python analyzer.py
    resume = """Priya Sharma  priya.example@email.com
    Built a churn model in Python with scikit-learn (0.82 ROC-AUC).
    Analysed a 50,000-row dataset with pandas and deployed a Flask API.
    Skills: Python, pandas, machine learning, Flask, git."""
    jd = """Looking for a junior ML engineer with Python, machine learning,
    SQL, Docker and Flask experience. Data visualization is a plus."""
    rep = analyze(resume, jd)
    print("Match score:", rep["match_score"], "%")
    print("Matched:", rep["matched_skills"])
    print("Missing:", rep["missing_skills"])
    print("Word count:", rep["word_count"], "| verbs:", rep["action_verbs"])
    print("Suggestions:")
    for s in rep["suggestions"]:
        print(" -", s)
