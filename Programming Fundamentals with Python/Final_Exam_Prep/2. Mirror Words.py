import re

text_string = input()
hidden_words_patter = r'([@|#])([a-zA-Z]{3,})\1{2}([a-zA-Z]{3,})\1'

matches = re.findall(hidden_words_patter, text_string)
mirrored_words = []

for match in matches:
    if match[1] == match[2][::-1]:
        mirrored_words.append(f'{match[1]} <=> {match[2]}')

if not matches:
    print("No word pairs found!")
else:
    print(f"{len(matches)} word pairs found!")

if not mirrored_words:
    print("No mirror words!")
else:
    print('The mirror words are:')
    print(', '.join(mirrored_words))