def sum_numbers(first: int, second: int) -> int:
    return first + second


def subtract(sum_numbers_result: int, third: int) -> int:
    return sum_numbers_result - third


def add_and_subtract(first, second, third):
    returned_result = sum_numbers(first, second)
    actual_result = subtract(returned_result, third)
    return actual_result


first_num = int(input())
second_num = int(input())
third_num = int(input())
print(add_and_subtract(first_num, second_num, third_num))