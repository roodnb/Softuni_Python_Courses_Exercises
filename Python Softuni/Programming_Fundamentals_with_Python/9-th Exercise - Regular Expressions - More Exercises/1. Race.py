import re


def separate_num(line):
    current_sum = 0
    pattern_n = r'([0-9])'
    numbers = re.findall(pattern_n, line)
    for num in numbers:
        current_sum += int(num)
    return current_sum


def separate_alpha(line):
    current_name = ''
    pattern_a = r'([a-zA-Z]+)'
    letters = re.findall(pattern_a, line)
    for letter in letters:
        current_name += letter
    return current_name


participants = input().split(', ')
participants_dict = {}

while True:
    info = input()
    if info == 'end of race':
        break

    player_sum = separate_num(info)
    player_name = separate_alpha(info)
    if player_name in participants:
        if player_name not in participants_dict.keys():
            participants_dict[player_name] = player_sum
        else:
            participants_dict[player_name] += player_sum


ordered_dict = dict(sorted(participants_dict.items(), key=lambda x: x[1], reverse=True))
count = 0
for name in ordered_dict.keys():
    count += 1
    if count == 1:
        print(f'{count}st place: {name}')
    elif count == 2:
        print(f'{count}nd place: {name}')
    elif count == 3:
        print(f'{count}rd place: {name}')
    else:
        break