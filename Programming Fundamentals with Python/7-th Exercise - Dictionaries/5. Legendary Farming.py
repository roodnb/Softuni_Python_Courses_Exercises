materials_quantity = {'shards': 0, 'fragments': 0, 'motes': 0}
founded = False

while True:
    command = input().split(' ')
    for index in range(0, len(command), 2):
        key = command[index + 1].lower()
        value = int(command[index])
        if key not in materials_quantity.keys():
            materials_quantity[key] = value
        else:
            materials_quantity[key] += value
        if materials_quantity['shards'] >= 250 or materials_quantity['fragments'] >= 250 or materials_quantity['motes'] >= 250:
            founded = True
            break

    if founded == True:
        break

if materials_quantity['shards'] >= 250:
    materials_quantity['shards'] -= 250
    print('Shadowmourne obtained!')
elif materials_quantity['fragments'] >= 250:
    materials_quantity['fragments'] -= 250
    print('Valanyr obtained!')
elif materials_quantity['motes'] >= 250:
    materials_quantity['motes'] -= 250
    print('Dragonwrath obtained!')

for key, value in materials_quantity.items():
    print(f'{key}: {value}')