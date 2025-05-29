class Pesho:
    __instance = None

    def __init__(self, name):
        if Pesho.__instance is not None:
            raise Exception("imame go veche")
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if Pesho.__instance is None:
            Pesho.__instance = value
        self.__name = value
        return self.__name


s1 = Pesho("test")
print(s1)

s2 = Pesho("test2")



getattr()