employees_happiness = list(map(int, input().split(' ')))
factor = int(input())
actual_employees_happiness = [each_employee * factor for each_employee in employees_happiness]
average_happiness = sum(actual_employees_happiness) / len(employees_happiness)
filtered = list(filter(lambda happy_person: happy_person >= average_happiness, actual_employees_happiness))

if len(filtered) >= len(employees_happiness) / 2:
    print(f'Score: {len(filtered)}/{len(employees_happiness)}. Employees are happy!')
else:
    print(f'Score: {len(filtered)}/{len(employees_happiness)}. Employees are not happy!')
