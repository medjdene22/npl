import nltk
from nltk.corpus import stopwords

stop_words = set(stopwords.words("english"))

def tokenize(text):
    return nltk.word_tokenize(text.lower())

def stopword_stats(tokens, stop_words):
    remaining = [t for t in tokens if t not in stop_words]
    removed = len(tokens) - len(remaining)
    return {
        "original": len(tokens),
        "remaining": len(remaining),
        "removed": removed,
        "percent_removed": round(100 * removed / len(tokens), 1) if tokens else 0.0,
    }

text = "The student is working on a natural language processing project."
words = tokenize(text)
filtered = [w for w in words if w not in stop_words]

print("original:", words)
print("filtered:", filtered)
print()

samples = {
    "tweet": "I can't wait for this NLP lab, it is so cool!",
    "formal": "The committee has decided that the proposal will be reviewed during the next session.",
    "keywords": "NLP tokenization stopwords preprocessing pipeline",
}

print(f"{'style':10} {'original':>8} {'kept':>5} {'removed':>8} {'% removed':>10}")
for name, sentence in samples.items():
    stats = stopword_stats(tokenize(sentence), stop_words)
    print(f"{name:10} {stats['original']:>8} {stats['remaining']:>5} "
          f"{stats['removed']:>8} {stats['percent_removed']:>9}%")
