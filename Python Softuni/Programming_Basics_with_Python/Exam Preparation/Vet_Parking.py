number_of_days = int(input())
number_of_hours = int(input())
total_cost = 0

for day in range(1, number_of_days + 1):
    day_cost = 0
    for hours in range(1, number_of_hours + 1):
        if day % 2 == 0 and hours % 2 != 0:
            hour_cost = 2.50
        elif day % 2 != 0 and hours % 2 == 0:
            hour_cost = 1.25
        else:
            hour_cost = 1

        day_cost += hour_cost

    print(f'Day: {day} - {day_cost:.2f} leva')
    total_cost += day_cost

print(f'Total: {total_cost:.2f} leva')
