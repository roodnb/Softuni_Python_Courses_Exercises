def data_types(type, value):
    if type == 'int':
        num = int(value) * 2
        return num
    elif type == 'real':
        num = float(value) * 1.5
        return f'{num:.2f}'
    return f'${value}$'


data_type = input()
numer = input()
print(data_types(data_type, numer))