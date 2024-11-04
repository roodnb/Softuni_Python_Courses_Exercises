open_tabs = int(input())
salary = float(input())


website = ''
remaining_salary = 0

for tab in range(1, open_tabs + 1):
    website = input()
    if website == 'Facebook':
        salary -= 150
    elif website == 'Instagram':
        salary -= 100
    elif website == 'Reddit':
        salary -= 50

    if salary <= 0:
        break

if salary > 0:
    print(round(salary))
else:
    print(f'You have lost your salary.')


