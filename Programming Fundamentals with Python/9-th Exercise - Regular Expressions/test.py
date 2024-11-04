import re

command = input()
total_spend = 0
pattern = r'>>([A-Za-z]+)<<(\d+\.?\d*)'
print(f'Bought furniture:')
while command != 'Purchase':
    matches = re.search(pattern, command)
    if matches:
        furniture = matches.group(1)
        price = float(matches[2])
        quantity = int(matches[3])
        total_spend += price*quantity
        print(furniture)
    command = input()

print(f'Total money spend: {total_spend:.2f}')