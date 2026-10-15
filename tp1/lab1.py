import re

announcement = (
    "Reminder: the NLP project (worth 12 points) is due on 30/09/2026 before 23:59. "
    "Send your report (max 2.5 MB) to nlp.lab@univ.dz or upload it at "
    "https://courses.univ.dz/submit. Late submissions lose -1.5 points per day. "
    "Contact +213 555 98 76 54 for questions."
)

date_pattern = r"\d{2}[/-]\d{2}[/-]\d{4}|\d{4}-\d{2}-\d{2}"
time_pattern = r"\d{2}:\d{2}|\d{2}h\d{2}"
email_pattern = r"[\w.+-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,}"
url_pattern = r"https?://[^\s,()]*[^\s,().]"
phone_pattern = r"(?:\+213\s?|0)\d{3}(?:\s?\d{2}){3}"
number_pattern = r"-?\d+\.?\d*"

report = {
    "dates": re.findall(date_pattern, announcement),
    "times": re.findall(time_pattern, announcement),
    "emails": re.findall(email_pattern, announcement),
    "urls": re.findall(url_pattern, announcement),
    "phones": re.findall(phone_pattern, announcement),
    "numbers": re.findall(number_pattern, announcement),
}

print("Information extraction report")
for name, values in report.items():
    print(f"{name}: {values}")

# Discussion
# Easiest: emails. @ and a domain match nothing else in the text.
# Hardest: numbers. The same pattern also matches the digits inside the date,
# the time and the phone, and the optional dot sticks to the period after 23:59.
