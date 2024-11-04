from collections import deque

starting_water = int(input())
names = deque()

while True:
    command = input()
    if command == 'Start':
        break
    names.append(command)

second_command = input()
while second_command != 'End':
    if 'refill' in second_command:
        second_command = second_command.split(' ')
        starting_water += int(second_command[1])
    else:
        liters = int(second_command)
        if starting_water >= liters:
            starting_water -= liters
            print(f'{names.popleft()} got water')
        else:
            print(f'{names.popleft()} must wait')
    second_command = input()

print(f'{starting_water} liters left')