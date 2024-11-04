animal_dict = {}

while True:
    command = input().split(' ')

    if command[0] == 'EndDay':
        break

    action = command[0]
    new_command = command[1].split('-')
    animal_name = new_command[0]

    if action == 'Add:':
        needed_food_quantity = int(new_command[1])
        area = new_command[2]
        if animal_name not in animal_dict:
            animal_dict[animal_name] = {'needed_food_quantity': needed_food_quantity, 'area': area}
        else:
            animal_dict[animal_name]['needed_food_quantity'] += needed_food_quantity

    elif action == 'Feed:':
        food = int(new_command[1])
        if animal_name not in animal_dict:
            continue
        else:
            if animal_dict[animal_name]['needed_food_quantity'] - food <= 0:
                del animal_dict[animal_name]
                print(f"{animal_name} was successfully fed")
            else:
                animal_dict[animal_name]['needed_food_quantity'] -= food

print('Animals:')
for animal, needed_food in animal_dict.items():
    print(f" {animal} -> {needed_food['needed_food_quantity']}g")

area_hungry_animals = {}
for key, value in animal_dict.items():
    for k, v in value.items():
        if k == 'area':
            if v not in area_hungry_animals:
                area_hungry_animals[v] = 1
            else:
                area_hungry_animals[v] += 1
print("Areas with hungry animals:")
for area, count in area_hungry_animals.items():
    print(f" {area}: {count}")