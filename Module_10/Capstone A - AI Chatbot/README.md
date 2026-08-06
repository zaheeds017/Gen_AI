# Capstone A — AI Chatbot 💬

A help-desk chatbot that answers questions from a **knowledge base**. It finds the best-matching answer with a tiny **TF-IDF retriever** written in pure Python (the idea from Module 6), and can optionally be powered by a real **Claude** model (Module 7).

This capstone ties together **NLP + Generative AI + Deployment**.

---

## What it does

- A real chat interface (`st.chat_input` / `st.chat_message`) with conversation memory.
- **Mock mode (default):** matches your question to the closest FAQ — offline, free, instant.
- **Real mode (optional):** sends the question to Claude, grounded in the same facts.
- Falls back gracefully ("I'm not sure...") when a question is out of scope.

---

## Files

```
chatbot_engine.py    # the brain: TF-IDF retriever + answering logic (pure Python)
knowledge_base.json  # the FAQ facts the bot answers from   <-- EDIT THIS
app.py               # the Streamlit chat UI
```

The logic is in `chatbot_engine.py` (no Streamlit), so you can test it directly:
```bash
python chatbot_engine.py
```

---

## ▶️ Run it

```bash
pip install streamlit          # once
streamlit run app.py           # opens http://localhost:8501
```

Ask things like *"what language does the course use?"*, *"how do I deploy my model?"*, or *"tell me about the capstone"*.

### Optional — real Claude mode

```bash
pip install anthropic
export ANTHROPIC_API_KEY="sk-ant-..."       # from console.anthropic.com
# then set  USE_REAL_API = True  at the top of chatbot_engine.py
```

---

## How the retriever works (the NLP idea)

```
1. Turn each FAQ (question + answer) into a bag of words, dropping stop-words.
2. Weight words by TF-IDF: rare, meaningful words count more than common ones.
3. For a new question, pick the FAQ with the highest cosine similarity.
4. If even the best match is weak, admit the bot doesn't know.
```

No machine-learning library needed — it's all a few lines of math, which makes it easy to read and explain in an interview.

---

## 🎯 Challenges

1. **Make it yours:** replace `knowledge_base.json` with facts about *your* project, club, or product.
2. **Show confidence:** display the match score next to each answer.
3. **Add "did you mean?":** when the score is low, suggest the 2 closest FAQ questions.
4. **Go live:** deploy to Streamlit Community Cloud and share the link (see notes §9 of Module 9).

> 💡 A chatbot that grounds its answers in *your* facts and admits when it doesn't know is far more trustworthy than one that guesses.
