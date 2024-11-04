import re


def get_the_key(message):
    pattern1 = r'(?i)([star])'
    matches = re.findall(pattern1, message)
    return len(matches)


def get_the_data(message):
    planet = ''
    popul = ''
    a_type = ''
    s_count = ''
    pattern2 = r'@([A-Za-z]+)([^@:!\->]*)(:(\d+))([^@:!\->]*)(!(A|D)!)([^@:!\->]*)(->(\d+))'
    matches = re.finditer(pattern2, message)
    for match in matches:
        planet = match.group(1)
        popul = match.group(4)
        a_type = match.group(7)
        s_count = match.group(10)
    return planet, popul, a_type, s_count


number_of_messages = int(input())
star_wars_dict = {}
for num in range(1, number_of_messages+1):
    encrypted_message = input()
    key = get_the_key(encrypted_message)
    decrypted_message = ''
    for letter in encrypted_message:
        decrypted_message += chr(ord(letter) - key)

    data = get_the_data(decrypted_message)
    planet_name = data[0]
    population = data[1]
    attack_type = data[2]
    solder_count = data[3]

    if planet_name and population and attack_type and solder_count != 'None':
        if planet_name not in star_wars_dict.keys():
            star_wars_dict[planet_name] = attack_type


ordered_dict = dict(sorted(star_wars_dict.items(), key=lambda x: (x[1], x[0])))
attacked_planets_sum = 0
destroyed_planets_sum = 0
for k, v in ordered_dict.items():
    if v == 'A':
        attacked_planets_sum += 1
    else:
        destroyed_planets_sum += 1

print(f'Attacked planets: {attacked_planets_sum}')
for key, value in ordered_dict.items():
    if value == 'A':
        print(f'-> {key}')

print(f'Destroyed planets: {destroyed_planets_sum}')
for key, value in ordered_dict.items():
    if value == 'D':
        print(f'-> {key}')
