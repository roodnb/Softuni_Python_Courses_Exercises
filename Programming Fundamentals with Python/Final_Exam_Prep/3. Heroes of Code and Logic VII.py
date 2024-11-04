def cast(some_command, data):
    name = some_command[1]
    mp_needed = int(some_command[2])
    spell_name = some_command[3]
    if data[name]['mana_points'] >= mp_needed:
        data[name]['mana_points'] -= mp_needed
        print(f"{name} has successfully cast {spell_name} and now has {data[name]['mana_points']} MP!")
    else:
        print(f"{name} does not have enough MP to cast {spell_name}!")
    return data


def take(some_command, data):
    name = some_command[1]
    damage = int(some_command[2])
    attacker = some_command[3]
    data[name]['hit_points'] -= damage
    if data[name]['hit_points'] <= 0:
        print(f'{name} has been killed by {attacker}!')
        del data[name]
    else:
        print(f"{name} was hit for {damage} HP by {attacker} and now has {data[name]['hit_points']} HP left!")
    return data


def recharge(some_command, data):
    name = some_command[1]
    amount = int(some_command[2])
    recharged_amount = 0
    if data[name]['mana_points'] + amount > 200:
        recharged_amount += 200 - data[name]['mana_points']
        data[name]['mana_points'] = 200
    else:
        recharged_amount += amount
        data[name]['mana_points'] += amount
    print(f'{name} recharged for {recharged_amount} MP!')
    return data


def heal(some_command, data):
    name = some_command[1]
    amount = int(some_command[2])
    recharged_amount = 0
    if data[name]['hit_points'] + amount > 100:
        recharged_amount += 100 - data[name]['hit_points']
        data[name]['hit_points'] = 100
    else:
        recharged_amount += amount
        data[name]['hit_points'] += amount
    print(f'{name} healed for {recharged_amount} HP!')
    return data


heroes_num = int(input())
heroes_data = {}

for hero in range(heroes_num):
    hero_name, health, mana = input().split(' ')
    heroes_data[hero_name] = {'hit_points': int(health), 'mana_points': int(mana)}

while True:
    command = input().split(' - ')
    if command[0] == 'End':
        break
    action = command[0]
    if command[0] == 'CastSpell':
        heroes_data = cast(command, heroes_data)
    elif command[0] == 'TakeDamage':
        heroes_data = take(command, heroes_data)
    elif command[0] == 'Recharge':
        heroes_data = recharge(command, heroes_data)
    elif command[0] == 'Heal':
        heroes_data = heal(command, heroes_data)


for key, value in heroes_data.items():
    print(f"{key}\n"
          f"  HP: {value['hit_points']}\n"
          f"  MP: {value['mana_points']}")