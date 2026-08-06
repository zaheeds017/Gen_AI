# Project 1 — Email Automation 📧⚙️

**Module 8 · AI Agents & Automation**

An automated **workflow** that generates a **personalized email for every person in a list** and "sends" it — the syllabus's *Email Automation* activity. This is exactly the kind of flow you'd build visually in **n8n**, done here in Python so you understand what happens under the hood.

---

## ▶️ How to run

**Mock mode (default — offline, no API key, no SMTP):**
```bash
python email_automation.py
```
It generates 3 personalized emails and "sends" them by saving to an **`outbox/`** folder.

**Real AI mode (Claude writes each email):**
1. `pip install anthropic`
2. Set `ANTHROPIC_API_KEY`, then set `USE_REAL_API = True` and run again.

---

## 🔄 The workflow

```
TRIGGER: read recipient list
   → for each recipient:
        build prompt → generate email → "send" (save to outbox/)
   → REPORT how many were processed
```

This **trigger → steps → action, looped over data** shape *is* workflow automation.

---

## 🖼️ Sample output

```
[1/3] Processing Aarav Sharma <aarav@example.com>
        Subject: A quick update from the AI Program team
        [SENT -> saved to outbox/aarav_sharma.txt]
...
Emails generated and 'sent': 3
```

Each `outbox/*.txt` file contains a complete, personalized email.

---

## ✉️ Real sending (SMTP) — off by default, on purpose

Mock mode "sends" by saving files so **nobody accidentally emails anyone**. To send for real, you'd use Python's built-in `smtplib` with an email account's SMTP settings (e.g., a Gmail **app password** — never your real password):

```python
import smtplib
from email.message import EmailMessage

msg = EmailMessage()
msg["Subject"] = subject
msg["From"] = "you@example.com"
msg["To"] = recipient["email"]
msg.set_content(body)

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login("you@example.com", os.environ["EMAIL_APP_PASSWORD"])
    server.send_message(msg)
```

> ⚠️ Only send emails to people who expect them, and never hard-code passwords — use an environment variable.

---

## 🧩 Concepts practised

Workflow automation (trigger → process → deliver) · per-item prompt building · optional LLM content generation · delivering results · looping over data.

---

## 💡 Challenges

1. Load the recipient list from a **CSV** (`recipients.csv`) instead of the inline list.
2. Add a **"campaign type"** (welcome / reminder / thank-you) that changes the prompt.
3. Add a **dry-run summary** table before sending.
4. Enable real AI mode and compare Claude's emails to the template.
