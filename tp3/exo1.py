import re

text = "NLP Is Used In Many Applications."
print(text.lower())

text2 = "Apple released a new iPhone; the apple I ate was sweet."
print(text2.lower())

print("\n3) In Named Entity Recognition Capitalization is one of the strongest clues, US vs us, Turkey vs turkey, and Bush vs bush")

def smart_lower(text):
    def fix(match: re.Match):
        w = match.group()
        if w.isupper() and 2 <= len(w) <= 5:
            return w
        return w.lower()
    return re.sub(r"\w+", fix, text)

print(smart_lower("\n4) The NLP course covers USA-based case studies."))
print(smart_lower("WE ARE FINE"))
