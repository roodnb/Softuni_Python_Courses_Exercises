key = int(input())
number_of_letters = int(input())

for char in range(number_of_letters):
    character = input()
    new_char = ord(character) + key
    print(chr(new_char), end='')