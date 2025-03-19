from project.animal import Animal


class Cat(Animal):

    @property
    def animal_sound(self):
        return "Meow meow!"

    def make_sound(self):
        return self.animal_sound
