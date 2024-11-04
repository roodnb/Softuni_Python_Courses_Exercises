flower_type = input()
flower_number = int(input())
budget = int(input())

Roses = 5
Dahlias = 3.80
Tulips = 2.80
Narcissus = 3
Gladiolus = 2.50


if flower_type == 'Roses':
    total_flower_price = flower_number * Roses
elif flower_type == 'Dahlias':
    total_flower_price = flower_number * Dahlias
elif flower_type == 'Tulips':
    total_flower_price = flower_number * Tulips
elif flower_type == 'Narcissus':
    total_flower_price = flower_number * Narcissus
elif flower_type == 'Gladiolus':
    total_flower_price = flower_number * Gladiolus

if flower_number > 80 and flower_type == 'Roses':
    total_flower_price *= 0.9
elif flower_number > 90 and flower_type == 'Dahlias':
    total_flower_price *= 0.85
elif flower_number > 80 and flower_type == 'Tulips':
    total_flower_price *= 0.85
elif flower_number < 120 and flower_type == 'Narcissus':
    total_flower_price *= 1.15
elif flower_number < 80 and flower_type == 'Gladiolus':
    total_flower_price *= 1.2



if budget >= total_flower_price:
    print(f"Hey, you have a great garden with {flower_number} {flower_type} and {budget - total_flower_price:.2f} leva left.")
else:
    print(f"Not enough money, you need {total_flower_price - budget:.2f} leva more.")