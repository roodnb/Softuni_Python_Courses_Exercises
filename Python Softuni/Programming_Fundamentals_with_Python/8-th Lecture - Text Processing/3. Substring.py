word = input()
current_string = input()

while word in current_string:
    current_string = current_string.replace(word, '')

print(current_string)