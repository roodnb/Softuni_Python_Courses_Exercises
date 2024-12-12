def accommodate(*groups, **rooms_capacity):
    sorted_rooms = sorted(rooms_capacity.items(), key=lambda x: (x[1], x[0]))

    occupied_rooms = {}
    unaccommodated = 0

    for group_size in groups:
        for index in  sorted_rooms:
            if group_size <= index[1]:
                occupied_rooms[index[0][-3:]] = group_size
                sorted_rooms.remove(index)
                break
        else:
            unaccommodated += group_size

    result = ''
    if occupied_rooms:
        result += f"A total of {len(occupied_rooms)} accommodations were completed!"
        sorted_occupied_room = sorted(occupied_rooms.items(), key=lambda x: x[0])
        for k, v in sorted_occupied_room:
            result += f"\n<Room {k} accommodates {v} guests>"

    else:
        result += f"No accommodations were completed!"

    if unaccommodated > 0:
        result += f"\nGuests with no accommodation: {unaccommodated}"

    if sorted_rooms:
        result += f"\nEmpty rooms: {len(sorted_rooms)}"

    return result



# test code
print('==========================================================')
print(accommodate(5, 4, 2, room_305=6, room_410=5, room_204=2))
print('==========================================================')
print(accommodate(10, 9, 8, room_307=6, room_802=5))
print('==========================================================')
print(accommodate(1, 2, 4, 8, room_102=3, room_101=1, room_103=2))
print('==========================================================')