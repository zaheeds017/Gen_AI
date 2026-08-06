"""
app.py - an interactive portfolio + live ML demo, built with Streamlit.

Streamlit turns a normal Python script into a web app: every time the user
moves a slider or clicks a button, Streamlit re-runs this file top to bottom
and redraws the page. You write Python; it handles the web part.

Run:  streamlit run app.py
Then your browser opens at http://localhost:8501
"""

import pandas as pd
import streamlit as st

import portfolio

# ---- Page setup (must be the first Streamlit call) -----------------------
st.set_page_config(page_title="My AI Portfolio", page_icon=":robot_face:",
                   layout="wide")

# Load data once.
profile = portfolio.load_profile()
projects = portfolio.load_projects()


# Train the demo model ONCE and reuse it (cache_resource remembers it between
# reruns, so sliders feel instant instead of retraining every time).
@st.cache_resource
def get_model():
    return portfolio.build_model()


# ---- Sidebar navigation --------------------------------------------------
st.sidebar.title(profile["name"])
st.sidebar.caption(profile["headline"])
page = st.sidebar.radio("Go to", ["About", "Projects", "Live ML Demo", "Contact"])
st.sidebar.markdown("---")
st.sidebar.write("[GitHub](%s)" % profile["github"])
st.sidebar.write("[LinkedIn](%s)" % profile["linkedin"])


# ---- Pages ---------------------------------------------------------------
if page == "About":
    st.title("Hi, I'm %s" % profile["name"])
    st.subheader(profile["headline"])
    st.write(":round_pushpin: " + profile["location"])
    st.write(profile["about"])

    st.markdown("### Skills")
    skills = profile["skills"]
    skills_df = pd.DataFrame(
        {"Skill": list(skills.keys()), "Level": list(skills.values())}
    ).set_index("Skill")
    st.bar_chart(skills_df)

elif page == "Projects":
    st.title("Projects")
    st.write("A few things I have built while learning.")
    # Two columns of project "cards".
    cols = st.columns(2)
    for i, proj in enumerate(projects):
        with cols[i % 2]:
            with st.container(border=True):
                st.markdown("#### " + proj["title"])
                st.write(proj["description"])
                st.write(" ".join("`%s`" % t for t in proj["tags"]))
                st.markdown("[View code](%s)" % proj["link"])

elif page == "Live ML Demo":
    st.title("Live ML Demo - Iris Classifier")
    st.write("Move the sliders to describe a flower; the model predicts its species in real time.")
    model, feature_names, target_names = get_model()

    # One slider per feature.
    ranges = [(4.0, 8.0, 5.1), (2.0, 4.5, 3.5), (1.0, 7.0, 1.4), (0.1, 2.5, 0.2)]
    features = []
    cols = st.columns(4)
    for col, name, (lo, hi, default) in zip(cols, feature_names, ranges):
        with col:
            features.append(st.slider(name, lo, hi, default, 0.1))

    label, proba = portfolio.predict(model, target_names, features)
    st.success("Predicted species: **%s**" % label)
    proba_df = pd.DataFrame(
        {"Species": list(proba.keys()), "Probability": list(proba.values())}
    ).set_index("Species")
    st.bar_chart(proba_df)

elif page == "Contact":
    st.title("Get in touch")
    st.write("Email: %s" % profile["email"])
    st.write("GitHub: %s" % profile["github"])
    st.write("LinkedIn: %s" % profile["linkedin"])
    st.info("Tip: replace the details in profile.json with your own, then redeploy.")
