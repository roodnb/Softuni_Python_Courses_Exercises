command = input()
products = {}

while command != 'buy':
    current_command = command.split(' ')
    name = current_command[0]
    price = float(current_command[1])
    quantity = float(current_command[2])
    if name not in products.keys():
        products[name] = []
        products[name].append(price)
        products[name].append(quantity)
    else:
        products[name][0] = price
        products[name][1] += quantity

    command = input()


for key,value in products.items():
    total_price_per_product = value[0]*value[1]
    print(f'{key} -> {total_price_per_product:.2f}')