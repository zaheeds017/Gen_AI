"""
============================================================
 PROJECT 1 : SPAM DETECTION  (Text Classification)
 Module 6  : Natural Language Processing
 AI Powered Engineering Upskilling Program (2026 Edition)
============================================================

WHAT THIS PROGRAM DOES
----------------------
Builds an NLP model that reads a text message and decides if it is
SPAM or HAM (not spam). This is the classic first NLP project and the
same idea behind your email spam filter.

    1. LOAD a small labelled dataset of messages (spam / ham).
    2. TURN TEXT INTO NUMBERS using TF-IDF (a model can't read words).
    3. TRAIN a Naive Bayes classifier (great for text).
    4. EVALUATE: accuracy, precision, recall, F1, confusion matrix.
    5. Show the TOP spam-indicating words the model learned.
    6. PREDICT spam/ham for brand-new messages (with probability).

HOW TO RUN
----------
1. Install once:  pip install scikit-learn matplotlib seaborn
2. In this folder:  python spam_detection.py
3. Open `spam_confusion_matrix.png`.

CONCEPTS PRACTISED (Module 6)
-----------------------------
- Text preprocessing (lowercasing, stop-word removal via TF-IDF)
- Bag-of-words / TF-IDF: turning text into feature vectors
- Text classification with Naive Bayes
- Evaluating a classifier (confusion matrix, precision/recall)
- Interpreting a model (most spammy words)

NOTE ON OUTPUT
--------------
Console text is plain ASCII; the chart is SAVED as a PNG.
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import (accuracy_score, confusion_matrix,
                             classification_report)

CHART_FILE = "spam_confusion_matrix.png"

# A small labelled dataset. In the real world you'd load thousands of rows
# from a CSV; here they are inline so the project is self-contained.
DATA = [
    # ---- SPAM ----
    ("Congratulations! You won a FREE iPhone. Click here to claim now!", "spam"),
    ("WINNER!! You have been selected for a $1000 cash prize. Call now!", "spam"),
    ("URGENT! Your account has been suspended. Verify at this link.", "spam"),
    ("Free entry in a weekly competition to win tickets! Text WIN to 80085", "spam"),
    ("Claim your free gift card now, limited time offer, click below", "spam"),
    ("You have won a lottery of 5,00,000. Send your bank details to claim.", "spam"),
    ("Hot singles in your area want to chat! Reply YES to connect.", "spam"),
    ("Get cheap loans instantly with no credit check. Apply today!", "spam"),
    ("Your number won our lucky draw! Claim $500 reward immediately.", "spam"),
    ("Buy now and get 90% OFF! Best deal ever, hurry limited stock!", "spam"),
    ("Earn $5000 per week working from home, no experience needed!", "spam"),
    ("Final notice: your prize is waiting. Click to collect your reward.", "spam"),
    ("Exclusive offer just for you! Free vacation to Dubai, claim now.", "spam"),
    ("Your PayPal account is limited. Confirm your details urgently here.", "spam"),
    ("Double your bitcoin in 24 hours! Invest now, guaranteed returns.", "spam"),
    ("Text STOP to unsubscribe. You won a free ringtone every week!", "spam"),
    ("Act now! Your car warranty is about to expire. Call this number.", "spam"),
    ("You are pre-approved for a credit card with $10000 limit. Apply!", "spam"),
    ("FREE!! Nokia phone waiting for you. Just pay shipping to claim it.", "spam"),
    ("Cheap meds online without prescription. Order now and save big!", "spam"),
    # ---- HAM (normal messages) ----
    ("Hey, are we still meeting for lunch tomorrow at 1pm?", "ham"),
    ("Can you send me the notes from today's lecture please?", "ham"),
    ("Happy birthday! Hope you have a wonderful day today.", "ham"),
    ("I'll be a bit late for the meeting, stuck in traffic.", "ham"),
    ("Thanks for your help yesterday, really appreciate it.", "ham"),
    ("Don't forget to submit the assignment by Friday.", "ham"),
    ("Let's catch up this weekend, been a while!", "ham"),
    ("The project demo went really well, the team was impressed.", "ham"),
    ("Mom asked if you're coming home for dinner tonight.", "ham"),
    ("Please review the pull request when you get a chance.", "ham"),
    ("Great game last night! Did you see that final goal?", "ham"),
    ("I've attached the report. Let me know your feedback.", "ham"),
    ("Reminder: dentist appointment on Monday at 10am.", "ham"),
    ("Could you pick up some milk on your way back home?", "ham"),
    ("The train is delayed by 20 minutes, sorry for the wait.", "ham"),
    ("Congrats on passing your exam, you worked so hard for it!", "ham"),
    ("Let me know if the code changes fixed the bug.", "ham"),
    ("We're planning a trip next month, want to join us?", "ham"),
    ("Your order has shipped and will arrive on Thursday.", "ham"),
    ("See you at the study group at 6, bring your laptop.", "ham"),
]


def top_spam_words(vectorizer, model, n=10):
    """Return the words most strongly associated with the 'spam' class."""
    features = vectorizer.get_feature_names_out()
    # model.classes_ is sorted -> ['ham', 'spam']; index 1 is 'spam'.
    spam_scores = model.feature_log_prob_[1] - model.feature_log_prob_[0]
    top_idx = spam_scores.argsort()[-n:][::-1]      # highest-scoring features
    return [features[i] for i in top_idx]


def main() -> None:
    print("=" * 52)
    print("           SPAM DETECTION (NLP)")
    print("=" * 52)

    texts = [text for text, label in DATA]
    labels = [label for text, label in DATA]
    print(f"Dataset: {len(texts)} messages "
          f"({labels.count('spam')} spam, {labels.count('ham')} ham).")

    # --- STEP 1: turn text into numbers with TF-IDF ------------------------
    # TF-IDF gives each word a weight: common-everywhere words count little,
    # words that are distinctive to a message count a lot. stop_words removes
    # 'the', 'a', 'is', etc. Every message becomes a vector of numbers.
    vectorizer = TfidfVectorizer(stop_words="english", lowercase=True)
    X = vectorizer.fit_transform(texts)
    print(f"Vocabulary size: {len(vectorizer.get_feature_names_out())} words. "
          f"Each message -> a {X.shape[1]}-number vector.")

    # --- STEP 2: split into train/test -------------------------------------
    X_train, X_test, y_train, y_test = train_test_split(
        X, labels, test_size=0.3, random_state=42, stratify=labels)

    # --- STEP 3: train Naive Bayes (a fast, strong text classifier) --------
    model = MultinomialNB()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    # --- STEP 4: evaluate --------------------------------------------------
    acc = accuracy_score(y_test, y_pred)
    print(f"\n----- RESULTS (on unseen test messages) -----")
    print(f"Accuracy: {acc:.3f}")
    print("\nClassification report:")
    print(classification_report(y_test, y_pred))

    # --- STEP 5: what did it learn? ----------------------------------------
    print("Top words the model treats as SPAM signals:")
    print("   " + ", ".join(top_spam_words(vectorizer, model)))

    # Confusion matrix -> PNG
    cm = confusion_matrix(y_test, y_pred, labels=["ham", "spam"])
    plt.figure(figsize=(6, 5))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues",
                xticklabels=["ham", "spam"], yticklabels=["ham", "spam"])
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.title("Spam Detection - Confusion Matrix")
    plt.tight_layout()
    plt.savefig(CHART_FILE, dpi=100)
    plt.close()
    print(f"\n[OK] Confusion matrix saved to '{CHART_FILE}'.")

    # --- STEP 6: try the model on brand-new messages -----------------------
    new_messages = [
        "Congratulations! Claim your FREE prize money now by clicking here!",
        "Hey, can we reschedule our call to 3pm tomorrow?",
        "URGENT: verify your bank account or it will be closed today!",
        "Thanks for the notes, see you in class on Monday.",
    ]
    print("\n----- PREDICTIONS ON NEW MESSAGES -----")
    new_X = vectorizer.transform(new_messages)
    preds = model.predict(new_X)
    probs = model.predict_proba(new_X)
    spam_index = list(model.classes_).index("spam")
    for msg, pred, prob in zip(new_messages, preds, probs):
        tag = "SPAM" if pred == "spam" else "ham "
        print(f"   [{tag}] ({prob[spam_index]*100:3.0f}% spam)  {msg[:50]}...")


if __name__ == "__main__":
    main()
