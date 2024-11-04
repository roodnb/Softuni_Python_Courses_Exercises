words = input().split(', ')
words_to_look_in = input().split(', ')
new_list = []
for word in words:
    for current_word in words_to_look_in:
        if word in current_word:
            new_list.append(word)
            break

print(new_list)
