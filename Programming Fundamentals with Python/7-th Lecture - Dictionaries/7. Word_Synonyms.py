word_count = int(input())
word_synonyms = {}
for count in range(word_count):
    word = input()
    synonym = input()
    if word not in word_synonyms:
        word_synonyms[word] = []
    word_synonyms[word].append(synonym)

for key, value in word_synonyms.items():
    print(f"{key} - {', '.join(value)}")