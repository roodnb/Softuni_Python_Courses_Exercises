class Circle:
    pi = 3.14

    def __init__(self, radius: float):
        self.radius = radius

    def set_radius(self, new_radius: float):
        self.radius = new_radius

    def get_area(self, ):
        return self.radius ** 2 * Circle.pi # ili self.pi syshto shte stane shtoto python ako ne nameri neshto v local
                                            # scope-a shte go tyrsi v enclosed

    def get_circumference(self):
        return 2 * Circle.pi * self.radius


circle = Circle(10)
circle.set_radius(12)
print(circle.get_area())
print(circle.get_circumference())
