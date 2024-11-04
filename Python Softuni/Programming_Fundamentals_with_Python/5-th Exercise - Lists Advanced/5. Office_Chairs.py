number_of_rooms = int(input())
free_chair_count = 0
flag = False

for room in range(1, number_of_rooms + 1):
    command = input().split()
    chairs = command[0]
    people = int(command[1])
    # gornite 3 reda mogat da bydat napisani i taka : chairs, people = input().split()
    difference = abs(people - len(chairs))
    if len(chairs) < people:
        print(f"{difference} more chairs needed in room {room}")
        flag = True
    else:
        free_chair_count += difference

if not flag == True:
    print(f'Game On, {free_chair_count} free chairs left')