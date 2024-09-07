products_and_quantities = input().split()
bakery = {}

for index in range(0, len(products_and_quantities), 2):
    key = products_and_quantities[index]
    value = products_and_quantities[index + 1]
    bakery[key] = int(value)

searched_product = input().split()

for product in searched_product:
    if product in bakery:
        print(f"We have {bakery[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")