command = input()
final_string = ''
strength = 0
for i in range(len(command)):
    if command[i] == '>':
        final_string += '>'
        strength += int(command[i+1])
    elif strength > 0 and command[i] != '>':
        strength -= 1
    elif command[i] != '>':
        final_string += command[i]

print(final_string)


