import re

text = "The course has 20 hours and 12 exercises."
result = re.sub(r"\d+", "<NUMBER>", text)
print(result)


comment = ("Contact me at ali.ben@example.com or call 0555123456 "
           "if you have questions about the 20-hour course. — Ali, 16/09/2026.")

result = re.sub(r"\d+", "<NUMBER>", comment)
print(result)

def anonymize(text):
    text = re.sub(r"[\w.+-]+@[\w-]+\.[\w.]+", "[EMAIL]", text)
    text = re.sub(r"(?:\+213\s?|0)\d{3}(?:\s?\d{2}){3}", "[PHONE]", text)
    text = re.sub(r"\b\d{2}/\d{2}/\d{4}\b", "[DATE]", text)
    return text

print(anonymize(comment))
