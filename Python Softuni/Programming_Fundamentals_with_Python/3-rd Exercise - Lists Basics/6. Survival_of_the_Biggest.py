# numbers = input().split()
# remove_count = int(input())
# numbers_int = []
# for num in numbers:
#     numbers_int.append(int(num))
# numbers_int.sort(reverse=True)
# for remove in range(remove_count):
#     numbers_int.pop(-1)
# numbers_str = []
# for integer in numbers_int:
#     current_string = str(integer)
#     numbers_str.append(current_string)
# print(', '.join(numbers_str))

numbers = input().split()
remove_count = int(input())
numbers_int = []
for num in numbers:
    numbers_int.append(int(num))
for action in range(remove_count):
    digit_to_remove = min(numbers_int)
    numbers_int.remove(digit_to_remove)
numbers_str = []
for integer in numbers_int:
    current_string = str(integer)
    numbers_str.append(current_string)

print(', '.join(numbers_str))