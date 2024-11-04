phonebook = {}

command = input()

while '-' in command:
    name, number = command.split('-')
    if name not in phonebook.keys():
        phonebook[name] = number
    phonebook[name] = number
    command = input()

for count in range(int(command)):
    current_name = input()
    if current_name in phonebook.keys():
        print(f'{current_name} -> {phonebook[current_name]}')
    else:
        print(f'Contact {current_name} does not exist.')