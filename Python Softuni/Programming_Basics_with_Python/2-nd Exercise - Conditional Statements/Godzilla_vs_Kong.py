budget = float(input())
staff = int(input())
price_per_wear = float(input())

decor = budget*0.1
price_of_total_wear = staff*price_per_wear

if staff > 150:
    price_of_total_wear *= 0.9

total_cost = decor + price_of_total_wear

if total_cost > budget:
    print('Not enough money!')
    print(f'Wingard needs {total_cost - budget:.2f} leva more.')
if total_cost <= budget:
    print('Action!')
    print(f'Wingard starts filming with {budget - total_cost:.2f} leva left.')