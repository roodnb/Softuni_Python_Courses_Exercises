# class sequence_repeat:
#     def __init__(self, sequence: str, number: int) -> None:
#         self.sequence = sequence
#         self.number = number
#         self.current_index = 0
#         self.count = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#
#         if self.count >= self.number:
#             raise StopIteration
#         self.count += 1
#         if self.current_index >= len(self.sequence):
#             self.current_index = 0
#         current_result = self.sequence[self.current_index]
#         self.current_index += 1
#         return current_result



class sequence_repeat:
    def __init__(self, sequence: str, number: int) -> None:
        self.sequence = sequence
        self.number = number
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.number:
            current_index = self.count % len(self.sequence)
            self.count += 1
            return self.sequence[current_index]
        raise StopIteration


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')

print(f"\n{'-----------------------------NEW TEST CODE-----------------------------'}")

result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end ='')
