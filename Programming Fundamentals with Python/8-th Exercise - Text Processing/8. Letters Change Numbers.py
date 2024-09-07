import string

data = input().split()
final_number = 0
for section in data:
    first_char = section[0]
    last_char = section[-1]
    number = int(section[1:-1])
    if first_char.isupper():
        first_letter_position = ord(first_char) - 64
        final_number += number / first_letter_position
    elif first_char.islower():
        first_letter_position = ord(first_char) - 96
        final_number += number * first_letter_position
    if last_char.isupper():
        last_letter_position = ord(last_char) - 64
        final_number -= last_letter_position
    elif last_char.islower():
        last_letter_position = ord(last_char) - 96
        final_number += last_letter_position

print(f'{final_number:.2f}')
