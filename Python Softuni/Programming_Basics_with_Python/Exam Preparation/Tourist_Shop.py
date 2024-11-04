budget = float(input())

equipment_price = 0
number_of_products = 0
third_product = 0
command = input()

while command != 'Stop':
    product = command
    product_price = float(input())
    number_of_products += 1
    third_product += 1
    if third_product == 3:
        product_price *= 0.5
        third_product = 0


    equipment_price += product_price
    remaining_money = abs(budget - equipment_price)

    if equipment_price > budget:
        print(f"You don't have enough money!")
        print(f'You need {equipment_price - budget:.2f} leva!')
        break

    command = input()

else:
    print(f"You bought {number_of_products} products for {equipment_price:.2f} leva.")