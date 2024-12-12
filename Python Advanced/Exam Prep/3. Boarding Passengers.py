def boarding_passengers(capacity, *args):
    total_guests = sum([passenger_group_info[0] for passenger_group_info in args])
    boarded_guests = {}
    on_board = 0

    for index in args:
        guests, benefit = index

        if capacity == 0:
            break

        if guests <= capacity:
            if benefit not in boarded_guests:
                boarded_guests[benefit] = 0
            boarded_guests[benefit] += guests
            capacity -= guests

            on_board += guests

    remaining_guests = total_guests - on_board
    sorted_guests = dict(sorted(boarded_guests.items(), key=lambda x: (-x[1], x[0])))

    result = "Boarding details by benefit plan:\n"
    for k, v in sorted_guests.items():
        result += f"## {k}: {v} guests\n"

    if remaining_guests <= 0:
        result += "All passengers are successfully boarded!"

    if capacity == 0 and remaining_guests > 0:
        result += "Boarding unsuccessful. Cruise ship at full capacity."

    if capacity != 0 and remaining_guests > 0:
        result += f"Partial boarding completed. Available capacity: {capacity}."

    return result




print(boarding_passengers(150, (35, 'Diamond'), (55, 'Platinum'), (35, 'Gold'), (25, 'First Cruiser')))

print(boarding_passengers(100, (20, 'Diamond'), (15, 'Platinum'), (25, 'Gold'), (25, 'First Cruiser'), (15, 'Diamond'), (10, 'Gold')))

print(boarding_passengers(120, (30, 'Gold'), (20, 'Platinum'), (30, 'Diamond'), (10, 'First Cruiser'), (31, 'Platinum'), (20, 'Diamond')))


