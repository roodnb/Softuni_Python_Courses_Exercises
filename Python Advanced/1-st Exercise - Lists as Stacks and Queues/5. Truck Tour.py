from collections import deque
petrol_pumps = int(input())
pumps = deque()

for _ in range(petrol_pumps):
    petrol, distance = list(map(int, input().split()))
    pumps.append([petrol, distance])

starting_position = 0
stops = 0

while stops < petrol_pumps:
    fuel = 0
    for i in range(petrol_pumps):
        fuel += pumps[i][0]
        distance = pumps[i][1]
        if fuel < distance:
            pumps.rotate(-1)
            starting_position += 1
            stops = 0
            break
        fuel -= distance
        stops += 1

print(starting_position)
