from collections import deque

packages_weight = list(map(int, input().split()))  # lifo
couriers_capacity = deque(map(int, input().split()))  # fifo

total_weight = 0

while packages_weight and couriers_capacity:

    if couriers_capacity[0] >= packages_weight[-1]:
        if couriers_capacity[0] > packages_weight[-1]:
            couriers_capacity[0] -= 2 * packages_weight[-1]
            if couriers_capacity[0] < 0:
                couriers_capacity.popleft()
            else:
                couriers_capacity.append(couriers_capacity.popleft())
        else:
            couriers_capacity.popleft()
        total_weight += packages_weight.pop()

    else:
        packages_weight[-1] -= couriers_capacity[0]
        total_weight += couriers_capacity.popleft()

print(f"Total weight: {total_weight} kg")

if len(packages_weight) == 0 and len(couriers_capacity) == 0:
    print("Congratulations, all packages were delivered successfully by the couriers today.")
elif len(packages_weight) != 0 and len(couriers_capacity) == 0:
    print(f"Unfortunately, there are no more available couriers to deliver the following packages: "
          f"{', '.join(str(i) for i in packages_weight)}")
else:
    print(f"Couriers are still on duty: {', '.join(str(i) for i in couriers_capacity)} "
          f"but there are no more packages to deliver.")
