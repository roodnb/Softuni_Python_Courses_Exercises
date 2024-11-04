raw_activation_key = input()
command = input()
while command != 'Generate':
    command = command.split('>>>')
    current_command = command[0]
    if current_command == 'Contains':
        substring = command[1]
        if substring in raw_activation_key:
            print(f'{raw_activation_key} contains {substring}')
        else:
            print(f'Substring not found!')

    elif current_command == 'Flip':
        flip_type = command[1]
        start_index = int(command[2])
        end_index = int(command[3])
        substring_to_be_changed = raw_activation_key[start_index: end_index]
        if flip_type == 'Upper':
            new_string = substring_to_be_changed.upper()
            raw_activation_key = raw_activation_key[:start_index] + new_string + raw_activation_key[end_index:]
        elif flip_type == 'Lower':
            new_string = substring_to_be_changed.lower()
            raw_activation_key = raw_activation_key[:start_index] + new_string + raw_activation_key[end_index:]
        print(raw_activation_key)

    elif current_command == 'Slice':
        start_idk = int(command[1])
        end_idk = int(command[2])
        raw_activation_key = raw_activation_key[:start_idk] + raw_activation_key[end_idk:]
        print(raw_activation_key)
    command = input()

print(f'Your activation key is: {raw_activation_key}')



#another solution with functions

"""
def contains(activation_key, some_command):
    substring = some_command[1]
    if substring in activation_key:
        return f'{activation_key} contains {substring}'
    return f'Substring not found!'


def flip(activation_key, some_command):
    flip_type = some_command[1]
    start_index = int(some_command[2])
    end_index = int(some_command[3])
    before_string = activation_key[:start_index]
    after_string = activation_key[end_index:]
    if flip_type == 'Upper':
        sub_string = activation_key[start_index: end_index].upper()
        activation_key = before_string + sub_string + after_string
    elif flip_type == 'Lower':
        sub_string = activation_key[start_index: end_index].lower()
        activation_key = before_string + sub_string + after_string
    return activation_key


def sliced(activation_key, some_command):
    start_idk = int(some_command[1])
    end_idk = int(some_command[2])
    before_idk = activation_key[:start_idk]
    after_idk = activation_key[end_idk:]
    activation_key = before_idk + after_idk
    return activation_key


raw_activation_key = input()
command = input()
while command != 'Generate':
    command = command.split('>>>')
    current_command = command[0]
    if current_command == 'Contains':
        print(contains(raw_activation_key, command))
    elif current_command == 'Flip':
        raw_activation_key = flip(raw_activation_key, command)
        print(raw_activation_key)
    elif current_command == 'Slice':
        raw_activation_key = sliced(raw_activation_key, command)
        print(raw_activation_key)
    command = input()

print(f'Your activation key is: {raw_activation_key}')
"""