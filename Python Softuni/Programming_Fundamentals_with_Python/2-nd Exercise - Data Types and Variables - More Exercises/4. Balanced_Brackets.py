number_of_lines = int(input())
balanced = 0
first_bracket = ''
for i in range(number_of_lines):
    command = input()
    if command == "(":
        first_bracket = '('
        balanced += 1
        if balanced > 1:
            print("UNBALANCED")
            exit()
    if command == ")":
        balanced -= 1
    if command == ')' and first_bracket == '':
        print("UNBALANCED")
        exit()
if balanced == 0:
    print("BALANCED")
else:
    print("UNBALANCED")