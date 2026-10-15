import re

text = "The exam is on 16/09/2026 at 14:30."
iso_text = "The exam is on 2026-09-16"
multi_time_format = "The exam is at 14:30 and 15h45."

print(re.findall(r"\d{2}[/-]\d{2}[/-]\d{4}", text))
print(re.findall(r"\d{2}:\d{2}", text))

#iso format
print(re.findall(r"\d{4}-\d{2}-\d{2}", iso_text))

#all formats
print(re.findall(r"\d{2}[/-]\d{2}[/-]\d{4}|\d{4}-\d{2}-\d{2}", text + " " + iso_text))

#multi time format
print(re.findall(r"\d{2}:\d{2}|\d{2}h\d{2}", multi_time_format))


# Questions :
# 1-
# 2-
# 3-
