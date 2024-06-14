import re
level_of_fire_and_cell_value = input()
new_list_with_single_indexing = re.split('[# ]', level_of_fire_and_cell_value)
water = int(input())
actual_list = []
small_list = []
for index in new_list_with_single_indexing:
    for revolution in range(1):
        small_list.append(index)
        if len(small_list) == 3:
            actual_list.append(small_list)
            small_list = []
            break
effort = 0
total_fire = 0
print(f'Cells: ')
for index_lst in actual_list:
    if water <= 0:
        break
    current_cell_value = int(index_lst[2])
    if 'High' in index_lst and 81 <= current_cell_value <= 125:
        if current_cell_value > water:
            continue
        water -= int(index_lst[2])
        effort += current_cell_value * 0.25
        total_fire += current_cell_value
        print(f' - {current_cell_value}')
    if 'Medium' in index_lst and 51 <= current_cell_value <= 80:
        if current_cell_value > water:
            continue
        water -= int(index_lst[2])
        effort += current_cell_value * 0.25
        total_fire += current_cell_value
        print(f' - {current_cell_value}')
    if 'Low' in index_lst and 1 <= current_cell_value <= 50:
        if current_cell_value > water:
            continue
        water -= int(index_lst[2])
        effort += current_cell_value * 0.25
        total_fire += current_cell_value
        print(f' - {current_cell_value}')
print(f'Effort: {effort:.2f}')
print(f'Total Fire: {total_fire}')


'''
another better solution

fires = input().split("#")
water = int(input())

effort = 0
total_fire = 0
put_out_cells = []

print("Cells:")

for fire in fires:
    args = fire.split(" = ")
    fire_type = args[0]
    level = int(args[1])
    valid = False
    if water < level:
        continue
    if fire_type == 'High':
        if 81 <= level <= 125:
            valid = True
    elif fire_type == 'Medium':
        if 51 <= level <= 80:
            valid = True
    elif fire_type == 'Low':
        if 1 <= level <= 50:
            valid = True
    if valid:
        put_out_cells.append(level)
        water -= level
        effort += level * 0.25
        total_fire += level

for cell in put_out_cells:
    print(f' - {cell}')

print(f'Effort: {effort:.2f}')
print(f'Total Fire: {total_fire}')

'''