# starting_string = input()
# starting_list = starting_string.split()
# dictionary = {}
# for char in starting_string:
#     if char == ' ':
#         continue
#     if char not in dictionary:
#         dictionary[char] = 0
#     dictionary[char] += 1
#
# for key, value in dictionary.items():
#     print(f'{key} -> {value}')

# another working examples

starting_string = [char for char in input() if char != ' ']
dictionary = {}
for char in starting_string:
    if char not in dictionary.keys():
        dictionary[char] = 0
    dictionary[char] += 1

for key, value in dictionary.items():
    print(f'{key} -> {value}')