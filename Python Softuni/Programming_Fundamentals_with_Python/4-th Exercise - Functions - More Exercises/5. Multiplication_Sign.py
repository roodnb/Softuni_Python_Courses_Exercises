def multiplication_sign(first: int, second: int, third: int) -> str:
    if first == 0 or second == 0 or third == 0:
        return 'zero'
    new_list = [first, second, third]
    below_zero_count = 0
    for index in new_list:
        if index < 0:
            below_zero_count += 1
    if below_zero_count == 1 or below_zero_count == 3:
        return 'negative'
    return 'positive'


first_num = int(input())
second_num = int(input())
third_num = int(input())
print(multiplication_sign(first_num, second_num, third_num))
