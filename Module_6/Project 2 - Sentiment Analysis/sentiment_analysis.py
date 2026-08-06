"""
============================================================
 PROJECT 2 : SENTIMENT ANALYSIS  (Positive / Negative)
 Module 6  : Natural Language Processing
 AI Powered Engineering Upskilling Program (2026 Edition)
============================================================

WHAT THIS PROGRAM DOES
----------------------
Builds an NLP model that reads a review and decides if the sentiment
is POSITIVE or NEGATIVE. Companies use this to understand what
customers feel from thousands of reviews, tweets, and support tickets.

    1. LOAD a small labelled dataset of reviews (positive / negative).
    2. TURN TEXT INTO NUMBERS with TF-IDF.
    3. TRAIN a Logistic Regression classifier.
    4. EVALUATE it.
    5. Show the most POSITIVE and most NEGATIVE words it learned.
    6. PREDICT the sentiment of new sentences (with confidence).
    7. VISUALIZE the sentiment-driving words -> sentiment_words.png.

HOW TO RUN
----------
1. Install once:  pip install scikit-learn matplotlib
2. In this folder:  python sentiment_analysis.py
3. Open `sentiment_words.png`.

CONCEPTS PRACTISED (Module 6)
-----------------------------
- Sentiment analysis (a core NLP task)
- TF-IDF vectorization
- Logistic Regression for text
- Reading model coefficients (positive vs negative words)
- predict_proba (a confidence, not just a label)

NOTE ON OUTPUT
--------------
Console text is plain ASCII; the chart is SAVED as a PNG.
"""

import numpy as np

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

CHART_FILE = "sentiment_words.png"

DATA = [
    # ---- POSITIVE ----
    ("This movie was absolutely fantastic, I loved every minute!", "positive"),
    ("Amazing product, works perfectly and great value for money.", "positive"),
    ("The food was delicious and the service was wonderful.", "positive"),
    ("Brilliant performance, highly recommend it to everyone.", "positive"),
    ("I am so happy with this purchase, exceeded my expectations.", "positive"),
    ("Excellent quality and super fast delivery, very pleased.", "positive"),
    ("A beautiful, heartwarming story with great acting.", "positive"),
    ("Best decision ever, this app makes my life so much easier.", "positive"),
    ("The hotel was clean, comfortable and the staff were lovely.", "positive"),
    ("Superb experience from start to finish, thank you so much!", "positive"),
    ("Incredible value, I will definitely buy this again.", "positive"),
    ("The course was informative, engaging and really well taught.", "positive"),
    ("Loved the design, it is sleek, fast and easy to use.", "positive"),
    ("Wonderful customer support, they solved my issue instantly.", "positive"),
    ("Such a fun and enjoyable game, I really liked it a lot.", "positive"),
    ("Great phone with an awesome camera and long battery life.", "positive"),
    ("Fantastic value, the quality is excellent and worth every penny.", "positive"),
    ("I love this restaurant, the pizza is amazing and tasty.", "positive"),
    ("Perfect fit, comfortable and stylish, I am very satisfied.", "positive"),
    ("The teacher was helpful and the lessons were clear and fun.", "positive"),
    ("Smooth, fast and reliable, this laptop is a great buy.", "positive"),
    ("Delightful stay, cozy rooms and a friendly, helpful staff.", "positive"),
    ("This book is inspiring, well written and truly enjoyable.", "positive"),
    ("Outstanding service and a wonderful, memorable experience.", "positive"),
    ("The app is intuitive, beautiful and works flawlessly.", "positive"),
    ("Delicious meal, generous portions and a lovely atmosphere.", "positive"),
    ("Highly satisfied, excellent build quality and great support.", "positive"),
    ("An amazing concert, the band was energetic and brilliant.", "positive"),
    ("Very impressed, easy setup and it works like a charm.", "positive"),
    ("A joy to use, thoughtful design and superb performance.", "positive"),
    # ---- NEGATIVE ----
    ("Terrible experience, the product broke after one day.", "negative"),
    ("Awful service, the staff were rude and unhelpful.", "negative"),
    ("I hated this movie, it was boring and way too long.", "negative"),
    ("Worst purchase ever, a complete waste of money.", "negative"),
    ("The food was cold, tasteless and overpriced.", "negative"),
    ("Very disappointed, it did not work as advertised.", "negative"),
    ("Poor quality, cheap materials and it fell apart quickly.", "negative"),
    ("Horrible app, it keeps crashing and freezing constantly.", "negative"),
    ("The delivery was late and the item arrived damaged.", "negative"),
    ("Do not buy this, it is a scam and total garbage.", "negative"),
    ("Extremely frustrating, the instructions made no sense.", "negative"),
    ("The hotel room was dirty and smelled bad, never again.", "negative"),
    ("Slow, buggy and full of annoying ads, I uninstalled it.", "negative"),
    ("A boring, predictable and disappointing sequel.", "negative"),
    ("I regret buying this, it stopped working within a week.", "negative"),
    ("Useless product, it never worked and the support ignored me.", "negative"),
    ("Disgusting food and painfully slow service, avoid this place.", "negative"),
    ("The phone is laggy, the battery dies fast and it overheats.", "negative"),
    ("Overpriced and low quality, I feel completely ripped off.", "negative"),
    ("The worst hotel stay, noisy, dirty and terribly managed.", "negative"),
    ("Cheaply made and it broke on the first day, very poor.", "negative"),
    ("Confusing, clunky and frustrating, a truly bad experience.", "negative"),
    ("The movie was dull and the acting was awful and lifeless.", "negative"),
    ("Rude staff and a filthy table, I will not come back.", "negative"),
    ("This gadget is a total failure, it does not do anything right.", "negative"),
    ("Horrible quality control, the item arrived broken and useless.", "negative"),
    ("Very unhappy, the app is slow and constantly loses my data.", "negative"),
    ("A disappointing meal, bland, greasy and not worth the price.", "negative"),
    ("Terrible customer service, they were unhelpful and dismissive.", "negative"),
    ("The product is faulty, it stopped charging after two days.", "negative"),
]


