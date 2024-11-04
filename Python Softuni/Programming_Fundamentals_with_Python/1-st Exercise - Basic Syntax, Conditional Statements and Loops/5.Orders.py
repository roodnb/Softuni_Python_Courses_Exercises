number_of_orders = int(input())
total_price = 0
for n in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())
    if 100 < price_per_capsule or price_per_capsule < 0.01:
        continue
    elif 31 < days or days < 1: # elif days not in range(1,31+1)
        continue
    elif 2000 < capsules_per_day or capsules_per_day < 1:
        continue
    price = price_per_capsule*days*capsules_per_day
    print(f'The price for the coffee is: ${price:.2f}')
    total_price += price
print(f'Total: ${total_price:.2f}')