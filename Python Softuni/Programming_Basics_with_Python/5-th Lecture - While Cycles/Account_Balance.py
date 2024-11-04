account_balance = 0
while True:
    text = input()
    if text == 'NoMoreMoney':
        break

    current_number = float(text)
    if current_number >= 0:
        account_balance += current_number
        print(f'Increase: {current_number:.2f}')
    else:
        print(f'Invalid operation!')
        break

print(f'Total: {account_balance:.2f}')

'''
drugo reshenie


inpt = input()
balance = 0

while inpt != 'NoMoreMoney':
    amount = float(inpt)
    if amount < 0:
        print(f'Invalid operation!')
        break

    balance += amount
    print(f'Increase: {amount:.2f}')
    inpt = input()

print(f'Total: {balance:.2f}')

'''