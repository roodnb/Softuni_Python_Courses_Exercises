age = int(input())
washing_machine = float(input())
toy_price = int(input())

toys = 0
toy_money = 0
money = 0
save_money = 0

for birthdays in range(1, age + 1):

    if birthdays % 2 == 1:
        toys += 1
        toy_money = toys * toy_price
    else:
        money += 10
        save_money += money -1

total_collected_money = save_money + toy_money

if washing_machine <= total_collected_money:
    print(f'Yes! {total_collected_money - washing_machine:.2f}')
else:
    print(f'No! {washing_machine - total_collected_money:.2f}')




