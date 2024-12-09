class InvalidOperandError(Exception):
    pass


# With mapper
def sum_num(num1, num2):
    return num1 + num2


def subtract_num(num1, num2):
    return num1 - num2


def divide_num(num1, num2):
    return num1 / num2


def multiply_num(num1, num2):
    return num1 * num2


def power_num(num1, num2):
    return num1 ** num2


mapper = {
    '+': sum_num,
    '-': subtract_num,
    '/': divide_num,
    '*': multiply_num,
    '^': power_num
}


def execute(num1, sign, num2):
    if sign in mapper:
        return mapper[sign](num1, num2)
    else:
        raise InvalidOperandError




# def math_operations(n1, s, n2):
#     result = 0
#     if s == '/':
#         result = n1 / n2
#     elif s == '*':
#         result = n1*n2
#     elif s == '-':
#         result = n1 - n2
#     elif s == '+':
#         result = n1 + n2
#     elif s == '^':
#         result = n1 ** n2
#     else:
#         raise InvalidOperandError('Try again Later')
#
#     print(f"{result:.2f}")
