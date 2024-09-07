initial_energy = int(input())

won_battle_count = 0
command = input()
while command != 'End of battle':
    distance = int(command)
    if initial_energy < distance:
        print(f"Not enough energy! Game ends with {won_battle_count} won battles and {initial_energy} energy")
        break
    else:
        won_battle_count += 1
        if won_battle_count % 3 == 0:
            initial_energy += won_battle_count
    initial_energy -= distance
    command = input()

if command == 'End of battle':
    print(f'Won battles: {won_battle_count}. Energy left: {initial_energy}')

