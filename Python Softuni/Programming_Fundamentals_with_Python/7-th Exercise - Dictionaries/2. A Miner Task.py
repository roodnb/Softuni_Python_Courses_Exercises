# dictionary = {}
# some_list = []
# while True:
#     command = input()
#     if command == 'stop':
#         break
#     some_list.append(command)
#
# for index in range(0, len(some_list), 2):
#     key = some_list[index]
#     value = some_list[index + 1]
#     if key not in dictionary:
#         dictionary[key] = 0
#     dictionary[key] += int(value)
#
# for key, value in dictionary.items():
#     print(f'{key} -> {value}')

# another working examples

dictionary = {}

while True:
    current_resources = input()
    if current_resources == 'stop':
        break
    resource_quantity = int(input())
    if current_resources not in dictionary.keys():
        dictionary[current_resources] = 0
    dictionary[current_resources] += resource_quantity

for key, value in dictionary.items():
    print(f'{key} -> {value}')