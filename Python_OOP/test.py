# class Car:
#
#     def __init__(self, type: str, model: str, licplate: str):
#         self.type = type
#         self.model = model
#         self.licplate = licplate
#
#     def __str__(self):
#         return f"nai-dobroto {self.type}, {self.model}, {self.licplate}"
#
#
# c = Car("SUV", "Kodiaq", "CB2153AB")
#
# print(c)
#
#
# c.model = "Octavia"
# print(c)


class Car:

    def __init__(self,*args, **kwargs):
        for k, v in kwargs.items():
            print(self.__setattr__(k, v))


c = Car(1, 2, 3, car="Skoda", Model="Octavia")

