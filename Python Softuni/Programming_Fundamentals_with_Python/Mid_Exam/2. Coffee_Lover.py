list_of_coffees = input().split()
command_count = int(input())


for command in range(command_count):
    current_command = input().split()
    action = current_command[0]
    if action == 'Include':
        list_of_coffees.append(current_command[1])
    elif action == 'Remove':
        from_where_to_start = current_command[1]
        number_of_coffees_to_remove = int(current_command[2])
        if from_where_to_start == 'first':
            list_of_coffees = list_of_coffees[number_of_coffees_to_remove:]
        else:
            removed_coffees = len(list_of_coffees) - number_of_coffees_to_remove
            list_of_coffees = list_of_coffees[:removed_coffees]
    elif action == 'Prefer':
        coffee1_idx = int(current_command[1])
        coffee2_idx = int(current_command[2])
        if coffee1_idx in range(len(list_of_coffees)) and coffee2_idx in range(len(list_of_coffees)):
            list_of_coffees[coffee1_idx], list_of_coffees[coffee2_idx] = list_of_coffees[coffee2_idx], list_of_coffees[coffee1_idx]
        else:
            continue
    elif action == 'Reverse':
        list_of_coffees = list_of_coffees[:: -1]

print(f"Coffees:\n{' '.join(list_of_coffees)}")