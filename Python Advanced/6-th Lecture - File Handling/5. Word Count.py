import re
with open(".\\ex_5\\words.txt") as words:
    words = words.readline().split()

with open(".\\ex_5\\text.txt") as text:
    content = text.read()

word_count = {}

for word in words:
    pattern = rf'\\b{word}\\b'
    result = re.findall(pattern, content, re.IGNORECASE)
    word_count[word] = len(result)

sorted_word = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

with open(".\\ex_5\\output.txt", 'w') as output:
    for k,v in sorted_word:
        output.write(f'{k} - {v}\n')