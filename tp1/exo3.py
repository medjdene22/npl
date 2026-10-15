import re

text = "The course has 20 hours, 3 labs and 12 exercises."
receipt = "2 apples, 1.5 kg of rice, 3 juices at $2.50 each, total: $12.75 (-$1.00 discount)."

print(re.findall(r"\d+", text))

print(re.findall(r"\d+\.?\d*", receipt))

print(re.findall(r"-?\$?\d+\.?\d*", receipt))

amounts = [float(a.replace("$", "")) for a in re.findall(r"-?\$\d+\.?\d*", receipt)]
print(amounts)
print(sum(amounts))

#challenge
money = re.findall(r"-?\$\d+\.?\d*", receipt)
rest = re.sub(r"-?\$\d+\.?\d*", "", receipt)
quantities = re.findall(r"\d+\.?\d*", rest)

print("Quantities:", quantities)
print("Money:", money)


# Questions :
# 1- \d matches one digit. + means "one or more"
# 2- The dot isn't a digit, so \d+ stops at it.
# 3- The minus needs no escaping when written as -?.
