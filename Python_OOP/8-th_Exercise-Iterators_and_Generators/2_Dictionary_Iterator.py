# class dictionary_iter:
#     def __init__(self, my_dict: dict):
#         self.my_dict = my_dict
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if len(self.my_dict) > 0:
#             for k, v in self.my_dict.items():
#                 resultt = (k, v)
#                 self.my_dict.pop(k)
#                 return resultt
#         raise StopIteration




class dictionary_iter:
    def __init__(self, my_dict: dict):
        self.my_dict = tuple(my_dict.items())
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < len(self.my_dict):
            res = self.my_dict[self.i]
            self.i += 1
            return res

        raise StopIteration




result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)


print('-----------------------------NEW TEST CODE-----------------------------')

result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)
