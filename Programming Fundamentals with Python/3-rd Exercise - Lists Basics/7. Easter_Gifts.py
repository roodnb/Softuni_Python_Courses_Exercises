gifts = input().split()
command = input()

while command != 'No Money':
    new_command = command.split()
    if 'OutOfStock' in new_command and new_command[1] in gifts:
        while new_command[1] in gifts:
            index = gifts.index(new_command[1])
            gifts[index] = 'None'
    if 'Required' in new_command:
        if 0 <= int(new_command[2]) < len(gifts):
            gifts[int(new_command[2])] = new_command[1]
    if 'JustInCase' in new_command:
        gifts[-1] = new_command[1]
    command = input()
while 'None' in gifts:
    gifts.remove('None')
print(' '.join(gifts))