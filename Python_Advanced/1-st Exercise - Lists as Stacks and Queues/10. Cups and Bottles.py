from collections import deque

cup_capacity = deque(map(int, input().split()))
bottle_capacity = list(map(int, input().split()))
wasted_watter = 0

while cup_capacity and bottle_capacity:
    if cup_capacity[0] > bottle_capacity[-1]:
        cup_capacity[0] -= bottle_capacity[-1]
        bottle_capacity.pop()
    elif cup_capacity[0] > bottle_capacity[-1]:
        bottle_capacity.pop()
        cup_capacity.popleft()
    else:
        wasted_watter += bottle_capacity[-1] - cup_capacity.popleft()
        bottle_capacity.pop()


if len(cup_capacity) == 0 and bottle_capacity:
    print(f"Bottles:", *bottle_capacity)
    print(f"Wasted litters of water: {wasted_watter}")
elif cup_capacity and len(bottle_capacity) == 0:
    print("Cups:", *cup_capacity)
    print(f"Wasted litters of water: {wasted_watter}")