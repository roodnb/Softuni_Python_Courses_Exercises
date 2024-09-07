command = input()
company = {}

while command != 'End':
    company_name, employee = command.split(' -> ')
    if company_name not in company.keys():
        company[company_name] = []
    if employee not in company[company_name]:
        company[company_name].append(employee)
    command = input()

for key,value in company.items():
    print(f'{key}')
    for value in company[key]:
        print(f'-- {value}')