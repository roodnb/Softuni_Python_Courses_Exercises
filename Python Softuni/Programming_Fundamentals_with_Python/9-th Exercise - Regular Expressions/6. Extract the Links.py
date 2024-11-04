import re

line = input()
pattern = r'(?i)(www\.([A-Za-z0-9\-]+)(\.[a-z]+)+)' # another way (www\.([A-Za-z0-9\-]+)(\.[a-z]+)+)
while line:
    matches = re.finditer(pattern, line)
    if matches:
        for match in matches:
            print(match.group(1))
    line = input()
