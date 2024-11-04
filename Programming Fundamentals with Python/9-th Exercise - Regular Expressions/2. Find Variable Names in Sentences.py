import re

text = input()
pattern = r'\b_([A-Za-z0-9]+)\b'
variables = re.finditer(pattern, text)
for match in variables:
    print(match.group(1), end=' ')