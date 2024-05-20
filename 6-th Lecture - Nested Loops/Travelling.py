destination = input()

total_saved_money = 0

while destination != 'End':
    required_budget = float(input())
    while total_saved_money <= required_budget:
        daily_saved_money = float(input())
        total_saved_money += daily_saved_money
        if total_saved_money >= required_budget:
            print(f'Going to {destination}!')
            total_saved_money = 0
            break

    destination = input()

    if destination == 'End':
        break



