import re
from nltk.tokenize import word_tokenize

# Patterns from Lab 1
email_pattern = r"[\w.+-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,}"
url_pattern   = r"https?://[^\s,()]*[^\s,().]"

comment = """OMG this courseeee is SOOOO good!!! 10/10 would recommend :) Visit
https://univ.dz/nlp for more info. Contact: prof@univ.dz"""

def clean_text(text):
    text = text.lower()
    text = re.sub(r"\s+", " ", text).strip()

    text = re.sub(url_pattern, " ", text)
    text = re.sub(email_pattern, " ", text)

    text = re.sub(r"(.)\1{2,}", r"\1\1", text)
    return text

print("\ncomment:", comment)
print("\nclean_text(comment):", clean_text(comment))

orig_tokens = word_tokenize(comment)
clean_tokens = word_tokenize(clean_text(comment))

print("\ncomment tokens:", orig_tokens)
print("count:", len(orig_tokens), "| distinct:", len(set(orig_tokens)))

print("\ncleaned comment tokens:", clean_tokens)
print("count:", len(clean_tokens), "| distinct:", len(set(clean_tokens)))
