# class Circle:
#     __fi = 6.25
#
#     def __init__(self, radius):
#         self.radius = radius
#         self.__pi = 3.14
#         self._test = 9
#
#
#
#
# c = Circle(5)
# c.radius = 8
# # print(c.radius)
# # print(c._test)
#
# # print(c._Circle__pi)
#
# print(c._Circle__fi)
# c._Circle__fi = 8
# print(c._Circle__fi)
#
#
#
#


class Phone:
    def __getattr__(self, attr):
        return "pesho"

phone = Phone()
print(phone.color)
print(getattr(phone, 'size'))