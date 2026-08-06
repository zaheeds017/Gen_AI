"""
chatbot_engine.py - the "brain" of the chatbot, with NO Streamlit and NO web code.

It answers questions from a small knowledge base (knowledge_base.json) using a
tiny TF-IDF retriever written in plain Python -- the same idea you learned in
the NLP module (Module 6), here with zero external libraries so it runs anywhere.

TWO MODES:
  * MOCK (default)  -> finds the best-matching FAQ answer. Offline, free, instant.
  * REAL (optional) -> sends the question to Claude for a natural reply.

Flip USE_REAL_API to True and set an API key to try the real mode.
"""

import json
import math
import os
import re
from collections import Counter

# ---- Config -------------------------------------------------------------
USE_REAL_API = False          # keep False for the offline mock (no key needed)
MODEL = "claude-opus-5"       # used only when USE_REAL_API is True
SIMILARITY_FLOOR = 0.05       # below this we admit we don't know

HERE = os.path.dirname(__file__)


# ---- Load the knowledge base -------------------------------------------
def load_kb(path=None):
    path = path or os.path.join(HERE, "knowledge_base.json")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


# ---- Tiny TF-IDF retriever (pure Python) --------------------------------
# Very common words carry little meaning and would make unrelated questions
# look similar, so we drop them (the same idea as stop-words in Module 6).
STOPWORDS = {
    "the", "a", "an", "is", "are", "was", "were", "be", "been", "to", "of",
    "in", "on", "for", "and", "or", "do", "does", "did", "i", "you", "it",
    "this", "that", "what", "how", "can", "me", "my", "your", "about", "with",
    "as", "at", "by", "from", "will", "would", "should", "if", "so", "we",
}


def tokenize(text):
    """Lowercase, split into word tokens, and drop common stop-words."""
    return [t for t in re.findall(r"[a-z0-9]+", text.lower()) if t not in STOPWORDS]


class Retriever:
    """Ranks FAQ entries by TF-IDF cosine similarity to the user's question."""

    def __init__(self, faqs):
        self.faqs = faqs
        # Each "document" is the question + answer text.
        self.docs = [tokenize(f["q"] + " " + f["a"]) for f in faqs]
        self.idf = self._compute_idf(self.docs)
        self.doc_vecs = [self._vectorize(doc) for doc in self.docs]

    def _compute_idf(self, docs):
        n = len(docs)
        df = Counter()
        for doc in docs:
            for term in set(doc):
                df[term] += 1
        # +1 smoothing so no term ever gets an infinite/zero weight.
        return {t: math.log((n + 1) / (df_t + 1)) + 1 for t, df_t in df.items()}

    def _vectorize(self, tokens):
        tf = Counter(tokens)
        return {t: tf[t] * self.idf.get(t, 0.0) for t in tf}

    @staticmethod
    def _cosine(a, b):
        common = set(a) & set(b)
        dot = sum(a[t] * b[t] for t in common)
        na = math.sqrt(sum(v * v for v in a.values()))
        nb = math.sqrt(sum(v * v for v in b.values()))
        if na == 0 or nb == 0:
            return 0.0
        return dot / (na * nb)

    def best_match(self, query):
        """Returns (faq_dict, score) for the closest FAQ, or (None, 0)."""
        qv = self._vectorize(tokenize(query))
        best_i, best_score = -1, 0.0
        for i, dv in enumerate(self.doc_vecs):
            s = self._cosine(qv, dv)
            if s > best_score:
                best_i, best_score = i, s
        if best_i == -1:
            return None, 0.0
        return self.faqs[best_i], best_score


# ---- The two answering modes -------------------------------------------
def answer_mock(query, retriever):
    """Offline answer: return the best-matching FAQ, or a polite fallback."""
    faq, score = retriever.best_match(query)
    if faq is None or score < SIMILARITY_FLOOR:
        return ("I'm not sure about that one. Try asking about the program, "
                "prerequisites, machine learning, deployment, or the capstone.")
    return faq["a"]


def answer_real(query, history, kb):
    """Online answer via Claude. Only called when USE_REAL_API is True."""
    import anthropic  # imported here so mock mode needs nothing installed

    client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY from the environment
    facts = "\n".join("Q: %s\nA: %s" % (f["q"], f["a"]) for f in kb["faqs"])
    system = (
        "You are a friendly help-desk assistant for an AI learning program. "
        "Answer ONLY using the facts below. If the answer is not in them, say "
        "you do not know. Keep replies short and clear.\n\nFACTS:\n" + facts
    )
    messages = history + [{"role": "user", "content": query}]
    resp = client.messages.create(
        model=MODEL, max_tokens=400, system=system, messages=messages
    )
    return "".join(b.text for b in resp.content if b.type == "text")


def get_response(query, history, kb, retriever):
    """Single entry point the app calls. Chooses mock or real automatically."""
    if USE_REAL_API:
        return answer_real(query, history, kb)
    return answer_mock(query, retriever)


if __name__ == "__main__":
    # Quick offline self-test:  python chatbot_engine.py
    kb = load_kb()
    r = Retriever(kb["faqs"])
    for q in ["what language do you use?",
              "how do I put my model online?",
              "tell me about the final project",
              "what is the weather today?"]:
        print("Q:", q)
        print("A:", answer_mock(q, r), "\n")
