number_sequence = [int(number) for number in input().split()]

sum_numbers = sum(number_sequence)
print(f'The minimum number is {min(number_sequence)}')
print(f'The maximum number is {max(number_sequence)}')
print(f'The sum number is: {sum_numbers}')