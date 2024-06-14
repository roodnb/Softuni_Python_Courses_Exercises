import math
def calculator(operator, first_num, second_num):
    result = 0
    if operator == 'multiply':
        result = first_num * second_num
    elif operator == 'divide':
        result = int(first_num / second_num)
    elif operator == 'add':
        result = first_num + second_num
    elif operator == 'subtract':
        result = first_num - second_num
    return result


operator = input()
first_num = int(input())
second_num = int(input())

print(calculator(operator, first_num, second_num))