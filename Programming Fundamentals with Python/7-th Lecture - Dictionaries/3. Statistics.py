command = input().split(': ')
bakery = {}

while command[0] != "statistics":
    key = command[0]
    value = int(command[1])
    if key in bakery:
        bakery[key] += value
    else:
        bakery[key] = value

    command = input().split(': ')

print(f"Products in stock:")
for (product, quantity) in bakery.items():
    print(f"- {product}: {quantity}")
print(f"Total Products: {len(bakery.keys())}")
print(f"Total Quantity: {sum(bakery.values())}")