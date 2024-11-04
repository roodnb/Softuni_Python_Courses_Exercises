import re

text = input()
pattern = r'\s((([a-z0-9]+)[\w+\.\-]*)@([\w+\-]+)(\.[a-z]+)+)\b'
matches = re.finditer(pattern, text)

for group in matches:
    print(group.groups(1)[0])

#another option
# matches = re.findall(pattern, text)
# for group in matches:
#     print(group[0])