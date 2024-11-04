# stack = []
# count = int(input())
# for i in range(count):
#     command = input().split()
#     if command[0] == '1':
#         num = int(command[1])
#         stack.append(num)
#     elif len(stack) > 0:
#         if command[0] == '2':
#             stack.pop()
#         elif command[0] == '3':
#             print(max(stack))
#         elif command[0] == '4':
#             print(min(stack))
#
# print(f"{', '.join([str(x) for x in reversed(stack)])}") # tva tuka izvrashtenie e shtoto sme kazali int po-gore

# toq print moje da izglejd ai po drug nachin
# print(*reversed(stack), sep=', ') - sep e separator , a zvezdichkata otpred realno mi unpackva lista

# in addition the if elif construction can be replaced is a dictionary were the key is acutally the command[0] ( the digint ) and the value will be
# a lambda function that will perform a specific task once.
# tova


# so a second solution :

stack = []
count = int(input())

functions = {
    '1': lambda x: stack.append(int(x)),
    '2': lambda: stack.pop() if stack else None,
    '3': lambda: print(max(stack)) if stack else None,
    '4': lambda: print(min(stack)) if stack else None,
}

for i in range(count):
    command = input().split()
    functions[command[0]](*command[1:])
    # kakvo se sluchva tuk : казваме така , пипни от тоя речник ключа и понеже value-to на тоя кey e функция ,
    # тя ще бъде изпълнена.
    #понеже при 1-цата ламбдата иска и аргумент за това казваме така : пипни ключа след което ако има нещо от индекс 1 натам в командата ,
    # която е лист все пак. то го подай като аргумент на ламбдата.

print(*reversed(stack), sep=', ')