def extreme_words(vectorizer, model, n=10):
    """Return the most positive and most negative words (by coefficient)."""
    features = vectorizer.get_feature_names_out()
    coefs = model.coef_[0]        # >0 pushes toward 'positive', <0 toward 'negative'
    top_pos_idx = coefs.argsort()[-n:][::-1]
    top_neg_idx = coefs.argsort()[:n]
    pos = [(features[i], coefs[i]) for i in top_pos_idx]
    neg = [(features[i], coefs[i]) for i in top_neg_idx]
    return pos, neg


def main() -> None:
    print("=" * 52)
    print("          SENTIMENT ANALYSIS (NLP)")
    print("=" * 52)

    texts = [t for t, s in DATA]
    labels = [s for t, s in DATA]
    print(f"Dataset: {len(texts)} reviews "
          f"({labels.count('positive')} positive, "
          f"{labels.count('negative')} negative).")

    # STEP 1: TF-IDF vectorization (text -> numbers).
    # IMPORTANT: for sentiment we do NOT remove stop words, because words like
    # "not", "no" and "never" flip meaning ("not good" != "good"). We also add
    # bigrams (pairs of words) so "not good" is captured as one feature.
    vectorizer = TfidfVectorizer(lowercase=True, ngram_range=(1, 2))
    X = vectorizer.fit_transform(texts)

    # STEP 2: split.
    X_train, X_test, y_train, y_test = train_test_split(
        X, labels, test_size=0.3, random_state=42, stratify=labels)

    # STEP 3: train Logistic Regression.
    # C=10 lowers the regularization so the model can be more confident
    # (TF-IDF values are small, so we let the coefficients grow a bit).
    model = LogisticRegression(max_iter=1000, C=10)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    # STEP 4: evaluate.
    print(f"\n----- RESULTS (on unseen test reviews) -----")
    print(f"Accuracy: {accuracy_score(y_test, y_pred):.3f}")
    print("\nClassification report:")
    print(classification_report(y_test, y_pred, zero_division=0))

    # STEP 5: most positive / negative words.
    pos, neg = extreme_words(vectorizer, model)
    print("Most POSITIVE words:", ", ".join(w for w, c in pos))
    print("Most NEGATIVE words:", ", ".join(w for w, c in neg))

    # STEP 6: predict new sentences.
    new_reviews = [
        "This is the best thing I have ever bought, absolutely love it!",
        "What a horrible waste of time, I want a refund.",
        "The design is beautiful and it works great.",
        "Cheap, broken and completely useless.",
    ]
    print("\n----- PREDICTIONS ON NEW REVIEWS -----")
    new_X = vectorizer.transform(new_reviews)
    preds = model.predict(new_X)
    probs = model.predict_proba(new_X)
    pos_index = list(model.classes_).index("positive")
    for review, pred, prob in zip(new_reviews, preds, probs):
        print(f"   [{pred.upper():8}] ({prob[pos_index]*100:3.0f}% positive)  "
              f"{review[:45]}...")

    # STEP 7: visualize the sentiment-driving words.
    words = [w for w, c in reversed(neg)] + [w for w, c in reversed(pos)]
    scores = [c for w, c in reversed(neg)] + [c for w, c in reversed(pos)]
    colors = ["#c44e52" if s < 0 else "#55a868" for s in scores]
    plt.figure(figsize=(10, 8))
    plt.barh(range(len(words)), scores, color=colors)
    plt.yticks(range(len(words)), words)
    plt.axvline(0, color="black", linewidth=0.8)
    plt.xlabel("<- Negative        Coefficient        Positive ->")
    plt.title("Words That Drive Sentiment")
    plt.tight_layout()
    plt.savefig(CHART_FILE, dpi=100)
    plt.close()
    print(f"\n[OK] Sentiment-word chart saved to '{CHART_FILE}'.")


if __name__ == "__main__":
    main()
