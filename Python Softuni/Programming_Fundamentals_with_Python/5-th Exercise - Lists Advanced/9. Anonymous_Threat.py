def merge(data, start_index, end_index):
    start_index = max(0, start_index) # tuk kazwame taka
    end_index = min(len(data) - 1, end_index)
    if start_index < end_index:
        merged = ''.join(data[start_index:end_index + 1])
        data[start_index:end_index + 1] = [merged]


def divide(data, index, partitions):
    element = data[index]
    part_length = len(element) // partitions
    divided_parts = []
    start = 0
    for i in range(partitions):
        if i == partitions - 1:
            divided_parts.append(element[start:])
        else:
            divided_parts.append(element[start:start + part_length])
            start += part_length

    data[index:index + 1] = divided_parts


def process_commands(data, commands):
    for command in commands:
        parts = command.split()
        if parts[0] == 'merge':
            start_index = int(parts[1])
            end_index = int(parts[2])
            merge(data, start_index, end_index)
        elif parts[0] == 'divide':
            index = int(parts[1])
            partitions = int(parts[2])
            divide(data, index, partitions)
    return data


data = input().split()
commands = []
while True:
    command = input()
    if command == '3:1':
        break
    commands.append(command)

result = process_commands(data, commands)
print(' '.join(result))





# the below resolution gives 90/100 but not sure why
# input_line = input().split()
# command = input()
#
# while command != '3:1':
#     command = command.split()
#
#     if command[0] == 'merge':
#         start_index, end_index = int(command[1]), int(command[2])
#         if end_index <= len(input_line):
#             input_line_new = ''.join(input_line[start_index: end_index + 1])
#             input_line[start_index:end_index + 1] = [input_line_new]
#         else:
#             input_line_new = ''.join(input_line[start_index:])
#             input_line[start_index:] = [input_line_new]
#
#     if command[0] == 'divide':
#         index, partitions = int(command[1]), int(command[2])
#         element = input_line[index]
#         part_length = len(element) // partitions
#         new_element = []
#         start = 0
#         for i in range(partitions):
#             if i == int(partitions) - 1:
#                 new_element.append(element[start:])
#             else:
#                 new_element.append(element[start:start + part_length])
#                 start += part_length
#         input_line[index: index + 1] = new_element
#     command = input()
# print(' '.join(input_line))