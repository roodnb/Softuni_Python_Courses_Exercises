# class take_skip:
#     def __init__(self, step: int, count: int) -> None:
#         self.step = step
#         self.count = count
#         self.current_idk = 0 - self.step
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.current_idk += self.step
#         self.count -= 1
#         if self.count < 0:
#             raise StopIteration
#         return self.current_idk


class take_skip:
    def __init__(self, step: int, count: int) -> None:
        self.step = step
        self.count = count
        self.current_idk = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_idk < self.count:
            result = self.current_idk * self.step
            self.current_idk += 1
            return result
        raise StopIteration





numbers = take_skip(2, 6)
for number in numbers:
    print(number)




numbers = take_skip(10, 5)
for number in numbers:
    print(number)
