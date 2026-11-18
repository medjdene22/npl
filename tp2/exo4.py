from nltk.tokenize import sent_tokenize

text = "NLP is useful. Students can practise it. The exercises are interesting."
sentences = sent_tokenize(text)
print(" 1) Sentences:", sentences, "length:", len(sentences))

text2 = "Is NLP hard? Not really! It just takes practice."
sentences2 = sent_tokenize(text2)
print(" 2) Sentences:", sentences2, "length:", len(sentences2))

text3 = "Dr. Smith arrived at 9 a.m. He gave a talk on NLP. It lasted 1.5 hrs."
sentences3 = sent_tokenize(text3)
print(" 3) Sentences:", sentences3, "length:", len(sentences3))


print(" 4) keep a list of known abbreviations (e.g. a.m., Dr., ...) dont split when the sentence when it ends with a period that belongs to an abbreviation")
