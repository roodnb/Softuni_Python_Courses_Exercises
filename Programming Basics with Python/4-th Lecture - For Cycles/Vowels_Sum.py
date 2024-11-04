text = str(input())



sum = 0

for index in range(0,len(text)):
    if text[index] == 'a':
        sum += 1
    if text[index] == 'e':
        sum += 2
    if text[index] == 'i':
        sum += 3
    if text[index] == 'o':
        sum += 4
    if text[index] == 'u':
        sum += 5
print(sum)


