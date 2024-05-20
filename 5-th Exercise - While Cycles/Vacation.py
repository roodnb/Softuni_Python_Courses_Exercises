trip_fund = float(input())
daily_money = float(input())

days_counter = 0
spend_count = 0

while True:
    action = input()
    save_spend_sum = float(input())
    days_counter += 1
    if action == 'spend':
        daily_money -= save_spend_sum
        if daily_money < 0:
            daily_money = 0
        spend_count += 1

        if spend_count == 5:
            print("You can't save the money.")
            print(days_counter)
            break

    if action == 'save':
        spend_count = 0
        daily_money += save_spend_sum
        if daily_money >= trip_fund:
            print(f'You saved the money for {days_counter} days.')
            break

'''
Drugo reshenie

trip_fund = float(input())
daily_money = float(input())

days_counter = 0
spend_count = 0

while daily_money < trip_fund and spend_count < 5:
    command = input()
    money = float(input())
    days_counter += 1
    
    if command == 'save':
        daily_money += money
        spend_count = 0
    elif command == 'spend':
        daily_money -= money
        spend_count += 1
        if daily_money < 0:
            daily_money = 0
            
if spend_count == 5:
    print()
    print(days_counter)

if daily_money >= trip_fund
    print()   

'''




