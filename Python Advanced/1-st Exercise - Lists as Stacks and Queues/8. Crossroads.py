from collections import deque

green_light = int(input())
free_window = int(input())
cars = deque()
count = 0

while True:
    current_green_light = green_light
    current_free_window = free_window
    command = input()
    if command == 'END':
        break

    if command == 'green':
        while cars:
            if current_green_light > 0:
                if current_green_light < len(cars[0]) and current_free_window < len(cars[0]) - current_green_light:
                    hit_index = current_green_light + current_free_window
                    hit_letter = cars[0][hit_index]
                    print(f"A crash happened!\n"
                          f"{cars[0]} was hit at {hit_letter}.")
                    exit()
                elif current_green_light >= len(cars[0]):
                    current_green_light -= len(cars.popleft())
                    count += 1
                elif current_green_light < len(cars[0]) and current_free_window >= len(cars[0]) - current_green_light:
                    cars.popleft()
                    current_green_light = 0
                    count +=1
                else:
                    continue
            else:
                break
    else:
        cars.append(command)

print(f"Everyone is safe. \n"
      f"{count} total cars passed the crossroads.")