original_string = [index for index in input()]
numbers_list = []
non_numbers_list = []

for i in original_string:
    try:
        int(i)
        numbers_list.append(int(i))
    except:
        non_numbers_list.append(i)

take_list = []
skip_list = []
for index in range(len(numbers_list)):
    if index % 2 == 0:
        take_list.append(numbers_list[index])
    else:
        skip_list.append(numbers_list[index])

result_string = []
starting_skip_index = 0
taken_list = []
final_list = []
for current_take_index in take_list:
    how_much_to_skip = skip_list[starting_skip_index]
    if current_take_index == 0:
        result_string += non_numbers_list[how_much_to_skip:]
        non_numbers_list = result_string
    elif current_take_index > 0:
        taken_list = result_string[:current_take_index]
        result_string = result_string[current_take_index + 1:]
    starting_skip_index += 1
    final_list += taken_list

print(''.join(final_list))

