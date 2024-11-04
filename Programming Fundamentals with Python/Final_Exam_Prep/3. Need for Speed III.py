number_of_cars = int(input())
cars_dict = {}
for data in range(number_of_cars):
    command = input().split('|')
    car = command[0]
    mileage = int(command[1])
    fuel = int(command[2])
    cars_dict[car] = {'mileage': mileage, 'fuel': fuel}

while True:
    new_command = input().split(' : ')
    if new_command[0] == 'Stop':
        break

    action = new_command[0]
    if action == 'Drive':
        current_car = new_command[1]
        distance = int(new_command[2])
        current_fuel = int(new_command[3])
        if cars_dict[current_car]['fuel'] >= current_fuel:
            cars_dict[current_car]['mileage'] += distance
            cars_dict[current_car]['fuel'] -= current_fuel
            print(f"{current_car} driven for {distance} kilometers. {current_fuel} liters of fuel consumed.")
        elif cars_dict[current_car]['fuel'] < current_fuel:
            print("Not enough fuel to make that ride")
        if cars_dict[current_car]['mileage'] >= 100000:
            del cars_dict[current_car]
            print(f"Time to sell the {current_car}!")

    elif action == 'Refuel':
        current_car = new_command[1]
        current_fuel = int(new_command[2])
        recharged_amount = 0
        if cars_dict[current_car]['fuel'] + current_fuel > 75:
            recharged_amount += 75 - cars_dict[current_car]['fuel']
            cars_dict[current_car]['fuel'] = 75
        else:
            recharged_amount += current_fuel
            cars_dict[current_car]['fuel'] += current_fuel
        print(f'{current_car} refueled with {recharged_amount} liters')

    elif action == 'Revert':
        current_car = new_command[1]
        kilometers = int(new_command[2])
        if cars_dict[current_car]['mileage'] - kilometers < 10000:
            cars_dict[current_car]['mileage'] = 10000
        else:
            cars_dict[current_car]['mileage'] -= kilometers
            print(f'{current_car} mileage decreased by {kilometers} kilometers')

for car, info in cars_dict.items():
    print(f"{car} -> Mileage: {info['mileage']} kms, Fuel in the tank: {info['fuel']} lt.")