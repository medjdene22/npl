import re

text = "NLP is useful. NLP is interesting. Machine learning is useful."
text2 = "NLP is useful. nlpP is interesting. Machine learning is useful., NLPS are good"
print(re.findall(r"NLP", text))
print(re.findall(r"useful", text))

print(re.findall(r"\bNLP\b", text2, 2))


def count_occurrences(pattern, text, case_sensitive=True):
    flags = 0 if case_sensitive else re.IGNORECASE
    return len(re.findall(pattern, text, flags=flags))

print(count_occurrences(r"useful|interesting", text))

print(count_occurrences(r"NLP", text2, False  ))


#chalange
#
sentences = text.split(". ")
hits = [s for s in sentences if re.search(r"\b(NLP|machine learning)\b", s, re.IGNORECASE)]

print(f"{100 * len(hits) / len(sentences):.0f}%")   # 100%
