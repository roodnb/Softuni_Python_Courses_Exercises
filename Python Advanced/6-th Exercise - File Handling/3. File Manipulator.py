import os

while True:
    command = input().split('-')
    current_command = command[0]

    if current_command == 'End':
        break

    current_file = command[1]
    if current_command == 'Create':
        open(f'.\\ex_3\\{current_file}', 'w').close()

    elif current_command == "Add":
        what_to_add = command[2]
        with open(f'.\\ex_3\\{current_file}', 'a') as file:
            file.write(f'{what_to_add}\n')

    elif current_command == "Replace":
        old_str = command[2]
        new_str = command[3]
        try:
            with open(f'.\\ex_3\\{current_file}', 'r+') as file:
                content = file.read()
                file.seek(0)
                file.truncate(0)
                file.write(content.replace(old_str, new_str))
        except FileNotFoundError:
            print("An error occurred")
    elif current_command == "Delete":
        if os.path.exists(f'.\\ex_3\\{current_file}'):
            os.remove(f'.\\ex_3\\{current_file}')
        else:
            print("An error occurred")