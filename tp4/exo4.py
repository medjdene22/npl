import nltk
from collections import Counter
from nltk.corpus import stopwords

stop_words = set(stopwords.words("english"))
custom_stopwords = {"the", "is", "a", "on"}

print("NLTK only:", len(stop_words - custom_stopwords))
print("in NLTK but not custom (sample):", sorted(stop_words - custom_stopwords)[:20])
print("in custom but not NLTK:", custom_stopwords - stop_words)

corpus = [
    "Natural language processing helps computers understand text.",
    "This course covers tokenization and text processing.",
    "NLP pipelines often start with normalization.",
    "Language models are trained on large text collections.",
    "Processing speech is different from processing written language.",
]

corpus_tokens = [nltk.word_tokenize(s.lower()) for s in corpus]
flat = [t for toks in corpus_tokens for t in toks if t.isalpha()]
freq = Counter(flat)
print("\nraw frequencies:", freq.most_common())

domain_stopwords = {"processing", "language", "text"}

def vocabulary(stop):
    return {t for t in flat if t not in stop}

nltk_vocab = vocabulary(stop_words)
extended_vocab = vocabulary(stop_words | domain_stopwords)
print("\nNLTK only   :", len(nltk_vocab), sorted(nltk_vocab))
print("NLTK + domain:", len(extended_vocab), sorted(extended_vocab))
print("removed by domain list:", sorted(nltk_vocab - extended_vocab))
