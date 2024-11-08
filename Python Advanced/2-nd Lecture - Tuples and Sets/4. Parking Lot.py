num_commands = int(input())
car_numbers = set()

for _ in range(num_commands):
    direction, number = input().split(', ')
    if direction == "IN":
        car_numbers.add(number)
    elif direction == "OUT":
        car_numbers.remove(number)

if car_numbers:
    print(*car_numbers, sep="\n")
else:
    print("Parking Lot is Empty")