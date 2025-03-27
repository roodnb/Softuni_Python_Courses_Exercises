# def read_next(*args):
#     for ele in args:
#         for i in ele:
#             yield i


def read_next(*args):
    for ele in args:
        yield from ele # tova from na background shte naprawi realno vtoriq for cycle




for item in read_next("string", (2,), {"d": 1, "i": 2, "c": 3, "t": 4}):
    print(item, end='')


print(f"\n{'-----------------------------NEW TEST CODE-----------------------------'}")


for i in read_next("Need", (2, 3), ["words", "."]):
    print(i)
