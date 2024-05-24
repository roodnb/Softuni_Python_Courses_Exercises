number_of_symbols = int(input())

for first_symbol in range(number_of_symbols):
    for second_symbol in range(number_of_symbols):
        for third_symbol in range(number_of_symbols):
            print(f'{chr(97+first_symbol)}{chr(97+second_symbol)}{chr(97+third_symbol)}')


'''
another solution is 

for first_symbol in range(97, 97 + number_of_symbols):
    for second_symbol in range(97, 97+number_of_symbols):
        for third_symbol in range(97, 97+number_of_symbols):
            print(f'{chr(first_symbol)}{chr(second_symbol)}{chr(third_symbol)}')
'''