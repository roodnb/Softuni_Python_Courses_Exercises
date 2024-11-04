n = int(input())
balanced = 0
first_bracket = ''
for i in range(n):
    string = input()
    if string == "(":
        balanced += 1
        if balanced > 1:
            print("UNBALANCED")
            exit()
    if string == ")":
        balanced -= 1
    if string == ')' and first_bracket == '':
        print("UNBALANCED")
        exit()
if balanced == 0:
    print("BALANCED")
else:
    print("UNBALANCED")