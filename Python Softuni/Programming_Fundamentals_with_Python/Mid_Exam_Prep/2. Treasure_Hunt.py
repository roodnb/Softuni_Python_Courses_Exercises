
###### The below works fine but judge gives 80/100
def loot(_initial_loot, new_treasure):
    for current_loot in new_treasure:
        if current_loot not in _initial_loot:
            _initial_loot.insert(0, current_loot)
    return _initial_loot


def drop(_initial_loot, what_to_drop):
    if what_to_drop in range(len(_initial_loot)):
        _initial_loot.append(_initial_loot.pop(what_to_drop))
    return _initial_loot


def steal(_initial_loot, how_much_to_steal):
    if how_much_to_steal >= len(_initial_loot):
        print(', '.join(_initial_loot))
        return []
    stolen_items = len(_initial_loot) - how_much_to_steal
    print(', '.join(_initial_loot[stolen_items:]))
    _initial_loot = _initial_loot[:stolen_items]
    return _initial_loot


def process_command(_initial_loot, _commands):
    for one_command in commands:
        command_parts = one_command.split()
        actual_command = command_parts[0]
        if actual_command == 'Loot':
            new_treasure = command_parts[1:]
            _initial_loot = loot(initial_loot, new_treasure)
        elif actual_command == 'Drop':
            what_to_drop = int(command_parts[1])
            _initial_loot = drop(initial_loot, what_to_drop)
        elif actual_command == 'Steal':
            how_much_to_steal = int(command_parts[1])
            _initial_loot = steal(_initial_loot, how_much_to_steal)
    return _initial_loot


initial_loot = input().split('|')
commands = []
while True:
    command = input()
    if command == 'Yohoho!':
        break
    commands.append(command)

initial_loot = process_command(initial_loot, commands)
if not initial_loot:
    print('Failed treasure hunt.')
else:
    average = sum(len(item) for item in initial_loot) / len(initial_loot)
    print(f'Average treasure gain: {average:.2f} pirate credits.')

#### The below judge gives 100/100

# def loot(_initial_loot, new_treasure):
#     for current_loot in new_treasure:
#         if current_loot not in _initial_loot:
#             _initial_loot.insert(0, current_loot)
#     return _initial_loot
#
#
# def drop(_initial_loot, what_to_drop):
#     if what_to_drop in range(len(_initial_loot)):
#         _initial_loot.append(_initial_loot.pop(what_to_drop))
#     return _initial_loot
#
#
# def steal(_initial_loot, how_much_to_steal):
#     if how_much_to_steal >= len(_initial_loot):
#         print(', '.join(_initial_loot))
#         return []
#     stolen_items = len(_initial_loot) - how_much_to_steal
#     print(', '.join(_initial_loot[stolen_items:]))
#     _initial_loot = _initial_loot[:stolen_items]
#     return _initial_loot
#
#
# initial_loot = input().split('|')
# command = input().split()
# while command[0] != "Yohoho!":
#     action = command[0]
#     if action == "Loot":
#         initial_loot = loot(initial_loot, command[1:])
#     elif action == "Drop":
#         index = int(command[1])
#         initial_loot = drop(initial_loot, index)
#     elif action == "Steal":  # else
#         count = int(command[1])
#         initial_loot = steal(initial_loot, count)
#     command = input().split()
#
# if not initial_loot:
#     print('Failed treasure hunt.')
# else:
#     average = sum(len(item) for item in initial_loot) / len(initial_loot)
#     print(f'Average treasure gain: {average:.2f} pirate credits.')

