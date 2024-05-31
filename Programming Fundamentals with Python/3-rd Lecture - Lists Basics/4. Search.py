number = int(input())
word = input()
new_list = list()
for string in range(number):
    current_string = input()
    new_list.append(current_string)

filtered_string = []
for string in new_list:
    if word in string:
        filtered_string.append(string)

print(new_list)
print(filtered_string)


