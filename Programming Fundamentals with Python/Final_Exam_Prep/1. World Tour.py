def add_stop(some_command, places):
    start_index = int(some_command[1])
    string = some_command[2]
    if start_index < len(places):
        places = places[:start_index] + string + places[start_index:]
    return places


def remove_stop(some_command, places):
    start_index = int(some_command[1])
    end_index = int(some_command[2])
    if start_index < len(places) and end_index < len(places):
        places = places[:start_index] + places[end_index + 1:]
    return places


def switch_stop(some_command, places):
    old_string = some_command[1]
    new_string = some_command[2]
    if old_string in places:
        places = places.replace(old_string, new_string)
    return places


stops = input()
while True:
    command = input().split(':')
    if command[0] == "Travel":
        break

    action = command[0]
    if action == 'Add Stop':
        stops = add_stop(command, stops)
        print(stops)

    elif action == 'Remove Stop':
        stops = remove_stop(command, stops)
        print(stops)

    elif action == 'Switch':
        stops = switch_stop(command, stops)
        print(stops)

print(f"Ready for world tour! Planned stops: {stops}")