def multiply(*args):
    total = args[0]
    for ele in range(1, len(args)):
        total *= args[ele]
    return total


print(multiply(1, 4, 5))
print(multiply(4, 5, 6, 1, 3))
print(multiply(2, 0, 1000, 5000))


# another way
# def multiply(*args):
#     total = 1
#     for ele in args:
#         total *= ele
#     return total