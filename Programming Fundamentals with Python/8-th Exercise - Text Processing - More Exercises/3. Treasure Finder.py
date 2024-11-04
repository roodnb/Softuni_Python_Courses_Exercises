def finding_treasure(middle_string):
    treasure_string = ''
    for index in range(len(middle_string)):
        if middle_string[index] == "&":
            for next_char in range(index+1, len(middle_string) + 1):
                if middle_string[next_char] == '&':
                    break
                else:
                    treasure_string += middle_string[next_char]
            return treasure_string


def find_coordinates(mid_string):
    coordinates_string = ''
    for i in range(len(mid_string)):
        if mid_string[i] == '<':
            for next_idk in range(i+1, len(mid_string) + 1):
                if mid_string[next_idk] == '>':
                    break
                else:
                    coordinates_string += mid_string[next_idk]
            return coordinates_string


key = input().split()
while True:
    middle_string = ''
    treasure = ''
    coordinates = ''
    command = input()

    if command == 'find':
        break
    some_index = 0
    for char in command:
        new_char = ord(char) - int(key[some_index])
        some_index += 1
        middle_string += chr(new_char)
        if some_index == len(key):
            some_index = 0

    treasure += finding_treasure(middle_string)
    coordinates += find_coordinates(middle_string)

    print(f'Found {treasure} at {coordinates}')



