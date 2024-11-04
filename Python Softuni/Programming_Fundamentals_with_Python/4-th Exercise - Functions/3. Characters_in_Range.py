def ascii_chars(char_one: str, char_two: str) -> str:
    first_char_int = ord(char_one)
    second_char_int = ord(char_two)
    char_list = []
    for number in range(first_char_int + 1, second_char_int):
        char = chr(number)
        char_list.append(char)
    return ' '.join(char_list)
'''
the function body can be a bit tuned to look like this
char_list = []
    for number in range(ord(first_char_int) + 1, ord(second_char_int))
        char_list.append(chr(number))

'''
first_char = input()
second_char = input()
print(ascii_chars(first_char, second_char))