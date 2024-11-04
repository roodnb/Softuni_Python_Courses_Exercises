sea_left = int(input())
mountain_left = int(input())

total_sum_sea = 0
total_sum_mountain = 0
profit = total_sum_mountain + total_sum_sea
command = input()

while command != 'Stop':
    trip_name = command
    if trip_name == 'sea':
        price_sea = 680
        if sea_left <= 0:
            total_sum_sea += 0
        else:
            total_sum_sea += price_sea
            sea_left -= 1

    if trip_name == 'mountain':
        price_mountain = 499
        if mountain_left <= 0:
            total_sum_mountain += 0
        else:
            total_sum_mountain += price_mountain
            mountain_left -= 1

    profit = total_sum_mountain + total_sum_sea

    if sea_left <= 0 and mountain_left <= 0:
        print(f'Good job! Everything is sold.')
        print(f'Profit: {profit} leva.')
        break

    command = input()

if command == 'Stop':
    print(f'Profit: {profit} leva.')

