# 1-st resolution using reduce
from functools import reduce


def operate(operator, *args):

    def sum_num():
        return reduce(lambda x, y: x + y, args)

    def subtract_num():
        return reduce(lambda x, y: x - y, args)

    def multiply_num():
        return reduce(lambda x, y: x * y, args)

    def divide_num():
        return reduce(lambda x, y: x / y, args)

    if operator == "+":
        return sum_num()
    elif operator == "-":
        return subtract_num()
    elif operator == "*":
        return multiply_num()
    elif operator == "/":
        return divide_num()


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))



# 2nd resolution using mapper ( dictionary key valye pair )

# from functools import reduce
# def operate(operator, *args):
#
#     def sum_num():
#         return reduce(lambda x, y: x + y, args)
#
#     def subtract_num():
#         return reduce(lambda x, y: x - y, args)
#
#     def multiply_num():
#         return reduce(lambda x, y: x * y, args)
#
#     def divide_num():
#         return reduce(lambda x, y: x / y, args)
#
#     dictionary = {'+': sum_num, "-": subtract_num, "*": multiply_num, "/": divide_num}
#     # кръстихме го дикт , в който ние реално mapwavame key към value
#     return dictionary[operator]()
#
#
# print(operate("+", 1, 2, 3))
# print(operate("*", 3, 4))
