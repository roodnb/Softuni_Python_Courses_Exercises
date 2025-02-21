# from project.product import Product
# from project.food.dessert import Dessert
# from project.food.cake import Cake
# from project.food.food import Food
# from project.food.main_dish import MainDish
# from project.food.salmon import Salmon
# from project.food.soup import Soup
# from project.food.starter import Starter
# from project.beverage.beverage import Beverage
# from project.beverage.hot_beverage import HotBeverage
# from project.beverage.cold_beverage import ColdBeverage
# from project.beverage.tea import Tea
# from project.beverage.coffee import Coffee
#
#
# product = Product("coffee", 2.5)
# print(product.__class__.__name__)
# print(product.name)
# print(product.price)
# beverage = Beverage("coffee", 2.5, 50)
# print(beverage.__class__.__name__)
# print(beverage.__class__.__bases__[0].__name__)
# print(beverage.name)
# print(beverage.price)
# print(beverage.milliliters)
# soup = Soup("fish soup", 9.90, 230)
# print(soup.__class__.__name__)
# print(soup.__class__.__bases__[0].__name__)
# print(soup.name)
# print(soup.price)
# print(soup.grams)




# zero test
from project.product import Product
from project.beverage.beverage import Beverage
from project.food.soup import Soup
import unittest

class Tests(unittest.TestCase):
    def test(self):
        product = Product("coffee", 2.5)
        self.assertEqual(product.__class__.__name__, "Product")
        self.assertEqual(product.name, "coffee")
        self.assertEqual(product.price, 2.5)
        beverage = Beverage("coffee", 2.5, 50)
        self.assertEqual(beverage.__class__.__name__, "Beverage")
        self.assertEqual(beverage.__class__.__bases__[0].__name__, "Product")
        self.assertEqual(beverage.name, "coffee")
        self.assertEqual(beverage.price, 2.5)
        self.assertEqual(beverage.milliliters, 50)
        soup = Soup("fish soup", 9.90, 230)
        self.assertEqual(soup.__class__.__name__, "Soup")
        self.assertEqual(soup.__class__.__bases__[0].__name__, "Starter")
        self.assertEqual(soup.name, "fish soup")
        self.assertEqual(soup.price, 9.90)
        self.assertEqual(soup.grams, 230)

if __name__ == "__main__":
    unittest.main()

