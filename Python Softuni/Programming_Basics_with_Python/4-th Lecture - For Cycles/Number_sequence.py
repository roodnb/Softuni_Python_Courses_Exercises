'''
number_count = int(input())


max_number = int(input())
min_number = int(input())



for _ in range(number_count - 2):
    current_number = int(input())

    if current_number > max_number:
        max_number = current_number

    if current_number < min_number:
        min_number = current_number


print(f'Max number: {max_number}')
print(f'Min number: {min_number}')


това решение е така защото :
в началото ние казваме че искаме да извъртим цикъла например 5 пъти. Това е заложено в Number_count.
и на конзолата на пъривя ред ще се чете колко пъти ще въртим например 5. 
след това в конзолата започваме да поставяме числата който ще въртим. Само ЧЕ първите две числа след 5 който зададем ,
ще станат макс и мин нъмбър. понеже те вече са зададени намаляме броя на врътките от 5 на 3 което е 5-2.
'''
import sys

number_count = int(input())

max_number = -sys.maxsize
min_number = sys.maxsize


for _ in range(number_count):
    current_number = int(input())

    if current_number > max_number:
        max_number = current_number

    if current_number < min_number:
        min_number = current_number


print(f'Max number: {max_number}')
print(f'Min number: {min_number}')



'''
трети вариянт:

number = int(input())
numbers = [int(input)) for _ in range(number)]
print(f'Max number: {max(numbers)}')
print(f'Min number: {min(numbers)}')

но не разбирам защо работи така.
'''