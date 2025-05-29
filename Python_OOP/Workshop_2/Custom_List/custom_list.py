class CustomList:
    def __init__(self, *args, **kwargs):
        self.__value = list(args)

    def append(self, value):
        self.__value.append(value)
        return self.__value

    def remove(self, index):
        if not 0 <= index < len(self.__value):
            raise IndexError("Invalid index")

        return self.__value.pop(index)

    def get(self, index):
        if not 0 <= index < len(self.__value):
            raise IndexError("Invalid index")

        return self.__value[index]

    def extend(self, iterable):
        pass

    def insert(self, index, value):
        pass

    def pop(self):
        pass

    def clear(self):
        pass

    def index(self, value):
        pass
    