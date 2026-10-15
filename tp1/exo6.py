import http
import re

text = "Visit https://www.univ.dz or http://example.org."
naive = r"https?://[^\s]+"
print(re.findall(naive, text))


text = ("See https://www.univ.dz/lab1?page=2,http://example.org, "
        "https://docs.python.org/3/library/re.html and "
        "ftp://old-server.com(not a web link).")

print(f"naive: {re.findall(naive, text)}")

fixed = r"https?://[^\s,()]*[^\s,().]"
print(f"fixed: {re.findall(fixed, text)}")

domain = r"https?://([^/\s,()]+)"
print(f"domain: {re.findall(domain, text)}")


pattern_ftp = r"(?:https?|ftp)://[^\s,()]*[^\s,().]"
print(re.findall(pattern_ftp, text))

https_urls = re.findall(r"https://[^\s,()]*[^\s,().]", text)
http_urls = re.findall(r"http://[^\s,()]*[^\s,().]", text)
print(len(https_urls))
print(len(http_urls))
