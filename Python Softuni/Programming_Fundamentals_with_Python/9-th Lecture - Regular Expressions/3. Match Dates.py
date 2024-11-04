import re
text = input()
pattern = r'(\d{2})([-.\/])([A-Z][a-z]{2})\2(\d{4})'
match = re.finditer(pattern, text)

for each in match:
    print(f'Day: {each.group(1)}, Month: {each.group(3)}, Year: {each.group(4)}')