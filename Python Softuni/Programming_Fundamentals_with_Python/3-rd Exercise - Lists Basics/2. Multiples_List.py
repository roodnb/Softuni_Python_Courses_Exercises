factor = int(input())
count = int(input())
new_list = []

for numbers in range(1, count + 1):
    new_list.append(numbers * factor)

print(new_list)