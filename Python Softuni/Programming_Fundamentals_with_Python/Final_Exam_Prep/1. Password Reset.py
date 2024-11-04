line = input()
new_pass = line
command = input()
while command != 'Done':
    command = command.split(' ')
    if command[0] == "TakeOdd":
        current_pass = ''
        for index in range(len(new_pass)):
            if index % 2 != 0:
                current_pass += new_pass[index]
        new_pass = current_pass
        print(new_pass)
    elif command[0] == 'Cut':
        start_index = int(command[1])
        length = int(command[2])
        string_to_be_removed = new_pass[start_index:start_index + length]
        new_pass = new_pass.replace(string_to_be_removed, '', 1)
        print(new_pass)
    elif command[0] == 'Substitute':
        substring = command[1]
        substitute = command[2]
        if substring in new_pass:
            new_pass = new_pass.replace(substring, substitute)
            print(new_pass)
        else:
            print('Nothing to replace!')
    command = input()
print(f'Your password is: {new_pass}')