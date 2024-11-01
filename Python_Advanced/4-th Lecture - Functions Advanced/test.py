# def test(num):
#     if num == 10:
#         return num
#     return test(num + 1)
#
#
# print(test(1))



def facturiel(num):
    if num == 1:
        return 1
    return num * facturiel(num-1)

print(facturiel(5))