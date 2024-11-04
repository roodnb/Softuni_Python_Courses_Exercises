number = int(input())
number_string = str(number)

highest_number = sorted(number_string, reverse=True)

for digit in highest_number:
    print(digit, end='')