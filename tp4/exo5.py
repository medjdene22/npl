import re
import nltk
from nltk.corpus import stopwords

text = ("Natural Language Processing (NLP) has grown VERY fast since 2018!! "
        "Companies such as Google and OpenAI now offer APIs at "
        "https://api.example.com, and models cost around $0.002 per 1,000 tokens. "
        "Isn't that amazing?")

url_pattern = r"https?://[^\s,()]*[^\s,().]"
price_pattern = r"\$\d+(?:,\d{3})*(?:\.\d+)?"
number_pattern = r"\d+(?:,\d{3})*(?:\.\d+)?"

# Stage 1: mask the URL and the price
masked = re.sub(url_pattern, "URLTOKEN", text)
masked = re.sub(price_pattern, "PRICETOKEN", masked)
regex_view = masked.replace("URLTOKEN", "<URL>").replace("PRICETOKEN", "<PRICE>")
print("1) after RegEx:\n  ", regex_view)

# Stage 2: tokenize
tokens = nltk.word_tokenize(masked)
print("\n2) after tokenization:\n  ",
      [t.replace("URLTOKEN", "<URL>").replace("PRICETOKEN", "<PRICE>") for t in tokens])

# Stage 3: lowercase and mask numbers
normalized = []
for tok in tokens:
    low = tok.lower()
    if low == "urltoken":
        normalized.append("<URL>")
    elif low == "pricetoken":
        normalized.append("<PRICE>")
    elif re.fullmatch(number_pattern, tok):
        normalized.append("<NUM>")
    else:
        normalized.append(low)
print("\n3) after normalization:\n  ", normalized)

# Stage 4: remove stopwords, but keep negation
negators = {"not", "no", "never", "n't", "nor"}
sw = set(stopwords.words("english")) - negators
filtered = [t for t in normalized if t not in sw]
print("\n4) after stopword removal (negation kept):\n  ", filtered)

# Stage 5: token count after every stage
raw_tokens = nltk.word_tokenize(text)
stages = [
    ("raw", raw_tokens),
    ("after RegEx", nltk.word_tokenize(masked)),
    ("after tokenization", tokens),
    ("after normalization", normalized),
    ("after stopword removal", filtered),
]
print(f"\n{'stage':25}{'tokens':>7}")
for name, toks in stages:
    print(f"{name:25}{len(toks):>7}")
