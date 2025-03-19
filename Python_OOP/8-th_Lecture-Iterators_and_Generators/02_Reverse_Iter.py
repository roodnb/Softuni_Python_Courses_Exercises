# class reverse_iter:
#     def __init__(self, iterable):
#         self.iterable = iterable
#         self.start_index = -1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.start_index += 1
#         result = self.iterable[::-1]
#         if self.start_index < len(result):
#             return result[self.start_index]
#         raise StopIteration


# class reverse_iter:
#     def __init__(self, iterable):
#         self.iterable = iterable
#         self.end_index = len(self.iterable)
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.end_index -= 1
#         if self.end_index >= 0:
#             return self.iterable[self.end_index]
#         raise StopIteration


class reverse_iter:
    def __init__(self, iterable):
        self.iterable = iterable
        self.end_index = len(self.iterable)

    def __iter__(self):
        return reversed(self.iterable)


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)





