degree = int(input())
around_the_clock = input()

outfit = ''
shoes = ''

if 10 <= degree <= 18:
    if around_the_clock == 'Morning':
        outfit = 'Sweatshirt'
        shoes = 'Sneakers'
    elif around_the_clock == 'Afternoon':
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif around_the_clock == 'Evening':
        outfit = 'Shirt'
        shoes = 'Moccasins'


elif 18 < degree <= 24:
    if around_the_clock == 'Morning':
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif around_the_clock == 'Afternoon':
        outfit = 'T-Shirt'
        shoes = 'Sandals'
    elif around_the_clock == 'Evening':
        outfit = 'Shirt'
        shoes = 'Moccasins'

elif  degree >= 25:
    if around_the_clock == 'Morning':
        outfit = 'T-Shirt'
        shoes = 'Sandals'
    elif around_the_clock == 'Afternoon':
        outfit = 'Swim Suit'
        shoes = 'Barefoot'
    elif around_the_clock == 'Evening':
        outfit = 'Shirt'
        shoes = 'Moccasins'

print(f"It's {degree} degrees, get your {outfit} and {shoes}.")