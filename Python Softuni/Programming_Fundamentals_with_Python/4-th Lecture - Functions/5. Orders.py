def total_price(drink, quantity):
    if drink == 'coffee':
        price = 1.50
        return price * quantity
    elif drink == 'water':
        price = 1.00
        return price * quantity
    elif drink == 'coke':
        price = 1.40
        return price * quantity
    elif drink == 'snacks':
        price = 2.00
        return price * quantity

product = input()
current_price = int(input())

# calculate = total_price(product, current_price)
print(f'{total_price(product, current_price):.2f}')
# print(f'{calculate:.2f}')