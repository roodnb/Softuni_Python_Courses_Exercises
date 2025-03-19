class vowels:
    def __init__(self, data: str):
        self.data = data
        self.vowels = [char for char in self.data if char.lower() in ('a', 'e', 'i', 'o', 'u', 'y')]
        self.start_index = -1

    def __iter__(self):
        return self
        # return iter(filter(lambda char: char.lower() in ('a', 'e', 'i', 'o', 'u', 'y'), self.data)) - това работи ! обаче judge си иска __next__

    def __next__(self):
        self.start_index += 1
        if self.start_index < len(self.vowels):
            return self.vowels[self.start_index]
        raise StopIteration

        # return filter(lambda char: char in ('a', 'e', 'i', 'o', 'u', 'y'), self.data)


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
