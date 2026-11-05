import nltk
from nltk.corpus import stopwords

stop_words = set(stopwords.words("english"))

sentences = [
    "This movie is not good.",
    "This movie is really not that bad, actually.",
]

positive = {"good", "great", "excellent"}
negative = {"bad", "terrible", "awful"}
negators = {"not", "no", "never", "n't", "nor"}

def tokens(text):
    return nltk.word_tokenize(text.lower())

def remove_stopwords(toks, sw=stop_words):
    return [t for t in toks if t not in sw]

def score(toks, handle_negation=False):
    total = 0
    for i, tok in enumerate(toks):
        value = 1 if tok in positive else -1 if tok in negative else 0
        if value and handle_negation and any(w in negators for w in toks[max(0, i - 2):i]):
            value = -value
        total += value
    return total

print("WITHOUT stopword removal")
for s in sentences:
    toks = tokens(s)
    print(f"  {s}  tokens={toks}  score={score(toks)}")

print("\nWITH stopword removal (NLTK list)")
for s in sentences:
    toks = remove_stopwords(tokens(s))
    print(f"  {s}  tokens={toks}  score={score(toks)}")

fixed_stop_words = stop_words - negators
print("\nWith negators kept + negation-aware scorer")
for s in sentences:
    toks = [t for t in tokens(s) if t not in fixed_stop_words]
    print(f"  {s}  tokens={toks}  score={score(toks, handle_negation=True)}")
