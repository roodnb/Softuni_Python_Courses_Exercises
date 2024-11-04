number_of_commands = int(input())
parking = {}

for action in range(number_of_commands):
    command = input().split()
    actual_command = command[0]
    if actual_command == 'register':
        username = command[1]
        license_plate_num = command[2]
        if username not in parking.keys():
            parking[username] = license_plate_num
            print(f"{username} registered {license_plate_num} successfully")
        else:
            print(f'ERROR: already registered with plate number {license_plate_num}')
    elif actual_command == 'unregister':
        username = command[1]
        if username in parking.keys():
            parking.pop(username)
            print(f"{username} unregistered successfully")
        else:
            print(f"ERROR: user {username} not found")

for key,value in parking.items():
    print(f'{key} => {value}')
