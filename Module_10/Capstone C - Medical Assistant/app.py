"""
app.py - Educational Health-Info Assistant (Streamlit).

Describe everyday symptoms in plain words and get GENERAL, educational
information plus clear "see a doctor if..." guidance. If the description
contains an emergency red-flag, the app stops and tells you to seek urgent
help instead of showing self-care tips.

This app is deliberately conservative. It is a learning project, not a
medical device.

Run:  streamlit run app.py
"""

import streamlit as st

import medical_engine as engine

st.set_page_config(page_title="Health-Info Assistant (Educational)", page_icon=":hospital:")


@st.cache_resource
def get_info():
    return engine.load_info()


info = get_info()

st.title("Health-Info Assistant")
st.caption("An educational demo - it explains common symptoms. It does not diagnose.")

# The disclaimer is shown FIRST and always -- this is the most important element.
st.error(info["disclaimer"])

symptoms = st.text_area(
    "Describe how you are feeling (plain words are fine):",
    placeholder="e.g. runny nose, sore throat and a mild cough",
    height=110,
)

if st.button("Get information", type="primary"):
    if not symptoms.strip():
        st.warning("Please describe your symptoms first.")
    else:
        result = engine.assess(symptoms, info)

        if result["emergency"]:
            # Emergency path: loud warning, NO self-care tips.
            st.markdown("## :red[Seek urgent help]")
            st.error(result["message"])
            st.write("Detected: **%s**" % ", ".join(result["emergency_flags"]))
        elif result["conditions"]:
            st.info(result["message"])
            for cond in result["conditions"]:
                with st.expander(cond["name"], expanded=True):
                    st.write(cond["info"])
                    st.markdown("**Self-care ideas:**")
                    for tip in cond["self_care"]:
                        st.write("- " + tip)
                    st.markdown("**See a doctor if:**")
                    for warn in cond["see_doctor_if"]:
                        st.write("- " + warn)
        else:
            st.info(result["message"])

        st.divider()
        st.caption(info["disclaimer"])

with st.sidebar:
    st.header("Why so cautious?")
    st.write(
        "When software touches health, being honest about its limits matters "
        "more than looking clever. This app:")
    st.write("- always shows a disclaimer")
    st.write("- never claims to diagnose")
    st.write("- checks for emergency red-flags first")
    st.write("Topics it knows: cold, fever, headache, cough, upset stomach, muscle strain.")
