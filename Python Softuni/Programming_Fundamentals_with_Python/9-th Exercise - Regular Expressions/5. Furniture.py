import re

command = input()
total_spend = 0
pattern = r'\b(?<=>>)([\w]+)<<([\d\.]+)!([\d]+)\b'
print(f'Bought furniture:')
while command != 'Purchase':
    matches = re.findall(pattern, command)
    for match in matches:
        furniture = match[0]
        price = float(match[1])
        quantity = int(match[2])
        total_spend += price*quantity
        print(furniture)
    command = input()
print(f'Total money spend: {total_spend:.2f}')


# another solution:
# import re
#
# command = input()
# total_spend = 0
# pattern = r'>>([A-Za-z]+)<<(\d+\.?\d*)'
# print(f'Bought furniture:')
# while command != 'Purchase':
#     matches = re.search(pattern, command)
#     if matches:
#         furniture, price, quantity = matches.groups()
#         total_spend += float(price) * int(quantity)
#         print(furniture)
#     command = input()
#
# print(f'Total money spend: {total_spend:.2f}')