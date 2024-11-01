# Original totaly wrong code :

numbers_list = int(input()).split(", ")
result = 1

for i in range(numbers_list):
    number = numbers_list[i+1]
    if number <= 5
        result *= number
    elif 5 < number <= 10:
        result /= number

print(total)




# fixed code. Different types of errors below:
'''
SyntaxError - expected:
ValueError - invalid literal for int() with base 10: '2, 5, 10' - line 1
TypeError - 'list' object cannot be interpreted as an integer - line 4
TypeError - 
IndexError
NameError
'''

numbers_list = list(map(int, input().split(", ")))
result = 1

for i in range(len(numbers_list)):
    number = numbers_list[i]
    if number <= 5:
        result *= number
    elif 5 < number <= 10:
        result /= number

print(result)
