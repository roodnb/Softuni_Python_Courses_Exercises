str1 = input()
str2 = input()
items = []
for char in range(0, len(str1) + 1):
    current_string = str2[:char+1] + str1[char+1:]
    items.append(current_string)

items = list(dict.fromkeys(items))

for i in items:
    print(i)