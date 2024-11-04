import re
names = input()
regex = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"
match = re.findall(regex, names)

print(' '.join(match))