from project.cat import Cat


class Kitten(Cat):
    def __init__(self, name: str, age: int):
        super().__init__(name, age, gender="Female")

    @property
    def animal_sound(self):
        return "Meow"
