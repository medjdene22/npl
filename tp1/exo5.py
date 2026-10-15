import re

text = "Contact ali@example.com or student.name@univ.dz."
pattern = r"[\w.-]+@[\w.-]+\.\w+"
print(re.findall(pattern, text))

def is_valid_email(address):
    return PATTERN.fullmatch(address) is not None

mailing_list = [
    'ali@example.com', 'student.name@univ.dz', 'a.b-c@sub.univ.dz',
    'not-an-email', 'missing@domain', 'double@@example.com',
    '@no-local-part.com', 'ok.name+lab@example.co.uk',
]

PATTERN = re.compile(r"[\w.+-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,}")

valid   = [a for a in mailing_list if is_valid_email(a)]
invalid = [a for a in mailing_list if not is_valid_email(a)]

print(f"Valid:   {len(valid)}  -> {valid}")
print(f"Invalid: {len(invalid)}  -> {invalid}")


#Question
# still fails admin@localhost or user@mailserver or IP literal domains
