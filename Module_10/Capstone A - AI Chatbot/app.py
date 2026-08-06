"""
app.py - the AI Chatbot, as a Streamlit web app.

Streamlit gives us a real chat interface (st.chat_message / st.chat_input) with
almost no web code. The chatbot's "brain" lives in chatbot_engine.py; this file
is only the UI and the conversation memory.

Run:  streamlit run app.py
"""

import streamlit as st

import chatbot_engine as engine

st.set_page_config(page_title="AI Help-Desk Chatbot", page_icon=":speech_balloon:")

st.title("AI Help-Desk Chatbot")
st.caption("A capstone chatbot. Ask about the AI program, ML, deployment, or the capstone.")


# Load the knowledge base + build the retriever ONCE (cached across reruns).
@st.cache_resource
def get_brain():
    kb = engine.load_kb()
    return kb, engine.Retriever(kb["faqs"])


kb, retriever = get_brain()

# st.session_state persists across reruns -> it is our conversation memory.
if "history" not in st.session_state:
    st.session_state.history = [
        {"role": "assistant", "content": "Hi! I'm your program help-desk bot. Ask me anything."}
    ]

# Draw the whole conversation so far.
for msg in st.session_state.history:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# The input box at the bottom. Returns the text when the user hits enter.
user_text = st.chat_input("Type your question...")
if user_text:
    # 1) show + store the user's message
    st.session_state.history.append({"role": "user", "content": user_text})
    with st.chat_message("user"):
        st.write(user_text)

    # 2) get the bot's reply (mock by default; real Claude if enabled)
    reply = engine.get_response(
        user_text,
        [m for m in st.session_state.history if m["role"] in ("user", "assistant")],
        kb,
        retriever,
    )

    # 3) show + store the reply
    st.session_state.history.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.write(reply)

with st.sidebar:
    st.header("About")
    st.write("Mode: **%s**" % ("Real (Claude)" if engine.USE_REAL_API else "Mock (offline)"))
    st.write("The bot answers from a small knowledge base using a TF-IDF retriever.")
    if st.button("Clear chat"):
        st.session_state.history = [
            {"role": "assistant", "content": "Chat cleared. Ask me anything!"}
        ]
        st.rerun()
