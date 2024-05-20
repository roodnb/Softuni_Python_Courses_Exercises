import math

change = float(input())
change = int(change*100)

coins_counter = 0

while change > 0:
    if change >= 200:
        change -= 200
        coins_counter += 1
    elif 200 > change >= 100:
        change -= 100
        coins_counter += 1
    elif 100 > change >= 50:
        change -= 50
        coins_counter += 1
    elif 50 > change >= 20:
        change -= 20
        coins_counter += 1
    elif 20 > change >= 10:
        change -= 10
        coins_counter += 1
    elif 10 > change >= 5:
        change -= 5
        coins_counter += 1
    elif 5 > change >= 2:
        change -= 2
        coins_counter += 1
    else:
        change -= 1
        coins_counter += 1

    change = math.floor(change)

print(coins_counter)