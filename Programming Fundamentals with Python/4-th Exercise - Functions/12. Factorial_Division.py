def factorial_division(num_one, num_two):
    first_num_multiply = 1
    second_num_multiply = 1
    for num in range(1, num_one +1):
        first_num_multiply *= num
    for num in range(1, num_two + 1):
        second_num_multiply *= num
    return f'{first_num_multiply/second_num_multiply:.2f}'


first_number = int(input())
second_number = int(input())
print(factorial_division(first_number, second_number))

'''
for the sake of the fact that we have a function instead of having 1 function to do everything for BOTH numbers.
i will create a function that will do it one after another



# def factorial_division(num):
#     for i in range(1, num):# tuk ne pishem num + 1 zashtoto nie taka ili inache kazvame che num *= na i. ama nie num veche go imame
#         num *= i
#     return num
# 
# 
# first_number = int(input())
# second_number = int(input())
# print(f"{factorial_division(first_number) / factorial_division(second_number):.2f}")
'''