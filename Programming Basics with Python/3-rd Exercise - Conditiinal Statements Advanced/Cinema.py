type_of_projections = input()
row = int(input())
colum = int(input())


all_seats = row * colum
income = 0

if type_of_projections == ('Premiere'):
    income = all_seats * 12.00
elif type_of_projections == ('Normal'):
    income = all_seats * 7.50
elif type_of_projections == ('Discount'):
    income = all_seats * 5.00

print(f'{income:.2f} leva')