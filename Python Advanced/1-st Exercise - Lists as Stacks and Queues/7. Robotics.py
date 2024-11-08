from collections import deque

robot_time = deque([i.split('-') for i in input().split(';')])
cpy_robot_time = robot_time.copy()
hours, minutes, seconds = [int(i) for i in input().split(':')]
product_line = deque()

while True:
    command = input()
    if command == 'End':
        break
    product_line.append(command)

count = 0
while product_line:
    seconds = seconds + 1
    if seconds >= 60:
        seconds -= 60
        minutes += 1
    if minutes >= 60:
        minutes -= 60
        hours += 1
    if hours >= 24:
        hours -= 24
    if not cpy_robot_time:
        for index in robot_time:
            if seconds % int(index[1]) == 0 and int(index[1]) <= seconds:
                cpy_robot_time.append(index)

    if cpy_robot_time:
        name = cpy_robot_time[0][0]
        print(f"{name} - {product_line.popleft()} [{hours:02d}:{minutes:02d}:{seconds:02d}]")
        cpy_robot_time.popleft()
    else:
        product_line.rotate(-1)