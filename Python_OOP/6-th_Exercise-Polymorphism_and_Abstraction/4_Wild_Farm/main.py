from project.food import *
from project.animals.animal import *
from project.animals.birds import *
from project.animals.mammals import *

owl = Owl("Pip", 10, 10)
print(owl)
meat = Meat(4)
print(owl.make_sound())
owl.feed(meat)
veg = Vegetable(1)
print(owl.feed(veg))
print(owl)


# print("---------------------\nNew Test\n--------------------")
#
# hen = Hen("Harry", 10, 10)
# veg = Vegetable(3)
# fruit = Fruit(5)
# meat = Meat(1)
# print(hen)
# print(hen.make_sound())
# hen.feed(veg)
# hen.feed(fruit)
# hen.feed(meat)
# print(hen)


# first zero test
# import unittest
# from project.animals.birds import Owl, Hen
# from project.animals.mammals import Mouse, Dog, Cat, Tiger
# from project.food import Vegetable, Fruit, Meat, Seed
#
#
# class WildFarmTests(unittest.TestCase):
#     def test_first_zero(self):
#         owl = Owl("Pip", 10, 10)
#         self.assertEqual(str(owl), "Owl [Pip, 10, 10, 0]")
#         meat = Meat(4)
#         self.assertEqual(owl.make_sound(), "Hoot Hoot")
#         owl.feed(meat)
#         veg = Vegetable(1)
#         owl.feed(veg)
#         self.assertEqual(owl.feed(veg), "Owl does not eat Vegetable!")
#         self.assertEqual(str(owl), "Owl [Pip, 10, 11.0, 4]")
#
#
# if __name__ == "__main__":
#     unittest.main()
