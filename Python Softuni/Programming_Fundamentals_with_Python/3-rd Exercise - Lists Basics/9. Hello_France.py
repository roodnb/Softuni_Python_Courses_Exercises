items_with_prices = input().split('|')
budget = float(input())
train_ticket = 150
new_prices = []
money_spend = 0
for index in items_with_prices:
    article_price = index.split('->')
    item = article_price[0]
    price = float(article_price[1])
    if price > budget:
        continue
    if item == 'Clothes' and price <= 50:
        budget -= price
        money_spend += price
        new_prices.append(price * 1.4)
    elif item == 'Shoes' and price <= 35:
        budget -= price
        money_spend += price
        new_prices.append(price * 1.4)
    elif item == 'Accessories' and price <= 20.50:
        budget -= price
        money_spend += price
        new_prices.append(price * 1.4)
new_price_sum = 0
for newprice in new_prices:
    new_price_sum += newprice
    print(f'{newprice:.2f}', end=' ')
print()
new_budget = budget + new_price_sum
print(f'Profit: {new_price_sum - money_spend:.2f}')
if new_budget >= train_ticket:
    print(f'Hello, France!')
else:
    print(f'Not enough money.')


'''
the if/elif section can also be written as follows
        if (item == "Clothes" and price <= 50.0) \
                or (item == "Shoes" and price <= 35.0) \
                or (item == "Accessories" and price <= 20.50):
            budget -= price
            money_spend += price
            new_prices.append(price * 1.4)

'''