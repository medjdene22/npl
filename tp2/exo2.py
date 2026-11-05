from nltk.tokenize import word_tokenize

text = "Natural language processing is interesting."
tokens = word_tokenize(text)

print("1) tokens:", tokens, "lenth:", len(tokens))


def naive_tokenize(text):
    return text.split()

naive_tokens = naive_tokenize(text)

print("2) naive tokens:", naive_tokens, "lenth:", len(naive_tokens))


hard_text = "Well, that's... surprising (and a bit odd)!"
naive_hard = naive_tokenize(hard_text)
nltk_hard = word_tokenize(hard_text)

print("3) Harder sentence:", hard_text)
print("   naive tokens:", naive_hard)
print("   nltk tokens:", nltk_hard)

only_naive = [token for token in naive_hard if token not in nltk_hard]
only_nltk = [token for token in nltk_hard if token not in naive_hard]

print("   Tokens only in naive output: ", only_naive)
print("   Tokens only in NLTK output:  ", only_nltk)


print("4) Comparison table:")

punct = [".", ",", "!", "?", "(", ")", "..."]
sentences = [text, hard_text]

for sentence in sentences:
    for name, tokens in [("naive", naive_tokenize(sentence)), ("nltk", word_tokenize(sentence))]:
        print(name, "|", len(tokens), "|", "yes" if any(token in punct for token in tokens) else "no")
