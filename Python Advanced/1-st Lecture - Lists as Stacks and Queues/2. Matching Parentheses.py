# expression = input()
# stack = []
#
#
# for i, char in enumerate(expression):
#     if char == '(':
#         stack.append(i)
#     elif char == ')':
#         result = expression[stack.pop():i + 1]
#         print(result)
#
#
#
#
# antother similar solution

expression = input()
stack = []

for i, in range(len(expression)):
    if expression[i] == '(':
        stack.append(i)
    elif expression[i] == ')':
        result = expression[stack.pop():i + 1]
        print(result)
