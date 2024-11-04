command = input()
star_wars = {}

while command != 'Lumpawaroo':
    if '|' in command:
        force_side, force_user = command.split(' | ')
        force_user_is_part_of_the_force = False
        if force_side not in star_wars.keys():
            star_wars[force_side] = []
        for list_of_force_users in star_wars.values():
            if force_user in list_of_force_users:
                force_user_is_part_of_the_force = True
                break
        if not force_user_is_part_of_the_force:
            star_wars[force_side].append(force_user)

    elif '->' in command:
        force_user, force_side = command.split(" -> ")
        if force_side not in star_wars.keys():
            star_wars[force_side] = []
        for list_of_force_users in star_wars.values():
            if force_user in list_of_force_users:
                list_of_force_users.remove(force_user)
                break
        star_wars[force_side].append(force_user)
        print(f"{force_user} joins the {force_side} side!")
    command = input()


for key,value in star_wars.items():
    if len(value) > 0:
        print(f'Side: {key}, Members: {len(value)}')
    for force_user in value:
        print(f'! {force_user}')