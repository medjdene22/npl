import re

text = "cat bat rat dog hot"

print(re.findall(r"\b\w+at\b", text))

print(re.findall(r"[bcdfghjklmnpqrstvwxyz]{3}", text))

usernames = ['ali_92', 'A', 'student.name', 'nlp_lab_2026']
pattern = r"^[a-z0-9_]{4,12}$"


for username in usernames:
    if re.match(pattern, username):
        print(f"{username} is valid")
    else:
        print(f"{username} is invalid")
