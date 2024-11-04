import sys

input_number = int(input())

max_num = -sys.maxsize
sum_numbers = 0


for index in range(0, input_number):
    num = int(input())
    if num > max_num:
        max_num = num
    sum_numbers += num

if max_num == sum_numbers - max_num:
    print('Yes')
    print(f'Sum = {sum_numbers - max_num}')
else:
    print('No')
    sum_numbers = sum_numbers - max_num
    print(f'Diff = {abs(max_num - sum_numbers)}')

