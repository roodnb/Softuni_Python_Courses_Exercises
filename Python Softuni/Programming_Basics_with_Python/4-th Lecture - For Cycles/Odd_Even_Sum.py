number = int(input())

odd_sum = 0
even_sum = 0

for index in range(1, number + 1):
    current_number = int(input())

    if index % 2 == 0:
        even_sum += current_number
    else:
        odd_sum += current_number

if even_sum == odd_sum:
    print(f'Yes')
    print(f'Sum = {even_sum}')
else:
    diff = abs(even_sum - odd_sum)
    print(f'No')
    print(f'Diff = {diff}')
