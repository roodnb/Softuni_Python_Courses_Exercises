budget = float(input())
flour_price_per_kg = float(input())
pack_of_eggs = 0.75*flour_price_per_kg
liter_of_milk = 1.25*flour_price_per_kg
quarter_milk_price = liter_of_milk / 4
bread_price = pack_of_eggs + flour_price_per_kg + quarter_milk_price

bread_count = 0
colored_eggs_count = 0

while budget > bread_price:
    bread_count += 1
    colored_eggs_count += 3
    budget -= bread_price
    if bread_count % 3 == 0:
        colored_eggs_count -= bread_count -2

print(f'You made {bread_count} loaves of Easter bread! Now you have {colored_eggs_count} eggs and {budget:.2f}BGN left.')

