import nltk
from nltk.corpus import stopwords

stop_words = set(stopwords.words("english"))

text = "The student is working on a natural language processing project."
words = nltk.word_tokenize(text.lower())

print("stopwords found:", [word for word in words if word in stop_words])
print("content words:  ", [word for word in words if word not in stop_words])
print()
print("natural / language / processing:",
      {word: word in stop_words for word in ["natural", "language", "processing"]})
print()
print("first 15 stopwords:", stopwords.words("english")[:15])
