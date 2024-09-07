import re


def get_the_customer(string):
    pattern1 = r'%([A-Z][a-z]+)%'
    match_name = re.search(pattern1, string)
    if match_name:
        return match_name.group(1)


def get_the_product(string):
    pattern2 = r'<(\w+)>'
    match_product = re.search(pattern2, string)
    if match_product:
        return match_product.group(1)


def get_the_count(string):
    pattern3 = r'\|(\d+)\|'
    match_count = re.search(pattern3, string)
    if match_count:
        return match_count.group(1)


def get_the_price(string):
    pattern4 = r'(\d+([.\d+]*))([\$])'
    match_price = re.search(pattern4, string)
    if match_price:
        return match_price.group(1)


command = input()
total_income = 0
while command != 'end of shift':

    customer = get_the_customer(command)
    product = get_the_product(command)
    count = get_the_count(command)
    price = get_the_price(command)
    if customer and product and count and price != None:
        total_price = int(count) * float(price)
        total_income += total_price
        print(f'{customer}: {product} - {total_price:.2f}')

    command = input()

print(f'Total income: {total_income:.2f}')