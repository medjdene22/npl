from nltk.tokenize import TreebankWordTokenizer, WordPunctTokenizer, word_tokenize

# 1. word_tokenize()
text = "I don't know. It's useful, isn't it?"
print("1) word_tokenize(text):", word_tokenize(text))

# 2+3. TreebankWordTokenizer and WordPunctTokenizer
expressions = ["don't", "isn't", "New York", "state-of-the-art", "twenty-one"]
tb = TreebankWordTokenizer()
wp = WordPunctTokenizer()

print("\n2+3) TreebankWordTokenizer and WordPunctTokenizer:")
for e in expressions:
    print(e, "|", word_tokenize(e), "|", tb.tokenize(e), "|", wp.tokenize(e))
