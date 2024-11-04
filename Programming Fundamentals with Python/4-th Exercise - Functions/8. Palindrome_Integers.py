def is_palindrome(number):
    reversed_num = number[::-1]
    return number == reversed_num

numbers = input().split(', ')
for current_num in numbers:
    print(is_palindrome(current_num))

'''
in this case , the if actually returns you a bool which means that i can just do the following:

return number == reversed_num

because in any case will send you either true of false

'''