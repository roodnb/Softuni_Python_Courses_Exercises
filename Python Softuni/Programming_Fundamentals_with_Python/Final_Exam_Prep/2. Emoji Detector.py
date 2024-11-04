import re

line = input()
cool_pattern = r'\d'
cool_matches = re.findall(cool_pattern, line)

cool_threshold = 1
for m in cool_matches:
    cool_threshold *= int(m)

emoji_pattern = r'(::|\*\*)([A-Z][a-z]{2,})\1'
matches = re.findall(emoji_pattern, line)
some_list = []
for match in matches:
    cool_factor = 0
    surrounding = match[0]
    emoji = match[1]
    for index in emoji:
        cool_factor += ord(index)
    if cool_factor > cool_threshold:
        some_list.append(f'{surrounding}{emoji}{surrounding}')


print(f'Cool threshold: {cool_threshold}')
print(f"{len(matches)} emojis found in the text. The cool ones are:")
print(' \n'.join(some_list))