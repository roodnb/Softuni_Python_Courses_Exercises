# number_of_strings = int(input())
# is_pure = True
# for strings in range(number_of_strings):
#     string = input()
#     for char in string:
#         if char == '_' or char == '.' or char == ',':
#             print(f'{string} is not pure!')
#             is_pure = False
#             break
#     if is_pure:
#         print(f'{string} is pure.')
#
# The above example works but it gives only 83 % in judge. A better solution is


number_of_strings = int(input())
for strings in range(number_of_strings):
    string = input()
    if ',' in string or '.' in string or '_' in string:
        print(f'{string} is not pure!')
    else:
        print(f'{string} is pure.')
