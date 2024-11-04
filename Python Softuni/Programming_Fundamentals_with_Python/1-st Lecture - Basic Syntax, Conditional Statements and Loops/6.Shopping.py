budget = int(input())
total_spend = 0
while True:
    command = input()
    if command == 'End':
        print('You bought everything needed.')
        break
    else:
        price = int(command)
        total_spend += price
        if total_spend > budget:
            print(f'You went in overdraft!')
            break