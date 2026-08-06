"""
app.py - Resume Analyzer as a Streamlit web app.

Paste your resume and a job description; get a match score, the skills you have
vs the skills you are missing, and concrete tips. The analysis logic lives in
analyzer.py (pure Python) so it can be tested on its own.

Run:  streamlit run app.py
"""

import pandas as pd
import streamlit as st

import analyzer

st.set_page_config(page_title="Resume Analyzer", page_icon=":page_facing_up:", layout="wide")

st.title("Resume Analyzer")
st.caption("Paste a resume and a job description to see how well they match - and how to improve.")


@st.cache_resource
def get_db():
    return analyzer.load_db()


db = get_db()

SAMPLE_RESUME = (
    "Priya Sharma  |  priya.example@email.com\n"
    "Built a churn-prediction model in Python with scikit-learn (0.82 ROC-AUC).\n"
    "Analysed a 50,000-row dataset with pandas and deployed a Flask API.\n"
    "Skills: Python, pandas, machine learning, Flask, Git."
)
SAMPLE_JD = (
    "We are hiring a junior ML engineer. Required: Python, machine learning, "
    "SQL, Docker, and Flask. Data visualization experience is a plus."
)

col1, col2 = st.columns(2)
with col1:
    resume_text = st.text_area("Your resume", value=SAMPLE_RESUME, height=260)
with col2:
    jd_text = st.text_area("Job description", value=SAMPLE_JD, height=260)

if st.button("Analyze", type="primary"):
    if not resume_text.strip() or not jd_text.strip():
        st.warning("Please paste both a resume and a job description.")
    else:
        r = analyzer.analyze(resume_text, jd_text, db)

        st.subheader("Match score")
        st.progress(r["match_score"] / 100)
        st.metric("Resume vs Job match", "%d%%" % r["match_score"])

        c1, c2 = st.columns(2)
        with c1:
            st.markdown("### Skills you have")
            st.write(", ".join(r["matched_skills"]) or "None found")
        with c2:
            st.markdown("### Skills to add")
            st.write(", ".join(r["missing_skills"]) or "None - great coverage!")

        st.markdown("### Resume health")
        health = pd.DataFrame(
            {
                "Check": ["Word count", "Action verbs", "Has email", "Uses numbers"],
                "Result": [
                    str(r["word_count"]),
                    str(len(r["action_verbs"])),
                    "Yes" if r["contact"]["email"] else "No",
                    "Yes" if r["has_numbers"] else "No",
                ],
            }
        )
        st.table(health)

        st.markdown("### Suggestions")
        for tip in r["suggestions"]:
            st.write("- " + tip)

with st.sidebar:
    st.header("How it works")
    st.write("1. Finds known skills in both texts.")
    st.write("2. Score = job skills you already have / job skills required.")
    st.write("3. Checks length, verbs, contact info, and quantified results.")
    st.info("Tip: replace the sample text with your real resume and a job you want.")
