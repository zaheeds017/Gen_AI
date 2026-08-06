# Capstone C — Medical Assistant 🏥

> ⚠️ **This is an EDUCATIONAL demo. It does NOT diagnose and is NOT medical advice.** It matches everyday symptom words to general information and clear "see a doctor if..." guidance, and it checks for emergency warning signs first. Always consult a qualified healthcare professional. In an emergency, call your local emergency number.

This capstone is the program's lesson in **responsible AI**: when software touches people's health, being honest about its limits matters more than looking clever.

---

## What it does

- You describe how you feel in plain words.
- If your description contains an **emergency red-flag** (e.g. "chest pain", "difficulty breathing", "slurred speech"), the app **stops and tells you to seek urgent help** — no self-care tips.
- Otherwise it shows **general, educational information** for common topics (cold, fever, headache, cough, upset stomach, muscle strain), each with self-care ideas and "see a doctor if..." warnings.
- A disclaimer is shown **first and always**.

---

## Files

```
medical_engine.py   # the logic: emergency check + educational matching (pure Python)
health_info.json    # the disclaimer, red-flags, and educational topics   <-- EDIT THIS
app.py              # the Streamlit UI (disclaimer banner + results)
```

Test the engine directly:
```bash
python medical_engine.py
```

---

## ▶️ Run it

```bash
pip install streamlit          # once
streamlit run app.py           # opens http://localhost:8501
```

Try *"runny nose, sore throat and a mild cough"* (educational info) and *"sudden chest pain and difficulty breathing"* (emergency path).

---

## The safety design (why it's built this way)

```
1. ALWAYS show the disclaimer, up front and again at the end.
2. Check for emergency red-flags FIRST. If found -> urge urgent help, show NOTHING else.
3. Only for everyday symptoms -> show general info + "see a doctor if..." limits.
4. NEVER output a diagnosis or a treatment decision.
```

This "safety gate before features" ordering is the whole point of the project.

---

## 🎯 Challenges

1. **Add a topic** (carefully): add one common condition to `health_info.json` with the same fields, keeping the cautious tone.
2. **Strengthen the red-flags:** add more emergency phrases and test that they trigger the urgent-help path.
3. **Add an age/consent gate** before showing any information.
4. **Reflect:** write a short paragraph on the *ethical risks* of a real symptom checker and how you would reduce them (great interview material).

> 💡 The most important feature of this app is the word "**no**" — knowing when *not* to answer. That instinct is what makes AI safe to put in front of real people.
