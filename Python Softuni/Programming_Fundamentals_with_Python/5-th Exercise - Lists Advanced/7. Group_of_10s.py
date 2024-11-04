def group_numbers(numbers):
    group_boundary = 10
    result = []
    while numbers:
        group = [num for num in numbers if num <= group_boundary]
        numbers = [num for num in numbers if num > group_boundary]
        result.append(f"Group of {group_boundary}'s: {group}")
        group_boundary += 10
    for group in result:
        print(group)


input_numbers = list(map(int, input().split(', ')))
group_numbers(input_numbers)



# print(f"Group of 10's: {list(num for num in numbers if 0 <= num <= 10)}")
# print(f"Group of 20's: {list(num for num in numbers if 10 < num <= 20)}")
# print(f"Group of 30's: {list(num for num in numbers if 20 < num <= 30)}")
# print(f"Group of 40's: {list(num for num in numbers if 30 < num <= 40)}")
# print(f"Group of 50's: {list(num for num in numbers if 40 < num <= 50)}")
