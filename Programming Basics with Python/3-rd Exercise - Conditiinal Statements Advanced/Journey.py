budget = float(input())
season = str(input())

location = ''
place = ''
money_to_spend = 0

if budget <= 100:
    location = 'Bulgaria'
elif 100 < budget <= 1000:
    location = 'Balkans'
elif budget > 1000:
    location = 'Europe'

if season == 'summer':
    if location == 'Bulgaria':
        money_to_spend = budget * 0.3
        place = 'Camp'
    elif location == 'Balkans':
        money_to_spend = budget * 0.4
        place = 'Camp'
    elif location == 'Europe':
        money_to_spend = budget * 0.9
        place = 'Hotel'
elif season == 'winter':
    if location == 'Bulgaria':
        money_to_spend = budget * 0.7
        place = 'Hotel'
    elif location == 'Balkans':
        money_to_spend = budget * 0.8
        place = 'Hotel'
    elif location == 'Europe':
        money_to_spend = budget * 0.9
        place = 'Hotel'

print(f'Somewhere in {location}')
print(f'{place} - {money_to_spend:.2f}')


'''
Tazi zadacha moje da byde reshena i taka : 

budget = float(input())
season = str(input())

location = ''
place = ''
money_to_spend = 0

if budget <= 100:
    location = 'Bulgaria'
    if season == 'summer':
        money_to_spend = budget * 0.3
        place = 'Camp'
    else:
        money_to_spend = budget * 0.7
        place = 'Hotel'
      
    
    
elif 100 < budget <= 1000:
    location = 'Balkans'
    if season == 'summer':
        money_to_spend = budget * 0.4
        place = 'Camp'
    else:
        money_to_spend = budget * 0.8
        place = 'Hotel'
    
else: 
    location = 'Europe'
    place = 'Hotel'
    money_to_spend = budget * 0.9
    
print(f'Somewhere in {location}')
print(f'{place} - {money_to_spend:.2f}')    
'''