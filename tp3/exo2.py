import re

text = "NLP   is \n\n very    useful."
result = re.sub(r"\s+", " ", text).strip()
print(result)

messy = "NLP\tis\n\nvery\u00a0\u00a0useful."
print(re.sub(r"\s+", " ", messy).strip())

def normalize_whitespace(text):
    text = text.replace("\u00a0", " ")

    lines = [line.strip() for line in text.splitlines()]
    cleaned = " ".join(line for line in lines if line)

    return re.sub(r"\s+", " ", cleaned).strip()

para = """   Natural language   processing
        is a field of AI \t
   that studies\u00a0human language.   """

print(normalize_whitespace(para))
