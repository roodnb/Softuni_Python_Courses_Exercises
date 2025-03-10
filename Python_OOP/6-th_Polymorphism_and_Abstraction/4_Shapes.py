from abc import ABC, abstractmethod
import math


class Shape(ABC):

    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius

    def calculate_area(self):
        return math.pi * self.__radius**2

    def calculate_perimeter(self):
        return 2 * self.__radius * math.pi


class Rectangle(Shape):
    def __init__(self, height, width):
        self.__width = width
        self.__height = height

    def calculate_area(self):
        return self.__width * self.__height

    def calculate_perimeter(self):
        return 2 * (self.__height + self.__width)



circle = Circle(5)
print(circle.calculate_area())
print(circle.calculate_perimeter())
