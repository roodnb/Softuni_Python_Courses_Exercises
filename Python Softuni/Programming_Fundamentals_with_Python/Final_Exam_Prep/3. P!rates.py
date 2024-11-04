city_info = {}

while True:
    command = input().split("||")
    if command[0] == "Sail":
        break
    city = command[0]
    population = int(command[1])
    gold = int(command[2])
    if city not in city_info:
        city_info[city] = {'population': population, 'gold': gold}
    else:
        city_info[city]['population'] += population
        city_info[city]['gold'] += gold

while True:
    new_command = input().split('=>')
    if new_command[0] == 'End':
        break

    action = new_command[0]
    if action == 'Plunder':
        town = new_command[1]
        people = int(new_command[2])
        gold = int(new_command[3])
        city_info[town]['population'] -= people
        city_info[town]['gold'] -= gold
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        if city_info[town]['population'] <= 0 or city_info[town]['gold'] <= 0:
            del city_info[town]
            print(f"{town} has been wiped off the map!")

    elif action == 'Prosper':
        town = new_command[1]
        gold = int(new_command[2])
        if gold < 0:
            print("Gold added cannot be a negative number!")
            continue
        else:
            city_info[town]['gold'] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {city_info[town]['gold']} gold.")


if city_info != {}:
    print(f"Ahoy, Captain! There are {len(city_info.keys())} wealthy settlements to go to: ")
    for citi, info in city_info.items():
        print(f"{citi} -> Population: {info['population']} citizens, Gold: {info['gold']} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")

