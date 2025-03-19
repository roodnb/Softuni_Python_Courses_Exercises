from project.animal import Animal


class Dog(Animal):

    @property
    def animal_sound(self):
        return "Woof!"

    def make_sound(self):
        return self.animal_sound
