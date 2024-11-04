def even_odd_sums(the_number: str):
    even_sum = 0
    odd_sum = 0
    for digit in the_number:
        digit = int(digit)
        if digit % 2 == 0:
            even_sum += digit
        else:
            odd_sum += digit
    return f'Odd sum = {odd_sum}, Even sum = {even_sum}'


number = input()
print(even_odd_sums(number))



'''
another option for the return is 

return odd_sum , even_sum

and before we pring we say

sum_odd, sum_even = even_odd_sums(numer)
'''