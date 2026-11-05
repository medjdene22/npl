import re

text = "The course lasts 20 hours and contains 12 exercises."
print(re.sub(r"\d+", "<NUM>", text))

invoice = "The invoice #4521 totals $1,250.00, due in 30 days."
print(re.sub(r"\d+", "<NUM>", invoice))

pattern = r"\d+(?:,\d{3})*(?:\.\d+)?"
print(re.sub(pattern, "<NUM>", invoice))

def normalize_num(text):
    return re.sub(pattern, "<NUM>", text)

def normalize_num_magnitude(text):
    def repl(m):
        value = float(m.group().replace(",", ""))
        return "<NUM_SMALL>" if value < 100 else "<NUM_LARGE>"
    return re.sub(pattern, repl, text)

print(normalize_num(invoice))
print(normalize_num_magnitude(invoice))
