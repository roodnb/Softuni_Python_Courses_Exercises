concealed_message = input()

command = input().split(':|:')

while command[0] != 'Reveal':
    if command[0] == 'InsertSpace':
        space_index = int(command[1])
        concealed_message = concealed_message[:space_index] + ' ' + concealed_message[space_index:]
    elif command[0] == 'Reverse':
        if command[1] in concealed_message:
            string = command[1]
            new_string = string[::-1]
            concealed_message = concealed_message.replace(command[1], new_string, 1)
        else:
            print('error')
            command = input().split(':|:')
            continue
    elif command[0] == 'ChangeAll':
        substring = command[1]
        replacement_string = command[2]
        concealed_message = concealed_message.replace(substring, replacement_string)
    print(concealed_message)
    command = input().split(':|:')

print(f'You have a new text message: {concealed_message}')