number = int(input())
new_list = []
for num in range(number):
    current_number = int(input())
    new_list.append(current_number)

command = input()
filtered_numbers = []
for num in new_list:
    if command == 'even' and num % 2 == 0:
        filtered_numbers.append(num)
    elif command == 'odd' and num % 2 != 0:
        filtered_numbers.append(num)
    elif command == 'negative' and num < 0:
        filtered_numbers.append(num)
    elif command == 'positive' and num >= 0:
        filtered_numbers.append(num)

print(filtered_numbers)