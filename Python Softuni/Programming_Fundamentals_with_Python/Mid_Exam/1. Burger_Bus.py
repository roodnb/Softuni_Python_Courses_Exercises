number_of_cities = int(input())

total_profit = 0
for current_city in range(1, number_of_cities + 1):
    city_name = input()
    earned_money = float(input())
    expenses = float(input())
    if current_city % 5 == 0:
        earned_money *= 0.9
    elif current_city % 3 == 0:
        expenses *= 1.5
    profit = earned_money - expenses
    total_profit += profit
    print(f'In {city_name} Burger Bus earned {profit:.2f} leva.')

print(f'Burger Bus total profit: {total_profit:.2f} leva.')