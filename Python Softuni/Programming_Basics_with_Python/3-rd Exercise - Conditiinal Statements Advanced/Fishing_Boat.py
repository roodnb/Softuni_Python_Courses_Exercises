budget = int(input())
season = str(input())
fisherman = int(input())

total_price = 0

boatprice_spring = 3000
boatprice_summer_autumn = 4200
boatprice_winter = 2600
total_boat_price = 0



if season == 'Spring':
    if fisherman <= 6:
        boatprice_spring *= 0.9
    elif 7 <= fisherman <= 11:
        boatprice_spring *= 0.85
    elif fisherman >= 12:
        boatprice_spring *= 0.75

elif season == 'Summer' or season == 'Autumn':
    if fisherman <= 6:
        boatprice_summer_autumn *= 0.9
    elif 7 <= fisherman <= 11:
        boatprice_summer_autumn *= 0.85
    elif fisherman >= 12:
        boatprice_summer_autumn *= 0.75

elif season == 'Winter':
    if fisherman <= 6:
        boatprice_winter *= 0.9
    elif 7 <= fisherman <= 11:
        boatprice_winter *= 0.85
    elif fisherman >= 12:
        boatprice_winter *= 0.75

if fisherman % 2 == 0:
    if season == "Spring":
        total_boat_price = boatprice_spring * 0.95
    elif season == 'Summer':
        total_boat_price = boatprice_summer_autumn * 0.95
    elif season == 'Autumn':
        total_boat_price = boatprice_summer_autumn
    elif season == 'Winter':
        total_boat_price = boatprice_winter * 0.95

elif fisherman % 2 == 1:
    if season == "Spring":
        total_boat_price = boatprice_spring
    elif season == 'Summer':
        total_boat_price = boatprice_summer_autumn
    elif season == 'Autumn':
        total_boat_price = boatprice_summer_autumn
    elif season == 'Winter':
        total_boat_price = boatprice_winter


if budget >= total_boat_price:
    print(f'Yes! You have {budget - total_boat_price:.2f} leva left.')
else:
    print(f'Not enough money! You need {total_boat_price - budget:.2f} leva.')


'''
друг вариянт за решение , който е в пъти по лесен : 

budget = int(input())
season = str(input())
fisherman = int(input())

total_price = 0

if season == 'Spring':
    total_price = 3000
elif season == 'Summer' or season == 'Autumn':
    total_price = 4200
elif season == 'Winter':
    total_price = 2600


if fisherman <= 6:
    total_price *= 0.9
elif 7 <= fisherman <= 11:
    total_price *= 0.85
elif fisherman >= 12:
    total_price *= 0.75


if season != 'Autumn' and fisherman % 2 == 0:
    total_price *= 0.95
else:
    pass

if budget >= total_price:
    print(f'Yes! You have {budget - total_price:.2f} leva left.')
else:
    print(f'Not enough money! You need {total_price - budget:.2f} leva.')

'''