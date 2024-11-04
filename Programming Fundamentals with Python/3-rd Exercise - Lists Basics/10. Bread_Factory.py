event_string = input().split('|')
energy = 100
coins = 100
isopen = True
for index in event_string:
    new_event_string = index.split("-")
    event_or_ingredient = new_event_string[0]
    energy_or_coin_number = int(new_event_string[1])
    if event_or_ingredient == 'rest':
        initial_energy = energy
        energy += energy_or_coin_number
        if energy > 100:
            energy = 100
        gained_energy = energy - initial_energy
        print(f'You gained {gained_energy} energy.')
        print(f'Current energy: {energy}.')
    elif event_or_ingredient == 'order':
        if energy >= 30:
            coins += energy_or_coin_number
            energy -= 30
            print(f'You earned {energy_or_coin_number} coins.')
        else:
            energy += 50
            print('You had to rest!')
    else:
        if coins >= energy_or_coin_number:
            coins -= energy_or_coin_number
            print(f'You bought {event_or_ingredient}.')
        else:
            isopen = False
            break
if isopen == True:
    print(f'Day completed! \n'
          f'Coins: {coins} \n'
          f'Energy: {energy}')
else:
    print(f'Closed! Cannot afford {event_or_ingredient}.')