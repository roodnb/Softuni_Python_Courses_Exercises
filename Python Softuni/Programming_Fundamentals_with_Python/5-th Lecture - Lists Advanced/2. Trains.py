wagons = [0] * int(input())

command = input()

while command != 'End':
    current_command = command.split(' ')
    if current_command[0] == 'add':
        wagons[-1] += int(current_command[1])
    elif current_command[0] == 'insert':
        wagons[int(current_command[1])] += int(current_command[2])
    elif current_command[0] == 'leave':
        wagons[int(current_command[1])] -= int(current_command[2])
    command = input()
print(wagons)


'''antoher example

using while true

while true
    command = input().split
    
    if command[0] =='End':
    print(wagons)
    break
    
    elif command[0] == 'add':
        wagons[-1] += int(command[1])
    elif command[0] == 'insert':
        wagons[int(command[1])] += int(command[2])
    elif command[0] == 'leave':
        wagons[int(command[1])] -= int(command[2])
         
'''