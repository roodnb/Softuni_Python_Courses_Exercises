from collections import deque
robots_list = list(input().split(";"))

free_robots_dict = {}
working_robots_dict = {}
product_deque = deque()

for robs in robots_list:
    robot_data = robs.split("-")
    working_robots_dict[robot_data[0]] = int(robot_data[1])
    free_robots_dict[robot_data[0]] = -1

hours, minutes, seconds = [int(i) for i in input().split(':')]

while True:
    product = input()
    if product == "End":
        break
    product_deque.append(product)

while product_deque:
    seconds += 1
    if seconds == 60:
        seconds = 0
        minutes += 1
    if minutes == 60:
        minutes = 0
        hours += 1
    if hours == 24:
        hours = 0

    for rob in free_robots_dict:
        if product_deque:
            if free_robots_dict[rob] == -1:
                free_robots_dict[rob] = 0
                print(f"{rob} - {product_deque.popleft()} [{hours:02d}:{minutes:02d}:{seconds:02d}]")
                continue
            elif free_robots_dict[rob] > -1:
                free_robots_dict[rob] += 1
                if free_robots_dict[rob] >= working_robots_dict[rob]:
                    free_robots_dict[rob] = -1
                    if product_deque:
                        free_robots_dict[rob] = 0
                        print(f"{rob} - {product_deque.popleft()} [{hours:02d}:{minutes:02d}:{seconds:02d}]")
                        continue
            product_deque.rotate(-1)