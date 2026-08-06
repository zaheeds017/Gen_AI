"""
============================================================
 PROJECT 3 : TEXT PREPROCESSING TOOLKIT
 Module 6  : Natural Language Processing
 AI Powered Engineering Upskilling Program (2026 Edition)
============================================================

WHY THIS PROJECT MATTERS
------------------------
Before any NLP model (spam, sentiment, chatbots) can work, raw text
must be CLEANED and turned into NUMBERS. This toolkit walks through
every core preprocessing step, showing the text before and after, then
turns sentences into Bag-of-Words and TF-IDF vectors - the exact
technique Projects 1 and 2 rely on.

STEPS DEMONSTRATED
    1. Lowercasing
    2. Removing punctuation & numbers
    3. Tokenization (split into words)
    4. Stop-word removal
    5. Stemming (chopping words to their root - simplified demo)
    6. Bag-of-Words (word counts)
    7. TF-IDF (weighted importance)
    8. A word-frequency chart -> word_frequencies.png

HOW TO RUN
----------
1. Install once:  pip install scikit-learn matplotlib
2. In this folder:  python text_preprocessing.py
3. Open `word_frequencies.png`.

CONCEPTS PRACTISED (Module 6)
-----------------------------
- Text preprocessing pipeline (the foundation of all NLP)
- Tokenization, stop words, stemming
- Bag-of-Words and TF-IDF (turning words into numbers = "embeddings 101")

NOTE ON OUTPUT
--------------
Console text is plain ASCII; the chart is SAVED as a PNG.
"""

import re

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from sklearn.feature_extraction.text import (CountVectorizer, TfidfVectorizer,
                                             ENGLISH_STOP_WORDS)

CHART_FILE = "word_frequencies.png"

SAMPLE_TEXT = (
    "Natural Language Processing is amazing! In 2026, AI systems can read, "
    "understand, and generate human language. Machines are learning to "
    "process text, analyze sentiment, and even chat like humans."
)

# A few short sentences for the Bag-of-Words / TF-IDF demo.
SENTENCES = [
    "I love natural language processing",
    "Language models can process text",
    "I love learning about AI and language",
]


def simple_stem(word: str) -> str:
    """A VERY simplified stemmer: chop common English suffixes to a root.
    (Real stemmers like Porter are smarter; this shows the idea.)"""
    for suffix in ("ing", "ly", "ed", "es", "s"):
        if word.endswith(suffix) and len(word) - len(suffix) >= 3:
            return word[: -len(suffix)]
    return word


def main() -> None:
    print("=" * 60)
    print("           TEXT PREPROCESSING TOOLKIT")
    print("=" * 60)
    print(f"\nOriginal text:\n   {SAMPLE_TEXT}")

    # STEP 1: lowercasing - "AI" and "ai" should be the same token.
    lowered = SAMPLE_TEXT.lower()
    print(f"\n[1] Lowercased:\n   {lowered}")

    # STEP 2: remove punctuation and numbers with a regex (keep letters/spaces).
    no_punct = re.sub(r"[^a-z\s]", "", lowered)
    no_punct = re.sub(r"\s+", " ", no_punct).strip()   # squeeze extra spaces
    print(f"\n[2] Punctuation & numbers removed:\n   {no_punct}")

    # STEP 3: tokenization - split the string into a list of words (tokens).
    tokens = no_punct.split()
    print(f"\n[3] Tokenized ({len(tokens)} tokens):\n   {tokens}")

    # STEP 4: stop-word removal - drop common low-meaning words (the, is, and).
    meaningful = [t for t in tokens if t not in ENGLISH_STOP_WORDS]
    print(f"\n[4] Stop words removed ({len(meaningful)} tokens):\n   {meaningful}")

    # STEP 5: stemming - reduce words to a root so 'learning'/'learn' match.
    stemmed = [simple_stem(t) for t in meaningful]
    print(f"\n[5] Stemmed:\n   {stemmed}")

    # STEP 6: Bag-of-Words - count how often each word appears per sentence.
    print("\n" + "-" * 60)
    print("[6] BAG-OF-WORDS (word counts per sentence)")
    print("-" * 60)
    count_vec = CountVectorizer()
    bow = count_vec.fit_transform(SENTENCES).toarray()
    vocab = count_vec.get_feature_names_out()
    print("Vocabulary:", list(vocab))
    for i, sentence in enumerate(SENTENCES):
        # int(c) keeps the printout clean (plain 0/1 instead of np.int64(0)).
        counts_row = {w: int(c) for w, c in zip(vocab, bow[i])}
        print(f"   S{i+1}: {counts_row}")
        print(f"        \"{sentence}\"")

    # STEP 7: TF-IDF - like Bag-of-Words but rare, distinctive words weigh more.
    print("\n" + "-" * 60)
    print("[7] TF-IDF (importance weights, rounded)")
    print("-" * 60)
    tfidf_vec = TfidfVectorizer()
    tfidf = tfidf_vec.fit_transform(SENTENCES).toarray()
    tvocab = tfidf_vec.get_feature_names_out()
    print("For sentence 1, word weights:")
    weights = sorted(zip(tvocab, tfidf[0].round(2)), key=lambda kv: -kv[1])
    for word, weight in weights:
        if weight > 0:
            print(f"   {word:<12}: {weight}")

    # STEP 8: word-frequency chart across all sentences.
    total_counts = bow.sum(axis=0)                     # sum counts down columns
    pairs = sorted(zip(vocab, total_counts), key=lambda kv: -kv[1])
    words = [w for w, c in pairs]
    counts = [c for w, c in pairs]
    plt.figure(figsize=(10, 6))
    plt.bar(words, counts, color="#4c72b0")
    plt.title("Word Frequencies (Bag-of-Words)")
    plt.ylabel("Count")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(CHART_FILE, dpi=100)
    plt.close()
    print(f"\n[OK] Word-frequency chart saved to '{CHART_FILE}'.")
    print("\nThese vectors are exactly what Projects 1 & 2 feed to their models!")


if __name__ == "__main__":
    main()
