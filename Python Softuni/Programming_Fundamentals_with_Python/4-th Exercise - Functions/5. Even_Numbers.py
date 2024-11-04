def is_even(current_number):
    return current_number % 2 == 0


numbers_string = input().split()
number_list = []
for number in numbers_string:
    number_list.append(int(number))


final_list = list(filter(is_even, number_list))
print(final_list)

'''
another example:

numbers_string = input().split()
number_list = []
for number in numbers_string:
    number_list.append(int(number))
is_even = lambda x: x % 2 == 0
final_list = list(filter(is_even, number_list))
print(final_list)

'''

'''and one more example:

number_as_digit = [int(number) for number in input().split() if int(number) % 2 == 0]
print(number_as_digit)

'''