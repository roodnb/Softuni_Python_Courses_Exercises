N1 = int(input())
N2 = int(input())
operator = str(input())

result = 0
leftover = 0

if operator == '+' or operator == '-' or operator == '*':
    if operator == '+':
        result = N1 + N2
    elif operator == '-':
        result = N1 - N2
    elif operator == '*':
        result = N1 * N2

if operator == '/':
    if N2 == 0:
        print(f'Cannot divide {N1} by zero')
        exit()
    elif N2 != 0:
        result = N1 / N2

elif operator == '%':
    if N2 == 0:
        print(f'Cannot divide {N1} by zero')
        exit()
    elif N2 != 0:
        leftover = N1 % N2


if operator == '+' or operator == '-' or operator == '*':
    number_type = result % 2 == 0
    if number_type == True:
        number_type = 'even'
    elif number_type == False:
        number_type = 'odd'
    print(f'{N1} {operator} {N2} = {result} - {number_type}')

elif operator == '/':
    if N2 != 0:
        print(f'{N1} / {N2} = {result:.2f}')
else:
    operator = '%'
    print(f'{N1} % {N2} = {leftover}')



'''
print(f'{N1} {operator} {N2} = {result} - {number_type}')
print(f'{N1} / {N2} = {result:.2f}')
print(f'{N1} % {N2} = {leftover}')
print(f'Cannot divide {N1} by zero')
'''